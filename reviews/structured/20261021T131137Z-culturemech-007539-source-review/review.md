# Source and formulation review: alkalinus_abyssiniese_medium (CultureMech:007539)

- Review: 20261021T131137Z-culturemech-007539-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:04:57Z
- Finished UTC: 2026-10-21T13:11:37Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

This partial review identifies TOGO M1025 / JCM 974 from the exact provider records, while the requested JCM primary returns HTTP 200 with Nothing found. Both local layers flatten seven mg-scale stock solutes into g/L, combine main and stock water as 901 g/L, and encode three mL stock additions as g/L. Provider main volume 115 mL conflicts with its 900 mL preparation stage and cannot supply a reliable final denominator. Source-stage preparation and chemical-form conflicts remain explicit.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 217; batch 022 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-one task batches contain 210 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 213 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007539 | data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml | generated | alkalinus_abyssiniese_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007539 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007539 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/217/strict.tsv |
| validate-terms | passed | True | CultureMech:007539 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007539 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007539 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm974 | unavailable | True | CultureMech:007539 | The exact JCM GRMD=974 page returned HTTP 200 but says Nothing found; no primary formulation or collection sterilization default is available. TOGO M1025 and MediaDive J974 are assessed as providers, without substituting another JCM accession. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007539.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:007539.

11 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 11/14 primary and 3/14 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 14: primary 78.57%; secondary 21.43%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007539.

24 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main water and wrongly combined stock solvent",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "901.0",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Add components to distilled water and bring volume to 900 ml. For preparation of solid medium, add 20.0 g/L agar. Autoclave and cool (to 50 -- 60C for agar medium). Then, add aseptically the following solutions (separately autoclaved):",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "The 901 G_PER_L value combines the numeric 900 mL main item and 1 L stock item across different units and stages. Neither is a supported mass-concentration conversion. Preserve each solvent quantity and the distinct 900 mL make-up instruction.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "901.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "901.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "900 mL and 1 L describe different preparation stages; adding the numbers 900 + 1 does not produce g/L or an appropriate final solvent total."
  },
  {
    "ingredient_or_context": "MgSO4・7H2O basal amount",
    "field_path": "ingredients[1].concentration",
    "decision": "conflict",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.73913,\n                        \"mmol_l\": 7.05598,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The original source batch mass agrees numerically with the local value, but neither the local implicit 1 L denominator nor the provider 115 mL denominator is established as final medium volume. Retain the mass and source stage; do not select a final g/L from conflicting basis claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "Provider reports 0.2 g / 0.115 L = approximately 1.73913 g/L, but the 0.115 L basis conflicts with its own 900 mL preparation step and is not adopted."
  },
  {
    "ingredient_or_context": "NaCl basal amount",
    "field_path": "ingredients[2].concentration",
    "decision": "conflict",
    "local": {
      "value": "117",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 117,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 117,\n                        \"unit\": \"g\",\n                        \"g_l\": 1017.39,\n                        \"mmol_l\": 17409.2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The original source batch mass agrees numerically with the local value, but neither the local implicit 1 L denominator nor the provider 115 mL denominator is established as final medium volume. Retain the mass and source stage; do not select a final g/L from conflicting basis claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "117",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "117",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "Provider reports 117 g / 0.115 L = approximately 1017.39 g/L, but the 0.115 L basis conflicts with its own 900 mL preparation step and is not adopted."
  },
  {
    "ingredient_or_context": "CaCl2・2H2O basal amount",
    "field_path": "ingredients[3].concentration",
    "decision": "conflict",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.73913,\n                        \"mmol_l\": 11.8296,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The original source batch mass agrees numerically with the local value, but neither the local implicit 1 L denominator nor the provider 115 mL denominator is established as final medium volume. Retain the mass and source stage; do not select a final g/L from conflicting basis claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "Provider reports 0.2 g / 0.115 L = approximately 1.73913 g/L, but the 0.115 L basis conflicts with its own 900 mL preparation step and is not adopted."
  },
  {
    "ingredient_or_context": "KH2PO4 basal amount",
    "field_path": "ingredients[4].concentration",
    "decision": "conflict",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.869565,\n                        \"mmol_l\": 6.38982,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The original source batch mass agrees numerically with the local value, but neither the local implicit 1 L denominator nor the provider 115 mL denominator is established as final medium volume. Retain the mass and source stage; do not select a final g/L from conflicting basis claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "Provider reports 0.1 g / 0.115 L = approximately 0.869565 g/L, but the 0.115 L basis conflicts with its own 900 mL preparation step and is not adopted."
  },
  {
    "ingredient_or_context": "Yeast extract (BD-Difco) basal amount",
    "field_path": "ingredients[5].concentration",
    "decision": "conflict",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 43.4783,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The original source batch mass agrees numerically with the local value, but neither the local implicit 1 L denominator nor the provider 115 mL denominator is established as final medium volume. Retain the mass and source stage; do not select a final g/L from conflicting basis claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "Provider reports 5 g / 0.115 L = approximately 43.4783 g/L, but the 0.115 L basis conflicts with its own 900 mL preparation step and is not adopted."
  },
  {
    "ingredient_or_context": "Peptone (Oxoid) basal amount",
    "field_path": "ingredients[6].concentration",
    "decision": "conflict",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Peptone (Oxoid)\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Peptone\",\n                        \"compound_id\": 1,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 43.4783,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The original source batch mass agrees numerically with the local value, but neither the local implicit 1 L denominator nor the provider 115 mL denominator is established as final medium volume. Retain the mass and source stage; do not select a final g/L from conflicting basis claims.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "Provider reports 5 g / 0.115 L = approximately 43.4783 g/L, but the 0.115 L basis conflicts with its own 900 mL preparation step and is not adopted."
  },
  {
    "ingredient_or_context": "Na2MoO4・2H2O in trace stock",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"mmol_l\": 0.0123993,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "3 mg = 0.003 g; provider stock basis 1 L gives 0.003 g/L. A 10 mL aliquot of that nominal stock transfers 0.03 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "H3BO4 in trace stock",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "30",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO4\",\n          \"volume\": 30,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"H3BO4\",\n                        \"compound_id\": 1250,\n                        \"amount\": 30,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.03,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "30 mg = 0.03 g; provider stock basis 1 L gives 0.03 g/L. A 10 mL aliquot of that nominal stock transfers 0.30 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "MnCl2・4H2O in trace stock",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.003,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "3 mg = 0.003 g; provider stock basis 1 L gives 0.003 g/L. A 10 mL aliquot of that nominal stock transfers 0.03 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "CoCl2・6H2O in trace stock",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0770185,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "10 mg = 0.01 g; provider stock basis 1 L gives 0.01 g/L. A 10 mL aliquot of that nominal stock transfers 0.10 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "NiCl2・6H2O in trace stock",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0154322,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "2 mg = 0.002 g; provider stock basis 1 L gives 0.002 g/L. A 10 mL aliquot of that nominal stock transfers 0.02 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "ZnSO4・7H2O in trace stock",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0347752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "10 mg = 0.01 g; provider stock basis 1 L gives 0.01 g/L. A 10 mL aliquot of that nominal stock transfers 0.10 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "CuCl2・2H2O in trace stock",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00586569,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Restore this mg-scale amount to the trace-stock composition; it is currently an undiluted direct g/L value with an additional mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity limits remain unresolved where specified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "correct"
      }
    ],
    "arithmetic": "1 mg = 0.001 g; provider stock basis 1 L gives 0.001 g/L. A 10 mL aliquot of that nominal stock transfers 0.01 mg, not a final-medium g/L without a valid final denominator."
  },
  {
    "ingredient_or_context": "Trace stock water",
    "field_path": "solutions[0].composition",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "Retain the separate 1 L stock-water quantity and provider-declared 1000 mL stock basis. Do not merge it into main water or treat the whole stock batch as the receiving dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Trace mineral solution (see below) receiving dose",
    "field_path": "solutions[0].concentration",
    "decision": "correct",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Trace mineral solution (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace mineral solution\",\n                        \"solution_id\": 4998,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The source quantity is a stock volume in mL, not a g/L mass concentration. Preserve the original batch addition and its stage; a normalized per-liter dose needs an independently justified denominator.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Source addition is 10 mL. No density or final-medium-volume conversion is performed."
  },
  {
    "ingredient_or_context": "10% (w/v) Na2CO3 solution receiving dose",
    "field_path": "solutions[1].concentration",
    "decision": "correct",
    "local": {
      "value": "100",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Na2CO3 solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"attribute\": \"w/v, 10%\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The source quantity is a stock volume in mL, not a g/L mass concentration. Preserve the original batch addition and its stage; a normalized per-liter dose needs an independently justified denominator.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Source addition is 100 mL. No density or final-medium-volume conversion is performed."
  },
  {
    "ingredient_or_context": "10% (w/v) Glucose solution receiving dose",
    "field_path": "solutions[2].concentration",
    "decision": "correct",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Glucose solution\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      },
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"attribute\": \"w/v, 10%\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      }
    ],
    "rationale": "The source quantity is a stock volume in mL, not a g/L mass concentration. Preserve the original batch addition and its stage; a normalized per-liter dose needs an independently justified denominator.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Source addition is 5 mL. No density or final-medium-volume conversion is performed."
  },
  {
    "ingredient_or_context": "Sodium carbonate stock strength",
    "field_path": "solutions[1].preferred_term",
    "decision": "evidence_only",
    "local": "10% (w/v) Na2CO3 solution",
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Na2CO3 solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "The preferred name already preserves the explicit 10% (w/v) strength, but no attached claim evidence exists. Strength, composition and receiving dose remain separate.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].preferred_term",
        "stored": "10% (w/v) Na2CO3 solution",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[1].preferred_term",
        "stored": "10% (w/v) Na2CO3 solution",
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "10% (w/v) means 10 g per 100 mL stock. The listed aliquot transfers 10 g; no final g/L is inferred."
  },
  {
    "ingredient_or_context": "Glucose stock strength",
    "field_path": "solutions[2].preferred_term",
    "decision": "evidence_only",
    "local": "10% (w/v) Glucose solution",
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"10% (w/v) Glucose solution\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "The preferred name already preserves the explicit 10% (w/v) strength, but no attached claim evidence exists. Strength, composition and receiving dose remain separate.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].preferred_term",
        "stored": "10% (w/v) Glucose solution",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "solutions[2].preferred_term",
        "stored": "10% (w/v) Glucose solution",
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "10% (w/v) means 10 g per 100 mL stock. The listed aliquot transfers 0.5 g; no final g/L is inferred."
  },
  {
    "ingredient_or_context": "Basal make-up stage",
    "field_path": "preparation.basal_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Add components to distilled water and bring volume to 900 ml. For preparation of solid medium, add 20.0 g/L agar. Autoclave and cool (to 50 -- 60C for agar medium). Then, add aseptically the following solutions (separately autoclaved):",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "Preserve the instruction to bring the basal stage to 900 mL before the separately sterilized later solutions. Distinguish this from the separate 900 mL water item and avoid treating either as the final medium volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Provider-declared main basis",
    "field_path": "source.main4997.volume",
    "decision": "conflict",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadiveJ974api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J974",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 115",
        "snapshot_sha256": "f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed"
      },
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Add components to distilled water and bring volume to 900 ml. For preparation of solid medium, add 20.0 g/L agar. Autoclave and cool (to 50 -- 60C for agar medium). Then, add aseptically the following solutions (separately autoclaved):",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "The provider 115 mL basis omits the explicit 900 mL basal stage and cannot be adopted to compute final concentrations. The local preparation container is absent; source locator remains explicitly source-scoped.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "conflict"
      }
    ],
    "arithmetic": "10 + 100 + 5 = 115 mL counts listed stock additions only. A literal liquid-item sum 900 + 10 + 100 + 5 = 1015 mL is not equivalent to the instruction to bring the initial stage to 900 mL, nor a measured final volume."
  },
  {
    "ingredient_or_context": "Conditional solid-medium agar",
    "field_path": "variants",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "For preparation of solid medium, add 20.0 g/L agar.",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "This is an explicitly conditional solid-medium branch. Retain it as source preparation/variant context if represented; it is not a missing mandatory ingredient in the selected liquid baseline.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "variants",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Conditional agar cooling interval",
    "field_path": "preparation.agar_cooling",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "togoM1025",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Autoclave and cool (to 50 -- 60C for agar medium).",
        "snapshot_sha256": "f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389"
      }
    ],
    "rationale": "The 50–60°C interval applies to the agar branch. Retain the conditional range; do not assign it as liquid incubation temperature or infer an autoclave cycle.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ]
  }
]

### Exact provider identity and missing primary

identity: supported. Targets: CultureMech:007539.

CultureMech:007539 is generated from the explicitly named TOGO M1025 owner. Exact TOGO metadata and MediaDive J974 link the requested JCM 974 and medium name. Identity is resolved despite the required primary content being unavailable; provider data are not relabeled as primary verification.

### Basal masses, trace formulation, additions and conflicting volumes

consistency: concern. Targets: CultureMech:007539.

The inventory covers all 14 direct concentrations, three solution concentrations, the stock strengths and solvent/preparation contexts. Seven mg-scale trace solutes are flattened into main g/L; main and stock water are numerically combined; all three stock volumes have mass units. The provider’s main 115 mL basis conflicts with the explicit 900 mL stage, while its stock endpoint is internally consistent. No final denominator or synthesized recipe is selected.

### Hydrate mismatches and provider chemical ambiguity

grounding: concern. Targets: CultureMech:007539.

Local CoCl2·6H2O and NiCl2·6H2O names match the provider hydrates, but CHEBI:35696 and CHEBI:34887 have unhydrated formulas. The other explicitly asserted hydrates and phosphate identities correspond to the source forms. H3BO4 is literal in both providers while TOGO labels it Boric acid; the unavailable primary does not resolve that identity discrepancy, and no H3BO3 replacement or new identifier is invented.

### Make-up, separate sterilization and conditional agar branch

completeness: concern. Targets: CultureMech:007539.

Both layers omit the source comment: basal make-up to 900 mL, autoclaving and cooling, then aseptic addition of separately autoclaved carbonate and glucose stocks. Agar 20 g/L and cooling to 50–60°C are conditional solid-medium instructions, not mandatory liquid-baseline ingredients or incubation conditions. No exact pH, autoclave temperature or duration is supplied by the available record-specific provider content.

### Complex liquid baseline and unsupported metal calculation

scope: concern. Targets: CultureMech:007539.

COMPLEX/UNDEFINED and LIQUID agree with the provider baseline; the agar branch is explicitly conditional. high_metal:true needs a defensible source-stage molar derivation after correcting stock and volume scope. The large original NaCl mass is real provider content, so trace errors do not establish that the flag should be false. No organism, strain, taxonomy, assembly, DOI/PMID, growth or separate variant evidence is asserted.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007539.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Inherited flattening, numeric water merge and current ownership

provenance: concern. Targets: CultureMech:007539.

The target repeats the maintained owner’s defects. Its water note explicitly preserves the earlier 900.0 plus 1.0 duplicate sum; those rows are different preparation contexts. Current TOGO stock separation and migration-copy functions, plus the current cleanup code’s conflict retention rather than summation, are hash-bound implementation context, not historical replay or authority to mutate this recipe.

## Findings

### f1: Stock composition, stock additions and solvent stages collapse into false concentrations

blocker / open / confirmed; issue key: culturemech.007539.stock-unit-collapse.

Seven mg-scale trace solutes are direct g/L values; the 10 mL trace, 100 mL carbonate and 5 mL glucose doses are encoded as g/L; and 900 mL main water plus 1 L stock water become 901 g/L. The provider’s 115 mL main denominator also conflicts with its own 900 mL stage. These combined errors prevent faithful representation of the named formulation.

### f2: Two explicit hydrates use unhydrated terms and one source chemical remains ambiguous

major / open / confirmed; issue key: culturemech.007539.form-and-identity-conflicts.

Source CoCl2·6H2O and NiCl2·6H2O are mapped to the unhydrated CHEBI:35696 and CHEBI:34887 formulas. Both providers also preserve H3BO4, while TOGO calls it Boric acid. Valid canonical labels do not resolve the hydrate mismatches or the provider chemical ambiguity.

### f3: The source-specific stock addition sequence is absent

major / open / confirmed; issue key: culturemech.007539.preparation-loss.

Neither layer preserves basal make-up, autoclaving/cooling, or aseptic addition of separately autoclaved later stocks. Empty Unknown solution stubs do not encode these operational boundaries. Conditional agar and cooling text must remain separately scoped.

### f4: The high-metal flag lacks a valid source-stage derivation

major / open / confirmed; issue key: culturemech.007539.high-metal-support.

high_metal:true has no attached calculation consistent with the schema’s molar threshold. Flattened stock quantities and a conflicted final denominator invalidate deriving it directly from the current values, and current analyzer approximations do not establish exact metal molarity. The genuine 117 g basal NaCl amount means this finding is not evidence for automatically setting false.

### f5: No scoped formulation evidence distinguishes provider content from unavailable primary

minor / open / confirmed; issue key: culturemech.007539.claim-evidence.

Both layers name the sources but lack attached formulation evidence and references for the stock hierarchy, quantity claims and preparation. The currently inaccessible exact primary must not be treated as if its full recipe had been inspected.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct source-scoped basal amounts, stock composition, stock strength and batch doses in maintained input after resolving the primary and denominator conflicts. Preserve original units and stage-specific solvent quantities; do not adopt the provider g_l values or invent a final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the exact supplied hydrates and ambiguous boron compound against an authoritative recipe before choosing identifiers or molecular weights. Preserve conflicting source text and do not guess replacement CHEBI IDs or silently correct the formula.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Restore the exact available provider preparation with explicit provider status and primary-access limit, distinguishing basal versus later-stock steps and optional agar conditions. Add no pH or sterilization cycle absent from the exact available sources.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Reassess the flag using resolved source-stage quantities and exact chemical forms with an explicit valid molar method. Retain uncertainty until the final basis is established; do not infer a replacement boolean from the trace-unit errors alone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach the exact inspected provider snippets with original timestamps and preserved conflicts to their narrow claims when curating. Record the actual primary-access limitation and resolve it before claiming primary authentication.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch022/217/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/217/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml:1:id: CultureMech:007539<br>./data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml:1:id: CultureMech:007539<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/217/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 15 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/217/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| jcm974-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=974; Preserved exact public retrieval result | context_only | The exact JCM GRMD=974 page returned HTTP 200 but says Nothing found; no primary formulation or collection sterilization default is available. TOGO M1025 and MediaDive J974 are assessed as providers, without substituting another JCM accession. |
| togoM1025 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025; Entire captured exact source, all rows and preparation fields | supports | Full exact provider metadata, three component sections and preparation comment: basal 900 mL item, separate 900 mL make-up instruction, trace stock 10 mL, later 100 mL carbonate and 5 mL glucose stocks, seven mg-scale trace solutes and stock water. |
| mediadiveJ974api | https://mediadive.dsmz.de/rest/medium/J974; Entire captured exact source, all rows and preparation fields | supports | Complete main 4997 and stock 4998. Main declared volume 115 mL and g_l fields are retained as conflicted provider calculations; original masses, stock doses and preparation stages are assessed separately. |
| solution4998 | https://mediadive.dsmz.de/rest/solution/4998; Entire captured exact source, all rows and preparation fields | supports | Complete exact stock endpoint, seven mg-scale solutes plus 1000 mL water and declared 1000 mL stock basis. Rows agree with main-provider stock after null-only keys are removed; this is provider consistency, not independent primary support. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch022/217/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch022/217/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| writer-0 | src/culturemech/schema/culturemech.yaml; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current analyzer/tagger and schema metal definition read. Schema names ≥1049.84 mM and includes sodium; the analyzer uses direct ingredients, approximate raw-unit factors and default factor 1 for enum units, without exact hydrate molecular-weight conversion. Current behavior is not a historical run. |
| writer-1 | scripts/analyze_metal_concentrations.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current analyzer/tagger and schema metal definition read. Schema names ≥1049.84 mM and includes sodium; the analyzer uses direct ingredients, approximate raw-unit factors and default factor 1 for enum units, without exact hydrate molecular-weight conversion. Current behavior is not a historical run. |
| writer-2 | scripts/add_metal_ree_labels.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Full current analyzer/tagger and schema metal definition read. Schema names ≥1049.84 mM and includes sodium; the analyzer uses direct ingredients, approximate raw-unit factors and default factor 1 for enum units, without exact hydrate molecular-weight conversion. Current behavior is not a historical run. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | src/culturemech/import/togo_importer.py; _ingredient_from_item lines 273–339; _local_batch_volume_ml lines 480–507; _solution_from_item lines 533–585; _extract_primary_components lines 587–641 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml", "events": 12, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact JCM GRMD=974 page returned HTTP 200 but says Nothing found; no primary formulation or collection sterilization default is available. TOGO M1025 and MediaDive J974 are assessed as providers, without substituting another JCM accession.
- Exact JCM 974 primary formulation remains unavailable. No collection default from a different JCM page is transferred.
- The 900 mL water item, 900 mL make-up instruction, later stock additions and provider 115 mL basis are retained as distinct source statements. No measured final medium volume or final g/L correction is asserted.
- Stock-dose mass calculations are conditional on the explicitly declared provider 1000 mL stock basis; they are transferred masses, not final-medium concentrations. No corpus-wide metal analysis was executed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131137Z-culturemech-007539-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkalinus_abyssiniese_medium (CultureMech:007539)'
started_at: '2026-10-21T13:04:57Z'
finished_at: '2026-10-21T13:11:37Z'
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
summary: This partial review identifies TOGO M1025 / JCM 974 from the exact provider
  records, while the requested JCM primary returns HTTP 200 with Nothing found. Both
  local layers flatten seven mg-scale stock solutes into g/L, combine main and stock
  water as 901 g/L, and encode three mL stock additions as g/L. Provider main volume
  115 mL conflicts with its 900 mL preparation stage and cannot supply a reliable
  final denominator. Source-stage preparation and chemical-form conflicts remain explicit.
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
  - path: data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
    sha256: c1a790ace1a798690064f9797a23b55cf638cec79e20b3e62e8324b07a62fbb0
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
    sha256: e90eaced188122c863f212ae185ae6faaedc20e3bc9fc4415456603d8e6f0f2d
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
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 217; batch 022 item 7 of 10, selected in Python lexicographic
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
  - CultureMech:007539
targets:
- target_id: CultureMech:007539
  path: data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  label: alkalinus_abyssiniese_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/217/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/217/strict.tsv"
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007539
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
  - CultureMech:007539
- check_id: jcm974-source-access
  name: 'Exact source content access: jcm974'
  required: true
  status: unavailable
  summary: The exact JCM GRMD=974 page returned HTTP 200 but says Nothing found; no
    primary formulation or collection sterilization default is available. TOGO M1025
    and MediaDive J974 are assessed as providers, without substituting another JCM
    accession.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - jcm974-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:54.496919Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/217/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:58.384132Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/217/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:02.821977Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:06:04.939601Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:11:35Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml:1:id: CultureMech:007539

    ./data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml:1:id:
    CultureMech:007539

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/217/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:11:35Z'
  support: supports
  summary: 15 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: c7298f2de13fb263470e46e0c078a12dccfdd8863c13ed7204bb931d48975fef
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/217/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: b75a6a1ed73c68d14335f417efea8a103e123659870459be0799f8ee52786c52
- evidence_id: jcm974-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=974
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:48:26.737709Z'
  support: context_only
  summary: The exact JCM GRMD=974 page returned HTTP 200 but says Nothing found; no
    primary formulation or collection sterilization default is available. TOGO M1025
    and MediaDive J974 are assessed as providers, without substituting another JCM
    accession.
  snapshot_sha256: 4e20b68a26dca3aa5e30c6d4ebf3d39fe0858a2100a7575a57d541551f874707
- evidence_id: togoM1025
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025
  locator: Entire captured exact source, all rows and preparation fields
  accessed_at: '2026-10-21T12:48:25.706065Z'
  support: supports
  summary: 'Full exact provider metadata, three component sections and preparation
    comment: basal 900 mL item, separate 900 mL make-up instruction, trace stock 10
    mL, later 100 mL carbonate and 5 mL glucose stocks, seven mg-scale trace solutes
    and stock water.'
  snapshot_sha256: f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389
- evidence_id: mediadiveJ974api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J974
  locator: Entire captured exact source, all rows and preparation fields
  accessed_at: '2026-10-21T12:48:25.537806Z'
  support: supports
  summary: Complete main 4997 and stock 4998. Main declared volume 115 mL and g_l
    fields are retained as conflicted provider calculations; original masses, stock
    doses and preparation stages are assessed separately.
  snapshot_sha256: f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed
- evidence_id: solution4998
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4998
  locator: Entire captured exact source, all rows and preparation fields
  accessed_at: '2026-10-21T12:49:29.674378Z'
  support: supports
  summary: Complete exact stock endpoint, seven mg-scale solutes plus 1000 mL water
    and declared 1000 mL stock basis. Rows agree with main-provider stock after null-only
    keys are removed; this is provider consistency, not independent primary support.
  snapshot_sha256: c0931f9d88ec850be7850b88c3f06e5e83a8dc36a602deca27e71e6ec2bddbdb
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
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
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
  accessed_at: '2026-10-21T13:11:35Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/217/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: ada408b7d2e781ee80b293104f05557fd6fa3066323b085b674052f14adbb902
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/217/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: f0866a258df83564cfae3d107b2b86ea63ffc0ba48c220cb43e141d8729505ea
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Full current analyzer/tagger and schema metal definition read. Schema names
    ≥1049.84 mM and includes sodium; the analyzer uses direct ingredients, approximate
    raw-unit factors and default factor 1 for enum units, without exact hydrate molecular-weight
    conversion. Current behavior is not a historical run.
  snapshot_sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
- evidence_id: writer-1
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Full current analyzer/tagger and schema metal definition read. Schema names
    ≥1049.84 mM and includes sodium; the analyzer uses direct ingredients, approximate
    raw-unit factors and default factor 1 for enum units, without exact hydrate molecular-weight
    conversion. Current behavior is not a historical run.
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: writer-2
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Full current analyzer/tagger and schema metal definition read. Schema names
    ≥1049.84 mM and includes sodium; the analyzer uses direct ingredients, approximate
    raw-unit factors and default factor 1 for enum units, without exact hydrate molecular-weight
    conversion. Current behavior is not a historical run.
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item lines 273–339; _local_batch_volume_ml lines 480–507;
    _solution_from_item lines 533–585; _extract_primary_components lines 587–641
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINUS_ABYSSINIESE_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:11:35Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml",
    "events": 12, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '11 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 11/14 primary and 3/14 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi26710
  - chebi31795
  - chebi32312
  - chebi34887
  - chebi35696
  - chebi63036
  - chebi75213
  - chebi86158
  - chebi86318
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 14: primary 78.57%;
    secondary 21.43%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 24 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main water and wrongly combined\
    \ stock solvent\",\n    \"field_path\": \"ingredients[0].concentration\",\n  \
    \  \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"901.0\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n      },\n\
    \      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Add components to distilled water and bring volume to 900 ml. For preparation\
    \ of solid medium, add 20.0 g/L agar. Autoclave and cool (to 50 -- 60C for agar\
    \ medium). Then, add aseptically the following solutions (separately autoclaved):\"\
    ,\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      }\n    ],\n    \"rationale\": \"The 901 G_PER_L value combines the numeric\
    \ 900 mL main item and 1 L stock item across different units and stages. Neither\
    \ is a supported mass-concentration conversion. Preserve each solvent quantity\
    \ and the distinct 900 mL make-up instruction.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"901.0\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"901.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"900 mL and 1 L describe different preparation stages; adding the numbers 900\
    \ + 1 does not produce g/L or an appropriate final solvent total.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"MgSO4・7H2O basal amount\",\n    \"field_path\"\
    : \"ingredients[1].concentration\",\n    \"decision\": \"conflict\",\n    \"local\"\
    : {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.73913,\\\
    n                        \\\"mmol_l\\\": 7.05598,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n      }\n\
    \    ],\n    \"rationale\": \"The original source batch mass agrees numerically\
    \ with the local value, but neither the local implicit 1 L denominator nor the\
    \ provider 115 mL denominator is established as final medium volume. Retain the\
    \ mass and source stage; do not select a final g/L from conflicting basis claims.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"conflict\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ reports 0.2 g / 0.115 L = approximately 1.73913 g/L, but the 0.115 L basis conflicts\
    \ with its own 900 mL preparation step and is not adopted.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"NaCl basal amount\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"conflict\",\n    \"local\": {\n      \"value\": \"117\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 117,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 117,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1017.39,\\n            \
    \            \\\"mmol_l\\\": 17409.2,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"The original source batch mass agrees\
    \ numerically with the local value, but neither the local implicit 1 L denominator\
    \ nor the provider 115 mL denominator is established as final medium volume. Retain\
    \ the mass and source stage; do not select a final g/L from conflicting basis\
    \ claims.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"117\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"conflict\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"117\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ reports 117 g / 0.115 L = approximately 1017.39 g/L, but the 0.115 L basis conflicts\
    \ with its own 900 mL preparation step and is not adopted.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"CaCl2・2H2O basal amount\",\n    \"field_path\": \"\
    ingredients[3].concentration\",\n    \"decision\": \"conflict\",\n    \"local\"\
    : {\n      \"value\": \"0.2\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.73913,\\\
    n                        \\\"mmol_l\\\": 11.8296,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n      }\n\
    \    ],\n    \"rationale\": \"The original source batch mass agrees numerically\
    \ with the local value, but neither the local implicit 1 L denominator nor the\
    \ provider 115 mL denominator is established as final medium volume. Retain the\
    \ mass and source stage; do not select a final g/L from conflicting basis claims.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"conflict\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ reports 0.2 g / 0.115 L = approximately 1.73913 g/L, but the 0.115 L basis conflicts\
    \ with its own 900 mL preparation step and is not adopted.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"KH2PO4 basal amount\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"decision\": \"conflict\",\n    \"local\": {\n      \"value\": \"0.1\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.869565,\\n           \
    \             \\\"mmol_l\\\": 6.38982,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"The original source batch mass agrees\
    \ numerically with the local value, but neither the local implicit 1 L denominator\
    \ nor the provider 115 mL denominator is established as final medium volume. Retain\
    \ the mass and source stage; do not select a final g/L from conflicting basis\
    \ claims.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"conflict\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ reports 0.1 g / 0.115 L = approximately 0.869565 g/L, but the 0.115 L basis\
    \ conflicts with its own 900 mL preparation step and is not adopted.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Yeast extract (BD-Difco) basal amount\"\
    ,\n    \"field_path\": \"ingredients[5].concentration\",\n    \"decision\": \"\
    conflict\",\n    \"local\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1025\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"BD-Difco\\\",\\n    \
    \                    \\\"amount\\\": 5,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 43.4783,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"The original source batch mass agrees numerically\
    \ with the local value, but neither the local implicit 1 L denominator nor the\
    \ provider 115 mL denominator is established as final medium volume. Retain the\
    \ mass and source stage; do not select a final g/L from conflicting basis claims.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"conflict\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ reports 5 g / 0.115 L = approximately 43.4783 g/L, but the 0.115 L basis conflicts\
    \ with its own 900 mL preparation step and is not adopted.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Peptone (Oxoid) basal amount\",\n    \"field_path\"\
    : \"ingredients[6].concentration\",\n    \"decision\": \"conflict\",\n    \"local\"\
    : {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Peptone (Oxoid)\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Peptone\\\",\\n                        \\\"compound_id\\\":\
    \ 1,\\n                        \\\"attribute\\\": \\\"Oxoid\\\",\\n          \
    \              \\\"amount\\\": 5,\\n                        \\\"unit\\\": \\\"\
    g\\\",\\n                        \\\"g_l\\\": 43.4783,\\n                    \
    \    \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"The original source batch mass agrees numerically\
    \ with the local value, but neither the local implicit 1 L denominator nor the\
    \ provider 115 mL denominator is established as final medium volume. Retain the\
    \ mass and source stage; do not select a final g/L from conflicting basis claims.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"conflict\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ reports 5 g / 0.115 L = approximately 43.4783 g/L, but the 0.115 L basis conflicts\
    \ with its own 900 mL preparation step and is not adopted.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Na2MoO4・2H2O in trace stock\",\n    \"field_path\"\
    : \"ingredients[7].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"3\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 3,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 3,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.003,\\n \
    \                       \\\"mmol_l\\\": 0.0123993,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n      }\n\
    \    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"3 mg = 0.003 g; provider stock basis 1 L gives 0.003 g/L. A 10 mL aliquot\
    \ of that nominal stock transfers 0.03 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"H3BO4 in trace\
    \ stock\",\n    \"field_path\": \"ingredients[8].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"30\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO4\\\",\\n          \\\"volume\\\": 30,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"H3BO4\\\",\\n                        \\\"compound_id\\\": 1250,\\\
    n                        \\\"amount\\\": 30,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.03,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"30\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"30 mg = 0.03 g; provider stock basis 1 L gives 0.03 g/L. A 10 mL aliquot of\
    \ that nominal stock transfers 0.30 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"MnCl2・4H2O\
    \ in trace stock\",\n    \"field_path\": \"ingredients[9].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"3\",\n  \
    \    \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 3,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.003,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"3 mg = 0.003 g; provider stock basis 1 L gives 0.003 g/L. A 10 mL aliquot\
    \ of that nominal stock transfers 0.03 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"CoCl2・6H2O\
    \ in trace stock\",\n    \"field_path\": \"ingredients[10].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"10\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0770185,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"10 mg = 0.01 g; provider stock basis 1 L gives 0.01 g/L. A 10 mL aliquot of\
    \ that nominal stock transfers 0.10 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"NiCl2・6H2O\
    \ in trace stock\",\n    \"field_path\": \"ingredients[11].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"2\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n\
    \                        \\\"mmol_l\\\": 0.0154322,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"2 mg = 0.002 g; provider stock basis 1 L gives 0.002 g/L. A 10 mL aliquot\
    \ of that nominal stock transfers 0.02 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"ZnSO4・7H2O\
    \ in trace stock\",\n    \"field_path\": \"ingredients[12].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"10\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 10,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.01,\\n\
    \                        \\\"mmol_l\\\": 0.0347752,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"10 mg = 0.01 g; provider stock basis 1 L gives 0.01 g/L. A 10 mL aliquot of\
    \ that nominal stock transfers 0.10 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"CuCl2・2H2O\
    \ in trace stock\",\n    \"field_path\": \"ingredients[13].concentration\",\n\
    \    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1\",\n \
    \     \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.001,\\n\
    \                        \\\"mmol_l\\\": 0.00586569,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\n     \
    \ }\n    ],\n    \"rationale\": \"Restore this mg-scale amount to the trace-stock\
    \ composition; it is currently an undiluted direct g/L value with an additional\
    \ mg/g error. The stock dose is a separate claim. Exact hydrate and H3BO4 identity\
    \ limits remain unresolved where specified.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"1 mg = 0.001 g; provider stock basis 1 L gives 0.001 g/L. A 10 mL aliquot\
    \ of that nominal stock transfers 0.01 mg, not a final-medium g/L without a valid\
    \ final denominator.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace stock\
    \ water\",\n    \"field_path\": \"solutions[0].composition\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the separate 1 L stock-water quantity\
    \ and provider-declared 1000 mL stock basis. Do not merge it into main water or\
    \ treat the whole stock batch as the receiving dose.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions[0].composition\"\
    ,\n        \"stored\": [],\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace mineral solution (see below) receiving dose\",\n    \"field_path\":\
    \ \"solutions[0].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace mineral solution (see below)\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace mineral solution\\\",\\n                        \\\"solution_id\\\
    \": 4998,\\n                        \\\"amount\\\": 10,\\n                   \
    \     \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"The source quantity is a stock volume\
    \ in mL, not a g/L mass concentration. Preserve the original batch addition and\
    \ its stage; a normalized per-liter dose needs an independently justified denominator.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ addition is 10 mL. No density or final-medium-volume conversion is performed.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"10% (w/v) Na2CO3 solution receiving\
    \ dose\",\n    \"field_path\": \"solutions[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"100\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Na2CO3 solution\\\",\\n          \\\"\
    volume\\\": 100,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\
    \": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"attribute\\\": \\\"w/v, 10%\\\",\\n             \
    \           \\\"amount\\\": 100,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"The source quantity is a stock volume\
    \ in mL, not a g/L mass concentration. Preserve the original batch addition and\
    \ its stage; a normalized per-liter dose needs an independently justified denominator.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"100\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ addition is 100 mL. No density or final-medium-volume conversion is performed.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"10% (w/v) Glucose solution receiving\
    \ dose\",\n    \"field_path\": \"solutions[2].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"5\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM1025\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Glucose solution\\\",\\n          \\\
    \"volume\\\": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\
    \": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"attribute\\\": \\\"w/v, 10%\\\",\\n       \
    \                 \\\"amount\\\": 5,\\n                        \\\"unit\\\": \\\
    \"ml\\\",\\n                        \\\"optional\\\": 0\\n                   \
    \ }\",\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      }\n    ],\n    \"rationale\": \"The source quantity is a stock volume\
    \ in mL, not a g/L mass concentration. Preserve the original batch addition and\
    \ its stage; a normalized per-liter dose needs an independently justified denominator.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ addition is 5 mL. No density or final-medium-volume conversion is performed.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Sodium carbonate stock strength\"\
    ,\n    \"field_path\": \"solutions[1].preferred_term\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": \"10% (w/v) Na2CO3 solution\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Na2CO3 solution\\\",\\n          \\\"\
    volume\\\": 100,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\
    \": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ }\n    ],\n    \"rationale\": \"The preferred name already preserves the explicit\
    \ 10% (w/v) strength, but no attached claim evidence exists. Strength, composition\
    \ and receiving dose remain separate.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"solutions[1].preferred_term\",\n    \
    \    \"stored\": \"10% (w/v) Na2CO3 solution\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].preferred_term\",\n        \"stored\"\
    : \"10% (w/v) Na2CO3 solution\",\n        \"decision\": \"evidence_only\"\n  \
    \    }\n    ],\n    \"arithmetic\": \"10% (w/v) means 10 g per 100 mL stock. The\
    \ listed aliquot transfers 10 g; no final g/L is inferred.\"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Glucose stock strength\",\n    \"field_path\": \"solutions[2].preferred_term\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": \"10% (w/v) Glucose solution\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1025\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% (w/v) Glucose solution\\\",\\n          \\\
    \"volume\\\": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\
    \": 10,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ }\n    ],\n    \"rationale\": \"The preferred name already preserves the explicit\
    \ 10% (w/v) strength, but no attached claim evidence exists. Strength, composition\
    \ and receiving dose remain separate.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"solutions[2].preferred_term\",\n    \
    \    \"stored\": \"10% (w/v) Glucose solution\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].preferred_term\",\n        \"stored\"\
    : \"10% (w/v) Glucose solution\",\n        \"decision\": \"evidence_only\"\n \
    \     }\n    ],\n    \"arithmetic\": \"10% (w/v) means 10 g per 100 mL stock.\
    \ The listed aliquot transfers 0.5 g; no final g/L is inferred.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Basal make-up stage\",\n    \"field_path\":\
    \ \"preparation.basal_volume\",\n    \"decision\": \"add\",\n    \"local\": null,\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM1025\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Add components to distilled water and bring volume to 900 ml. For preparation\
    \ of solid medium, add 20.0 g/L agar. Autoclave and cool (to 50 -- 60C for agar\
    \ medium). Then, add aseptically the following solutions (separately autoclaved):\"\
    ,\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve the instruction to bring the\
    \ basal stage to 900 mL before the separately sterilized later solutions. Distinguish\
    \ this from the separate 900 mL water item and avoid treating either as the final\
    \ medium volume.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n      \
    \  \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Provider-declared main basis\",\n    \"field_path\": \"source.main4997.volume\"\
    ,\n    \"decision\": \"conflict\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadiveJ974api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J974\",\n        \"source_locator\"\
    : \"$.data.solutions[0].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 115\",\n        \"snapshot_sha256\": \"f573ea40ff6d5c116dbec809c7d465917a50fe33622e1d104d048595c25404ed\"\
    \n      },\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Add components to distilled water and bring volume to 900 ml. For preparation\
    \ of solid medium, add 20.0 g/L agar. Autoclave and cool (to 50 -- 60C for agar\
    \ medium). Then, add aseptically the following solutions (separately autoclaved):\"\
    ,\n        \"snapshot_sha256\": \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\
    \n      }\n    ],\n    \"rationale\": \"The provider 115 mL basis omits the explicit\
    \ 900 mL basal stage and cannot be adopted to compute final concentrations. The\
    \ local preparation container is absent; source locator remains explicitly source-scoped.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"conflict\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"10\
    \ + 100 + 5 = 115 mL counts listed stock additions only. A literal liquid-item\
    \ sum 900 + 10 + 100 + 5 = 1015 mL is not equivalent to the instruction to bring\
    \ the initial stage to 900 mL, nor a measured final volume.\"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Conditional solid-medium agar\",\n    \"field_path\"\
    : \"variants\",\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"For preparation of solid medium, add 20.0 g/L agar.\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ }\n    ],\n    \"rationale\": \"This is an explicitly conditional solid-medium\
    \ branch. Retain it as source preparation/variant context if represented; it is\
    \ not a missing mandatory ingredient in the selected liquid baseline.\",\n   \
    \ \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"variants\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"variants\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Conditional agar cooling interval\",\n    \"field_path\": \"preparation.agar_cooling\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM1025\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1025\",\n\
    \        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Autoclave and cool (to 50 -- 60C for agar medium).\",\n        \"snapshot_sha256\"\
    : \"f4d430d7492450432b0841a6544556f95904c0f33a55c0a7c006a246c5e7a389\"\n     \
    \ }\n    ],\n    \"rationale\": \"The 50–60°C interval applies to the agar branch.\
    \ Retain the conditional range; do not assign it as liquid incubation temperature\
    \ or infer an autoclave cycle.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact provider identity and missing primary
  outcome: supported
  summary: CultureMech:007539 is generated from the explicitly named TOGO M1025 owner.
    Exact TOGO metadata and MediaDive J974 link the requested JCM 974 and medium name.
    Identity is resolved despite the required primary content being unavailable; provider
    data are not relabeled as primary verification.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - owner-0
  - id-search
  - togoM1025
  - mediadiveJ974api
  - jcm974-attempt
- assessment_id: source-stage-consistency
  area: consistency
  topic: Basal masses, trace formulation, additions and conflicting volumes
  outcome: concern
  summary: The inventory covers all 14 direct concentrations, three solution concentrations,
    the stock strengths and solvent/preparation contexts. Seven mg-scale trace solutes
    are flattened into main g/L; main and stock water are numerically combined; all
    three stock volumes have mass units. The provider’s main 115 mL basis conflicts
    with the explicit 900 mL stage, while its stock endpoint is internally consistent.
    No final denominator or synthesized recipe is selected.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - quantity-inventory
  - quantity-local-fields
  - togoM1025
  - mediadiveJ974api
  - solution4998
- assessment_id: forms
  area: grounding
  topic: Hydrate mismatches and provider chemical ambiguity
  outcome: concern
  summary: Local CoCl2·6H2O and NiCl2·6H2O names match the provider hydrates, but
    CHEBI:35696 and CHEBI:34887 have unhydrated formulas. The other explicitly asserted
    hydrates and phosphate identities correspond to the source forms. H3BO4 is literal
    in both providers while TOGO labels it Boric acid; the unavailable primary does
    not resolve that identity discrepancy, and no H3BO3 replacement or new identifier
    is invented.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - chebi35696
  - chebi34887
  - chebi31795
  - chebi86158
  - chebi75213
  - chebi86368
  - chebi32312
  - chebi86318
  - chebi63036
- assessment_id: preparation
  area: completeness
  topic: Make-up, separate sterilization and conditional agar branch
  outcome: concern
  summary: 'Both layers omit the source comment: basal make-up to 900 mL, autoclaving
    and cooling, then aseptic addition of separately autoclaved carbonate and glucose
    stocks. Agar 20 g/L and cooling to 50–60°C are conditional solid-medium instructions,
    not mandatory liquid-baseline ingredients or incubation conditions. No exact pH,
    autoclave temperature or duration is supplied by the available record-specific
    provider content.'
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Complex liquid baseline and unsupported metal calculation
  outcome: concern
  summary: COMPLEX/UNDEFINED and LIQUID agree with the provider baseline; the agar
    branch is explicitly conditional. high_metal:true needs a defensible source-stage
    molar derivation after correcting stock and volume scope. The large original NaCl
    mass is real provider content, so trace errors do not establish that the flag
    should be false. No organism, strain, taxonomy, assembly, DOI/PMID, growth or
    separate variant evidence is asserted.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - quantity-inventory
  - writer-0
  - writer-1
  - writer-2
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: generation
  area: provenance
  topic: Inherited flattening, numeric water merge and current ownership
  outcome: concern
  summary: The target repeats the maintained owner’s defects. Its water note explicitly
    preserves the earlier 900.0 plus 1.0 duplicate sum; those rows are different preparation
    contexts. Current TOGO stock separation and migration-copy functions, plus the
    current cleanup code’s conflict retention rather than summation, are hash-bound
    implementation context, not historical replay or authority to mutate this recipe.
  target_ids:
  - CultureMech:007539
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - writer-context-0
  - writer-context-1
  - writer-context-2
findings:
- finding_id: f1
  issue_key: culturemech.007539.stock-unit-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock composition, stock additions and solvent stages collapse into false
    concentrations
  description: Seven mg-scale trace solutes are direct g/L values; the 10 mL trace,
    100 mL carbonate and 5 mL glucose doses are encoded as g/L; and 900 mL main water
    plus 1 L stock water become 901 g/L. The provider’s 115 mL main denominator also
    conflicts with its own 900 mL stage. These combined errors prevent faithful representation
    of the named formulation.
  target_ids:
  - CultureMech:007539
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - solution4998
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  issue_key: culturemech.007539.form-and-identity-conflicts
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two explicit hydrates use unhydrated terms and one source chemical remains
    ambiguous
  description: Source CoCl2·6H2O and NiCl2·6H2O are mapped to the unhydrated CHEBI:35696
    and CHEBI:34887 formulas. Both providers also preserve H3BO4, while TOGO calls
    it Boric acid. Valid canonical labels do not resolve the hydrate mismatches or
    the provider chemical ambiguity.
  target_ids:
  - CultureMech:007539
  field_paths:
  - ingredients[8].preferred_term
  - ingredients[10].term
  - ingredients[11].term
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - chebi35696
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  issue_key: culturemech.007539.preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The source-specific stock addition sequence is absent
  description: Neither layer preserves basal make-up, autoclaving/cooling, or aseptic
    addition of separately autoclaved later stocks. Empty Unknown solution stubs do
    not encode these operational boundaries. Conditional agar and cooling text must
    remain separately scoped.
  target_ids:
  - CultureMech:007539
  field_paths:
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because the omitted source-specific
    separate sterilization and addition sequence changes stock preparation and assembly
    of the formulation; no generic cycle is proposed.
- finding_id: f4
  issue_key: culturemech.007539.high-metal-support
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The high-metal flag lacks a valid source-stage derivation
  description: high_metal:true has no attached calculation consistent with the schema’s
    molar threshold. Flattened stock quantities and a conflicted final denominator
    invalidate deriving it directly from the current values, and current analyzer
    approximations do not establish exact metal molarity. The genuine 117 g basal
    NaCl amount means this finding is not evidence for automatically setting false.
  target_ids:
  - CultureMech:007539
  field_paths:
  - high_metal
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  - writer-0
  - writer-1
  - writer-2
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  issue_key: culturemech.007539.claim-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: No scoped formulation evidence distinguishes provider content from unavailable
    primary
  description: Both layers name the sources but lack attached formulation evidence
    and references for the stock hierarchy, quantity claims and preparation. The currently
    inaccessible exact primary must not be treated as if its full recipe had been
    inspected.
  target_ids:
  - CultureMech:007539
  field_paths:
  - references
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - togoM1025
  - mediadiveJ974api
  - solution4998
  - jcm974-attempt
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconstruct source-scoped basal amounts, stock composition, stock strength
    and batch doses in maintained input after resolving the primary and denominator
    conflicts. Preserve original units and stage-specific solvent quantities; do not
    adopt the provider g_l values or invent a final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007539
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  description: Resolve the exact supplied hydrates and ambiguous boron compound against
    an authoritative recipe before choosing identifiers or molecular weights. Preserve
    conflicting source text and do not guess replacement CHEBI IDs or silently correct
    the formula.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007539
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  description: Restore the exact available provider preparation with explicit provider
    status and primary-access limit, distinguishing basal versus later-stock steps
    and optional agar conditions. Add no pH or sterilization cycle absent from the
    exact available sources.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007539
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  description: Reassess the flag using resolved source-stage quantities and exact
    chemical forms with an explicit valid molar method. Retain uncertainty until the
    final basis is established; do not infer a replacement boolean from the trace-unit
    errors alone.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007539
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
  description: Attach the exact inspected provider snippets with original timestamps
    and preserved conflicts to their narrow claims when curating. Record the actual
    primary-access limitation and resolve it before claiming primary authentication.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007539
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1025_Alkalinus_Abyssiniese_Medium.yaml
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
- The exact JCM GRMD=974 page returned HTTP 200 but says Nothing found; no primary
  formulation or collection sterilization default is available. TOGO M1025 and MediaDive
  J974 are assessed as providers, without substituting another JCM accession.
- Exact JCM 974 primary formulation remains unavailable. No collection default from
  a different JCM page is transferred.
- The 900 mL water item, 900 mL make-up instruction, later stock additions and provider
  115 mL basis are retained as distinct source statements. No measured final medium
  volume or final g/L correction is asserted.
- Stock-dose mass calculations are conditional on the explicitly declared provider
  1000 mL stock basis; they are transferred masses, not final-medium concentrations.
  No corpus-wide metal analysis was executed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-022
- generated-medium
```
