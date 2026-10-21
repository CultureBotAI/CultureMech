# Source and formulation review: alkaliphilic_thermococcus_medium (CultureMech:006844)

- Review: 20261021T131453Z-culturemech-006844-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:05:00Z
- Finished UTC: 2026-10-21T13:14:53Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 926 primary and provider expose flattened mineral stock amounts, four incompatible sums, omitted receiving branches and broken owner paths. The current 141/241 mineral stock differs from selected provider stock 5902 without established chronology. Scientific coverage is partial only because exact historical correspondence of the asserted legacy MediaIngredientMech:000232 remains unresolved; its absence from the complete current snapshot is a completed lookup, not proof of an incorrect historical KI mapping.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence. Required historical legacy-secondary correspondence remains unresolved; all current captured formulation and owner layers are assessed.

Selection: Task review 220; batch 022 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-one task batches contain 210 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 213 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006844 | data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml | generated | alkaliphilic_thermococcus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006844 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006844 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/220/strict.tsv |
| validate-terms | passed | True | CultureMech:006844 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006844 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006844 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo926detail | unavailable | False | CultureMech:006844 | Exact KOMODO 926 detail returned HTTP 403. This optional detail does not negate available primary/provider formulation support or itself make the review partial. |
| Exact current legacy-secondary lookup | passed | True | CultureMech:006844 | Complete current snapshot lookup finished and confirmed exact 000232 absence; this is a bounded negative result, not a failed lookup or a historical identity judgment. |
| Historical MediaIngredientMech:000232 to KI correspondence | unavailable | True | CultureMech:006844 | Required historical object or replacement correspondence is unavailable in the bound evidence. Current absence cannot validate or refute the old KI link; this unresolved historical check is the explicit reason for partial coverage. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006844.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006844.

44 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "NaCl basal contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "14.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "14.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "14.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 27.7 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "Four duplicate contributions must be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3; CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01. These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium source 0.05 mg is not 0.05 g.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 27.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 13.85,\n                        \"mmol_l\": 236.995,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "MgSO4 x 7 H2O basal contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 7 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "Four duplicate contributions must be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3; CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01. These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium source 0.05 mg is not 0.05 g.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 7,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.5,\n                        \"mmol_l\": 14.2002,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "MgCl2 x 6 H2O basal contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.75",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.75",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.75",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 5.5 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "The number matches the provider nominal 2000 mL normalization but has no attached amount evidence. Preserve original mass units and denominator scope rather than claiming measured final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 5.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.75,\n                        \"mmol_l\": 13.5266,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "KCl basal contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.325",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.325",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.325",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 0.65 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "The number matches the provider nominal 2000 mL normalization but has no attached amount evidence. Preserve original mass units and denominator scope rather than claiming measured final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.65,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.325,\n                        \"mmol_l\": 4.35949,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "NaBr basal contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 0.1 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "The number matches the provider nominal 2000 mL normalization but has no attached amount evidence. Preserve original mass units and denominator scope rather than claiming measured final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaBr\",\n                        \"compound_id\": 353,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.485956,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "NaHCO3 basal contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.16",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 0.32 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "The number matches the provider nominal 2000 mL normalization but has no attached amount evidence. Preserve original mass units and denominator scope rather than claiming measured final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.32,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.16,\n                        \"mmol_l\": 1.9046,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "K2HPO4 basal contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 1 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "The number matches the provider nominal 2000 mL normalization but has no attached amount evidence. Preserve original mass units and denominator scope rather than claiming measured final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.87066,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "CaCl2 x 2 H2O basal contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.100025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.100025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.100025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.05 mg in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "Four duplicate contributions must be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3; CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01. These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium source 0.05 mg is not 0.05 g.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"mg\",\n                        \"g_l\": 2.5e-5,\n                        \"mmol_l\": 0.000170051,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "KI basal contribution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0075",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0075",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.0075",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 15 mg in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "The number matches the provider nominal 2000 mL normalization but has no attached amount evidence. Preserve original mass units and denominator scope rather than claiming measured final-medium concentration.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"KI\",\n                        \"compound_id\": 354,\n                        \"amount\": 15,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0075,\n                        \"mmol_l\": 0.028919,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "H3BO3 basal contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Retain 0.03 g in the basal source recipe with 2000 mL listed water and a separate 20 mL stock dose.",
    "rationale": "Four duplicate contributions must be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3; CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01. These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium source 0.05 mg is not 0.05 g.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.015,\n                        \"mmol_l\": 0.242561,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Nitrilotriacetic acid mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 1.5 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "MgSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "6.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 3 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "MnSO4 x H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.5 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "NaCl mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "14.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "14.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "14.85",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 1 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "FeSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.1 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "CoSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.18 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "CaCl2 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.100025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.100025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.100025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.1 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "ZnSO4 x 7 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.18 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "CuSO4 x 5 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.01 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "AlK(SO4)2 x 12 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.02 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "H3BO3 mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.01 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Na2MoO4 x 2 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.01 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "NiCl2 x 6 H2O mineral stock",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.025 g in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. Current 141/241 instead specifies 0.03 g nickel hexahydrate; preserve the version conflict.",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.192903,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
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
        "source_locator": "Page 2, mineral subsection",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Na2SeO3 x 5 H2O mineral stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "Selected stock 5902 has 0.3 mg in its source 1000 mL-water recipe; retain a separate 20 mL basal receiving dose. ",
    "rationale": "The current local value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct stock scope before any volume calculation. The explicit nickel hexahydrate is not represented by anhydrous CHEBI:34887.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Current named mineral stock tungstate discrepancy",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Current 141/241 lists 0.40 mg tungstate dihydrate; selected 5902 has no corresponding row. Preserve the alternatives without unconditionally adding it to this medium.",
    "rationale": "The complete recipe comparison establishes a source-version difference, not historical chronology or equivalence.",
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
        "source_locator": "Page 2, mineral subsection",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8",
        "parsed_text_sha256": "734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Mineral receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "20 ml in its exact source stage.",
    "rationale": "Source water is a volume, not a solute g/L. Literal basal liquid inputs total 2020 mL before additional branch supplements, whereas provider declares 2000 mL; neither establishes the measured final receiving volume.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Modified Wolin's mineral solution II\",\n                        \"solution_id\": 5902,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Basal water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "2000 ml in its exact source stage.",
    "rationale": "Source water is a volume, not a solute g/L. Literal basal liquid inputs total 2020 mL before additional branch supplements, whereas provider declares 2000 mL; neither establishes the measured final receiving volume.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 2000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Mineral stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "1000 ml in its exact source stage.",
    "rationale": "Source water is a volume, not a solute g/L. Literal basal liquid inputs total 2020 mL before additional branch supplements, whereas provider declares 2000 mL; neither establishes the measured final receiving volume.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Casamino acids stock percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "10% source stock; percentage basis is unspecified, so do not assert W_V or an unsupported g/L conversion.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "Casamino acids(10%)",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Yeast extract stock percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "10% source stock; basis unspecified.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "Yeast extract (10%)",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Glycine stock molarity",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "2 M glycine stock as stated, separate from the receiving concentration.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "glycine (2M = 150 g/l)",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Glycine stock mass concentration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "150 g/L source stock, retaining the source paired statement with 2 M without recomputing or silently changing either.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "glycine (2M = 150 g/l)",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Polysulfide stock label",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.5 M polysulfide as the source stock label; chemical species basis and make-up volume are not independently established.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "A 0.5M polysulphide solution",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Polysulfide sulfide ingredient",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "12.0 g sodium sulfide nonahydrate in the separately prepared stock, not the basal medium.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "12.0 g Na2S x 9 H2O",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Polysulfide sulfur ingredient",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "1.6 g sulfur in the separate stock; no unsupported allotrope or replacement chemical identifier is inferred.",
    "rationale": "Target and KOMODO owner lack this stock procedure (add). DSMZ owner already retains the exact stock-specific prose in preparation_steps[1].description (evidence_only); preserve it and attach source evidence. No percentage basis or unlisted make-up volume is supplied.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "1.6 g sulphur",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Polysulfide stock make-up volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6 g sulphur - the solution will be dark yellow.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Oxygen-free water is named but its volume and final stock make-up are unquantified.",
    "rationale": "Do not derive a final stock volume from the nominal 0.5 M label or assume how polysulfide speciation is counted. Preserve the source ambiguity and existing DSMZ prose.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "in oxygen free water",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "DSM 10322 polysulfide receiving ratio",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "0.12 mL polysulfide per 10 mL medium, only in the DSM 10322 source branch.",
    "rationale": "These are distinct source formulation qualifiers, not growth assertions or unconditional additions. Retain receiving ratio versus final concentration and do not calculate a receiving volume or percent mass basis that the source does not establish.",
    "source_snippets": [
      {
        "source_key": "dsmz926",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf",
        "source_locator": "Page 1, explicitly named receiving branch",
        "exact_source_quote": "0.12 ml polysulphide/10 ml medium, yeast extract to a final concentration of 0.2% and \nglycine to a final concentration of 0.1 M for DSM 10322.",
        "snapshot_sha256": "574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102",
        "parsed_text_sha256": "e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "DSM 10322 yeast extract final percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Final yeast extract 0.2%, with unspecified percentage basis, only in the DSM 10322 branch.",
    "rationale": "These are distinct source formulation qualifiers, not growth assertions or unconditional additions. Retain receiving ratio versus final concentration and do not calculate a receiving volume or percent mass basis that the source does not establish.",
    "source_snippets": [
      {
        "source_key": "dsmz926",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf",
        "source_locator": "Page 1, explicitly named receiving branch",
        "exact_source_quote": "0.12 ml polysulphide/10 ml medium, yeast extract to a final concentration of 0.2% and \nglycine to a final concentration of 0.1 M for DSM 10322.",
        "snapshot_sha256": "574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102",
        "parsed_text_sha256": "e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "DSM 10322 glycine final molarity",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Final glycine 0.1 M only in the DSM 10322 branch.",
    "rationale": "These are distinct source formulation qualifiers, not growth assertions or unconditional additions. Retain receiving ratio versus final concentration and do not calculate a receiving volume or percent mass basis that the source does not establish.",
    "source_snippets": [
      {
        "source_key": "dsmz926",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf",
        "source_locator": "Page 1, explicitly named receiving branch",
        "exact_source_quote": "0.12 ml polysulphide/10 ml medium, yeast extract to a final concentration of 0.2% and \nglycine to a final concentration of 0.1 M for DSM 10322.",
        "snapshot_sha256": "574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102",
        "parsed_text_sha256": "e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "DSM 11906 polysulfide receiving ratio",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "0.08 mL polysulfide per 10 mL medium only in the DSM 11906 branch.",
    "rationale": "These are distinct source formulation qualifiers, not growth assertions or unconditional additions. Retain receiving ratio versus final concentration and do not calculate a receiving volume or percent mass basis that the source does not establish.",
    "source_snippets": [
      {
        "source_key": "dsmz926",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf",
        "source_locator": "Page 1, explicitly named receiving branch",
        "exact_source_quote": "0.08 ml polysulphide/10 ml medium, casamino acids to a final concentration of 0.2% for \nDSM 11906.",
        "snapshot_sha256": "574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102",
        "parsed_text_sha256": "e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "DSM 11906 Casamino acids final percentage",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Final Casamino acids 0.2%, basis unspecified, only in the DSM 11906 branch.",
    "rationale": "These are distinct source formulation qualifiers, not growth assertions or unconditional additions. Retain receiving ratio versus final concentration and do not calculate a receiving volume or percent mass basis that the source does not establish.",
    "source_snippets": [
      {
        "source_key": "dsmz926",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf",
        "source_locator": "Page 1, explicitly named receiving branch",
        "exact_source_quote": "0.08 ml polysulphide/10 ml medium, casamino acids to a final concentration of 0.2% for \nDSM 11906.",
        "snapshot_sha256": "574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102",
        "parsed_text_sha256": "e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "Mineral initial pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "First dissolve NTA and adjust the stock to pH 6.5 with KOH, then add minerals.",
    "rationale": "Target/KOMODO omit the procedure. DSMZ owner places mineral-stock adjustment at main preparation_steps[2], so correct its scope rather than validating a main-medium adjustment. The primary main instruction is do not adjust pH.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "Mineral final pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "After the other minerals, adjust the stock to pH 7.0 with KOH.",
    "rationale": "Target/KOMODO omit the procedure. DSMZ owner places mineral-stock adjustment at main preparation_steps[2], so correct its scope rather than validating a main-medium adjustment. The primary main instruction is do not adjust pH.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Mineral KOH quantity",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "KOH quantity and strength are unspecified; preserve the two stock endpoints without an invented dose.",
    "rationale": "Only the stock pH sequence is quantified. Restore stock scope in the DSMZ owner and preserve main do-not-adjust-pH separately.",
    "source_snippets": [
      {
        "source_key": "mediadive926api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/926",
        "source_locator": "$.data.solutions[1].steps[0].step",
        "exact_source_quote": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "snapshot_sha256": "071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:006844.

20 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 20/20 primary and 19/20 secondary instances; all asserted current CHEBI-based secondary keys have exact pinned MIM rows. The separately asserted legacy MediaIngredientMech:000232 remains historically unresolved; current exact lookup is complete and negative, not historical identity validation. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 20: primary 100.00%; secondary 95.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source accession and maintained ownership

identity: concern. Targets: CultureMech:006844.

CM006844 resolves to the exact KOMODO 926 owner and DSMZ contributor CM002098 under archaea. Both accessions map to DSMZ 926, but all three bacterial-folder relationship paths are dangling. Ingredient signature equivalence does not establish matching preparation or complete receiving branches.

### Claim-level amount support and source scope

evidence: concern. Targets: CultureMech:006844.

The local layers have import provenance but no attached amount evidence. The inventory covers every local concentration and scoped source-only quantity using literal excerpts, exact source locators, units, stages and original capture hashes. Provider-declared volume is kept separate from measured assembled final volume.

### Preparation stages, source-only additions and owner differences

completeness: concern. Targets: CultureMech:006844.

DSMZ owner retains main preparation under nitrogen/do not adjust pH and separate stock-strength prose. Target/KOMODO omit them. All layers omit the two primary receiving branches. DSMZ preparation_steps[2] is mineral-stock pH adjustment mislocated at the main level; restore its stock scope so it does not contradict the basal instruction. Preserve unspecified percentage bases and missing polysulfide make-up volume; do not transfer unrelated parent 141 instructions.

### Composition and physical-state classification

scope: concern. Targets: CultureMech:006844.

DEFINED/DEFINED may describe a deliberately bounded mineral basal stage, but not the complete source branches adding yeast extract or Casamino acids. Clarify basal versus receiving variants before assigning composition to each representation. LIQUID is supported by absence of a mandatory gelling agent. No growth or phenotype is inferred from the title.

### Supplied forms and chemical specificity

grounding: concern. Targets: CultureMech:006844.

All explicit hydrated salts were compared with canonical OLS forms. Source nickel hexahydrate conflicts with anhydrous CHEBI:34887 in both primary and secondary local slots. KI primary CHEBI:8346 is valid independently of unresolved legacy 000232. Sulfur source wording alone does not justify a specific allotrope or a wrong-ID assertion.

### Growth, organism taxonomy and graph claims

scope: not_applicable. Targets: CultureMech:006844.

The title, generic Microbial cultivation application and catalog Aerobic flags are not experimental growth or taxonomy evidence. No growth assertions, current taxonomy IDs or graph membership are added. Explicit source strain qualifiers remain formulation scope only.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006844.

25 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Authoritative inputs and current writer scope

provenance: concern. Targets: CultureMech:006844.

Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction.

## Findings

### f1: Stock flattening creates four incompatible basal sums

blocker / open / confirmed; issue key: flattened-mineral-stock.

The target and both owners treat undiluted mineral stock composition as direct medium concentrations. NaCl, magnesium sulfate, calcium chloride and boric acid additionally combine incompatible main and stock g/L values. Source 20 mL receiving dose and separate water stages are absent. Calcium is literally 0.05 mg in the 2000 mL-water basal source.

### f2: Three relationship paths point to absent bacterial files

blocker / open / confirmed; issue key: broken-owner-relationships.

Target and KOMODO owner parent_media.path reference bacterial/alkaliphilic_thermococcus_medium.yaml; DSMZ owner variant_children[0].path references bacterial/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml. Ignored-inclusive search confirms these paths are absent; exact stable-ID owners exist in archaea.

### f3: Current named mineral stock differs from provider-selected stock

major / open / confirmed; issue key: mineral-source-version-conflict.

Selected stock 5902 has nickel hexahydrate 0.025 g and no tungstate; current referenced 141/241 has 0.03 g nickel hexahydrate and 0.40 mg tungstate. The available evidence does not establish the historical choice or temporal order.

### f4: Nickel hexahydrate is grounded to anhydrous nickel dichloride

major / open / confirmed; issue key: nickel-hydrate-grounding.

ingredients[18] explicitly names NiCl2 x 6 H2O, but primary and CHEBI-based secondary slots assert CHEBI:34887 with formula Cl2Ni. Both candidate source stocks specify hexahydrate.

### f5: Missing receiving branches and misplaced stock procedure obscure source scope

major / open / confirmed; issue key: missing-source-branches-and-stage-scope.

Both maintained contributors omit the distinct primary receiving branches, while only DSMZ retains stock preparation. Mineral pH instructions remain at its main root despite the source main do-not-adjust-pH instruction. Uniform DEFINED classification does not describe branches with complex supplements unless the record is explicitly restricted to basal medium.

### f6: Historical legacy KI correspondence remains unverified

minor / open / confirmed; issue key: legacy-secondary-history-unresolved.

All layers assert MediaIngredientMech:000232 for KI. The complete current index/catalog/tree lack that exact legacy key; this establishes a present snapshot gap, not a historically wrong KI identity. Required historical correspondence remains unavailable.

### f7: Historical timestamp strings remain malformed or timezone-naive

minor / open / confirmed; issue key: historical-timestamp-shape.

The target and KOMODO owner each retain one malformed import timestamp and one timezone-naive resolver timestamp. These do not validate source chronology and should not be silently rewritten.

## Recommended Actions And Acceptance Checks

### a1

Correct both exact normalized contributors: separate basal and mineral-stock quantities, restore dose and water volumes, undo all four incompatible sums, and attach source-stage evidence. Preserve source mg calcium and avoid double counting. Establish a final-volume basis before final-medium conversions or regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct the two maintained relationship directions to exact archaea owner paths while preserving stable IDs and separately checking SOURCE_DUPLICATE semantics. Regenerate the target path after owner repair. Append clarification without rewriting historical relocation events.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve both exact stock alternatives and obtain source-version evidence before choosing a canonical replacement. Do not silently import current 141 stock composition or unrelated parent-medium instructions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Re-ground the exact supplied hexahydrate in both maintained contributors only after validating the specific ontology and secondary correspondence. Preserve amount/version uncertainty independently; no unverified replacement ID is supplied.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve DSMZ stock prose, recover exact missing procedures in KOMODO, restore mineral pH instructions to the stock, and represent the two source-qualified receiving branches separately. Keep unqualified percentages and unknown polysulfide make-up volume explicit; distinguish basal/variant classification and add no new growth assertion or taxonomy ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Recover exact historical legacy object or explicit replacement evidence before changing this secondary link. Preserve the valid primary KI identifier and document the current lookup result separately from unresolved history; do not use fuzzy name substitution.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a7

Preserve original history and append a clarification identifying the literal timestamp defects and known provenance limits when the owner is curated; do not fabricate historical times or source chronology.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch022/220/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/220/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml:1:id: CultureMech:006844<br>./data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml:1:id: CultureMech:006844<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/220/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 29 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/220/evidence-context-original.json; Complete frozen target/owners, source stages, exact secondary lookup and ignored-inclusive relationships | context_only | Full captured records re-read and compared by exact equality with fresh inspected records. Context is supporting provenance; exact bound primary/provider captures independently support scientific claims. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf; Page 1: basal table, separate stocks and two explicitly strain-qualified receiving branches | supports | The source lists 2000 mL water and 20 mL mineral stock. Calcium chloride dihydrate is literally 0.05 mg. Two separate receiving branches specify different polysulfide ratios and complex supplements; no unconditional merged branch or growth assertion is inferred. |
| provider | https://mediadive.dsmz.de/rest/medium/926; data.medium; main 1907 and stock 5902 recipes/steps | supports | Provider declares 2000 mL main volume and retains basal/stock stages, but its main steps omit the primary receiving branches. This response does not justify merging undiluted stock concentrations into main amounts. |
| referenced-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Page 2: Modified Wolin mineral subsection ONLY | supports | Only the explicitly referenced mineral subsection is compared. Current 141/241 lists 0.03 g nickel hexahydrate and 0.40 mg tungstate; selected 5902 lists 0.025 g nickel hexahydrate and no tungstate row. No parent-medium, vitamin, gas, pressure or growth context transfers. |
| solution241 | https://mediadive.dsmz.de/rest/solution/241; data.id/name/volume/recipe/steps | supports | Exact stock endpoint identity and complete quantities retained. Current named stock 241 and selected mineral II stock 5902 remain distinct source versions without inferred temporal order. |
| solution5902 | https://mediadive.dsmz.de/rest/solution/5902; data.id/name/volume/recipe/steps | supports | Exact stock endpoint identity and complete quantities retained. Current named stock 241 and selected mineral II stock 5902 remain distinct source versions without inferred temporal order. |
| komodo-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact table row 926 | supports | Exact KOMODO accession maps to DSMZ 926. Catalog Aerobic flags supply provenance, not experimental growth evidence. |
| komodo926detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=926; Preserved exact public retrieval result | context_only | Exact KOMODO 926 detail returned HTTP 403. This optional detail does not negate available primary/provider formulation support or itself make the review partial. |
| mimPinnedCatalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete exact pinned snapshot, source commit 6643131b0f12ab40b66f98135245fca04027e0e9 | supports | The full current snapshot contains no exact legacy 000232 identifier or object path. This completed negative lookup cannot establish the content of an unavailable historical object. |
| mimPinnedTree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete exact pinned snapshot, source commit 6643131b0f12ab40b66f98135245fca04027e0e9 | supports | The full current snapshot contains no exact legacy 000232 identifier or object path. This completed negative lookup cannot establish the content of an unavailable historical object. |
| legacy-lookup | src/culturemech/data/mediaingredientmech/label_index.csv; All 9077 index rows, 2953 full catalog objects and 7384 nontruncated tree entries | context_only | Exact 000232 absence rechecked across all complete pinned structures. The local KI primary CHEBI:8346 is independently available. Historical legacy correspondence is not recovered by the present snapshot. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch022/220/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63004 resolves to sodium bromide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8346 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8346; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8346 resolves to potassium iodide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63004": [{"label": "NaBr", "match_type": "preferred_term", "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| relationship-lookup | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/220/evidence-context-original.json; Three parent/child path assertions and full ignored-inclusive normalized file enumeration | refutes | The target and KOMODO parent paths and DSMZ variant_children[0] path point to absent bacterial paths. Exact same-basename, stable-ID contributors exist in archaea; their byte hashes match inspected owners. |
| history-metadata | data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml; data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml; data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.931490"}]}, {"input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:58.931490"}]}, {"input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-1 | src/culturemech/enrich/dsmz_resolver.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current MediaDive code distinguishes stock additions and solutions, preserves preparation steps and uses provider stage volumes for normalization. DSMZ resolver/merge ownership and current cleanup were inspected; current cleanup does not reproduce the historical disagreeing-duplicate sums. Current code is context, not proof of a particular historical execution. Correct every exact normalized contributor, attach claim-scoped evidence and append provenance clarification; regenerate derived products only after separately authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact KOMODO 926 detail returned HTTP 403. This optional detail does not negate available primary/provider formulation support or itself make the review partial.
- Historical MediaIngredientMech:000232 correspondence remains unresolved. Current exact absence is a completed lookup; no replacement, chemical error or historical deletion is inferred from it.
- Only exact per-record bound captures are used. Current collection and provider differences do not establish their temporal order or the historical imported formulation.
- Source stock concentrations, receiving doses and listed water amounts do not independently establish a measured final mixture volume. No density, percent basis, exact hydration, default sterilization cycle or stock volume is invented.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131453Z-culturemech-006844-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilic_thermococcus_medium (CultureMech:006844)'
started_at: '2026-10-21T13:05:00Z'
finished_at: '2026-10-21T13:14:53Z'
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
summary: The exact DSMZ 926 primary and provider expose flattened mineral stock amounts,
  four incompatible sums, omitted receiving branches and broken owner paths. The current
  141/241 mineral stock differs from selected provider stock 5902 without established
  chronology. Scientific coverage is partial only because exact historical correspondence
  of the asserted legacy MediaIngredientMech:000232 remains unresolved; its absence
  from the complete current snapshot is a completed lookup, not proof of an incorrect
  historical KI mapping.
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
  - path: data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
    sha256: 6f33a2bf8262e9d45dc80d313b5ebc80b4a89770b1fff8e4ca42c2121f9e1c88
    role: target
  - path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    sha256: 88891a5ab467a909f5ad2db627208bb3275bee259ad17cfa4ec8bd6d066a1644
    role: context
  - path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
    sha256: fe1d46d884ae5f643dbb8fb2e79a1357c985282e832fde31ce3df3a0b1904bcf
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
    provenance, and maintained-input correspondence. Required historical legacy-secondary
    correspondence remains unresolved; all current captured formulation and owner
    layers are assessed.
  selection: Task review 220; batch 022 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-one task batches
    contain 210 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 213 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006844
targets:
- target_id: CultureMech:006844
  path: data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  label: alkaliphilic_thermococcus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/220/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/220/strict.tsv"
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006844
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
  - CultureMech:006844
- check_id: komodo926detail-source-access
  name: 'Exact source content access: komodo926detail'
  required: false
  status: unavailable
  summary: Exact KOMODO 926 detail returned HTTP 403. This optional detail does not
    negate available primary/provider formulation support or itself make the review
    partial.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - komodo926detail-attempt
- check_id: current-legacy-negative-lookup
  name: Exact current legacy-secondary lookup
  required: true
  status: passed
  summary: Complete current snapshot lookup finished and confirmed exact 000232 absence;
    this is a bounded negative result, not a failed lookup or a historical identity
    judgment.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - legacy-lookup
  - mimPinnedCatalog
  - mimPinnedTree
- check_id: historical-legacy-correspondence
  name: Historical MediaIngredientMech:000232 to KI correspondence
  required: true
  status: unavailable
  summary: Required historical object or replacement correspondence is unavailable
    in the bound evidence. Current absence cannot validate or refute the old KI link;
    this unresolved historical check is the explicit reason for partial coverage.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - legacy-lookup
  - mimPinnedCatalog
  - mimPinnedTree
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:36.917996Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/220/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:38.258647Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/220/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:39.877009Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:40.878043Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:14:51Z'
  support: supports
  summary: './data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml:1:id:
    CultureMech:006844

    ./data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml:1:id: CultureMech:006844

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/220/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:14:51Z'
  support: supports
  summary: 29 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: d4b2161b2260d5ca5de06aa020637537e763c342be05a5d78e5524df41533567
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/220/evidence-context-original.json
  locator: Complete frozen target/owners, source stages, exact secondary lookup and
    ignored-inclusive relationships
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: Full captured records re-read and compared by exact equality with fresh
    inspected records. Context is supporting provenance; exact bound primary/provider
    captures independently support scientific claims.
  snapshot_sha256: 99eeb9247317bab54e7642544d9ae47953369b9aaa4ed218ab314b9098b67f3c
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf
  locator: 'Page 1: basal table, separate stocks and two explicitly strain-qualified
    receiving branches'
  accessed_at: '2026-10-21T12:48:26.643390Z'
  support: supports
  summary: The source lists 2000 mL water and 20 mL mineral stock. Calcium chloride
    dihydrate is literally 0.05 mg. Two separate receiving branches specify different
    polysulfide ratios and complex supplements; no unconditional merged branch or
    growth assertion is inferred.
  snapshot_sha256: 574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/926
  locator: data.medium; main 1907 and stock 5902 recipes/steps
  accessed_at: '2026-10-21T12:48:25.161331Z'
  support: supports
  summary: Provider declares 2000 mL main volume and retains basal/stock stages, but
    its main steps omit the primary receiving branches. This response does not justify
    merging undiluted stock concentrations into main amounts.
  snapshot_sha256: 071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052
- evidence_id: referenced-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: 'Page 2: Modified Wolin mineral subsection ONLY'
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: Only the explicitly referenced mineral subsection is compared. Current
    141/241 lists 0.03 g nickel hexahydrate and 0.40 mg tungstate; selected 5902 lists
    0.025 g nickel hexahydrate and no tungstate row. No parent-medium, vitamin, gas,
    pressure or growth context transfers.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: solution241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T10:37:16.846684Z'
  support: supports
  summary: Exact stock endpoint identity and complete quantities retained. Current
    named stock 241 and selected mineral II stock 5902 remain distinct source versions
    without inferred temporal order.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: solution5902
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5902
  locator: data.id/name/volume/recipe/steps
  accessed_at: '2026-10-21T12:49:29.674664Z'
  support: supports
  summary: Exact stock endpoint identity and complete quantities retained. Current
    named stock 241 and selected mineral II stock 5902 remain distinct source versions
    without inferred temporal order.
  snapshot_sha256: 6dad1881991322b2ffaa009e69a224698f3b1a939b605c633bbbbefb63544270
- evidence_id: komodo-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact table row 926
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Exact KOMODO accession maps to DSMZ 926. Catalog Aerobic flags supply provenance,
    not experimental growth evidence.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo926detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=926
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:48:24.885539Z'
  support: context_only
  summary: Exact KOMODO 926 detail returned HTTP 403. This optional detail does not
    negate available primary/provider formulation support or itself make the review
    partial.
  snapshot_sha256: 15f4bf528a747ec490e84b482d973f5879bd32c927330343d1f17e429362b692
- evidence_id: mimPinnedCatalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete exact pinned snapshot, source commit 6643131b0f12ab40b66f98135245fca04027e0e9
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: The full current snapshot contains no exact legacy 000232 identifier or
    object path. This completed negative lookup cannot establish the content of an
    unavailable historical object.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mimPinnedTree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete exact pinned snapshot, source commit 6643131b0f12ab40b66f98135245fca04027e0e9
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: The full current snapshot contains no exact legacy 000232 identifier or
    object path. This completed negative lookup cannot establish the content of an
    unavailable historical object.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-lookup
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All 9077 index rows, 2953 full catalog objects and 7384 nontruncated tree
    entries
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: Exact 000232 absence rechecked across all complete pinned structures. The
    local KI primary CHEBI:8346 is independently available. Historical legacy correspondence
    is not recovered by the present snapshot.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
  search_scope: Complete pinned label index, full ingredient catalog and nontruncated
    tree; no ignored-file-dependent search or fuzzy label substitution.
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/220/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7ea19d683f8c7e0b7b2c01e11340b02126973985b00557d9bd204eb960433653
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
- evidence_id: chebi8346
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8346
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:26:30.240205Z'
  support: supports
  summary: CHEBI:8346 resolves to potassium iodide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 261d4862f5ae3627f515eefe14ca4f27cfed8c87604dbf8b8206b81af884631d
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
  accessed_at: '2026-10-21T13:14:51Z'
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
    "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O",
    "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier":
    "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status":
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
    "unique"}], "CHEBI:63004": [{"label": "NaBr", "match_type": "preferred_term",
    "identifier": "CHEBI:63004", "preferred_term": "NaBr", "ontology_id": "CHEBI:63004",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
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
- evidence_id: relationship-lookup
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/220/evidence-context-original.json
  locator: Three parent/child path assertions and full ignored-inclusive normalized
    file enumeration
  accessed_at: '2026-10-21T13:14:51Z'
  support: refutes
  summary: The target and KOMODO parent paths and DSMZ variant_children[0] path point
    to absent bacterial paths. Exact same-basename, stable-ID contributors exist in
    archaea; their byte hashes match inspected owners.
  snapshot_sha256: 99eeb9247317bab54e7642544d9ae47953369b9aaa4ed218ab314b9098b67f3c
  search_scope: Path.rglob over every normalized file includes ignored and hidden
    files; exact paths, basenames, stable IDs and owner hashes compared.
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml; data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml;
    data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:14:51Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:58.931490"}]}, {"input": "data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:58.931490"}]}, {"input": "data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:14:51Z'
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
  accessed_at: '2026-10-21T13:14:51Z'
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
  accessed_at: '2026-10-21T13:14:51Z'
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
  accessed_at: '2026-10-21T13:14:51Z'
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
  - CultureMech:006844
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 44 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    NaCl basal contribution\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.85\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.85\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"14.85\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 27.7 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"Four duplicate contributions must\
    \ be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3;\
    \ CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01.\
    \ These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium\
    \ source 0.05 mg is not 0.05 g.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"NaCl\\\",\\n                  \
    \      \\\"compound_id\\\": 43,\\n                        \\\"amount\\\": 27.7,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 13.85,\\n                        \\\"mmol_l\\\": 236.995,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"MgSO4 x 7 H2O basal contribution\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 7 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"Four duplicate contributions must\
    \ be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3;\
    \ CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01.\
    \ These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium\
    \ source 0.05 mg is not 0.05 g.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 8,\\n                        \\\"amount\\\
    \": 7,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 3.5,\\n                        \\\"mmol_l\\\": 14.2002,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"MgCl2 x 6 H2O basal contribution\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.75\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.75\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"2.75\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 5.5 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ 2000 mL normalization but has no attached amount evidence. Preserve original\
    \ mass units and denominator scope rather than claiming measured final-medium\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 79,\\n                        \\\"amount\\\
    \": 5.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 2.75,\\n                        \\\"mmol_l\\\": 13.5266,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"KCl basal contribution\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.325\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.325\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.325\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.65 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ 2000 mL normalization but has no attached amount evidence. Preserve original\
    \ mass units and denominator scope rather than claiming measured final-medium\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"KCl\\\",\\n                   \
    \     \\\"compound_id\\\": 61,\\n                        \\\"amount\\\": 0.65,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.325,\\n                        \\\"mmol_l\\\": 4.35949,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"NaBr basal contribution\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.1 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ 2000 mL normalization but has no attached amount evidence. Preserve original\
    \ mass units and denominator scope rather than claiming measured final-medium\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"NaBr\\\",\\n                  \
    \      \\\"compound_id\\\": 353,\\n                        \\\"amount\\\": 0.1,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.485956,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"NaHCO3 basal contribution\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.16\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.32 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ 2000 mL normalization but has no attached amount evidence. Preserve original\
    \ mass units and denominator scope rather than claiming measured final-medium\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"NaHCO3\\\",\\n                \
    \        \\\"compound_id\\\": 55,\\n                        \\\"amount\\\": 0.32,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.16,\\n                        \\\"mmol_l\\\": 1.9046,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"K2HPO4 basal contribution\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 1 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ 2000 mL normalization but has no attached amount evidence. Preserve original\
    \ mass units and denominator scope rather than claiming measured final-medium\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"K2HPO4\\\",\\n                \
    \        \\\"compound_id\\\": 10,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.5,\\n                        \\\"mmol_l\\\": 2.87066,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O basal contribution\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.100025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.100025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.100025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.05 mg in the basal source recipe with 2000 mL listed water and a\
    \ separate 20 mL stock dose.\",\n    \"rationale\": \"Four duplicate contributions\
    \ must be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5\
    \ + 3; CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01.\
    \ These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium\
    \ source 0.05 mg is not 0.05 g.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 7,\\n                        \\\"amount\\\
    \": 0.05,\\n                        \\\"unit\\\": \\\"mg\\\",\\n             \
    \           \\\"g_l\\\": 2.5e-5,\\n                        \\\"mmol_l\\\": 0.000170051,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"KI basal contribution\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0075\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0075\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0075\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 15 mg in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"The number matches the provider nominal\
    \ 2000 mL normalization but has no attached amount evidence. Preserve original\
    \ mass units and denominator scope rather than claiming measured final-medium\
    \ concentration.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"KI\\\",\\n                    \
    \    \\\"compound_id\\\": 354,\\n                        \\\"amount\\\": 15,\\\
    n                        \\\"unit\\\": \\\"mg\\\",\\n                        \\\
    \"g_l\\\": 0.0075,\\n                        \\\"mmol_l\\\": 0.028919,\\n    \
    \                    \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"H3BO3 basal contribution\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[9].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Retain 0.03 g in the basal source recipe with 2000 mL listed water and a separate\
    \ 20 mL stock dose.\",\n    \"rationale\": \"Four duplicate contributions must\
    \ be separated: local NaCl 14.85 = 13.85 + 1; MgSO4 heptahydrate 6.5 = 3.5 + 3;\
    \ CaCl2 dihydrate 0.100025 = 0.000025 + 0.1; boric acid 0.025 = 0.015 + 0.01.\
    \ These combine provider main-stage g/L with undiluted stock-stage g/L. Calcium\
    \ source 0.05 mg is not 0.05 g.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"H3BO3\\\",\\n                 \
    \       \\\"compound_id\\\": 37,\\n                        \\\"amount\\\": 0.03,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.015,\\n                        \\\"mmol_l\\\": 0.242561,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Nitrilotriacetic acid mineral stock\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 1.5 g in its source 1000 mL-water recipe; retain a\
    \ separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current local\
    \ value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct\
    \ stock scope before any volume calculation. The explicit nickel hexahydrate is\
    \ not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                        \\\"compound_id\\\
    \": 189,\\n                        \\\"amount\\\": 1.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n\
    \                        \\\"mmol_l\\\": 7.84765,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"MgSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 3 g in its source 1000 mL-water recipe; retain a separate\
    \ 20 mL basal receiving dose. \",\n    \"rationale\": \"The current local value\
    \ is an undiluted stock amount or an incompatible main-plus-stock sum. Correct\
    \ stock scope before any volume calculation. The explicit nickel hexahydrate is\
    \ not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 3,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n      \
    \                  \\\"mmol_l\\\": 12.1716,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"MnSO4 x H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.5 g in its source 1000 mL-water recipe; retain a\
    \ separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current local\
    \ value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct\
    \ stock scope before any volume calculation. The explicit nickel hexahydrate is\
    \ not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 2.9583,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"NaCl mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.85\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"14.85\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[0].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"14.85\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 1 g in its source 1000 mL-water recipe; retain a separate\
    \ 20 mL basal receiving dose. \",\n    \"rationale\": \"The current local value\
    \ is an undiluted stock amount or an incompatible main-plus-stock sum. Correct\
    \ stock scope before any volume calculation. The explicit nickel hexahydrate is\
    \ not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"FeSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.1 g in its source 1000 mL-water recipe; retain a\
    \ separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current local\
    \ value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct\
    \ stock scope before any volume calculation. The explicit nickel hexahydrate is\
    \ not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.359693,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"CoSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.18 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 198,\\n                        \\\"amount\\\": 0.18,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 1.16132,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.100025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.100025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[7].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.100025\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.1 g in its source 1000 mL-water recipe; retain a\
    \ separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current local\
    \ value is an undiluted stock amount or an incompatible main-plus-stock sum. Correct\
    \ stock scope before any volume calculation. The explicit nickel hexahydrate is\
    \ not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.680203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"ZnSO4 x 7 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.18 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.18,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.18,\\\
    n                        \\\"mmol_l\\\": 0.625954,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"CuSO4 x 5 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.01 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 0.01,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0400503,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"AlK(SO4)2 x 12 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.02 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0421596,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"H3BO3 mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[9].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.01 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\":\
    \ 37,\\n                        \\\"amount\\\": 0.01,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\n \
    \                       \\\"mmol_l\\\": 0.161708,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Na2MoO4 x 2 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.01 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.01,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0413309,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"NiCl2 x 6 H2O mineral stock\",\n    \"decision\": \"conflict\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.025 g in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. Current 141/241 instead specifies 0.03\
    \ g nickel hexahydrate; preserve the version conflict.\",\n    \"rationale\":\
    \ \"The current local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 0.025,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.025,\\\
    n                        \\\"mmol_l\\\": 0.192903,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      },\n\
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
    source_locator\": \"Page 2, mineral subsection\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 0.03 g\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Na2SeO3 x 5 H2O mineral stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Selected stock 5902 has 0.3 mg in its source 1000 mL-water recipe; retain\
    \ a separate 20 mL basal receiving dose. \",\n    \"rationale\": \"The current\
    \ local value is an undiluted stock amount or an incompatible main-plus-stock\
    \ sum. Correct stock scope before any volume calculation. The explicit nickel\
    \ hexahydrate is not represented by anhydrous CHEBI:34887.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 107,\\n                        \\\"amount\\\": 0.3,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0003,\\\
    n                        \\\"mmol_l\\\": 0.00114062,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Current named mineral stock tungstate discrepancy\",\n    \"decision\": \"\
    conflict\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Current 141/241 lists 0.40 mg tungstate dihydrate; selected 5902 has no corresponding\
    \ row. Preserve the alternatives without unconditionally adding it to this medium.\"\
    ,\n    \"rationale\": \"The complete recipe comparison establishes a source-version\
    \ difference, not historical chronology or equivalence.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"solution241\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/solution/241\",\n        \"source_locator\"\
    : \"$.data.recipe[14]\",\n        \"exact_source_quote\": \"{\\n             \
    \   \\\"recipe_order\\\": 15,\\n                \\\"compound\\\": \\\"Na2WO4 x\
    \ 2 H2O\\\",\\n                \\\"compound_id\\\": 249,\\n                \\\"\
    solution\\\": null,\\n                \\\"solution_id\\\": null,\\n          \
    \      \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\n\
    \                \\\"amount\\\": 0.4,\\n                \\\"unit\\\": \\\"mg\\\
    \",\\n                \\\"g_l\\\": 0.0004,\\n                \\\"mmol_l\\\": 0.00121267,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz141\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf\",\n        \"\
    source_locator\": \"Page 2, mineral subsection\",\n        \"exact_source_quote\"\
    : \"Na2WO4 x 2 H2O 0.40 mg\",\n        \"snapshot_sha256\": \"8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8\"\
    ,\n        \"parsed_text_sha256\": \"734e01731efdb11616ac424a3b12c8fa2f0f6a7d90424a38f8cb979d63fc44c5\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Mineral receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"20 ml in its exact source stage.\",\n    \"rationale\": \"Source water is\
    \ a volume, not a solute g/L. Literal basal liquid inputs total 2020 mL before\
    \ additional branch supplements, whereas provider declares 2000 mL; neither establishes\
    \ the measured final receiving volume.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"solution\\\": \\\"Modified Wolin's mineral solution\
    \ II\\\",\\n                        \\\"solution_id\\\": 5902,\\n            \
    \            \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Basal water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"2000 ml in its exact source stage.\",\n    \"rationale\": \"Source water is\
    \ a volume, not a solute g/L. Literal basal liquid inputs total 2020 mL before\
    \ additional branch supplements, whereas provider declares 2000 mL; neither establishes\
    \ the measured final receiving volume.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[11]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 12,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 2000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Mineral stock water\",\n    \"decision\": \"add\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1000 ml in its exact source stage.\",\n    \"rationale\": \"Source water is\
    \ a volume, not a solute g/L. Literal basal liquid inputs total 2020 mL before\
    \ additional branch supplements, whereas provider declares 2000 mL; neither establishes\
    \ the measured final receiving volume.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[14]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 16,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Casamino acids stock percentage\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"10% source stock;\
    \ percentage basis is unspecified, so do not assert W_V or an unsupported g/L\
    \ conversion.\",\n    \"rationale\": \"Target and KOMODO owner lack this stock\
    \ procedure (add). DSMZ owner already retains the exact stock-specific prose in\
    \ preparation_steps[1].description (evidence_only); preserve it and attach source\
    \ evidence. No percentage basis or unlisted make-up volume is supplied.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n        \"\
    exact_source_quote\": \"Casamino acids(10%)\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Yeast extract stock percentage\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"10% source stock;\
    \ basis unspecified.\",\n    \"rationale\": \"Target and KOMODO owner lack this\
    \ stock procedure (add). DSMZ owner already retains the exact stock-specific prose\
    \ in preparation_steps[1].description (evidence_only); preserve it and attach\
    \ source evidence. No percentage basis or unlisted make-up volume is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n        \"\
    exact_source_quote\": \"Yeast extract (10%)\",\n        \"snapshot_sha256\": \"\
    071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n      }\n\
    \    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Glycine stock molarity\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"2 M glycine stock\
    \ as stated, separate from the receiving concentration.\",\n    \"rationale\"\
    : \"Target and KOMODO owner lack this stock procedure (add). DSMZ owner already\
    \ retains the exact stock-specific prose in preparation_steps[1].description (evidence_only);\
    \ preserve it and attach source evidence. No percentage basis or unlisted make-up\
    \ volume is supplied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n      \
    \  \"exact_source_quote\": \"glycine (2M = 150 g/l)\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Glycine stock mass concentration\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"150 g/L source stock,\
    \ retaining the source paired statement with 2 M without recomputing or silently\
    \ changing either.\",\n    \"rationale\": \"Target and KOMODO owner lack this\
    \ stock procedure (add). DSMZ owner already retains the exact stock-specific prose\
    \ in preparation_steps[1].description (evidence_only); preserve it and attach\
    \ source evidence. No percentage basis or unlisted make-up volume is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n        \"\
    exact_source_quote\": \"glycine (2M = 150 g/l)\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Polysulfide stock label\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"0.5 M polysulfide\
    \ as the source stock label; chemical species basis and make-up volume are not\
    \ independently established.\",\n    \"rationale\": \"Target and KOMODO owner\
    \ lack this stock procedure (add). DSMZ owner already retains the exact stock-specific\
    \ prose in preparation_steps[1].description (evidence_only); preserve it and attach\
    \ source evidence. No percentage basis or unlisted make-up volume is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n        \"\
    exact_source_quote\": \"A 0.5M polysulphide solution\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Polysulfide sulfide ingredient\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"12.0 g sodium sulfide\
    \ nonahydrate in the separately prepared stock, not the basal medium.\",\n   \
    \ \"rationale\": \"Target and KOMODO owner lack this stock procedure (add). DSMZ\
    \ owner already retains the exact stock-specific prose in preparation_steps[1].description\
    \ (evidence_only); preserve it and attach source evidence. No percentage basis\
    \ or unlisted make-up volume is supplied.\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\": \"$.data.solutions[0].steps[1].step\"\
    ,\n        \"exact_source_quote\": \"12.0 g Na2S x 9 H2O\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Polysulfide sulfur ingredient\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"1.6 g sulfur in the\
    \ separate stock; no unsupported allotrope or replacement chemical identifier\
    \ is inferred.\",\n    \"rationale\": \"Target and KOMODO owner lack this stock\
    \ procedure (add). DSMZ owner already retains the exact stock-specific prose in\
    \ preparation_steps[1].description (evidence_only); preserve it and attach source\
    \ evidence. No percentage basis or unlisted make-up volume is supplied.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n        \"\
    exact_source_quote\": \"1.6 g sulphur\",\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Polysulfide stock make-up volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare separate anaerobic stock solutions of, Casamino acids(10%), Yeast\
    \ extract (10%), and glycine (2M = 150 g/l). A 0.5M polysulphide solution is prepared\
    \ by dissolving 12.0 g Na2S x 9 H2O in oxygen free water, followed by adding 1.6\
    \ g sulphur - the solution will be dark yellow.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"Oxygen-free water\
    \ is named but its volume and final stock make-up are unquantified.\",\n    \"\
    rationale\": \"Do not derive a final stock volume from the nominal 0.5 M label\
    \ or assume how polysulfide speciation is counted. Preserve the source ambiguity\
    \ and existing DSMZ prose.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive926api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[1].step\",\n      \
    \  \"exact_source_quote\": \"in oxygen free water\",\n        \"snapshot_sha256\"\
    : \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"DSM 10322 polysulfide receiving ratio\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"0.12 mL polysulfide per 10 mL medium, only in the DSM 10322 source branch.\"\
    ,\n    \"rationale\": \"These are distinct source formulation qualifiers, not\
    \ growth assertions or unconditional additions. Retain receiving ratio versus\
    \ final concentration and do not calculate a receiving volume or percent mass\
    \ basis that the source does not establish.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz926\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf\"\
    ,\n        \"source_locator\": \"Page 1, explicitly named receiving branch\",\n\
    \        \"exact_source_quote\": \"0.12 ml polysulphide/10 ml medium, yeast extract\
    \ to a final concentration of 0.2% and \\nglycine to a final concentration of\
    \ 0.1 M for DSM 10322.\",\n        \"snapshot_sha256\": \"574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102\"\
    ,\n        \"parsed_text_sha256\": \"e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"DSM 10322 yeast extract final percentage\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Final yeast extract 0.2%, with unspecified percentage basis, only in the DSM\
    \ 10322 branch.\",\n    \"rationale\": \"These are distinct source formulation\
    \ qualifiers, not growth assertions or unconditional additions. Retain receiving\
    \ ratio versus final concentration and do not calculate a receiving volume or\
    \ percent mass basis that the source does not establish.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz926\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf\",\n        \"\
    source_locator\": \"Page 1, explicitly named receiving branch\",\n        \"exact_source_quote\"\
    : \"0.12 ml polysulphide/10 ml medium, yeast extract to a final concentration\
    \ of 0.2% and \\nglycine to a final concentration of 0.1 M for DSM 10322.\",\n\
    \        \"snapshot_sha256\": \"574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102\"\
    ,\n        \"parsed_text_sha256\": \"e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"DSM 10322 glycine final molarity\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Final glycine 0.1 M only in the DSM 10322 branch.\",\n    \"rationale\": \"\
    These are distinct source formulation qualifiers, not growth assertions or unconditional\
    \ additions. Retain receiving ratio versus final concentration and do not calculate\
    \ a receiving volume or percent mass basis that the source does not establish.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz926\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf\"\
    ,\n        \"source_locator\": \"Page 1, explicitly named receiving branch\",\n\
    \        \"exact_source_quote\": \"0.12 ml polysulphide/10 ml medium, yeast extract\
    \ to a final concentration of 0.2% and \\nglycine to a final concentration of\
    \ 0.1 M for DSM 10322.\",\n        \"snapshot_sha256\": \"574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102\"\
    ,\n        \"parsed_text_sha256\": \"e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"DSM 11906 polysulfide receiving ratio\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"0.08 mL polysulfide per 10 mL medium only in the DSM 11906 branch.\",\n  \
    \  \"rationale\": \"These are distinct source formulation qualifiers, not growth\
    \ assertions or unconditional additions. Retain receiving ratio versus final concentration\
    \ and do not calculate a receiving volume or percent mass basis that the source\
    \ does not establish.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz926\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf\"\
    ,\n        \"source_locator\": \"Page 1, explicitly named receiving branch\",\n\
    \        \"exact_source_quote\": \"0.08 ml polysulphide/10 ml medium, casamino\
    \ acids to a final concentration of 0.2% for \\nDSM 11906.\",\n        \"snapshot_sha256\"\
    : \"574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102\",\n    \
    \    \"parsed_text_sha256\": \"e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"DSM 11906 Casamino acids final percentage\",\n    \"decision\": \"add\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ \"Final Casamino acids 0.2%, basis unspecified, only in the DSM 11906 branch.\"\
    ,\n    \"rationale\": \"These are distinct source formulation qualifiers, not\
    \ growth assertions or unconditional additions. Retain receiving ratio versus\
    \ final concentration and do not calculate a receiving volume or percent mass\
    \ basis that the source does not establish.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz926\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium926.pdf\"\
    ,\n        \"source_locator\": \"Page 1, explicitly named receiving branch\",\n\
    \        \"exact_source_quote\": \"0.08 ml polysulphide/10 ml medium, casamino\
    \ acids to a final concentration of 0.2% for \\nDSM 11906.\",\n        \"snapshot_sha256\"\
    : \"574272a8553f3e675cd1911048be34c724b3a874f9c3f85109677c0ea7fc5102\",\n    \
    \    \"parsed_text_sha256\": \"e8e8868d33fd00b2fee1f5b5cc0587c24a774db368af86e3ae25ae3857f761a2\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"Mineral initial pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"First dissolve NTA\
    \ and adjust the stock to pH 6.5 with KOH, then add minerals.\",\n    \"rationale\"\
    : \"Target/KOMODO omit the procedure. DSMZ owner places mineral-stock adjustment\
    \ at main preparation_steps[2], so correct its scope rather than validating a\
    \ main-medium adjustment. The primary main instruction is do not adjust pH.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[1].steps[0].step\",\n        \"\
    exact_source_quote\": \"First dissolve nitrilotriacetic acid and adjust pH to\
    \ 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\",\n     \
    \   \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"Mineral final pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"After the other minerals,\
    \ adjust the stock to pH 7.0 with KOH.\",\n    \"rationale\": \"Target/KOMODO\
    \ omit the procedure. DSMZ owner places mineral-stock adjustment at main preparation_steps[2],\
    \ so correct its scope rather than validating a main-medium adjustment. The primary\
    \ main instruction is do not adjust pH.\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive926api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/926\",\n        \"source_locator\": \"$.data.solutions[1].steps[0].step\"\
    ,\n        \"exact_source_quote\": \"First dissolve nitrilotriacetic acid and\
    \ adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\"\
    ,\n        \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Mineral KOH quantity\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILIC_THERMOCOCCUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": \"KOH quantity and\
    \ strength are unspecified; preserve the two stock endpoints without an invented\
    \ dose.\",\n    \"rationale\": \"Only the stock pH sequence is quantified. Restore\
    \ stock scope in the DSMZ owner and preserve main do-not-adjust-pH separately.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive926api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/926\",\n  \
    \      \"source_locator\": \"$.data.solutions[1].steps[0].step\",\n        \"\
    exact_source_quote\": \"First dissolve nitrilotriacetic acid and adjust pH to\
    \ 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\",\n     \
    \   \"snapshot_sha256\": \"071c6ca361b9f9d4d35141bae800fd816c05e32751d8a8926fa30dced8aaa052\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '20 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 20/20 primary and 19/20 secondary
    instances; all asserted current CHEBI-based secondary keys have exact pinned MIM
    rows. The separately asserted legacy MediaIngredientMech:000232 remains historically
    unresolved; current exact lookup is complete and negative, not historical identity
    validation. Exact supplied-form mismatch is addressed separately; valid IDs and
    labels do not establish correct source grounding.'
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131361
  - chebi131527
  - chebi26710
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi63004
  - chebi75213
  - chebi75836
  - chebi8346
  - chebi86158
  - chebi86345
  - chebi86364
  - chebi86465
  - chebi91244
  - legacy-lookup
  - mimPinnedCatalog
  - mimPinnedTree
  details: 'Instance coverage on a 0–100 percent scale, denominator 20: primary 100.00%;
    secondary 95.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Source accession and maintained ownership
  outcome: concern
  summary: CM006844 resolves to the exact KOMODO 926 owner and DSMZ contributor CM002098
    under archaea. Both accessions map to DSMZ 926, but all three bacterial-folder
    relationship paths are dangling. Ingredient signature equivalence does not establish
    matching preparation or complete receiving branches.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - id-search
  - bound-owner-context
  - owner-0
  - owner-1
  - primary
  - provider
  - referenced-primary
  - solution241
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
  - CultureMech:006844
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution5902
- assessment_id: preparation
  area: completeness
  topic: Preparation stages, source-only additions and owner differences
  outcome: concern
  summary: DSMZ owner retains main preparation under nitrogen/do not adjust pH and
    separate stock-strength prose. Target/KOMODO omit them. All layers omit the two
    primary receiving branches. DSMZ preparation_steps[2] is mineral-stock pH adjustment
    mislocated at the main level; restore its stock scope so it does not contradict
    the basal instruction. Preserve unspecified percentage bases and missing polysulfide
    make-up volume; do not transfer unrelated parent 141 instructions.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - quantity-inventory
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution5902
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: concern
  summary: DEFINED/DEFINED may describe a deliberately bounded mineral basal stage,
    but not the complete source branches adding yeast extract or Casamino acids. Clarify
    basal versus receiving variants before assigning composition to each representation.
    LIQUID is supported by absence of a mandatory gelling agent. No growth or phenotype
    is inferred from the title.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution5902
- assessment_id: forms
  area: grounding
  topic: Supplied forms and chemical specificity
  outcome: concern
  summary: All explicit hydrated salts were compared with canonical OLS forms. Source
    nickel hexahydrate conflicts with anhydrous CHEBI:34887 in both primary and secondary
    local slots. KI primary CHEBI:8346 is valid independently of unresolved legacy
    000232. Sulfur source wording alone does not justify a specific allotrope or a
    wrong-ID assertion.
  target_ids:
  - CultureMech:006844
  evidence_ids:
  - record
  - primary
  - provider
  - referenced-primary
  - solution241
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
  - CultureMech:006844
  evidence_ids:
  - record
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution5902
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 25 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006844
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
  - CultureMech:006844
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: flattened-mineral-stock
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock flattening creates four incompatible basal sums
  description: The target and both owners treat undiluted mineral stock composition
    as direct medium concentrations. NaCl, magnesium sulfate, calcium chloride and
    boric acid additionally combine incompatible main and stock g/L values. Source
    20 mL receiving dose and separate water stages are absent. Calcium is literally
    0.05 mg in the 2000 mL-water basal source.
  target_ids:
  - CultureMech:006844
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
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  issue_key: broken-owner-relationships
  category: ownership
  severity: blocker
  status: open
  certainty: confirmed
  title: Three relationship paths point to absent bacterial files
  description: Target and KOMODO owner parent_media.path reference bacterial/alkaliphilic_thermococcus_medium.yaml;
    DSMZ owner variant_children[0].path references bacterial/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml.
    Ignored-inclusive search confirms these paths are absent; exact stable-ID owners
    exist in archaea.
  target_ids:
  - CultureMech:006844
  field_paths:
  - parent_media.path
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - relationship-lookup
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  issue_key: mineral-source-version-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Current named mineral stock differs from provider-selected stock
  description: Selected stock 5902 has nickel hexahydrate 0.025 g and no tungstate;
    current referenced 141/241 has 0.03 g nickel hexahydrate and 0.40 mg tungstate.
    The available evidence does not establish the historical choice or temporal order.
  target_ids:
  - CultureMech:006844
  field_paths:
  - solutions
  - ingredients[18].concentration
  evidence_ids:
  - primary
  - provider
  - referenced-primary
  - solution241
  - solution5902
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  issue_key: nickel-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel dichloride
  description: ingredients[18] explicitly names NiCl2 x 6 H2O, but primary and CHEBI-based
    secondary slots assert CHEBI:34887 with formula Cl2Ni. Both candidate source stocks
    specify hexahydrate.
  target_ids:
  - CultureMech:006844
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - chebi34887
  - provider
  - referenced-primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: missing-source-branches-and-stage-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing receiving branches and misplaced stock procedure obscure source scope
  description: Both maintained contributors omit the distinct primary receiving branches,
    while only DSMZ retains stock preparation. Mineral pH instructions remain at its
    main root despite the source main do-not-adjust-pH instruction. Uniform DEFINED
    classification does not describe branches with complex supplements unless the
    record is explicitly restricted to basal medium.
  target_ids:
  - CultureMech:006844
  field_paths:
  - preparation_steps
  - solutions
  - variants
  - medium_type
  - composition_type
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: P3.5 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: legacy-secondary-history-unresolved
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Historical legacy KI correspondence remains unverified
  description: All layers assert MediaIngredientMech:000232 for KI. The complete current
    index/catalog/tree lack that exact legacy key; this establishes a present snapshot
    gap, not a historically wrong KI identity. Required historical correspondence
    remains unavailable.
  target_ids:
  - CultureMech:006844
  field_paths:
  - ingredients[8].mediaingredientmech_term
  evidence_ids:
  - record
  - legacy-lookup
  - mimPinnedCatalog
  - mimPinnedTree
  - chebi8346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f7
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
  - CultureMech:006844
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  description: 'Correct both exact normalized contributors: separate basal and mineral-stock
    quantities, restore dose and water volumes, undo all four incompatible sums, and
    attach source-stage evidence. Preserve source mg calcium and avoid double counting.
    Establish a final-volume basis before final-medium conversions or regeneration.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  description: Correct the two maintained relationship directions to exact archaea
    owner paths while preserving stable IDs and separately checking SOURCE_DUPLICATE
    semantics. Regenerate the target path after owner repair. Append clarification
    without rewriting historical relocation events.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  description: Preserve both exact stock alternatives and obtain source-version evidence
    before choosing a canonical replacement. Do not silently import current 141 stock
    composition or unrelated parent-medium instructions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  description: Re-ground the exact supplied hexahydrate in both maintained contributors
    only after validating the specific ontology and secondary correspondence. Preserve
    amount/version uncertainty independently; no unverified replacement ID is supplied.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  description: Preserve DSMZ stock prose, recover exact missing procedures in KOMODO,
    restore mineral pH instructions to the stock, and represent the two source-qualified
    receiving branches separately. Keep unqualified percentages and unknown polysulfide
    make-up volume explicit; distinguish basal/variant classification and add no new
    growth assertion or taxonomy ID.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
  description: Recover exact historical legacy object or explicit replacement evidence
    before changing this secondary link. Preserve the valid primary KI identifier
    and document the current lookup result separately from unresolved history; do
    not use fuzzy name substitution.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
- action_id: a7
  description: Preserve original history and append a clarification identifying the
    literal timestamp defects and known provenance limits when the owner is curated;
    do not fabricate historical times or source chronology.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:006844
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkaliphilic_thermococcus_medium.yaml
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
- Exact KOMODO 926 detail returned HTTP 403. This optional detail does not negate
  available primary/provider formulation support or itself make the review partial.
- Historical MediaIngredientMech:000232 correspondence remains unresolved. Current
  exact absence is a completed lookup; no replacement, chemical error or historical
  deletion is inferred from it.
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
