# Source and formulation review: aminiphilus_medium (CultureMech:003734)

- Review: 20261021T143437Z-culturemech-003734-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:22:42Z
- Finished UTC: 2026-10-21T14:34:37Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1082 and both maintained contributors resolve to the same named source medium, but the stored formula combines main-medium and undiluted mineral-stock concentrations. Sodium chloride and calcium chloride additionally sum incompatible stage values. The generated target omits preparation and final pH range retained by the DSMZ owner; nickel hydrate and sodium-resazurin grounding need correction. Current formulation comparison is complete despite optional KOMODO detail access failure.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 246; batch 025 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-four task batches contain 240 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 243 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003734 | data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml | generated | aminiphilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003734 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003734 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/246/strict.tsv |
| validate-terms | passed | True | CultureMech:003734 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003734 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003734 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo1082detail | unavailable | False | CultureMech:003734 | The exact KOMODO 1082 detail request returned HTTP403. Exact catalog provenance and complete current DSMZ 1082 primary/provider formulations are available, so this optional historical-detail limitation does not prevent the current scientific comparison. Historical import execution and source chronology are not reconstructed. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003734.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003734.

41 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "KH2PO4 main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.29703",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.29703",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.29703",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 0.3 g; provider reports 0.29703 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.29703,\n                        \"mmol_l\": 2.18268,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 1",
        "exact_source_quote": "KH2PO4 0.30 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "K2HPO4 main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.29703",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.29703",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.29703",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 0.3 g; provider reports 0.29703 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.29703,\n                        \"mmol_l\": 1.70534,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 2",
        "exact_source_quote": "K2HPO4 0.30 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "NH4Cl main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.990099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.990099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.990099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 1 g; provider reports 0.990099 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.990099,\n                        \"mmol_l\": 18.51,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 3",
        "exact_source_quote": "NH4Cl 1.00 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "NaCl main",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain source main addition 10 g; provider reports 9.90099 g/L on declared 1010 mL.",
    "rationale": "Stored value additionally includes an undiluted stock g/L term. Restore the distinct main addition and stock contribution; do not subtract a stock concentration from a mass or count it as another main dose.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.90099,\n                        \"mmol_l\": 169.421,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 4",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "KCl main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0990099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0990099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0990099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 0.1 g; provider reports 0.0990099 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0990099,\n                        \"mmol_l\": 1.3281,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 5",
        "exact_source_quote": "KCl 0.10 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "CaCl2 x 2 H2O main",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain source main addition 0.1 g; provider reports 0.0990099 g/L on declared 1010 mL.",
    "rationale": "Stored value additionally includes an undiluted stock g/L term. Restore the distinct main addition and stock contribution; do not subtract a stock concentration from a mass or count it as another main dose.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0990099,\n                        \"mmol_l\": 0.673468,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 6",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "MgCl2 x 6 H2O main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.49505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.49505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.49505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 0.5 g; provider reports 0.49505 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.43503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 7",
        "exact_source_quote": "MgCl2 x 6 H2O 0.50 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Modified Wolin's mineral solution main",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain the source mineral-stock dose of 10 mL separately from its composition and main-medium mass contributions.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 8",
        "exact_source_quote": "Modified Wolin's mineral solution 10.00 ml",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Trypticase peptone main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "9.90099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "9.90099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "9.90099",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 10 g; provider reports 9.90099 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.90099,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 9",
        "exact_source_quote": "Trypticase peptone (BD BBL) 10.00 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Yeast extract main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.9802",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.9802",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.9802",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 2 g; provider reports 1.9802 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.9802,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 10",
        "exact_source_quote": "Yeast extract 2.00 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Sodium resazurin main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00049505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00049505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.00049505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 0.50 mL of 0.1% w/v sodium-resazurin stock. This is 0.0005 g per listed batch; the provider reports 0.00049505 g/L on its 1010 mL denominator.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049505,\n                        \"mmol_l\": 0.00197097,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 11",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "L-Cysteine HCl x H2O main",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.49505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.49505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.49505",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain source main addition 0.5 g; provider reports 0.49505 g/L on declared 1010 mL.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49505,\n                        \"mmol_l\": 2.81861,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 12",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.50 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Distilled water main",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain 1000 mL distilled water as a main preparation volume, not 1000 g/L or proof of final volume.",
    "rationale": "No attached local amount evidence is present. The provider numeric transcription can be supported with its stated denominator, without declaring a measured primary final volume.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main table row 13",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Nitrilotriacetic acid mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 1.5 g in the separately prepared mineral stock. Provider stock concentration 1.5 g/L, dose 10 mL, yields 0.015 g per receiving batch; conditional provider-normalized contribution 0.0148514851485 g/L. This is not 1.5 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 1",
        "exact_source_quote": "Nitrilotriacetic acid 1.50 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "MgSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 3 g in the separately prepared mineral stock. Provider stock concentration 3 g/L, dose 10 mL, yields 0.03 g per receiving batch; conditional provider-normalized contribution 0.029702970297 g/L. This is not 3 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 2",
        "exact_source_quote": "MgSO4 x 7 H2O 3.00 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "MnSO4 x H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.5 g in the separately prepared mineral stock. Provider stock concentration 0.5 g/L, dose 10 mL, yields 0.005 g per receiving batch; conditional provider-normalized contribution 0.0049504950495 g/L. This is not 0.5 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 3",
        "exact_source_quote": "MnSO4 x H2O 0.50 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "NaCl mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 1 g in the separately prepared mineral stock. Provider stock concentration 1 g/L, dose 10 mL, yields 0.01 g per receiving batch; conditional provider-normalized contribution 0.00990099009901 g/L. This is not 1 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 4",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "FeSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.1 g in the separately prepared mineral stock. Provider stock concentration 0.1 g/L, dose 10 mL, yields 0.001 g per receiving batch; conditional provider-normalized contribution 0.000990099009901 g/L. This is not 0.1 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 5",
        "exact_source_quote": "FeSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "CoSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.18 g in the separately prepared mineral stock. Provider stock concentration 0.18 g/L, dose 10 mL, yields 0.0018 g per receiving batch; conditional provider-normalized contribution 0.00178217821782 g/L. This is not 0.18 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 6",
        "exact_source_quote": "CoSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "CaCl2 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.1 g in the separately prepared mineral stock. Provider stock concentration 0.1 g/L, dose 10 mL, yields 0.001 g per receiving batch; conditional provider-normalized contribution 0.000990099009901 g/L. This is not 0.1 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 7",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "ZnSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.18 g in the separately prepared mineral stock. Provider stock concentration 0.18 g/L, dose 10 mL, yields 0.0018 g per receiving batch; conditional provider-normalized contribution 0.00178217821782 g/L. This is not 0.18 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 8",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "CuSO4 x 5 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.01 g in the separately prepared mineral stock. Provider stock concentration 0.01 g/L, dose 10 mL, yields 0.0001 g per receiving batch; conditional provider-normalized contribution 9.90099009901e-05 g/L. This is not 0.01 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 9",
        "exact_source_quote": "CuSO4 x 5 H2O 0.01 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "AlK(SO4)2 x 12 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.02 g in the separately prepared mineral stock. Provider stock concentration 0.02 g/L, dose 10 mL, yields 0.0002 g per receiving batch; conditional provider-normalized contribution 0.00019801980198 g/L. This is not 0.02 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 10",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.02 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "H3BO3 mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.01 g in the separately prepared mineral stock. Provider stock concentration 0.01 g/L, dose 10 mL, yields 0.0001 g per receiving batch; conditional provider-normalized contribution 9.90099009901e-05 g/L. This is not 0.01 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 11",
        "exact_source_quote": "H3BO3 0.01 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Na2MoO4 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.01 g in the separately prepared mineral stock. Provider stock concentration 0.01 g/L, dose 10 mL, yields 0.0001 g per receiving batch; conditional provider-normalized contribution 9.90099009901e-05 g/L. This is not 0.01 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 12",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.01 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "NiCl2 x 6 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.03 g in the separately prepared mineral stock. Provider stock concentration 0.03 g/L, dose 10 mL, yields 0.0003 g per receiving batch; conditional provider-normalized contribution 0.00029702970297 g/L. This is not 0.03 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 13",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Na2SeO3 x 5 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.3 mg in the separately prepared mineral stock. Provider stock concentration 0.0003 g/L, dose 10 mL, yields 3e-06 g per receiving batch; conditional provider-normalized contribution 2.9702970297e-06 g/L. This is not 0.0003 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 14",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.30 mg",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Na2WO4 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.4 mg in the separately prepared mineral stock. Provider stock concentration 0.0004 g/L, dose 10 mL, yields 4e-06 g per receiving batch; conditional provider-normalized contribution 3.9603960396e-06 g/L. This is not 0.0004 g/L directly in main medium.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 15",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Distilled water mineral stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Retain stock water 1000 mL within the mineral-stock preparation, distinct from main water; provider declares this stock volume 1000 mL.",
    "rationale": "The stock formula is explicitly present in this primary, so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve original hydrate and units, and keep provider-declared stock/main volumes distinct from measurement. Sodium chloride and calcium are also supplied directly in the main recipe and need separate stage rows.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[15]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 mineral stock row 16",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Sodium chloride combined contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.90099",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "The source supplies a total 10.01 g per listed receiving batch after stock transfer; on provider-declared 1010 mL this is 9.91089108911 g/L.",
    "rationale": "The stored duplicate sum combines main g/L with undiluted-stock g/L, not two comparable main-medium concentrations. Keep the explicit recipe stages as authoritative representation; any collapsed total must declare the provider denominator and avoid double counting the restored stock.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.90099,\n                        \"mmol_l\": 169.421,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Calcium chloride dihydrate combined contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.19900990000000002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "The source supplies a total 0.101 g per listed receiving batch after stock transfer; on provider-declared 1010 mL this is 0.1 g/L.",
    "rationale": "The stored duplicate sum combines main g/L with undiluted-stock g/L, not two comparable main-medium concentrations. Keep the explicit recipe stages as authoritative representation; any collapsed total must declare the provider denominator and avoid double counting the restored stock.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0990099,\n                        \"mmol_l\": 0.673468,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Resazurin stock strength",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "0.1% w/v = 1 g/L sodium-resazurin stock; 0.50 mL contributes 0.0005 g.",
    "rationale": "Mass/volume percentage is explicit, unlike an unqualified percent. Preserve the sodium salt; do not use free-acid molecular mass.",
    "source_snippets": [
      {
        "source_key": "dsmz1082",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf",
        "source_locator": "Page 1 main sodium-resazurin row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b",
        "parsed_text_sha256": "f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Declared main-volume basis versus listed liquid inputs",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1 and dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.  The pH of the complete medium should be 7.0 - 7.2."
          },
          {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."
          }
        ],
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": "Provider declares 1010 mL. Main liquid entries are 1000+10+0.50=1010.5 mL before any adjustment. The primary does not state a final make-up volume.",
    "rationale": "Do not silently substitute 1010.5 mL or assume 1010 mL is a measured final volume. Existing provider-normalized values can be documented with that explicit limitation; original mass/dose/water rows remain the primary representation.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1010",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049505,\n                        \"mmol_l\": 0.00197097,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      },
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 17,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Main initial pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.1,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.1,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1 and dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.  The pH of the complete medium should be 7.0 - 7.2.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "pH 7.1 is a preparation adjustment before dispensing/autoclaving, not a replacement for the final range.",
    "rationale": "Local layer decisions distinguish missing target/KOMODO preparation from existing DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "adjust pH to 7.1",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Main final pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.0,
          "max": 7.2
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain complete-medium final pH 7.0–7.2; already present in DSMZ owner ph_range.",
    "rationale": "Local layer decisions distinguish missing target/KOMODO preparation from existing DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "The pH of the complete medium should be 7.0 - 7.2.",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Main sparging duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1 and dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.  The pH of the complete medium should be 7.0 - 7.2.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 30–45 minutes at the main sparging stage.",
    "rationale": "Local layer decisions distinguish missing target/KOMODO preparation from existing DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "30 - 45 min",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Main nitrogen atmosphere",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1 and dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.  The pH of the complete medium should be 7.0 - 7.2.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 100% N2 during main sparging and same gas during dispensing.",
    "rationale": "Local layer decisions distinguish missing target/KOMODO preparation from existing DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "100% N2",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Stock first adjustment",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Within mineral stock, dissolve nitrilotriacetic acid first, adjust to pH 6.5 with KOH, then add minerals.",
    "rationale": "Local layer decisions distinguish missing target/KOMODO preparation from existing DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].steps[0].step",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Stock final adjustment",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Adjust the mineral stock final pH 7.0 with KOH; do not apply this as the final main-medium range.",
    "rationale": "Local layer decisions distinguish missing target/KOMODO preparation from existing DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].steps[0].step",
        "exact_source_quote": "final to pH 7.0 with KOH.",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "KOH amount",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "KOH receiving quantity is unquantified; source gives two stock pH endpoints.",
    "rationale": "No fixed dose or stock strength is supplied; correct the DSMZ owner root preparation scope and recover missing target/KOMODO stock context.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[1].steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1 and dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.  The pH of the complete medium should be 7.0 - 7.2.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Autoclaving is specified, but no temperature or duration is given.",
    "rationale": "Do not add a default cycle or transfer one from DSM 141. Preserve cysteine addition before pH adjustment and dispensing as stated in this exact source.",
    "source_snippets": [
      {
        "source_key": "mediadive1082api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1082",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "and autoclave.",
        "snapshot_sha256": "03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:003734.

22 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 22/24 primary and 21/24 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 24: primary 91.67%; secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source accession and maintained ownership

identity: supported. Targets: CultureMech:003734.

The generated CM003734 resolves to exact KOMODO 1082 owner CM003734 and DSMZ 1082 owner CM000517. Both recipe IDs and reciprocal SOURCE_DUPLICATE paths resolve in the inspected tree; the two ingredients arrays are exactly equal. Same accession/signature does not imply all fields are equal: DSMZ retains final ph_range and preparation omitted by target/KOMODO.

### Claim-level amount support and source scope

evidence: concern. Targets: CultureMech:003734.

The local layers have import provenance but no attached amount evidence. The inventory covers every local concentration and scoped source-only quantity using literal excerpts, exact source locators, units, stages and original capture hashes. Provider-declared volume is kept separate from measured assembled final volume.

### Preparation stages, source-only additions and owner differences

completeness: concern. Targets: CultureMech:003734.

The target/KOMODO omit main preparation; DSMZ retains the exact main sequence and final pH range but places mineral-stock pH instructions at the main root. Recover the distinct main and mineral stages, water, dose and source strength. No source autoclave cycle is available; no default is invented.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:003734.

COMPLEX/UNDEFINED and LIQUID are consistent with Trypticase peptone, yeast extract and absence of a gelling agent in this formulation. The generic application and source collection metadata do not establish growth, phenotype or a new taxonomic assignment.

### Supplied forms and chemical specificity

grounding: concern. Targets: CultureMech:003734.

Source nickel chloride is explicitly hexahydrate, whereas CHEBI:34887 has formula Cl2Ni. Source sodium resazurin is a sodium salt, whereas CHEBI:8806 has sodium-free formula C12H7NO4. All other asserted specific hydrate/form correspondences match the source at its stated specificity. Trypticase peptone and yeast extract remain mixtures without invented pure-compound IDs; retain source BD BBL qualifier.

### Growth, organism taxonomy and graph claims

scope: not_applicable. Targets: CultureMech:003734.

The title, generic Microbial cultivation application and catalog Aerobic flags are not experimental growth or taxonomy evidence. No growth assertions, current taxonomy IDs or graph membership are added. Explicit source strain qualifiers remain formulation scope only.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003734.

26 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Authoritative inputs and current writer scope

provenance: concern. Targets: CultureMech:003734.

Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction.

## Findings

### f1: Undiluted mineral-stock values are stored as main-medium concentrations

blocker / open / confirmed; issue key: culturemech.003734.main-stock-stage-collapse.

All three layers flatten 15 mineral solutes into the main recipe. NaCl 10.90099 and calcium chloride dihydrate 0.19900990000000002 additionally sum main g/L with undiluted-stock g/L. The primary explicitly calls for 10 mL of the separately described stock, not its full-strength composition. Nine unchanged main values match provider normalization but have no attached amount evidence; provider volume 1010 mL is not asserted as a measured final volume.

### f2: Nickel hydration and sodium-resazurin identity do not match asserted forms

major / open / confirmed; issue key: culturemech.003734.nickel-resazurin-forms.

The source and local preferred terms specify NiCl2 x 6H2O, but primary and secondary CHEBI:34887 correspond to anhydrous Cl2Ni. Sodium resazurin is mapped to CHEBI:8806, formula C12H7NO4 without sodium. Canonical labels and current secondary-key existence do not resolve either source-form mismatch.

### f3: Preparation and final pH are lost or assigned to the wrong stage

major / open / confirmed; issue key: culturemech.003734.main-and-stock-preparation-scope.

Target/KOMODO lack preparation and retain only initial ph_value 7.1; the DSMZ owner has final ph_range 7.0–7.2 and main procedure, but its second root step is the mineral-stock procedure. Stock pH 6.5 then7.0 must remain separate from main final pH 7.0–7.2. The main cysteine timing and nitrogen context are source-specific.

### f4: Historical timestamp strings remain malformed or timezone-naive

minor / open / confirmed; issue key: culturemech.003734.historical-timestamp-shape.

The target and KOMODO owner each retain one malformed import timestamp and one timezone-naive resolver timestamp. These do not validate source chronology and should not be silently rewritten.

## Recommended Actions And Acceptance Checks

### a1

Repair both normalized contributors with distinct main additions and mineral-stock composition/dose; undo the two incompatible duplicate sums. Preserve main and stock water, exact chemical forms and source units; attach claim-level evidence. Document provider 1010 mL versus listed liquid 1010.5 mL without inventing a measured denominator. Regenerate only after authorized owner correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify exact supplied-form replacements before changing both normalized owners; preserve source masses and stock scope. Do not infer uninspected replacement IDs or convert using anhydrous/free-acid molecular weights.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve DSMZ owner main procedure and ph_range, recover corresponding missing KOMODO context, and move/represent the mineral procedure at its stock scope. Retain initial versus final pH and unquantified KOH/cycle limits; do not overwrite final range with a midpoint or stock pH. Review current resolver/merge ownership before authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve original history and append a clarification identifying the literal timestamp defects and known provenance limits when the owner is curated; do not fabricate historical times or source chronology.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/aminiphilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch025/246/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/246/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml:1:id: CultureMech:003734<br>./data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml:1:id: CultureMech:003734<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/246/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 28 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/246/evidence-context-original.json; Complete frozen target/owners, source stages, exact secondary lookup and ignored-inclusive relationships | context_only | Full captured records re-read and compared by exact equality with fresh inspected records. Context is supporting provenance; exact bound primary/provider captures independently support scientific claims. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf; Page 1 full main table, procedure and mineral-stock subsection | supports | The primary specifies 13 main rows, including mineral stock and water, and 16 separate mineral-stock rows including its own water. It distinguishes initial pH 7.1, final pH 7.0–7.2 and stock pH 6.5 then 7.0. It does not declare a measured main final volume or sterilization cycle. |
| provider | https://mediadive.dsmz.de/rest/medium/1082; data.medium; solutions[0] ID 2191 and solutions[1] ID 241, all recipes/steps | supports | The exact provider declares main volume 1010 mL and stock volume 1000 mL; main g_l and stock g_l belong to different scopes. Listed primary liquid inputs total 1010.5 mL before adjustment, not a measured final volume. Provider normalization is retained as explicitly provider-based evidence. |
| stock-crosscheck | https://mediadive.dsmz.de/rest/solution/241; data.id, name, volume, complete recipe and preparation | supports | Exact solution241 agrees with the mineral subsection explicitly included in DSM 1082. Other DSM 141 main-medium, vitamin, strain and incubation instructions are excluded. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact first-cell accession 1082 catalog row | supports | The exact KOMODO catalog maps accession 1082 to DSMZ 1082. This is accession provenance, not support for every normalized quantity or preparation field. |
| komodo1082detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1082; Preserved exact public retrieval result | context_only | The exact KOMODO 1082 detail request returned HTTP403. Exact catalog provenance and complete current DSMZ 1082 primary/provider formulations are available, so this optional historical-detail limitation does not prevent the current scientific comparison. Historical import execution and source chronology are not reconstructed. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch025/246/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml; data/normalized_yaml/bacterial/aminiphilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.710392"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.710392"}]}, {"input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml", "events": 8, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code separates first-stage ingredients and stock references and retains provider g_l values, but collects preparation steps from all solutions at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation; current lossless merge requires scientific-field equality. Current cleanup flags disagreeing duplicate values rather than summing them. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact KOMODO 1082 detail request returned HTTP403. Exact catalog provenance and complete current DSMZ 1082 primary/provider formulations are available, so this optional historical-detail limitation does not prevent the current scientific comparison. Historical import execution and source chronology are not reconstructed.
- Only exact per-record bound captures are used. Current collection and provider differences do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently establish a measured final mixture volume. No density, percent basis, exact hydration, default sterilization cycle or stock volume is invented.
- Current scientific formulation comparison is completed: optional historical KOMODO detail is inaccessible, but exact catalog identity and primary/provider recipe and stock content are available. No required historical legacy-secondary correspondence is asserted in these layers.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143437Z-culturemech-003734-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aminiphilus_medium (CultureMech:003734)'
started_at: '2026-10-21T14:22:42Z'
finished_at: '2026-10-21T14:34:37Z'
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
summary: DSMZ 1082 and both maintained contributors resolve to the same named source
  medium, but the stored formula combines main-medium and undiluted mineral-stock
  concentrations. Sodium chloride and calcium chloride additionally sum incompatible
  stage values. The generated target omits preparation and final pH range retained
  by the DSMZ owner; nickel hydrate and sodium-resazurin grounding need correction.
  Current formulation comparison is complete despite optional KOMODO detail access
  failure.
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
  - path: data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
    sha256: fb7679d44b23eaa26bd1e569038f6a49affb45bf46c9992f624d5c0d668ca81f
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    sha256: 835f8644cc1bc9eca2f1b42b20a6188d66610e278f74f5a70f0004a3df8cf59e
    role: context
  - path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
    sha256: 683100b5f6dcafb850e5146d47a5915c4be6a458cbcd6c59058f64b78152c1d0
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
  selection: Task review 246; batch 025 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-four task batches
    contain 240 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 243 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003734
targets:
- target_id: CultureMech:003734
  path: data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  label: aminiphilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch025/246/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/246/strict.tsv"
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003734
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
  - CultureMech:003734
- check_id: komodo1082detail-source-access
  name: 'Exact source content access: komodo1082detail'
  required: false
  status: unavailable
  summary: The exact KOMODO 1082 detail request returned HTTP403. Exact catalog provenance
    and complete current DSMZ 1082 primary/provider formulations are available, so
    this optional historical-detail limitation does not prevent the current scientific
    comparison. Historical import execution and source chronology are not reconstructed.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - komodo1082detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:34.685834Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch025/246/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:36.268715Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/246/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:38.465837Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:39.626359Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:34:36Z'
  support: supports
  summary: './data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml:1:id: CultureMech:003734

    ./data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml:1:id: CultureMech:003734

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/246/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:34:36Z'
  support: supports
  summary: 28 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 52be3b3efe03184cb9fccfea6b43b4dd7672eba99edbc10a1628b4c7e306a1ea
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/246/evidence-context-original.json
  locator: Complete frozen target/owners, source stages, exact secondary lookup and
    ignored-inclusive relationships
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Full captured records re-read and compared by exact equality with fresh
    inspected records. Context is supporting provenance; exact bound primary/provider
    captures independently support scientific claims.
  snapshot_sha256: d9e1b77c2bef30566c5aedaeca58692a59a60421e74f24f3c8d1a2d5a733a40e
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf
  locator: Page 1 full main table, procedure and mineral-stock subsection
  accessed_at: '2026-10-21T14:01:45.680103Z'
  support: supports
  summary: The primary specifies 13 main rows, including mineral stock and water,
    and 16 separate mineral-stock rows including its own water. It distinguishes initial
    pH 7.1, final pH 7.0–7.2 and stock pH 6.5 then 7.0. It does not declare a measured
    main final volume or sterilization cycle.
  snapshot_sha256: 166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1082
  locator: data.medium; solutions[0] ID 2191 and solutions[1] ID 241, all recipes/steps
  accessed_at: '2026-10-21T14:01:43.148679Z'
  support: supports
  summary: The exact provider declares main volume 1010 mL and stock volume 1000 mL;
    main g_l and stock g_l belong to different scopes. Listed primary liquid inputs
    total 1010.5 mL before adjustment, not a measured final volume. Provider normalization
    is retained as explicitly provider-based evidence.
  snapshot_sha256: 03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203
- evidence_id: stock-crosscheck
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: data.id, name, volume, complete recipe and preparation
  accessed_at: '2026-10-21T10:37:16.846684Z'
  support: supports
  summary: Exact solution241 agrees with the mineral subsection explicitly included
    in DSM 1082. Other DSM 141 main-medium, vitamin, strain and incubation instructions
    are excluded.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact first-cell accession 1082 catalog row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact KOMODO catalog maps accession 1082 to DSMZ 1082. This is accession
    provenance, not support for every normalized quantity or preparation field.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo1082detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1082
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:01:43.148291Z'
  support: context_only
  summary: The exact KOMODO 1082 detail request returned HTTP403. Exact catalog provenance
    and complete current DSMZ 1082 primary/provider formulations are available, so
    this optional historical-detail limitation does not prevent the current scientific
    comparison. Historical import execution and source chronology are not reconstructed.
  snapshot_sha256: b3aaa5ef120c836658805673651772cd568cb3a3f9017e652337caa2ceabb056
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/246/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: b35efe480eb432f8c68643f4f74585134a710368f380fb0f4e510117211f4ee5
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
  accessed_at: '2026-10-21T14:34:36Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
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
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic
    acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label":
    "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364":
    [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O",
    "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id":
    "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml;
    data/normalized_yaml/bacterial/aminiphilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:59.710392"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:59.710392"}]}, {"input": "data/normalized_yaml/bacterial/aminiphilus_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:36Z'
  support: context_only
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 41 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    KH2PO4 main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29703\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29703\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.29703\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 0.3 g; provider reports 0.29703 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.3,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.29703,\\n            \
    \            \\\"mmol_l\\\": 2.18268,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 1\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.30 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"K2HPO4 main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29703\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.29703\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.29703\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 0.3 g; provider reports 0.29703 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.3,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.29703,\\n            \
    \            \\\"mmol_l\\\": 1.70534,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 2\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.30 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"NH4Cl main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.990099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.990099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.990099\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 1 g; provider reports 0.990099 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.990099,\\n           \
    \             \\\"mmol_l\\\": 18.51,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 3\",\n        \"exact_source_quote\"\
    : \"NH4Cl 1.00 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"NaCl main\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.90099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"10.90099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10.90099\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ source main addition 10 g; provider reports 9.90099 g/L on declared 1010 mL.\"\
    ,\n    \"rationale\": \"Stored value additionally includes an undiluted stock\
    \ g/L term. Restore the distinct main addition and stock contribution; do not\
    \ subtract a stock concentration from a mass or count it as another main dose.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1082api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\
    \": 43,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 9.90099,\\\
    n                        \\\"mmol_l\\\": 169.421,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table row 4\",\n        \"exact_source_quote\"\
    : \"NaCl 10.00 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"KCl main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0990099\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"evidence_only\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0990099\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"evidence_only\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.0990099\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 0.1 g; provider reports 0.0990099 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0990099,\\n          \
    \              \\\"mmol_l\\\": 1.3281,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 5\",\n        \"exact_source_quote\"\
    : \"KCl 0.10 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O main\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 0.1 g; provider reports 0.0990099 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"Stored value additionally includes an undiluted\
    \ stock g/L term. Restore the distinct main addition and stock contribution; do\
    \ not subtract a stock concentration from a mass or count it as another main dose.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1082api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.0990099,\\n                        \\\"mmol_l\\\": 0.673468,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 6\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.10 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"MgCl2 x 6 H2O main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49505\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49505\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.49505\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 0.5 g; provider reports 0.49505 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.43503,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table row 7\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 0.50 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Modified Wolin's mineral solution main\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain the source mineral-stock dose of 10 mL separately from its composition\
    \ and main-medium mass contributions.\",\n    \"rationale\": \"No attached local\
    \ amount evidence is present. The provider numeric transcription can be supported\
    \ with its stated denominator, without declaring a measured primary final volume.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1082api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n       \
    \                 \\\"solution_id\\\": 241,\\n                        \\\"amount\\\
    \": 10,\\n                        \\\"unit\\\": \\\"ml\\\",\\n               \
    \         \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 8\",\n        \"exact_source_quote\"\
    : \"Modified Wolin's mineral solution 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\",\n    \
    \    \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Trypticase peptone main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.90099\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"9.90099\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"9.90099\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 10 g; provider reports 9.90099 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Trypticase peptone\\\",\\n                        \\\"compound_id\\\
    \": 124,\\n                        \\\"attribute\\\": \\\"BD BBL\\\",\\n     \
    \                   \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 9.90099,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 9\",\n        \"exact_source_quote\"\
    : \"Trypticase peptone (BD BBL) 10.00 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Yeast extract main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.9802\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.9802\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"1.9802\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 2 g; provider reports 1.9802 g/L on declared 1010\
    \ mL.\",\n    \"rationale\": \"No attached local amount evidence is present. The\
    \ provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.9802,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 10\",\n        \"exact_source_quote\"\
    : \"Yeast extract 2.00 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Sodium resazurin main\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00049505\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"evidence_only\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00049505\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"evidence_only\"\n      },\n      {\n     \
    \   \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00049505\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.50 mL of 0.1% w/v sodium-resazurin stock. This is 0.0005 g per listed\
    \ batch; the provider reports 0.00049505 g/L on its 1010 mL denominator.\",\n\
    \    \"rationale\": \"No attached local amount evidence is present. The provider\
    \ numeric transcription can be supported with its stated denominator, without\
    \ declaring a measured primary final volume.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.00049505,\\n        \
    \                \\\"mmol_l\\\": 0.00197097,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 11\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"L-Cysteine HCl x H2O main\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49505\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.49505\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[10].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.49505\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain source main addition 0.5 g; provider reports 0.49505 g/L on declared\
    \ 1010 mL.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 16,\\n                        \\\
    \"compound\\\": \\\"L-Cysteine HCl x H2O\\\",\\n                        \\\"compound_id\\\
    \": 770,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.49505,\\\
    n                        \\\"mmol_l\\\": 2.81861,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table row 12\",\n        \"exact_source_quote\"\
    : \"L-Cysteine HCl x H2O 0.50 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Distilled water main\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[24].concentration\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain 1000\
    \ mL distilled water as a main preparation volume, not 1000 g/L or proof of final\
    \ volume.\",\n    \"rationale\": \"No attached local amount evidence is present.\
    \ The provider numeric transcription can be supported with its stated denominator,\
    \ without declaring a measured primary final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 17,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 main table row 13\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Nitrilotriacetic acid mineral stock\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1.5 g in the separately prepared mineral stock. Provider stock concentration\
    \ 1.5 g/L, dose 10 mL, yields 0.015 g per receiving batch; conditional provider-normalized\
    \ contribution 0.0148514851485 g/L. This is not 1.5 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                        \\\"compound_id\\\
    \": 189,\\n                        \\\"amount\\\": 1.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n\
    \                        \\\"mmol_l\\\": 7.84765,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 mineral stock row 1\",\n        \"exact_source_quote\"\
    : \"Nitrilotriacetic acid 1.50 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"MgSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 3 g in the separately prepared mineral stock. Provider stock concentration\
    \ 3 g/L, dose 10 mL, yields 0.03 g per receiving batch; conditional provider-normalized\
    \ contribution 0.029702970297 g/L. This is not 3 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 3,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n      \
    \                  \\\"mmol_l\\\": 12.1716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 2\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 3.00 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"MnSO4 x H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.5 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.5 g/L, dose 10 mL, yields 0.005 g per receiving batch; conditional provider-normalized\
    \ contribution 0.0049504950495 g/L. This is not 0.5 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 2.9583,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 3\",\n        \"exact_source_quote\"\
    : \"MnSO4 x H2O 0.50 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"NaCl mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.90099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"10.90099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10.90099\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 1 g in the separately prepared mineral stock. Provider stock concentration 1\
    \ g/L, dose 10 mL, yields 0.01 g per receiving batch; conditional provider-normalized\
    \ contribution 0.00990099009901 g/L. This is not 1 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 4\",\n        \"exact_source_quote\"\
    : \"NaCl 1.00 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"FeSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.1 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.1 g/L, dose 10 mL, yields 0.001 g per receiving batch; conditional provider-normalized\
    \ contribution 0.000990099009901 g/L. This is not 0.1 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.359693,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 mineral stock row 5\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O 0.10 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"CoSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.18\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.18 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.18 g/L, dose 10 mL, yields 0.0018 g per receiving batch; conditional provider-normalized\
    \ contribution 0.00178217821782 g/L. This is not 0.18 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 198,\\n                        \\\"amount\\\": 0.18,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 1.16132,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 mineral stock row 6\",\n        \"exact_source_quote\"\
    : \"CoSO4 x 7 H2O 0.18 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.1 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.1 g/L, dose 10 mL, yields 0.001 g per receiving batch; conditional provider-normalized\
    \ contribution 0.000990099009901 g/L. This is not 0.1 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.680203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 7\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.10 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"ZnSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.18\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.18 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.18 g/L, dose 10 mL, yields 0.0018 g per receiving batch; conditional provider-normalized\
    \ contribution 0.00178217821782 g/L. This is not 0.18 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.18,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 0.625954,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 mineral stock row 8\",\n        \"exact_source_quote\"\
    : \"ZnSO4 x 7 H2O 0.18 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"CuSO4 x 5 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.01 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.01 g/L, dose 10 mL, yields 0.0001 g per receiving batch; conditional provider-normalized\
    \ contribution 9.90099009901e-05 g/L. This is not 0.01 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0400503,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 9\",\n        \"exact_source_quote\"\
    : \"CuSO4 x 5 H2O 0.01 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"AlK(SO4)2 x 12 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.02 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.02 g/L, dose 10 mL, yields 0.0002 g per receiving batch; conditional provider-normalized\
    \ contribution 0.00019801980198 g/L. This is not 0.02 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0421596,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 10\",\n        \"exact_source_quote\"\
    : \"AlK(SO4)2 x 12 H2O 0.02 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"H3BO3 mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.01 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.01 g/L, dose 10 mL, yields 0.0001 g per receiving batch; conditional provider-normalized\
    \ contribution 9.90099009901e-05 g/L. This is not 0.01 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\":\
    \ 37,\\n                        \\\"amount\\\": 0.01,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\n \
    \                       \\\"mmol_l\\\": 0.161708,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 mineral stock row 11\",\n        \"exact_source_quote\"\
    : \"H3BO3 0.01 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Na2MoO4 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.01 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.01 g/L, dose 10 mL, yields 0.0001 g per receiving batch; conditional provider-normalized\
    \ contribution 9.90099009901e-05 g/L. This is not 0.01 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.01,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0413309,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 12\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 0.01 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"NiCl2 x 6 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.03\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.03 g in the separately prepared mineral stock. Provider stock concentration\
    \ 0.03 g/L, dose 10 mL, yields 0.0003 g per receiving batch; conditional provider-normalized\
    \ contribution 0.00029702970297 g/L. This is not 0.03 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 0.03,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.03,\\\
    n                        \\\"mmol_l\\\": 0.231483,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 mineral stock row 13\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 0.03 g\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Na2SeO3 x 5 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0003\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.3 mg in the separately prepared mineral stock. Provider stock concentration\
    \ 0.0003 g/L, dose 10 mL, yields 3e-06 g per receiving batch; conditional provider-normalized\
    \ contribution 2.9702970297e-06 g/L. This is not 0.0003 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 107,\\n                        \\\"amount\\\": 0.3,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0003,\\\
    n                        \\\"mmol_l\\\": 0.00114062,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 14\",\n        \"exact_source_quote\"\
    : \"Na2SeO3 x 5 H2O 0.30 mg\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Na2WO4 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"Retain\
    \ 0.4 mg in the separately prepared mineral stock. Provider stock concentration\
    \ 0.0004 g/L, dose 10 mL, yields 4e-06 g per receiving batch; conditional provider-normalized\
    \ contribution 3.9603960396e-06 g/L. This is not 0.0004 g/L directly in main medium.\"\
    ,\n    \"rationale\": \"The stock formula is explicitly present in this primary,\
    \ so no transfer of DSM 141 parent medium is required. Restore stock scope, preserve\
    \ original hydrate and units, and keep provider-declared stock/main volumes distinct\
    \ from measurement. Sodium chloride and calcium are also supplied directly in\
    \ the main recipe and need separate stage rows.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 249,\\n                        \\\"amount\\\": 0.4,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0004,\\\
    n                        \\\"mmol_l\\\": 0.00121267,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 15\",\n        \"exact_source_quote\"\
    : \"Na2WO4 x 2 H2O 0.40 mg\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Distilled water mineral stock\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain stock water 1000 mL within the mineral-stock preparation, distinct\
    \ from main water; provider declares this stock volume 1000 mL.\",\n    \"rationale\"\
    : \"The stock formula is explicitly present in this primary, so no transfer of\
    \ DSM 141 parent medium is required. Restore stock scope, preserve original hydrate\
    \ and units, and keep provider-declared stock/main volumes distinct from measurement.\
    \ Sodium chloride and calcium are also supplied directly in the main recipe and\
    \ need separate stage rows.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive1082api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[15]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 16,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1082\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\",\n   \
    \     \"source_locator\": \"Page 1 mineral stock row 16\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Sodium chloride combined contribution\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.90099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"10.90099\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10.90099\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": \"The\
    \ source supplies a total 10.01 g per listed receiving batch after stock transfer;\
    \ on provider-declared 1010 mL this is 9.91089108911 g/L.\",\n    \"rationale\"\
    : \"The stored duplicate sum combines main g/L with undiluted-stock g/L, not two\
    \ comparable main-medium concentrations. Keep the explicit recipe stages as authoritative\
    \ representation; any collapsed total must declare the provider denominator and\
    \ avoid double counting the restored stock.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 9.90099,\\n            \
    \            \\\"mmol_l\\\": 169.421,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Calcium chloride dihydrate combined contribution\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.19900990000000002\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"The source supplies a total 0.101 g per listed receiving batch after stock\
    \ transfer; on provider-declared 1010 mL this is 0.1 g/L.\",\n    \"rationale\"\
    : \"The stored duplicate sum combines main g/L with undiluted-stock g/L, not two\
    \ comparable main-medium concentrations. Keep the explicit recipe stages as authoritative\
    \ representation; any collapsed total must declare the provider denominator and\
    \ avoid double counting the restored stock.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0990099,\\\
    n                        \\\"mmol_l\\\": 0.673468,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.680203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Resazurin stock strength\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.1% w/v = 1 g/L sodium-resazurin stock; 0.50 mL contributes 0.0005 g.\",\n\
    \    \"rationale\": \"Mass/volume percentage is explicit, unlike an unqualified\
    \ percent. Preserve the sodium salt; do not use free-acid molecular mass.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1082\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1082.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main sodium-resazurin row\",\n       \
    \ \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"\
    snapshot_sha256\": \"166af6f2b7e905080b8c22f01eefa3faa4b5173cc968466ed63ea7392a96b74b\"\
    ,\n        \"parsed_text_sha256\": \"f9f9268dd3531256fa5b0de7470a4a4b967f54eb8801178573fe0c6159911285\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Declared main-volume basis versus listed liquid inputs\",\n    \"decision\"\
    : \"unsupported\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"unsupported\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n   \
    \     \"decision\": \"unsupported\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/aminiphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": [\n          {\n            \"step_number\"\
    : 1,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min with\
    \ 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1 and\
    \ dispense medium under same gas atmosphere into anoxic Hungate-type tubes or\
    \ serum vials and autoclave.  The pH of the complete medium should be 7.0 - 7.2.\"\
    \n          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"ADJUST_PH\",\n            \"description\": \"First dissolve nitrilotriacetic\
    \ acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0\
    \ with KOH.\"\n          }\n        ],\n        \"decision\": \"unsupported\"\n\
    \      }\n    ],\n    \"proposed_source_representation\": \"Provider declares\
    \ 1010 mL. Main liquid entries are 1000+10+0.50=1010.5 mL before any adjustment.\
    \ The primary does not state a final make-up volume.\",\n    \"rationale\": \"\
    Do not silently substitute 1010.5 mL or assume 1010 mL is a measured final volume.\
    \ Existing provider-normalized values can be documented with that explicit limitation;\
    \ original mass/dose/water rows remain the primary representation.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"mediadive1082api\",\n\
    \        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n   \
    \     \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1010\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Sodium resazurin\\\",\\n                        \\\"compound_id\\\
    \": 1852,\\n                        \\\"attribute\\\": \\\"0.1% w/v\\\",\\n  \
    \                      \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"g_l\\\": 0.00049505,\\n        \
    \                \\\"mmol_l\\\": 0.00197097,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 17,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Main initial pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.1,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.1,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min\
    \ with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1\
    \ and dispense medium under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave.  The pH of the complete medium should be 7.0 -\
    \ 7.2.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"pH 7.1 is a preparation adjustment before dispensing/autoclaving, not a replacement\
    \ for the final range.\",\n    \"rationale\": \"Local layer decisions distinguish\
    \ missing target/KOMODO preparation from existing DSMZ prose. Preserve the source\
    \ sequence; no stock pH is a main final-pH substitute.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"adjust\
    \ pH to 7.1\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Main final pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.0,\n          \"max\": 7.2\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Retain complete-medium\
    \ final pH 7.0–7.2; already present in DSMZ owner ph_range.\",\n    \"rationale\"\
    : \"Local layer decisions distinguish missing target/KOMODO preparation from existing\
    \ DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1082api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n \
    \       \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"The pH of the complete medium should be 7.0 - 7.2.\",\n\
    \        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Main sparging duration\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min\
    \ with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1\
    \ and dispense medium under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave.  The pH of the complete medium should be 7.0 -\
    \ 7.2.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 30–45 minutes at the main sparging stage.\",\n    \"rationale\": \"\
    Local layer decisions distinguish missing target/KOMODO preparation from existing\
    \ DSMZ prose. Preserve the source sequence; no stock pH is a main final-pH substitute.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1082api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\",\n \
    \       \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n        \"\
    exact_source_quote\": \"30 - 45 min\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"Main nitrogen atmosphere\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min\
    \ with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1\
    \ and dispense medium under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave.  The pH of the complete medium should be 7.0 -\
    \ 7.2.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 100% N2 during main sparging and same gas during dispensing.\",\n \
    \   \"rationale\": \"Local layer decisions distinguish missing target/KOMODO preparation\
    \ from existing DSMZ prose. Preserve the source sequence; no stock pH is a main\
    \ final-pH substitute.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1082api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"100% N2\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"Stock first adjustment\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Within mineral stock,\
    \ dissolve nitrilotriacetic acid first, adjust to pH 6.5 with KOH, then add minerals.\"\
    ,\n    \"rationale\": \"Local layer decisions distinguish missing target/KOMODO\
    \ preparation from existing DSMZ prose. Preserve the source sequence; no stock\
    \ pH is a main final-pH substitute.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive1082api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"adjust pH to 6.5 with KOH\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Stock final adjustment\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Adjust the mineral\
    \ stock final pH 7.0 with KOH; do not apply this as the final main-medium range.\"\
    ,\n    \"rationale\": \"Local layer decisions distinguish missing target/KOMODO\
    \ preparation from existing DSMZ prose. Preserve the source sequence; no stock\
    \ pH is a main final-pH substitute.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive1082api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\"\
    : \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"KOH amount\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"KOH receiving quantity\
    \ is unquantified; source gives two stock pH endpoints.\",\n    \"rationale\"\
    : \"No fixed dose or stock strength is supplied; correct the DSMZ owner root preparation\
    \ scope and recover missing target/KOMODO stock context.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1082api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1082\",\n        \"source_locator\"\
    : \"$.data.solutions[1].steps[0].step\",\n        \"exact_source_quote\": \"First\
    \ dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals.\
    \ Adjust final to pH 7.0 with KOH.\",\n        \"snapshot_sha256\": \"03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"Autoclave cycle\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIPHILUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/aminiphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except cysteine), then sparge medium for 30 - 45 min\
    \ with 100% N2 gas atmosphere to make it anoxic. Add cysteine, adjust pH to 7.1\
    \ and dispense medium under same gas atmosphere into anoxic Hungate-type tubes\
    \ or serum vials and autoclave.  The pH of the complete medium should be 7.0 -\
    \ 7.2.\",\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Autoclaving is specified, but no temperature or duration is given.\",\n  \
    \  \"rationale\": \"Do not add a default cycle or transfer one from DSM 141. Preserve\
    \ cysteine addition before pH adjustment and dispensing as stated in this exact\
    \ source.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive1082api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1082\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"and autoclave.\",\n        \"snapshot_sha256\": \"\
    03c7085275fe63af19cf06ed7d3a53401539b9b50b89d0b416df5b96b68a6203\"\n      }\n\
    \    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '22 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 22/24
    primary and 21/24 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131361
  - chebi131527
  - chebi26710
  - chebi31206
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi86158
  - chebi86345
  - chebi86364
  - chebi86465
  - chebi8806
  - chebi91244
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 24: primary 91.67%;
    secondary 87.50%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Source accession and maintained ownership
  outcome: supported
  summary: 'The generated CM003734 resolves to exact KOMODO 1082 owner CM003734 and
    DSMZ 1082 owner CM000517. Both recipe IDs and reciprocal SOURCE_DUPLICATE paths
    resolve in the inspected tree; the two ingredients arrays are exactly equal. Same
    accession/signature does not imply all fields are equal: DSMZ retains final ph_range
    and preparation omitted by target/KOMODO.'
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - owner-1
  - primary
  - provider
  - stock-crosscheck
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
  - CultureMech:003734
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - stock-crosscheck
  - komodo-catalog
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, source-only additions and owner differences
  outcome: concern
  summary: The target/KOMODO omit main preparation; DSMZ retains the exact main sequence
    and final pH range but places mineral-stock pH instructions at the main root.
    Recover the distinct main and mineral stages, water, dose and source strength.
    No source autoclave cycle is available; no default is invented.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - stock-crosscheck
  - komodo-catalog
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID are consistent with Trypticase peptone, yeast
    extract and absence of a gelling agent in this formulation. The generic application
    and source collection metadata do not establish growth, phenotype or a new taxonomic
    assignment.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - primary
  - provider
  - stock-crosscheck
  - komodo-catalog
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical specificity
  outcome: concern
  summary: Source nickel chloride is explicitly hexahydrate, whereas CHEBI:34887 has
    formula Cl2Ni. Source sodium resazurin is a sodium salt, whereas CHEBI:8806 has
    sodium-free formula C12H7NO4. All other asserted specific hydrate/form correspondences
    match the source at its stated specificity. Trypticase peptone and yeast extract
    remain mixtures without invented pure-compound IDs; retain source BD BBL qualifier.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - primary
  - provider
  - stock-crosscheck
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
  - CultureMech:003734
  evidence_ids:
  - record
  - primary
  - provider
  - stock-crosscheck
  - komodo-catalog
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 26 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: writer
  area: provenance
  topic: Authoritative inputs and current writer scope
  outcome: concern
  summary: Current MediaDive code separates first-stage ingredients and stock references
    and retains provider g_l values, but collects preparation steps from all solutions
    at the main root. Current DSMZ resolver copies ingredients/solutions but not preparation;
    current lossless merge requires scientific-field equality. Current cleanup flags
    disagreeing duplicate values rather than summing them. Current code is context,
    not proof of a particular historical execution. Correct every exact normalized
    contributor, attach claim-scoped evidence and append provenance clarification;
    regenerate derived products only after separately authorized correction.
  target_ids:
  - CultureMech:003734
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: culturemech.003734.main-stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Undiluted mineral-stock values are stored as main-medium concentrations
  description: All three layers flatten 15 mineral solutes into the main recipe. NaCl
    10.90099 and calcium chloride dihydrate 0.19900990000000002 additionally sum main
    g/L with undiluted-stock g/L. The primary explicitly calls for 10 mL of the separately
    described stock, not its full-strength composition. Nine unchanged main values
    match provider normalization but have no attached amount evidence; provider volume
    1010 mL is not asserted as a measured final volume.
  target_ids:
  - CultureMech:003734
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - stock-crosscheck
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
  issue_key: culturemech.003734.nickel-resazurin-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydration and sodium-resazurin identity do not match asserted forms
  description: The source and local preferred terms specify NiCl2 x 6H2O, but primary
    and secondary CHEBI:34887 correspond to anhydrous Cl2Ni. Sodium resazurin is mapped
    to CHEBI:8806, formula C12H7NO4 without sodium. Canonical labels and current secondary-key
    existence do not resolve either source-form mismatch.
  target_ids:
  - CultureMech:003734
  field_paths:
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  - ingredients[9].term
  evidence_ids:
  - record
  - primary
  - provider
  - chebi34887
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
  issue_key: culturemech.003734.main-and-stock-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and final pH are lost or assigned to the wrong stage
  description: Target/KOMODO lack preparation and retain only initial ph_value 7.1;
    the DSMZ owner has final ph_range 7.0–7.2 and main procedure, but its second root
    step is the mineral-stock procedure. Stock pH 6.5 then7.0 must remain separate
    from main final pH 7.0–7.2. The main cysteine timing and nitrogen context are
    source-specific.
  target_ids:
  - CultureMech:003734
  field_paths:
  - preparation_steps
  - ph_value
  - ph_range
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3.4
  normalization_reason: P3.4 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.003734.historical-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamp strings remain malformed or timezone-naive
  description: The target and KOMODO owner each retain one malformed import timestamp
    and one timezone-naive resolver timestamp. These do not validate source chronology
    and should not be silently rewritten.
  target_ids:
  - CultureMech:003734
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
  description: Repair both normalized contributors with distinct main additions and
    mineral-stock composition/dose; undo the two incompatible duplicate sums. Preserve
    main and stock water, exact chemical forms and source units; attach claim-level
    evidence. Document provider 1010 mL versus listed liquid 1010.5 mL without inventing
    a measured denominator. Regenerate only after authorized owner correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003734
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
  description: Verify exact supplied-form replacements before changing both normalized
    owners; preserve source masses and stock scope. Do not infer uninspected replacement
    IDs or convert using anhydrous/free-acid molecular weights.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003734
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
  description: Preserve DSMZ owner main procedure and ph_range, recover corresponding
    missing KOMODO context, and move/represent the mineral procedure at its stock
    scope. Retain initial versus final pH and unquantified KOH/cycle limits; do not
    overwrite final range with a midpoint or stock pH. Review current resolver/merge
    ownership before authorized regeneration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003734
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
  description: Preserve original history and append a clarification identifying the
    literal timestamp defects and known provenance limits when the owner is curated;
    do not fabricate historical times or source chronology.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003734
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/aminiphilus_medium.yaml
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
- The exact KOMODO 1082 detail request returned HTTP403. Exact catalog provenance
  and complete current DSMZ 1082 primary/provider formulations are available, so this
  optional historical-detail limitation does not prevent the current scientific comparison.
  Historical import execution and source chronology are not reconstructed.
- Only exact per-record bound captures are used. Current collection and provider differences
  do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently
  establish a measured final mixture volume. No density, percent basis, exact hydration,
  default sterilization cycle or stock volume is invented.
- 'Current scientific formulation comparison is completed: optional historical KOMODO
  detail is inaccessible, but exact catalog identity and primary/provider recipe and
  stock content are available. No required historical legacy-secondary correspondence
  is asserted in these layers.'
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-025
- generated-medium
```
