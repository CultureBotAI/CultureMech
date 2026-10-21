# Source and formulation review: anoxybacillus_medium (CultureMech:002061)

- Review: 20261021T162636Z-culturemech-002061-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T16:17:51Z
- Finished UTC: 2026-10-21T16:26:36Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 898 and 898a are distinct source recipes: the merged target combines 898a salt with 898 identity and preparation. Both owners flatten SL-10 and vitamins into direct ingredients and omit source water/doses. Exact source form and variant claims require curation; current primaries resolve their stated branches, while the historical normalization basis remains unauthenticated.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 283; batch 029 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-eight task batches contain 280 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 283 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002061 | data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml | generated | anoxybacillus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002061 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002061 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/283/strict.tsv |
| validate-terms | passed | True | CultureMech:002061 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002061 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002061 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required source assembly/denominator clarification | unavailable | True | CultureMech:002061 | Required historical authentication of the existing base-rate normalization remains unavailable: both primary recipes provide source inputs without a main final-volume statement, and all four exact API attempts failed503. The local approximate1.002 L basis is not established by the listed1002.5 mL liquid sum or unspecified late-stock volumes. Current source branch identity and explicit branch concentrations are available and assessed; partial completion is restricted to the unresolved base-rate provenance/volume basis. |
| Exact source content access: mediadive898api | unavailable | False | CultureMech:002061 | Exact mediadive898api returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |
| Exact source content access: mediadive898api_retry | unavailable | False | CultureMech:002061 | Exact mediadive898api_retry returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |
| Exact source content access: mediadive898aapi | unavailable | False | CultureMech:002061 | Exact mediadive898aapi returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |
| Exact source content access: mediadive898aapi_retry | unavailable | False | CultureMech:002061 | Exact mediadive898aapi_retry returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002061.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002061.

52 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.199601",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.199601",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.199601",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.2,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "KH2PO4 0.20 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "KH2PO4 0.20 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "MgCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.0998004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.0998004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.0998004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.1,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "MgCl2 x 6 H2O 0.10 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "MgCl2 x 6 H2O 0.10 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "KCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.199601",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.199601",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.199601",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.2,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "KCl 0.20 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "KCl 0.20 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "NH4Cl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.998004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.998004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.998004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 1,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NH4Cl 1.00 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NH4Cl 1.00 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Na2CO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.75449",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.75449",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.75449",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 2.76,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na2CO3 2.76 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na2CO3 2.76 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "NaHCO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "9.98004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "9.98004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "9.98004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 10,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaHCO3 10.00 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaHCO3 10.00 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.5,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Yeast extract 0.50 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Yeast extract 0.50 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "D-Glucose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 5,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "D-Glucose 5.00 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "D-Glucose 5.00 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Na2S x 9 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.5,
      "main_final_volume_ml": null,
      "final_g_per_l": null
    },
    "rationale": "Preserve the explicit batch mass. Local rates approximate division by 1.002 L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither sum establishes measured final volume. Keep source-specific preparation and branch substitutions separate.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "NaCl differs between the two source recipes",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "14.9701",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "14.9701",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "4.99002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "source_mass_g_by_accession": {
        "898": 5,
        "898a": 15
      },
      "target_identity": "898",
      "target_should_not_inherit": "898a salt rate",
      "final_g_per_l": null
    },
    "rationale": "The target identifies898 and retains its pH/procedure but carries the898a salt rate. Restore separate source recipes and literal batch amounts; do not select a convenient normalized denominator or change the898a owner to898 amounts.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaCl 5.00 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaCl 15.00 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Sodium-resazurin strength and dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.000499002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_strength": "0.1% w/v",
      "dose_ml": 0.5,
      "mass_g_per_receiving_batch": 0.0005,
      "final_g_per_l": null
    },
    "rationale": "0.1 g/100 mL times 0.5 mL equals 0.0005 g per receiving batch. This does not validate the stored final g/L or neutral-resazurin identifier.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "SL-10 HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 10,
      "source_unit": "ml",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": null
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. HCl 25% has no stated percentage basis, so 10 mL cannot be converted to 2.5 g or assigned a molarity.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "SL-10 FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 1.5,
      "source_unit": "g",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 1.5
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "SL-10 ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 70,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.07
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "SL-10 MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 100,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.1
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "SL-10 H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 6,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.006
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "SL-10 CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 190,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.19
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "SL-10 CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 2,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.002
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "SL-10 NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 24,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.024
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "SL-10 Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "source_amount": 36,
      "source_unit": "mg",
      "explicit_final_makeup_ml": 1000,
      "main_dose_ml": 1,
      "stock_g_per_l": 0.036
    },
    "rationale": "Move to the SL-10 stock and preserve source form. The explicit 1 L make-up supports stock mass concentration for solid solutes; the 1 mL dose is separate from main g/L. No finished-main-volume assumption is made.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Pages 1–2 SL-10 table",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "10x vitamin stock Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 20,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "10x vitamin stock Folic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 20,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "10x vitamin stock Pyridoxine hydrochloride",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 100,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "10x vitamin stock Thiamine HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 50,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "10x vitamin stock Riboflavin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 50,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "10x vitamin stock Nicotinic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 50,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "10x vitamin stock Calcium D-(+)-pantothenate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 50,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "10x vitamin stock Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 1,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "10x vitamin stock p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 50,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "10x vitamin stock (DL)-alpha-Lipoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock",
      "source_mass_mg": 50,
      "source_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_finished_stock_volume_ml": null
    },
    "rationale": "The vitamin mass belongs to the stock, not the main medium. The source lists 1000 mL water, without an explicit make-up instruction; keep the batch amount and 10x designation without treating the local direct g/L as verified.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 Wolin vitamin solution (10x) table",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "water_input_ml": 1000
    },
    "rationale": "Restore this source-only solvent or dose at its exact stage. Repeated water rows in different tables are not additive main-medium water.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "SL-10 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "water_input_ml": 990,
      "final_makeup_ml": 1000
    },
    "rationale": "Restore this source-only solvent or dose at its exact stage. Repeated water rows in different tables are not additive main-medium water.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "SL-10 table",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "SL-10 table",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Vitamin water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamins",
      "water_input_ml": 1000
    },
    "rationale": "Restore this source-only solvent or dose at its exact stage. Repeated water rows in different tables are not additive main-medium water.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 2 vitamin table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 2 vitamin table",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "SL-10 receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "main_dose_ml": 1,
      "stock": "SL-10"
    },
    "rationale": "Restore this source-only solvent or dose at its exact stage. Repeated water rows in different tables are not additive main-medium water.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Vitamin receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "main_dose_ml": 1,
      "stock": "Wolin vitamins 10x"
    },
    "rationale": "Restore this source-only solvent or dose at its exact stage. Repeated water rows in different tables are not additive main-medium water.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Main nitrogen and sparging duration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 8.5 - 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main sparging",
      "N2_percent": 100,
      "duration_min": [
        30,
        45
      ]
    },
    "rationale": "This context is already present in all layers and needs attached source evidence; no new cultivation or gas-basis claim is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Late-stock atmosphere",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 8.5 - 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "yeast/glucose/vitamins/sulfide late stocks",
      "N2_percent": 100,
      "unquantified_stock_strengths_and_doses": true
    },
    "rationale": "Retain the literal late-stock atmosphere and filtering qualifier; source unspecified stock strengths/volumes remain unknown.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 late-stock preparation",
        "exact_source_quote": "extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas.",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 late-stock preparation",
        "exact_source_quote": "extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas.",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "dsmz898 base pH stages",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 9.5,
          "max": 9.7
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 9.5,
          "max": 9.7
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "accession": "dsmz898",
      "initial_main_pH": [
        9,
        9.5
      ],
      "complete_main_pH": [
        9.5,
        9.7
      ]
    },
    "rationale": "Retain each owner and the898-labelled target pH according to its source. The merge problem is cross-source salt and identity selection, not proof that each stored pH is false. Source-specific relationship notes must acknowledge this difference.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main preparation ending",
        "exact_source_quote": "100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to\n9.5 - 9.7.",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "dsmz898a base pH stages",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 8.5 - 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 8.5,
          "max": 9.0
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "accession": "dsmz898a",
      "initial_main_pH": [
        8,
        8.5
      ],
      "complete_main_pH": [
        8.5,
        9
      ]
    },
    "rationale": "Retain each owner and the898-labelled target pH according to its source. The merge problem is cross-source salt and identity selection, not proof that each stored pH is false. Source-specific relationship notes must acknowledge this difference.",
    "source_snippets": [
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense under 100% N2 gas",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main preparation ending",
        "exact_source_quote": "100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to\n8.5 - 9.0.",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "SL-10 final make-up",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "final_makeup_ml": 1000
    },
    "rationale": "The instruction is retained locally but at main root; relocate it with the stock rather than treating 1000 mL as the complete medium volume.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "SL-10 preparation ending",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "SL-10 preparation ending",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Unquantified autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 8.5 - 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by filtration. Adjust pH of complete medium to 9.5 - 9.7.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "method": "autoclave",
      "temperature": null,
      "duration": null
    },
    "rationale": "Keep existing source ordering and vitamin filtration. No numerical cycle is provided.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      },
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "dsmz898 source-only DSM16504 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898",
      "strain": "DSM16504",
      "omit": "glucose",
      "betaine_g_per_l": 2.7,
      "Na2SO3_g_per_l": 0.65,
      "late_stock_N2_percent": 100
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 named DSM16504 paragraph",
        "exact_source_quote": "For DSM 16504: Omit glucose and add to the autoclaved medium 2.70 g/l betaine and 0.65\ng/l Na2SO3 from filter-sterilized anoxic stock solutions prepared under 100% N2 gas.",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "dsmz898 source-only DSM18346 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898",
      "strain": "DSM18346",
      "omit": "glucose",
      "yeast_g_per_l": 2,
      "final_pH": 8.5
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 named DSM18346 paragraph",
        "exact_source_quote": "For DSM 18346: Omit glucose, increase amount of yeast extract to 2.00 g/l. Adjust pH of\ncomplete medium to 8.5.",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "dsmz898 source-only DSM18978 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898",
      "strain": "DSM18978",
      "final_pH": 9
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf",
        "source_locator": "Page 1 named DSM18978 paragraph",
        "exact_source_quote": "For DSM 18978: Adjust pH of complete medium to 9.0.",
        "snapshot_sha256": "76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7",
        "parsed_text_sha256": "21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82",
        "accessed_at": "2026-10-21T15:56:58.627284Z"
      }
    ]
  },
  {
    "quantity_id": "q45",
    "component_or_context": "dsmz898a source-only DSM18345 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898a",
      "strain": "DSM18345",
      "replace": "glucose",
      "D_mannitol_g_per_l": 2.5,
      "final_pH": [
        9.5,
        9.7
      ]
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 named DSM18345 paragraph",
        "exact_source_quote": "For DSM 18345: Replace glucose with 2.50 g/l D-mannitol as substrate and adjust pH of\ncomplete medium to 9.5 - 9.7.",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q46",
    "component_or_context": "dsmz898a source-only DSM18979 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898a",
      "strain": "DSM18979",
      "omit": "D-glucose",
      "yeast_g_per_l": 2
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 named DSM18979 paragraph",
        "exact_source_quote": "For DSM 18979: Omit D-glucose and increase amount of yeast extract to 2.00 g/l.",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q47",
    "component_or_context": "dsmz898a source-only DSM100017 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898a",
      "strain": "DSM100017",
      "omit": "D-glucose",
      "yeast_g_per_l": 2,
      "thiosulfate_pentahydrate_g_per_l": 2.5,
      "crotonate_stock_dose_ml_per_l": 10,
      "crotonate_stock_M": 1
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 named DSM100017 paragraph",
        "exact_source_quote": "For DSM 100017: Omit D-glucose, increase amount of yeast extract to 2.00 g/l and add\n2.50 g/l Na2S2O3 x 5 H2O from an anoxic sterile stock solution after autoclaving. Prior to\ninoculation add 10.00 ml/l of a sterile anoxic 1 M Na-crotonate solution (see medium 870).",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q48",
    "component_or_context": "dsmz898a source-only DSM100337 branch",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": [
          {
            "path": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": "CultureMech:002062",
            "name": "anaerobacillus_medium",
            "notes": "NaCl increased from 4.99002 g/L to 14.9701 g/L while the DSMZ 898/898a base formulation remains unchanged."
          }
        ],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "variant_children",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "scope": "named collection branch only",
      "source_accession": "dsmz898a",
      "strain": "DSM100337",
      "replace": "D-glucose",
      "maltose_g_per_l": 5,
      "yeast_g_per_l": 1,
      "thiosulfate_pentahydrate_g_per_l": 2.5
    },
    "rationale": "These are separate source-supported branch instructions, absent from the local quantitative branch representation. Add only with exact parent/strain scope; omission is not a zero-valued ingredient, and this is not a new growth assertion or taxonomy assignment.",
    "source_snippets": [
      {
        "source_key": "dsmz898a",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf",
        "source_locator": "Page 1 named DSM100337 paragraph",
        "exact_source_quote": "For DSM 100337: Replace D-glucose with 5.00 g/l maltose, increase amount of yeast\nextract to 1.00 g/l and add 2.50 g/l Na2S2O3 x 5 H2O from an anoxic sterile stock solution\nafter autoclaving.",
        "snapshot_sha256": "5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36",
        "parsed_text_sha256": "2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46",
        "accessed_at": "2026-10-21T15:56:59.109033Z"
      }
    ]
  },
  {
    "quantity_id": "q49",
    "component_or_context": "Crotonic acid for DSM100017 only",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "crotonate stock for898a DSM100017",
      "mass_g": 86,
      "product_string": "ALDRICH 113018",
      "supplier_composition_not_independently_verified": true
    },
    "rationale": "This stock is relevant only through the explicit898a branch reference; it is not a basal898/898a ingredient or an invitation to transfer other DSM870 content.",
    "source_snippets": [
      {
        "source_key": "dsmz870",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf",
        "source_locator": "Page 2 Na-crotonate (1 M) table only",
        "exact_source_quote": "Crotonic acid (ALDRICH 113018) 86.00 g",
        "snapshot_sha256": "f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20",
        "parsed_text_sha256": "ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49",
        "accessed_at": "2026-10-21T13:16:27.838686Z"
      }
    ]
  },
  {
    "quantity_id": "q50",
    "component_or_context": "Crotonate base for DSM100017 only",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "crotonate stock for898a DSM100017",
      "normality": 10,
      "table_volume_ml": 100,
      "procedure_qualifier": "around"
    },
    "rationale": "This stock is relevant only through the explicit898a branch reference; it is not a basal898/898a ingredient or an invitation to transfer other DSM870 content.",
    "source_snippets": [
      {
        "source_key": "dsmz870",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf",
        "source_locator": "Page 2 Na-crotonate (1 M) table only",
        "exact_source_quote": "NaOH (10 N) 100.00 ml",
        "snapshot_sha256": "f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20",
        "parsed_text_sha256": "ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49",
        "accessed_at": "2026-10-21T13:16:27.838686Z"
      }
    ]
  },
  {
    "quantity_id": "q51",
    "component_or_context": "Crotonate table water for DSM100017 only",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "crotonate stock for898a DSM100017",
      "table_water_ml": 900
    },
    "rationale": "This stock is relevant only through the explicit898a branch reference; it is not a basal898/898a ingredient or an invitation to transfer other DSM870 content.",
    "source_snippets": [
      {
        "source_key": "dsmz870",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf",
        "source_locator": "Page 2 Na-crotonate (1 M) table only",
        "exact_source_quote": "Distilled water 900.00 ml",
        "snapshot_sha256": "f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20",
        "parsed_text_sha256": "ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49",
        "accessed_at": "2026-10-21T13:16:27.838686Z"
      }
    ]
  },
  {
    "quantity_id": "q52",
    "component_or_context": "Crotonate stock preparation quantities",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "crotonate stock for898a DSM100017",
      "initial_water_ml": 800,
      "base_around_ml": 100,
      "base_normality": 10,
      "approximate_pH": 7,
      "final_makeup_ml": 1000,
      "N2_percent": 100,
      "sterilization": "filtration"
    },
    "rationale": "Preserve the difference between table water and staged initial/make-up water. Approximate titrant volume and pH remain approximate; no density conversion is introduced.",
    "source_snippets": [
      {
        "source_key": "dsmz870",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf",
        "source_locator": "Page 2 Na-crotonate (1 M) preparation only",
        "exact_source_quote": "Dissolve crotonic acid in 800 ml distilled water, add around 100 ml of 10 N NaOH and\nadjust pH to around 7. Then add water to reach a volume of 1000 ml. Sterilize by filtration\nunder 100% N2 gas atmosphere.",
        "snapshot_sha256": "f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20",
        "parsed_text_sha256": "ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49",
        "accessed_at": "2026-10-21T13:16:27.838686Z"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:002061.

29 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 29/30 primary and 27/30 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 30: primary 96.67%; secondary 90.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002061.

26 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Two exact accessions and mismatched merged formula

identity: concern. Targets: CultureMech:002061.

Both stable owners and relationship paths resolve. DSM898 and898a share many ingredient identities but differ in salt, initial/final pH and named source branches. The target reports898 while carrying the898a salt amount. SALINITY_VARIANT notes in target/owners saying only salt differs contradict the captured primary pH instructions and the owners themselves.

### Source quantities and historical rate basis

evidence: concern. Targets: CultureMech:002061.

No ingredient amount evidence is attached in any layer. Current exact primary batch and stock quantities are available; all four current main API attempts failed503. These failures do not make the current primary branch comparison unavailable, but they leave the historical1.002 L normalization unauthenticated. Source branch g/L and mL/L quantities are explicit and distinct from this unresolved base denominator.

### Salt/hydrate and stereochemical distinctions

grounding: concern. Targets: CultureMech:002061.

Source sodium resazurin is mapped to neutral CHEBI:8806, and nickel chloride hexahydrate to CHEBI:34887 Cl2Ni in primary and secondary slots. Other asserted form metadata were inspected. Calcium D-(+)-pantothenate is explicitly D in both source tables; no DL-versus-D conflict is claimed. Generic CHEBI:16494 lipoic acid does not assert an unsupported specific enantiomer for the DL source. Unmapped yeast is a mixture linkage gap, not an invented identity.

### Main, stock and branch procedures

completeness: concern. Targets: CultureMech:002061.

Each maintained owner retains its own source-specific main pH/gas sequence. Main root also holds SL-10 make-up; all stock containers and dose/solvent inputs are absent. Seven named primary branches and the narrowly referenced crotonate stock are not quantitatively represented. Preserve stage and strain scope, approximate endpoints, filtration and sequencing; no sterilization cycle or unprinted late-stock volume can be supplied.

### Complex liquid recipe and biological scope

scope: supported. Targets: CultureMech:002061.

COMPLEX/SEMI_DEFINED and LIQUID are compatible with the yeast-extract recipe plus identified salts/stocks. The record has no target organism CURIE or graph-match assertion. Collection strain paragraphs are formulation branches, not newly verified growth, optimum or taxonomic assertions.

### Current writers and maintained input follow-up

provenance: concern. Targets: CultureMech:002061.

Current importer preserves later stock additions but collects preparation across sections. Current fingerprints compare ingredient identity, not quantity or pH; relationship writers can annotate topology without correcting formula content. Preserve the two source owners and their distinct pH/salt branches; correct source-specific stock topology and relationship prose before a separately authorized merge. Current implementation is not proof of historical causation.

## Findings

### f1: Merged target combines two distinct source recipes

blocker / open / confirmed; issue key: culturemech.002061.mixed-source-variant.

The target retains DSM898 identity and its pH/procedure but inherits898a NaCl14.9701 g/L. The two exact primaries specify different salt inputs, pH stages and strain branches; their ingredient-set fingerprint does not justify one hybrid formula.

### f2: SL-10 and vitamins are flattened into direct medium concentrations

blocker / open / confirmed; issue key: culturemech.002061.stock-and-basis-collapse.

All layers retain19 stock constituents as direct ingredients, omit stock doses/waters, and give unverified main normalization. HCl10 mL at an unqualified25% became2.5 g/L; no source percentage basis supports that conversion.

### f3: Sodium resazurin and nickel hydrate have incompatible groundings

major / open / confirmed; issue key: culturemech.002061.salt-hydrate-grounding.

The sodium-salt dye maps to neutral resazurin and nickel hexahydrate maps to nickel dichloride without waters. Matching canonical labels and current secondary keys do not establish correct supplied form.

### f4: Variant prose understates differences and stock preparation is detached

major / open / confirmed; issue key: culturemech.002061.variant-and-preparation-scope.

The target child note and owner relationship/modification notes say the base is unchanged or differs only in NaCl, despite different source pH sequences. Seven primary strain branches are absent; SL-10 make-up remains at main root.

## Recommended Actions And Acceptance Checks

### a1

Preserve source-specific898 and898a owners and prevent cross-source amount/pH selection during regeneration. Review the merge boundary using the actual formulation distinctions rather than fingerprint equality; do not change one owner to the other source.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore both complete stocks with their exact source quantities, forms, solvent/make-up and receiving doses. Restore explicit main batch inputs without inventing final volume, density or percentage basis; attach narrow evidence in each owner.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify exact source-compatible primary IDs and reassess secondary mappings independently. Preserve source masses and other explicitly supported stereochemical scope; do not infer replacement identifiers.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Correct active relationship prose in both owners to acknowledge pH and source-branch distinctions. Preserve the seven explicit branches without widening growth claims; recover only the referenced crotonate stock for DSM100017, and relocate SL-10 preparation with its stock. Append history instead of rewriting old events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/anaerobacillus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anoxybacillus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch029/283/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch029/283/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml:1:id: CultureMech:002061<br>./data/normalized_yaml/bacterial/anoxybacillus_medium.yaml:1:id: CultureMech:002061<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/283/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 36 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch029/source-preflight-bound/283/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| dsmz898 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf; Pages 1–2, complete recipe and explicit strain paragraphs | supports | DSMZ898 main, stock and three named branches read in full. Main batch, stock compositions, stock doses and strain-specific changes remain distinct. No main final-volume statement is printed. |
| dsmz898a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf; Pages 1–2, complete recipe and explicit strain paragraphs | supports | DSMZ898a main, stock and four named branches read in full. Main batch, stock compositions, stock doses and strain-specific changes remain distinct. No main final-volume statement is printed. |
| crotonate | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf; Page 2 Na-crotonate solution (1 M) subsection only | supports | Only the explicitly referenced crotonate stock transfers for DSM100017 in medium898a. Its water, base, make-up and gas instructions are stock-scoped. DSM870 basal formula, other stocks and unrelated variant do not transfer. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch029/283/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerobacillus_medium.yaml; data/normalized_yaml/bacterial/anoxybacillus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml", "events": 8, "timestamp_issues": []}] |
| current-code-0 | src/culturemech/import/mediadive_importer.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current importer preserves later stock additions but collects preparation across sections. Current fingerprints compare ingredient identity, not quantity or pH; relationship writers can annotate topology without correcting formula content. Preserve the two source owners and their distinct pH/salt branches; correct source-specific stock topology and relationship prose before a separately authorized merge. Current implementation is not proof of historical causation. |
| current-code-1 | src/culturemech/merge/merger.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current importer preserves later stock additions but collects preparation across sections. Current fingerprints compare ingredient identity, not quantity or pH; relationship writers can annotate topology without correcting formula content. Preserve the two source owners and their distinct pH/salt branches; correct source-specific stock topology and relationship prose before a separately authorized merge. Current implementation is not proof of historical causation. |
| current-code-2 | src/culturemech/merge/fingerprint.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current importer preserves later stock additions but collects preparation across sections. Current fingerprints compare ingredient identity, not quantity or pH; relationship writers can annotate topology without correcting formula content. Preserve the two source owners and their distinct pH/salt branches; correct source-specific stock topology and relationship prose before a separately authorized merge. Current implementation is not proof of historical causation. |
| current-code-3 | scripts/propose_media_variant_links.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current importer preserves later stock additions but collects preparation across sections. Current fingerprints compare ingredient identity, not quantity or pH; relationship writers can annotate topology without correcting formula content. Preserve the two source owners and their distinct pH/salt branches; correct source-specific stock topology and relationship prose before a separately authorized merge. Current implementation is not proof of historical causation. |
| current-code-4 | scripts/apply_media_variant_links.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current importer preserves later stock additions but collects preparation across sections. Current fingerprints compare ingredient identity, not quantity or pH; relationship writers can annotate topology without correcting formula content. Preserve the two source owners and their distinct pH/salt branches; correct source-specific stock topology and relationship prose before a separately authorized merge. Current implementation is not proof of historical causation. |
| mediadive898api-attempt | https://mediadive.dsmz.de/rest/medium/898; Preserved exact public retrieval result | context_only | Exact mediadive898api returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |
| mediadive898api_retry-attempt | https://mediadive.dsmz.de/rest/medium/898; Preserved exact public retrieval result | context_only | Exact mediadive898api_retry returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |
| mediadive898aapi-attempt | https://mediadive.dsmz.de/rest/medium/898a; Preserved exact public retrieval result | context_only | Exact mediadive898aapi returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |
| mediadive898aapi_retry-attempt | https://mediadive.dsmz.de/rest/medium/898a; Preserved exact public retrieval result | context_only | Exact mediadive898aapi_retry returned503; preserved error body is not recipe evidence and does not establish chronology or absence. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required historical authentication of the existing base-rate normalization remains unavailable: both primary recipes provide source inputs without a main final-volume statement, and all four exact API attempts failed503. The local approximate1.002 L basis is not established by the listed1002.5 mL liquid sum or unspecified late-stock volumes. Current source branch identity and explicit branch concentrations are available and assessed; partial completion is restricted to the unresolved base-rate provenance/volume basis.
- Exact mediadive898api returned503; preserved error body is not recipe evidence and does not establish chronology or absence.
- Exact mediadive898api_retry returned503; preserved error body is not recipe evidence and does not establish chronology or absence.
- Exact mediadive898aapi returned503; preserved error body is not recipe evidence and does not establish chronology or absence.
- Exact mediadive898aapi_retry returned503; preserved error body is not recipe evidence and does not establish chronology or absence.
- The parent320 and120 recipes are not imported: both child primaries already reproduce complete SL-10 and vitamin tables. Only the explicit DSM870 crotonate subsection transfers. Captured source dates do not establish whether historical provider or current primary changed first.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162636Z-culturemech-002061-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anoxybacillus_medium (CultureMech:002061)'
started_at: '2026-10-21T16:17:51Z'
finished_at: '2026-10-21T16:26:36Z'
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
summary: 'DSMZ 898 and 898a are distinct source recipes: the merged target combines
  898a salt with 898 identity and preparation. Both owners flatten SL-10 and vitamins
  into direct ingredients and omit source water/doses. Exact source form and variant
  claims require curation; current primaries resolve their stated branches, while
  the historical normalization basis remains unauthenticated.'
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
  - path: data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
    sha256: 0e6f1ffa97d1dce417ebc1a69f709202db255ea51d7b16cb94142c139bbb5829
    role: target
  - path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    sha256: af0e9a5f5f5cb20b642891691eeb64cf1e6fdf76682000b63b9f3ba6da0403ef
    role: context
  - path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
    sha256: 963daee2fb57a383ec32e1894e7a22c18a42f5c9a9baabf408829c6a6dd968a9
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
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
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
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
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
  selection: Task review 283; batch 029 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-eight task batches
    contain 280 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 283 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002061
targets:
- target_id: CultureMech:002061
  path: data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  label: anoxybacillus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch029/283/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/283/strict.tsv"
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002061
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
  - CultureMech:002061
- check_id: source-assembly-basis
  name: Required source assembly/denominator clarification
  required: true
  status: unavailable
  summary: 'Required historical authentication of the existing base-rate normalization
    remains unavailable: both primary recipes provide source inputs without a main
    final-volume statement, and all four exact API attempts failed503. The local approximate1.002
    L basis is not established by the listed1002.5 mL liquid sum or unspecified late-stock
    volumes. Current source branch identity and explicit branch concentrations are
    available and assessed; partial completion is restricted to the unresolved base-rate
    provenance/volume basis.'
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - dsmz898
  - dsmz898a
  - quantity-inventory
- check_id: mediadive898api-source-access
  name: 'Exact source content access: mediadive898api'
  required: false
  status: unavailable
  summary: Exact mediadive898api returned503; preserved error body is not recipe evidence
    and does not establish chronology or absence.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - mediadive898api-attempt
- check_id: mediadive898api_retry-source-access
  name: 'Exact source content access: mediadive898api_retry'
  required: false
  status: unavailable
  summary: Exact mediadive898api_retry returned503; preserved error body is not recipe
    evidence and does not establish chronology or absence.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - mediadive898api_retry-attempt
- check_id: mediadive898aapi-source-access
  name: 'Exact source content access: mediadive898aapi'
  required: false
  status: unavailable
  summary: Exact mediadive898aapi returned503; preserved error body is not recipe
    evidence and does not establish chronology or absence.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - mediadive898aapi-attempt
- check_id: mediadive898aapi_retry-source-access
  name: 'Exact source content access: mediadive898aapi_retry'
  required: false
  status: unavailable
  summary: Exact mediadive898aapi_retry returned503; preserved error body is not recipe
    evidence and does not establish chronology or absence.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - mediadive898aapi_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:11.309500Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch029/283/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:13.010609Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-029/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch029/283/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:14.507181Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T16:18:15.421609Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T16:26:35Z'
  support: supports
  summary: './data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml:1:id: CultureMech:002061

    ./data/normalized_yaml/bacterial/anoxybacillus_medium.yaml:1:id: CultureMech:002061

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/283/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T16:26:35Z'
  support: supports
  summary: 36 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 0eb8cd2678bf3b4b442e694b1104f4eacabe899d5fd5d819e63a6a8c0d8db0a6
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/source-preflight-bound/283/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: 985a92a39f6727d731691f9fa577f5f8c8f225c50c497bf1eee9a9813dc350f1
- evidence_id: dsmz898
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf
  locator: Pages 1–2, complete recipe and explicit strain paragraphs
  accessed_at: '2026-10-21T15:56:58.627284Z'
  support: supports
  summary: DSMZ898 main, stock and three named branches read in full. Main batch,
    stock compositions, stock doses and strain-specific changes remain distinct. No
    main final-volume statement is printed.
  snapshot_sha256: 76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7
- evidence_id: dsmz898a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf
  locator: Pages 1–2, complete recipe and explicit strain paragraphs
  accessed_at: '2026-10-21T15:56:59.109033Z'
  support: supports
  summary: DSMZ898a main, stock and four named branches read in full. Main batch,
    stock compositions, stock doses and strain-specific changes remain distinct. No
    main final-volume statement is printed.
  snapshot_sha256: 5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36
- evidence_id: crotonate
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf
  locator: Page 2 Na-crotonate solution (1 M) subsection only
  accessed_at: '2026-10-21T13:16:27.838686Z'
  support: supports
  summary: Only the explicitly referenced crotonate stock transfers for DSM100017
    in medium898a. Its water, base, make-up and gas instructions are stock-scoped.
    DSM870 basal formula, other stocks and unrelated variant do not transfer.
  snapshot_sha256: f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch029/283/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 81ff7c765cd1c993424cdf448eb7dceaa457a38fafe349e7b170b59f380c0a70
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
- evidence_id: chebi17634
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:33.425023Z'
  support: supports
  summary: CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d11b31a8e91c3fffe7744f612dab69cdb4e02f42068cd2eb1458acee4503a62f
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
  accessed_at: '2026-10-21T16:26:35Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15940":
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
    "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634",
    "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:176843": [{"label":
    "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label":
    "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label":
    "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753":
    [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label":
    "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961",
    "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term",
    "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label":
    "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label":
    "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209":
    [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209",
    "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerobacillus_medium.yaml;
    data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/anaerobacillus_medium.yaml", "events": 8, "timestamp_issues":
    []}, {"input": "data/normalized_yaml/bacterial/anoxybacillus_medium.yaml", "events":
    8, "timestamp_issues": []}]'
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Current importer preserves later stock additions but collects preparation
    across sections. Current fingerprints compare ingredient identity, not quantity
    or pH; relationship writers can annotate topology without correcting formula content.
    Preserve the two source owners and their distinct pH/salt branches; correct source-specific
    stock topology and relationship prose before a separately authorized merge. Current
    implementation is not proof of historical causation.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Current importer preserves later stock additions but collects preparation
    across sections. Current fingerprints compare ingredient identity, not quantity
    or pH; relationship writers can annotate topology without correcting formula content.
    Preserve the two source owners and their distinct pH/salt branches; correct source-specific
    stock topology and relationship prose before a separately authorized merge. Current
    implementation is not proof of historical causation.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: current-code-2
  kind: record_content
  reference: src/culturemech/merge/fingerprint.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Current importer preserves later stock additions but collects preparation
    across sections. Current fingerprints compare ingredient identity, not quantity
    or pH; relationship writers can annotate topology without correcting formula content.
    Preserve the two source owners and their distinct pH/salt branches; correct source-specific
    stock topology and relationship prose before a separately authorized merge. Current
    implementation is not proof of historical causation.
  snapshot_sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
- evidence_id: current-code-3
  kind: record_content
  reference: scripts/propose_media_variant_links.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Current importer preserves later stock additions but collects preparation
    across sections. Current fingerprints compare ingredient identity, not quantity
    or pH; relationship writers can annotate topology without correcting formula content.
    Preserve the two source owners and their distinct pH/salt branches; correct source-specific
    stock topology and relationship prose before a separately authorized merge. Current
    implementation is not proof of historical causation.
  snapshot_sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
- evidence_id: current-code-4
  kind: record_content
  reference: scripts/apply_media_variant_links.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T16:26:35Z'
  support: context_only
  summary: Current importer preserves later stock additions but collects preparation
    across sections. Current fingerprints compare ingredient identity, not quantity
    or pH; relationship writers can annotate topology without correcting formula content.
    Preserve the two source owners and their distinct pH/salt branches; correct source-specific
    stock topology and relationship prose before a separately authorized merge. Current
    implementation is not proof of historical causation.
  snapshot_sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
- evidence_id: mediadive898api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/898
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:56:57.350968Z'
  support: context_only
  summary: Exact mediadive898api returned503; preserved error body is not recipe evidence
    and does not establish chronology or absence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive898api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/898
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:09.142828Z'
  support: context_only
  summary: Exact mediadive898api_retry returned503; preserved error body is not recipe
    evidence and does not establish chronology or absence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive898aapi-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/898a
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:56:57.673353Z'
  support: context_only
  summary: Exact mediadive898aapi returned503; preserved error body is not recipe
    evidence and does not establish chronology or absence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive898aapi_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/898a
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T16:01:09.774283Z'
  support: context_only
  summary: Exact mediadive898aapi_retry returned503; preserved error body is not recipe
    evidence and does not establish chronology or absence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 52 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    KH2PO4\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.199601\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.199601\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.199601\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main batch\",\n      \"source_mass_g\": 0.2,\n      \"\
    main_final_volume_ml\": null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\"\
    : \"Preserve the explicit batch mass. Local rates approximate division by 1.002\
    \ L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes,\
    \ and neither sum establishes measured final volume. Keep source-specific preparation\
    \ and branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.20 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.20 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"MgCl2\
    \ x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.0998004\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0998004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0998004\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main batch\",\n      \"source_mass_g\": 0.1,\n      \"\
    main_final_volume_ml\": null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\"\
    : \"Preserve the explicit batch mass. Local rates approximate division by 1.002\
    \ L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes,\
    \ and neither sum establishes measured final volume. Keep source-specific preparation\
    \ and branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 0.10 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 0.10 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"KCl\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.199601\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.199601\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.199601\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 0.2,\n      \"main_final_volume_ml\"\
    : null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\": \"Preserve\
    \ the explicit batch mass. Local rates approximate division by 1.002 L; primary\
    \ listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither\
    \ sum establishes measured final volume. Keep source-specific preparation and\
    \ branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"KCl 0.20 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"KCl 0.20 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"NH4Cl\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.998004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.998004\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.998004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 1,\n      \"main_final_volume_ml\"\
    : null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\": \"Preserve\
    \ the explicit batch mass. Local rates approximate division by 1.002 L; primary\
    \ listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither\
    \ sum establishes measured final volume. Keep source-specific preparation and\
    \ branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 1.00 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 1.00 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\": \"Na2CO3\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2.75449\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.75449\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2.75449\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 2.76,\n      \"main_final_volume_ml\"\
    : null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\": \"Preserve\
    \ the explicit batch mass. Local rates approximate division by 1.002 L; primary\
    \ listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither\
    \ sum establishes measured final volume. Keep source-specific preparation and\
    \ branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na2CO3 2.76 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na2CO3 2.76 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\": \"NaHCO3\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"9.98004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.98004\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"9.98004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 10,\n      \"main_final_volume_ml\"\
    : null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\": \"Preserve\
    \ the explicit batch mass. Local rates approximate division by 1.002 L; primary\
    \ listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither\
    \ sum establishes measured final volume. Keep source-specific preparation and\
    \ branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaHCO3 10.00 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaHCO3 10.00 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"Yeast\
    \ extract\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"ingredients[8].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main batch\",\n      \"source_mass_g\": 0.5,\n      \"\
    main_final_volume_ml\": null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\"\
    : \"Preserve the explicit batch mass. Local rates approximate division by 1.002\
    \ L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes,\
    \ and neither sum establishes measured final volume. Keep source-specific preparation\
    \ and branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 0.50 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 0.50 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\": \"D-Glucose\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"4.99002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 5,\n      \"main_final_volume_ml\"\
    : null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\": \"Preserve\
    \ the explicit batch mass. Local rates approximate division by 1.002 L; primary\
    \ listed liquids total 1002.5 mL before unspecified late-stock volumes, and neither\
    \ sum establishes measured final volume. Keep source-specific preparation and\
    \ branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"D-Glucose 5.00 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"D-Glucose 5.00 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\": \"Na2S\
    \ x 9 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.499002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.499002\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main batch\",\n      \"source_mass_g\": 0.5,\n      \"\
    main_final_volume_ml\": null,\n      \"final_g_per_l\": null\n    },\n    \"rationale\"\
    : \"Preserve the explicit batch mass. Local rates approximate division by 1.002\
    \ L; primary listed liquids total 1002.5 mL before unspecified late-stock volumes,\
    \ and neither sum establishes measured final volume. Keep source-specific preparation\
    \ and branch substitutions separate.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\": \"NaCl\
    \ differs between the two source recipes\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.9701\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"14.9701\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.99002\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"source_mass_g_by_accession\": {\n        \"898\": 5,\n        \"\
    898a\": 15\n      },\n      \"target_identity\": \"898\",\n      \"target_should_not_inherit\"\
    : \"898a salt rate\",\n      \"final_g_per_l\": null\n    },\n    \"rationale\"\
    : \"The target identifies898 and retains its pH/procedure but carries the898a\
    \ salt rate. Restore separate source recipes and literal batch amounts; do not\
    \ select a convenient normalized denominator or change the898a owner to898 amounts.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz898\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaCl 5.00 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaCl 15.00 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\": \"Sodium-resazurin\
    \ strength and dose\",\n    \"decision\": \"correct\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.000499002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stock_strength\": \"0.1% w/v\",\n      \"dose_ml\": 0.5,\n      \"mass_g_per_receiving_batch\"\
    : 0.0005,\n      \"final_g_per_l\": null\n    },\n    \"rationale\": \"0.1 g/100\
    \ mL times 0.5 mL equals 0.0005 g per receiving batch. This does not validate\
    \ the stored final g/L or neutral-resazurin identifier.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\": \"Sodium\
    \ resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\": \"SL-10\
    \ HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n   \
    \     \"field_path\": \"ingredients[11].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 10,\n      \"\
    source_unit\": \"ml\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": null\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ HCl 25% has no stated percentage basis, so 10 mL cannot be converted to 2.5\
    \ g or assigned a molarity.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\": \"SL-10\
    \ FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 1.5,\n      \"\
    source_unit\": \"g\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 1.5\n    },\n    \"rationale\": \"Move to the SL-10\
    \ stock and preserve source form. The explicit 1 L make-up supports stock mass\
    \ concentration for solid solutes; the 1 mL dose is separate from main g/L. No\
    \ finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\": \"SL-10\
    \ ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 70,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.07\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ No finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\": \"SL-10\
    \ MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 100,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.1\n    },\n    \"rationale\": \"Move to the SL-10\
    \ stock and preserve source form. The explicit 1 L make-up supports stock mass\
    \ concentration for solid solutes; the 1 mL dose is separate from main g/L. No\
    \ finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\": \"SL-10\
    \ H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 6,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.006\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ No finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"SL-10\
    \ CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 190,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.19\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ No finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\": \"SL-10\
    \ CuCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 2,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.002\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ No finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"SL-10\
    \ NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 24,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.024\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ No finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\": \"SL-10\
    \ Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"source_amount\": 36,\n      \"\
    source_unit\": \"mg\",\n      \"explicit_final_makeup_ml\": 1000,\n      \"main_dose_ml\"\
    : 1,\n      \"stock_g_per_l\": 0.036\n    },\n    \"rationale\": \"Move to the\
    \ SL-10 stock and preserve source form. The explicit 1 L make-up supports stock\
    \ mass concentration for solid solutes; the 1 mL dose is separate from main g/L.\
    \ No finished-main-volume assumption is made.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2 SL-10 table\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Biotin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 20,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Folic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 20,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Pyridoxine hydrochloride\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 100,\n   \
    \   \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\",\n   \
    \     \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\",\n   \
    \     \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Thiamine HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 50,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Riboflavin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[24].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 50,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Nicotinic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 50,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Calcium D-(+)-pantothenate\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 50,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\",\n  \
    \      \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\",\n  \
    \      \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\": \"10x\
    \ vitamin stock Vitamin B12\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 1,\n     \
    \ \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\": \"10x\
    \ vitamin stock p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[28].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 50,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n        \"\
    snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n        \"\
    snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\": \"10x\
    \ vitamin stock (DL)-alpha-Lipoic acid\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[29].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock\",\n      \"source_mass_mg\": 50,\n    \
    \  \"source_water_input_ml\": 1000,\n      \"main_dose_ml\": 1,\n      \"measured_finished_stock_volume_ml\"\
    : null\n    },\n    \"rationale\": \"The vitamin mass belongs to the stock, not\
    \ the main medium. The source lists 1000 mL water, without an explicit make-up\
    \ instruction; keep the batch amount and 10x designation without treating the\
    \ local direct g/L as verified.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\",\n      \
    \  \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Wolin vitamin solution (10x) table\",\n\
    \        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\",\n      \
    \  \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\": \"Main\
    \ water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"water_input_ml\": 1000\n    },\n    \"\
    rationale\": \"Restore this source-only solvent or dose at its exact stage. Repeated\
    \ water rows in different tables are not additive main-medium water.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz898\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\": \"SL-10\
    \ water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"water_input_ml\": 990,\n      \"final_makeup_ml\"\
    : 1000\n    },\n    \"rationale\": \"Restore this source-only solvent or dose\
    \ at its exact stage. Repeated water rows in different tables are not additive\
    \ main-medium water.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"SL-10 table\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"SL-10 table\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\": \"Vitamin\
    \ water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamins\",\n      \"water_input_ml\": 1000\n    },\n\
    \    \"rationale\": \"Restore this source-only solvent or dose at its exact stage.\
    \ Repeated water rows in different tables are not additive main-medium water.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz898\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 2 vitamin table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 2 vitamin table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\": \"SL-10\
    \ receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_dose_ml\": 1,\n      \"stock\": \"SL-10\"\n    },\n    \"rationale\"\
    : \"Restore this source-only solvent or dose at its exact stage. Repeated water\
    \ rows in different tables are not additive main-medium water.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\": \"Trace\
    \ element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\": \"Vitamin\
    \ receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"main_dose_ml\": 1,\n      \"stock\": \"Wolin vitamins 10x\"\n   \
    \ },\n    \"rationale\": \"Restore this source-only solvent or dose at its exact\
    \ stage. Repeated water rows in different tables are not additive main-medium\
    \ water.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz898\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n        \"\
    parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n        \"\
    parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\": \"Main\
    \ nitrogen and sparging duration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense\
    \ under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by\
    \ filtration. Adjust pH of complete medium to 8.5 - 9.0.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"main sparging\",\n      \"N2_percent\": 100,\n      \"\
    duration_min\": [\n        30,\n        45\n      ]\n    },\n    \"rationale\"\
    : \"This context is already present in all layers and needs attached source evidence;\
    \ no new cultivation or gas-basis claim is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add\
    \ carbonate\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add\
    \ carbonate\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\": \"Late-stock\
    \ atmosphere\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense\
    \ under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by\
    \ filtration. Adjust pH of complete medium to 8.5 - 9.0.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"yeast/glucose/vitamins/sulfide late stocks\",\n      \"\
    N2_percent\": 100,\n      \"unquantified_stock_strengths_and_doses\": true\n \
    \   },\n    \"rationale\": \"Retain the literal late-stock atmosphere and filtering\
    \ qualifier; source unspecified stock strengths/volumes remain unknown.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz898\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 late-stock preparation\",\n        \"\
    exact_source_quote\": \"extract, glucose, vitamins and sulfide from sterile anoxic\
    \ stock solutions prepared under\\n100% N2 gas.\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 late-stock preparation\",\n        \"\
    exact_source_quote\": \"extract, glucose, vitamins and sulfide from sterile anoxic\
    \ stock solutions prepared under\\n100% N2 gas.\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\": \"dsmz898\
    \ base pH stages\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 9.5,\n          \"max\": 9.7\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 9.5,\n          \"max\": 9.7\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"accession\"\
    : \"dsmz898\",\n      \"initial_main_pH\": [\n        9,\n        9.5\n      ],\n\
    \      \"complete_main_pH\": [\n        9.5,\n        9.7\n      ]\n    },\n \
    \   \"rationale\": \"Retain each owner and the898-labelled target pH according\
    \ to its source. The merge problem is cross-source salt and identity selection,\
    \ not proof that each stored pH is false. Source-specific relationship notes must\
    \ acknowledge this difference.\",\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense medium under 100%\
    \ N2 gas\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation ending\",\n        \"\
    exact_source_quote\": \"100% N2 gas. Vitamins should be sterilized by filtration.\
    \ Adjust pH of complete medium to\\n9.5 - 9.7.\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\": \"dsmz898a\
    \ base pH stages\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense\
    \ under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by\
    \ filtration. Adjust pH of complete medium to 8.5 - 9.0.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 8.5,\n          \"max\": 9.0\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"accession\"\
    : \"dsmz898a\",\n      \"initial_main_pH\": [\n        8,\n        8.5\n     \
    \ ],\n      \"complete_main_pH\": [\n        8.5,\n        9\n      ]\n    },\n\
    \    \"rationale\": \"Retain each owner and the898-labelled target pH according\
    \ to its source. The merge problem is cross-source salt and identity selection,\
    \ not proof that each stored pH is false. Source-specific relationship notes must\
    \ acknowledge this difference.\",\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense under 100% N2\
    \ gas\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation ending\",\n        \"\
    exact_source_quote\": \"100% N2 gas. Vitamins should be sterilized by filtration.\
    \ Adjust pH of complete medium to\\n8.5 - 9.0.\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\": \"SL-10\
    \ final make-up\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"SL-10\",\n      \"final_makeup_ml\": 1000\n    },\n    \"rationale\": \"The\
    \ instruction is retained locally but at main root; relocate it with the stock\
    \ rather than treating 1000 mL as the complete medium volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"SL-10 preparation ending\",\n        \"exact_source_quote\"\
    : \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"SL-10 preparation ending\",\n        \"exact_source_quote\"\
    : \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\": \"Unquantified\
    \ autoclave cycle\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 8.0 - 8.5, then dispense\
    \ under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile anoxic\
    \ stock solutions prepared under 100% N2 gas. Vitamins should be sterilized by\
    \ filtration. Adjust pH of complete medium to 8.5 - 9.0.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve all ingredients except carbonates, yeast extract, glucose, vitamins\
    \ and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it\
    \ anoxic. Add carbonate and hydrogencarbonate, adjust pH to 9.0 - 9.5, dispense\
    \ medium under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, glucose, vitamins and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Vitamins should be sterilized\
    \ by filtration. Adjust pH of complete medium to 9.5 - 9.7.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"method\": \"autoclave\",\n      \"temperature\": null,\n      \"\
    duration\": null\n    },\n    \"rationale\": \"Keep existing source ordering and\
    \ vitamin filtration. No numerical cycle is provided.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add\
    \ yeast\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      },\n      {\n\
    \        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add\
    \ yeast\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\": \"dsmz898\
    \ source-only DSM16504 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898\",\n      \"strain\": \"DSM16504\",\n      \"omit\": \"glucose\",\n\
    \      \"betaine_g_per_l\": 2.7,\n      \"Na2SO3_g_per_l\": 0.65,\n      \"late_stock_N2_percent\"\
    : 100\n    },\n    \"rationale\": \"These are separate source-supported branch\
    \ instructions, absent from the local quantitative branch representation. Add\
    \ only with exact parent/strain scope; omission is not a zero-valued ingredient,\
    \ and this is not a new growth assertion or taxonomy assignment.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"Page 1 named DSM16504 paragraph\",\n        \"exact_source_quote\"\
    : \"For DSM 16504: Omit glucose and add to the autoclaved medium 2.70 g/l betaine\
    \ and 0.65\\ng/l Na2SO3 from filter-sterilized anoxic stock solutions prepared\
    \ under 100% N2 gas.\",\n        \"snapshot_sha256\": \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\"\
    ,\n        \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\": \"dsmz898\
    \ source-only DSM18346 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898\",\n      \"strain\": \"DSM18346\",\n      \"omit\": \"glucose\",\n\
    \      \"yeast_g_per_l\": 2,\n      \"final_pH\": 8.5\n    },\n    \"rationale\"\
    : \"These are separate source-supported branch instructions, absent from the local\
    \ quantitative branch representation. Add only with exact parent/strain scope;\
    \ omission is not a zero-valued ingredient, and this is not a new growth assertion\
    \ or taxonomy assignment.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz898\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\"\
    ,\n        \"source_locator\": \"Page 1 named DSM18346 paragraph\",\n        \"\
    exact_source_quote\": \"For DSM 18346: Omit glucose, increase amount of yeast\
    \ extract to 2.00 g/l. Adjust pH of\\ncomplete medium to 8.5.\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\": \"dsmz898\
    \ source-only DSM18978 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anoxybacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898\",\n      \"strain\": \"DSM18978\",\n      \"final_pH\": 9\n    },\n\
    \    \"rationale\": \"These are separate source-supported branch instructions,\
    \ absent from the local quantitative branch representation. Add only with exact\
    \ parent/strain scope; omission is not a zero-valued ingredient, and this is not\
    \ a new growth assertion or taxonomy assignment.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz898\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898.pdf\",\n        \"\
    source_locator\": \"Page 1 named DSM18978 paragraph\",\n        \"exact_source_quote\"\
    : \"For DSM 18978: Adjust pH of complete medium to 9.0.\",\n        \"snapshot_sha256\"\
    : \"76799c65b7bb08674ba55842fa00a06cae6d8c393e8327fbdabfb5fc670e70a7\",\n    \
    \    \"parsed_text_sha256\": \"21e808aaff061f24183c66fc80ad0a8ad6baa1d16fe329ef75c1d380fe33ec82\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:58.627284Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\": \"dsmz898a\
    \ source-only DSM18345 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898a\",\n      \"strain\": \"DSM18345\",\n      \"replace\": \"glucose\"\
    ,\n      \"D_mannitol_g_per_l\": 2.5,\n      \"final_pH\": [\n        9.5,\n \
    \       9.7\n      ]\n    },\n    \"rationale\": \"These are separate source-supported\
    \ branch instructions, absent from the local quantitative branch representation.\
    \ Add only with exact parent/strain scope; omission is not a zero-valued ingredient,\
    \ and this is not a new growth assertion or taxonomy assignment.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 named DSM18345 paragraph\",\n        \"exact_source_quote\"\
    : \"For DSM 18345: Replace glucose with 2.50 g/l D-mannitol as substrate and adjust\
    \ pH of\\ncomplete medium to 9.5 - 9.7.\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q46\",\n    \"component_or_context\": \"dsmz898a\
    \ source-only DSM18979 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898a\",\n      \"strain\": \"DSM18979\",\n      \"omit\": \"D-glucose\"\
    ,\n      \"yeast_g_per_l\": 2\n    },\n    \"rationale\": \"These are separate\
    \ source-supported branch instructions, absent from the local quantitative branch\
    \ representation. Add only with exact parent/strain scope; omission is not a zero-valued\
    \ ingredient, and this is not a new growth assertion or taxonomy assignment.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz898a\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\"\
    ,\n        \"source_locator\": \"Page 1 named DSM18979 paragraph\",\n        \"\
    exact_source_quote\": \"For DSM 18979: Omit D-glucose and increase amount of yeast\
    \ extract to 2.00 g/l.\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q47\",\n    \"component_or_context\": \"dsmz898a\
    \ source-only DSM100017 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898a\",\n      \"strain\": \"DSM100017\",\n      \"omit\": \"D-glucose\"\
    ,\n      \"yeast_g_per_l\": 2,\n      \"thiosulfate_pentahydrate_g_per_l\": 2.5,\n\
    \      \"crotonate_stock_dose_ml_per_l\": 10,\n      \"crotonate_stock_M\": 1\n\
    \    },\n    \"rationale\": \"These are separate source-supported branch instructions,\
    \ absent from the local quantitative branch representation. Add only with exact\
    \ parent/strain scope; omission is not a zero-valued ingredient, and this is not\
    \ a new growth assertion or taxonomy assignment.\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 named DSM100017 paragraph\",\n        \"exact_source_quote\"\
    : \"For DSM 100017: Omit D-glucose, increase amount of yeast extract to 2.00 g/l\
    \ and add\\n2.50 g/l Na2S2O3 x 5 H2O from an anoxic sterile stock solution after\
    \ autoclaving. Prior to\\ninoculation add 10.00 ml/l of a sterile anoxic 1 M Na-crotonate\
    \ solution (see medium 870).\",\n        \"snapshot_sha256\": \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\"\
    ,\n        \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q48\",\n    \"component_or_context\": \"dsmz898a\
    \ source-only DSM100337 branch\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": [\n    \
    \      {\n            \"path\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n            \"relationship\": \"SALINITY_VARIANT\",\n            \"id\": \"\
    CultureMech:002062\",\n            \"name\": \"anaerobacillus_medium\",\n    \
    \        \"notes\": \"NaCl increased from 4.99002 g/L to 14.9701 g/L while the\
    \ DSMZ 898/898a base formulation remains unchanged.\"\n          }\n        ],\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"scope\": \"named collection branch only\",\n      \"source_accession\"\
    : \"dsmz898a\",\n      \"strain\": \"DSM100337\",\n      \"replace\": \"D-glucose\"\
    ,\n      \"maltose_g_per_l\": 5,\n      \"yeast_g_per_l\": 1,\n      \"thiosulfate_pentahydrate_g_per_l\"\
    : 2.5\n    },\n    \"rationale\": \"These are separate source-supported branch\
    \ instructions, absent from the local quantitative branch representation. Add\
    \ only with exact parent/strain scope; omission is not a zero-valued ingredient,\
    \ and this is not a new growth assertion or taxonomy assignment.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz898a\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium898a.pdf\",\n       \
    \ \"source_locator\": \"Page 1 named DSM100337 paragraph\",\n        \"exact_source_quote\"\
    : \"For DSM 100337: Replace D-glucose with 5.00 g/l maltose, increase amount of\
    \ yeast\\nextract to 1.00 g/l and add 2.50 g/l Na2S2O3 x 5 H2O from an anoxic\
    \ sterile stock solution\\nafter autoclaving.\",\n        \"snapshot_sha256\"\
    : \"5eadd7fde6a1a3d1286f0cf9370e6b9ccf78231374ba42ddd71b0f3f615f6e36\",\n    \
    \    \"parsed_text_sha256\": \"2a180b5cfc6ebb5b33b3b6592e78063f4c971b340bae5e6f1fe601c6ba610a46\"\
    ,\n        \"accessed_at\": \"2026-10-21T15:56:59.109033Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q49\",\n    \"component_or_context\": \"Crotonic\
    \ acid for DSM100017 only\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"crotonate stock for898a DSM100017\",\n      \"mass_g\"\
    : 86,\n      \"product_string\": \"ALDRICH 113018\",\n      \"supplier_composition_not_independently_verified\"\
    : true\n    },\n    \"rationale\": \"This stock is relevant only through the explicit898a\
    \ branch reference; it is not a basal898/898a ingredient or an invitation to transfer\
    \ other DSM870 content.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz870\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Na-crotonate (1 M) table only\",\n   \
    \     \"exact_source_quote\": \"Crotonic acid (ALDRICH 113018) 86.00 g\",\n  \
    \      \"snapshot_sha256\": \"f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20\"\
    ,\n        \"parsed_text_sha256\": \"ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:16:27.838686Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q50\",\n    \"component_or_context\": \"Crotonate\
    \ base for DSM100017 only\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"crotonate stock for898a DSM100017\",\n      \"normality\"\
    : 10,\n      \"table_volume_ml\": 100,\n      \"procedure_qualifier\": \"around\"\
    \n    },\n    \"rationale\": \"This stock is relevant only through the explicit898a\
    \ branch reference; it is not a basal898/898a ingredient or an invitation to transfer\
    \ other DSM870 content.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz870\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Na-crotonate (1 M) table only\",\n   \
    \     \"exact_source_quote\": \"NaOH (10 N) 100.00 ml\",\n        \"snapshot_sha256\"\
    : \"f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20\",\n    \
    \    \"parsed_text_sha256\": \"ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:16:27.838686Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q51\",\n    \"component_or_context\": \"Crotonate\
    \ table water for DSM100017 only\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"crotonate stock for898a DSM100017\",\n      \"table_water_ml\"\
    : 900\n    },\n    \"rationale\": \"This stock is relevant only through the explicit898a\
    \ branch reference; it is not a basal898/898a ingredient or an invitation to transfer\
    \ other DSM870 content.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz870\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Na-crotonate (1 M) table only\",\n   \
    \     \"exact_source_quote\": \"Distilled water 900.00 ml\",\n        \"snapshot_sha256\"\
    : \"f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20\",\n    \
    \    \"parsed_text_sha256\": \"ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:16:27.838686Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q52\",\n    \"component_or_context\": \"Crotonate\
    \ stock preparation quantities\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacillus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"crotonate stock for898a DSM100017\",\n      \"initial_water_ml\"\
    : 800,\n      \"base_around_ml\": 100,\n      \"base_normality\": 10,\n      \"\
    approximate_pH\": 7,\n      \"final_makeup_ml\": 1000,\n      \"N2_percent\":\
    \ 100,\n      \"sterilization\": \"filtration\"\n    },\n    \"rationale\": \"\
    Preserve the difference between table water and staged initial/make-up water.\
    \ Approximate titrant volume and pH remain approximate; no density conversion\
    \ is introduced.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz870\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium870.pdf\"\
    ,\n        \"source_locator\": \"Page 2 Na-crotonate (1 M) preparation only\"\
    ,\n        \"exact_source_quote\": \"Dissolve crotonic acid in 800 ml distilled\
    \ water, add around 100 ml of 10 N NaOH and\\nadjust pH to around 7. Then add\
    \ water to reach a volume of 1000 ml. Sterilize by filtration\\nunder 100% N2\
    \ gas atmosphere.\",\n        \"snapshot_sha256\": \"f58f4adb6bfbfb14701cbfb92b16faa0f933cb6122d1fdafc2fcf37f6acc8f20\"\
    ,\n        \"parsed_text_sha256\": \"ff950dac89f30ae011011b2ce040ae1484315b52f0c7d5d95e3c77b546b25c49\"\
    ,\n        \"accessed_at\": \"2026-10-21T13:16:27.838686Z\"\n      }\n    ]\n\
    \  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '29 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 29/30
    primary and 27/30 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17634
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32139
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi76209
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 30: primary 96.67%;
    secondary 90.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 26 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Two exact accessions and mismatched merged formula
  outcome: concern
  summary: Both stable owners and relationship paths resolve. DSM898 and898a share
    many ingredient identities but differ in salt, initial/final pH and named source
    branches. The target reports898 while carrying the898a salt amount. SALINITY_VARIANT
    notes in target/owners saying only salt differs contradict the captured primary
    pH instructions and the owners themselves.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz898
  - dsmz898a
  - id-search
- assessment_id: evidence
  area: evidence
  topic: Source quantities and historical rate basis
  outcome: concern
  summary: No ingredient amount evidence is attached in any layer. Current exact primary
    batch and stock quantities are available; all four current main API attempts failed503.
    These failures do not make the current primary branch comparison unavailable,
    but they leave the historical1.002 L normalization unauthenticated. Source branch
    g/L and mL/L quantities are explicit and distinct from this unresolved base denominator.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - dsmz898
  - dsmz898a
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Salt/hydrate and stereochemical distinctions
  outcome: concern
  summary: Source sodium resazurin is mapped to neutral CHEBI:8806, and nickel chloride
    hexahydrate to CHEBI:34887 Cl2Ni in primary and secondary slots. Other asserted
    form metadata were inspected. Calcium D-(+)-pantothenate is explicitly D in both
    source tables; no DL-versus-D conflict is claimed. Generic CHEBI:16494 lipoic
    acid does not assert an unsupported specific enantiomer for the DL source. Unmapped
    yeast is a mixture linkage gap, not an invented identity.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - dsmz898
  - dsmz898a
  - chebi8806
  - chebi34887
  - chebi31345
  - chebi16494
- assessment_id: preparation
  area: completeness
  topic: Main, stock and branch procedures
  outcome: concern
  summary: Each maintained owner retains its own source-specific main pH/gas sequence.
    Main root also holds SL-10 make-up; all stock containers and dose/solvent inputs
    are absent. Seven named primary branches and the narrowly referenced crotonate
    stock are not quantitatively represented. Preserve stage and strain scope, approximate
    endpoints, filtration and sequencing; no sterilization cycle or unprinted late-stock
    volume can be supplied.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz898
  - dsmz898a
  - crotonate
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Complex liquid recipe and biological scope
  outcome: supported
  summary: COMPLEX/SEMI_DEFINED and LIQUID are compatible with the yeast-extract recipe
    plus identified salts/stocks. The record has no target organism CURIE or graph-match
    assertion. Collection strain paragraphs are formulation branches, not newly verified
    growth, optimum or taxonomic assertions.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - dsmz898
  - dsmz898a
- assessment_id: current-writers
  area: provenance
  topic: Current writers and maintained input follow-up
  outcome: concern
  summary: Current importer preserves later stock additions but collects preparation
    across sections. Current fingerprints compare ingredient identity, not quantity
    or pH; relationship writers can annotate topology without correcting formula content.
    Preserve the two source owners and their distinct pH/salt branches; correct source-specific
    stock topology and relationship prose before a separately authorized merge. Current
    implementation is not proof of historical causation.
  target_ids:
  - CultureMech:002061
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
  - current-code-3
  - current-code-4
findings:
- finding_id: f1
  issue_key: culturemech.002061.mixed-source-variant
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Merged target combines two distinct source recipes
  description: The target retains DSM898 identity and its pH/procedure but inherits898a
    NaCl14.9701 g/L. The two exact primaries specify different salt inputs, pH stages
    and strain branches; their ingredient-set fingerprint does not justify one hybrid
    formula.
  target_ids:
  - CultureMech:002061
  field_paths:
  - media_term
  - ingredients[4].concentration
  - ph_range
  - preparation_steps
  - merged_from
  evidence_ids:
  - dsmz898
  - dsmz898a
  - owner-0
  - owner-1
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
  issue_key: culturemech.002061.stock-and-basis-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: SL-10 and vitamins are flattened into direct medium concentrations
  description: All layers retain19 stock constituents as direct ingredients, omit
    stock doses/waters, and give unverified main normalization. HCl10 mL at an unqualified25%
    became2.5 g/L; no source percentage basis supports that conversion.
  target_ids:
  - CultureMech:002061
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsmz898
  - dsmz898a
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
  issue_key: culturemech.002061.salt-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin and nickel hydrate have incompatible groundings
  description: The sodium-salt dye maps to neutral resazurin and nickel hexahydrate
    maps to nickel dichloride without waters. Matching canonical labels and current
    secondary keys do not establish correct supplied form.
  target_ids:
  - CultureMech:002061
  field_paths:
  - ingredients[5].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz898
  - chebi8806
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
  issue_key: culturemech.002061.variant-and-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Variant prose understates differences and stock preparation is detached
  description: The target child note and owner relationship/modification notes say
    the base is unchanged or differs only in NaCl, despite different source pH sequences.
    Seven primary strain branches are absent; SL-10 make-up remains at main root.
  target_ids:
  - CultureMech:002061
  field_paths:
  - variant_children
  - preparation_steps
  - solutions
  evidence_ids:
  - dsmz898
  - dsmz898a
  - crotonate
  - quantity-inventory
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Preserve source-specific898 and898a owners and prevent cross-source
    amount/pH selection during regeneration. Review the merge boundary using the actual
    formulation distinctions rather than fingerprint equality; do not change one owner
    to the other source.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
  description: Restore both complete stocks with their exact source quantities, forms,
    solvent/make-up and receiving doses. Restore explicit main batch inputs without
    inventing final volume, density or percentage basis; attach narrow evidence in
    each owner.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
  description: Verify exact source-compatible primary IDs and reassess secondary mappings
    independently. Preserve source masses and other explicitly supported stereochemical
    scope; do not infer replacement identifiers.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
  description: Correct active relationship prose in both owners to acknowledge pH
    and source-branch distinctions. Preserve the seven explicit branches without widening
    growth claims; recover only the referenced crotonate stock for DSM100017, and
    relocate SL-10 preparation with its stock. Append history instead of rewriting
    old events.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002061
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacillus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anoxybacillus_medium.yaml
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
- 'Required historical authentication of the existing base-rate normalization remains
  unavailable: both primary recipes provide source inputs without a main final-volume
  statement, and all four exact API attempts failed503. The local approximate1.002
  L basis is not established by the listed1002.5 mL liquid sum or unspecified late-stock
  volumes. Current source branch identity and explicit branch concentrations are available
  and assessed; partial completion is restricted to the unresolved base-rate provenance/volume
  basis.'
- Exact mediadive898api returned503; preserved error body is not recipe evidence and
  does not establish chronology or absence.
- Exact mediadive898api_retry returned503; preserved error body is not recipe evidence
  and does not establish chronology or absence.
- Exact mediadive898aapi returned503; preserved error body is not recipe evidence
  and does not establish chronology or absence.
- Exact mediadive898aapi_retry returned503; preserved error body is not recipe evidence
  and does not establish chronology or absence.
- 'The parent320 and120 recipes are not imported: both child primaries already reproduce
  complete SL-10 and vitamin tables. Only the explicit DSM870 crotonate subsection
  transfers. Captured source dates do not establish whether historical provider or
  current primary changed first.'
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-029
- generated-medium
```
