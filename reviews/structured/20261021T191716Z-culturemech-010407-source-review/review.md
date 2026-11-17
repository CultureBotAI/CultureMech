# Source and formulation review: acidilobus_saccharovorans_medium (CultureMech:010407)

- Review: 20261021T191716Z-culturemech-010407-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:13:51Z
- Finished UTC: 2026-10-21T19:17:16Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 934 explicitly delegates to JCM 308 with yeast extract 0.1 g/L final and glucose 2 g/L. The local record instead assigns mass-rate units to water, resazurin and three stock doses, omits the stock compositions and source preparation, and leaves an unresolved historical sulfur linkage. Only the named M180 iron/trace and M190 vitamin subsections transfer; their current amount evidence is separately authenticated. Historical legacy correspondence remains unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 341; batch 035 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-four task batches contain 340 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 343 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010407 | data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml | generated | acidilobus_saccharovorans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010407 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010407 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/341/strict.tsv |
| validate-terms | passed | True | CultureMech:010407 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010407 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010407 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required source-scope verification | unavailable | True | CultureMech:010407 | Required historical correspondence of legacy MediaIngredientMech:001072 for sulfur powder remains unavailable. The complete current catalog/tree negative lookup is finished and is not itself an unavailable check or proof of historical invalidity. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010407.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010407.

55 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Main: Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1,
      "source_unit": "L",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The source states a volume or milligram batch amount, not the stored gram-per-liter value. Restore original units and stage; no assumed final volume."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Main: CaCl2・2H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.33,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Main: KH2PO4",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.33,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main: NH4Cl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.33,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main: Resazurin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 1,
      "source_unit": "mg",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The source states a volume or milligram batch amount, not the stored gram-per-liter value. Restore original units and stage; no assumed final volume."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Main: MgCl2・6H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.33,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Main: Na2S・9H2O",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.5,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Main: KCl",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.33,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Main: Sulfur (powder)",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Sulfur (powder)\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 10,
      "source_unit": "g",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid stocks and separate additions does not establish a measured final liter; preserve batch mass instead of asserting an unsupported exact g/L rate."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Main: glucose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"glucose\",\n          \"volume\": 2,\n          \"unit\": \"g/L\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 2,
      "source_unit": "g/L",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The exact receiving source explicitly gives this g/L rate. The local value matches but has no attached claim-level evidence. Yeast 0.1 g/L final overrides the delegated parent yeast row; it is not additive."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Main: Yeast extract (BD-Difco)",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\": \"g/L\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": 0.1,
      "source_unit": "g/L",
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "The exact receiving source explicitly gives this g/L rate. The local value matches but has no attached claim-level evidence. Yeast 0.1 g/L final overrides the delegated parent yeast row; it is not additive."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Main: H2SO4",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"H2SO4\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": null,
      "source_unit": null,
      "reagent_strength": 1,
      "reagent_strength_unit": "N",
      "measured_final_volume_L": null
    },
    "rationale": "No fixed receiving dose is given for the adjustment reagent or gases. VARIABLE preserves an unspecified dose but does not capture the separately stated reagent strength or preparation gas ratio."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Main: Carbon dioxide gas",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[15]",
        "exact_source_quote": "\"component_name\": \"Carbon dioxide gas\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": null,
      "source_unit": null,
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "No fixed receiving dose is given for the adjustment reagent or gases. VARIABLE preserves an unspecified dose but does not capture the separately stated reagent strength or preparation gas ratio."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Main: Nitrogen gas",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[16]",
        "exact_source_quote": "\"component_name\": \"Nitrogen gas\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "source_amount": null,
      "source_unit": null,
      "reagent_strength": null,
      "reagent_strength_unit": null,
      "measured_final_volume_L": null
    },
    "rationale": "No fixed receiving dose is given for the adjustment reagent or gases. VARIABLE preserves an unspecified dose but does not capture the separately stated reagent strength or preparation gas ratio."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Receiving stock dose: FeCl2 solution (see Medium [M180])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "batch_addition_mL": 1,
      "stock_subsection_only": true
    },
    "rationale": "The stated 1/1/10 mL additions are batch volumes, not g/L. Preserve the separate stock preparation and receiving dose without computing an unprovided final-medium denominator."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Receiving stock dose: Trace element solution (see Medium [M180])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "batch_addition_mL": 1,
      "stock_subsection_only": true
    },
    "rationale": "The stated 1/1/10 mL additions are batch volumes, not g/L. Preserve the separate stock preparation and receiving dose without computing an unprovided final-medium denominator."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Receiving stock dose: Trace vitamins (see Medium [M190])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM980original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95",
        "accessed_at": "2026-10-21T18:58:50.958420Z"
      }
    ],
    "proposed_source_representation": {
      "batch_addition_mL": 10,
      "stock_subsection_only": true
    },
    "rationale": "The stated 1/1/10 mL additions are batch volumes, not g/L. Preserve the separate stock preparation and receiving dose without computing an unprovided final-medium denominator."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Stock 1: 25% HCl (7.7 M)",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].solutions[0].concentration",
        "stored": {
          "value": "0.01",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 10,
      "unit": "ml",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Stock 1: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "0.99",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 990,
      "unit": "ml",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Stock 1: FeCl2・4H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].composition[1].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 1.5,
      "unit": "g",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Stock 2: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 1,
      "unit": "L",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Stock 2: Na2MoO4・2H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 36,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Stock 2: H3BO3",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 6,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Stock 2: MnCl2・4H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 100,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Stock 2: CoCl2・6H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 190,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Stock 2: NiCl2・6H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 24,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Stock 2: CuCl2・2H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 2,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Stock 2: ZnCl2",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
        "accessed_at": "2026-10-21T10:35:28.558157Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 70,
      "unit": "mg",
      "receiving_dose_mL": 1,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Stock 3: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 1,
      "unit": "L",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Stock 3: Biotin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 2,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Stock 3: p--Aminobenzoic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Stock 3: Thiamine・HCl",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Stock 3: Calcium pantothenate",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Stock 3: Pyridoxine・HCl",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 10,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Stock 3: Folic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 2,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Stock 3: Vitamin B12",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 0.1,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Stock 3: Riboflavin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[8].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Stock 3: Nicotinic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[9].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Stock 3: Lipoic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[10].notes",
        "stored": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
        "accessed_at": "2026-10-21T09:28:25.418127Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "mg",
      "receiving_dose_mL": 10,
      "stock_measured_final_volume_L": null
    },
    "rationale": "The receiving stock composition is empty; add this exact subsection with evidence. The maintained dependency already preserves this batch amount with attached matching raw/hash evidence. Keep the original water input, mass and reagent stage; do not divide by an inferred stock or final volume. Preserve source hydrate and unresolved chemical specificity separately."
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Iron-stock HCl strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].solutions[0].composition[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "MOLAR"
        },
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock acid row only",
        "exact_source_quote": "25% HCl (7.7 M)",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8",
        "accessed_at": "2026-10-21T10:35:30.362855Z"
      }
    ],
    "proposed_source_representation": {
      "value": 7.7,
      "unit": "M"
    },
    "rationale": "The source separately states 7.7 M and 25%; their equivalence is not derived. No percentage basis or density is inferred. The maintained nested reagent already has exact supporting source evidence."
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Iron-stock HCl percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].solutions[0].composition[0].notes",
        "stored": "Role: Solvating media; Properties: Defined component, Inorganic compound, Solution\n\nExplicit HCl reagent strength 7.7 M, not a final-medium concentration. The 25% basis is unspecified; the enclosing stock holds the 10 ml batch dose.",
        "decision": "verified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock acid row only",
        "exact_source_quote": "25% HCl (7.7 M)",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8",
        "accessed_at": "2026-10-21T10:35:30.362855Z"
      }
    ],
    "proposed_source_representation": {
      "value": 25,
      "unit": "percent; basis unspecified"
    },
    "rationale": "The source separately states 7.7 M and 25%; their equivalence is not derived. No percentage basis or density is inferred. The maintained nested reagent already has exact supporting source evidence."
  },
  {
    "quantity_id": "q42",
    "component_or_context": "Yeast reagent strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "10% (w/v)",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "value": 10,
      "unit": "PERCENT_W_V",
      "scope": "separate yeast extract reagent"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q43",
    "component_or_context": "Sulfide reagent strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "5% (w/v)",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "value": 5,
      "unit": "PERCENT_W_V",
      "scope": "separate sodium sulfide nonahydrate reagent"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Main gas ratio",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "(80:20)",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "ratio": [
        80,
        20
      ],
      "gases": [
        "N2",
        "CO2"
      ],
      "basis": "not explicitly stated"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q45",
    "component_or_context": "Sulfur steaming duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "3 hr",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "hours": 3,
      "scope": "each daily steaming"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q46",
    "component_or_context": "Sulfur steaming repetitions",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "3 successive days",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "successive_days": 3
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q47",
    "component_or_context": "Receiving pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "3.5 - 3.8",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "pH_range": [
        3.5,
        3.8
      ],
      "stage": "before inoculation"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q48",
    "component_or_context": "Acid reagent strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "1 N H 2 SO 4",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "strength": 1,
      "unit": "N",
      "dose": "not quantified"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q49",
    "component_or_context": "Post-inoculation pressure",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "100 kPa",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "pressure_kPa": 100,
      "gases": "N2:CO2 80:20",
      "gauge_or_absolute": "not stated",
      "stage": "inoculated bottle"
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q50",
    "component_or_context": "JCM default temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "121°C",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "temperature_C": 121
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q51",
    "component_or_context": "JCM default duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Delegated basal preparation or exact page default",
        "exact_source_quote": "15 min.",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "minutes": 15
    },
    "rationale": "This source-specific preparation quantity is absent from both layers. Preserve the stated stage, exceptions and sequence; do not convert into an incubation optimum or inherit different parent M180/M190 receiving conditions."
  },
  {
    "quantity_id": "q52",
    "component_or_context": "Main final volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm308",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308",
        "source_locator": "Relevant main or explicitly transferred stock water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c",
        "parsed_text_sha256": "fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207",
        "accessed_at": "2026-10-21T10:35:30.491607Z"
      }
    ],
    "proposed_source_representation": {
      "listed_water_L": 1,
      "listed_water_plus_three_stocks_mL": 1012,
      "measured_final_volume_L": null
    },
    "rationale": "Listed liquid arithmetic is not a measured final-volume declaration. Keep mass and volume batch amounts; do not silently normalize stock or main components to an assumed final liter."
  },
  {
    "quantity_id": "q53",
    "component_or_context": "Iron stock final volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Relevant main or explicitly transferred stock water row",
        "exact_source_quote": "Distilled water 990.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8",
        "accessed_at": "2026-10-21T10:35:30.362855Z"
      }
    ],
    "proposed_source_representation": {
      "water_mL": 990,
      "acid_mL": 10,
      "measured_final_volume_L": null
    },
    "rationale": "Listed liquid arithmetic is not a measured final-volume declaration. Keep mass and volume batch amounts; do not silently normalize stock or main components to an assumed final liter."
  },
  {
    "quantity_id": "q54",
    "component_or_context": "Trace stock final volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Relevant main or explicitly transferred stock water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8",
        "accessed_at": "2026-10-21T10:35:30.362855Z"
      }
    ],
    "proposed_source_representation": {
      "water_L": 1,
      "measured_final_volume_L": null
    },
    "rationale": "Listed liquid arithmetic is not a measured final-volume declaration. Keep mass and volume batch amounts; do not silently normalize stock or main components to an assumed final liter."
  },
  {
    "quantity_id": "q55",
    "component_or_context": "Vitamin stock final volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
        "field_path": "solutions",
        "stored": [
          {
            "preferred_term": "FeCl2 solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace element solution (see Medium [M180])",
            "composition": [],
            "notes": "Cross-reference to Medium M180",
            "concentration": {
              "value": "1",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          },
          {
            "preferred_term": "Trace vitamins (see Medium [M190])",
            "composition": [],
            "notes": "Cross-reference to Medium M190",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            },
            "name": "Unknown solution"
          }
        ],
        "decision": "not_quantified"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Relevant main or explicitly transferred stock water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f",
        "accessed_at": "2026-10-20T06:58:05.867253Z"
      }
    ],
    "proposed_source_representation": {
      "water_L": 1,
      "measured_final_volume_L": null
    },
    "rationale": "Listed liquid arithmetic is not a measured final-volume declaration. Keep mass and volume batch amounts; do not silently normalize stock or main components to an assumed final liter."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:010407.

13 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 13/14 primary and 7/14 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding. Historical sulfur linkage remains unresolved separately; current CHEBI-based lookup does not authenticate it.

Instance coverage on a 0–100 percent scale, denominator 14: primary 92.86%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010407.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Supplied forms and indirect stock specificity

grounding: concern. Targets: CultureMech:010407.

All main asserted CHEBI labels match; elemental sulfur does not contradict powder form. M180 trace cobalt/nickel hexahydrate names instead map to anhydrous CHEBI:35696/34887. M190 calcium pantothenate is unqualified while CHEBI:31345 encodes D stereochemistry; this is unsupported specificity, not proof that a D product is false. Other explicitly hydrated main/stock constituents agree at the stated formula level. Undefined yeast extract has no fabricated pure-chemical ID.

### Exact receiving accession and delegated stock scope

identity: supported. Targets: CultureMech:010407.

CultureMech:010407 has one exact maintained archaea owner and identifies TOGO M980/JCM 934. JCM 934 expressly delegates to JCM 308. Only FeCl2/trace stocks from M180/JCM 187 and trace vitamins from M190/JCM 197 transfer. No organism growth, taxonomy or whole-parent equivalence follows from the title or references.

### Absent source-specific preparation and conditions

completeness: concern. Targets: CultureMech:010407.

Both layers omit the delegated exclusions and staged autoclaving, separate 10% w/v yeast/5% w/v sulfide reagents, sulfur steaming, vitamin filtration, pH range/acid strength and post-inoculation pressure. JCM 934 additionally requires glucose separately autoclaved. Keep the source N2 versus N2:CO2 stage distinction, unknown pressure basis and exact sulfur repetitions; no M180/M190 parent conditions transfer.

### Composition, application and growth assertions

scope: supported. Targets: CultureMech:010407.

COMPLEX/SEMI_DEFINED and LIQUID are compatible with the salts, defined additions and undefined yeast extract. The generic microbial-cultivation application is not a strain-specific growth assertion. No target organism, growth performance, optimum, incubation temperature or additional taxonomy identifier is inferred from the title. Source physical preparation and supplied forms remain separately qualified.

### Claim-level evidence and source ownership

provenance: concern. Targets: CultureMech:010407.

The target and sole owner have source URLs/history but no attached amount evidence. Twenty-three transferred dependency evidence objects are independently reauthenticated: 22 exact raw snippets and one exact JCM extracted-text excerpt, each with the cited raw hash; their historical timestamps remain distinct from later identical capture times. Fifty-two unrelated parent evidence objects are excluded. Preserve the later dependency repairs and all history; fix the receiving owner without overwriting parent recipes.

## Findings

### f1: Water, indicator and stock doses have incorrect units and missing scope

blocker / open / confirmed; issue key: culturemech.010407.units-and-stock-boundaries.

Water 1 L is stored as 1 G_PER_L, resazurin 1 mg as 1 G_PER_L, and three 1/1/10 mL stock doses as G_PER_L with empty compositions. Other delegated masses lack a measured final-volume basis; yeast and glucose alone have explicit receiving g/L statements.

### f2: Exact staged preparation is absent

major / open / confirmed; issue key: culturemech.010407.preparation-omission.

The record omits materially different sterilization/addition stages, sulfur treatment and pre-/post-inoculation conditions from its explicitly delegated source.

### f3: Referenced trace stock contains hydrate mismatches

major / open / confirmed; issue key: culturemech.010407.indirect-stock-form-conflicts.

The explicitly transferred M180 trace stock maps CoCl2·6H2O and NiCl2·6H2O to anhydrous cobalt/nickel dichloride IDs. Matching labels do not establish exact source form.

### f4: Historical sulfur linkage and vitamin stereochemistry need qualification

minor / open / confirmed; issue key: culturemech.010407.legacy-and-vitamin-specificity.

Legacy sulfur ID correspondence is not recoverable from the current pinned catalog, while the transferred calcium-pantothenate source does not establish the D specificity encoded in its current term. Neither uncertainty proves the source ingredient is false.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained owner units and represent exact stock subsections/doses, with batch masses where final volume is unspecified. Keep yeast 0.1 g/L final and glucose 2 g/L with claim-level evidence; do not add the parent yeast amount. Regenerate only after maintaining source scope.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the source-specific preparation with literal evidence and exact stage boundaries, including glucose treatment, separate stock strengths, sulfur repetitions, pH and pressure limits. Do not substitute the referenced parents’ receiving conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve exact supplied-form identifiers within M180 solutions[1].composition[4].term and [5].term before stock transfer. Preserve amount evidence and unrelated parent content; do not invent replacement IDs.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Seek exact historical sulfur mapping provenance and supplier/form evidence for the transferred pantothenate. Until resolved, document the limits without changing sulfur identity, guessing a replacement key or asserting a different stereoisomer.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch035/341/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/341/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml:1:id: CultureMech:010407<br>./data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml:1:id: CultureMech:010407<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/341/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 49 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/341/evidence-context-original.json; Complete frozen source context and full local objects | context_only | Frozen target/owner objects match freshly inspected records. Source interpretations are assessed against actual bound capture bytes; historical limitations remain separate. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=934; Complete exact JCM 934 page | supports | Explicit yeast 0.1 g/L final is the receiving override, not an additional 0.1 g on top of the parent 0.3 g; glucose is separately autoclaved. |
| basal | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308; Complete delegated basal table and receiving preparation | supports | This expressly delegated basal source supplies the main recipe and stages; final measured volume is not stated. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980; meta, components[0], comments[0] and comments[2].comment (paragraph_index 4) | supports | Expanded source agrees with the primary override and basal amounts. The frozen preparatory context comments[3] locator is corrected here to the actual comments[2]. |
| provider-api | https://mediadive.dsmz.de/rest/medium/J934; data.medium and data.solutions[0].steps[0] | supports | This API supplies the same delegation sentence, not an independently expanded recipe or measured denominator. |
| iron-trace | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; FeCl2 solution and Trace element solution subsections only | supports | Only these stock formulas transfer; JCM 187 basal recipe, vitamins, gas, pH and other receiving conditions are excluded. |
| vitamin | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only | supports | Only the ten vitamin solutes plus water transfer. Parent basal medium, mineral stock, pH and other receiving preparations are excluded. |
| iron-trace-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; components[1] and components[2] only | supports | Exact stock amounts and reagent strengths; parent receiving recipe is not interchangeable. |
| vitamin-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; components[1] only | supports | Exact named vitamin stock; no parent mineral or gas transfer. |
| dep-iron-trace | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; Scoped stock fields, attached evidence, provenance and exclusions | context_only | This is an indirect stock dependency, not another owner or an interchangeable receiving medium. Its receiving dose cannot establish the dose in this target. |
| dep-vitamin | data/normalized_yaml/bacterial/togo_medium_m190.yaml; Scoped stock fields, attached evidence, provenance and exclusions | context_only | This is an indirect stock dependency, not another owner or an interchangeable receiving medium. Its receiving dose cannot establish the dose in this target. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch035/341/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33403 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33403; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33403 resolves to elemental sulfur. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml; data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml", "events": 12, "timestamp_issues": []}] |
| dependency-amount-evidence | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/341/evidence-context-original.json; Scoped M180 iron/trace and M190 vitamin evidence only | supports | {"matched_claims": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[0].composition[0].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[0].composition[0].concentration: Source water batch input: 990 ml = 0.99 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[1]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[0].composition[1].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[0].composition[1].concentration: Source batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[2]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[0].solutions[0].composition[0].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[0].solutions[0].composition[0].concentration: Explicit HCl reagent strength 7.7 M, not a final-medium concentration. The 25% basis is unspecified; the enclosing stock holds the 10 ml batch dose. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[0].solutions[0].composition[0].evidence[1]", "source_key": "jcm187", "raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804", "original_explanation": "solutions[0].solutions[0].composition[0].concentration: Original FeCl2 table corroborates the reagent strength and dose. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=original recipe text; accessed=2026-10-08T13:22:47.560712+00:00; capture SHA256=e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804.", "literal_snippet": "25% HCl (7.7 M) 10.0 ml", "authentication_mode": "exact_extracted_text_substring_and_cited_raw_hash", "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[0].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[0].concentration: Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[0]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[1].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[1].concentration: Source batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[1]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[2].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[2].concentration: Source batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[2]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[3].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[3].concentration: Source batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[3]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[4].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[4].concentration: Source batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[4]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[5].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[5].concentration: Source batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[5]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[6].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[6].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[6]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "$.solutions[1].composition[7].evidence[0]", "source_key": "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba", "original_explanation": "solutions[1].composition[7].concentration: Source batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[7]; accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet": "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[0].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[0].concentration: Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[1].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[1].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[1]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[2].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[2].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[2]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[3].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[3].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[3]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[4].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[4].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[4]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[5].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[5].concentration: Source batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[5]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[6].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[6].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[6]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[7].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[7].concentration: Source batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[7]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[8].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[8].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[8]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[9].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[9].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[9]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[10].evidence[0]", "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "original_explanation": "solutions[1].composition[10].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[10]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\"", "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}], "excluded_parent_claim_count": 52} |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact transferred-component OLS metadata/form | supports | Matching canonical label does not prove source-specific hydrate or stereochemistry. |
| scoped-chemical-metadata | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; data/normalized_yaml/bacterial/togo_medium_m190.yaml; Only solutions[0..1] of M180 and solutions[1] of M190 | context_only | {"CHEBI:15377": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].composition[0].term", "label": "water"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].composition[0].mediaingredientmech_chebi_term", "label": "water"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[0].term", "label": "water"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[0].mediaingredientmech_chebi_term", "label": "water"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[0].term", "label": "water"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[0].mediaingredientmech_chebi_term", "label": "water"}], "CHEBI:86249": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[0].composition[1].term", "label": "iron dichloride tetrahydrate"}], "CHEBI:75213": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[1].term", "label": "sodium molybdate dihydrate"}], "CHEBI:33118": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[2].term", "label": "boric acid"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[2].mediaingredientmech_chebi_term", "label": "boric acid"}], "CHEBI:86368": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[3].term", "label": "manganese(II) chloride tetrahydrate"}], "CHEBI:35696": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[4].term", "label": "cobalt dichloride"}], "CHEBI:34887": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[5].term", "label": "nickel dichloride"}], "CHEBI:86318": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[6].term", "label": "copper(II) chloride dihydrate"}], "CHEBI:49976": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[7].term", "label": "zinc dichloride"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml", "field_path": "solutions[1].composition[7].mediaingredientmech_chebi_term", "label": "zinc dichloride"}], "CHEBI:15956": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[1].term", "label": "biotin"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[1].mediaingredientmech_chebi_term", "label": "biotin"}], "CHEBI:30753": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[2].term", "label": "4-aminobenzoic acid"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[2].mediaingredientmech_chebi_term", "label": "4-aminobenzoic acid"}], "CHEBI:49105": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[3].term", "label": "thiamine hydrochloride"}], "CHEBI:31345": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[4].term", "label": "Calcium pantothenate"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[4].mediaingredientmech_chebi_term", "label": "Calcium pantothenate"}], "CHEBI:30961": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[5].term", "label": "pyridoxine hydrochloride"}], "CHEBI:27470": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[6].term", "label": "folic acid"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[6].mediaingredientmech_chebi_term", "label": "folic acid"}], "CHEBI:176843": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[7].term", "label": "vitamin B12"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[7].mediaingredientmech_chebi_term", "label": "vitamin B12"}], "CHEBI:17015": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[8].term", "label": "riboflavin"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[8].mediaingredientmech_chebi_term", "label": "riboflavin"}], "CHEBI:15940": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[9].term", "label": "nicotinic acid"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[9].mediaingredientmech_chebi_term", "label": "nicotinic acid"}], "CHEBI:16494": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[10].term", "label": "lipoic acid"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[10].mediaingredientmech_chebi_term", "label": "lipoic acid"}]} |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned current catalog/tree exact legacy-key lookup | supports | Current snapshot lacks MediaIngredientMech:001072; this is a completed current lookup, not evidence that the historical mapping was invalid. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned current catalog/tree exact legacy-key lookup | supports | Current snapshot lacks MediaIngredientMech:001072; this is a completed current lookup, not evidence that the historical mapping was invalid. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes primary versus named stock sections and has amount-unit parsing plus conditional water/volume-based stock inference; it cannot make an unstated measured volume explicit. Current migration preserves external medium references as empty compositions when unresolved, and current duplicate cleanup retains conflicting quantities rather than summing them. These current code paths do not establish historical causation; review normalized inputs before any regeneration. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes primary versus named stock sections and has amount-unit parsing plus conditional water/volume-based stock inference; it cannot make an unstated measured volume explicit. Current migration preserves external medium references as empty compositions when unresolved, and current duplicate cleanup retains conflicting quantities rather than summing them. These current code paths do not establish historical causation; review normalized inputs before any regeneration. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes primary versus named stock sections and has amount-unit parsing plus conditional water/volume-based stock inference; it cannot make an unstated measured volume explicit. Current migration preserves external medium references as empty compositions when unresolved, and current duplicate cleanup retains conflicting quantities rather than summing them. These current code paths do not establish historical causation; review normalized inputs before any regeneration. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required historical correspondence of legacy MediaIngredientMech:001072 for sulfur powder remains unavailable. The complete current catalog/tree negative lookup is finished and is not itself an unavailable check or proof of historical invalidity.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191716Z-culturemech-010407-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acidilobus_saccharovorans_medium (CultureMech:010407)'
started_at: '2026-10-21T19:13:51Z'
finished_at: '2026-10-21T19:17:16Z'
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
summary: JCM 934 explicitly delegates to JCM 308 with yeast extract 0.1 g/L final
  and glucose 2 g/L. The local record instead assigns mass-rate units to water, resazurin
  and three stock doses, omits the stock compositions and source preparation, and
  leaves an unresolved historical sulfur linkage. Only the named M180 iron/trace and
  M190 vitamin subsections transfer; their current amount evidence is separately authenticated.
  Historical legacy correspondence remains unavailable.
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
  - path: data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
    sha256: 90051926fa98b3816b408561f4a6e80da376b2032f46fe40b0f5b93e9321eb41
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
    sha256: ba325dde14aa234878571849ca3f063d2be2ec0a5d4c968f7112e06397e7bfaf
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 341; batch 035 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-four task batches
    contain 340 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 343 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010407
targets:
- target_id: CultureMech:010407
  path: data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  label: acidilobus_saccharovorans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/341/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/341/strict.tsv"
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010407
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
  - CultureMech:010407
- check_id: historical-legacy-link
  name: Required source-scope verification
  required: true
  status: unavailable
  summary: Required historical correspondence of legacy MediaIngredientMech:001072
    for sulfur powder remains unavailable. The complete current catalog/tree negative
    lookup is finished and is not itself an unavailable check or proof of historical
    invalidity.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - mimPinnedCatalog
  - mimPinnedTree
  - record
  - owner-0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:11.206051Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/341/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:12.317675Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/341/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:14.170562Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:15.221649Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:17:15Z'
  support: supports
  summary: './data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml:1:id:
    CultureMech:010407

    ./data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml:1:id: CultureMech:010407

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/341/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:17:15Z'
  support: supports
  summary: 49 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a2659c1b6c1742db8f28eac3fda2a9c3d887b62a3a709c1c4510d177515abfd5
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/341/evidence-context-original.json
  locator: Complete frozen source context and full local objects
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Frozen target/owner objects match freshly inspected records. Source interpretations
    are assessed against actual bound capture bytes; historical limitations remain
    separate.
  snapshot_sha256: 2b4c6ceaca0507ec7ce01d4c4e7dfd0ffb6df50c33dca19a163a3cdeaecbaa66
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=934
  locator: Complete exact JCM 934 page
  accessed_at: '2026-10-21T11:01:48.405671Z'
  support: supports
  summary: Explicit yeast 0.1 g/L final is the receiving override, not an additional
    0.1 g on top of the parent 0.3 g; glucose is separately autoclaved.
  snapshot_sha256: b922390e5c9142f021fd5170543dec7732c43e37bcbe466bd9a0172617959036
- evidence_id: basal
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308
  locator: Complete delegated basal table and receiving preparation
  accessed_at: '2026-10-21T10:35:30.491607Z'
  support: supports
  summary: This expressly delegated basal source supplies the main recipe and stages;
    final measured volume is not stated.
  snapshot_sha256: a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980
  locator: meta, components[0], comments[0] and comments[2].comment (paragraph_index
    4)
  accessed_at: '2026-10-21T18:58:50.958420Z'
  support: supports
  summary: Expanded source agrees with the primary override and basal amounts. The
    frozen preparatory context comments[3] locator is corrected here to the actual
    comments[2].
  snapshot_sha256: 320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95
- evidence_id: provider-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J934
  locator: data.medium and data.solutions[0].steps[0]
  accessed_at: '2026-10-21T11:01:45.599625Z'
  support: supports
  summary: This API supplies the same delegation sentence, not an independently expanded
    recipe or measured denominator.
  snapshot_sha256: 9acc2ce86a8248f35253dfb5e9cb3d3814d001df419fb11bda9aec4d752edb00
- evidence_id: iron-trace
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: FeCl2 solution and Trace element solution subsections only
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: Only these stock formulas transfer; JCM 187 basal recipe, vitamins, gas,
    pH and other receiving conditions are excluded.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: vitamin
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Only the ten vitamin solutes plus water transfer. Parent basal medium,
    mineral stock, pH and other receiving preparations are excluded.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: iron-trace-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  locator: components[1] and components[2] only
  accessed_at: '2026-10-21T10:35:28.558157Z'
  support: supports
  summary: Exact stock amounts and reagent strengths; parent receiving recipe is not
    interchangeable.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: vitamin-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: components[1] only
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: Exact named vitamin stock; no parent mineral or gas transfer.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: dep-iron-trace
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: Scoped stock fields, attached evidence, provenance and exclusions
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: This is an indirect stock dependency, not another owner or an interchangeable
    receiving medium. Its receiving dose cannot establish the dose in this target.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dep-vitamin
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: Scoped stock fields, attached evidence, provenance and exclusions
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: This is an indirect stock dependency, not another owner or an interchangeable
    receiving medium. Its receiving dose cannot establish the dose in this target.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/341/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: b9dc93f13aa5614511413338d98ba698b33eb68f7407705599008c6cc9422470
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
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
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
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
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
  accessed_at: '2026-10-21T19:17:15Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type":
    "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id":
    "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836":
    [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836",
    "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml; data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml",
    "events": 12, "timestamp_issues": []}]'
- evidence_id: dependency-amount-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/341/evidence-context-original.json
  locator: Scoped M180 iron/trace and M190 vitamin evidence only
  accessed_at: '2026-10-21T19:17:15Z'
  support: supports
  summary: '{"matched_claims": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[0].composition[0].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[0].composition[0].concentration: Source water
    batch input: 990 ml = 0.99 L. This is not a measured final volume. Prior duplicate-collapse
    notes describe the superseded flattened record. No final-medium volume, percentage
    basis, density or chemical grounding is inferred. Locator=components[1].items[1];
    accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.",
    "literal_snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"",
    "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256":
    "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input":
    "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[0].composition[1].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[0].composition[1].concentration: Source batch
    input: 1.5 g. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[2]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[0].solutions[0].composition[0].evidence[0]", "source_key":
    "togoM180original", "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[0].solutions[0].composition[0].concentration:
    Explicit HCl reagent strength 7.7 M, not a final-medium concentration. The 25%
    basis is unspecified; the enclosing stock holds the 10 ml batch dose. No final-medium
    volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0];
    accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.",
    "literal_snippet": "{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\":
    \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[0].solutions[0].composition[0].evidence[1]", "source_key":
    "jcm187", "raw_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
    "original_explanation": "solutions[0].solutions[0].composition[0].concentration:
    Original FeCl2 table corroborates the reagent strength and dose. No final-medium
    volume, percentage basis, density or chemical grounding is inferred. Locator=original
    recipe text; accessed=2026-10-08T13:22:47.560712+00:00; capture SHA256=e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804.",
    "literal_snippet": "25% HCl (7.7 M) 10.0 ml", "authentication_mode": "exact_extracted_text_substring_and_cited_raw_hash",
    "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[0].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[0].concentration: Source water
    batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse
    notes describe the superseded flattened record. No final-medium volume, percentage
    basis, density or chemical grounding is inferred. Locator=components[2].items[0];
    accessed=2026-10-08T13:22:45.762376+00:00; capture SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.",
    "literal_snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"",
    "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256":
    "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"}, {"input":
    "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[1].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[1].concentration: Source batch
    input: 36 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[1]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[2].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[2].concentration: Source batch
    input: 6 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[2]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[3].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[3].concentration: Source batch
    input: 100 mg. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[3]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[4].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[4].concentration: Source batch
    input: 190 mg. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[4]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[5].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[5].concentration: Source batch
    input: 24 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[5]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[6].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[6].concentration: Source batch
    input: 2 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[6]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "$.solutions[1].composition[7].evidence[0]", "source_key": "togoM180original",
    "raw_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba",
    "original_explanation": "solutions[1].composition[7].concentration: Source batch
    input: 70 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[2].items[7]; accessed=2026-10-08T13:22:45.762376+00:00; capture
    SHA256=a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba.", "literal_snippet":
    "{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "10dfb30304835338c19b715b8269918045d2fcfb8fadd207a9caf6698fe1665b"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[0].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[0].concentration: Source water
    batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse
    notes describe the superseded flattened record. No final-medium volume, percentage
    basis, density or chemical grounding is inferred. Locator=components[1].items[0];
    accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "literal_snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"",
    "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256":
    "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[1].evidence[0]",
    "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[1].concentration: Source batch
    input: 2 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[1]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[2].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[2].concentration: Source batch
    input: 5 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[2]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\"",
    "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256":
    "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[3].evidence[0]",
    "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[3].concentration: Source batch
    input: 5 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[3]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[4].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[4].concentration: Source batch
    input: 5 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[4]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\"",
    "authentication_mode": "exact_raw_substring_and_cited_hash", "parsed_text_sha256":
    "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[5].evidence[0]",
    "source_key": "togoM190original", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[5].concentration: Source batch
    input: 10 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[5]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[6].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[6].concentration: Source batch
    input: 2 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[6]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[7].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[7].concentration: Source batch
    input: 0.1 mg. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[7]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[8].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[8].concentration: Source batch
    input: 5 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[8]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[9].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[9].concentration: Source batch
    input: 5 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[9]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "$.solutions[1].composition[10].evidence[0]", "source_key": "togoM190original",
    "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "original_explanation": "solutions[1].composition[10].concentration: Source batch
    input: 5 mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.
    No final-medium volume, percentage basis, density or chemical grounding is inferred.
    Locator=components[1].items[10]; accessed=2026-10-08T13:22:46.432534+00:00; capture
    SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "literal_snippet":
    "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\"", "authentication_mode":
    "exact_raw_substring_and_cited_hash", "parsed_text_sha256": "288fc01a439a7c12ae0c8421c26c5768888a01c7e983f8242be0d1cc229dafcb"}],
    "excluded_parent_claim_count": 52}'
  snapshot_sha256: 2b4c6ceaca0507ec7ce01d4c4e7dfd0ffb6df50c33dca19a163a3cdeaecbaa66
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi86368
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:17:30.657545Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi86318
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:43:12.592415Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact transferred-component OLS metadata/form
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: Matching canonical label does not prove source-specific hydrate or stereochemistry.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: scoped-chemical-metadata
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml;
    data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: Only solutions[0..1] of M180 and solutions[1] of M190
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: '{"CHEBI:15377": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].composition[0].term", "label": "water"}, {"input":
    "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].composition[0].mediaingredientmech_chebi_term", "label":
    "water"}, {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[0].term", "label": "water"}, {"input":
    "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[0].mediaingredientmech_chebi_term", "label":
    "water"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[0].term", "label": "water"}, {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[0].mediaingredientmech_chebi_term", "label":
    "water"}], "CHEBI:86249": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[0].composition[1].term", "label": "iron dichloride tetrahydrate"}],
    "CHEBI:75213": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[1].term", "label": "sodium molybdate dihydrate"}],
    "CHEBI:33118": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[2].term", "label": "boric acid"}, {"input":
    "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[2].mediaingredientmech_chebi_term", "label":
    "boric acid"}], "CHEBI:86368": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[3].term", "label": "manganese(II) chloride
    tetrahydrate"}], "CHEBI:35696": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[4].term", "label": "cobalt dichloride"}],
    "CHEBI:34887": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[5].term", "label": "nickel dichloride"}],
    "CHEBI:86318": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[6].term", "label": "copper(II) chloride
    dihydrate"}], "CHEBI:49976": [{"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[7].term", "label": "zinc dichloride"},
    {"input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
    "field_path": "solutions[1].composition[7].mediaingredientmech_chebi_term", "label":
    "zinc dichloride"}], "CHEBI:15956": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[1].term", "label": "biotin"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[1].mediaingredientmech_chebi_term",
    "label": "biotin"}], "CHEBI:30753": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[2].term", "label": "4-aminobenzoic acid"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[2].mediaingredientmech_chebi_term", "label": "4-aminobenzoic
    acid"}], "CHEBI:49105": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[3].term", "label": "thiamine hydrochloride"}],
    "CHEBI:31345": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[4].term", "label": "Calcium pantothenate"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[4].mediaingredientmech_chebi_term", "label": "Calcium
    pantothenate"}], "CHEBI:30961": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[5].term", "label": "pyridoxine hydrochloride"}],
    "CHEBI:27470": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[6].term", "label": "folic acid"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[6].mediaingredientmech_chebi_term",
    "label": "folic acid"}], "CHEBI:176843": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[7].term", "label": "vitamin B12"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[7].mediaingredientmech_chebi_term",
    "label": "vitamin B12"}], "CHEBI:17015": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[8].term", "label": "riboflavin"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[8].mediaingredientmech_chebi_term",
    "label": "riboflavin"}], "CHEBI:15940": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[9].term", "label": "nicotinic acid"},
    {"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[9].mediaingredientmech_chebi_term", "label": "nicotinic
    acid"}], "CHEBI:16494": [{"input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "solutions[1].composition[10].term", "label": "lipoic acid"}, {"input":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[10].mediaingredientmech_chebi_term",
    "label": "lipoic acid"}]}'
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned current catalog/tree exact legacy-key lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Current snapshot lacks MediaIngredientMech:001072; this is a completed
    current lookup, not evidence that the historical mapping was invalid.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned current catalog/tree exact legacy-key lookup
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Current snapshot lacks MediaIngredientMech:001072; this is a completed
    current lookup, not evidence that the historical mapping was invalid.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Current importer distinguishes primary versus named stock sections and
    has amount-unit parsing plus conditional water/volume-based stock inference; it
    cannot make an unstated measured volume explicit. Current migration preserves
    external medium references as empty compositions when unresolved, and current
    duplicate cleanup retains conflicting quantities rather than summing them. These
    current code paths do not establish historical causation; review normalized inputs
    before any regeneration.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Current importer distinguishes primary versus named stock sections and
    has amount-unit parsing plus conditional water/volume-based stock inference; it
    cannot make an unstated measured volume explicit. Current migration preserves
    external medium references as empty compositions when unresolved, and current
    duplicate cleanup retains conflicting quantities rather than summing them. These
    current code paths do not establish historical causation; review normalized inputs
    before any regeneration.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:15Z'
  support: context_only
  summary: Current importer distinguishes primary versus named stock sections and
    has amount-unit parsing plus conditional water/volume-based stock inference; it
    cannot make an unstated measured volume explicit. Current migration preserves
    external medium references as empty compositions when unresolved, and current
    duplicate cleanup retains conflicting quantities rather than summing them. These
    current code paths do not establish historical causation; review normalized inputs
    before any regeneration.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 55 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Main: Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1,\n    \
    \  \"source_unit\": \"L\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The source states a volume or milligram batch amount, not the stored gram-per-liter\
    \ value. Restore original units and stage; no assumed final volume.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"Main: CaCl2・2H2O\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.33,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.33,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid\
    \ stocks and separate additions does not establish a measured final liter; preserve\
    \ batch mass instead of asserting an unsupported exact g/L rate.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"Main: KH2PO4\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.33,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.33,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid\
    \ stocks and separate additions does not establish a measured final liter; preserve\
    \ batch mass instead of asserting an unsupported exact g/L rate.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"Main: NH4Cl\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.33,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.33,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid\
    \ stocks and separate additions does not establish a measured final liter; preserve\
    \ batch mass instead of asserting an unsupported exact g/L rate.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q5\",\n    \"component_or_context\": \"Main: Resazurin\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n \
    \       \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 1,\n    \
    \  \"source_unit\": \"mg\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The source states a volume or milligram batch amount, not the stored gram-per-liter\
    \ value. Restore original units and stage; no assumed final volume.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\": \"Main: MgCl2・6H2O\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.33,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.33,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid\
    \ stocks and separate additions does not establish a measured final liter; preserve\
    \ batch mass instead of asserting an unsupported exact g/L rate.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"Main: Na2S・9H2O\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S・9H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.5,\n  \
    \    \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid\
    \ stocks and separate additions does not establish a measured final liter; preserve\
    \ batch mass instead of asserting an unsupported exact g/L rate.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q8\",\n    \"component_or_context\": \"Main: KCl\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.33,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 0.33,\n \
    \     \"source_unit\": \"g\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The numeric mass matches the delegated batch recipe. A 1 L water input plus liquid\
    \ stocks and separate additions does not establish a measured final liter; preserve\
    \ batch mass instead of asserting an unsupported exact g/L rate.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q9\",\n    \"component_or_context\": \"Main: Sulfur (powder)\"\
    ,\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"unsupported\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sulfur (powder)\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\",\n        \"\
    accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"source_amount\": 10,\n      \"source_unit\": \"g\",\n      \"reagent_strength\"\
    : null,\n      \"reagent_strength_unit\": null,\n      \"measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The numeric mass matches the delegated batch\
    \ recipe. A 1 L water input plus liquid stocks and separate additions does not\
    \ establish a measured final liter; preserve batch mass instead of asserting an\
    \ unsupported exact g/L rate.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n  \
    \  \"component_or_context\": \"Main: glucose\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"glucose\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"g/L\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": 2,\n    \
    \  \"source_unit\": \"g/L\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The exact receiving source explicitly gives this g/L rate. The local value matches\
    \ but has no attached claim-level evidence. Yeast 0.1 g/L final overrides the\
    \ delegated parent yeast row; it is not additive.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q11\",\n    \"component_or_context\": \"Main: Yeast extract (BD-Difco)\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 0.1,\\n          \\\"unit\\\": \\\"g/L\\\"\",\n        \"snapshot_sha256\"\
    : \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\",\n    \
    \    \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"source_amount\": 0.1,\n      \"source_unit\"\
    : \"g/L\",\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    The exact receiving source explicitly gives this g/L rate. The local value matches\
    \ but has no attached claim-level evidence. Yeast 0.1 g/L final overrides the\
    \ delegated parent yeast row; it is not additive.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q12\",\n    \"component_or_context\": \"Main: H2SO4\",\n    \"decision\":\
    \ \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n        \"decision\"\
    : \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H2SO4\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"source_amount\": null,\n \
    \     \"source_unit\": null,\n      \"reagent_strength\": 1,\n      \"reagent_strength_unit\"\
    : \"N\",\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\":\
    \ \"No fixed receiving dose is given for the adjustment reagent or gases. VARIABLE\
    \ preserves an unspecified dose but does not capture the separately stated reagent\
    \ strength or preparation gas ratio.\"\n  },\n  {\n    \"quantity_id\": \"q13\"\
    ,\n    \"component_or_context\": \"Main: Carbon dioxide gas\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n        \"decision\"\
    : \"not_quantified\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[15]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Carbon dioxide gas\\\"\",\n        \"snapshot_sha256\"\
    : \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\",\n    \
    \    \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"source_amount\": null,\n      \"\
    source_unit\": null,\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    No fixed receiving dose is given for the adjustment reagent or gases. VARIABLE\
    \ preserves an unspecified dose but does not capture the separately stated reagent\
    \ strength or preparation gas ratio.\"\n  },\n  {\n    \"quantity_id\": \"q14\"\
    ,\n    \"component_or_context\": \"Main: Nitrogen gas\",\n    \"decision\": \"\
    not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[16]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrogen gas\\\"\",\n        \"snapshot_sha256\"\
    : \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\",\n    \
    \    \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"source_amount\": null,\n      \"\
    source_unit\": null,\n      \"reagent_strength\": null,\n      \"reagent_strength_unit\"\
    : null,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"\
    No fixed receiving dose is given for the adjustment reagent or gases. VARIABLE\
    \ preserves an unspecified dose but does not capture the separately stated reagent\
    \ strength or preparation gas ratio.\"\n  },\n  {\n    \"quantity_id\": \"q15\"\
    ,\n    \"component_or_context\": \"Receiving stock dose: FeCl2 solution (see Medium\
    \ [M180])\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2 solution (see Medium [M180])\\\",\\n   \
    \       \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_addition_mL\": 1,\n\
    \      \"stock_subsection_only\": true\n    },\n    \"rationale\": \"The stated\
    \ 1/1/10 mL additions are batch volumes, not g/L. Preserve the separate stock\
    \ preparation and receiving dose without computing an unprovided final-medium\
    \ denominator.\"\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Receiving stock dose: Trace element solution (see Medium [M180])\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n        \"\
    field_path\": \"solutions[1].concentration\",\n        \"stored\": {\n       \
    \   \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"\
    decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M180])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_addition_mL\": 1,\n\
    \      \"stock_subsection_only\": true\n    },\n    \"rationale\": \"The stated\
    \ 1/1/10 mL additions are batch volumes, not g/L. Preserve the separate stock\
    \ preparation and receiving dose without computing an unprovided final-medium\
    \ denominator.\"\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Receiving stock dose: Trace vitamins (see Medium [M190])\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM980original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M980\",\n \
    \       \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"320fef27f5eabdbce6cc9944953d6c446ad92b9e09a0f7cd9e29fb6a63232f95\"\
    ,\n        \"accessed_at\": \"2026-10-21T18:58:50.958420Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"batch_addition_mL\": 10,\n\
    \      \"stock_subsection_only\": true\n    },\n    \"rationale\": \"The stated\
    \ 1/1/10 mL additions are batch volumes, not g/L. Preserve the separate stock\
    \ preparation and receiving dose without computing an unprovided final-medium\
    \ denominator.\"\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Stock 1: 25% HCl (7.7 M)\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].solutions[0].concentration\",\n    \
    \    \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"L\"\n\
    \        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM180original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl (7.7 M)\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 10,\n\
    \      \"unit\": \"ml\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"Stock\
    \ 1: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.99\",\n          \"unit\": \"L\"\
    \n        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM180original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 990,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\",\n        \"\
    accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 990,\n      \"unit\": \"ml\",\n      \"receiving_dose_mL\"\
    : 1,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q20\",\n    \"component_or_context\": \"Stock 1: FeCl2・4H2O\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 1.5 g. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2・4H2O\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 1.5,\n\
    \      \"unit\": \"g\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\": \"Stock\
    \ 2: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM180original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\",\n \
    \       \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 1,\n\
    \      \"unit\": \"L\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\": \"Stock\
    \ 2: Na2MoO4・2H2O\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 36 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\",\n        \"\
    accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 36,\n      \"unit\": \"mg\",\n      \"receiving_dose_mL\"\
    : 1,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q23\",\n    \"component_or_context\": \"Stock 2: H3BO3\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 6 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 6,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\": \"Stock\
    \ 2: MnCl2・4H2O\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 100 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 100,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\": \"Stock\
    \ 2: CoCl2・6H2O\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 190 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 190,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\": \"Stock\
    \ 2: NiCl2・6H2O\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 24 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 24,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\": \"Stock\
    \ 2: CuCl2・2H2O\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 2 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 2,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\": \"Stock\
    \ 2: ZnCl2\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 70 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM180original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 70,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:28.558157Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 70,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 1,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\": \"Stock\
    \ 3: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[0].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"1\",\n          \"unit\": \"L\"\n        },\n        \"decision\"\
    : \"verified\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"togoM190original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 1,\n\
    \      \"unit\": \"L\",\n      \"receiving_dose_mL\": 10,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\": \"Stock\
    \ 3: Biotin\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[1].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 2 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 2,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 10,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\": \"Stock\
    \ 3: p--Aminobenzoic acid\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[2].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\",\n        \"\
    accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 5,\n      \"unit\": \"mg\",\n      \"receiving_dose_mL\"\
    : 10,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q32\",\n    \"component_or_context\": \"Stock 3: Thiamine・HCl\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[3].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\",\n        \"\
    accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 5,\n      \"unit\": \"mg\",\n      \"receiving_dose_mL\"\
    : 10,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q33\",\n    \"component_or_context\": \"Stock 3: Calcium pantothenate\",\n\
    \    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n        \"\
    field_path\": \"solutions[2].composition\",\n        \"stored\": [],\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[4].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\",\n        \"\
    accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 5,\n      \"unit\": \"mg\",\n      \"receiving_dose_mL\"\
    : 10,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q34\",\n    \"component_or_context\": \"Stock 3: Pyridoxine・HCl\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n        \"field_path\"\
    : \"solutions[2].composition\",\n        \"stored\": [],\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[5].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 10 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\",\n        \"\
    accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 10,\n      \"unit\": \"mg\",\n      \"receiving_dose_mL\"\
    : 10,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q35\",\n    \"component_or_context\": \"Stock 3: Folic acid\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[6].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 2 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 2,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 10,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\": \"Stock\
    \ 3: Vitamin B12\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[7].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 0.1 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 0.1,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 10,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\": \"Stock\
    \ 3: Riboflavin\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[8].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 5,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 10,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\": \"Stock\
    \ 3: Nicotinic acid\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[9].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\",\n        \"\
    accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 5,\n      \"unit\": \"mg\",\n      \"receiving_dose_mL\"\
    : 10,\n      \"stock_measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"The receiving stock composition is empty; add this exact subsection with evidence.\
    \ The maintained dependency already preserves this batch amount with attached\
    \ matching raw/hash evidence. Keep the original water input, mass and reagent\
    \ stage; do not divide by an inferred stock or final volume. Preserve source hydrate\
    \ and unresolved chemical specificity separately.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q39\",\n    \"component_or_context\": \"Stock 3: Lipoic acid\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[10].notes\",\n        \"stored\": \"Role: Growth\
    \ factor; Properties: Organic compound, Defined component, Simple component\\\
    n\\nSource batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\",\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM190original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.418127Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 5,\n\
    \      \"unit\": \"mg\",\n      \"receiving_dose_mL\": 10,\n      \"stock_measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"The receiving stock composition is empty;\
    \ add this exact subsection with evidence. The maintained dependency already preserves\
    \ this batch amount with attached matching raw/hash evidence. Keep the original\
    \ water input, mass and reagent stage; do not divide by an inferred stock or final\
    \ volume. Preserve source hydrate and unresolved chemical specificity separately.\"\
    \n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\": \"Iron-stock\
    \ HCl strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].solutions[0].composition[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.7\",\n          \"unit\": \"\
    MOLAR\"\n        },\n        \"decision\": \"verified\"\n      }\n    ],\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock acid row only\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M)\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.362855Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"value\": 7.7,\n      \"unit\"\
    : \"M\"\n    },\n    \"rationale\": \"The source separately states 7.7 M and 25%;\
    \ their equivalence is not derived. No percentage basis or density is inferred.\
    \ The maintained nested reagent already has exact supporting source evidence.\"\
    \n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\": \"Iron-stock\
    \ HCl percentage\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].solutions[0].composition[0].notes\"\
    ,\n        \"stored\": \"Role: Solvating media; Properties: Defined component,\
    \ Inorganic compound, Solution\\n\\nExplicit HCl reagent strength 7.7 M, not a\
    \ final-medium concentration. The 25% basis is unspecified; the enclosing stock\
    \ holds the 10 ml batch dose.\",\n        \"decision\": \"verified\"\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock acid row only\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M)\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.362855Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"value\": 25,\n      \"unit\"\
    : \"percent; basis unspecified\"\n    },\n    \"rationale\": \"The source separately\
    \ states 7.7 M and 25%; their equivalence is not derived. No percentage basis\
    \ or density is inferred. The maintained nested reagent already has exact supporting\
    \ source evidence.\"\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"Yeast reagent strength\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"10% (w/v)\",\n        \"snapshot_sha256\"\
    : \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"value\": 10,\n      \"unit\"\
    : \"PERCENT_W_V\",\n      \"scope\": \"separate yeast extract reagent\"\n    },\n\
    \    \"rationale\": \"This source-specific preparation quantity is absent from\
    \ both layers. Preserve the stated stage, exceptions and sequence; do not convert\
    \ into an incubation optimum or inherit different parent M180/M190 receiving conditions.\"\
    \n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\": \"Sulfide\
    \ reagent strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"5% (w/v)\",\n        \"snapshot_sha256\"\
    : \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"value\": 5,\n      \"unit\"\
    : \"PERCENT_W_V\",\n      \"scope\": \"separate sodium sulfide nonahydrate reagent\"\
    \n    },\n    \"rationale\": \"This source-specific preparation quantity is absent\
    \ from both layers. Preserve the stated stage, exceptions and sequence; do not\
    \ convert into an incubation optimum or inherit different parent M180/M190 receiving\
    \ conditions.\"\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Main gas ratio\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"(80:20)\",\n        \"snapshot_sha256\":\
    \ \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"ratio\": [\n        80,\n\
    \        20\n      ],\n      \"gases\": [\n        \"N2\",\n        \"CO2\"\n\
    \      ],\n      \"basis\": \"not explicitly stated\"\n    },\n    \"rationale\"\
    : \"This source-specific preparation quantity is absent from both layers. Preserve\
    \ the stated stage, exceptions and sequence; do not convert into an incubation\
    \ optimum or inherit different parent M180/M190 receiving conditions.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\": \"Sulfur steaming\
    \ duration\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"3 hr\",\n        \"snapshot_sha256\": \"\
    a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n        \"\
    parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"hours\": 3,\n      \"scope\"\
    : \"each daily steaming\"\n    },\n    \"rationale\": \"This source-specific preparation\
    \ quantity is absent from both layers. Preserve the stated stage, exceptions and\
    \ sequence; do not convert into an incubation optimum or inherit different parent\
    \ M180/M190 receiving conditions.\"\n  },\n  {\n    \"quantity_id\": \"q46\",\n\
    \    \"component_or_context\": \"Sulfur steaming repetitions\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"3 successive days\",\n        \"snapshot_sha256\"\
    : \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"successive_days\": 3\n   \
    \ },\n    \"rationale\": \"This source-specific preparation quantity is absent\
    \ from both layers. Preserve the stated stage, exceptions and sequence; do not\
    \ convert into an incubation optimum or inherit different parent M180/M190 receiving\
    \ conditions.\"\n  },\n  {\n    \"quantity_id\": \"q47\",\n    \"component_or_context\"\
    : \"Receiving pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"3.5 - 3.8\",\n        \"snapshot_sha256\"\
    : \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pH_range\": [\n        3.5,\n\
    \        3.8\n      ],\n      \"stage\": \"before inoculation\"\n    },\n    \"\
    rationale\": \"This source-specific preparation quantity is absent from both layers.\
    \ Preserve the stated stage, exceptions and sequence; do not convert into an incubation\
    \ optimum or inherit different parent M180/M190 receiving conditions.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q48\",\n    \"component_or_context\": \"Acid reagent\
    \ strength\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"1 N H 2 SO 4\",\n        \"snapshot_sha256\"\
    : \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"strength\": 1,\n      \"unit\"\
    : \"N\",\n      \"dose\": \"not quantified\"\n    },\n    \"rationale\": \"This\
    \ source-specific preparation quantity is absent from both layers. Preserve the\
    \ stated stage, exceptions and sequence; do not convert into an incubation optimum\
    \ or inherit different parent M180/M190 receiving conditions.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q49\",\n    \"component_or_context\": \"Post-inoculation\
    \ pressure\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"100 kPa\",\n        \"snapshot_sha256\":\
    \ \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"pressure_kPa\": 100,\n   \
    \   \"gases\": \"N2:CO2 80:20\",\n      \"gauge_or_absolute\": \"not stated\"\
    ,\n      \"stage\": \"inoculated bottle\"\n    },\n    \"rationale\": \"This source-specific\
    \ preparation quantity is absent from both layers. Preserve the stated stage,\
    \ exceptions and sequence; do not convert into an incubation optimum or inherit\
    \ different parent M180/M190 receiving conditions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q50\",\n    \"component_or_context\": \"JCM default temperature\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"\
    add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"121°C\",\n        \"snapshot_sha256\": \"\
    a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n        \"\
    parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"temperature_C\": 121\n   \
    \ },\n    \"rationale\": \"This source-specific preparation quantity is absent\
    \ from both layers. Preserve the stated stage, exceptions and sequence; do not\
    \ convert into an incubation optimum or inherit different parent M180/M190 receiving\
    \ conditions.\"\n  },\n  {\n    \"quantity_id\": \"q51\",\n    \"component_or_context\"\
    : \"JCM default duration\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\"\
    ,\n        \"source_locator\": \"Delegated basal preparation or exact page default\"\
    ,\n        \"exact_source_quote\": \"15 min.\",\n        \"snapshot_sha256\":\
    \ \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\",\n    \
    \    \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"minutes\": 15\n    },\n  \
    \  \"rationale\": \"This source-specific preparation quantity is absent from both\
    \ layers. Preserve the stated stage, exceptions and sequence; do not convert into\
    \ an incubation optimum or inherit different parent M180/M190 receiving conditions.\"\
    \n  },\n  {\n    \"quantity_id\": \"q52\",\n    \"component_or_context\": \"Main\
    \ final volume\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm308\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=308\",\n        \"source_locator\"\
    : \"Relevant main or explicitly transferred stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"a350204f40d466c8fd6129a9aa9b56ccc85659130e726c84574d4d24673c5a8c\"\
    ,\n        \"parsed_text_sha256\": \"fbaeda57b6805bd116b4f09a68dba40c5e705ec519d69809c4763cd4788a7207\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.491607Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"listed_water_L\": 1,\n   \
    \   \"listed_water_plus_three_stocks_mL\": 1012,\n      \"measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"Listed liquid arithmetic is not a measured\
    \ final-volume declaration. Keep mass and volume batch amounts; do not silently\
    \ normalize stock or main components to an assumed final liter.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q53\",\n    \"component_or_context\": \"Iron stock final\
    \ volume\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm187\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\",\n        \"source_locator\"\
    : \"Relevant main or explicitly transferred stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.362855Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"water_mL\": 990,\n      \"\
    acid_mL\": 10,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\"\
    : \"Listed liquid arithmetic is not a measured final-volume declaration. Keep\
    \ mass and volume batch amounts; do not silently normalize stock or main components\
    \ to an assumed final liter.\"\n  },\n  {\n    \"quantity_id\": \"q54\",\n   \
    \ \"component_or_context\": \"Trace stock final volume\",\n    \"decision\": \"\
    not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm187\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\",\n        \"source_locator\"\
    : \"Relevant main or explicitly transferred stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    ,\n        \"accessed_at\": \"2026-10-21T10:35:30.362855Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"water_L\": 1,\n      \"measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"Listed liquid arithmetic is not a measured\
    \ final-volume declaration. Keep mass and volume batch amounts; do not silently\
    \ normalize stock or main components to an assumed final liter.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q55\",\n    \"component_or_context\": \"Vitamin stock\
    \ final volume\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"FeCl2 solution (see Medium [M180])\",\n   \
    \         \"composition\": [],\n            \"notes\": \"Cross-reference to Medium\
    \ M180\",\n            \"concentration\": {\n              \"value\": \"1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"name\": \"\
    Unknown solution\"\n          },\n          {\n            \"preferred_term\"\
    : \"Trace element solution (see Medium [M180])\",\n            \"composition\"\
    : [],\n            \"notes\": \"Cross-reference to Medium M180\",\n          \
    \  \"concentration\": {\n              \"value\": \"1\",\n              \"unit\"\
    : \"G_PER_L\"\n            },\n            \"name\": \"Unknown solution\"\n  \
    \        },\n          {\n            \"preferred_term\": \"Trace vitamins (see\
    \ Medium [M190])\",\n            \"composition\": [],\n            \"notes\":\
    \ \"Cross-reference to Medium M190\",\n            \"concentration\": {\n    \
    \          \"value\": \"10\",\n              \"unit\": \"G_PER_L\"\n         \
    \   },\n            \"name\": \"Unknown solution\"\n          }\n        ],\n\
    \        \"decision\": \"not_quantified\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"Relevant main or explicitly transferred stock water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    ,\n        \"accessed_at\": \"2026-10-20T06:58:05.867253Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"water_L\": 1,\n      \"measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"Listed liquid arithmetic is not a measured\
    \ final-volume declaration. Keep mass and volume batch amounts; do not silently\
    \ normalize stock or main components to an assumed final liter.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '13 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 13/14
    primary and 7/14 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding. Historical sulfur linkage remains unresolved
    separately; current CHEBI-based lookup does not authenticate it.'
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi16526
  - chebi17234
  - chebi17997
  - chebi26836
  - chebi31206
  - chebi32588
  - chebi33403
  - chebi63036
  - chebi76209
  - chebi86158
  - chebi86345
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 14: primary 92.86%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: forms
  area: grounding
  topic: Supplied forms and indirect stock specificity
  outcome: concern
  summary: All main asserted CHEBI labels match; elemental sulfur does not contradict
    powder form. M180 trace cobalt/nickel hexahydrate names instead map to anhydrous
    CHEBI:35696/34887. M190 calcium pantothenate is unqualified while CHEBI:31345
    encodes D stereochemistry; this is unsupported specificity, not proof that a D
    product is false. Other explicitly hydrated main/stock constituents agree at the
    stated formula level. Undefined yeast extract has no fabricated pure-chemical
    ID.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - owner-0
  - scoped-chemical-metadata
  - iron-trace
  - vitamin
  - chebi35696
  - chebi34887
  - chebi31345
  - chebi33403
- assessment_id: identity
  area: identity
  topic: Exact receiving accession and delegated stock scope
  outcome: supported
  summary: CultureMech:010407 has one exact maintained archaea owner and identifies
    TOGO M980/JCM 934. JCM 934 expressly delegates to JCM 308. Only FeCl2/trace stocks
    from M180/JCM 187 and trace vitamins from M190/JCM 197 transfer. No organism growth,
    taxonomy or whole-parent equivalence follows from the title or references.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - basal
  - provider
  - provider-api
- assessment_id: preparation
  area: completeness
  topic: Absent source-specific preparation and conditions
  outcome: concern
  summary: Both layers omit the delegated exclusions and staged autoclaving, separate
    10% w/v yeast/5% w/v sulfide reagents, sulfur steaming, vitamin filtration, pH
    range/acid strength and post-inoculation pressure. JCM 934 additionally requires
    glucose separately autoclaved. Keep the source N2 versus N2:CO2 stage distinction,
    unknown pressure basis and exact sulfur repetitions; no M180/M190 parent conditions
    transfer.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - primary
  - basal
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Composition, application and growth assertions
  outcome: supported
  summary: COMPLEX/SEMI_DEFINED and LIQUID are compatible with the salts, defined
    additions and undefined yeast extract. The generic microbial-cultivation application
    is not a strain-specific growth assertion. No target organism, growth performance,
    optimum, incubation temperature or additional taxonomy identifier is inferred
    from the title. Source physical preparation and supplied forms remain separately
    qualified.
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - owner-0
  - primary
  - basal
- assessment_id: provenance
  area: provenance
  topic: Claim-level evidence and source ownership
  outcome: concern
  summary: 'The target and sole owner have source URLs/history but no attached amount
    evidence. Twenty-three transferred dependency evidence objects are independently
    reauthenticated: 22 exact raw snippets and one exact JCM extracted-text excerpt,
    each with the cited raw hash; their historical timestamps remain distinct from
    later identical capture times. Fifty-two unrelated parent evidence objects are
    excluded. Preserve the later dependency repairs and all history; fix the receiving
    owner without overwriting parent recipes.'
  target_ids:
  - CultureMech:010407
  evidence_ids:
  - record
  - owner-0
  - dependency-amount-evidence
  - dep-iron-trace
  - dep-vitamin
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: culturemech.010407.units-and-stock-boundaries
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Water, indicator and stock doses have incorrect units and missing scope
  description: Water 1 L is stored as 1 G_PER_L, resazurin 1 mg as 1 G_PER_L, and
    three 1/1/10 mL stock doses as G_PER_L with empty compositions. Other delegated
    masses lack a measured final-volume basis; yeast and glucose alone have explicit
    receiving g/L statements.
  target_ids:
  - CultureMech:010407
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - basal
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
  issue_key: culturemech.010407.preparation-omission
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact staged preparation is absent
  description: The record omits materially different sterilization/addition stages,
    sulfur treatment and pre-/post-inoculation conditions from its explicitly delegated
    source.
  target_ids:
  - CultureMech:010407
  field_paths:
  - preparation_steps
  - ph_range
  evidence_ids:
  - primary
  - basal
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: Native P3.5 is elevated to major because the absent distinctions
    materially change the stated receiving preparation; this is a record-specific
    completeness impact.
- finding_id: f3
  issue_key: culturemech.010407.indirect-stock-form-conflicts
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Referenced trace stock contains hydrate mismatches
  description: The explicitly transferred M180 trace stock maps CoCl2·6H2O and NiCl2·6H2O
    to anhydrous cobalt/nickel dichloride IDs. Matching labels do not establish exact
    source form.
  target_ids:
  - CultureMech:010407
  field_paths:
  - solutions[1]
  evidence_ids:
  - dep-iron-trace
  - iron-trace
  - chebi35696
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
  issue_key: culturemech.010407.legacy-and-vitamin-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Historical sulfur linkage and vitamin stereochemistry need qualification
  description: Legacy sulfur ID correspondence is not recoverable from the current
    pinned catalog, while the transferred calcium-pantothenate source does not establish
    the D specificity encoded in its current term. Neither uncertainty proves the
    source ingredient is false.
  target_ids:
  - CultureMech:010407
  field_paths:
  - ingredients[8].mediaingredientmech_term
  - solutions[2]
  evidence_ids:
  - mimPinnedCatalog
  - mimPinnedTree
  - dep-vitamin
  - vitamin
  - chebi31345
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
  description: Correct the maintained owner units and represent exact stock subsections/doses,
    with batch masses where final volume is unspecified. Keep yeast 0.1 g/L final
    and glucose 2 g/L with claim-level evidence; do not add the parent yeast amount.
    Regenerate only after maintaining source scope.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
  description: Add the source-specific preparation with literal evidence and exact
    stage boundaries, including glucose treatment, separate stock strengths, sulfur
    repetitions, pH and pressure limits. Do not substitute the referenced parents’
    receiving conditions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
  description: Resolve exact supplied-form identifiers within M180 solutions[1].composition[4].term
    and [5].term before stock transfer. Preserve amount evidence and unrelated parent
    content; do not invent replacement IDs.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
  description: Seek exact historical sulfur mapping provenance and supplier/form evidence
    for the transferred pantothenate. Until resolved, document the limits without
    changing sulfur identity, guessing a replacement key or asserting a different
    stereoisomer.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010407
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M980_Acidilobus_Saccharovorans_Medium.yaml
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
- Required historical correspondence of legacy MediaIngredientMech:001072 for sulfur
  powder remains unavailable. The complete current catalog/tree negative lookup is
  finished and is not itself an unavailable check or proof of historical invalidity.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-035
- generated-medium
```
