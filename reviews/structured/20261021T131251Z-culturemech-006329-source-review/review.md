# Source and formulation review: alkaliphilic_spirochaete_medium (CultureMech:006329)

- Review: 20261021T131251Z-culturemech-006329-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:04:59Z
- Finished UTC: 2026-10-21T13:12:51Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 700 primary, provider and explicitly referenced DSMZ 141 stocks support a completed comparison. The record flattens vitamin/mineral stock quantities into the medium and combines NaCl contributions at incompatible scopes. Current mineral stock 241 differs from selected provider stock 5902; this is a documented source conflict without established chronology, not permission to silently replace either formulation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 219; batch 022 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-one task batches contain 210 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 213 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006329 | data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml | generated | alkaliphilic_spirochaete_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006329 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006329 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/219/strict.tsv |
| validate-terms | passed | True | CultureMech:006329 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006329 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006329 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo700detail | unavailable | False | CultureMech:006329 | Exact KOMODO 700 detail returned HTTP 403. The primary DSMZ 700 recipe, complete provider and exact catalog identity are available; this optional detail does not make the current comparison incomplete or resolve historical stock chronology. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006329.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006329.

46 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Na2CO3 main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 10 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 94.3503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "NaHCO3 main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 15 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 178.557,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "NaCl main-stage contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Preserve 10 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "NaCl 11 g/L is a sum of 10 main and 1 stock-stage g/L, which must be separated.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 171.116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "K2HPO4 main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 0.2 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "NH4Cl main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 1 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "KCl main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 0.2 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 2.68276,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Na2S x 9 H2O main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 1 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.16351,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Yeast extract main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 0.5 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Sucrose main-stage contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Preserve 5 g in the main source recipe with listed 1000 mL water and separate receiving doses.",
    "rationale": "The number matches the provider nominal g/L but has no attached amount evidence. Source mass plus water and stock doses does not independently establish measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sucrose\",\n                        \"compound_id\": 108,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 14.6071,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Biotin vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 2 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Folic acid vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 2 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Pyridoxine hydrochloride vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 10 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Thiamine HCl vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Riboflavin vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Nicotinic acid vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Calcium D-(+)-pantothenate vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0209846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Vitamin B12 vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.0001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 0.1 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "p-Aminobenzoic acid vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "(DL)-alpha-Lipoic acid vitamin stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate 10 mL receiving dose.",
    "rationale": "The current stock g/L is presented as a direct medium concentration. Retain original mg units and stage; do not treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly named, so D stereochemistry is supported here.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Nitrilotriacetic acid mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 1.5 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "MgSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 3 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "MnSO4 x H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.5 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "NaCl mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "11.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 1 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "FeSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.1 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "CoSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.18 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "CaCl2 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.1 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "ZnSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.18 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "CuSO4 x 5 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.01 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "AlK(SO4)2 x 12 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.02 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "H3BO3 mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.01 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Na2MoO4 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.01 g, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "NiCl2 x 6 H2O mineral stock",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.025 g, 1000 mL water and 1 mL receiving dose. Current 141/241 instead gives 0.03 g nickel hexahydrate; retain both alternatives pending exact source-version reconciliation.",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.192903,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      },
      {
        "source_key": "solution241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/241",
        "source_locator": "$.data.recipe[12]",
        "exact_source_quote": "{\n                \"recipe_order\": 13,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.03,\n                \"unit\": \"g\",\n                \"g_l\": 0.03,\n                \"mmol_l\": 0.231483,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d"
      },
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Page 2, named mineral subsection",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Na2SeO3 x 5 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore separate mineral stock stage: selected 5902 gives 0.3 mg, 1000 mL water and 1 mL receiving dose. ",
    "rationale": "Stock concentration was flattened into the medium; NaCl must remain a separate stock contribution. Nickel is additionally grounded to an anhydrous ontology entity despite explicit hexahydrate source wording; source amount/version and chemical form are distinct corrections.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Current named mineral stock tungstate discrepancy",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Current 141/241 lists 0.40 mg sodium tungstate dihydrate in the mineral stock; selected 5902 omits it. Preserve a source-version conflict rather than adding an unconditional medium component.",
    "rationale": "Exact complete recipe comparison establishes the discrepancy, not temporal order or which historical stock was imported.",
    "source_snippets": [
      {
        "source_key": "solution241",
        "source_url": "https://mediadive.dsmz.de/rest/solution/241",
        "source_locator": "$.data.recipe[14]",
        "exact_source_quote": "{\n                \"recipe_order\": 15,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.0004,\n                \"mmol_l\": 0.00121267,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d"
      },
      {
        "source_key": "dsmz141",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf",
        "source_locator": "Page 2, named mineral subsection",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Vitamin receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "10 ml in the exact named source stage.",
    "rationale": "This source volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition do not prove a measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Wolin's vitamin solution\",\n                        \"solution_id\": 242,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Mineral receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1 ml in the exact named source stage.",
    "rationale": "This source volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition do not prove a measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Modified Wolin's mineral solution II\",\n                        \"solution_id\": 5902,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 ml in the exact named source stage.",
    "rationale": "This source volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition do not prove a measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Vitamin stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 ml in the exact named source stage.",
    "rationale": "This source volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition do not prove a measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Mineral stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 ml in the exact named source stage.",
    "rationale": "This source volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition do not prove a measured final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive700api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/700",
        "source_locator": "$.data.solutions[2].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Main NaOH adjustment strength",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "6 N NaOH reagent for the stated main pH adjustment; not 6 N final-medium hydroxide.",
    "rationale": "A generic VARIABLE entry loses the explicit reagent strength and stage. Do not convert normality into a final concentration or claim a fixed addition volume.",
    "source_snippets": [
      {
        "source_key": "dsmz700",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf",
        "source_locator": "Page 1, preparation",
        "exact_source_quote": "to 9.7 with 6N NaOH (about 15 ml).",
        "snapshot_sha256": "dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f",
        "parsed_text_sha256": "103061987b1ffc16dbde76c553d4c3ac9a1eded8fde516ebec3513a84c951b20"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Approximate NaOH addition",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "About 15 mL of the named 6 N NaOH reagent, with the approximate qualifier and pH endpoint retained.",
    "rationale": "No local procedure preserves this source quantity; it is an approximate adjustment amount, not a measured final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz700",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf",
        "source_locator": "Page 1, preparation",
        "exact_source_quote": "to 9.7 with 6N NaOH (about 15 ml).",
        "snapshot_sha256": "dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f",
        "parsed_text_sha256": "103061987b1ffc16dbde76c553d4c3ac9a1eded8fde516ebec3513a84c951b20"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "Main pH endpoint",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 9.7,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.7,
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "pH 9.7 at the documented adjustment stage.",
    "rationale": "The scalar matches the source but lacks attached evidence and its preparation context.",
    "source_snippets": [
      {
        "source_key": "dsmz700",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf",
        "source_locator": "Page 1, preparation",
        "exact_source_quote": "to 9.7 with 6N NaOH (about 15 ml).",
        "snapshot_sha256": "dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f",
        "parsed_text_sha256": "103061987b1ffc16dbde76c553d4c3ac9a1eded8fde516ebec3513a84c951b20"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "Mineral initial pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Dissolve NTA first, then pH 6.5 with KOH before other minerals.",
    "rationale": "This is the named mineral stock procedure, not the main pH. Both selected and current named mineral stocks retain this sequence.",
    "source_snippets": [
      {
        "source_key": "solution5902",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5902",
        "source_locator": "$.data.steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Mineral final pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "After mineral addition, adjust the stock to pH 7.0 with KOH.",
    "rationale": "This is the named mineral stock procedure, not the main pH. Both selected and current named mineral stocks retain this sequence.",
    "source_snippets": [
      {
        "source_key": "solution5902",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5902",
        "source_locator": "$.data.steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270"
      }
    ]
  },
  {
    "quantity_id": "q45",
    "component_or_context": "Mineral KOH dose",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "KOH amount and strength are not quantified; preserve the two stock pH endpoints without inventing a dose.",
    "rationale": "The source names an adjustment reagent but supplies no fixed mass, concentration or volume.",
    "source_snippets": [
      {
        "source_key": "solution5902",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5902",
        "source_locator": "$.data.steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270"
      }
    ]
  },
  {
    "quantity_id": "q46",
    "component_or_context": "Provider vitamin filtration context",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Provider stock 242 specifies a 0.22 µm filter. Attach as provider stock-specific procedure, separately from the primary 700 instruction to use sterile stocks.",
    "rationale": "This quantitative detail comes from the exact selected provider stock; do not present it as verbatim primary 700 or transfer parent 141 main-medium conditions.",
    "source_snippets": [
      {
        "source_key": "solution242",
        "source_url": "https://mediadive.dsmz.de/rest/solution/242",
        "source_locator": "$.data.steps[0].step; parsed JSON text",
        "exact_source_quote": "Filtrate (pore size 0.22 µm to sterilize).",
        "snapshot_sha256": "4e58a59546c43de94390f51434fabda2699f6914cabef073a405d81d8fc8b4f6",
        "parsed_text_sha256": "4478d1d45be0b313e7da87e1ea90feb05959800faeec154edfd839fe7269eed5"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:006329.

32 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 32/33 primary and 31/33 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 33: primary 96.97%; secondary 93.94%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source accession and maintained ownership

identity: supported. Targets: CultureMech:006329.

CM006329 resolves exactly to the maintained KOMODO 700 contributor and DSMZ 700 provenance. No distinct local relationship claims require repair. Both current source versions are explicitly compared, with no inferred publication or import chronology.

### Claim-level amount support and source scope

evidence: concern. Targets: CultureMech:006329.

The local layers have import provenance but no attached amount evidence. The inventory covers every local concentration and scoped source-only quantity using literal excerpts, exact source locators, units, stages and original capture hashes. Provider-declared volume is kept separate from measured assembled final volume.

### Preparation stages, source-only additions and owner differences

completeness: concern. Targets: CultureMech:006329.

Both local layers omit preparation_steps. Preserve the source nitrogen preparation, initial omissions, boil/cool sequence, bicarbonate/carbonate addition, 6 N NaOH pH adjustment and approximate volume, autoclaving, then neutralized sulfide/vitamins/sucrose from sterile stocks. Stock NTA/KOH sequence and provider-only vitamin filtration remain in their own stocks. No temperature or duration is specified by the main primary source.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:006329.

Yeast extract supports COMPLEX/UNDEFINED and the source has no mandatory gelling agent, consistent with LIQUID. Aerobic: Yes from KOMODO is not a growth result and does not negate the primary preparation under nitrogen.

### Supplied forms and chemical specificity

grounding: concern. Targets: CultureMech:006329.

Nickel hexahydrate in both stock versions conflicts with CHEBI:34887 nickel dichloride, whose formula Cl2Ni lacks hydration water. Exact label resolution does not validate supplied-form grounding. Calcium D-(+)-pantothenate is explicitly supported; no DL-to-D conflict applies. Generic vitamin B12 and biotin source wording does not resolve every possible supplied form, so no speculative replacement is proposed.

### Growth, organism taxonomy and graph claims

scope: not_applicable. Targets: CultureMech:006329.

The title, generic Microbial cultivation application and catalog Aerobic flags are not experimental growth or taxonomy evidence. No growth assertions, current taxonomy IDs or graph membership are added. Explicit source strain qualifiers remain formulation scope only.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006329.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Authoritative inputs and current writer scope

provenance: concern. Targets: CultureMech:006329.

Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction.

## Findings

### f1: Vitamin and mineral stocks are flattened and NaCl contributions summed

blocker / open / confirmed; issue key: flattened-stocks.

Vitamin and mineral concentrations are incorrectly direct medium quantities. NaCl 11 G_PER_L combines a main contribution of 10 with a stock contribution of 1 without the 1 mL receiving dose. Source water and stock descriptors are omitted.

### f2: Selected mineral II stock differs from current referenced mineral stock

major / open / confirmed; issue key: mineral-version-conflict.

The provider selects 5902 with 0.025 g nickel hexahydrate and no tungstate; the primary 700 cross-reference currently resolves to 141/241 with 0.03 g nickel hexahydrate and 0.40 mg tungstate. Available captures do not establish historical correspondence or chronology.

### f3: Anhydrous nickel identifier conflicts with explicit hexahydrate

major / open / confirmed; issue key: nickel-hydrate-grounding.

ingredients[30] names NiCl2 x 6 H2O but both primary and secondary CHEBI assertions use CHEBI:34887, anhydrous nickel dichloride. Both candidate stock sources explicitly name the hexahydrate.

### f4: Source preparation and stock stages are absent

major / open / confirmed; issue key: missing-preparation.

The record retains only a pH scalar and variable NaOH ingredient, omitting the complete main sequence and stock-specific procedures. The missing stage context affects the interpretation of the amounts.

### f5: Historical timestamp strings remain malformed or timezone-naive

minor / open / confirmed; issue key: historical-timestamp-shape.

The target and KOMODO owner each retain one malformed import timestamp and one timezone-naive resolver timestamp. These do not validate source chronology and should not be silently rewritten.

## Recommended Actions And Acceptance Checks

### a1

Correct the exact maintained KOMODO owner: restore separate main, vitamin and mineral stages, receiving doses and original water units; remove incompatible NaCl summation and double counting. Preserve nominal provider volume versus unestablished measured final volume. Attach every amount to its literal source scope before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Represent the exact alternatives and seek version-specific evidence before choosing a canonical stock; do not silently substitute current 241 for selected 5902 or infer a chronology. Keep all shared stock rows and dose basis separate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Re-ground the exact supplied hexahydrate in the maintained owner after separately validating its ontology and secondary correspondence. Preserve source hydration, stock amount and unresolved source-version alternatives; do not infer an unverified replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Restore exact source-scoped preparation and its qualifiers in the owner; include approximate NaOH dose/strength, distinct stock pH sequence and provenance-qualified provider filtration. Do not transfer the parent 141 medium recipe, gas ratios, pressure or organism-specific conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve original history and append a clarification identifying the literal timestamp defects and known provenance limits when the owner is curated; do not fabricate historical times or source chronology.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch022/219/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/219/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml:1:id: CultureMech:006329<br>./data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml:1:id: CultureMech:006329<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/219/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 40 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/219/evidence-context-original.json; Complete frozen target/owners, source stages, exact secondary lookup and ignored-inclusive relationships | context_only | Full captured records re-read and compared by exact equality with fresh inspected records. Context is supporting provenance; exact bound primary/provider captures independently support scientific claims. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf; Page 1: main table and complete preparation | supports | The main source identifies nine direct components, vitamin and mineral receiving doses, water, staged nitrogen preparation, and pH adjustment with an approximate reagent volume. |
| provider | https://mediadive.dsmz.de/rest/medium/700; data.medium and solutions 1451/242/5902, full recipes and steps | supports | The provider preserves main-stage masses, nominal 1000 mL denominator, 10 mL vitamin and 1 mL mineral doses, and separate stocks. |
| referenced-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Pages 2–3: Modified Wolin mineral and Wolin vitamin subsections ONLY | supports | Only the two explicitly referenced stock subsections are compared. The parent medium, its conditions and strain-specific alternatives are excluded. The current mineral subsection contains 0.03 g nickel hexahydrate and 0.40 mg tungstate; provider stock 5902 has 0.025 g nickel hexahydrate and no tungstate row. |
| solution241 | https://mediadive.dsmz.de/rest/solution/241; data.id/name/volume/recipe/steps | supports | Exact endpoint identity and complete stock-stage quantities are retained. Stock 5902 is selected by this medium; current named stock 241 is a distinct comparison, not an established historical replacement. |
| solution242 | https://mediadive.dsmz.de/rest/solution/242; data.id/name/volume/recipe/steps | supports | Exact endpoint identity and complete stock-stage quantities are retained. Stock 5902 is selected by this medium; current named stock 241 is a distinct comparison, not an established historical replacement. |
| solution5902 | https://mediadive.dsmz.de/rest/solution/5902; data.id/name/volume/recipe/steps | supports | Exact endpoint identity and complete stock-stage quantities are retained. Stock 5902 is selected by this medium; current named stock 241 is a distinct comparison, not an established historical replacement. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact table row 700 | supports | Exact KOMODO accession maps to DSMZ 700; catalog Aerobic: Yes is retained as provenance only. |
| komodo700detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=700; Preserved exact public retrieval result | context_only | Exact KOMODO 700 detail returned HTTP 403. The primary DSMZ 700 recipe, complete provider and exact catalog identity are available; this optional detail does not make the current comparison incomplete or resolve historical stock chronology. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch022/219/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17992 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17992 resolves to sucrose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17992": [{"label": "Sucrose", "match_type": "preferred_term", "identifier": "CHEBI:17992", "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 12, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.460859"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.460859"}]}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact KOMODO 700 detail returned HTTP 403. The primary DSMZ 700 recipe, complete provider and exact catalog identity are available; this optional detail does not make the current comparison incomplete or resolve historical stock chronology.
- Only exact per-record bound captures are used. Current collection and provider differences do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently establish a measured final mixture volume. No density, percent basis, exact hydration, default sterilization cycle or stock volume is invented.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131251Z-culturemech-006329-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilic_spirochaete_medium (CultureMech:006329)'
started_at: '2026-10-21T13:04:59Z'
finished_at: '2026-10-21T13:12:51Z'
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
summary: The exact DSMZ 700 primary, provider and explicitly referenced DSMZ 141 stocks
  support a completed comparison. The record flattens vitamin/mineral stock quantities
  into the medium and combines NaCl contributions at incompatible scopes. Current
  mineral stock 241 differs from selected provider stock 5902; this is a documented
  source conflict without established chronology, not permission to silently replace
  either formulation.
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
  - path: data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
    sha256: f7e6b98df0b44958b90ad244486e6db211bb109d199eaa1e3da8e2d2623b5f39
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
    sha256: 8d5a40b6bc88554aaf0c566627d05d951995d0da8d115b32c140f1df0667bf30
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
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
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
  selection: Task review 219; batch 022 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-one task batches
    contain 210 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 213 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006329
targets:
- target_id: CultureMech:006329
  path: data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  label: alkaliphilic_spirochaete_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/219/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/219/strict.tsv"
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006329
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
  - CultureMech:006329
- check_id: komodo700detail-source-access
  name: 'Exact source content access: komodo700detail'
  required: false
  status: unavailable
  summary: Exact KOMODO 700 detail returned HTTP 403. The primary DSMZ 700 recipe,
    complete provider and exact catalog identity are available; this optional detail
    does not make the current comparison incomplete or resolve historical stock chronology.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - komodo700detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:28.789402Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/219/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:32.443866Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/219/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:34.709697Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:35.929957Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:12:50Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml:1:id: CultureMech:006329

    ./data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml:1:id:
    CultureMech:006329

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/219/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:12:50Z'
  support: supports
  summary: 40 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e6db84acd3141c66be3f891341b89222291e3483a408d7081d8d2f18b5369b80
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/219/evidence-context-original.json
  locator: Complete frozen target/owners, source stages, exact secondary lookup and
    ignored-inclusive relationships
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Full captured records re-read and compared by exact equality with fresh
    inspected records. Context is supporting provenance; exact bound primary/provider
    captures independently support scientific claims.
  snapshot_sha256: a8bbe1317a024113f60bcfe703e6d5b82815818af2a8de2bffc2c1674bad77d1
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf
  locator: 'Page 1: main table and complete preparation'
  accessed_at: '2026-10-21T12:48:26.091581Z'
  support: supports
  summary: The main source identifies nine direct components, vitamin and mineral
    receiving doses, water, staged nitrogen preparation, and pH adjustment with an
    approximate reagent volume.
  snapshot_sha256: dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/700
  locator: data.medium and solutions 1451/242/5902, full recipes and steps
  accessed_at: '2026-10-21T12:48:25.152582Z'
  support: supports
  summary: The provider preserves main-stage masses, nominal 1000 mL denominator,
    10 mL vitamin and 1 mL mineral doses, and separate stocks.
  snapshot_sha256: b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575
- evidence_id: referenced-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: 'Pages 2–3: Modified Wolin mineral and Wolin vitamin subsections ONLY'
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: Only the two explicitly referenced stock subsections are compared. The
    parent medium, its conditions and strain-specific alternatives are excluded. The
    current mineral subsection contains 0.03 g nickel hexahydrate and 0.40 mg tungstate;
    provider stock 5902 has 0.025 g nickel hexahydrate and no tungstate row.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: solution241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T10:37:16.846684Z'
  support: supports
  summary: Exact endpoint identity and complete stock-stage quantities are retained.
    Stock 5902 is selected by this medium; current named stock 241 is a distinct comparison,
    not an established historical replacement.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: solution242
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/242
  locator: data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T12:01:14.832446Z'
  support: supports
  summary: Exact endpoint identity and complete stock-stage quantities are retained.
    Stock 5902 is selected by this medium; current named stock 241 is a distinct comparison,
    not an established historical replacement.
  snapshot_sha256: 4e58a59546c43de94390f51434fabda2699f6914cabef073a405d81d8fc8b4f6
- evidence_id: solution5902
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5902
  locator: data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T12:49:29.674664Z'
  support: supports
  summary: Exact endpoint identity and complete stock-stage quantities are retained.
    Stock 5902 is selected by this medium; current named stock 241 is a distinct comparison,
    not an established historical replacement.
  snapshot_sha256: 6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact table row 700
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: 'Exact KOMODO accession maps to DSMZ 700; catalog Aerobic: Yes is retained
    as provenance only.'
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo700detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=700
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:48:24.885027Z'
  support: context_only
  summary: Exact KOMODO 700 detail returned HTTP 403. The primary DSMZ 700 recipe,
    complete provider and exact catalog identity are available; this optional detail
    does not make the current comparison incomplete or resolve historical stock chronology.
  snapshot_sha256: 9679f09b48462e567b571c532b8d5705c7a732e28084147859b7f99315028e9b
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/219/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ffa47393049aad0ecacf3c1d52441c697a530d5f6ed73ed68cb573614204bf98
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
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: CHEBI:15940 resolves to nicotinic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
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
- evidence_id: chebi17992
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17992
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:31.913996Z'
  support: supports
  summary: CHEBI:17992 resolves to sucrose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 509f9cbc014a0211d3a8e536a2c68048a090719ce68ee80550c8bbf532f150aa
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
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: CHEBI:27470 resolves to folic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
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
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
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
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
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
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
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
  accessed_at: '2026-10-20T06:55:07.038393Z'
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
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
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
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:12:50Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940":
    [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940",
    "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494":
    [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label":
    "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17992":
    [{"label": "Sucrose", "match_type": "preferred_term", "identifier": "CHEBI:17992",
    "preferred_term": "Sucrose", "ontology_id": "CHEBI:17992", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic
    acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type":
    "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier":
    "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label":
    "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term":
    "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity":
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
    "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105":
    [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105",
    "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status":
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
    "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label":
    "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465",
    "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: '[{"input": "target", "events": 12, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:04.460859"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml",
    "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:04.460859"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Current MediaDive code distinguishes stock additions and solutions, preserves
    preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge
    ownership and current cleanup were inspected; current cleanup does not reproduce
    the historical disagreeing-duplicate sums. Current code is context, not proof
    of a particular historical execution. Correct every exact normalized contributor,
    attach claim-scoped evidence and append provenance clarification; regenerate derived
    products only after separately authorized correction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Current MediaDive code distinguishes stock additions and solutions, preserves
    preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge
    ownership and current cleanup were inspected; current cleanup does not reproduce
    the historical disagreeing-duplicate sums. Current code is context, not proof
    of a particular historical execution. Correct every exact normalized contributor,
    attach claim-scoped evidence and append provenance clarification; regenerate derived
    products only after separately authorized correction.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Current MediaDive code distinguishes stock additions and solutions, preserves
    preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge
    ownership and current cleanup were inspected; current cleanup does not reproduce
    the historical disagreeing-duplicate sums. Current code is context, not proof
    of a particular historical execution. Correct every exact normalized contributor,
    attach claim-scoped evidence and append provenance clarification; regenerate derived
    products only after separately authorized correction.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:12:50Z'
  support: context_only
  summary: Current MediaDive code distinguishes stock additions and solutions, preserves
    preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge
    ownership and current cleanup were inspected; current cleanup does not reproduce
    the historical disagreeing-duplicate sums. Current code is context, not proof
    of a particular historical execution. Correct every exact normalized contributor,
    attach claim-scoped evidence and append provenance clarification; regenerate derived
    products only after separately authorized correction.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 46 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Na2CO3 main-stage contribution\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 10 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 94.3503,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"NaHCO3 main-stage contribution\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 15 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NaHCO3\\\",\\n                        \\\"compound_id\\\": 55,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 178.557,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"NaCl main-stage contribution\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 10 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"NaCl 11 g/L is a sum of 10 main and\
    \ 1 stock-stage g/L, which must be separated.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 171.116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"K2HPO4 main-stage contribution\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 0.2 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                \
    \        \\\"mmol_l\\\": 1.14826,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"NH4Cl main-stage contribution\",\n    \"decision\": \"evidence_only\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 1 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 18.6951,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"KCl main-stage contribution\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 0.2 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                \
    \        \\\"mmol_l\\\": 2.68276,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Na2S x 9 H2O main-stage contribution\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 1 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"mmol_l\\\": 4.16351,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Yeast extract main-stage contribution\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 0.5 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \   \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Sucrose main-stage contribution\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Preserve 5 g in the main source recipe with listed 1000 mL water and separate\
    \ receiving doses.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ g/L but has no attached amount evidence. Source mass plus water and stock doses\
    \ does not independently establish measured final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Sucrose\\\",\\n                        \\\"compound_id\\\":\
    \ 108,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n      \
    \                  \\\"mmol_l\\\": 14.6071,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Biotin vitamin stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 2 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n             \
    \           \\\"mmol_l\\\": 0.00818632,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Folic acid vitamin stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 2 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Folic acid\\\",\\n                        \\\"compound_id\\\"\
    : 138,\\n                        \\\"amount\\\": 2,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n \
    \                       \\\"mmol_l\\\": 0.00453104,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Pyridoxine hydrochloride vitamin stock\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 10 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                        \\\"\
    compound_id\\\": 519,\\n                        \\\"amount\\\": 10,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.01,\\n                        \\\"mmol_l\\\": 0.0486287,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Thiamine HCl vitamin stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Thiamine HCl\\\",\\n                        \\\"compound_id\\\
    \": 1207,\\n                        \\\"amount\\\": 5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0148236,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Riboflavin vitamin stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Riboflavin\\\",\\n                        \\\"compound_id\\\"\
    : 136,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n \
    \                       \\\"mmol_l\\\": 0.0132837,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Nicotinic acid vitamin stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"compound_id\\\
    \": 139,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0406141,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Calcium D-(+)-pantothenate vitamin stock\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Calcium D-(+)-pantothenate\\\",\\n                        \\\
    \"compound_id\\\": 1512,\\n                        \\\"amount\\\": 5,\\n     \
    \                   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.005,\\n                        \\\"mmol_l\\\": 0.0209846,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Vitamin B12 vitamin stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0001\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 0.1 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0001,\\\
    n                        \\\"mmol_l\\\": 7.3779e-5,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"p-Aminobenzoic acid vitamin stock\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                        \\\"compound_id\\\
    \": 47,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n\
    \                        \\\"mmol_l\\\": 0.0364591,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"(DL)-alpha-Lipoic acid vitamin stock\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 5 mg in Wolin vitamin stock 242, with source water 1000 mL and separate\
    \ 10 mL receiving dose.\",\n    \"rationale\": \"The current stock g/L is presented\
    \ as a direct medium concentration. Retain original mg units and stage; do not\
    \ treat it as a final-medium concentration. Calcium D-(+)-pantothenate is explicitly\
    \ named, so D stereochemistry is supported here.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"(DL)-alpha-Lipoic acid\\\",\\n                        \\\"\
    compound_id\\\": 252,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.005,\\n                        \\\"mmol_l\\\": 0.024233,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Nitrilotriacetic acid mineral stock\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 1.5 g, 1000 mL water\
    \ and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration was flattened\
    \ into the medium; NaCl must remain a separate stock contribution. Nickel is additionally\
    \ grounded to an anhydrous ontology entity despite explicit hexahydrate source\
    \ wording; source amount/version and chemical form are distinct corrections.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive700api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\",\n  \
    \      \"source_locator\": \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                   \
    \     \\\"compound_id\\\": 189,\\n                        \\\"amount\\\": 1.5,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 1.5,\\n                        \\\"mmol_l\\\": 7.84765,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"MgSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 3 g, 1000 mL water\
    \ and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration was flattened\
    \ into the medium; NaCl must remain a separate stock contribution. Nickel is additionally\
    \ grounded to an anhydrous ontology entity despite explicit hexahydrate source\
    \ wording; source amount/version and chemical form are distinct corrections.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive700api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\",\n  \
    \      \"source_locator\": \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 3,\\n          \
    \              \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 3,\\n                        \\\"mmol_l\\\": 12.1716,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"MnSO4 x H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.5 g, 1000 mL water\
    \ and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration was flattened\
    \ into the medium; NaCl must remain a separate stock contribution. Nickel is additionally\
    \ grounded to an anhydrous ontology entity despite explicit hexahydrate source\
    \ wording; source amount/version and chemical form are distinct corrections.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive700api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\",\n  \
    \      \"source_locator\": \"$.data.solutions[2].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 2.9583,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"NaCl mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"11.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 1 g, 1000 mL water\
    \ and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration was flattened\
    \ into the medium; NaCl must remain a separate stock contribution. Nickel is additionally\
    \ grounded to an anhydrous ontology entity despite explicit hexahydrate source\
    \ wording; source amount/version and chemical form are distinct corrections.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive700api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\",\n  \
    \      \"source_locator\": \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"FeSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.1 g, 1000 mL water\
    \ and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration was flattened\
    \ into the medium; NaCl must remain a separate stock contribution. Nickel is additionally\
    \ grounded to an anhydrous ontology entity despite explicit hexahydrate source\
    \ wording; source amount/version and chemical form are distinct corrections.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive700api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\",\n  \
    \      \"source_locator\": \"$.data.solutions[2].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 12,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.359693,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"CoSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.18 g, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"CoSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 198,\\n                        \\\"amount\\\
    \": 0.18,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.18,\\n                        \\\"mmol_l\\\": 1.16132,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.1 g, 1000 mL water\
    \ and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration was flattened\
    \ into the medium; NaCl must remain a separate stock contribution. Nickel is additionally\
    \ grounded to an anhydrous ontology entity despite explicit hexahydrate source\
    \ wording; source amount/version and chemical form are distinct corrections.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive700api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\",\n  \
    \      \"source_locator\": \"$.data.solutions[2].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.1,\\n                        \\\"mmol_l\\\": 0.680203,\\n                \
    \        \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"ZnSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.18 g, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 35,\\n                        \\\"amount\\\
    \": 0.18,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.18,\\n                        \\\"mmol_l\\\": 0.625954,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"CuSO4 x 5 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.01 g, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 121,\\n                        \\\"amount\\\
    \": 0.01,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.0400503,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"AlK(SO4)2 x 12 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.02 g, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n    \
    \                    \\\"compound_id\\\": 908,\\n                        \\\"\
    amount\\\": 0.02,\\n                        \\\"unit\\\": \\\"g\\\",\\n      \
    \                  \\\"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\"\
    : 0.0421596,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"H3BO3 mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.01 g, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"compound\\\": \\\"H3BO3\\\",\\n                 \
    \       \\\"compound_id\\\": 37,\\n                        \\\"amount\\\": 0.01,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.161708,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Na2MoO4 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.01 g, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[11]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 12,\\\
    n                        \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 9,\\n                        \\\"amount\\\
    \": 0.01,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.0413309,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"NiCl2 x 6 H2O mineral stock\",\n    \"decision\": \"conflict\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.025 g, 1000 mL\
    \ water and 1 mL receiving dose. Current 141/241 instead gives 0.03 g nickel hexahydrate;\
    \ retain both alternatives pending exact source-version reconciliation.\",\n \
    \   \"rationale\": \"Stock concentration was flattened into the medium; NaCl must\
    \ remain a separate stock contribution. Nickel is additionally grounded to an\
    \ anhydrous ontology entity despite explicit hexahydrate source wording; source\
    \ amount/version and chemical form are distinct corrections.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\":\
    \ \"$.data.solutions[2].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 0.025,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.025,\\\
    n                        \\\"mmol_l\\\": 0.192903,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\n      },\n\
    \      {\n        \"source_key\": \"solution241\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/solution/241\",\n        \"source_locator\": \"\
    $.data.recipe[12]\",\n        \"exact_source_quote\": \"{\\n                \\\
    \"recipe_order\\\": 13,\\n                \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\
    \",\\n                \\\"compound_id\\\": 40,\\n                \\\"solution\\\
    \": null,\\n                \\\"solution_id\\\": null,\\n                \\\"\
    condition\\\": null,\\n                \\\"attribute\\\": null,\\n           \
    \     \\\"amount\\\": 0.03,\\n                \\\"unit\\\": \\\"g\\\",\\n    \
    \            \\\"g_l\\\": 0.03,\\n                \\\"mmol_l\\\": 0.231483,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz141\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\",\n        \"\
    source_locator\": \"Page 2, named mineral subsection\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 0.03 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Na2SeO3 x 5 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore separate mineral stock stage: selected 5902 gives 0.3 mg, 1000 mL\
    \ water and 1 mL receiving dose. \",\n    \"rationale\": \"Stock concentration\
    \ was flattened into the medium; NaCl must remain a separate stock contribution.\
    \ Nickel is additionally grounded to an anhydrous ontology entity despite explicit\
    \ hexahydrate source wording; source amount/version and chemical form are distinct\
    \ corrections.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive700api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/700\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[13]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 14,\\\
    n                        \\\"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 107,\\n                        \\\"amount\\\
    \": 0.3,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.0003,\\n                        \\\"mmol_l\\\": 0.00114062,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Current named mineral stock tungstate discrepancy\",\n    \"decision\": \"\
    conflict\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Current 141/241 lists 0.40 mg sodium tungstate dihydrate in the mineral stock;\
    \ selected 5902 omits it. Preserve a source-version conflict rather than adding\
    \ an unconditional medium component.\",\n    \"rationale\": \"Exact complete recipe\
    \ comparison establishes the discrepancy, not temporal order or which historical\
    \ stock was imported.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution241\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/241\"\
    ,\n        \"source_locator\": \"$.data.recipe[14]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 15,\\n                \\\"compound\\\
    \": \\\"Na2WO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 249,\\n   \
    \             \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 0.4,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.0004,\\n                \\\"mmol_l\\\
    \": 0.00121267,\\n                \\\"optional\\\": 0\\n            }\",\n   \
    \     \"snapshot_sha256\": \"50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d\"\
    \n      },\n      {\n        \"source_key\": \"dsmz141\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\",\n    \
    \    \"source_locator\": \"Page 2, named mineral subsection\",\n        \"exact_source_quote\"\
    : \"Na2WO4 x 2 H2O 0.40 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Vitamin receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"10 ml in the exact named source stage.\",\n    \"rationale\": \"This source\
    \ volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral\
    \ dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition\
    \ do not prove a measured final volume.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\": \"$.data.solutions[0].recipe[9]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 10,\\n                        \\\"solution\\\": \\\"Wolin's vitamin solution\\\
    \",\\n                        \\\"solution_id\\\": 242,\\n                   \
    \     \\\"amount\\\": 10,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Mineral receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1 ml in the exact named source stage.\",\n    \"rationale\": \"This source\
    \ volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral\
    \ dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition\
    \ do not prove a measured final volume.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\": \"$.data.solutions[0].recipe[10]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 11,\\n                        \\\"solution\\\": \\\"Modified Wolin's mineral\
    \ solution II\\\",\\n                        \\\"solution_id\\\": 5902,\\n   \
    \                     \\\"amount\\\": 1,\\n                        \\\"unit\\\"\
    : \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n               \
    \     }\",\n        \"snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 ml in the exact named source stage.\",\n    \"rationale\": \"This source\
    \ volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral\
    \ dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition\
    \ do not prove a measured final volume.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\": \"$.data.solutions[0].recipe[11]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 12,\\n                        \\\"compound\\\": \\\"Distilled water\\\",\\\
    n                        \\\"compound_id\\\": 4,\\n                        \\\"\
    amount\\\": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"Vitamin stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 ml in the exact named source stage.\",\n    \"rationale\": \"This source\
    \ volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral\
    \ dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition\
    \ do not prove a measured final volume.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\": \"$.data.solutions[1].recipe[10]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 11,\\n                        \\\"compound\\\": \\\"Distilled water\\\",\\\
    n                        \\\"compound_id\\\": 4,\\n                        \\\"\
    amount\\\": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Mineral stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 ml in the exact named source stage.\",\n    \"rationale\": \"This source\
    \ volume is omitted locally. Keep main water 1000 mL, vitamin dose 10 mL and mineral\
    \ dose 1 mL separate; their literal sum 1011 mL and the approximate NaOH addition\
    \ do not prove a measured final volume.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive700api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/700\",\n        \"source_locator\": \"$.data.solutions[2].recipe[14]\"\
    ,\n        \"exact_source_quote\": \"{\\n                        \\\"recipe_order\\\
    \": 16,\\n                        \\\"compound\\\": \\\"Distilled water\\\",\\\
    n                        \\\"compound_id\\\": 4,\\n                        \\\"\
    amount\\\": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"b7ab7457473b4d44ce94720cb6f292b682ce054fb5ad03b657523451e71cb575\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Main NaOH adjustment strength\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"6 N NaOH reagent for the stated main pH adjustment; not 6 N final-medium hydroxide.\"\
    ,\n    \"rationale\": \"A generic VARIABLE entry loses the explicit reagent strength\
    \ and stage. Do not convert normality into a final concentration or claim a fixed\
    \ addition volume.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz700\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf\"\
    ,\n        \"source_locator\": \"Page 1, preparation\",\n        \"exact_source_quote\"\
    : \"to 9.7 with 6N NaOH (about 15 ml).\",\n        \"snapshot_sha256\": \"dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f\"\
    ,\n        \"parsed_text_sha256\": \"103061987b1ffc16dbde76c553d4c3ac9a1eded8fde516ebec3513a84c951b20\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"Approximate NaOH addition\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"About 15 mL of the named 6 N NaOH reagent, with the approximate qualifier\
    \ and pH endpoint retained.\",\n    \"rationale\": \"No local procedure preserves\
    \ this source quantity; it is an approximate adjustment amount, not a measured\
    \ final volume.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz700\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf\"\
    ,\n        \"source_locator\": \"Page 1, preparation\",\n        \"exact_source_quote\"\
    : \"to 9.7 with 6N NaOH (about 15 ml).\",\n        \"snapshot_sha256\": \"dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f\"\
    ,\n        \"parsed_text_sha256\": \"103061987b1ffc16dbde76c553d4c3ac9a1eded8fde516ebec3513a84c951b20\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"Main pH endpoint\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.7,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.7,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"pH 9.7 at the documented adjustment stage.\",\n    \"rationale\": \"The scalar\
    \ matches the source but lacks attached evidence and its preparation context.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz700\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium700.pdf\"\
    ,\n        \"source_locator\": \"Page 1, preparation\",\n        \"exact_source_quote\"\
    : \"to 9.7 with 6N NaOH (about 15 ml).\",\n        \"snapshot_sha256\": \"dee469358f5e6c0d297c0160b1a8fdad51cf81f47512b9ed17df96594ac6955f\"\
    ,\n        \"parsed_text_sha256\": \"103061987b1ffc16dbde76c553d4c3ac9a1eded8fde516ebec3513a84c951b20\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"Mineral initial pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Dissolve NTA first, then pH 6.5 with KOH before other minerals.\",\n    \"\
    rationale\": \"This is the named mineral stock procedure, not the main pH. Both\
    \ selected and current named mineral stocks retain this sequence.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5902\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5902\",\n        \"source_locator\"\
    : \"$.data.steps[0].step\",\n        \"exact_source_quote\": \"First dissolve\
    \ nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\
    \ final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Mineral final pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"After mineral addition, adjust the stock to pH 7.0 with KOH.\",\n    \"rationale\"\
    : \"This is the named mineral stock procedure, not the main pH. Both selected\
    \ and current named mineral stocks retain this sequence.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5902\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5902\",\n        \"source_locator\"\
    : \"$.data.steps[0].step\",\n        \"exact_source_quote\": \"First dissolve\
    \ nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\
    \ final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\"\
    : \"Mineral KOH dose\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"KOH amount and strength are not quantified; preserve the two stock pH endpoints\
    \ without inventing a dose.\",\n    \"rationale\": \"The source names an adjustment\
    \ reagent but supplies no fixed mass, concentration or volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution5902\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/5902\",\n        \"source_locator\"\
    : \"$.data.steps[0].step\",\n        \"exact_source_quote\": \"First dissolve\
    \ nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust\
    \ final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"component_or_context\"\
    : \"Provider vitamin filtration context\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_SPIROCHAETE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Provider stock 242 specifies a 0.22 µm filter. Attach as provider stock-specific\
    \ procedure, separately from the primary 700 instruction to use sterile stocks.\"\
    ,\n    \"rationale\": \"This quantitative detail comes from the exact selected\
    \ provider stock; do not present it as verbatim primary 700 or transfer parent\
    \ 141 main-medium conditions.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"solution242\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/242\"\
    ,\n        \"source_locator\": \"$.data.steps[0].step; parsed JSON text\",\n \
    \       \"exact_source_quote\": \"Filtrate (pore size 0.22 µm to sterilize).\"\
    ,\n        \"snapshot_sha256\": \"4e58a59546c43de94390f51434fabda2699f6914cabef073a405d81d8fc8b4f6\"\
    ,\n        \"parsed_text_sha256\": \"4478d1d45be0b313e7da87e1ea90feb05959800faeec154edfd839fe7269eed5\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '32 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 32/33 primary and 31/33 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi131527
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi17992
  - chebi26710
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32145
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi49105
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86364
  - chebi86465
  - chebi91244
  details: 'Instance coverage on a 0–100 percent scale, denominator 33: primary 96.97%;
    secondary 93.94%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Source accession and maintained ownership
  outcome: supported
  summary: CM006329 resolves exactly to the maintained KOMODO 700 contributor and
    DSMZ 700 provenance. No distinct local relationship claims require repair. Both
    current source versions are explicitly compared, with no inferred publication
    or import chronology.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution242
  - solution5902
- assessment_id: evidence
  area: evidence
  topic: Claim-level amount support and source scope
  outcome: concern
  summary: The local layers have import provenance but no attached amount evidence.
    The inventory covers every local concentration and scoped source-only quantity
    using literal excerpts, exact source locators, units, stages and original capture
    hashes. Provider-declared volume is kept separate from measured assembled final
    volume.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution242
  - solution5902
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, source-only additions and owner differences
  outcome: concern
  summary: Both local layers omit preparation_steps. Preserve the source nitrogen
    preparation, initial omissions, boil/cool sequence, bicarbonate/carbonate addition,
    6 N NaOH pH adjustment and approximate volume, autoclaving, then neutralized sulfide/vitamins/sucrose
    from sterile stocks. Stock NTA/KOH sequence and provider-only vitamin filtration
    remain in their own stocks. No temperature or duration is specified by the main
    primary source.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution242
  - solution5902
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: 'Yeast extract supports COMPLEX/UNDEFINED and the source has no mandatory
    gelling agent, consistent with LIQUID. Aerobic: Yes from KOMODO is not a growth
    result and does not negate the primary preparation under nitrogen.'
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution242
  - solution5902
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical specificity
  outcome: concern
  summary: Nickel hexahydrate in both stock versions conflicts with CHEBI:34887 nickel
    dichloride, whose formula Cl2Ni lacks hydration water. Exact label resolution
    does not validate supplied-form grounding. Calcium D-(+)-pantothenate is explicitly
    supported; no DL-to-D conflict applies. Generic vitamin B12 and biotin source
    wording does not resolve every possible supplied form, so no speculative replacement
    is proposed.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution242
  - solution5902
- assessment_id: growth
  area: scope
  topic: Growth, organism taxonomy and graph claims
  outcome: not_applicable
  summary: The title, generic Microbial cultivation application and catalog Aerobic
    flags are not experimental growth or taxonomy evidence. No growth assertions,
    current taxonomy IDs or graph membership are added. Explicit source strain qualifiers
    remain formulation scope only.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution242
  - solution5902
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: writer
  area: provenance
  topic: Authoritative inputs and current writer scope
  outcome: concern
  summary: Current MediaDive code distinguishes stock additions and solutions, preserves
    preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge
    ownership and current cleanup were inspected; current cleanup does not reproduce
    the historical disagreeing-duplicate sums. Current code is context, not proof
    of a particular historical execution. Correct every exact normalized contributor,
    attach claim-scoped evidence and append provenance clarification; regenerate derived
    products only after separately authorized correction.
  target_ids:
  - CultureMech:006329
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: flattened-stocks
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Vitamin and mineral stocks are flattened and NaCl contributions summed
  description: Vitamin and mineral concentrations are incorrectly direct medium quantities.
    NaCl 11 G_PER_L combines a main contribution of 10 with a stock contribution of
    1 without the 1 mL receiving dose. Source water and stock descriptors are omitted.
  target_ids:
  - CultureMech:006329
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
  issue_key: mineral-version-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Selected mineral II stock differs from current referenced mineral stock
  description: The provider selects 5902 with 0.025 g nickel hexahydrate and no tungstate;
    the primary 700 cross-reference currently resolves to 141/241 with 0.03 g nickel
    hexahydrate and 0.40 mg tungstate. Available captures do not establish historical
    correspondence or chronology.
  target_ids:
  - CultureMech:006329
  field_paths:
  - solutions
  - ingredients[30].concentration
  evidence_ids:
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution5902
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Anhydrous nickel identifier conflicts with explicit hexahydrate
  description: ingredients[30] names NiCl2 x 6 H2O but both primary and secondary
    CHEBI assertions use CHEBI:34887, anhydrous nickel dichloride. Both candidate
    stock sources explicitly name the hexahydrate.
  target_ids:
  - CultureMech:006329
  field_paths:
  - ingredients[30].term
  - ingredients[30].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - chebi34887
  - provider
  - referenced-primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and stock stages are absent
  description: The record retains only a pH scalar and variable NaOH ingredient, omitting
    the complete main sequence and stock-specific procedures. The missing stage context
    affects the interpretation of the amounts.
  target_ids:
  - CultureMech:006329
  field_paths:
  - preparation_steps
  - ph_value
  - ingredients[32].concentration
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: P3.5 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: historical-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamp strings remain malformed or timezone-naive
  description: The target and KOMODO owner each retain one malformed import timestamp
    and one timezone-naive resolver timestamp. These do not validate source chronology
    and should not be silently rewritten.
  target_ids:
  - CultureMech:006329
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
  description: 'Correct the exact maintained KOMODO owner: restore separate main,
    vitamin and mineral stages, receiving doses and original water units; remove incompatible
    NaCl summation and double counting. Preserve nominal provider volume versus unestablished
    measured final volume. Attach every amount to its literal source scope before
    regeneration.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
  description: Represent the exact alternatives and seek version-specific evidence
    before choosing a canonical stock; do not silently substitute current 241 for
    selected 5902 or infer a chronology. Keep all shared stock rows and dose basis
    separate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
  description: Re-ground the exact supplied hexahydrate in the maintained owner after
    separately validating its ontology and secondary correspondence. Preserve source
    hydration, stock amount and unresolved source-version alternatives; do not infer
    an unverified replacement ID.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
  description: Restore exact source-scoped preparation and its qualifiers in the owner;
    include approximate NaOH dose/strength, distinct stock pH sequence and provenance-qualified
    provider filtration. Do not transfer the parent 141 medium recipe, gas ratios,
    pressure or organism-specific conditions.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
  description: Preserve original history and append a clarification identifying the
    literal timestamp defects and known provenance limits when the owner is curated;
    do not fabricate historical times or source chronology.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_700_ALKALIPHILIC_SPIROCHAETE_medium.yaml
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
- Exact KOMODO 700 detail returned HTTP 403. The primary DSMZ 700 recipe, complete
  provider and exact catalog identity are available; this optional detail does not
  make the current comparison incomplete or resolve historical stock chronology.
- Only exact per-record bound captures are used. Current collection and provider differences
  do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently
  establish a measured final mixture volume. No density, percent basis, exact hydration,
  default sterilization cycle or stock volume is invented.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-022
- generated-medium
```
