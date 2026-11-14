# Source and formulation review: aquifex_medium (CultureMech:009054)

- Review: 20261021T165957Z-culturemech-009054-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:49:34Z
- Finished UTC: 2026-10-21T16:59:57Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M247 and exact JCM 255 agree on the Aquifex source recipe. Water, milligram inputs and two 10 mL stock doses are mislabeled as g/L; both stock compositions are empty and gas/preparation stages are absent. Complete scoped mineral and vitamin sources are available. Current chemical labels resolve, while parent-stock identities and historical evidence must remain restricted to the explicitly transferred subsections.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 294; batch 030 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-nine task batches contain 290 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 293 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009054 | data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml | generated | aquifex_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009054 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009054 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch030/294/strict.tsv |
| validate-terms | passed | True | CultureMech:009054 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009054 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009054 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ255api | unavailable | False | CultureMech:009054 | Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source material is independently available; this optional failure does not make the required primary comparison unavailable. |
| Exact source content access: mediadiveJ255api_retry | unavailable | False | CultureMech:009054 | Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source material is independently available; this optional failure does not make the required primary comparison unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009054.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009054.

49 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Distilled water main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 1,
      "source_unit": "L",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. One liter of input water is not 1 g/L.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "MgSO4・7H2O main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 7,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 7,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "NaCl main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 30,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 30,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "CaCl2・2H2O main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.5,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "NH4Cl main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.15,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "K2HPO4 main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.15,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "MgCl2・6H2O main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 5.5,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 5.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "KCl main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.65",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.65",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.65,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.65,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "NaHCO3 main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 2,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Na2WO4・2H2O main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.1,
      "source_unit": "mg",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The source amount is milligrams, not grams per liter; no final-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "NaBr main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.1,
      "source_unit": "g",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The number matches the source mass, but a final-volume denominator and attached claim evidence are absent.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"NaBr\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "(NH4)2Ni(SO4)2・6H2O main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 20,
      "source_unit": "mg",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The source amount is milligrams, not grams per liter; no final-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"(NH4)2Ni(SO4)2・6H2O\",\n          \"volume\": 20,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Na2SeO4 main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount": 0.1,
      "source_unit": "mg",
      "finished_medium_volume_ml": null
    },
    "rationale": "Restore the literal source batch amount and unit. The source amount is milligrams, not grams per liter; no final-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"Na2SeO4\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Trace minerals (see Medium [M142]) receiving dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 10,
      "source_reference": "JCM 151 mineral subsection",
      "final_medium_denominator": null
    },
    "rationale": "A stock volume is stored as a mass concentration. Restore the ten-milliliter receiving amount, resolve only the named stock subsection and preserve the separate one-liter main water input.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Trace vitamins (see Medium [M190]) receiving dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 10,
      "source_reference": "JCM 197 vitamin subsection",
      "final_medium_denominator": null
    },
    "rationale": "A stock volume is stored as a mass concentration. Restore the ten-milliliter receiving amount, resolve only the named stock subsection and preserve the separate one-liter main water input.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Carbon dioxide gas staged gas context",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "initial_H2_CO2_volume_ratio": [
        4,
        1
      ],
      "replacement_H2_CO2_O2_volume_ratio": [
        79,
        20,
        1
      ],
      "absolute_gas_amount": null
    },
    "rationale": "The provider item itself has no bulk amount. Replace the loss of source-stage information in variable gas placeholders with the exact mixture context, not an invented mass concentration or absolute gas dose.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Adjust pH to 6.0. Sterilize by filtration. Aseptically dispense the medium into culture vessels (e.g., 20 ml medium in 120 ml serum bottles) under a stream of H2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Replace the gas phase with a H2--CO2--O2 (79:20:1, v/v) gas mixture and pressurize to 200 kPa with the same gas mixture. Readjust pH to 5.5--6.0, if necessary.",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Oxygen gas staged gas context",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "initial_H2_CO2_volume_ratio": [
        4,
        1
      ],
      "replacement_H2_CO2_O2_volume_ratio": [
        79,
        20,
        1
      ],
      "absolute_gas_amount": null
    },
    "rationale": "The provider item itself has no bulk amount. Replace the loss of source-stage information in variable gas placeholders with the exact mixture context, not an invented mass concentration or absolute gas dose.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Adjust pH to 6.0. Sterilize by filtration. Aseptically dispense the medium into culture vessels (e.g., 20 ml medium in 120 ml serum bottles) under a stream of H2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Replace the gas phase with a H2--CO2--O2 (79:20:1, v/v) gas mixture and pressurize to 200 kPa with the same gas mixture. Readjust pH to 5.5--6.0, if necessary.",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Hydrogen gas staged gas context",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "initial_H2_CO2_volume_ratio": [
        4,
        1
      ],
      "replacement_H2_CO2_O2_volume_ratio": [
        79,
        20,
        1
      ],
      "absolute_gas_amount": null
    },
    "rationale": "The provider item itself has no bulk amount. Replace the loss of source-stage information in variable gas placeholders with the exact mixture context, not an invented mass concentration or absolute gas dose.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Adjust pH to 6.0. Sterilize by filtration. Aseptically dispense the medium into culture vessels (e.g., 20 ml medium in 120 ml serum bottles) under a stream of H2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Replace the gas phase with a H2--CO2--O2 (79:20:1, v/v) gas mixture and pressurize to 200 kPa with the same gas mixture. Readjust pH to 5.5--6.0, if necessary.",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "JCM 151 Trace minerals: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "Distilled water",
      "batch_amount": 1,
      "source_unit": "L",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "JCM 151 Trace minerals: MgSO4・7H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "MgSO4・7H2O",
      "batch_amount": 3,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "JCM 151 Trace minerals: NaCl",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "NaCl",
      "batch_amount": 1,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "JCM 151 Trace minerals: CaCl2・2H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[3].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[3].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "CaCl2・2H2O",
      "batch_amount": 0.1,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "JCM 151 Trace minerals: Na2MoO4・2H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[4].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[4].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "Na2MoO4・2H2O",
      "batch_amount": 0.01,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "JCM 151 Trace minerals: H3BO3",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[5].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "H3BO3",
      "batch_amount": 0.01,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "JCM 151 Trace minerals: FeSO4・7H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[6].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[6].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "FeSO4・7H2O",
      "batch_amount": 0.1,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "JCM 151 Trace minerals: ZnSO4・7H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[7].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "ZnSO4・7H2O",
      "batch_amount": 0.1,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "JCM 151 Trace minerals: CuSO4・5H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[8].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[8].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "CuSO4・5H2O",
      "batch_amount": 0.01,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[8]",
        "exact_source_quote": "\"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "JCM 151 Trace minerals: CoSO4・7H2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[9].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[9].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "CoSO4・7H2O",
      "batch_amount": 0.1,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[9]",
        "exact_source_quote": "\"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "JCM 151 Trace minerals: Nitrilotriacetic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[10].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[10].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "Nitrilotriacetic acid",
      "batch_amount": 1.5,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[10]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "JCM 151 Trace minerals: MnSO4・xH2O",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[11].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[11].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "MnSO4・xH2O",
      "batch_amount": 0.5,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred. Preserve x-hydrate wording; a parent anhydrous term cannot establish a hydration number.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[11]",
        "exact_source_quote": "\"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "JCM 151 Trace minerals: AlK(SO4)2",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[12].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[12].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "AlK(SO4)2",
      "batch_amount": 0.01,
      "source_unit": "g",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[12]",
        "exact_source_quote": "\"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "JCM 151 Trace minerals: KOH solution",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].composition[13].concentration",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].composition[13].concentration",
        "stored": null,
        "decision": "not_quantified"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 151 Trace minerals",
      "ingredient": "KOH solution",
      "batch_amount": null,
      "source_unit": null,
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "KOH is a titration reagent with no fixed source amount; preserve the ordered pH adjustment without inventing a dose.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.components[2].items[13]",
        "exact_source_quote": "\"component_name\": \"KOH solution\"",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "JCM 197 Trace vitamins: Distilled water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Distilled water",
      "batch_amount": 1,
      "source_unit": "L",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "JCM 197 Trace vitamins: Biotin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[1].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Biotin",
      "batch_amount": 2,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "JCM 197 Trace vitamins: p--Aminobenzoic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[2].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "p--Aminobenzoic acid",
      "batch_amount": 5,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "JCM 197 Trace vitamins: Thiamine・HCl",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[3].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Thiamine・HCl",
      "batch_amount": 5,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "JCM 197 Trace vitamins: Calcium pantothenate",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[4].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Calcium pantothenate",
      "batch_amount": 5,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred. Generic source calcium pantothenate does not establish the parent D-specific identifier.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "JCM 197 Trace vitamins: Pyridoxine・HCl",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[5].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Pyridoxine・HCl",
      "batch_amount": 10,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "JCM 197 Trace vitamins: Folic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[6].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Folic acid",
      "batch_amount": 2,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "JCM 197 Trace vitamins: Vitamin B12",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[7].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[7].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Vitamin B12",
      "batch_amount": 0.1,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "JCM 197 Trace vitamins: Riboflavin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[8].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[8].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Riboflavin",
      "batch_amount": 5,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "JCM 197 Trace vitamins: Nicotinic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[9].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[9].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Nicotinic acid",
      "batch_amount": 5,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "JCM 197 Trace vitamins: Lipoic acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[1].composition[10].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[1].composition[10].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "source_stock": "JCM 197 Trace vitamins",
      "ingredient": "Lipoic acid",
      "batch_amount": 5,
      "source_unit": "mg",
      "receiving_dose_ml": 10,
      "finished_stock_volume_ml": null,
      "final_medium_concentration": null
    },
    "rationale": "Recover this exact source-only component into the currently empty stock composition. Source water is an input amount; no finished stock volume or final-medium dilution is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Initial main pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "initial_pH": 6
    },
    "rationale": "Restore this precisely scoped source statement. The vessel quantities are examples, the pressure convention is unstated, and the final pH adjustment is conditional. These are not independent growth/optimization claims.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Adjust pH to 6.0.",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q45",
    "component_or_context": "Illustrative vessel and medium amounts",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "example_medium_ml": 20,
      "example_vessel_ml": 120,
      "mandatory_recipe_scale": false
    },
    "rationale": "Restore this precisely scoped source statement. The vessel quantities are examples, the pressure convention is unstated, and the final pH adjustment is conditional. These are not independent growth/optimization claims.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "20 ml medium in 120 ml serum bottles",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q46",
    "component_or_context": "Replacement gas pressure",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "pressure_kPa": 200,
      "gauge_or_absolute": null,
      "stage": "Replacement 79:20:1 v/v gas mixture"
    },
    "rationale": "Restore this precisely scoped source statement. The vessel quantities are examples, the pressure convention is unstated, and the final pH adjustment is conditional. These are not independent growth/optimization claims.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "pressurize to 200 kPa with the same gas mixture",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q47",
    "component_or_context": "Conditional readjusted pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "pH_range": [
        5.5,
        6
      ],
      "conditional": true
    },
    "rationale": "Restore this precisely scoped source statement. The vessel quantities are examples, the pressure convention is unstated, and the final pH adjustment is conditional. These are not independent growth/optimization claims.",
    "source_snippets": [
      {
        "source_key": "togoM247",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Readjust pH to 5.5--6.0, if necessary.",
        "snapshot_sha256": "897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc",
        "parsed_text_sha256": "1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2",
        "accessed_at": "2026-10-21T16:33:42.538979Z"
      }
    ]
  },
  {
    "quantity_id": "q48",
    "component_or_context": "Chelator-first trace adjustment",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "Dissolve nitrilotriacetic acid first",
      "pH": 6.5,
      "reagent": "KOH",
      "quantity": null
    },
    "rationale": "Preserve the exact order: chelator dissolution, KOH adjustment, mineral addition, then final pH. The unrelated JCM 197 trace-mineral 1 N KOH statement is outside scope.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
        "parsed_text_sha256": "2cfd46cc453b6c97030970fc0d8811706dd2ddb6f98306357e8a9727d09241ba",
        "accessed_at": "2026-10-21T09:28:25.414106Z"
      }
    ]
  },
  {
    "quantity_id": "q49",
    "component_or_context": "Final trace-stock pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "After mineral addition",
      "pH": 7
    },
    "rationale": "Preserve the exact order: chelator dissolution, KOH adjustment, mineral addition, then final pH. The unrelated JCM 197 trace-mineral 1 N KOH statement is outside scope.",
    "source_snippets": [
      {
        "source_key": "togoM142",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.",
        "snapshot_sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
        "parsed_text_sha256": "2cfd46cc453b6c97030970fc0d8811706dd2ddb6f98306357e8a9727d09241ba",
        "accessed_at": "2026-10-21T09:28:25.414106Z"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:009054.

15 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 15/16 primary and 8/16 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 16: primary 93.75%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009054.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accession, dependency and owner identity

identity: supported. Targets: CultureMech:009054.

The one maintained owner and generated target share stable ID CultureMech:009054 and TOGO M247/JCM 255. M142 resolves to the named JCM 151 mineral stock; M190 resolves to JCM 197 vitamins. These are scoped dependencies, not additional recipes merged into this target.

### Scoped dependency forms and preserved historical evidence

grounding: concern. Targets: CultureMech:009054.

All asserted target/owner primary labels and current CHEBI secondary keys resolve. The mineral dependency includes MnSO4·xH2O, while its parent mapping cannot resolve x; parent calcium-pantothenate stereochemistry is not established by the generic vitamin name. Preserve supplied forms without copying over-specific parent mappings blindly. Existing in-scope amount snippets match exact captured bytes and hashes, but parent main-recipe evidence and legacy IDs do not transfer.

### Explicit filtration, gas stages and stock adjustments

completeness: concern. Targets: CultureMech:009054.

Local layers omit the complete preparation context. JCM 255 explicitly specifies filtration, so its generic autoclave cycle is inapplicable to the main recipe. Preserve source pH stages, example vessel scope, gas ratios and pressure convention limit; preserve trace chelator-first ordering. Do not import unrelated parent-medium operations or infer growth.

### Mixture classification and application scope

scope: concern. Targets: CultureMech:009054.

The resolved formulation comprises named chemicals and defined trace/vitamin constituents rather than yeast extract or peptone. COMPLEX/UNDEFINED should be re-evaluated against those exact constituents; hydrate/form uncertainty should be explicit rather than misclassified as an undefined extract. LIQUID is supported. No taxonomy, nutrient-role mechanism or growth claim is inferred from the title or generic application.

### Current writers and follow-up ownership

provenance: concern. Targets: CultureMech:009054.

Current TOGO code contains explicit unit handling and stock/reference logic, unlike these persisted placeholders; the snapshot is not historical-writer proof. Source dependency notes and current cleanup behavior do not authorize whole-parent transplantation. Correct the maintained M247 owner, preserve historical events and regenerate afterward.

## Findings

### f1: Volume and milligram inputs are stored as grams per liter

blocker / open / confirmed; issue key: culturemech.009054.amount-units.

Both layers store water 1 g/L, ammonium nickel sulfate 20 g/L, tungstate and selenate 0.1 g/L, and both ten-milliliter stocks as 10 g/L. These disagree with explicit source units; other gram amounts also lack an independently established final-volume basis.

### f2: Two source-resolvable stock nodes remain empty placeholders

major / open / confirmed; issue key: culturemech.009054.empty-stock-scope.

Both stocks have empty composition and Unknown solution names despite explicit source cross-references. Complete mineral and vitamin subsections are available, including their waters and unquantified KOH context.

### f3: Variable gases omit explicit staged source conditions

major / open / confirmed; issue key: culturemech.009054.preparation-context.

Generic variable gas entries lose the two source mixture ratios and the associated preparation stages. Main filtration and pH context, example vessel amounts, pressure limit and mineral-stock ordering are absent.

### f4: Classification does not reflect the resolved chemical formulation

minor / open / confirmed; issue key: culturemech.009054.composition-category.

COMPLEX/UNDEFINED is unsupported by the named salt/trace/vitamin formulation. Parent yeast extract and peptone are outside the transferred stock sections and cannot support that classification.

## Recommended Actions And Acceptance Checks

### a1

Restore every literal source amount/unit with exact evidence, separating batch inputs from stock addition volumes and final concentrations. Preserve water as a volume input and do not assume measured final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Populate or resolve only the named subsections with source-bound composition evidence. Preserve later dependency amount evidence and form caveats; exclude all unrelated parent recipes and legacy identifiers.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach scoped source preparation and gas-stage evidence, preserving the example/conditional qualifiers and unstated pressure convention. Filtration overrides the main generic autoclave default; do not invent a cycle or borrow other parent procedures.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reassess composition category after resolving exact stock constituents and retain any form uncertainty explicitly. Do not infer growth targets from the medium name.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch030/294/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch030/294/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml:1:id: CultureMech:009054<br>./data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml:1:id: CultureMech:009054<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch030/source-preflight-bound/294/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 63 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch030/source-preflight-bound/294/evidence-context-original.json; Whole target, all maintained owners and scoped dependencies | context_only | All frozen local-record objects match fresh inspected YAML. Source interpretations are separately checked against actual bound raw/text bytes. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247; $.meta, $.components[0], $.comments[0] | supports | Exact provider names JCM 255 and supplies the original amounts, two referenced stock doses and preparation paragraph. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=255; Medium 255 entire recipe and its explicit preparation paragraph | supports | Primary agrees with provider. Explicit filtration overrides the generic JCM autoclave default; source example vessels, gas-stage ratios, pressure and conditional pH are documentary source context, not experimentally verified growth claims. |
| trace-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Trace minerals subsection and its immediate preparation only | supports | Transfer twelve mineral/chelator solutes, input water and the nitrilotriacetic-acid/KOH sequence only. The parent salt-base solution, main medium, sulfur, organism and other procedures do not transfer. |
| vitamin-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only | supports | Transfer ten vitamin solutes and water only. Parent main-medium sulfide, reductants, mineral solution and its 1 N KOH instruction are outside the referenced vitamin scope. |
| trace-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2]; $.comments[1] | supports | Exact scoped mineral counterpart, including unquantified KOH and ordered pH adjustments. |
| vitamin-provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1] | supports | Exact vitamin counterpart; no legacy identifier or unrelated parent evidence transfers merely because it appears elsewhere in this record. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch030/294/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:18276 resolves to dihydrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63004 resolves to sodium bromide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:77775 resolves to sodium selenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label": "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:77775": [{"label": "Na2SeO4", "match_type": "preferred_term", "identifier": "CHEBI:77775", "preferred_term": "Na2SeO4", "ontology_id": "CHEBI:77775", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| dependency-evidence | /private/tmp/culturemech-review-work-batch030/source-preflight-bound/294/evidence-context-original.json; existing_owner_evidence_recheck, transferred trace/vitamin sections only | supports | {"in_scope": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[0].evidence[0]", "snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"", "explanation": "solutions[1].composition[0].concentration: Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[0]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[1].evidence[0]", "snippet": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\"", "explanation": "solutions[1].composition[1].concentration: Source batch input: 3 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[1]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[2].evidence[0]", "snippet": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\"", "explanation": "solutions[1].composition[2].concentration: Source batch input: 1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[2]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[3].evidence[0]", "snippet": "{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\"", "explanation": "solutions[1].composition[3].concentration: Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[3]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[4].evidence[0]", "snippet": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\"", "explanation": "solutions[1].composition[4].concentration: Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[4]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[5].evidence[0]", "snippet": "{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\"", "explanation": "solutions[1].composition[5].concentration: Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[5]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[6].evidence[0]", "snippet": "{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\"", "explanation": "solutions[1].composition[6].concentration: Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[6]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[7].evidence[0]", "snippet": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\"", "explanation": "solutions[1].composition[7].concentration: Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[7]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[8].evidence[0]", "snippet": "{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\"", "explanation": "solutions[1].composition[8].concentration: Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[8]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[9].evidence[0]", "snippet": "{\n          \"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001050\"", "explanation": "solutions[1].composition[9].concentration: Source batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[9]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[10].evidence[0]", "snippet": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\"", "explanation": "solutions[1].composition[10].concentration: Source batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[10]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[11].evidence[0]", "snippet": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\"", "explanation": "solutions[1].composition[11].concentration: Source batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[11]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml", "field_path": "$.solutions[1].composition[12].evidence[0]", "snippet": "{\n          \"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\"", "explanation": "solutions[1].composition[12].concentration: Source batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[12]; accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.", "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33", "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[0].evidence[0]", "snippet": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\"", "explanation": "solutions[1].composition[0].concentration: Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[1].evidence[0]", "snippet": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\"", "explanation": "solutions[1].composition[1].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[1]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[2].evidence[0]", "snippet": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\"", "explanation": "solutions[1].composition[2].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[2]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[3].evidence[0]", "snippet": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\"", "explanation": "solutions[1].composition[3].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[3]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[4].evidence[0]", "snippet": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\"", "explanation": "solutions[1].composition[4].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[4]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[5].evidence[0]", "snippet": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\"", "explanation": "solutions[1].composition[5].concentration: Source batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[5]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[6].evidence[0]", "snippet": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\"", "explanation": "solutions[1].composition[6].concentration: Source batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[6]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[7].evidence[0]", "snippet": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\"", "explanation": "solutions[1].composition[7].concentration: Source batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[7]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[8].evidence[0]", "snippet": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\"", "explanation": "solutions[1].composition[8].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[8]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[9].evidence[0]", "snippet": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\"", "explanation": "solutions[1].composition[9].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[9]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "$.solutions[1].composition[10].evidence[0]", "snippet": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\"", "explanation": "solutions[1].composition[10].concentration: Source batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration. No final-medium volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[10]; accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.", "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status": "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text": true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"], "historical_hash_matches_current": true}]}], "excluded_parent_evidence_objects": 48} |
| current-code-0 | src/culturemech/import/togo_importer.py; Current scoped code; no historical-version inference | context_only | Current TOGO code contains explicit unit handling and stock/reference logic, unlike these persisted placeholders; the snapshot is not historical-writer proof. Source dependency notes and current cleanup behavior do not authorize whole-parent transplantation. Correct the maintained M247 owner, preserve historical events and regenerate afterward. |
| current-code-1 | scripts/cleanup_media_quality.py; Current scoped code; no historical-version inference | context_only | Current TOGO code contains explicit unit handling and stock/reference logic, unlike these persisted placeholders; the snapshot is not historical-writer proof. Source dependency notes and current cleanup behavior do not authorize whole-parent transplantation. Correct the maintained M247 owner, preserve historical events and regenerate afterward. |
| current-code-2 | src/culturemech/merge/merge_recipes.py; Current scoped code; no historical-version inference | context_only | Current TOGO code contains explicit unit handling and stock/reference logic, unlike these persisted placeholders; the snapshot is not historical-writer proof. Source dependency notes and current cleanup behavior do not authorize whole-parent transplantation. Correct the maintained M247 owner, preserve historical events and regenerate afterward. |
| mediadiveJ255api-attempt | https://mediadive.dsmz.de/rest/medium/J255; Preserved exact public retrieval result | context_only | Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source material is independently available; this optional failure does not make the required primary comparison unavailable. |
| mediadiveJ255api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J255; Preserved exact public retrieval result | context_only | Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source material is independently available; this optional failure does not make the required primary comparison unavailable. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source material is independently available; this optional failure does not make the required primary comparison unavailable.
- Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source material is independently available; this optional failure does not make the required primary comparison unavailable.
- No final-medium or measured stock volume is established from the input water entries. All molecular-form qualifiers and density/pressure limits are retained; no final concentrations are manufactured.
- Only the explicitly referenced mineral and vitamin sections transfer. M190 parent legacy MediaIngredientMech:001072 and unrelated parent organism, sulfide and trace-mineral instructions are excluded, so they are not required-unavailable checks for this target.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T165957Z-culturemech-009054-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aquifex_medium (CultureMech:009054)'
started_at: '2026-10-21T16:49:34Z'
finished_at: '2026-10-21T16:59:57Z'
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
summary: TOGO M247 and exact JCM 255 agree on the Aquifex source recipe. Water, milligram
  inputs and two 10 mL stock doses are mislabeled as g/L; both stock compositions
  are empty and gas/preparation stages are absent. Complete scoped mineral and vitamin
  sources are available. Current chemical labels resolve, while parent-stock identities
  and historical evidence must remain restricted to the explicitly transferred subsections.
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
  - path: data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
    sha256: 813ab4f186e460cc02612fe22e8e897b68225a68220e7b90c5f22f0b3e6e0a97
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
    sha256: 032f79f6d1ede00b920a7453ff1c1927169bde7dc172a01af7be36086b5af0e5
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
  - path: scripts/add_metal_ree_labels.py
    sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
    role: context
  - path: scripts/analyze_metal_concentrations.py
    sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
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
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
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
  selection: Task review 294; batch 030 item 4 of 10, selected in Python lexicographic
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
  - CultureMech:009054
targets:
- target_id: CultureMech:009054
  path: data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  label: aquifex_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch030/294/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch030/294/strict.tsv"
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009054
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
  - CultureMech:009054
- check_id: mediadiveJ255api-source-access
  name: 'Exact source content access: mediadiveJ255api'
  required: false
  status: unavailable
  summary: Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO
    source material is independently available; this optional failure does not make
    the required primary comparison unavailable.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - mediadiveJ255api-attempt
- check_id: mediadiveJ255api_retry-source-access
  name: 'Exact source content access: mediadiveJ255api_retry'
  required: false
  status: unavailable
  summary: Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO
    source material is independently available; this optional failure does not make
    the required primary comparison unavailable.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - mediadiveJ255api_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:12.056772Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch030/294/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:13.177367Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-030/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch030/294/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:14.409325Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:50:15.186848Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:59:56Z'
  support: supports
  summary: './data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml:1:id: CultureMech:009054

    ./data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml:1:id: CultureMech:009054

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/source-preflight-bound/294/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:59:56Z'
  support: supports
  summary: 63 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: df931276c93f07e09d918d428f5fd33607ea0d896a0e1b6ec5a4ad9465f4b365
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/source-preflight-bound/294/evidence-context-original.json
  locator: Whole target, all maintained owners and scoped dependencies
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: All frozen local-record objects match fresh inspected YAML. Source interpretations
    are separately checked against actual bound raw/text bytes.
  snapshot_sha256: a48d2b87cd0c2ed8113e77a11a964a8c7a288373abf88317cd64ddcdd28b3575
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247
  locator: $.meta, $.components[0], $.comments[0]
  accessed_at: '2026-10-21T16:33:42.538979Z'
  support: supports
  summary: Exact provider names JCM 255 and supplies the original amounts, two referenced
    stock doses and preparation paragraph.
  snapshot_sha256: 897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=255
  locator: Medium 255 entire recipe and its explicit preparation paragraph
  accessed_at: '2026-10-21T16:33:44.064679Z'
  support: supports
  summary: Primary agrees with provider. Explicit filtration overrides the generic
    JCM autoclave default; source example vessels, gas-stage ratios, pressure and
    conditional pH are documentary source context, not experimentally verified growth
    claims.
  snapshot_sha256: a75d6675e0daeda381dafa75ab6190362a44e368fd07b742836158e13f677040
- evidence_id: trace-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  locator: Trace minerals subsection and its immediate preparation only
  accessed_at: '2026-10-21T09:01:28.851101Z'
  support: supports
  summary: Transfer twelve mineral/chelator solutes, input water and the nitrilotriacetic-acid/KOH
    sequence only. The parent salt-base solution, main medium, sulfur, organism and
    other procedures do not transfer.
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: vitamin-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Transfer ten vitamin solutes and water only. Parent main-medium sulfide,
    reductants, mineral solution and its 1 N KOH instruction are outside the referenced
    vitamin scope.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: trace-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  locator: $.components[2]; $.comments[1]
  accessed_at: '2026-10-21T09:28:25.414106Z'
  support: supports
  summary: Exact scoped mineral counterpart, including unquantified KOH and ordered
    pH adjustments.
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
- evidence_id: vitamin-provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: $.components[1]
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: Exact vitamin counterpart; no legacy identifier or unrelated parent evidence
    transfers merely because it appears elsewhere in this record.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/294/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 93c893b1be128f673ec49570b7ac7005e30e7cf20f5a6f693b906d0241084b70
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
- evidence_id: chebi18276
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18276
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.615173Z'
  support: supports
  summary: CHEBI:18276 resolves to dihydrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 47a32d9cfe41e3759385a0e4e002e9fa208fe1511d84e3d0d1f9f1ca9ce6e86d
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
- evidence_id: chebi63004
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:25.403149Z'
  support: supports
  summary: CHEBI:63004 resolves to sodium bromide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2665f3a4301ab51b67b814a8694bc906c1a13c9b301c85a4416891d3f9412c90
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
- evidence_id: chebi77775
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.354177Z'
  support: supports
  summary: CHEBI:77775 resolves to sodium selenate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: a1a4ab87bbf08908fef7df53a788a85d9f6eee32350f082895e0563d6344c908
- evidence_id: chebi86149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:08.844455Z'
  support: supports
  summary: CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 930d93c33f6115f19153868ae36f0153b69406fd555708237a7ccccfb010cd97
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T16:59:56Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label":
    "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004", "preferred_term":
    "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:77775": [{"label": "Na2SeO4", "match_type": "preferred_term",
    "identifier": "CHEBI:77775", "preferred_term": "Na2SeO4", "ontology_id": "CHEBI:77775",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml", "events": 13,
    "timestamp_issues": []}]'
- evidence_id: dependency-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch030/source-preflight-bound/294/evidence-context-original.json
  locator: existing_owner_evidence_recheck, transferred trace/vitamin sections only
  accessed_at: '2026-10-21T16:59:56Z'
  support: supports
  summary: '{"in_scope": [{"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[0].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\"", "explanation": "solutions[1].composition[0].concentration:
    Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior
    duplicate-collapse notes describe the superseded flattened record. No final-medium
    volume, percentage basis, density or chemical grounding is inferred. Locator=components[2].items[0];
    accessed=2026-10-08T13:22:45.018884+00:00; capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[1].evidence[0]", "snippet": "{\n          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\"", "explanation": "solutions[1].composition[1].concentration:
    Source batch input: 3 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[1]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[2].evidence[0]", "snippet": "{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\"", "explanation": "solutions[1].composition[2].concentration:
    Source batch input: 1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[2]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[3].evidence[0]", "snippet": "{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\"", "explanation": "solutions[1].composition[3].concentration:
    Source batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[3]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[4].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\"", "explanation": "solutions[1].composition[4].concentration:
    Source batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[4]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[5].evidence[0]", "snippet": "{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\"", "explanation": "solutions[1].composition[5].concentration:
    Source batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[5]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[6].evidence[0]", "snippet": "{\n          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\"", "explanation": "solutions[1].composition[6].concentration:
    Source batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[6]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[7].evidence[0]", "snippet": "{\n          \"component_name\":
    \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\"", "explanation": "solutions[1].composition[7].concentration:
    Source batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[7]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[8].evidence[0]", "snippet": "{\n          \"component_name\":
    \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001039\"", "explanation": "solutions[1].composition[8].concentration:
    Source batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[8]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[9].evidence[0]", "snippet": "{\n          \"component_name\":
    \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001050\"", "explanation": "solutions[1].composition[9].concentration:
    Source batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[9]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[10].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001053\"", "explanation": "solutions[1].composition[10].concentration:
    Source batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[10]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[11].evidence[0]", "snippet": "{\n          \"component_name\":
    \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001065\"", "explanation": "solutions[1].composition[11].concentration:
    Source batch input: 0.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[11]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml",
    "field_path": "$.solutions[1].composition[12].evidence[0]", "snippet": "{\n          \"component_name\":
    \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001088\"", "explanation": "solutions[1].composition[12].concentration:
    Source batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[2].items[12]; accessed=2026-10-08T13:22:45.018884+00:00;
    capture SHA256=610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33.",
    "captures": [{"key": "togoM142", "sha256": "610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33",
    "accessed_at": "2026-10-21T09:28:25.414106Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[0].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\"", "explanation": "solutions[1].composition[0].concentration:
    Source water batch input: 1 L = 1 L. This is not a measured final volume. Prior
    duplicate-collapse notes describe the superseded flattened record. No final-medium
    volume, percentage basis, density or chemical grounding is inferred. Locator=components[1].items[0];
    accessed=2026-10-08T13:22:46.432534+00:00; capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[1].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\"", "explanation": "solutions[1].composition[1].concentration:
    Source batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[1]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[2].evidence[0]", "snippet": "{\n          \"component_name\":
    \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\"", "explanation": "solutions[1].composition[2].concentration:
    Source batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[2]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[3].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\"", "explanation": "solutions[1].composition[3].concentration:
    Source batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[3]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[4].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001028\"", "explanation": "solutions[1].composition[4].concentration:
    Source batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[4]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[5].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\"", "explanation": "solutions[1].composition[5].concentration:
    Source batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[5]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[6].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\"", "explanation": "solutions[1].composition[6].concentration:
    Source batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[6]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[7].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\"", "explanation": "solutions[1].composition[7].concentration:
    Source batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[7]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[8].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\"", "explanation": "solutions[1].composition[8].concentration:
    Source batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[8]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[9].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\"", "explanation": "solutions[1].composition[9].concentration:
    Source batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[9]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}, {"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
    "field_path": "$.solutions[1].composition[10].evidence[0]", "snippet": "{\n          \"component_name\":
    \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\"", "explanation": "solutions[1].composition[10].concentration:
    Source batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration. No final-medium volume, percentage basis, density or chemical grounding
    is inferred. Locator=components[1].items[10]; accessed=2026-10-08T13:22:46.432534+00:00;
    capture SHA256=61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528.",
    "captures": [{"key": "togoM190", "sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "accessed_at": "2026-10-21T09:28:25.418127Z", "status": 200, "comparison_status":
    "exact_available_source_bytes", "snippet_exactly_in_raw": true, "snippet_exactly_in_extracted_text":
    true, "historical_sha256_literals": ["61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"],
    "historical_hash_matches_current": true}]}], "excluded_parent_evidence_objects":
    48}'
  snapshot_sha256: a48d2b87cd0c2ed8113e77a11a964a8c7a288373abf88317cd64ddcdd28b3575
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: Current TOGO code contains explicit unit handling and stock/reference logic,
    unlike these persisted placeholders; the snapshot is not historical-writer proof.
    Source dependency notes and current cleanup behavior do not authorize whole-parent
    transplantation. Correct the maintained M247 owner, preserve historical events
    and regenerate afterward.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: current-code-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: Current TOGO code contains explicit unit handling and stock/reference logic,
    unlike these persisted placeholders; the snapshot is not historical-writer proof.
    Source dependency notes and current cleanup behavior do not authorize whole-parent
    transplantation. Correct the maintained M247 owner, preserve historical events
    and regenerate afterward.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: current-code-2
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T16:59:56Z'
  support: context_only
  summary: Current TOGO code contains explicit unit handling and stock/reference logic,
    unlike these persisted placeholders; the snapshot is not historical-writer proof.
    Source dependency notes and current cleanup behavior do not authorize whole-parent
    transplantation. Correct the maintained M247 owner, preserve historical events
    and regenerate afterward.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: mediadiveJ255api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J255
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:33:41.898854Z'
  support: context_only
  summary: Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO
    source material is independently available; this optional failure does not make
    the required primary comparison unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ255api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J255
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:34:39.999185Z'
  support: context_only
  summary: Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO
    source material is independently available; this optional failure does not make
    the required primary comparison unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 49 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Distilled water main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 1,\n      \"source_unit\": \"L\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. One liter of input water is not 1 g/L.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"MgSO4・7H2O main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 7,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 7,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"NaCl main input\",\n    \"decision\": \"correct\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 30,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 30,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"CaCl2・2H2O main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.5,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"NH4Cl main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.15,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.15,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"K2HPO4 main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.15,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.15,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"MgCl2・6H2O main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 5.5,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 5.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"KCl main input\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.65\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.65\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.65,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.65,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"NaHCO3 main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 2,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Na2WO4・2H2O main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.1,\n      \"source_unit\": \"mg\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The source amount is milligrams, not grams per liter; no final-volume\
    \ assumption is made.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4・2H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"NaBr main input\",\n    \"decision\": \"correct\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.1,\n      \"source_unit\": \"g\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The number matches the source mass, but a final-volume denominator and\
    \ attached claim evidence are absent.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaBr\\\",\\n          \\\"volume\\\": 0.1,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"(NH4)2Ni(SO4)2・6H2O main input\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 20,\n      \"source_unit\": \"mg\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The source amount is milligrams, not grams per liter; no final-volume\
    \ assumption is made.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)2Ni(SO4)2・6H2O\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\":\
    \ \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Na2SeO4 main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount\": 0.1,\n      \"source_unit\": \"mg\",\n      \"finished_medium_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Restore the literal source batch amount and\
    \ unit. The source amount is milligrams, not grams per liter; no final-volume\
    \ assumption is made.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO4\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Trace minerals (see Medium [M142]) receiving dose\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 10,\n      \"source_reference\": \"JCM 151 mineral subsection\"\
    ,\n      \"final_medium_denominator\": null\n    },\n    \"rationale\": \"A stock\
    \ volume is stored as a mass concentration. Restore the ten-milliliter receiving\
    \ amount, resolve only the named stock subsection and preserve the separate one-liter\
    \ main water input.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace minerals (see Medium [M142])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Trace vitamins (see Medium [M190]) receiving dose\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 10,\n      \"source_reference\": \"JCM 197 vitamin subsection\"\
    ,\n      \"final_medium_denominator\": null\n    },\n    \"rationale\": \"A stock\
    \ volume is stored as a mass concentration. Restore the ten-milliliter receiving\
    \ amount, resolve only the named stock subsection and preserve the separate one-liter\
    \ main water input.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Carbon dioxide gas staged gas context\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_H2_CO2_volume_ratio\": [\n        4,\n        1\n      ],\n\
    \      \"replacement_H2_CO2_O2_volume_ratio\": [\n        79,\n        20,\n \
    \       1\n      ],\n      \"absolute_gas_amount\": null\n    },\n    \"rationale\"\
    : \"The provider item itself has no bulk amount. Replace the loss of source-stage\
    \ information in variable gas placeholders with the exact mixture context, not\
    \ an invented mass concentration or absolute gas dose.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM247\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\",\n     \
    \   \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.0. Sterilize by filtration. Aseptically dispense the medium\
    \ into culture vessels (e.g., 20 ml medium in 120 ml serum bottles) under a stream\
    \ of H2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Replace\
    \ the gas phase with a H2--CO2--O2 (79:20:1, v/v) gas mixture and pressurize to\
    \ 200 kPa with the same gas mixture. Readjust pH to 5.5--6.0, if necessary.\"\
    ,\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    ,\n        \"parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"Oxygen\
    \ gas staged gas context\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_H2_CO2_volume_ratio\": [\n        4,\n        1\n      ],\n\
    \      \"replacement_H2_CO2_O2_volume_ratio\": [\n        79,\n        20,\n \
    \       1\n      ],\n      \"absolute_gas_amount\": null\n    },\n    \"rationale\"\
    : \"The provider item itself has no bulk amount. Replace the loss of source-stage\
    \ information in variable gas placeholders with the exact mixture context, not\
    \ an invented mass concentration or absolute gas dose.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM247\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\",\n     \
    \   \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.0. Sterilize by filtration. Aseptically dispense the medium\
    \ into culture vessels (e.g., 20 ml medium in 120 ml serum bottles) under a stream\
    \ of H2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Replace\
    \ the gas phase with a H2--CO2--O2 (79:20:1, v/v) gas mixture and pressurize to\
    \ 200 kPa with the same gas mixture. Readjust pH to 5.5--6.0, if necessary.\"\
    ,\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    ,\n        \"parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\": \"Hydrogen\
    \ gas staged gas context\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_H2_CO2_volume_ratio\": [\n        4,\n        1\n      ],\n\
    \      \"replacement_H2_CO2_O2_volume_ratio\": [\n        79,\n        20,\n \
    \       1\n      ],\n      \"absolute_gas_amount\": null\n    },\n    \"rationale\"\
    : \"The provider item itself has no bulk amount. Replace the loss of source-stage\
    \ information in variable gas placeholders with the exact mixture context, not\
    \ an invented mass concentration or absolute gas dose.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM247\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\",\n     \
    \   \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.0. Sterilize by filtration. Aseptically dispense the medium\
    \ into culture vessels (e.g., 20 ml medium in 120 ml serum bottles) under a stream\
    \ of H2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Replace\
    \ the gas phase with a H2--CO2--O2 (79:20:1, v/v) gas mixture and pressurize to\
    \ 200 kPa with the same gas mixture. Readjust pH to 5.5--6.0, if necessary.\"\
    ,\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    ,\n        \"parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"JCM\
    \ 151 Trace minerals: Distilled water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"Distilled water\",\n      \"batch_amount\"\
    : 1,\n      \"source_unit\": \"L\",\n      \"receiving_dose_ml\": 10,\n      \"\
    finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: MgSO4・7H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"MgSO4・7H2O\",\n      \"batch_amount\":\
    \ 3,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n      \"\
    finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: NaCl\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"NaCl\",\n      \"batch_amount\": 1,\n \
    \     \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n      \"finished_stock_volume_ml\"\
    : null,\n      \"final_medium_concentration\": null\n    },\n    \"rationale\"\
    : \"Recover this exact source-only component into the currently empty stock composition.\
    \ Source water is an input amount; no finished stock volume or final-medium dilution\
    \ is inferred.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM142\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: CaCl2・2H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[3].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[3].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"CaCl2・2H2O\",\n      \"batch_amount\":\
    \ 0.1,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: Na2MoO4・2H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[4].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[4].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"Na2MoO4・2H2O\",\n      \"batch_amount\"\
    : 0.01,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n   \
    \   \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: H3BO3\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[5].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"H3BO3\",\n      \"batch_amount\": 0.01,\n\
    \      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n      \"finished_stock_volume_ml\"\
    : null,\n      \"final_medium_concentration\": null\n    },\n    \"rationale\"\
    : \"Recover this exact source-only component into the currently empty stock composition.\
    \ Source water is an input amount; no finished stock volume or final-medium dilution\
    \ is inferred.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM142\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: FeSO4・7H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"FeSO4・7H2O\",\n      \"batch_amount\":\
    \ 0.1,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: ZnSO4・7H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"ZnSO4・7H2O\",\n      \"batch_amount\":\
    \ 0.1,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: CuSO4・5H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[8].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[8].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"CuSO4・5H2O\",\n      \"batch_amount\":\
    \ 0.01,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n   \
    \   \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4・5H2O\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: CoSO4・7H2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[9].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[9].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"CoSO4・7H2O\",\n      \"batch_amount\":\
    \ 0.1,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoSO4・7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: Nitrilotriacetic acid\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[10].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[10].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n  \
    \  \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"Nitrilotriacetic acid\",\n      \"batch_amount\"\
    : 1.5,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM142\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\",\n     \
    \   \"source_locator\": \"$.components[2].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid\\\",\\n          \\\"volume\\\
    \": 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: MnSO4・xH2O\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[11].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[11].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n  \
    \  \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"MnSO4・xH2O\",\n      \"batch_amount\":\
    \ 0.5,\n      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred. Preserve x-hydrate\
    \ wording; a parent anhydrous term cannot establish a hydration number.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM142\",\n \
    \       \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4・xH2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: AlK(SO4)2\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[12].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[12].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n  \
    \  \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 151 Trace\
    \ minerals\",\n      \"ingredient\": \"AlK(SO4)2\",\n      \"batch_amount\": 0.01,\n\
    \      \"source_unit\": \"g\",\n      \"receiving_dose_ml\": 10,\n      \"finished_stock_volume_ml\"\
    : null,\n      \"final_medium_concentration\": null\n    },\n    \"rationale\"\
    : \"Recover this exact source-only component into the currently empty stock composition.\
    \ Source water is an input amount; no finished stock volume or final-medium dilution\
    \ is inferred.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM142\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"AlK(SO4)2\\\",\\n          \\\"volume\\\": 0.01,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"JCM 151 Trace minerals: KOH solution\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[13].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"not_quantified\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[13].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"not_quantified\"\n      }\n\
    \    ],\n    \"proposed_source_representation\": {\n      \"source_stock\": \"\
    JCM 151 Trace minerals\",\n      \"ingredient\": \"KOH solution\",\n      \"batch_amount\"\
    : null,\n      \"source_unit\": null,\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"KOH is a titration reagent with no fixed\
    \ source amount; preserve the ordered pH adjustment without inventing a dose.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM142\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.components[2].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KOH solution\\\"\",\n        \"snapshot_sha256\"\
    : \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Distilled water\",\n    \"decision\": \"add\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Distilled water\",\n      \"batch_amount\"\
    : 1,\n      \"source_unit\": \"L\",\n      \"receiving_dose_ml\": 10,\n      \"\
    finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Biotin\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Biotin\",\n      \"batch_amount\": 2,\n\
    \      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n      \"finished_stock_volume_ml\"\
    : null,\n      \"final_medium_concentration\": null\n    },\n    \"rationale\"\
    : \"Recover this exact source-only component into the currently empty stock composition.\
    \ Source water is an input amount; no finished stock volume or final-medium dilution\
    \ is inferred.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM190\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: p--Aminobenzoic acid\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"p--Aminobenzoic acid\",\n      \"batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Thiamine・HCl\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Thiamine・HCl\",\n      \"batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Calcium pantothenate\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Calcium pantothenate\",\n      \"batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred. Generic source calcium pantothenate\
    \ does not establish the parent D-specific identifier.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Pyridoxine・HCl\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Pyridoxine・HCl\",\n      \"batch_amount\"\
    : 10,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n    \
    \  \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\":\
    \ null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Folic acid\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Folic acid\",\n      \"batch_amount\":\
    \ 2,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Vitamin B12\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Vitamin B12\",\n      \"batch_amount\"\
    : 0.1,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n   \
    \   \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"rationale\": \"Recover this exact source-only component\
    \ into the currently empty stock composition. Source water is an input amount;\
    \ no finished stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Riboflavin\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[8].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[8].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Riboflavin\",\n      \"batch_amount\":\
    \ 5,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Nicotinic acid\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[9].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[9].concentration\",\n  \
    \      \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n   \
    \ \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Nicotinic acid\",\n      \"batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"JCM 197 Trace vitamins: Lipoic acid\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n  \
    \  \"proposed_source_representation\": {\n      \"source_stock\": \"JCM 197 Trace\
    \ vitamins\",\n      \"ingredient\": \"Lipoic acid\",\n      \"batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"receiving_dose_ml\": 10,\n     \
    \ \"finished_stock_volume_ml\": null,\n      \"final_medium_concentration\": null\n\
    \    },\n    \"rationale\": \"Recover this exact source-only component into the\
    \ currently empty stock composition. Source water is an input amount; no finished\
    \ stock volume or final-medium dilution is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n     \
    \   \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Initial main pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n \
    \       \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"initial_pH\": 6\n    },\n    \"rationale\": \"Restore this precisely\
    \ scoped source statement. The vessel quantities are examples, the pressure convention\
    \ is unstated, and the final pH adjustment is conditional. These are not independent\
    \ growth/optimization claims.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.0.\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    ,\n        \"parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\": \"Illustrative\
    \ vessel and medium amounts\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"example_medium_ml\": 20,\n      \"example_vessel_ml\": 120,\n   \
    \   \"mandatory_recipe_scale\": false\n    },\n    \"rationale\": \"Restore this\
    \ precisely scoped source statement. The vessel quantities are examples, the pressure\
    \ convention is unstated, and the final pH adjustment is conditional. These are\
    \ not independent growth/optimization claims.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"20 ml medium in 120 ml serum bottles\",\n        \"snapshot_sha256\": \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\"\
    ,\n        \"parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q46\",\n    \"component_or_context\": \"Replacement\
    \ gas pressure\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n     \
    \   \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"pressure_kPa\": 200,\n      \"gauge_or_absolute\": null,\n      \"\
    stage\": \"Replacement 79:20:1 v/v gas mixture\"\n    },\n    \"rationale\": \"\
    Restore this precisely scoped source statement. The vessel quantities are examples,\
    \ the pressure convention is unstated, and the final pH adjustment is conditional.\
    \ These are not independent growth/optimization claims.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM247\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\",\n     \
    \   \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"pressurize to 200 kPa with the same gas mixture\",\n        \"snapshot_sha256\"\
    : \"897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\",\n    \
    \    \"parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q47\",\n    \"component_or_context\": \"Conditional\
    \ readjusted pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n    \
    \    \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"pH_range\": [\n        5.5,\n        6\n      ],\n      \"conditional\"\
    : true\n    },\n    \"rationale\": \"Restore this precisely scoped source statement.\
    \ The vessel quantities are examples, the pressure convention is unstated, and\
    \ the final pH adjustment is conditional. These are not independent growth/optimization\
    \ claims.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM247\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M247\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Readjust pH to 5.5--6.0, if necessary.\",\n        \"snapshot_sha256\": \"\
    897fd2bc162f80387649efc6cf9fc34294d9a7bf7d99239ec4cc79575aa0a9fc\",\n        \"\
    parsed_text_sha256\": \"1f47ea118edfd508d77023aefc0cb5518e59a441fd96dafecda0f70158cc7bf2\"\
    ,\n        \"accessed_at\": \"2026-10-21T16:33:42.538979Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q48\",\n    \"component_or_context\": \"Chelator-first\
    \ trace adjustment\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"solutions[0].preparation_notes\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Dissolve nitrilotriacetic acid first\",\n      \"pH\"\
    : 6.5,\n      \"reagent\": \"KOH\",\n      \"quantity\": null\n    },\n    \"\
    rationale\": \"Preserve the exact order: chelator dissolution, KOH adjustment,\
    \ mineral addition, then final pH. The unrelated JCM 197 trace-mineral 1 N KOH\
    \ statement is outside scope.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"togoM142\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\",\n    \
    \    \"parsed_text_sha256\": \"2cfd46cc453b6c97030970fc0d8811706dd2ddb6f98306357e8a9727d09241ba\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.414106Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q49\",\n    \"component_or_context\": \"Final\
    \ trace-stock pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml\",\n        \"\
    field_path\": \"solutions[0].preparation_notes\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"After mineral addition\",\n      \"pH\": 7\n    },\n \
    \   \"rationale\": \"Preserve the exact order: chelator dissolution, KOH adjustment,\
    \ mineral addition, then final pH. The unrelated JCM 197 trace-mineral 1 N KOH\
    \ statement is outside scope.\",\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"togoM142\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then\
    \ proceed to add minerals. Adjust final pH to 7.0.\",\n        \"snapshot_sha256\"\
    : \"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33\",\n    \
    \    \"parsed_text_sha256\": \"2cfd46cc453b6c97030970fc0d8811706dd2ddb6f98306357e8a9727d09241ba\"\
    ,\n        \"accessed_at\": \"2026-10-21T09:28:25.414106Z\"\n      }\n    ]\n\
    \  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '15 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 15/16
    primary and 8/16 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi16526
  - chebi18276
  - chebi26710
  - chebi31206
  - chebi31795
  - chebi32139
  - chebi32588
  - chebi63004
  - chebi63939
  - chebi77775
  - chebi86149
  - chebi86158
  - chebi86345
  details: 'Instance coverage on a 0–100 percent scale, denominator 16: primary 93.75%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 27 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact accession, dependency and owner identity
  outcome: supported
  summary: The one maintained owner and generated target share stable ID CultureMech:009054
    and TOGO M247/JCM 255. M142 resolves to the named JCM 151 mineral stock; M190
    resolves to JCM 197 vitamins. These are scoped dependencies, not additional recipes
    merged into this target.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - record
  - owner-0
  - provider
  - primary
  - trace-primary
  - vitamin-primary
- assessment_id: dependency-grounding
  area: grounding
  topic: Scoped dependency forms and preserved historical evidence
  outcome: concern
  summary: All asserted target/owner primary labels and current CHEBI secondary keys
    resolve. The mineral dependency includes MnSO4·xH2O, while its parent mapping
    cannot resolve x; parent calcium-pantothenate stereochemistry is not established
    by the generic vitamin name. Preserve supplied forms without copying over-specific
    parent mappings blindly. Existing in-scope amount snippets match exact captured
    bytes and hashes, but parent main-recipe evidence and legacy IDs do not transfer.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - dependency-evidence
  - trace-primary
  - vitamin-primary
  - trace-provider
  - vitamin-provider
- assessment_id: preparation
  area: completeness
  topic: Explicit filtration, gas stages and stock adjustments
  outcome: concern
  summary: Local layers omit the complete preparation context. JCM 255 explicitly
    specifies filtration, so its generic autoclave cycle is inapplicable to the main
    recipe. Preserve source pH stages, example vessel scope, gas ratios and pressure
    convention limit; preserve trace chelator-first ordering. Do not import unrelated
    parent-medium operations or infer growth.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - primary
  - provider
  - trace-primary
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Mixture classification and application scope
  outcome: concern
  summary: The resolved formulation comprises named chemicals and defined trace/vitamin
    constituents rather than yeast extract or peptone. COMPLEX/UNDEFINED should be
    re-evaluated against those exact constituents; hydrate/form uncertainty should
    be explicit rather than misclassified as an undefined extract. LIQUID is supported.
    No taxonomy, nutrient-role mechanism or growth claim is inferred from the title
    or generic application.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - primary
  - trace-primary
  - vitamin-primary
  - record
- assessment_id: current-writers
  area: provenance
  topic: Current writers and follow-up ownership
  outcome: concern
  summary: Current TOGO code contains explicit unit handling and stock/reference logic,
    unlike these persisted placeholders; the snapshot is not historical-writer proof.
    Source dependency notes and current cleanup behavior do not authorize whole-parent
    transplantation. Correct the maintained M247 owner, preserve historical events
    and regenerate afterward.
  target_ids:
  - CultureMech:009054
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
findings:
- finding_id: f1
  issue_key: culturemech.009054.amount-units
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Volume and milligram inputs are stored as grams per liter
  description: Both layers store water 1 g/L, ammonium nickel sulfate 20 g/L, tungstate
    and selenate 0.1 g/L, and both ten-milliliter stocks as 10 g/L. These disagree
    with explicit source units; other gram amounts also lack an independently established
    final-volume basis.
  target_ids:
  - CultureMech:009054
  field_paths:
  - ingredients[0].concentration
  - ingredients[9].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - solutions
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  issue_key: culturemech.009054.empty-stock-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Two source-resolvable stock nodes remain empty placeholders
  description: Both stocks have empty composition and Unknown solution names despite
    explicit source cross-references. Complete mineral and vitamin subsections are
    available, including their waters and unquantified KOH context.
  target_ids:
  - CultureMech:009054
  field_paths:
  - solutions[0]
  - solutions[1]
  evidence_ids:
  - trace-primary
  - vitamin-primary
  - trace-provider
  - vitamin-provider
  - dependency-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  issue_key: culturemech.009054.preparation-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Variable gases omit explicit staged source conditions
  description: Generic variable gas entries lose the two source mixture ratios and
    the associated preparation stages. Main filtration and pH context, example vessel
    amounts, pressure limit and mineral-stock ordering are absent.
  target_ids:
  - CultureMech:009054
  field_paths:
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - solutions
  evidence_ids:
  - primary
  - provider
  - trace-primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  issue_key: culturemech.009054.composition-category
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Classification does not reflect the resolved chemical formulation
  description: COMPLEX/UNDEFINED is unsupported by the named salt/trace/vitamin formulation.
    Parent yeast extract and peptone are outside the transferred stock sections and
    cannot support that classification.
  target_ids:
  - CultureMech:009054
  field_paths:
  - medium_type
  - composition_type
  evidence_ids:
  - primary
  - trace-primary
  - vitamin-primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  description: Restore every literal source amount/unit with exact evidence, separating
    batch inputs from stock addition volumes and final concentrations. Preserve water
    as a volume input and do not assume measured final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009054
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  description: Populate or resolve only the named subsections with source-bound composition
    evidence. Preserve later dependency amount evidence and form caveats; exclude
    all unrelated parent recipes and legacy identifiers.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009054
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  description: Attach scoped source preparation and gas-stage evidence, preserving
    the example/conditional qualifiers and unstated pressure convention. Filtration
    overrides the main generic autoclave default; do not invent a cycle or borrow
    other parent procedures.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009054
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
  description: Reassess composition category after resolving exact stock constituents
    and retain any form uncertainty explicitly. Do not infer growth targets from the
    medium name.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009054
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml
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
- Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source
  material is independently available; this optional failure does not make the required
  primary comparison unavailable.
- Current exact provider endpoint returned HTTP 503. Complete JCM and TOGO source
  material is independently available; this optional failure does not make the required
  primary comparison unavailable.
- No final-medium or measured stock volume is established from the input water entries.
  All molecular-form qualifiers and density/pressure limits are retained; no final
  concentrations are manufactured.
- Only the explicitly referenced mineral and vitamin sections transfer. M190 parent
  legacy MediaIngredientMech:001072 and unrelated parent organism, sulfide and trace-mineral
  instructions are excluded, so they are not required-unavailable checks for this
  target.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-030
- generated-medium
```
