# Source and formulation review: anaerobic_thauera_medium (CultureMech:004072)

- Review: 20261021T152505Z-culturemech-004072-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:15:04Z
- Finished UTC: 2026-10-21T15:25:05Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1315 and the separate KOMODO 1315/1315.1 catalog identities are established. Four local layers flatten five stocks into direct concentrations and lose source assembly scope. Nickel hydration conflicts with its identifier; source conditional strain membership and legacy MIM000170 history remain unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 266; batch 027 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-six task batches contain 260 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 263 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004072 | data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml | generated | anaerobic_thauera_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:004072 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:004072 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/266/strict.tsv |
| validate-terms | passed | True | CultureMech:004072 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:004072 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:004072 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact current secondary catalog/index/tree lookup | passed | True | CultureMech:004072 | Completed negative lookup for MediaIngredientMech:000170; current absence established within the pinned complete snapshots, historical validity not adjudicated. |
| Historical secondary identifier correspondence | unavailable | True | CultureMech:004072 | Required historical correspondence for asserted MediaIngredientMech:000170 remains unavailable in the inspected evidence. The current negative lookup completed successfully and is not itself an unavailable check or proof that the legacy identifier was historically wrong. |
| Exact source content access: mediadive1315api | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: komodo1315detail | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: komodo1315_1detail | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: mediadive1315api_retry | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: solution2636 | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: solution2632 | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: solution2633 | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact source content access: solution926 | unavailable | False | CultureMech:004072 | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| Exact strain-wrapper to primary branch correspondence | unavailable | True | CultureMech:004072 | Required exact correspondence between KOMODO 1315.1 strain-wrapper scope and the primary conditional substrate branch remains unresolved. Literal source lists differ; neither an inferred typo nor equal flattened ingredients resolves that identity. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:004072.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:004072.

50 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Main: KNO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 0.85,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "KNO3 0.85 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Main: NaHCO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2.52",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2.52",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2.52",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2.52",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 2.52,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaHCO3 2.52 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Main: CaCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 0.01,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "CaCl2 0.01 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main: MgSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 0.5,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main: MnSO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 0.01,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "MnSO4 0.01 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Main: NH4Cl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 0.3,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NH4Cl 0.30 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Main: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_batch_mass_g": 0.05,
      "listed_main_water_ml": 884,
      "listed_liquids_sum_ml": 1002,
      "measured_final_volume": null
    },
    "rationale": "The number matches the source batch mass, but local g/L claims a final denominator not stated by this primary. Retain batch mass, water and five receiving doses; no unavailable main API is treated as corroboration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaCl 0.05 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "phosphate: Na2HPO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "14.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "14.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "14.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "14.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "phosphate",
      "stock_mass_g": 1.45,
      "stock_water_ml": 100,
      "receiving_dose_ml": 100
    },
    "rationale": "Stored 14.5/2.5/98 g/L are stock-strength values, not undiluted main ingredient concentrations. Preserve explicit stock quantities and receiving doses.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 phosphate stock",
        "exact_source_quote": "Na2HPO4 x 2 H2O 1.45 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "phosphate: KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "phosphate",
      "stock_mass_g": 0.25,
      "stock_water_ml": 100,
      "receiving_dose_ml": 100
    },
    "rationale": "Stored 14.5/2.5/98 g/L are stock-strength values, not undiluted main ingredient concentrations. Preserve explicit stock quantities and receiving doses.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 phosphate stock",
        "exact_source_quote": "KH2PO4 0.25 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "acetate: K-acetate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "98",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "98",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "98",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "98",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "acetate",
      "stock_mass_g": 9.8,
      "stock_water_ml": 100,
      "receiving_dose_ml": 10
    },
    "rationale": "Stored 14.5/2.5/98 g/L are stock-strength values, not undiluted main ingredient concentrations. Preserve explicit stock quantities and receiving doses.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 acetate stock",
        "exact_source_quote": "K-acetate 9.80 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Vitamin stock: Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 50,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Vitamin B12 50.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Vitamin stock: Pantothenic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 50,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Pantothenic acid 50.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Vitamin stock: Riboflavin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 50,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Vitamin stock: Pyridoxamine hydrochloride",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 10,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Pyridoxamine-HCl 10.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Vitamin stock: Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 20,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Vitamin stock: Folic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 20,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Vitamin stock: Nicotinic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 25,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Nicotinic acid 25.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Vitamin stock: Nicotine amide",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 25,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Nicotine amide 25.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Vitamin stock: alpha-lipoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 50,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "α-lipoic acid 50.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Vitamin stock: p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 50,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "p-aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Vitamin stock: Thiamine-HCl x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "stock_mass_mg": 50,
      "listed_water_ml": 1000,
      "receiving_dose_ml": 5
    },
    "rationale": "The source stock mass and five-milliliter receiving dose must remain separate; the locally stored stock-strength g/L is not the assembled-medium concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin solution table across pages 1–2",
        "exact_source_quote": "Thiamine-HCl x 2 H2O 50.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "SL-10: HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 10,
      "unit": "ml",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": "25%; 7.7 M"
    },
    "rationale": "Restore stock scope and supplied form. The 25% basis remains unspecified while 7.7 M is explicit. Provider stock g_l 2.5 does not justify that mass conversion or its use as a main concentration.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "HCl (25%; 7.7 M) 10.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "SL-10: FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 1.5,
      "unit": "g",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "SL-10: ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 70,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "SL-10: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 100,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "SL-10: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 6,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "SL-10: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 190,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "SL-10: CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 2,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "SL-10: NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 24,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "SL-10: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "stock_amount": 36,
      "unit": "mg",
      "final_stock_makeup_ml": 1000,
      "receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "Restore stock scope and supplied form. Current stock endpoint corroborates the listed stock amount, not a historical main-medium denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Trace element solution SL-10",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Se/W: NaOH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Se/W",
      "stock_amount": 0.5,
      "unit": "g",
      "listed_water_ml": 1000,
      "receiving_dose_ml": 2
    },
    "rationale": "The stock recipe requires its explicit two-milliliter main addition; the flat g/L entries are not direct final-medium concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Selenite and tungstate solution",
        "exact_source_quote": "NaOH 0.50 g",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Se/W: Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Se/W",
      "stock_amount": 3,
      "unit": "mg",
      "listed_water_ml": 1000,
      "receiving_dose_ml": 2
    },
    "rationale": "The stock recipe requires its explicit two-milliliter main addition; the flat g/L entries are not direct final-medium concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Selenite and tungstate solution",
        "exact_source_quote": "Na2SeO3 x 5 H2O 3.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Se/W: Na2WO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Se/W",
      "stock_amount": 4,
      "unit": "mg",
      "listed_water_ml": 1000,
      "receiving_dose_ml": 2
    },
    "rationale": "The stock recipe requires its explicit two-milliliter main addition; the flat g/L entries are not direct final-medium concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 Selenite and tungstate solution",
        "exact_source_quote": "Na2WO4 x 2 H2O 4.00 mg",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "water_ml": 884
    },
    "rationale": "Restore exact source solvent stage and unit. Main water is not the final volume; SL-10 separately has an explicit final make-up.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "main table water row",
        "exact_source_quote": "Distilled water 884.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "phosphate water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "phosphate",
      "water_ml": 100
    },
    "rationale": "Restore exact source solvent stage and unit. Main water is not the final volume; SL-10 separately has an explicit final make-up.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "phosphate table water row",
        "exact_source_quote": "Distilled water 100.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "acetate water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "acetate",
      "water_ml": 100
    },
    "rationale": "Restore exact source solvent stage and unit. Main water is not the final volume; SL-10 separately has an explicit final make-up.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "acetate table water row",
        "exact_source_quote": "Distilled water 100.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "vitamins water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "water_ml": 1000
    },
    "rationale": "Restore exact source solvent stage and unit. Main water is not the final volume; SL-10 separately has an explicit final make-up.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "vitamins table water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "SL-10 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "water_ml": 990
    },
    "rationale": "Restore exact source solvent stage and unit. Main water is not the final volume; SL-10 separately has an explicit final make-up.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "SL-10 table water row",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Se/W water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "Se/W",
      "water_ml": 1000
    },
    "rationale": "Restore exact source solvent stage and unit. Main water is not the final volume; SL-10 separately has an explicit final make-up.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Se/W table water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Se/W receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "Se/W",
      "dose_ml": 2,
      "listed_liquid_sum_including_water_ml": 1002
    },
    "rationale": "No structured solution receiving dose is retained in any local layer. Restore the exact main addition without treating all stock constituents as direct main concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main additions",
        "exact_source_quote": "Selenite and tungstate solution  2.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "phosphate receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "phosphate",
      "dose_ml": 100,
      "listed_liquid_sum_including_water_ml": 1002
    },
    "rationale": "No structured solution receiving dose is retained in any local layer. Restore the exact main addition without treating all stock constituents as direct main concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main additions",
        "exact_source_quote": "Phosphate solution 100.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "acetate or conditional capronate receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "acetate or conditional capronate",
      "dose_ml": 10,
      "listed_liquid_sum_including_water_ml": 1002
    },
    "rationale": "No structured solution receiving dose is retained in any local layer. Restore the exact main addition without treating all stock constituents as direct main concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main additions",
        "exact_source_quote": "Acetate or capronate solution 10.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "vitamins receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "vitamins",
      "dose_ml": 5,
      "listed_liquid_sum_including_water_ml": 1002
    },
    "rationale": "No structured solution receiving dose is retained in any local layer. Restore the exact main addition without treating all stock constituents as direct main concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main additions",
        "exact_source_quote": "Vitamin solution 5.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "SL-10 receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "SL-10",
      "dose_ml": 1,
      "listed_liquid_sum_including_water_ml": 1002
    },
    "rationale": "No structured solution receiving dose is retained in any local layer. Restore the exact main addition without treating all stock constituents as direct main concentrations.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main additions",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q45",
    "component_or_context": "Conditional sodium capronate stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Filter sterilize and gas with N2. For strains DSM 12141, DSM 12142, DSM 11243 and DSM 12144, acetate may be replaced by Na-capronate (stock solution 2.76 g/100 ml).",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "conditional_stock": "sodium capronate",
      "mass_g": 2.76,
      "stock_basis_ml": 100,
      "may_replace": "acetate",
      "literal_strains": [
        "DSM 12141",
        "DSM 12142",
        "DSM 11243",
        "DSM 12144"
      ]
    },
    "rationale": "The specialized owner retains the branch in main-root stock prose; other layers omit it. Preserve the optional substitution and literal DSM 11243. The separate KOMODO 1315.1 title lists a different strain set and does not establish branch equivalence.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 acetate preparation, literal condition",
        "exact_source_quote": "For strains DSM 12141, DSM 12142, DSM 11243 and",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      },
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Following line",
        "exact_source_quote": "DSM 12144, acetate may be replaced by Na-capronate (stock solution 2.76 g/100 ml).",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q46",
    "component_or_context": "Main gas composition",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic conditions and autoclave. After cooling, add the phosphate solution, substrate solution, vitamin solution and trace element solution. After mixing, pH should be 7.1 - 7.5.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "N2_percent": 90,
      "CO2_percent": 10,
      "stage": "main"
    },
    "rationale": "Recover absent target/KOMODO preparation; retain specialized-owner source prose. Gas percentage basis is not independently relabeled v/v.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q47",
    "component_or_context": "Main final pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.5
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.5
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.5
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.1,
          "max": 7.5
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic conditions and autoclave. After cooling, add the phosphate solution, substrate solution, vitamin solution and trace element solution. After mixing, pH should be 7.1 - 7.5.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "pH_range": [
        7.1,
        7.5
      ],
      "stage": "after mixing"
    },
    "rationale": "All four stored pH ranges agree with the source final mixing stage; no attached evidence supports verified. Preserve stage rather than inventing a stock pH.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "vitamin solution and trace element solution. After mixing, pH should be 7.1 - 7.5.",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q48",
    "component_or_context": "SL-10 final make-up",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "final_stock_makeup_ml": 1000,
      "gas": "N2",
      "sterilization": "autoclave"
    },
    "rationale": "The specialized owner retains the make-up at main root but omits the primary trailing N2/autoclave instruction from this SL-10 step. Restore the complete scoped stock instruction; do not treat 1000 mL as main final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Page 2 SL-10 preparation",
        "exact_source_quote": "Finally make up to 1000 ml. Distribute to gas tight vessels under N2, autoclave.",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q49",
    "component_or_context": "Vitamin stirring duration",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Stir for some hours, filter sterilize the solution.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "duration": "some hours",
      "stage": "vitamins",
      "sterilization": "filtration"
    },
    "rationale": "Retain this qualitative duration and stock-specific filtration; no numerical time is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Vitamin stock preparation",
        "exact_source_quote": "Stir for some hours, filter sterilize the solution.",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  },
  {
    "quantity_id": "q50",
    "component_or_context": "Autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic conditions and autoclave. After cooling, add the phosphate solution, substrate solution, vitamin solution and trace element solution. After mixing, pH should be 7.1 - 7.5.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Distribute to gas tight vessels under N2, autoclave.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml",
        "field_path": "preparation_steps[5].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[5].description",
        "stored": "First dissolve NaOH, subsequently the metal salts. Distribute to gas tight vessels under N2, autoclave.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
        "field_path": "preparation_steps[5].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
        "field_path": "preparation_steps[5].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "temperature": null,
      "duration": null
    },
    "rationale": "Main, phosphate, SL-10 and Se/W autoclaving are source-scoped; a numeric cycle is not specified. The specialized phosphate/Se-W instructions require their stock containers; no default cycle is invented.",
    "source_snippets": [
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Main preparation",
        "exact_source_quote": "conditions and autoclave.",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      },
      {
        "source_key": "dsmz1315",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf",
        "source_locator": "Phosphate stock preparation",
        "exact_source_quote": "Distribute to gas tight vessels under N2, autoclave.",
        "snapshot_sha256": "964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564",
        "parsed_text_sha256": "2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:004072.

33 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 33/33 primary and 31/33 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 33: primary 100.00%; secondary 93.94%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Historical legacy linkage distinct from current CHEBI linkage

grounding: concern. Targets: CultureMech:004072.

Required historical correspondence for asserted MediaIngredientMech:000170 remains unavailable in the inspected evidence. The current negative lookup completed successfully and is not itself an unavailable check or proof that the legacy identifier was historically wrong.

### Main record and non-equivalent strain wrapper identity

identity: concern. Targets: CultureMech:004072.

The target joins main KOMODO 1315, DSMZ 1315 and KOMODO 1315.1 wrapper contributors. Stable IDs CultureMech:004072,015338,004071 resolve exactly and all ingredient lists match. Catalog 1315.1 names DSM 12138/12139/12140/12143; the primary capronate condition names DSM 12141/12142/11243/12144. Equal flattened ingredients do not establish equivalent strain/branch scope. Literal 11243 is not assumed a typo.

### Current sources and historical derivative limits

evidence: concern. Targets: CultureMech:004072.

No local ingredient concentration has attached amount evidence. All 132 concentration instances and source-only stock/preparation quantities are inventoried. Current primary is available; main API and several stock endpoints returned 503. Dated repository report quotations are derivative provenance with preserved hashes, not recovered raw historical responses or proof of source chronology.

### Main preparation recovery and stock separation

completeness: concern. Targets: CultureMech:004072.

Only the specialized owner retains six preparation steps. Target and both KOMODO owners omit them. The source requires distinct main gas/after-cooling additions, phosphate handling, acetate filtration, vitamin filtration, SL-10 make-up and Se/W sequence. The specialized SL-10 step lacks the current primary N2/autoclave continuation and all stock steps remain detached at main root.

### Supplied hydrates and generic vitamin identities

grounding: concern. Targets: CultureMech:004072.

CHEBI:34887 is Cl2Ni, whereas source/local nickel is hexahydrate. Other asserted salt hydrates match their source rows; pantothenic acid and lipoic acid remain generic source-compatible identities. Nicotine amide is preserved source spelling for nicotinamide. The legacy nitrate linkage is assessed separately from valid CHEBI:63043.

### Defined liquid composition and aerobic catalog note

scope: concern. Targets: CultureMech:004072.

DEFINED/DEFINED and LIQUID fit the named chemicals and absence of solidifier. Inherited Aerobic: Yes is a KOMODO catalog flag, not a growth or oxygen-tolerance conclusion; primary main preparation is explicitly anaerobic. No phenotype is inferred from the title or catalog flag.

### Organism and graph assertion limits

scope: concern. Targets: CultureMech:004072.

The title and synonym contain source strain labels but no grounded organism CURIE or experimental growth claim. No internal path graph is asserted. The synonym must retain its distinct catalog provenance and unresolved relation to the conditional primary branch; no new taxonomy or growth inference is made.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:004072.

37 timestamp instances inspected; 6 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current writers and maintained input follow-up

provenance: concern. Targets: CultureMech:004072.

Current MediaDive ingredient parsing selects the first solution and separates receiving stocks, while preparation aggregation may place all source solution steps at the main root. Cleanup retains the first conflicting duplicate rather than summing, and current lossless merging preserves scientific differences. These current behaviors do not authenticate the historical import or justify merging a strain wrapper solely on equal flattened ingredient values. Follow-up belongs in all three maintained contributors and authorized regeneration.

## Findings

### f1: Historical secondary correspondence remains unresolved

minor / open / confirmed; issue key: culturemech.004072.legacy-secondary-correspondence.

The inspected local layers assert MediaIngredientMech:000170 at ingredients[0].mediaingredientmech_term. The current exact lookup is negative, while the primary chemical name and CHEBI identifier can still be valid. Existing enrichment/migration history does not authenticate this historical mapping. This is a bounded provenance gap, not a confirmed wrong chemical or fabricated replacement.

### f2: Five stock recipes are represented as direct medium concentrations

blocker / open / confirmed; issue key: culturemech.004072.stock-stage-collapse.

All four local layers flatten phosphate, acetate, vitamins, SL-10 and Se/W recipes into the main list. For example potassium acetate is 98 g/L and stock phosphate 14.5/2.5 g/L. Main batch masses also acquire an unsupported g/L final basis, and HCl 2.5 g/L assumes unspecified percentage chemistry.

### f3: Nickel hexahydrate has an anhydrous identifier

major / open / confirmed; issue key: culturemech.004072.nickel-hydrate.

ingredients[28] names the hexahydrate but both primary and current secondary terms identify CHEBI:34887 Cl2Ni. Exact source and valid ontology labels expose a source-form mismatch.

### f4: Preparation is missing or detached from its stock

major / open / confirmed; issue key: culturemech.004072.preparation-loss-and-stock-scope.

Only the specialized owner retains the six source-derived steps; target and KOMODO contributors omit preparation. Stock steps need scope, and specialized SL-10 preparation lacks the source trailing N2/autoclave continuation.

### f5: A distinct strain-wrapper catalog entry is merged as a synonym without branch correspondence

major / open / confirmed; issue key: culturemech.004072.strain-wrapper-scope.

The target synonym and one owner identify KOMODO 1315.1 for DSM 12138,12139,12140,12143. Primary capronate substitution names DSM 12141,12142,11243,12144. These are not matching literal sets; source-supported equivalence or branch mapping is unavailable.

### f6: Six history timestamp instances do not establish precise times

minor / open / confirmed; issue key: culturemech.004072.history-timestamp-shape.

Target and both KOMODO owners each retain one malformed fractional timestamp and one timezone-naive timestamp; all 37 historical events are preserved. Current matching ingredients do not establish historical branch identity or provider version.

## Recommended Actions And Acceptance Checks

### a1

Recover an exact historical identifier-to-ingredient correspondence or explicitly qualify the unresolved legacy assertion in the maintained owner. Preserve old history and append the result; do not infer a replacement from names or the current negative lookup.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore seven main batch masses, 884 mL water, five explicit stock doses and each stock composition in all maintained contributors, with branch scope retained. Preserve 1002 mL listed-liquid arithmetic without claiming measured final volume. Attach exact stage evidence before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify source-compatible nickel-hydrate grounding separately for primary and secondary fields in all maintained contributors; do not fabricate a replacement identifier.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover source main preparation where absent; scope phosphate, substrate, vitamin, SL-10 and Se/W instructions to their own stocks, retaining conditional identities and the missing SL-10 continuation. Keep numeric cycle unspecified.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Retain exact catalog IDs and literal strain lists as separate provenance. Resolve wrapper/branch correspondence from exact supporting evidence before treating them as equivalent; preserve DSM11243 verbatim and do not introduce speculative corrections or taxonomy IDs.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve append-only history and qualify uncertain timestamps in a later authorized event; use explicit timezone-aware timestamps for new events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch027/266/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/266/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml:1:id: CultureMech:004072<br>./data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml:1:id: CultureMech:004072<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/266/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 46 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/266/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf; Complete two-page primary; main table, five stock sections and conditional substrate paragraph | supports | Primary distinguishes seven direct salts, five receiving stocks, their preparation and a conditional capronate substitution. Listed liquids total 1002 mL; no measured final volume is asserted. Literal DSM 11243 is preserved and is not rewritten to 12143. |
| sl10-provider | https://mediadive.dsmz.de/rest/solution/595; $.data.id/name/volume/recipe/steps | supports | Exact available SL-10 endpoint retains stock amounts and 1000 mL provider volume. Its HCl g_l 2.5 is a provider assertion, not evidence for an unstated percent basis. It does not recover the unavailable main response or authenticate historical import chronology. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact KOMODO rows 1315 and 1315.1 plus column headers | supports | Catalog separately identifies the main medium and the wrapper for DSM 12138,12139,12140,12143. This is identity metadata, not evidence equating that set with the primary conditional capronate set. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch027/266/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131531 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131531; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131531 resolves to pyridoxamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:132751 resolves to thiamine hydrochloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17154 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17154 resolves to nicotinamide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32029 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32029; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32029 resolves to potassium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3312 resolves to calcium dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63043 resolves to potassium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi7916 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_7916; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:7916 resolves to pantothenic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131531": [{"label": "Pyridoxamine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:131531", "preferred_term": "Pyridoxamine hydrochloride", "ontology_id": "CHEBI:131531", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term": "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32029": [{"label": "K-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32029", "preferred_term": "K-acetate", "ontology_id": "CHEBI:32029", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:7916": [{"label": "Pantothenic acid", "match_type": "preferred_term", "identifier": "CHEBI:7916", "preferred_term": "Pantothenic acid", "ontology_id": "CHEBI:7916", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86360": [{"label": "MnSO4", "match_type": "preferred_term", "identifier": "CHEBI:86360", "preferred_term": "MnSO4", "ontology_id": "CHEBI:86360", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term": "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned current catalog/tree, exact legacy-key lookup | supports | Current snapshot lookup for MediaIngredientMech:000170 completed negatively. It does not establish historical invalidity or an alternative linkage. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete pinned current catalog/tree, exact legacy-key lookup | supports | Current snapshot lookup for MediaIngredientMech:000170 completed negatively. It does not establish historical invalidity or an alternative linkage. |
| legacy-search | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/266/evidence-context-original.json; mim_provenance.legacy_lookup; complete 9077-row index, 2953-row catalog and 7384-entry nontruncated tree | context_only | {"identifier": "MediaIngredientMech:000170", "lookup_status": "completed_current_snapshot_absence", "index_data_rows": 9077, "index_matches": [], "catalog_rows": 2953, "catalog_matches": [], "catalog_source_key": "mimPinnedCatalog", "catalog_sha256": "474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7", "catalog_accessed_at": "2026-10-21T09:52:30.606764Z", "tree_entries": 7384, "tree_truncated": false, "tree_path_matches": [], "tree_source_key": "mimPinnedTree", "tree_sha256": "71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec", "tree_accessed_at": "2026-10-21T09:51:04.602158Z", "limit": "Current lookup is completed; historical correspondence remains unresolved. This legacy identifier is asserted on the target/owner, so it is distinct from merely unrelated parent context. No replacement mapping is inferred."} |
| history-metadata | data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml; data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml; data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml; data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:03.776971"}]}, {"input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:03.776971"}]}, {"input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:11.841156"}]}] |
| current-code-0 | src/culturemech/import/mediadive_importer.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive ingredient parsing selects the first solution and separates receiving stocks, while preparation aggregation may place all source solution steps at the main root. Cleanup retains the first conflicting duplicate rather than summing, and current lossless merging preserves scientific differences. These current behaviors do not authenticate the historical import or justify merging a strain wrapper solely on equal flattened ingredient values. Follow-up belongs in all three maintained contributors and authorized regeneration. |
| current-code-1 | scripts/cleanup_media_quality.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive ingredient parsing selects the first solution and separates receiving stocks, while preparation aggregation may place all source solution steps at the main root. Cleanup retains the first conflicting duplicate rather than summing, and current lossless merging preserves scientific differences. These current behaviors do not authenticate the historical import or justify merging a strain wrapper solely on equal flattened ingredient values. Follow-up belongs in all three maintained contributors and authorized regeneration. |
| current-code-2 | src/culturemech/merge/formulation.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive ingredient parsing selects the first solution and separates receiving stocks, while preparation aggregation may place all source solution steps at the main root. Cleanup retains the first conflicting duplicate rather than summing, and current lossless merging preserves scientific differences. These current behaviors do not authenticate the historical import or justify merging a strain wrapper solely on equal flattened ingredient values. Follow-up belongs in all three maintained contributors and authorized regeneration. |
| mediadive1315api-attempt | https://mediadive.dsmz.de/rest/medium/1315; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| komodo1315detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1315; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| komodo1315_1detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1315.1; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| mediadive1315api_retry-attempt | https://mediadive.dsmz.de/rest/medium/1315; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| solution2636-attempt | https://mediadive.dsmz.de/rest/solution/2636; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| solution2632-attempt | https://mediadive.dsmz.de/rest/solution/2632; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| solution2633-attempt | https://mediadive.dsmz.de/rest/solution/2633; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |
| solution926-attempt | https://mediadive.dsmz.de/rest/solution/926; Preserved exact public retrieval result | context_only | Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required historical correspondence for asserted MediaIngredientMech:000170 remains unavailable in the inspected evidence. The current negative lookup completed successfully and is not itself an unavailable check or proof that the legacy identifier was historically wrong.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and attempt timestamp. Available primary supports formulation comparison, so this optional access limit is distinct from required historical correspondence and branch clarification.
- Required exact correspondence between KOMODO 1315.1 strain-wrapper scope and the primary conditional substrate branch remains unresolved. Literal source lists differ; neither an inferred typo nor equal flattened ingredients resolves that identity.
- No source strain number is silently repaired, and no biological growth support is inferred. The optional capronate branch is retained separately from the catalog wrapper.
- No unqualified percentage basis, measured final volume or numeric autoclave cycle is invented. Current negative legacy lookup is complete, while historical linkage remains unresolved.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152505Z-culturemech-004072-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobic_thauera_medium (CultureMech:004072)'
started_at: '2026-10-21T15:15:04Z'
finished_at: '2026-10-21T15:25:05Z'
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
summary: DSMZ 1315 and the separate KOMODO 1315/1315.1 catalog identities are established.
  Four local layers flatten five stocks into direct concentrations and lose source
  assembly scope. Nickel hydration conflicts with its identifier; source conditional
  strain membership and legacy MIM000170 history remain unresolved.
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
  - path: data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
    sha256: 38fdd654d6679c5492e655d4297e8fe71dbaca713933f15fa52539355deb3c6d
    role: target
  - path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    sha256: d7a17405f9755c415aac31844b61aa2ccf8076885e8c2368d17f0380b8638a14
    role: context
  - path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
    sha256: 5542b7a0317b6b5a8bb3ed1b1ae979db548ad34e152a4ffc70e4466afa5dbad5
    role: context
  - path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    sha256: 022c5b9295e057a5babe96d2500765bfef2214fc4d3032bebdbac3171837697a
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/specialized/anaerobic_thauera_medium.yaml.md
    sha256: aa59c8102e3b5547bb49352ff6fcf3af1705dfa4c4a5abb9dda11b12052bb315
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/anaerobic_thauera_medium.yaml.md
    sha256: 732b851e8ed537952d1e880bdd072fddc3e283298aef8eede4e489f672441719
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml.md
    sha256: 7577c41041777d31a5e95218ac9ed0dc4a3b947a38782ce2cef4102474b78da4
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
  selection: Task review 266; batch 027 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-six task batches
    contain 260 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 263 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:004072
targets:
- target_id: CultureMech:004072
  path: data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  label: anaerobic_thauera_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/266/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/266/strict.tsv"
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:004072
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
  - CultureMech:004072
- check_id: legacy-current-lookup
  name: Exact current secondary catalog/index/tree lookup
  required: true
  status: passed
  summary: Completed negative lookup for MediaIngredientMech:000170; current absence
    established within the pinned complete snapshots, historical validity not adjudicated.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-search
- check_id: legacy-historical-correspondence
  name: Historical secondary identifier correspondence
  required: true
  status: unavailable
  summary: Required historical correspondence for asserted MediaIngredientMech:000170
    remains unavailable in the inspected evidence. The current negative lookup completed
    successfully and is not itself an unavailable check or proof that the legacy identifier
    was historically wrong.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-search
- check_id: mediadive1315api-source-access
  name: 'Exact source content access: mediadive1315api'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - mediadive1315api-attempt
- check_id: komodo1315detail-source-access
  name: 'Exact source content access: komodo1315detail'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - komodo1315detail-attempt
- check_id: komodo1315_1detail-source-access
  name: 'Exact source content access: komodo1315_1detail'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - komodo1315_1detail-attempt
- check_id: mediadive1315api_retry-source-access
  name: 'Exact source content access: mediadive1315api_retry'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - mediadive1315api_retry-attempt
- check_id: solution2636-source-access
  name: 'Exact source content access: solution2636'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - solution2636-attempt
- check_id: solution2632-source-access
  name: 'Exact source content access: solution2632'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - solution2632-attempt
- check_id: solution2633-source-access
  name: 'Exact source content access: solution2633'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - solution2633-attempt
- check_id: solution926-source-access
  name: 'Exact source content access: solution926'
  required: false
  status: unavailable
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - solution926-attempt
- check_id: strain-branch-correspondence
  name: Exact strain-wrapper to primary branch correspondence
  required: true
  status: unavailable
  summary: Required exact correspondence between KOMODO 1315.1 strain-wrapper scope
    and the primary conditional substrate branch remains unresolved. Literal source
    lists differ; neither an inferred typo nor equal flattened ingredients resolves
    that identity.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - catalog
  - primary
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:34.056713Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/266/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:35.170991Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/266/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:37.156408Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:38.414635Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:25:03Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml:1:id: CultureMech:004072

    ./data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml:1:id: CultureMech:004072

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/266/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:25:03Z'
  support: supports
  summary: 46 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 86b1f0a1febb7fb128981727b4904c1e1d52eba78b62bd3201cb81aa3b2d7c1d
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/266/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: 781a0bcc76827e88358e8545b14f0d3037ac75d547c51069a518ac2ba2094bce
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf
  locator: Complete two-page primary; main table, five stock sections and conditional
    substrate paragraph
  accessed_at: '2026-10-21T14:59:59.203064Z'
  support: supports
  summary: Primary distinguishes seven direct salts, five receiving stocks, their
    preparation and a conditional capronate substitution. Listed liquids total 1002
    mL; no measured final volume is asserted. Literal DSM 11243 is preserved and is
    not rewritten to 12143.
  snapshot_sha256: 964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564
- evidence_id: sl10-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: $.data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T11:03:05.357684Z'
  support: supports
  summary: Exact available SL-10 endpoint retains stock amounts and 1000 mL provider
    volume. Its HCl g_l 2.5 is a provider assertion, not evidence for an unstated
    percent basis. It does not recover the unavailable main response or authenticate
    historical import chronology.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact KOMODO rows 1315 and 1315.1 plus column headers
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Catalog separately identifies the main medium and the wrapper for DSM 12138,12139,12140,12143.
    This is identity metadata, not evidence equating that set with the primary conditional
    capronate set.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/266/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 8f79144127e01ee075c36a87395d4046ae4623d4f1e4ce39d43444e701ef5802
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
- evidence_id: chebi131531
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131531
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:00:00.508546Z'
  support: supports
  summary: CHEBI:131531 resolves to pyridoxamine hydrochloride. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: d2886129a812d1d1714de6967e7d679047d8e097d31ce06f4cc5f92034bdb536
- evidence_id: chebi132751
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:54.818359Z'
  support: supports
  summary: CHEBI:132751 resolves to thiamine hydrochloride dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
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
- evidence_id: chebi17154
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17154
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:46:50.867358Z'
  support: supports
  summary: CHEBI:17154 resolves to nicotinamide. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 45306ecefbab1f5ece64d269af2560e313330916a57d04fa168f19044dfe37d8
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
- evidence_id: chebi17883
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:25.439020Z'
  support: supports
  summary: CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
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
- evidence_id: chebi32029
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32029
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:00:00.694951Z'
  support: supports
  summary: CHEBI:32029 resolves to potassium acetate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ad3a69b398a98d72cdfc8e281c5c5c37f25059baa7675ca20adc51928cf2ba2c
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
- evidence_id: chebi3312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:16:24.822837Z'
  support: supports
  summary: CHEBI:3312 resolves to calcium dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
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
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
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
- evidence_id: chebi7916
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_7916
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:01:28.387666Z'
  support: supports
  summary: CHEBI:7916 resolves to pantothenic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 7b057eb0f384350a666b22dce9bd0529405271e968b5fe5fb69c63d74cc14122
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
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
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
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
- evidence_id: chebi91258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91258
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:28:27.054091Z'
  support: supports
  summary: CHEBI:91258 resolves to disodium hydrogenphosphate dihydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: f6c74e6e0b876aadf2fe47494521d320abb79244773bf4c44da7b288b1e27319
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:25:03Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131531": [{"label": "Pyridoxamine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:131531", "preferred_term":
    "Pyridoxamine hydrochloride", "ontology_id": "CHEBI:131531", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x
    2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term":
    "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid",
    "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier":
    "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term":
    "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier":
    "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label":
    "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term":
    "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32029": [{"label": "K-acetate", "match_type":
    "preferred_term", "identifier": "CHEBI:32029", "preferred_term": "K-acetate",
    "ontology_id": "CHEBI:32029", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id":
    "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118":
    [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118",
    "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213":
    [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:7916": [{"label": "Pantothenic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:7916", "preferred_term":
    "Pantothenic acid", "ontology_id": "CHEBI:7916", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id":
    "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318":
    [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86360": [{"label": "MnSO4", "match_type":
    "preferred_term", "identifier": "CHEBI:86360", "preferred_term": "MnSO4", "ontology_id":
    "CHEBI:86360", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91258": [{"label": "Na2HPO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91258", "preferred_term":
    "Na2HPO4 x 2 H2O", "ontology_id": "CHEBI:91258", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned current catalog/tree, exact legacy-key lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Current snapshot lookup for MediaIngredientMech:000170 completed negatively.
    It does not establish historical invalidity or an alternative linkage.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete pinned current catalog/tree, exact legacy-key lookup
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: Current snapshot lookup for MediaIngredientMech:000170 completed negatively.
    It does not establish historical invalidity or an alternative linkage.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-search
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/266/evidence-context-original.json
  locator: mim_provenance.legacy_lookup; complete 9077-row index, 2953-row catalog
    and 7384-entry nontruncated tree
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: '{"identifier": "MediaIngredientMech:000170", "lookup_status": "completed_current_snapshot_absence",
    "index_data_rows": 9077, "index_matches": [], "catalog_rows": 2953, "catalog_matches":
    [], "catalog_source_key": "mimPinnedCatalog", "catalog_sha256": "474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7",
    "catalog_accessed_at": "2026-10-21T09:52:30.606764Z", "tree_entries": 7384, "tree_truncated":
    false, "tree_path_matches": [], "tree_source_key": "mimPinnedTree", "tree_sha256":
    "71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec", "tree_accessed_at":
    "2026-10-21T09:51:04.602158Z", "limit": "Current lookup is completed; historical
    correspondence remains unresolved. This legacy identifier is asserted on the target/owner,
    so it is distinct from merely unrelated parent context. No replacement mapping
    is inferred."}'
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml; data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml;
    data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml; data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:03.776971"}]}, {"input": "data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml",
    "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:03.776971"}]}, {"input": "data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:11.841156"}]}]'
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Current MediaDive ingredient parsing selects the first solution and separates
    receiving stocks, while preparation aggregation may place all source solution
    steps at the main root. Cleanup retains the first conflicting duplicate rather
    than summing, and current lossless merging preserves scientific differences. These
    current behaviors do not authenticate the historical import or justify merging
    a strain wrapper solely on equal flattened ingredient values. Follow-up belongs
    in all three maintained contributors and authorized regeneration.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Current MediaDive ingredient parsing selects the first solution and separates
    receiving stocks, while preparation aggregation may place all source solution
    steps at the main root. Cleanup retains the first conflicting duplicate rather
    than summing, and current lossless merging preserves scientific differences. These
    current behaviors do not authenticate the historical import or justify merging
    a strain wrapper solely on equal flattened ingredient values. Follow-up belongs
    in all three maintained contributors and authorized regeneration.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: current-code-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:25:03Z'
  support: context_only
  summary: Current MediaDive ingredient parsing selects the first solution and separates
    receiving stocks, while preparation aggregation may place all source solution
    steps at the main root. Cleanup retains the first conflicting duplicate rather
    than summing, and current lossless merging preserves scientific differences. These
    current behaviors do not authenticate the historical import or justify merging
    a strain wrapper solely on equal flattened ingredient values. Follow-up belongs
    in all three maintained contributors and authorized regeneration.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: mediadive1315api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1315
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:59:58.481942Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo1315detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1315
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:59:58.217026Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 78bf301e56aa1610157b9a0b692a34f9f794ff2ad7246fca1f866f67da236ad2
- evidence_id: komodo1315_1detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1315.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:59:58.217447Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 0241a33357334c9cb43717d6e094e966d2770597f75be10437c75a7c2be4b7ef
- evidence_id: mediadive1315api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1315
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:49.950355Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution2636-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2636
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:04:29.869782Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution2632-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2632
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:04:29.869167Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution2633-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2633
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:04:29.869574Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution926-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/926
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:04:30.504060Z'
  support: context_only
  summary: Exact bound provider/detail access failed; preserve actual 503/403 response
    and attempt timestamp. Available primary supports formulation comparison, so this
    optional access limit is distinct from required historical correspondence and
    branch clarification.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 50 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Main: KNO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.85\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.85\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.85\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.85\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 0.85,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"KNO3 0.85 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Main: NaHCO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.52\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.52\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.52\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.52\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 2.52,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaHCO3 2.52 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Main: CaCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 0.01,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"CaCl2 0.01 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Main: MgSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 0.5,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Main: MnSO4\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 0.01,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"MnSO4 0.01 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Main: NH4Cl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 0.3,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.30 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Main: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_batch_mass_g\": 0.05,\n      \"listed_main_water_ml\": 884,\n\
    \      \"listed_liquids_sum_ml\": 1002,\n      \"measured_final_volume\": null\n\
    \    },\n    \"rationale\": \"The number matches the source batch mass, but local\
    \ g/L claims a final denominator not stated by this primary. Retain batch mass,\
    \ water and five receiving doses; no unavailable main API is treated as corroboration.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaCl 0.05 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"phosphate: Na2HPO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"14.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"phosphate\",\n      \"stock_mass_g\": 1.45,\n      \"\
    stock_water_ml\": 100,\n      \"receiving_dose_ml\": 100\n    },\n    \"rationale\"\
    : \"Stored 14.5/2.5/98 g/L are stock-strength values, not undiluted main ingredient\
    \ concentrations. Preserve explicit stock quantities and receiving doses.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 phosphate stock\",\n        \"exact_source_quote\"\
    : \"Na2HPO4 x 2 H2O 1.45 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"phosphate: KH2PO4\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"phosphate\",\n      \"stock_mass_g\": 0.25,\n      \"\
    stock_water_ml\": 100,\n      \"receiving_dose_ml\": 100\n    },\n    \"rationale\"\
    : \"Stored 14.5/2.5/98 g/L are stock-strength values, not undiluted main ingredient\
    \ concentrations. Preserve explicit stock quantities and receiving doses.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 phosphate stock\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.25 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"acetate: K-acetate\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"98\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"98\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"98\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"98\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"acetate\",\n      \"stock_mass_g\": 9.8,\n      \"stock_water_ml\"\
    : 100,\n      \"receiving_dose_ml\": 10\n    },\n    \"rationale\": \"Stored 14.5/2.5/98\
    \ g/L are stock-strength values, not undiluted main ingredient concentrations.\
    \ Preserve explicit stock quantities and receiving doses.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 1 acetate stock\",\n        \"exact_source_quote\"\
    : \"K-acetate 9.80 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Vitamin stock: Vitamin B12\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[10].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 50,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Vitamin B12 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"Vitamin stock: Pantothenic acid\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[11].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 50,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Pantothenic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Vitamin stock: Riboflavin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 50,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Vitamin stock: Pyridoxamine hydrochloride\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[13].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 10,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Pyridoxamine-HCl 10.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"Vitamin stock: Biotin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 20,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"Vitamin stock: Folic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 20,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"Vitamin stock: Nicotinic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 25,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Nicotinic acid 25.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"Vitamin stock: Nicotine amide\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 25,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Nicotine amide 25.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"Vitamin stock: alpha-lipoic acid\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 50,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"α-lipoic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Vitamin stock: p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 50,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"p-aminobenzoic acid 50.00 mg\",\n        \"\
    snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Vitamin stock: Thiamine-HCl x 2 H2O\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"stock_mass_mg\": 50,\n      \"listed_water_ml\"\
    : 1000,\n      \"receiving_dose_ml\": 5\n    },\n    \"rationale\": \"The source\
    \ stock mass and five-milliliter receiving dose must remain separate; the locally\
    \ stored stock-strength g/L is not the assembled-medium concentration.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin solution table across pages 1–2\",\n\
    \        \"exact_source_quote\": \"Thiamine-HCl x 2 H2O 50.00 mg\",\n        \"\
    snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"SL-10: HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 10,\n      \"unit\"\
    : \"ml\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": \"25%; 7.7 M\"\n    },\n    \"rationale\": \"Restore\
    \ stock scope and supplied form. The 25% basis remains unspecified while 7.7 M\
    \ is explicit. Provider stock g_l 2.5 does not justify that mass conversion or\
    \ its use as a main concentration.\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz1315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Trace element solution SL-10\",\n    \
    \    \"exact_source_quote\": \"HCl (25%; 7.7 M) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"SL-10: FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 1.5,\n      \"unit\"\
    : \"g\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"SL-10: ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[23].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 70,\n      \"unit\"\
    : \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"SL-10: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 100,\n      \"unit\"\
    : \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"SL-10: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 6,\n      \"unit\":\
    \ \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"SL-10: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[26].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 190,\n      \"unit\"\
    : \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"SL-10: CuCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[27].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 2,\n      \"unit\":\
    \ \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"SL-10: NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[28].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 24,\n      \"unit\"\
    : \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"SL-10: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[29].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"stock_amount\": 36,\n      \"unit\"\
    : \"mg\",\n      \"final_stock_makeup_ml\": 1000,\n      \"receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"Restore stock\
    \ scope and supplied form. Current stock endpoint corroborates the listed stock\
    \ amount, not a historical main-medium denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 2 Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Se/W: NaOH\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Se/W\",\n      \"stock_amount\": 0.5,\n      \"unit\"\
    : \"g\",\n      \"listed_water_ml\": 1000,\n      \"receiving_dose_ml\": 2\n \
    \   },\n    \"rationale\": \"The stock recipe requires its explicit two-milliliter\
    \ main addition; the flat g/L entries are not direct final-medium concentrations.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Selenite and tungstate solution\",\n \
    \       \"exact_source_quote\": \"NaOH 0.50 g\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Se/W: Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[31].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Se/W\",\n      \"stock_amount\": 3,\n      \"unit\": \"\
    mg\",\n      \"listed_water_ml\": 1000,\n      \"receiving_dose_ml\": 2\n    },\n\
    \    \"rationale\": \"The stock recipe requires its explicit two-milliliter main\
    \ addition; the flat g/L entries are not direct final-medium concentrations.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Selenite and tungstate solution\",\n \
    \       \"exact_source_quote\": \"Na2SeO3 x 5 H2O 3.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Se/W: Na2WO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"ingredients[32].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Se/W\",\n      \"stock_amount\": 4,\n      \"unit\": \"\
    mg\",\n      \"listed_water_ml\": 1000,\n      \"receiving_dose_ml\": 2\n    },\n\
    \    \"rationale\": \"The stock recipe requires its explicit two-milliliter main\
    \ addition; the flat g/L entries are not direct final-medium concentrations.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Selenite and tungstate solution\",\n \
    \       \"exact_source_quote\": \"Na2WO4 x 2 H2O 4.00 mg\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"water_ml\": 884\n    },\n    \"rationale\"\
    : \"Restore exact source solvent stage and unit. Main water is not the final volume;\
    \ SL-10 separately has an explicit final make-up.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"main table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 884.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"phosphate water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"phosphate\",\n      \"water_ml\": 100\n    },\n    \"\
    rationale\": \"Restore exact source solvent stage and unit. Main water is not\
    \ the final volume; SL-10 separately has an explicit final make-up.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"phosphate table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 100.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"acetate water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"acetate\",\n      \"water_ml\": 100\n    },\n    \"rationale\"\
    : \"Restore exact source solvent stage and unit. Main water is not the final volume;\
    \ SL-10 separately has an explicit final make-up.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"acetate table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 100.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"vitamins water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"water_ml\": 1000\n    },\n    \"\
    rationale\": \"Restore exact source solvent stage and unit. Main water is not\
    \ the final volume; SL-10 separately has an explicit final make-up.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"vitamins table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"SL-10 water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"water_ml\": 990\n    },\n    \"rationale\"\
    : \"Restore exact source solvent stage and unit. Main water is not the final volume;\
    \ SL-10 separately has an explicit final make-up.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"SL-10 table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Se/W water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Se/W\",\n      \"water_ml\": 1000\n    },\n    \"rationale\"\
    : \"Restore exact source solvent stage and unit. Main water is not the final volume;\
    \ SL-10 separately has an explicit final make-up.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Se/W table water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Se/W receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"Se/W\",\n      \"dose_ml\": 2,\n      \"listed_liquid_sum_including_water_ml\"\
    : 1002\n    },\n    \"rationale\": \"No structured solution receiving dose is\
    \ retained in any local layer. Restore the exact main addition without treating\
    \ all stock constituents as direct main concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main additions\",\n        \"exact_source_quote\"\
    : \"Selenite and tungstate solution  2.00 ml\",\n        \"snapshot_sha256\":\
    \ \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"phosphate receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"phosphate\",\n      \"dose_ml\": 100,\n      \"listed_liquid_sum_including_water_ml\"\
    : 1002\n    },\n    \"rationale\": \"No structured solution receiving dose is\
    \ retained in any local layer. Restore the exact main addition without treating\
    \ all stock constituents as direct main concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main additions\",\n        \"exact_source_quote\"\
    : \"Phosphate solution 100.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"acetate or conditional capronate receiving dose\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"acetate or conditional capronate\",\n      \"dose_ml\"\
    : 10,\n      \"listed_liquid_sum_including_water_ml\": 1002\n    },\n    \"rationale\"\
    : \"No structured solution receiving dose is retained in any local layer. Restore\
    \ the exact main addition without treating all stock constituents as direct main\
    \ concentrations.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main additions\",\n        \"exact_source_quote\"\
    : \"Acetate or capronate solution 10.00 ml\",\n        \"snapshot_sha256\": \"\
    964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n        \"\
    parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"vitamins receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"vitamins\",\n      \"dose_ml\": 5,\n      \"listed_liquid_sum_including_water_ml\"\
    : 1002\n    },\n    \"rationale\": \"No structured solution receiving dose is\
    \ retained in any local layer. Restore the exact main addition without treating\
    \ all stock constituents as direct main concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main additions\",\n        \"exact_source_quote\"\
    : \"Vitamin solution 5.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"SL-10 receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"SL-10\",\n      \"dose_ml\": 1,\n      \"listed_liquid_sum_including_water_ml\"\
    : 1002\n    },\n    \"rationale\": \"No structured solution receiving dose is\
    \ retained in any local layer. Restore the exact main addition without treating\
    \ all stock constituents as direct main concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main additions\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\"\
    : \"Conditional sodium capronate stock\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[2].description\",\n        \"stored\":\
    \ \"Filter sterilize and gas with N2. For strains DSM 12141, DSM 12142, DSM 11243\
    \ and DSM 12144, acetate may be replaced by Na-capronate (stock solution 2.76\
    \ g/100 ml).\",\n        \"decision\": \"correct\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"conditional_stock\": \"sodium capronate\",\n      \"mass_g\": 2.76,\n\
    \      \"stock_basis_ml\": 100,\n      \"may_replace\": \"acetate\",\n      \"\
    literal_strains\": [\n        \"DSM 12141\",\n        \"DSM 12142\",\n       \
    \ \"DSM 11243\",\n        \"DSM 12144\"\n      ]\n    },\n    \"rationale\": \"\
    The specialized owner retains the branch in main-root stock prose; other layers\
    \ omit it. Preserve the optional substitution and literal DSM 11243. The separate\
    \ KOMODO 1315.1 title lists a different strain set and does not establish branch\
    \ equivalence.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 acetate preparation, literal condition\"\
    ,\n        \"exact_source_quote\": \"For strains DSM 12141, DSM 12142, DSM 11243\
    \ and\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n   \
    \     \"source_locator\": \"Following line\",\n        \"exact_source_quote\"\
    : \"DSM 12144, acetate may be replaced by Na-capronate (stock solution 2.76 g/100\
    \ ml).\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"component_or_context\"\
    : \"Main gas composition\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[0].description\",\n        \"stored\":\
    \ \"Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic\
    \ conditions and autoclave. After cooling, add the phosphate solution, substrate\
    \ solution, vitamin solution and trace element solution. After mixing, pH should\
    \ be 7.1 - 7.5.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"N2_percent\": 90,\n      \"CO2_percent\": 10,\n      \"stage\": \"\
    main\"\n    },\n    \"rationale\": \"Recover absent target/KOMODO preparation;\
    \ retain specialized-owner source prose. Gas percentage basis is not independently\
    \ relabeled v/v.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1315\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic\"\
    ,\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q47\",\n    \"component_or_context\"\
    : \"Main final pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.1,\n          \"max\": 7.5\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.1,\n          \"max\": 7.5\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.1,\n          \"max\": 7.5\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.1,\n          \"max\": 7.5\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[0].description\",\n        \"stored\":\
    \ \"Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic\
    \ conditions and autoclave. After cooling, add the phosphate solution, substrate\
    \ solution, vitamin solution and trace element solution. After mixing, pH should\
    \ be 7.1 - 7.5.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"pH_range\": [\n        7.1,\n        7.5\n      ],\n      \"stage\"\
    : \"after mixing\"\n    },\n    \"rationale\": \"All four stored pH ranges agree\
    \ with the source final mixing stage; no attached evidence supports verified.\
    \ Preserve stage rather than inventing a stock pH.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"vitamin solution and trace element solution. After mixing, pH should be 7.1\
    \ - 7.5.\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q48\",\n    \"component_or_context\"\
    : \"SL-10 final make-up\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[4].description\",\n        \"stored\":\
    \ \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"final_stock_makeup_ml\": 1000,\n   \
    \   \"gas\": \"N2\",\n      \"sterilization\": \"autoclave\"\n    },\n    \"rationale\"\
    : \"The specialized owner retains the make-up at main root but omits the primary\
    \ trailing N2/autoclave instruction from this SL-10 step. Restore the complete\
    \ scoped stock instruction; do not treat 1000 mL as main final volume.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Page 2 SL-10 preparation\",\n        \"exact_source_quote\"\
    : \"Finally make up to 1000 ml. Distribute to gas tight vessels under N2, autoclave.\"\
    ,\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q49\",\n    \"component_or_context\"\
    : \"Vitamin stirring duration\",\n    \"decision\": \"not_quantified\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[3].description\",\n        \"stored\":\
    \ \"Stir for some hours, filter sterilize the solution.\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"duration\": \"some hours\",\n      \"stage\": \"vitamins\",\n   \
    \   \"sterilization\": \"filtration\"\n    },\n    \"rationale\": \"Retain this\
    \ qualitative duration and stock-specific filtration; no numerical time is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1315\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\"\
    ,\n        \"source_locator\": \"Vitamin stock preparation\",\n        \"exact_source_quote\"\
    : \"Stir for some hours, filter sterilize the solution.\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q50\",\n    \"component_or_context\"\
    : \"Autoclave cycle\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\",\n      \
    \  \"field_path\": \"preparation_steps[0].description\",\n        \"stored\":\
    \ \"Distribute to gas tight vessels, gas with 90% N2 +10% CO2 to achieve anaerobic\
    \ conditions and autoclave. After cooling, add the phosphate solution, substrate\
    \ solution, vitamin solution and trace element solution. After mixing, pH should\
    \ be 7.1 - 7.5.\",\n        \"decision\": \"evidence_only\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Distribute to gas tight vessels under N2, autoclave.\",\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[5].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[5].description\",\n        \"stored\"\
    : \"First dissolve NaOH, subsequently the metal salts. Distribute to gas tight\
    \ vessels under N2, autoclave.\",\n        \"decision\": \"correct\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[5].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[5].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"temperature\": null,\n      \"duration\": null\n    },\n    \"rationale\"\
    : \"Main, phosphate, SL-10 and Se/W autoclaving are source-scoped; a numeric cycle\
    \ is not specified. The specialized phosphate/Se-W instructions require their\
    \ stock containers; no default cycle is invented.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n       \
    \ \"source_locator\": \"Main preparation\",\n        \"exact_source_quote\": \"\
    conditions and autoclave.\",\n        \"snapshot_sha256\": \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\"\
    ,\n        \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1315\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1315.pdf\",\n   \
    \     \"source_locator\": \"Phosphate stock preparation\",\n        \"exact_source_quote\"\
    : \"Distribute to gas tight vessels under N2, autoclave.\",\n        \"snapshot_sha256\"\
    : \"964bfc90ff80e084f6eb2261adc015ba29d5d180505f8727da1b5c3756e93564\",\n    \
    \    \"parsed_text_sha256\": \"2013a10fbf3c397a39e94ce8c2452230e1c206c42bca166f0203398e3650add3\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '33 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 33/33
    primary and 31/33 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - chebi131361
  - chebi131531
  - chebi132751
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17154
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi31206
  - chebi31795
  - chebi32029
  - chebi32139
  - chebi32145
  - chebi33118
  - chebi3312
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63043
  - chebi63939
  - chebi75213
  - chebi7916
  - chebi86249
  - chebi86318
  - chebi86360
  - chebi86368
  - chebi91258
  details: 'Instance coverage on a 0–100 percent scale, denominator 33: primary 100.00%;
    secondary 93.94%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: legacy-correspondence
  area: grounding
  topic: Historical legacy linkage distinct from current CHEBI linkage
  outcome: concern
  summary: Required historical correspondence for asserted MediaIngredientMech:000170
    remains unavailable in the inspected evidence. The current negative lookup completed
    successfully and is not itself an unavailable check or proof that the legacy identifier
    was historically wrong.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-search
- assessment_id: identity
  area: identity
  topic: Main record and non-equivalent strain wrapper identity
  outcome: concern
  summary: The target joins main KOMODO 1315, DSMZ 1315 and KOMODO 1315.1 wrapper
    contributors. Stable IDs CultureMech:004072,015338,004071 resolve exactly and
    all ingredient lists match. Catalog 1315.1 names DSM 12138/12139/12140/12143;
    the primary capronate condition names DSM 12141/12142/11243/12144. Equal flattened
    ingredients do not establish equivalent strain/branch scope. Literal 11243 is
    not assumed a typo.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - id-search
  - catalog
  - primary
  - bound-owner-context
- assessment_id: evidence-scope
  area: evidence
  topic: Current sources and historical derivative limits
  outcome: concern
  summary: No local ingredient concentration has attached amount evidence. All 132
    concentration instances and source-only stock/preparation quantities are inventoried.
    Current primary is available; main API and several stock endpoints returned 503.
    Dated repository report quotations are derivative provenance with preserved hashes,
    not recovered raw historical responses or proof of source chronology.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - primary
  - quantity-inventory
  - bound-owner-context
  - sl10-provider
- assessment_id: preparation
  area: completeness
  topic: Main preparation recovery and stock separation
  outcome: concern
  summary: Only the specialized owner retains six preparation steps. Target and both
    KOMODO owners omit them. The source requires distinct main gas/after-cooling additions,
    phosphate handling, acetate filtration, vitamin filtration, SL-10 make-up and
    Se/W sequence. The specialized SL-10 step lacks the current primary N2/autoclave
    continuation and all stock steps remain detached at main root.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Supplied hydrates and generic vitamin identities
  outcome: concern
  summary: CHEBI:34887 is Cl2Ni, whereas source/local nickel is hexahydrate. Other
    asserted salt hydrates match their source rows; pantothenic acid and lipoic acid
    remain generic source-compatible identities. Nicotine amide is preserved source
    spelling for nicotinamide. The legacy nitrate linkage is assessed separately from
    valid CHEBI:63043.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - primary
  - chebi34887
  - chebi7916
  - chebi16494
  - chebi17154
  - chebi63043
- assessment_id: classification
  area: scope
  topic: Defined liquid composition and aerobic catalog note
  outcome: concern
  summary: 'DEFINED/DEFINED and LIQUID fit the named chemicals and absence of solidifier.
    Inherited Aerobic: Yes is a KOMODO catalog flag, not a growth or oxygen-tolerance
    conclusion; primary main preparation is explicitly anaerobic. No phenotype is
    inferred from the title or catalog flag.'
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - primary
  - catalog
- assessment_id: growth
  area: scope
  topic: Organism and graph assertion limits
  outcome: concern
  summary: The title and synonym contain source strain labels but no grounded organism
    CURIE or experimental growth claim. No internal path graph is asserted. The synonym
    must retain its distinct catalog provenance and unresolved relation to the conditional
    primary branch; no new taxonomy or growth inference is made.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - catalog
  - primary
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 37 timestamp instances inspected; 6 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
- assessment_id: current-writers
  area: provenance
  topic: Current writers and maintained input follow-up
  outcome: concern
  summary: Current MediaDive ingredient parsing selects the first solution and separates
    receiving stocks, while preparation aggregation may place all source solution
    steps at the main root. Cleanup retains the first conflicting duplicate rather
    than summing, and current lossless merging preserves scientific differences. These
    current behaviors do not authenticate the historical import or justify merging
    a strain wrapper solely on equal flattened ingredient values. Follow-up belongs
    in all three maintained contributors and authorized regeneration.
  target_ids:
  - CultureMech:004072
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
findings:
- finding_id: f1
  issue_key: culturemech.004072.legacy-secondary-correspondence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical secondary correspondence remains unresolved
  description: The inspected local layers assert MediaIngredientMech:000170 at ingredients[0].mediaingredientmech_term.
    The current exact lookup is negative, while the primary chemical name and CHEBI
    identifier can still be valid. Existing enrichment/migration history does not
    authenticate this historical mapping. This is a bounded provenance gap, not a
    confirmed wrong chemical or fabricated replacement.
  target_ids:
  - CultureMech:004072
  field_paths:
  - ingredients[0].mediaingredientmech_term
  - curation_history
  evidence_ids:
  - record
  - mim
  - mimPinnedCatalog
  - mimPinnedTree
  - legacy-search
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.004072.stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Five stock recipes are represented as direct medium concentrations
  description: All four local layers flatten phosphate, acetate, vitamins, SL-10 and
    Se/W recipes into the main list. For example potassium acetate is 98 g/L and stock
    phosphate 14.5/2.5 g/L. Main batch masses also acquire an unsupported g/L final
    basis, and HCl 2.5 g/L assumes unspecified percentage chemistry.
  target_ids:
  - CultureMech:004072
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.004072.nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate has an anhydrous identifier
  description: ingredients[28] names the hexahydrate but both primary and current
    secondary terms identify CHEBI:34887 Cl2Ni. Exact source and valid ontology labels
    expose a source-form mismatch.
  target_ids:
  - CultureMech:004072
  field_paths:
  - ingredients[28].term
  - ingredients[28].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.2
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.004072.preparation-loss-and-stock-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation is missing or detached from its stock
  description: Only the specialized owner retains the six source-derived steps; target
    and KOMODO contributors omit preparation. Stock steps need scope, and specialized
    SL-10 preparation lacks the source trailing N2/autoclave continuation.
  target_ids:
  - CultureMech:004072
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - owner-2
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  issue_key: culturemech.004072.strain-wrapper-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: A distinct strain-wrapper catalog entry is merged as a synonym without branch
    correspondence
  description: The target synonym and one owner identify KOMODO 1315.1 for DSM 12138,12139,12140,12143.
    Primary capronate substitution names DSM 12141,12142,11243,12144. These are not
    matching literal sets; source-supported equivalence or branch mapping is unavailable.
  target_ids:
  - CultureMech:004072
  field_paths:
  - synonyms
  - merged_from
  - media_term
  - curation_history
  evidence_ids:
  - record
  - owner-2
  - catalog
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: culturemech.004072.history-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Six history timestamp instances do not establish precise times
  description: Target and both KOMODO owners each retain one malformed fractional
    timestamp and one timezone-naive timestamp; all 37 historical events are preserved.
    Current matching ingredients do not establish historical branch identity or provider
    version.
  target_ids:
  - CultureMech:004072
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  description: Recover an exact historical identifier-to-ingredient correspondence
    or explicitly qualify the unresolved legacy assertion in the maintained owner.
    Preserve old history and append the result; do not infer a replacement from names
    or the current negative lookup.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:004072
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  description: Restore seven main batch masses, 884 mL water, five explicit stock
    doses and each stock composition in all maintained contributors, with branch scope
    retained. Preserve 1002 mL listed-liquid arithmetic without claiming measured
    final volume. Attach exact stage evidence before regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:004072
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  description: Verify source-compatible nickel-hydrate grounding separately for primary
    and secondary fields in all maintained contributors; do not fabricate a replacement
    identifier.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:004072
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  description: Recover source main preparation where absent; scope phosphate, substrate,
    vitamin, SL-10 and Se/W instructions to their own stocks, retaining conditional
    identities and the missing SL-10 continuation. Keep numeric cycle unspecified.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:004072
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  description: Retain exact catalog IDs and literal strain lists as separate provenance.
    Resolve wrapper/branch correspondence from exact supporting evidence before treating
    them as equivalent; preserve DSM11243 verbatim and do not introduce speculative
    corrections or taxonomy IDs.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:004072
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
  description: Preserve append-only history and qualify uncertain timestamps in a
    later authorized event; use explicit timezone-aware timestamps for new events.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:004072
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml
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
- Required historical correspondence for asserted MediaIngredientMech:000170 remains
  unavailable in the inspected evidence. The current negative lookup completed successfully
  and is not itself an unavailable check or proof that the legacy identifier was historically
  wrong.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Exact bound provider/detail access failed; preserve actual 503/403 response and
  attempt timestamp. Available primary supports formulation comparison, so this optional
  access limit is distinct from required historical correspondence and branch clarification.
- Required exact correspondence between KOMODO 1315.1 strain-wrapper scope and the
  primary conditional substrate branch remains unresolved. Literal source lists differ;
  neither an inferred typo nor equal flattened ingredients resolves that identity.
- No source strain number is silently repaired, and no biological growth support is
  inferred. The optional capronate branch is retained separately from the catalog
  wrapper.
- No unqualified percentage basis, measured final volume or numeric autoclave cycle
  is invented. Current negative legacy lookup is complete, while historical linkage
  remains unresolved.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-027
- generated-medium
```
