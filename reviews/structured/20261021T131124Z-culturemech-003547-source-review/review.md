# Source and formulation review: alkaliphilic_halomonas_medium (CultureMech:003547)

- Review: 20261021T131124Z-culturemech-003547-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:04:58Z
- Finished UTC: 2026-10-21T13:11:24Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 1034 primary and provider identify the two maintained contributors and expose stock-stage quantities flattened into direct medium concentrations. The complete source preserves two receiving doses and three separate water amounts. A completed scientific review identifies stock reconstruction, missing target/KOMODO preparation and evidence follow-up, without treating the optional inaccessible KOMODO detail as missing primary access.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 218; batch 022 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-one task batches contain 210 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 213 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003547 | data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml | generated | alkaliphilic_halomonas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003547 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003547 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/218/strict.tsv |
| validate-terms | passed | True | CultureMech:003547 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003547 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003547 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo1034detail | unavailable | False | CultureMech:003547 | Exact KOMODO 1034 detail returned HTTP 403. This optional historical detail does not prevent current source assessment because the exact collection PDF, full provider response and catalog identity are available; no historical formulation absence is inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003547.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003547.

13 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain the source main-stage mass and the matching provider-normalized number, with the provider-declared 1000 mL basis explicit.",
    "rationale": "The current number exactly matches the source mass and nominal provider g/L but has no attached amount evidence. The primary lists 1000 mL water plus stock additions; it does not establish a measured assembled final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Sodium citrate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain the source main-stage mass and the matching provider-normalized number, with the provider-declared 1000 mL basis explicit.",
    "rationale": "The current number exactly matches the source mass and nominal provider g/L but has no attached amount evidence. The primary lists 1000 mL water plus stock additions; it does not establish a measured assembled final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sodium citrate\",\n                        \"compound_id\": 792,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 11.6248,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "MgSO4 x 7 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain the source main-stage mass and the matching provider-normalized number, with the provider-declared 1000 mL basis explicit.",
    "rationale": "The current number exactly matches the source mass and nominal provider g/L but has no attached amount evidence. The primary lists 1000 mL water plus stock additions; it does not establish a measured assembled final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Na2CO3",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain the source main-stage mass and the matching provider-normalized number, with the provider-declared 1000 mL basis explicit.",
    "rationale": "The current number exactly matches the source mass and nominal provider g/L but has no attached amount evidence. The primary lists 1000 mL water plus stock additions; it does not establish a measured assembled final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 28.3051,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "NaCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain the source main-stage mass and the matching provider-normalized number, with the provider-declared 1000 mL basis explicit.",
    "rationale": "The current number exactly matches the source mass and nominal provider g/L but has no attached amount evidence. The primary lists 1000 mL water plus stock additions; it does not establish a measured assembled final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 100,\n                        \"unit\": \"g\",\n                        \"g_l\": 100,\n                        \"mmol_l\": 1711.16,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "MnCl2 x 4 H2O stock composition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 0.36 g in the exact A stock, whose source lists 1000 mL water; keep its 1 mL receiving dose separate.",
    "rationale": "The stored number is a stock-stage quantity wrongly asserted directly in the medium. Do not convert it to a final-medium g/L claim without the receiving final-volume basis. Literal stock strength, water and dose belong in separate source-scoped fields.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.36,\n                        \"mmol_l\": 1.81905,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "FeSO4 x 7 H2O stock composition",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Restore 50 g in the exact B stock, whose source lists 1000 mL water; keep its 1 mL receiving dose separate.",
    "rationale": "The stored number is a stock-stage quantity wrongly asserted directly in the medium. Do not convert it to a final-medium g/L claim without the receiving final-volume basis. Literal stock strength, water and dose belong in separate source-scoped fields.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 179.846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Solution A receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1 mL of exact mediadive.solution:2101 in the source main assembly.",
    "rationale": "Both contributors and target omit the stock descriptors. Add source identity and volume dose without double-counting the currently flattened solute.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 2101,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Solution B receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1 mL of exact mediadive.solution:2102 in the source main assembly.",
    "rationale": "Both contributors and target omit the stock descriptors. Add source identity and volume dose without double-counting the currently flattened solute.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 2102,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL distilled water in the named stage.",
    "rationale": "Preserve water as source volume. The literal main liquid inputs total 1002 mL, whereas provider declares 1000 mL; neither value proves a measured final volume after preparation.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Solution A water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL distilled water in the named stage.",
    "rationale": "Preserve water as source volume. The literal main liquid inputs total 1002 mL, whereas provider declares 1000 mL; neither value proves a measured final volume after preparation.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Solution B water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 mL distilled water in the named stage.",
    "rationale": "Preserve water as source volume. The literal main liquid inputs total 1002 mL, whereas provider declares 1000 mL; neither value proves a measured final volume after preparation.",
    "source_snippets": [
      {
        "source_key": "mediadive1034api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1034",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Main pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "pH 9.0, preserving the source adjustment instruction.",
    "rationale": "The numeric ph_value is present in all layers without attached evidence. DSMZ owner also retains preparation_steps[1].description; target and KOMODO owner omit that procedure.",
    "source_snippets": [
      {
        "source_key": "dsmz1034",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1034.pdf",
        "source_locator": "Page 1 preparation",
        "exact_source_quote": "adjust to pH 9.0",
        "snapshot_sha256": "94dca684236171a8c8438b113de2d1f384acc587a2b72f7fa4858089827ded73",
        "parsed_text_sha256": "49fb8e27257c3a2a75d6448118da67cad377f2ea3b33008674f81d3d14346322"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:003547.

6 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 6/7 primary and 6/7 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 7: primary 85.71%; secondary 85.71%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source accession and maintained ownership

identity: supported. Targets: CultureMech:003547.

CM003547 resolves to the exact KOMODO 1034 owner and explicitly merged DSMZ 1034 contributor CM000457. Their source accession and current ingredient signatures agree; their preparation fields are not identical. All three parent/child path assertions resolve exactly in the ignored-inclusive normalized corpus.

### Claim-level amount support and source scope

evidence: concern. Targets: CultureMech:003547.

The local layers have import provenance but no attached amount evidence. The inventory covers every local concentration and scoped source-only quantity using literal excerpts, exact source locators, units, stages and original capture hashes. Provider-declared volume is kept separate from measured assembled final volume.

### Preparation stages, source-only additions and owner differences

completeness: concern. Targets: CultureMech:003547.

DSMZ owner retains preparation_steps[0] separate Na2CO3/NaCl autoclaving and preparation_steps[1] pH 9.0. Target and KOMODO owner omit both. Reconstruct A/B stocks and their source water/doses, preserve the retained DSMZ steps and recover them in the other representation. No temperature or duration is given by this source, so none is inferred.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:003547.

Yeast extract supports COMPLEX/UNDEFINED. The source has no mandatory gelling agent, consistent with LIQUID. The medium title and catalog Aerobic: No do not establish an organism-specific phenotype.

### Supplied forms and chemical specificity

grounding: supported. Targets: CultureMech:003547.

All explicit magnesium, manganese and iron hydrate names agree with their asserted ontology forms. Sodium citrate CHEBI:53258 is trisodium citrate; the source does not specify a supplied hydrate or grade. Preserve that source uncertainty and do not infer an exact hydrate replacement or hydrate-dependent molarity.

### Growth, organism taxonomy and graph claims

scope: not_applicable. Targets: CultureMech:003547.

The title, generic Microbial cultivation application and catalog Aerobic flags are not experimental growth or taxonomy evidence. No growth assertions, current taxonomy IDs or graph membership are added. Explicit source strain qualifiers remain formulation scope only.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003547.

22 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Authoritative inputs and current writer scope

provenance: concern. Targets: CultureMech:003547.

Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction.

## Findings

### f1: A/B stock composition is presented as direct medium concentration

blocker / open / confirmed; issue key: flattened-a-b-stocks.

All three layers list manganese chloride tetrahydrate 0.36 G_PER_L and ferrous sulfate heptahydrate 50 G_PER_L directly. Those are the respective stock compositions, each dosed at 1 mL in the primary main recipe. The source stock descriptors and all three water volumes are absent.

### f2: Target and KOMODO owner omit preparation retained by the DSMZ owner

major / open / confirmed; issue key: preparation-loss.

The primary separate carbonate/salt autoclaving and pH 9.0 adjustment are present in DSMZ owner preparation_steps but omitted from the generated target and KOMODO contributor. A source-duplicate ingredient signature is not evidence that every field is equivalent.

### f3: Historical timestamp strings remain malformed or timezone-naive

minor / open / confirmed; issue key: historical-timestamp-shape.

The target and KOMODO owner each retain one malformed import timestamp and one timezone-naive resolver timestamp. These do not validate source chronology and should not be silently rewritten.

## Recommended Actions And Acceptance Checks

### a1

Correct both exact normalized contributors: restore the source A/B stock composition and identities, separate 1 mL receiving doses, and water volume for each stage. Attach literal amount evidence, preserve the primary/provider volume distinction, and avoid double-counting stock solutes. Regenerate after owner corrections.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the DSMZ owner steps, add matching scoped preparation/evidence to the KOMODO owner as appropriate, and ensure the merger retains the evidenced preparation. Do not invent a sterilization cycle or measured final volume. Append a clarification rather than rewriting historical events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve original history and append a clarification identifying the literal timestamp defects and known provenance limits when the owner is curated; do not fabricate historical times or source chronology.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch022/218/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/218/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml:1:id: CultureMech:003547<br>./data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml:1:id: CultureMech:003547<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/218/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 12 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/218/evidence-context-original.json; Complete frozen target/owners, source stages, exact secondary lookup and ignored-inclusive relationships | context_only | Full captured records re-read and compared by exact equality with fresh inspected records. Context is supporting provenance; exact bound primary/provider captures independently support scientific claims. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1034.pdf; Page 1: full main recipe, Solution A, Solution B and preparation | supports | DSMZ 1034 explicitly separates two stocks, their 1 mL receiving doses and listed 1000 mL water for each stage. Carbonate and salt are separately autoclaved; pH is 9.0. |
| provider | https://mediadive.dsmz.de/rest/medium/1034; data.medium; solutions2100/2101/2102 recipe and steps | supports | Provider declares 1000 mL for the main and each stock and retains exact A/B identities and doses. This is a nominal provider denominator, not an independent measured assembled final volume. |
| solution2101 | https://mediadive.dsmz.de/rest/solution/2101; data.id/name/volume/recipe | supports | Exact stock endpoint matches the same-ID stage in the main provider response after null-only fields are removed. |
| solution2102 | https://mediadive.dsmz.de/rest/solution/2102; data.id/name/volume/recipe | supports | Exact stock endpoint matches the same-ID stage in the main provider response after null-only fields are removed. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Table first cell exactly 1034; source mapping | supports | Exact KOMODO accession maps to DSMZ 1034. The Aerobic flag is catalog provenance, not a growth assertion. |
| komodo1034detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1034; Preserved exact public retrieval result | context_only | Exact KOMODO 1034 detail returned HTTP 403. This optional historical detail does not prevent current source assessment because the exact collection PDF, full provider response and catalog identity are available; no historical formulation absence is inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch022/218/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53258 resolves to sodium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml; data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.108527"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.108527"}]}, {"input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact KOMODO 1034 detail returned HTTP 403. This optional historical detail does not prevent current source assessment because the exact collection PDF, full provider response and catalog identity are available; no historical formulation absence is inferred.
- Only exact per-record bound captures are used. Current collection and provider differences do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently establish a measured final mixture volume. No density, percent basis, exact hydration, default sterilization cycle or stock volume is invented.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131124Z-culturemech-003547-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilic_halomonas_medium (CultureMech:003547)'
started_at: '2026-10-21T13:04:58Z'
finished_at: '2026-10-21T13:11:24Z'
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
summary: The exact DSMZ 1034 primary and provider identify the two maintained contributors
  and expose stock-stage quantities flattened into direct medium concentrations. The
  complete source preserves two receiving doses and three separate water amounts.
  A completed scientific review identifies stock reconstruction, missing target/KOMODO
  preparation and evidence follow-up, without treating the optional inaccessible KOMODO
  detail as missing primary access.
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
  - path: data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
    sha256: 6591c676141c5294cfbef3b30698dcaf65436b86f73effee270f4ef143da31b8
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    sha256: eb84d1ad628d709055f7394216b1c7657f3dec9c785d7ed3d0bc42c8dec5f940
    role: context
  - path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
    sha256: a572634de0fee1620a7cb855d3528cd0ef4ca0878f03e704ec04134dcf299e3a
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
  selection: Task review 218; batch 022 item 8 of 10, selected in Python lexicographic
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
  - CultureMech:003547
targets:
- target_id: CultureMech:003547
  path: data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  label: alkaliphilic_halomonas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/218/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/218/strict.tsv"
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003547
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
  - CultureMech:003547
- check_id: komodo1034detail-source-access
  name: 'Exact source content access: komodo1034detail'
  required: false
  status: unavailable
  summary: Exact KOMODO 1034 detail returned HTTP 403. This optional historical detail
    does not prevent current source assessment because the exact collection PDF, full
    provider response and catalog identity are available; no historical formulation
    absence is inferred.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - komodo1034detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:11:23Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:11:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:11:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:06.356426Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/218/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:10.763353Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/218/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:19.685459Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:22.628543Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:11:23Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml:1:id: CultureMech:003547

    ./data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml:1:id:
    CultureMech:003547

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/218/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:11:23Z'
  support: supports
  summary: 12 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 149c8a5ceaca3c26b662a0f74b396f08516bbe07b9f2382761dd0340d8548926
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/218/evidence-context-original.json
  locator: Complete frozen target/owners, source stages, exact secondary lookup and
    ignored-inclusive relationships
  accessed_at: '2026-10-21T13:11:23Z'
  support: context_only
  summary: Full captured records re-read and compared by exact equality with fresh
    inspected records. Context is supporting provenance; exact bound primary/provider
    captures independently support scientific claims.
  snapshot_sha256: f4cbbab3373b7d45ea738ec4b7f3848f7ff79c6e338bd9fbe9ba4d50c85d510a
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1034.pdf
  locator: 'Page 1: full main recipe, Solution A, Solution B and preparation'
  accessed_at: '2026-10-21T12:48:25.862330Z'
  support: supports
  summary: DSMZ 1034 explicitly separates two stocks, their 1 mL receiving doses and
    listed 1000 mL water for each stage. Carbonate and salt are separately autoclaved;
    pH is 9.0.
  snapshot_sha256: 94dca684236171a8c8438b113de2d1f384acc587a2b72f7fa4858089827ded73
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1034
  locator: data.medium; solutions2100/2101/2102 recipe and steps
  accessed_at: '2026-10-21T12:48:24.885961Z'
  support: supports
  summary: Provider declares 1000 mL for the main and each stock and retains exact
    A/B identities and doses. This is a nominal provider denominator, not an independent
    measured assembled final volume.
  snapshot_sha256: f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799
- evidence_id: solution2101
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2101
  locator: data.id/name/volume/recipe
  accessed_at: '2026-10-21T12:49:29.673062Z'
  support: supports
  summary: Exact stock endpoint matches the same-ID stage in the main provider response
    after null-only fields are removed.
  snapshot_sha256: e01ee5bba8fdf0d8f91a17ae8edcdd52933a5e025bf264821f1fb156ecc81c4e
- evidence_id: solution2102
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2102
  locator: data.id/name/volume/recipe
  accessed_at: '2026-10-21T12:49:29.673692Z'
  support: supports
  summary: Exact stock endpoint matches the same-ID stage in the main provider response
    after null-only fields are removed.
  snapshot_sha256: f2faba75410e5cd205677038264e5b807bcf2aa4ac177896458431d33195d6f2
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Table first cell exactly 1034; source mapping
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Exact KOMODO accession maps to DSMZ 1034. The Aerobic flag is catalog provenance,
    not a growth assertion.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo1034detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1034
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:48:24.884819Z'
  support: context_only
  summary: Exact KOMODO 1034 detail returned HTTP 403. This optional historical detail
    does not prevent current source assessment because the exact collection PDF, full
    provider response and catalog identity are available; no historical formulation
    absence is inferred.
  snapshot_sha256: 4f6f4a0fd4f28c0d9720197e55f401056c0206e030df26e5a873bb7c9e127985
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/218/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:11:23Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: b54a931fbbe1799fac73440e3a09151be1fb295e87fed8fe6f041107f204a758
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
- evidence_id: chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: CHEBI:53258 resolves to sodium citrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:11:23Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate",
    "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term":
    "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED",
    "ambiguity": "resolved:owned"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O",
    "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml;
    data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:11:23Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:58.108527"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:58.108527"}]}, {"input": "data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:11:23Z'
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
  accessed_at: '2026-10-21T13:11:23Z'
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
  accessed_at: '2026-10-21T13:11:23Z'
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
  accessed_at: '2026-10-21T13:11:23Z'
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
  - CultureMech:003547
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 13 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain the source main-stage mass and the matching provider-normalized number,\
    \ with the provider-declared 1000 mL basis explicit.\",\n    \"rationale\": \"\
    The current number exactly matches the source mass and nominal provider g/L but\
    \ has no attached amount evidence. The primary lists 1000 mL water plus stock\
    \ additions; it does not establish a measured assembled final volume.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"\
    compound_id\\\": 16,\\n                        \\\"amount\\\": 10,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 10,\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Sodium citrate\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain the source main-stage mass and the matching provider-normalized number,\
    \ with the provider-declared 1000 mL basis explicit.\",\n    \"rationale\": \"\
    The current number exactly matches the source mass and nominal provider g/L but\
    \ has no attached amount evidence. The primary lists 1000 mL water plus stock\
    \ additions; it does not establish a measured assembled final volume.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"Sodium citrate\\\",\\n                        \\\"\
    compound_id\\\": 792,\\n                        \\\"amount\\\": 3,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 3,\\n                        \\\"mmol_l\\\": 11.6248,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"MgSO4 x 7 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain the source main-stage mass and the matching provider-normalized number,\
    \ with the provider-declared 1000 mL basis explicit.\",\n    \"rationale\": \"\
    The current number exactly matches the source mass and nominal provider g/L but\
    \ has no attached amount evidence. The primary lists 1000 mL water plus stock\
    \ additions; it does not establish a measured assembled final volume.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 1,\\n          \
    \              \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 1,\\n                        \\\"mmol_l\\\": 4.05719,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Na2CO3\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain the source main-stage mass and the matching provider-normalized number,\
    \ with the provider-declared 1000 mL basis explicit.\",\n    \"rationale\": \"\
    The current number exactly matches the source mass and nominal provider g/L but\
    \ has no attached amount evidence. The primary lists 1000 mL water plus stock\
    \ additions; it does not establish a measured assembled final volume.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\
    \": 32,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"mmol_l\\\": 28.3051,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"NaCl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain the source main-stage mass and the matching provider-normalized number,\
    \ with the provider-declared 1000 mL basis explicit.\",\n    \"rationale\": \"\
    The current number exactly matches the source mass and nominal provider g/L but\
    \ has no attached amount evidence. The primary lists 1000 mL water plus stock\
    \ additions; it does not establish a measured assembled final volume.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 100,\\n \
    \                       \\\"mmol_l\\\": 1711.16,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"MnCl2 x 4 H2O stock composition\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 0.36 g in the exact A stock, whose source lists 1000 mL water; keep\
    \ its 1 mL receiving dose separate.\",\n    \"rationale\": \"The stored number\
    \ is a stock-stage quantity wrongly asserted directly in the medium. Do not convert\
    \ it to a final-medium g/L claim without the receiving final-volume basis. Literal\
    \ stock strength, water and dose belong in separate source-scoped fields.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"\
    compound_id\\\": 36,\\n                        \\\"amount\\\": 0.36,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.36,\\n                        \\\"mmol_l\\\": 1.81905,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"FeSO4 x 7 H2O stock composition\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Restore 50 g in the exact B stock, whose source lists 1000 mL water; keep\
    \ its 1 mL receiving dose separate.\",\n    \"rationale\": \"The stored number\
    \ is a stock-stage quantity wrongly asserted directly in the medium. Do not convert\
    \ it to a final-medium g/L claim without the receiving final-volume basis. Literal\
    \ stock strength, water and dose belong in separate source-scoped fields.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1034api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\",\n \
    \       \"source_locator\": \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 12,\\n                        \\\"amount\\\": 50,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 50,\\n                        \\\"mmol_l\\\": 179.846,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Solution A receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1 mL of exact mediadive.solution:2101 in the source main assembly.\",\n  \
    \  \"rationale\": \"Both contributors and target omit the stock descriptors. Add\
    \ source identity and volume dose without double-counting the currently flattened\
    \ solute.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive1034api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"solution\\\": \\\"Solution A\\\",\\n            \
    \            \\\"solution_id\\\": 2101,\\n                        \\\"amount\\\
    \": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                \
    \        \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Solution B receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1 mL of exact mediadive.solution:2102 in the source main assembly.\",\n  \
    \  \"rationale\": \"Both contributors and target omit the stock descriptors. Add\
    \ source identity and volume dose without double-counting the currently flattened\
    \ solute.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive1034api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"solution\\\": \\\"Solution B\\\",\\n            \
    \            \\\"solution_id\\\": 2102,\\n                        \\\"amount\\\
    \": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                \
    \        \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 mL distilled water in the named stage.\",\n    \"rationale\": \"Preserve\
    \ water as source volume. The literal main liquid inputs total 1002 mL, whereas\
    \ provider declares 1000 mL; neither value proves a measured final volume after\
    \ preparation.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1034api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Solution A water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 mL distilled water in the named stage.\",\n    \"rationale\": \"Preserve\
    \ water as source volume. The literal main liquid inputs total 1002 mL, whereas\
    \ provider declares 1000 mL; neither value proves a measured final volume after\
    \ preparation.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1034api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Solution B water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 mL distilled water in the named stage.\",\n    \"rationale\": \"Preserve\
    \ water as source volume. The literal main liquid inputs total 1002 mL, whereas\
    \ provider declares 1000 mL; neither value proves a measured final volume after\
    \ preparation.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1034api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1034\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f53240ef7262d433415ff10e892df1e116669c46a08f89e13cbcb56e2fab1799\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Main pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_HALOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"pH 9.0, preserving the source adjustment instruction.\",\n    \"rationale\"\
    : \"The numeric ph_value is present in all layers without attached evidence. DSMZ\
    \ owner also retains preparation_steps[1].description; target and KOMODO owner\
    \ omit that procedure.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1034\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1034.pdf\"\
    ,\n        \"source_locator\": \"Page 1 preparation\",\n        \"exact_source_quote\"\
    : \"adjust to pH 9.0\",\n        \"snapshot_sha256\": \"94dca684236171a8c8438b113de2d1f384acc587a2b72f7fa4858089827ded73\"\
    ,\n        \"parsed_text_sha256\": \"49fb8e27257c3a2a75d6448118da67cad377f2ea3b33008674f81d3d14346322\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '6 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 6/7 primary and 6/7 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi26710
  - chebi29377
  - chebi31795
  - chebi53258
  - chebi75836
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 7: primary 85.71%;
    secondary 85.71%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Source accession and maintained ownership
  outcome: supported
  summary: CM003547 resolves to the exact KOMODO 1034 owner and explicitly merged
    DSMZ 1034 contributor CM000457. Their source accession and current ingredient
    signatures agree; their preparation fields are not identical. All three parent/child
    path assertions resolve exactly in the ignored-inclusive normalized corpus.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - owner-1
  - primary
  - provider
  - komodo-catalog
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
  - CultureMech:003547
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - komodo-catalog
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, source-only additions and owner differences
  outcome: concern
  summary: DSMZ owner retains preparation_steps[0] separate Na2CO3/NaCl autoclaving
    and preparation_steps[1] pH 9.0. Target and KOMODO owner omit both. Reconstruct
    A/B stocks and their source water/doses, preserve the retained DSMZ steps and
    recover them in the other representation. No temperature or duration is given
    by this source, so none is inferred.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - komodo-catalog
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: 'Yeast extract supports COMPLEX/UNDEFINED. The source has no mandatory
    gelling agent, consistent with LIQUID. The medium title and catalog Aerobic: No
    do not establish an organism-specific phenotype.'
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical specificity
  outcome: supported
  summary: All explicit magnesium, manganese and iron hydrate names agree with their
    asserted ontology forms. Sodium citrate CHEBI:53258 is trisodium citrate; the
    source does not specify a supplied hydrate or grade. Preserve that source uncertainty
    and do not infer an exact hydrate replacement or hydrate-dependent molarity.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: growth
  area: scope
  topic: Growth, organism taxonomy and graph claims
  outcome: not_applicable
  summary: The title, generic Microbial cultivation application and catalog Aerobic
    flags are not experimental growth or taxonomy evidence. No growth assertions,
    current taxonomy IDs or graph membership are added. Explicit source strain qualifiers
    remain formulation scope only.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - primary
  - provider
  - komodo-catalog
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 22 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003547
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
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
  - CultureMech:003547
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: flattened-a-b-stocks
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: A/B stock composition is presented as direct medium concentration
  description: All three layers list manganese chloride tetrahydrate 0.36 G_PER_L
    and ferrous sulfate heptahydrate 50 G_PER_L directly. Those are the respective
    stock compositions, each dosed at 1 mL in the primary main recipe. The source
    stock descriptors and all three water volumes are absent.
  target_ids:
  - CultureMech:003547
  field_paths:
  - ingredients[5].concentration
  - ingredients[6].concentration
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - solution2101
  - solution2102
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
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
  issue_key: preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Target and KOMODO owner omit preparation retained by the DSMZ owner
  description: The primary separate carbonate/salt autoclaving and pH 9.0 adjustment
    are present in DSMZ owner preparation_steps but omitted from the generated target
    and KOMODO contributor. A source-duplicate ingredient signature is not evidence
    that every field is equivalent.
  target_ids:
  - CultureMech:003547
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
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
  - CultureMech:003547
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
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
  description: 'Correct both exact normalized contributors: restore the source A/B
    stock composition and identities, separate 1 mL receiving doses, and water volume
    for each stage. Attach literal amount evidence, preserve the primary/provider
    volume distinction, and avoid double-counting stock solutes. Regenerate after
    owner corrections.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003547
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
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
  description: Preserve the DSMZ owner steps, add matching scoped preparation/evidence
    to the KOMODO owner as appropriate, and ensure the merger retains the evidenced
    preparation. Do not invent a sterilization cycle or measured final volume. Append
    a clarification rather than rewriting historical events.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003547
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
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
  description: Preserve original history and append a clarification identifying the
    literal timestamp defects and known provenance limits when the owner is curated;
    do not fabricate historical times or source chronology.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003547
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml
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
- Exact KOMODO 1034 detail returned HTTP 403. This optional historical detail does
  not prevent current source assessment because the exact collection PDF, full provider
  response and catalog identity are available; no historical formulation absence is
  inferred.
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
