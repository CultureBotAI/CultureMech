# Source and formulation review: anaerobacterium_medium (CultureMech:001015)

- Review: 20261021T150905Z-culturemech-001015-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:47:53Z
- Finished UTC: 2026-10-21T15:09:05Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1538 identity is supported, but both local layers flatten three stock recipes into direct medium concentrations and place SL-10 preparation at the main root. Nickel hexahydrate is grounded to anhydrous nickel chloride. Primary main volume is unspecified; provider 1000 mL is retained only as provider scope, with source-specific biotin units and HCl strength preserved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 260; batch 026 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-five task batches contain 250 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 253 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001015 | data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml | generated | anaerobacterium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001015 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001015 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/260/strict.tsv |
| validate-terms | passed | True | CultureMech:001015 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001015 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001015 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Primary and provider main-volume comparison | passed | True | CultureMech:001015 | Completed full-document comparison: the primary does not specify main water/final volume, while the provider declares 1000 mL and lists 1000 mL water. This source limitation is recorded explicitly, not converted into an unavailable retrieval or fabricated primary claim. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001015.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001015.

36 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Main: KH2PO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 0.2,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 0.2,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 1",
        "exact_source_quote": "KH2PO4 0.2 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.46967,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Main: NH4Cl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 0.25,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 0.25,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 2",
        "exact_source_quote": "NH4Cl 0.25 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 4.67377,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Main: NaCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 1,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 1,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 3",
        "exact_source_quote": "NaCl 1 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Main: MgCl2 x 6 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 0.4,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 0.4,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 4",
        "exact_source_quote": "MgCl2 x 6 H2O 0.4 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 1.96751,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Main: KCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 0.5,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 0.5,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 5",
        "exact_source_quote": "KCl 0.5 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 6.70691,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Main: CaCl2 x 2 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 0.15,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 0.15,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 6",
        "exact_source_quote": "CaCl2 x 2 H2O 0.15 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 1.0203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Main: Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 1,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 1,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 7",
        "exact_source_quote": "Yeast extract 1.0 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Main: Cellobiose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 10,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 10,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 8",
        "exact_source_quote": "Cellobiose 10.0 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\": 214,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 29.2141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Main: NaHCO3",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.52",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "2.52",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 2.52,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 2.52,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 9",
        "exact_source_quote": "NaHCO3 2.52 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2.52,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.52,\n                        \"mmol_l\": 29.9975,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Main: Na2S x 9 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.36",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "primary_amount": 0.36,
      "primary_unit": "g",
      "primary_main_final_volume_ml": null,
      "provider_g_per_l": 0.36,
      "provider_declared_volume_ml": 1000
    },
    "rationale": "The unchanged number matches provider g_l but has no attached local evidence. Primary supplies a batch mass without a main denominator. Attach exact primary mass and separately attributed provider basis; do not represent an independently primary-verified 1 L final medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 main table, row 10",
        "exact_source_quote": "Na2S x 9 H2O 0.36 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.36,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.36,\n                        \"mmol_l\": 1.49886,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "SL-10: HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 10,
      "unit": "ml",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "primary_strength": "25%; 7.7 M",
      "percent_basis": null,
      "calculated_stock_molarity_M": 0.077,
      "provider_g_per_l_not_established": 2.5
    },
    "rationale": "Preserve both primary strength labels: 25% has no stated mass/volume basis, while 10 mL of 7.7 M made up to 1000 mL gives 0.077 M within SL-10. This calculation does not establish the provider 2.5 g/L mass value or any main-medium concentration. No density or percentage basis is invented.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 1",
        "exact_source_quote": "HCl (25%; 7.7 M) 10.00 ml",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "SL-10: FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 1.5,
      "unit": "g",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 1.5
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 2",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "SL-10: ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 70,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.07
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 3",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "SL-10: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 100,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.1
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 4",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "SL-10: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 6,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.006
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 5",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "SL-10: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 190,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.19
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 6",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "SL-10: CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 2,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.002
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 7",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "SL-10: NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 24,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.024
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator. Source hexahydrate is distinct from the asserted anhydrous nickel chloride.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 8",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "SL-10: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock 595",
      "amount": 36,
      "unit": "mg",
      "stock_final_make_up_ml": 1000,
      "main_receiving_dose_ml": 1,
      "provider_stock_g_per_l": 0.036
    },
    "rationale": "The current concentration is the stock strength misplaced in the main recipe. Restore SL-10 stage, original mass units and its separate receiving dose; do not use stock make-up as the main denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 table, row 9",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Vitamin stock: Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock 3189",
      "source_value": 20,
      "source_unit": "mg/l",
      "provider_stock_g_per_l": 0.02,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the vitamin stock stage; these are not direct main concentrations. Biotin explicitly uses mg/l, whereas the other three entries are mg batch amounts with 1000 mL listed water. Preserve this unit distinction and generic B12 identity; do not silently rewrite biotin as an unqualified 20 mg dose.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 vitamin table, row 1",
        "exact_source_quote": "Biotin 20.0 mg/l",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg/l\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Vitamin stock: p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock 3189",
      "source_value": 80,
      "source_unit": "mg",
      "provider_stock_g_per_l": 0.08,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the vitamin stock stage; these are not direct main concentrations. Biotin explicitly uses mg/l, whereas the other three entries are mg batch amounts with 1000 mL listed water. Preserve this unit distinction and generic B12 identity; do not silently rewrite biotin as an unqualified 20 mg dose.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 vitamin table, row 2",
        "exact_source_quote": "p-Aminobenzoic acid 80.0 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Vitamin stock: Thiamine-HCl x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock 3189",
      "source_value": 200,
      "source_unit": "mg",
      "provider_stock_g_per_l": 0.2,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the vitamin stock stage; these are not direct main concentrations. Biotin explicitly uses mg/l, whereas the other three entries are mg batch amounts with 1000 mL listed water. Preserve this unit distinction and generic B12 identity; do not silently rewrite biotin as an unqualified 20 mg dose.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 vitamin table, row 3",
        "exact_source_quote": "Thiamine-HCl x 2 H2O 200.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Vitamin stock: Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "vitamin stock 3189",
      "source_value": 50,
      "source_unit": "mg",
      "provider_stock_g_per_l": 0.05,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the vitamin stock stage; these are not direct main concentrations. Biotin explicitly uses mg/l, whereas the other three entries are mg batch amounts with 1000 mL listed water. Preserve this unit distinction and generic B12 identity; do not silently rewrite biotin as an unqualified 20 mg dose.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 vitamin table, row 4",
        "exact_source_quote": "Vitamin B12 50.00 mg",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      },
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.0368895,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Selenite-tungstate stock: NaOH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "selenite-tungstate stock 777",
      "amount": 0.5,
      "unit": "g",
      "provider_stock_g_per_l": 0.5,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the separate stock recipe and 1 mL receiving addition. The current stock-strength g/L values are not direct final-medium concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaOH\",\n                        \"compound_id\": 256,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 12.5009,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Selenite-tungstate stock: Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "selenite-tungstate stock 777",
      "amount": 3,
      "unit": "mg",
      "provider_stock_g_per_l": 0.003,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the separate stock recipe and 1 mL receiving addition. The current stock-strength g/L values are not direct final-medium concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[3].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Selenite-tungstate stock: Na2WO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "selenite-tungstate stock 777",
      "amount": 4,
      "unit": "mg",
      "provider_stock_g_per_l": 0.004,
      "listed_stock_water_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "Restore the separate stock recipe and 1 mL receiving addition. The current stock-strength g/L values are not direct final-medium concentrations.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[3].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.004,\n                        \"mmol_l\": 0.0121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Receiving dose: Trace element solution SL-10",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "solution_id": 595,
      "amount": 1,
      "unit": "ml",
      "stage": "main recipe with unspecified primary final volume"
    },
    "rationale": "The primary and provider agree on the 1 mL addition. Both local layers omit the stock reference and dose; do not convert it into an absolute final concentration without a stated denominator.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Receiving dose: Vitamin solution",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "solution_id": 3189,
      "amount": 1,
      "unit": "ml",
      "stage": "main recipe with unspecified primary final volume"
    },
    "rationale": "The primary and provider agree on the 1 mL addition. Both local layers omit the stock reference and dose; do not convert it into an absolute final concentration without a stated denominator.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Vitamin solution\",\n                        \"solution_id\": 3189,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Receiving dose: Selenite-tungstate solution",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "solution_id": 777,
      "amount": 1,
      "unit": "ml",
      "stage": "main recipe with unspecified primary final volume"
    },
    "rationale": "The primary and provider agree on the 1 mL addition. Both local layers omit the stock reference and dose; do not convert it into an absolute final concentration without a stated denominator.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Selenite-tungstate solution\",\n                        \"solution_id\": 777,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "SL-10 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "Trace element solution SL-10",
      "amount": 990,
      "unit": "ml"
    },
    "rationale": "Retain the stock-specific water quantity. SL-10 lists 990 mL water and separately makes up to 1000 mL; other stock water does not establish the main volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Vitamin stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "Vitamin solution",
      "amount": 1000,
      "unit": "ml"
    },
    "rationale": "Retain the stock-specific water quantity. SL-10 lists 990 mL water and separately makes up to 1000 mL; other stock water does not establish the main volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[2].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Selenite-tungstate stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "Selenite-tungstate solution",
      "amount": 1000,
      "unit": "ml"
    },
    "rationale": "Retain the stock-specific water quantity. SL-10 lists 990 mL water and separately makes up to 1000 mL; other stock water does not establish the main volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[3].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Provider-only main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "provider_main_water_ml": 1000,
      "primary_main_water_ml": null,
      "source_scope": "provider only"
    },
    "rationale": "The primary main table contains no water row; only the exact provider supplies 1000 mL. If represented, qualify this provider-only evidence explicitly. It is neither a primary-certified final volume nor 1000 g/L water.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Main-volume evidence boundary",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "notes",
        "stored": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "notes",
        "stored": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "primary_main_volume_ml": null,
      "provider_main_volume_ml": 1000,
      "provider_listed_water_plus_stocks_ml": 1003,
      "measured_final_volume_ml": null
    },
    "rationale": "Primary main volume is unspecified; its later 1000 mL instruction is only SL-10 make-up. The provider denominator is explicit but its 1000 mL water plus three 1 mL doses sums to 1003 mL, not a measured final volume. Complete source comparison can document this limit without inventing a failed access or historical mapping check.",
    "source_snippets": [
      {
        "source_key": "mediadive1538api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1538",
        "source_locator": "$.data.solutions[0].volume (solution 3187)",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475"
      },
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Last main-table row before stock subsections",
        "exact_source_quote": "Selenite-tungstate solution 1 ml",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "SL-10 final make-up",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "final_make_up_ml": 1000
    },
    "rationale": "The current main-root preparation reproduces this quantity but loses its stock scope. Restore it under SL-10, preserving dissolution order. Do not use it as a main-medium volume instruction.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 SL-10 preparation",
        "exact_source_quote": "Finally make up to 1000.0 ml.",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Main pH, gas and sterilization quantities unspecified",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "main_pH": null,
      "main_gas_composition": null,
      "main_sterilization_temperature": null,
      "main_sterilization_duration": null
    },
    "rationale": "The whole primary and provider main stage were inspected: neither gives numerical main pH, gas composition or a sterilization cycle. The only local preparation is actually SL-10. Preserve this absence without importing another medium or presumed default.",
    "source_snippets": [
      {
        "source_key": "dsmz1538",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf",
        "source_locator": "Page 1 section heading before the sole preparation paragraph",
        "exact_source_quote": "Trace element solution SL-10:",
        "snapshot_sha256": "7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b",
        "parsed_text_sha256": "a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:001015.

25 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 25/26 primary and 25/26 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 26: primary 96.15%; secondary 96.15%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact source identity and maintained ownership

identity: supported. Targets: CultureMech:001015.

CultureMech:001015 and DSMZ/MediaDive 1538 agree. The sole maintained owner and generated target have identical scientific fields; target-only differences are merge bookkeeping. All three exact stock endpoint identities agree with the named primary subsections and provider references. No legacy mediaingredientmech_term is asserted.

### Claim-level support and exact source stages

evidence: concern. Targets: CultureMech:001015.

No ingredient amount has attached supporting evidence in either local layer. Every local concentration and scoped source-only quantitative context has an inventory decision with exact quotations and locators. Matching provider transcription receives evidence_only, not verified. Source quantities and provider normalization remain separate.

### Main and stock preparation boundaries

completeness: concern. Targets: CultureMech:001015.

The only local preparation paragraph dissolves iron in HCl and makes up to 1000 mL, which belongs exclusively to SL-10. Named stock stages, receiving doses and water are missing. The primary does not specify main pH, gas, sterilization cycle or final volume; the provider supplies main water/volume independently. Preserve these limits rather than interpreting stock preparation as a complete main protocol.

### Composition and physical state

scope: supported. Targets: CultureMech:001015.

COMPLEX/UNDEFINED is supported by yeast extract alongside specified solutes. LIQUID is consistent with no listed solidifier. No growth phenotype or strain-specific outcome follows from the medium name.

### Source-specified molecular forms and mixtures

grounding: concern. Targets: CultureMech:001015.

Nickel chloride hexahydrate is mismatched to CHEBI:34887 formula Cl2Ni/mass 129.599 in both primary and current secondary slots. The remaining inspected hydrated salts, thiamine hydrochloride dihydrate and generic B12 are source-compatible. Generic cellobiose does not imply a uniquely supplied reducing-end anomer; no narrower identity is invented. Yeast extract remains an unresolved mixture, not a falsely exact molecular compound.

### Growth, taxonomy and graph assertion scope

scope: not_applicable. Targets: CultureMech:001015.

The medium title, bacterial filing and generic Microbial cultivation application are catalog context, not strain-level experimental growth evidence. No organism identifier, growth assertion, phenotype or graph membership is added. No internal variant/reference relationship is asserted in either complete local record.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001015.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Maintained input and current import/merge behavior

provenance: concern. Targets: CultureMech:001015.

Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes.

## Findings

### f1: Three stock recipes are flattened into the main formula

blocker / open / confirmed; issue key: culturemech.001015.stock-stage-collapse.

ingredients[10:26] store SL-10, vitamin and selenite/tungstate stock strengths directly in the medium. All three 1 mL receiving references and scoped water amounts are absent. HCl 2.5 g/L does not follow from an unqualified 25% label, while the primary also supplies 7.7 M; biotin 20 mg/l belongs to the vitamin stock. The primary has no main final-volume statement, whereas direct main g/L values match a provider-only 1000 mL basis. The flat representation conflates stocks, main quantities and denominators.

### f2: Nickel hexahydrate is identified as the anhydrous compound

major / open / confirmed; issue key: culturemech.001015.nickel-hydrate-grounding.

ingredients[17] names NiCl2 x 6 H2O, consistent with the primary SL-10 table, but both primary and current secondary CHEBI:34887 slots specify Cl2Ni without hydration. Identifier validity and label correspondence do not establish the supplied source form.

### f3: The sole preparation step belongs to SL-10, not the medium

major / open / confirmed; issue key: culturemech.001015.stock-preparation-scope.

preparation_steps[0] contains the SL-10 iron/HCl dissolution and 1000 mL make-up procedure but is stored at the main root. Neither the primary nor provider supplies a main preparation procedure that this stock paragraph could replace. Main pH, atmosphere, sterilization cycle and measured final volume remain unspecified.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the maintained owner with the ten main batch masses and separately attributed provider denominator, three named stock recipes, all receiving doses and stage-specific water. Preserve biotin mg/l literally and both HCl strength labels with unknown percentage basis. Do not infer measured final volume, density or main protocol from SL-10. Attach claim-level evidence before authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the source hexahydrate name and separately verify source-compatible primary and secondary grounding before replacement. Do not use anhydrous molecular mass to interpret the source 24 mg stock dose.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Move the intact existing procedure into restored SL-10 stock preparation. Record the main preparation gaps explicitly and seek exact target-specific evidence if later needed; do not fill them from stock instructions or neighboring media.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/anaerobacterium_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch026/260/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/260/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml:1:id: CultureMech:001015<br>./data/normalized_yaml/bacterial/anaerobacterium_medium.yaml:1:id: CultureMech:001015<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/260/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 30 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/260/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf; Whole single-page main table, SL-10, vitamin and selenite-tungstate subsections | supports | Primary lists ten main batch masses and three 1 mL receiving stocks but no main water/final-volume statement. Its only preparation paragraph belongs to SL-10. Biotin is explicitly 20.0 mg/l; SL-10 HCl explicitly carries both 25% and 7.7 M. |
| provider | https://mediadive.dsmz.de/rest/medium/1538; $.data.medium; all four solutions, recipes and SL-10 steps | supports | Exact medium 1538, main solution 3187, SL-10 595, vitamin 3189 and selenite-tungstate 777. Provider declares 1000 mL main volume and adds a 1000 mL main-water row absent from the PDF; that does not establish a primary or measured final-volume claim. |
| solution595 | https://mediadive.dsmz.de/rest/solution/595; Exact stock endpoint recipe and source stage | supports | Exact SL-10 endpoint confirms its separate recipe and make-up; its HCl attribute omits the primary 7.7 M wording. |
| solution3189 | https://mediadive.dsmz.de/rest/solution/3189; Exact stock endpoint recipe and source stage | supports | Exact vitamin endpoint retains 20 mg/l biotin, distinct from other mg batch amounts. |
| solution777 | https://mediadive.dsmz.de/rest/solution/777; Exact stock endpoint recipe and source stage | supports | Exact selenite-tungstate endpoint; its stock strengths are not direct medium values. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch026/260/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:132751 resolves to thiamine hydrochloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term": "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17057": [{"label": "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term": "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerobacterium_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive API parsing reads direct ingredients from the first solution, excludes water and stock additions, preserves provider g_l, and separately records receiving stock references; its preparation reader still gathers steps from all solutions at the main root. Bare-unit fallback is not final-volume proof. Current cleanup retains the first disagreeing duplicate with a warning instead of summing it. Current lossless formulation merging preserves scientific assertions and order, not their correctness. These current implementations do not establish which historical version produced this record. Correct the exact maintained owner, append curation provenance, and regenerate only after separately authorized changes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Only the exact bound collection/provider sources and pinned identifiers were assessed. Current source differences do not establish source chronology or the exact historical import version.
- Listed water, stock recipe volumes and receiving additions do not establish a measured assembled final volume. No unqualified percent basis, density, unspecified stock strength, sterilization cycle or source-specific replacement identifier is invented.
- This completed review assesses the available source disagreement and omission; it does not certify that the main medium has a known measured final volume or complete preparation protocol. No legacy MIM key is asserted, so no unavailable legacy-correspondence check is manufactured.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150905Z-culturemech-001015-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobacterium_medium (CultureMech:001015)'
started_at: '2026-10-21T14:47:53Z'
finished_at: '2026-10-21T15:09:05Z'
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
summary: DSMZ 1538 identity is supported, but both local layers flatten three stock
  recipes into direct medium concentrations and place SL-10 preparation at the main
  root. Nickel hexahydrate is grounded to anhydrous nickel chloride. Primary main
  volume is unspecified; provider 1000 mL is retained only as provider scope, with
  source-specific biotin units and HCl strength preserved.
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
  - path: data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
    sha256: 9e7abd849dd9e35e49c0b1ce9ea27fc3b7ff9b01e3f6fc8c700ac92388cb5814
    role: target
  - path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
    sha256: b2e17e362e189be8cfa9ea424d24358c5f00c7738a78d636f4e2339f41bf1b39
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
  selection: Task review 260; batch 026 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-five task batches
    contain 250 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 253 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001015
targets:
- target_id: CultureMech:001015
  path: data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  label: anaerobacterium_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/260/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/260/strict.tsv"
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001015
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
  - CultureMech:001015
- check_id: primary-provider-volume-scope
  name: Primary and provider main-volume comparison
  required: true
  status: passed
  summary: 'Completed full-document comparison: the primary does not specify main
    water/final volume, while the provider declares 1000 mL and lists 1000 mL water.
    This source limitation is recorded explicitly, not converted into an unavailable
    retrieval or fabricated primary claim.'
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - primary
  - provider
  - quantity-inventory
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:24.723102Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/260/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:26.096274Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/260/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:27.757372Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:28.758273Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:57:04Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml:1:id: CultureMech:001015

    ./data/normalized_yaml/bacterial/anaerobacterium_medium.yaml:1:id: CultureMech:001015

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/260/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:57:04Z'
  support: supports
  summary: 30 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: b8ea4070e3ea39bb3d3a02d634d84d9fe535344b87fe1078046dd0d69caa15b6
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/260/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: 3139b5117ece45cbf53edd1d77653929a53a8ff916019816d86b0120ce5ca1df
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf
  locator: Whole single-page main table, SL-10, vitamin and selenite-tungstate subsections
  accessed_at: '2026-10-21T14:35:46.590278Z'
  support: supports
  summary: Primary lists ten main batch masses and three 1 mL receiving stocks but
    no main water/final-volume statement. Its only preparation paragraph belongs to
    SL-10. Biotin is explicitly 20.0 mg/l; SL-10 HCl explicitly carries both 25% and
    7.7 M.
  snapshot_sha256: 7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1538
  locator: $.data.medium; all four solutions, recipes and SL-10 steps
  accessed_at: '2026-10-21T14:35:45.933036Z'
  support: supports
  summary: Exact medium 1538, main solution 3187, SL-10 595, vitamin 3189 and selenite-tungstate
    777. Provider declares 1000 mL main volume and adds a 1000 mL main-water row absent
    from the PDF; that does not establish a primary or measured final-volume claim.
  snapshot_sha256: 7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475
- evidence_id: solution595
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: Exact stock endpoint recipe and source stage
  accessed_at: '2026-10-21T11:03:05.357684Z'
  support: supports
  summary: Exact SL-10 endpoint confirms its separate recipe and make-up; its HCl
    attribute omits the primary 7.7 M wording.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: solution3189
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3189
  locator: Exact stock endpoint recipe and source stage
  accessed_at: '2026-10-21T14:36:40.005850Z'
  support: supports
  summary: Exact vitamin endpoint retains 20 mg/l biotin, distinct from other mg batch
    amounts.
  snapshot_sha256: 05e290c81e28beae3d2e1bf4d2276db6b5325fd7474ca88263473421e8705957
- evidence_id: solution777
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/777
  locator: Exact stock endpoint recipe and source stage
  accessed_at: '2026-10-21T13:20:07.510517Z'
  support: supports
  summary: Exact selenite-tungstate endpoint; its stock strengths are not direct medium
    values.
  snapshot_sha256: 3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/260/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a0771747dfb97e26546c9c2efe70de9bb527ef2ecbb71236acef8a36ee999636
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
- evidence_id: chebi17057
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17057
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:39.796651Z'
  support: supports
  summary: CHEBI:17057 resolves to cellobiose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 3548f79d3274a33683125152944998cffa00bd4fce774c8d872db9003222ed06
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T14:57:04Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:132751": [{"label": "Thiamine-HCl x
    2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:132751", "preferred_term":
    "Thiamine-HCl x 2 H2O", "ontology_id": "CHEBI:132751", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17057": [{"label":
    "Cellobiose", "match_type": "preferred_term", "identifier": "CHEBI:17057", "preferred_term":
    "Cellobiose", "ontology_id": "CHEBI:17057", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term",
    "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id":
    "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883":
    [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883",
    "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label":
    "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139":
    [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139",
    "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
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
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label":
    "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249",
    "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml; data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/anaerobacterium_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:57:04Z'
  support: context_only
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 36 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Main: KH2PO4\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 0.2,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 0.2,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 1\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.2 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n                \
    \        \\\"mmol_l\\\": 1.46967,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Main: NH4Cl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 0.25,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 0.25,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 2\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.25 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 0.25,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.25,\\n         \
    \               \\\"mmol_l\\\": 4.67377,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Main: NaCl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 1,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 1,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\":\
    \ \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 3\",\n        \"exact_source_quote\"\
    : \"NaCl 1 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Main: MgCl2 x 6 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 0.4,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 0.4,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 4\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 0.4 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.4,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n \
    \                       \\\"mmol_l\\\": 1.96751,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Main: KCl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 0.5,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 0.5,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 5\",\n        \"exact_source_quote\"\
    : \"KCl 0.5 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 6.70691,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Main: CaCl2 x 2 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 0.15,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 0.15,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 6\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.15 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.15,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.15,\\n\
    \                        \\\"mmol_l\\\": 1.0203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Main: Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n       \
    \ \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 1,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 1,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\":\
    \ \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 7\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.0 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Main: Cellobiose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n      \
    \  \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 10,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 10,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 8\",\n        \"exact_source_quote\"\
    : \"Cellobiose 10.0 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Cellobiose\\\",\\n                        \\\"compound_id\\\"\
    : 214,\\n                        \\\"amount\\\": 10,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n    \
    \                    \\\"mmol_l\\\": 29.2141,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Main: NaHCO3\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.52\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"2.52\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 2.52,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 2.52,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 9\",\n        \"exact_source_quote\"\
    : \"NaHCO3 2.52 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"NaHCO3\\\",\\n                        \\\"compound_id\\\": 55,\\\
    n                        \\\"amount\\\": 2.52,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.52,\\n         \
    \               \\\"mmol_l\\\": 29.9975,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Main: Na2S x 9 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.36\",\n          \"unit\": \"G_PER_L\"\n        },\n    \
    \    \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"primary_amount\": 0.36,\n      \"primary_unit\"\
    : \"g\",\n      \"primary_main_final_volume_ml\": null,\n      \"provider_g_per_l\"\
    : 0.36,\n      \"provider_declared_volume_ml\": 1000\n    },\n    \"rationale\"\
    : \"The unchanged number matches provider g_l but has no attached local evidence.\
    \ Primary supplies a batch mass without a main denominator. Attach exact primary\
    \ mass and separately attributed provider basis; do not represent an independently\
    \ primary-verified 1 L final medium.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table, row 10\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.36 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 0.36,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.36,\\\
    n                        \\\"mmol_l\\\": 1.49886,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"SL-10: HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 10,\n      \"unit\"\
    : \"ml\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"primary_strength\": \"25%; 7.7 M\",\n      \"percent_basis\": null,\n\
    \      \"calculated_stock_molarity_M\": 0.077,\n      \"provider_g_per_l_not_established\"\
    : 2.5\n    },\n    \"rationale\": \"Preserve both primary strength labels: 25%\
    \ has no stated mass/volume basis, while 10 mL of 7.7 M made up to 1000 mL gives\
    \ 0.077 M within SL-10. This calculation does not establish the provider 2.5 g/L\
    \ mass value or any main-medium concentration. No density or percentage basis\
    \ is invented.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 1\",\n        \"exact_source_quote\"\
    : \"HCl (25%; 7.7 M) 10.00 ml\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 10,\\n                        \\\"unit\\\": \\\"ml\\\"\
    ,\\n                        \\\"g_l\\\": 2.5,\\n                        \\\"mmol_l\\\
    \": 68.5683,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"SL-10: FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 1.5,\n      \"unit\"\
    : \"g\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 1.5\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 2\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"FeCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 260,\\n                        \\\"amount\\\": 1.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n\
    \                        \\\"mmol_l\\\": 7.54482,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"SL-10: ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 70,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.07\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 3\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"ZnCl2\\\",\\n                        \\\"compound_id\\\": 64,\\\
    n                        \\\"amount\\\": 70,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.07,\\n              \
    \          \\\"mmol_l\\\": 0.513573,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"SL-10: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 100,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.1\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 4\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"mmol_l\\\": 0.505293,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"SL-10: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 6,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.006\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 5\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 6,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.006,\\n             \
    \           \\\"mmol_l\\\": 0.0970246,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"SL-10: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[15].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 190,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.19\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 6\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 190,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.19,\\\
    n                        \\\"mmol_l\\\": 1.46335,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"SL-10: CuCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[16].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 2,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.002\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 7\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n\
    \                        \\\"mmol_l\\\": 0.0117314,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"SL-10: NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[17].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 24,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.024\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator. Source hexahydrate is distinct from the\
    \ asserted anhydrous nickel chloride.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 8\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 24,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.024,\\\
    n                        \\\"mmol_l\\\": 0.185187,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"SL-10: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[18].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock 595\",\n      \"amount\": 36,\n      \"unit\"\
    : \"mg\",\n      \"stock_final_make_up_ml\": 1000,\n      \"main_receiving_dose_ml\"\
    : 1,\n      \"provider_stock_g_per_l\": 0.036\n    },\n    \"rationale\": \"The\
    \ current concentration is the stock strength misplaced in the main recipe. Restore\
    \ SL-10 stage, original mass units and its separate receiving dose; do not use\
    \ stock make-up as the main denominator.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 table, row 9\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 36,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.036,\\n\
    \                        \\\"mmol_l\\\": 0.148791,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Vitamin stock: Biotin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[19].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock 3189\",\n      \"source_value\": 20,\n \
    \     \"source_unit\": \"mg/l\",\n      \"provider_stock_g_per_l\": 0.02,\n  \
    \    \"listed_stock_water_ml\": 1000,\n      \"main_receiving_dose_ml\": 1\n \
    \   },\n    \"rationale\": \"Restore the vitamin stock stage; these are not direct\
    \ main concentrations. Biotin explicitly uses mg/l, whereas the other three entries\
    \ are mg batch amounts with 1000 mL listed water. Preserve this unit distinction\
    \ and generic B12 identity; do not silently rewrite biotin as an unqualified 20\
    \ mg dose.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 vitamin table, row 1\",\n        \"exact_source_quote\"\
    : \"Biotin 20.0 mg/l\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 20,\\n                        \\\"unit\\\
    \": \\\"mg/l\\\",\\n                        \\\"g_l\\\": 0.02,\\n            \
    \            \\\"mmol_l\\\": 0.0818632,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Vitamin stock: p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[20].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock 3189\",\n      \"source_value\": 80,\n \
    \     \"source_unit\": \"mg\",\n      \"provider_stock_g_per_l\": 0.08,\n    \
    \  \"listed_stock_water_ml\": 1000,\n      \"main_receiving_dose_ml\": 1\n   \
    \ },\n    \"rationale\": \"Restore the vitamin stock stage; these are not direct\
    \ main concentrations. Biotin explicitly uses mg/l, whereas the other three entries\
    \ are mg batch amounts with 1000 mL listed water. Preserve this unit distinction\
    \ and generic B12 identity; do not silently rewrite biotin as an unqualified 20\
    \ mg dose.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 vitamin table, row 2\",\n        \"exact_source_quote\"\
    : \"p-Aminobenzoic acid 80.0 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                        \\\"compound_id\\\
    \": 47,\\n                        \\\"amount\\\": 80,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.08,\\n\
    \                        \\\"mmol_l\\\": 0.583345,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Vitamin stock: Thiamine-HCl x 2 H2O\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock 3189\",\n      \"source_value\": 200,\n\
    \      \"source_unit\": \"mg\",\n      \"provider_stock_g_per_l\": 0.2,\n    \
    \  \"listed_stock_water_ml\": 1000,\n      \"main_receiving_dose_ml\": 1\n   \
    \ },\n    \"rationale\": \"Restore the vitamin stock stage; these are not direct\
    \ main concentrations. Biotin explicitly uses mg/l, whereas the other three entries\
    \ are mg batch amounts with 1000 mL listed water. Preserve this unit distinction\
    \ and generic B12 identity; do not silently rewrite biotin as an unqualified 20\
    \ mg dose.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 vitamin table, row 3\",\n        \"exact_source_quote\"\
    : \"Thiamine-HCl x 2 H2O 200.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Thiamine-HCl x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 77,\\n                        \\\"amount\\\": 200,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.2,\\n\
    \                        \\\"mmol_l\\\": 0.535761,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Vitamin stock: Vitamin B12\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[22].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"vitamin stock 3189\",\n      \"source_value\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"provider_stock_g_per_l\": 0.05,\n    \
    \  \"listed_stock_water_ml\": 1000,\n      \"main_receiving_dose_ml\": 1\n   \
    \ },\n    \"rationale\": \"Restore the vitamin stock stage; these are not direct\
    \ main concentrations. Biotin explicitly uses mg/l, whereas the other three entries\
    \ are mg batch amounts with 1000 mL listed water. Preserve this unit distinction\
    \ and generic B12 identity; do not silently rewrite biotin as an unqualified 20\
    \ mg dose.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 vitamin table, row 4\",\n        \"exact_source_quote\"\
    : \"Vitamin B12 50.00 mg\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 50,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\n\
    \                        \\\"mmol_l\\\": 0.0368895,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Selenite-tungstate stock: NaOH\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"selenite-tungstate stock 777\",\n      \"amount\": 0.5,\n\
    \      \"unit\": \"g\",\n      \"provider_stock_g_per_l\": 0.5,\n      \"listed_stock_water_ml\"\
    : 1000,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"Restore\
    \ the separate stock recipe and 1 mL receiving addition. The current stock-strength\
    \ g/L values are not direct final-medium concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaOH\\\",\\n                        \\\"compound_id\\\": 256,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 12.5009,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Selenite-tungstate stock: Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[24].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"selenite-tungstate stock 777\",\n      \"amount\": 3,\n\
    \      \"unit\": \"mg\",\n      \"provider_stock_g_per_l\": 0.003,\n      \"listed_stock_water_ml\"\
    : 1000,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"Restore\
    \ the separate stock recipe and 1 mL receiving addition. The current stock-strength\
    \ g/L values are not direct final-medium concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 107,\\n                        \\\"amount\\\": 3,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.003,\\\
    n                        \\\"mmol_l\\\": 0.0114062,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Selenite-tungstate stock: Na2WO4 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[25].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"selenite-tungstate stock 777\",\n      \"amount\": 4,\n\
    \      \"unit\": \"mg\",\n      \"provider_stock_g_per_l\": 0.004,\n      \"listed_stock_water_ml\"\
    : 1000,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"Restore\
    \ the separate stock recipe and 1 mL receiving addition. The current stock-strength\
    \ g/L values are not direct final-medium concentrations.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 4,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.004,\\\
    n                        \\\"mmol_l\\\": 0.0121267,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Receiving dose: Trace element solution SL-10\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"solution_id\": 595,\n      \"amount\": 1,\n      \"unit\": \"ml\"\
    ,\n      \"stage\": \"main recipe with unspecified primary final volume\"\n  \
    \  },\n    \"rationale\": \"The primary and provider agree on the 1 mL addition.\
    \ Both local layers omit the stock reference and dose; do not convert it into\
    \ an absolute final concentration without a stated denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"solution\\\": \\\"Trace element solution SL-10\\\",\\n                     \
    \   \\\"solution_id\\\": 595,\\n                        \\\"amount\\\": 1,\\n\
    \                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Receiving dose: Vitamin solution\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"solution_id\": 3189,\n      \"amount\": 1,\n      \"unit\": \"ml\"\
    ,\n      \"stage\": \"main recipe with unspecified primary final volume\"\n  \
    \  },\n    \"rationale\": \"The primary and provider agree on the 1 mL addition.\
    \ Both local layers omit the stock reference and dose; do not convert it into\
    \ an absolute final concentration without a stated denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"solution\\\": \\\"Vitamin solution\\\",\\n                        \\\"solution_id\\\
    \": 3189,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Receiving dose: Selenite-tungstate solution\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"solution_id\": 777,\n      \"amount\": 1,\n      \"unit\": \"ml\"\
    ,\n      \"stage\": \"main recipe with unspecified primary final volume\"\n  \
    \  },\n    \"rationale\": \"The primary and provider agree on the 1 mL addition.\
    \ Both local layers omit the stock reference and dose; do not convert it into\
    \ an absolute final concentration without a stated denominator.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"solution\\\": \\\"Selenite-tungstate solution\\\",\\n                      \
    \  \\\"solution_id\\\": 777,\\n                        \\\"amount\\\": 1,\\n \
    \                       \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"SL-10 water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Trace element solution SL-10\",\n      \"amount\": 990,\n\
    \      \"unit\": \"ml\"\n    },\n    \"rationale\": \"Retain the stock-specific\
    \ water quantity. SL-10 lists 990 mL water and separately makes up to 1000 mL;\
    \ other stock water does not establish the main volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 990,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Vitamin stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Vitamin solution\",\n      \"amount\": 1000,\n      \"\
    unit\": \"ml\"\n    },\n    \"rationale\": \"Retain the stock-specific water quantity.\
    \ SL-10 lists 990 mL water and separately makes up to 1000 mL; other stock water\
    \ does not establish the main volume.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive1538api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1538\"\
    ,\n        \"source_locator\": \"$.data.solutions[2].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Selenite-tungstate stock water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Selenite-tungstate solution\",\n      \"amount\": 1000,\n\
    \      \"unit\": \"ml\"\n    },\n    \"rationale\": \"Retain the stock-specific\
    \ water quantity. SL-10 lists 990 mL water and separately makes up to 1000 mL;\
    \ other stock water does not establish the main volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Provider-only main water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"\
    field_path\": \"ingredients[26].concentration\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"provider_main_water_ml\": 1000,\n      \"primary_main_water_ml\"\
    : null,\n      \"source_scope\": \"provider only\"\n    },\n    \"rationale\"\
    : \"The primary main table contains no water row; only the exact provider supplies\
    \ 1000 mL. If represented, qualify this provider-only evidence explicitly. It\
    \ is neither a primary-certified final volume nor 1000 g/L water.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Main-volume evidence boundary\",\n    \"decision\": \"evidence_only\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: DSMZ | Link:\
    \ https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\",\n     \
    \   \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\",\n        \"field_path\"\
    : \"notes\",\n        \"stored\": \"Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"primary_main_volume_ml\": null,\n      \"provider_main_volume_ml\"\
    : 1000,\n      \"provider_listed_water_plus_stocks_ml\": 1003,\n      \"measured_final_volume_ml\"\
    : null\n    },\n    \"rationale\": \"Primary main volume is unspecified; its later\
    \ 1000 mL instruction is only SL-10 make-up. The provider denominator is explicit\
    \ but its 1000 mL water plus three 1 mL doses sums to 1003 mL, not a measured\
    \ final volume. Complete source comparison can document this limit without inventing\
    \ a failed access or historical mapping check.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1538api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1538\",\n        \"source_locator\"\
    : \"$.data.solutions[0].volume (solution 3187)\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"7fa4f7f21d0edb562d50a2090cfcaa67f397346d3aeb96af99d70613b9556475\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1538\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\",\n   \
    \     \"source_locator\": \"Last main-table row before stock subsections\",\n\
    \        \"exact_source_quote\": \"Selenite-tungstate solution 1 ml\",\n     \
    \   \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"SL-10 final make-up\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"SL-10\",\n      \"final_make_up_ml\": 1000\n    },\n    \"rationale\": \"\
    The current main-root preparation reproduces this quantity but loses its stock\
    \ scope. Restore it under SL-10, preserving dissolution order. Do not use it as\
    \ a main-medium volume instruction.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 preparation\",\n        \"exact_source_quote\"\
    : \"Finally make up to 1000.0 ml.\",\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Main pH, gas and sterilization quantities unspecified\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": null,\n        \"decision\": \"not_quantified\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"not_quantified\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBACTERIUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerobacterium_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"main_pH\"\
    : null,\n      \"main_gas_composition\": null,\n      \"main_sterilization_temperature\"\
    : null,\n      \"main_sterilization_duration\": null\n    },\n    \"rationale\"\
    : \"The whole primary and provider main stage were inspected: neither gives numerical\
    \ main pH, gas composition or a sterilization cycle. The only local preparation\
    \ is actually SL-10. Preserve this absence without importing another medium or\
    \ presumed default.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1538\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1538.pdf\"\
    ,\n        \"source_locator\": \"Page 1 section heading before the sole preparation\
    \ paragraph\",\n        \"exact_source_quote\": \"Trace element solution SL-10:\"\
    ,\n        \"snapshot_sha256\": \"7820d0bd7e5fa0e51bbbdb43073b3947798feaad220926e79d428075a9b4970b\"\
    ,\n        \"parsed_text_sha256\": \"a70221ec3574c1f1d902ea077f2f8521e957ebe4e4ae7dc35e6561494f7404d9\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '25 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 25/26
    primary and 25/26 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi132751
  - chebi15956
  - chebi17057
  - chebi176843
  - chebi17883
  - chebi26710
  - chebi30753
  - chebi31206
  - chebi32139
  - chebi32145
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 26: primary 96.15%;
    secondary 96.15%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact source identity and maintained ownership
  outcome: supported
  summary: CultureMech:001015 and DSMZ/MediaDive 1538 agree. The sole maintained owner
    and generated target have identical scientific fields; target-only differences
    are merge bookkeeping. All three exact stock endpoint identities agree with the
    named primary subsections and provider references. No legacy mediaingredientmech_term
    is asserted.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - primary
  - provider
  - solution595
  - solution3189
  - solution777
- assessment_id: evidence
  area: evidence
  topic: Claim-level support and exact source stages
  outcome: concern
  summary: No ingredient amount has attached supporting evidence in either local layer.
    Every local concentration and scoped source-only quantitative context has an inventory
    decision with exact quotations and locators. Matching provider transcription receives
    evidence_only, not verified. Source quantities and provider normalization remain
    separate.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - solution595
  - solution3189
  - solution777
- assessment_id: preparation
  area: completeness
  topic: Main and stock preparation boundaries
  outcome: concern
  summary: The only local preparation paragraph dissolves iron in HCl and makes up
    to 1000 mL, which belongs exclusively to SL-10. Named stock stages, receiving
    doses and water are missing. The primary does not specify main pH, gas, sterilization
    cycle or final volume; the provider supplies main water/volume independently.
    Preserve these limits rather than interpreting stock preparation as a complete
    main protocol.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - solution595
  - solution3189
  - solution777
- assessment_id: classification
  area: scope
  topic: Composition and physical state
  outcome: supported
  summary: COMPLEX/UNDEFINED is supported by yeast extract alongside specified solutes.
    LIQUID is consistent with no listed solidifier. No growth phenotype or strain-specific
    outcome follows from the medium name.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - primary
  - provider
  - solution595
  - solution3189
  - solution777
- assessment_id: forms
  area: grounding
  topic: Source-specified molecular forms and mixtures
  outcome: concern
  summary: Nickel chloride hexahydrate is mismatched to CHEBI:34887 formula Cl2Ni/mass
    129.599 in both primary and current secondary slots. The remaining inspected hydrated
    salts, thiamine hydrochloride dihydrate and generic B12 are source-compatible.
    Generic cellobiose does not imply a uniquely supplied reducing-end anomer; no
    narrower identity is invented. Yeast extract remains an unresolved mixture, not
    a falsely exact molecular compound.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - primary
  - provider
  - solution595
  - solution3189
  - solution777
- assessment_id: growth
  area: scope
  topic: Growth, taxonomy and graph assertion scope
  outcome: not_applicable
  summary: The medium title, bacterial filing and generic Microbial cultivation application
    are catalog context, not strain-level experimental growth evidence. No organism
    identifier, growth assertion, phenotype or graph membership is added. No internal
    variant/reference relationship is asserted in either complete local record.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - primary
  - provider
  - solution595
  - solution3189
  - solution777
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: writer
  area: provenance
  topic: Maintained input and current import/merge behavior
  outcome: concern
  summary: Current MediaDive API parsing reads direct ingredients from the first solution,
    excludes water and stock additions, preserves provider g_l, and separately records
    receiving stock references; its preparation reader still gathers steps from all
    solutions at the main root. Bare-unit fallback is not final-volume proof. Current
    cleanup retains the first disagreeing duplicate with a warning instead of summing
    it. Current lossless formulation merging preserves scientific assertions and order,
    not their correctness. These current implementations do not establish which historical
    version produced this record. Correct the exact maintained owner, append curation
    provenance, and regenerate only after separately authorized changes.
  target_ids:
  - CultureMech:001015
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: culturemech.001015.stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Three stock recipes are flattened into the main formula
  description: ingredients[10:26] store SL-10, vitamin and selenite/tungstate stock
    strengths directly in the medium. All three 1 mL receiving references and scoped
    water amounts are absent. HCl 2.5 g/L does not follow from an unqualified 25%
    label, while the primary also supplies 7.7 M; biotin 20 mg/l belongs to the vitamin
    stock. The primary has no main final-volume statement, whereas direct main g/L
    values match a provider-only 1000 mL basis. The flat representation conflates
    stocks, main quantities and denominators.
  target_ids:
  - CultureMech:001015
  field_paths:
  - ingredients
  - solutions
  - notes
  evidence_ids:
  - record
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
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
  issue_key: culturemech.001015.nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is identified as the anhydrous compound
  description: ingredients[17] names NiCl2 x 6 H2O, consistent with the primary SL-10
    table, but both primary and current secondary CHEBI:34887 slots specify Cl2Ni
    without hydration. Identifier validity and label correspondence do not establish
    the supplied source form.
  target_ids:
  - CultureMech:001015
  field_paths:
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - primary
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.2
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.001015.stock-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The sole preparation step belongs to SL-10, not the medium
  description: preparation_steps[0] contains the SL-10 iron/HCl dissolution and 1000
    mL make-up procedure but is stored at the main root. Neither the primary nor provider
    supplies a main preparation procedure that this stock paragraph could replace.
    Main pH, atmosphere, sterilization cycle and measured final volume remain unspecified.
  target_ids:
  - CultureMech:001015
  field_paths:
  - preparation_steps[0]
  - solutions
  evidence_ids:
  - record
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major because stock preparation is assigned
    to the receiving medium, a material representation and scope error. The P3.5 missing-sterilization
    rule does not describe this finding.
actions:
- action_id: a1
  description: Reconstruct the maintained owner with the ten main batch masses and
    separately attributed provider denominator, three named stock recipes, all receiving
    doses and stage-specific water. Preserve biotin mg/l literally and both HCl strength
    labels with unknown percentage basis. Do not infer measured final volume, density
    or main protocol from SL-10. Attach claim-level evidence before authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001015
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
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
  description: Preserve the source hexahydrate name and separately verify source-compatible
    primary and secondary grounding before replacement. Do not use anhydrous molecular
    mass to interpret the source 24 mg stock dose.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001015
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
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
  description: Move the intact existing procedure into restored SL-10 stock preparation.
    Record the main preparation gaps explicitly and seek exact target-specific evidence
    if later needed; do not fill them from stock instructions or neighboring media.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001015
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerobacterium_medium.yaml
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
- Only the exact bound collection/provider sources and pinned identifiers were assessed.
  Current source differences do not establish source chronology or the exact historical
  import version.
- Listed water, stock recipe volumes and receiving additions do not establish a measured
  assembled final volume. No unqualified percent basis, density, unspecified stock
  strength, sterilization cycle or source-specific replacement identifier is invented.
- This completed review assesses the available source disagreement and omission; it
  does not certify that the main medium has a known measured final volume or complete
  preparation protocol. No legacy MIM key is asserted, so no unavailable legacy-correspondence
  check is manufactured.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-026
- generated-medium
```
