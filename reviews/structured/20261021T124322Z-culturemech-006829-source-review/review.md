# Source and formulation review: alkalibacterium_olivapovliticus (CultureMech:006829)

- Review: 20261021T124322Z-culturemech-006829-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:39:23Z
- Finished UTC: 2026-10-21T12:43:22Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSMZ 923 formulation is identifiable and all seven listed amounts agree with the source/provider basis, including the solid-medium agar condition. Five DSMZ-owner amount claims have matching attached evidence. The generated target and KOMODO owner omit essential separate-carbonate sterilization and cooling instructions; source product qualifiers, water and later owner evidence also need preservation. No unsupported glutamate stereochemical change is proposed.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 205; batch 021 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty task batches contain 200 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 203 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006829 | data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml | generated | alkalibacterium_olivapovliticus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006829 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006829 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/205/strict.tsv |
| validate-terms | passed | True | CultureMech:006829 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006829 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006829 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo923 | unavailable | False | CultureMech:006829 | The preserved exact KOMODO detail request returned HTTP 403. The identity catalog, complete DSMZ primary and exact provider formulation are available; this bounded access limit does not prevent the current formulation assessment. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006829.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:006829.

6 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 6/7 primary and 6/7 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 7: primary 85.71%; secondary 85.71%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006829.

11 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Na glutamate",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 1",
        "exact_source_quote": "Na glutamate (Sigma) 10.000 g",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na glutamate\",\n                        \"compound_id\": 839,\n                        \"attribute\": \"Sigma\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 59.1328,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Preserve source product and chemical-form scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "10 g / (1000 mL / 1000 mL per L) = 10 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "Yeast extract",
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 2",
        "exact_source_quote": "Yeast extract (Oxoid) 5.000 g",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Preserve source product and chemical-form scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "5 g / (1000 mL / 1000 mL per L) = 5 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "Na2CO3",
    "field_path": "ingredients[2].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 3",
        "exact_source_quote": "Na2CO3 10.000 g",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 94.3503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Preserve source product and chemical-form scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[2].evidence[0]"
      }
    ],
    "arithmetic": "10 g / (1000 mL / 1000 mL per L) = 10 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "K2HPO4",
    "field_path": "ingredients[3].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "0.15",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 4",
        "exact_source_quote": "K2HPO4 0.150 g",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 0.861198,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Preserve source product and chemical-form scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[3].evidence[0]"
      }
    ],
    "arithmetic": "0.15 g / (1000 mL / 1000 mL per L) = 0.15 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "MgSO4 x 7 H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "0.025",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 5",
        "exact_source_quote": "MgSO4 x 7 H2O 0.025 g",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.10143,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Preserve source product and chemical-form scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.025",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[4].evidence[0]"
      }
    ],
    "arithmetic": "0.025 g / (1000 mL / 1000 mL per L) = 0.025 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "(NH4)2SO4",
    "field_path": "ingredients[5].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 6",
        "exact_source_quote": "(NH4)2SO4 1.000 g",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 7.56773,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Preserve source product and chemical-form scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[5].evidence[0]"
      }
    ],
    "arithmetic": "1 g / (1000 mL / 1000 mL per L) = 1 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "Distilled water",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, table row 7",
        "exact_source_quote": "Distilled water 1000.000 ml",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "The primary lists 1000 mL water; all layers omit this quantity. Preserve it as source batch preparation, not water mass or proof that the primary specifies adjustment to a final litre.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "We recommend that liquid media be made by autoclaving the Na2CO3 separately, otherwise the high pH will cause ammonia to be lost. When making media solidified with agar (20 g/l) the agar should also not be autoclaved with the Na2CO3 otherwise the agar will be hydrolysed. When mixing the ingredients for solid media cool all components to about 55°C otherwise hydrolysis of the agar may occur."
          }
        ],
        "decision": "add"
      }
    ],
    "arithmetic": "1000 mL = 1 L of listed water; no density or measured final volume is inferred.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "Agar",
    "field_path": "ingredients[6].concentration",
    "decision": "evidence_only",
    "local": {
      "value": "20",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz923",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf",
        "source_locator": "DSMZ 923 page 1, preparation paragraph, solid branch",
        "exact_source_quote": "agar (20 g/l)",
        "snapshot_sha256": "d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457",
        "parsed_text_sha256": "9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c"
      },
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Supported amount/unit on the provider nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments are verified; other layers need claim evidence. Agar applies to the explicitly selected SOLID_AGAR branch; preserve the source condition.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "verified",
        "attached_evidence_path": "ingredients[6].evidence[0]"
      }
    ],
    "arithmetic": "20 g / (1000 mL / 1000 mL per L) = 20 g/L on the provider basis; this is not a measured final-volume claim.",
    "primary_source_evidence_id": "dsmz923"
  },
  {
    "ingredient_or_context": "Provider nominal main volume",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607"
      }
    ],
    "rationale": "Retain the separately attributed nominal provider volume supporting g_l; the primary lists water rather than a make-up-to-volume instruction.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "We recommend that liquid media be made by autoclaving the Na2CO3 separately, otherwise the high pH will cause ammonia to be lost. When making media solidified with agar (20 g/l) the agar should also not be autoclaved with the Na2CO3 otherwise the agar will be hydrolysed. When mixing the ingredients for solid media cool all components to about 55°C otherwise hydrolysis of the agar may occur."
          }
        ],
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solid-branch agar in preparation",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "agar (20 g/l)",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607",
        "parsed_text_sha256": "6c71a3152cc325c9ee5afb1ac1c1fd65dcc022b501b7c0379c1290cf240463ea"
      }
    ],
    "rationale": "The complete DSMZ-owner step preserves this literal value and stage but lacks matching preparation evidence. Target and KOMODO owner omit the step. The 55°C value is cooling before mixing, not an autoclave cycle or incubation temperature.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "We recommend that liquid media be made by autoclaving the Na2CO3 separately, otherwise the high pH will cause ammonia to be lost. When making media solidified with agar (20 g/l) the agar should also not be autoclaved with the Na2CO3 otherwise the agar will be hydrolysed. When mixing the ingredients for solid media cool all components to about 55°C otherwise hydrolysis of the agar may occur.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Cooling before combining components",
    "field_path": "preparation_steps",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive923api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/923",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "about 55°C",
        "snapshot_sha256": "449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607",
        "parsed_text_sha256": "6c71a3152cc325c9ee5afb1ac1c1fd65dcc022b501b7c0379c1290cf240463ea"
      }
    ],
    "rationale": "The complete DSMZ-owner step preserves this literal value and stage but lacks matching preparation evidence. Target and KOMODO owner omit the step. The 55°C value is cooling before mixing, not an autoclave cycle or incubation temperature.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "We recommend that liquid media be made by autoclaving the Na2CO3 separately, otherwise the high pH will cause ammonia to be lost. When making media solidified with agar (20 g/l) the agar should also not be autoclaved with the Na2CO3 otherwise the agar will be hydrolysed. When mixing the ingredients for solid media cool all components to about 55°C otherwise hydrolysis of the agar may occur.",
        "decision": "evidence_only"
      }
    ]
  }
]

### Exact source and reciprocal maintained records

identity: supported. Targets: CultureMech:006829.

KOMODO 923, DSMZ 923 and MediaDive medium 923 identify the same named source accession. The actual two maintained contributors and reciprocal SOURCE_DUPLICATE paths/IDs resolve. Their ingredient objects agree apart from attached evidence; their preparation, reference and history content differs, so matching signatures do not prove lossless whole-record equivalence.

### Every amount and declared basis

consistency: supported. Targets: CultureMech:006829.

Six source masses are 10, 5, 10, 0.15, 0.025 and 1 g with 1000 mL listed water. The solid branch adds agar 20 g/L and is explicitly selected by the local physical_state and agar condition. All seven stored g/L values match the provider nominal 1000 mL basis. Five DSMZ-owner quantities are verified with matching evidence; the remaining owner quantities and all target quantities are evidence_only. No stock concentration, dosing volume or measured final volume is invented.

### Source chemical forms and supplier qualifiers

grounding: supported. Targets: CultureMech:006829.

CHEBI:64220 is generic monosodium glutamate: its definition, formula and structures have no specified D/L stereochemistry. Generic source Na glutamate supports that scope; there is no basis for a stereochemical replacement. The explicitly supplied magnesium sulfate heptahydrate and other source salts match their asserted forms. The missing Sigma and Oxoid qualifiers are source traceability gaps, not proof that a different chemical or yeast product was used. Yeast extract remains an ungrounded mixture; no pure-molecule ID is invented.

### Separate sterilization and component cooling

completeness: concern. Targets: CultureMech:006829.

The DSMZ owner preserves the full source paragraph, but target and KOMODO owner omit it. Carbonate must be autoclaved separately to prevent ammonia loss; agar must not be autoclaved with carbonate, and components are cooled to about 55°C before combination to avoid agar hydrolysis. This source-specific sequence has a stated formulation consequence. The primary provides no exact sterilization cycle, gas composition or numeric pH, so none is inferred.

### Selected solid branch and biological scope

scope: supported. Targets: CultureMech:006829.

COMPLEX/UNDEFINED is consistent with yeast extract and agar; SOLID_AGAR denotes the explicit 20 g/L agar branch while the source also describes a liquid branch. No target organism, taxon/strain accession, assembly, DOI/PMID or paper-derived growth/variant claim is asserted. The medium title and cultivation application do not establish growth. Aerobic: No is attributable to the exact catalog flag, not primary experimental evidence.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006829.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Later owner evidence versus generated content

provenance: concern. Targets: CultureMech:006829.

Current importer/resolver/merge excerpts are hash-bound context, not a historical replay. The DSMZ owner has later October source evidence and a reference; the August-generated target retains the ingredient values but omits those additions and the owner preparation. Current formulation merging requires compatible complete formulation content and unions evidence; a prior ingredient fingerprint does not validate the stale output.

## Findings

### f1: Essential separate sterilization and cooling instructions are absent

major / open / confirmed; issue key: culturemech.006829.preparation-loss.

The target and KOMODO owner omit the complete preparation paragraph retained by the DSMZ owner and primary. The source explicitly links joint carbonate autoclaving to ammonia loss and agar hydrolysis, and specifies cooling to about 55°C before combining solid-medium components. The omission therefore affects reproducing the selected formulation.

### f2: Listed water and supplier qualifiers are omitted

minor / open / confirmed; issue key: culturemech.006829.source-qualifiers.

All layers omit the source 1000 mL distilled-water quantity and the Sigma sodium-glutamate/Oxoid yeast-extract qualifiers. The supported masses remain unchanged; a generic name does not preserve the source product provenance or its batch preparation context.

### f3: The generated target lacks five verified owner amount excerpts

minor / open / confirmed; issue key: culturemech.006829.generated-evidence-loss.

The DSMZ owner has five matching amount snippets, exact source hash and bounded explanation, plus a provider reference. Target and KOMODO owner lack these attachments. Amount agreement is supported externally but must not be described as already evidenced in every layer.

### f4: Inherited import timestamps contain malformed and timezone-naive values

minor / open / confirmed; issue key: culturemech.006829.history-timezones.

The target and KOMODO owner each retain the malformed 2026-01-27T01:15:03.fZ import timestamp and timezone-naive 2026-02-03 resolver timestamp. These four instances limit historical timing, without invalidating the current source comparison.

## Recommended Actions And Acceptance Checks

### a1

Preserve the source-specific carbonate/agar sterilization separation and cooling stage in the maintained inputs before authorized regeneration. Retain the DSMZ-owner text and add scoped evidence; do not invent an unspecified sterilization temperature, duration or pH.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore the exact supplier qualifiers and source water quantity at their intended scope with evidence. Keep water volume separate from provider nominal volume; do not add an unsupported product code, stereochemistry or final-volume claim.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the five verified owner claims and their limits when regeneration is authorized; add narrow evidence for the remaining supported amounts rather than treating one recipe citation as evidence for all fields.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Keep historical events intact and append an authorized dated clarification if reliable timing evidence is available. Do not silently infer a timezone or rewrite provenance.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch021/205/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/205/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml:1:id: CultureMech:006829<br>./data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml:1:id: CultureMech:006829<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch021/source-preflight-bound/205/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 10 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch021/source-preflight-bound/205/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| dsmz923 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf; Entire official page 1 table and preparation paragraph; page image independently inspected | supports | The primary gives six basal ingredient masses, 1000 mL water, solid-branch agar 20 g/L, separate carbonate autoclaving and mixing near 55°C. No numeric pH, autoclave temperature or duration is supplied. |
| mediadive923 | https://mediadive.dsmz.de/rest/medium/923; Complete $.data.medium and $.data.solutions[0], including eight recipe rows and preparation | supports | Exact main solution 1898 preserves Sigma/Oxoid qualifiers and the solid agar condition. Its 1000 mL declared volume supports nominal g_l calculations, not independently measured final volume. |
| komodo-list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Header and exact ID 923 table row | supports | The catalog maps KOMODO 923 to DSMZ 923 and gives null pH, complex=true and aerobic=false. These are attributed catalog fields, not experimentally established culture requirements. |
| komodo923-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=923; Preserved exact public retrieval result | context_only | The preserved exact KOMODO detail request returned HTTP 403. The identity catalog, complete DSMZ primary and exact provider formulation are available; this bounded access limit does not prevent the current formulation assessment. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi64220 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:64220 resolves to monosodium glutamate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64220": [{"label": "Na glutamate", "match_type": "preferred_term", "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id": "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| attached-evidence-recheck | /private/tmp/culturemech-review-work-batch021/205/attached-evidence-recheck.json; Every existing ingredient evidence object, full reference/snippet/explanation and source locator | supports | 5 attached amount claims match the exact captured source rows and nominal provider basis. Verification applies only in the documented owner layers. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch021/205/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch021/205/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-3 | src/culturemech/enrich/dsmz_resolver.py; _build_dsmz_index lines 43–76; merge_composition lines 112–166; _add_enrichment_metadata lines 195–212 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:16.271419"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:16.271419"}]}, {"input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml", "events": 7, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved exact KOMODO detail request returned HTTP 403. The identity catalog, complete DSMZ primary and exact provider formulation are available; this bounded access limit does not prevent the current formulation assessment.
- No numeric pH, autoclave duration/temperature or experimentally measured final volume is supplied by the exact primary. Source-specific missing preparation is assessed without filling these unknowns.
- Current exact API bytes authenticate the five stored snippets/hashes, not the recorded historical access date. Ontology cross-references were not promoted to culture citations.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124322Z-culturemech-006829-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkalibacterium_olivapovliticus (CultureMech:006829)'
started_at: '2026-10-21T12:39:23Z'
finished_at: '2026-10-21T12:43:22Z'
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
summary: The exact DSMZ 923 formulation is identifiable and all seven listed amounts
  agree with the source/provider basis, including the solid-medium agar condition.
  Five DSMZ-owner amount claims have matching attached evidence. The generated target
  and KOMODO owner omit essential separate-carbonate sterilization and cooling instructions;
  source product qualifiers, water and later owner evidence also need preservation.
  No unsupported glutamate stereochemical change is proposed.
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
  - path: data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    sha256: 84d89a83c3e0d7bf62a3ebca0b09bcca5b2082ff45bfc0664f78cecc63494457
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    sha256: 6f5d460d50cc7ec458dff98ddc564570bb965e38e9783af1ce13472035968194
    role: context
  - path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
    sha256: de6149e72d5a7b10e2551aaf039f6eaf414b32b7b4d66d66b95f11091615e839
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
  selection: Task review 205; batch 021 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty task batches contain
    200 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 203 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006829
targets:
- target_id: CultureMech:006829
  path: data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  label: alkalibacterium_olivapovliticus
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/205/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/205/strict.tsv"
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006829
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
  - CultureMech:006829
- check_id: komodo923-source-access
  name: 'Exact source content access: komodo923'
  required: false
  status: unavailable
  summary: The preserved exact KOMODO detail request returned HTTP 403. The identity
    catalog, complete DSMZ primary and exact provider formulation are available; this
    bounded access limit does not prevent the current formulation assessment.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - komodo923-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:22.721846Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/205/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:24.338096Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/205/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:26.196789Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:27.346140Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:43:21Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml:1:id: CultureMech:006829

    ./data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml:1:id:
    CultureMech:006829

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/source-preflight-bound/205/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:43:21Z'
  support: supports
  summary: 10 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2f277bbb26611d63f833756809df3f04e3bb04fa638a40fde005f0f1486a2c7b
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/source-preflight-bound/205/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: f01f51390604365fee63d2ca5c815a45fa948faccac4975a58925092b88126f9
- evidence_id: dsmz923
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf
  locator: Entire official page 1 table and preparation paragraph; page image independently
    inspected
  accessed_at: '2026-10-21T12:23:18.739949Z'
  support: supports
  summary: The primary gives six basal ingredient masses, 1000 mL water, solid-branch
    agar 20 g/L, separate carbonate autoclaving and mixing near 55°C. No numeric pH,
    autoclave temperature or duration is supplied.
  snapshot_sha256: d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457
- evidence_id: mediadive923
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/923
  locator: Complete $.data.medium and $.data.solutions[0], including eight recipe
    rows and preparation
  accessed_at: '2026-10-21T12:23:16.951729Z'
  support: supports
  summary: Exact main solution 1898 preserves Sigma/Oxoid qualifiers and the solid
    agar condition. Its 1000 mL declared volume supports nominal g_l calculations,
    not independently measured final volume.
  snapshot_sha256: 449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607
- evidence_id: komodo-list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Header and exact ID 923 table row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The catalog maps KOMODO 923 to DSMZ 923 and gives null pH, complex=true
    and aerobic=false. These are attributed catalog fields, not experimentally established
    culture requirements.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo923-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=923
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:23:16.872873Z'
  support: context_only
  summary: The preserved exact KOMODO detail request returned HTTP 403. The identity
    catalog, complete DSMZ primary and exact provider formulation are available; this
    bounded access limit does not prevent the current formulation assessment.
  snapshot_sha256: 2d846b0a566367eb2a46bf7d5b97e0af16ad81bc5c8c96478d4b8c80524cb2e6
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
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to agar. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
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
- evidence_id: chebi62946
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:02.566401Z'
  support: supports
  summary: CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi64220
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64220
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:49:18.590575Z'
  support: supports
  summary: CHEBI:64220 resolves to monosodium glutamate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f365c8a94dc3b7bb63e10235e8728f2333b34fb60943ea59c357ebd3456fb25b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:43:21Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term",
    "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label":
    "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:64220": [{"label": "Na glutamate", "match_type": "preferred_term",
    "identifier": "CHEBI:64220", "preferred_term": "Na glutamate", "ontology_id":
    "CHEBI:64220", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: attached-evidence-recheck
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/205/attached-evidence-recheck.json
  locator: Every existing ingredient evidence object, full reference/snippet/explanation
    and source locator
  accessed_at: '2026-10-21T12:43:21Z'
  support: supports
  summary: 5 attached amount claims match the exact captured source rows and nominal
    provider basis. Verification applies only in the documented owner layers.
  snapshot_sha256: 0d262791403961f38512d50784ad52de8dee201648763ce69f7d55c710a02863
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/205/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: f3fa6675054e53199ac4d411295ac9e010e76cd9f4f78100ea58882a0fac3d82
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/205/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 0482a547b1578dfaaf79fa035a551e8ab1c1488bc1dc4acd30320da076c14912
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T12:43:21Z'
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
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-context-3
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: _build_dsmz_index lines 43–76; merge_composition lines 112–166; _add_enrichment_metadata
    lines 195–212
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml; data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml;
    data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:43:21Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:16.271419"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:16.271419"}]}, {"input": "data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml",
    "events": 7, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '6 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 6/7 primary and 6/7 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi2509
  - chebi29377
  - chebi31795
  - chebi62946
  - chebi64220
  details: 'Instance coverage on a 0–100 percent scale, denominator 7: primary 85.71%;
    secondary 85.71%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 11 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Na glutamate\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz923\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 1\",\n        \"exact_source_quote\"\
    : \"Na glutamate (Sigma) 10.000 g\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na glutamate\\\",\\n                        \\\"compound_id\\\
    \": 839,\\n                        \\\"attribute\\\": \\\"Sigma\\\",\\n      \
    \                  \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                   \
    \     \\\"mmol_l\\\": 59.1328,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"Supported amount/unit on the provider\
    \ nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments\
    \ are verified; other layers need claim evidence. Preserve source product and\
    \ chemical-form scope.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\",\n \
    \       \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"10 g / (1000 mL / 1000 mL per L) = 10 g/L on the provider basis; this is not\
    \ a measured final-volume claim.\",\n    \"primary_source_evidence_id\": \"dsmz923\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Yeast extract\",\n    \"field_path\"\
    : \"ingredients[1].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"5\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz923\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 2\",\n        \"exact_source_quote\"\
    : \"Yeast extract (Oxoid) 5.000 g\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"Oxoid\\\",\\n       \
    \                 \\\"amount\\\": 5,\\n                        \\\"unit\\\": \\\
    \"g\\\",\\n                        \\\"g_l\\\": 5,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\n      }\n\
    \    ],\n    \"rationale\": \"Supported amount/unit on the provider nominal main-recipe\
    \ basis. Only the five matching existing DSMZ-owner attachments are verified;\
    \ other layers need claim evidence. Preserve source product and chemical-form\
    \ scope.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\",\n \
    \       \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"5 g / (1000 mL / 1000 mL per L) = 5 g/L on the provider basis; this is not\
    \ a measured final-volume claim.\",\n    \"primary_source_evidence_id\": \"dsmz923\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Na2CO3\",\n    \"field_path\": \"\
    ingredients[2].concentration\",\n    \"decision\": \"evidence_only\",\n    \"\
    local\": {\n      \"value\": \"10\",\n      \"unit\": \"G_PER_L\"\n    },\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz923\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 3\",\n        \"exact_source_quote\"\
    : \"Na2CO3 10.000 g\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"amount\\\": 10,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                 \
    \       \\\"mmol_l\\\": 94.3503,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"Supported amount/unit on the provider\
    \ nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments\
    \ are verified; other layers need claim evidence. Preserve source product and\
    \ chemical-form scope.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\",\n \
    \       \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[2].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"10 g / (1000 mL / 1000 mL per L) = 10\
    \ g/L on the provider basis; this is not a measured final-volume claim.\",\n \
    \   \"primary_source_evidence_id\": \"dsmz923\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"K2HPO4\",\n    \"field_path\": \"ingredients[3].concentration\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": {\n      \"value\": \"0.15\",\n      \"unit\"\
    : \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz923\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 4\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.150 g\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.15,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.15,\\n         \
    \               \\\"mmol_l\\\": 0.861198,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"Supported amount/unit on the provider\
    \ nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments\
    \ are verified; other layers need claim evidence. Preserve source product and\
    \ chemical-form scope.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\",\n \
    \       \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[3].evidence[0]\"\n      }\n    ],\n    \"arithmetic\": \"0.15\
    \ g / (1000 mL / 1000 mL per L) = 0.15 g/L on the provider basis; this is not\
    \ a measured final-volume claim.\",\n    \"primary_source_evidence_id\": \"dsmz923\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"MgSO4 x 7 H2O\",\n    \"field_path\"\
    : \"ingredients[4].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"0.025\",\n      \"unit\": \"G_PER_L\"\n  \
    \  },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz923\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 5\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.025 g\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.025,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.025,\\\
    n                        \\\"mmol_l\\\": 0.10143,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\n      }\n\
    \    ],\n    \"rationale\": \"Supported amount/unit on the provider nominal main-recipe\
    \ basis. Only the five matching existing DSMZ-owner attachments are verified;\
    \ other layers need claim evidence. Preserve source product and chemical-form\
    \ scope.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.025\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.025\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"verified\",\n        \"attached_evidence_path\"\
    : \"ingredients[4].evidence[0]\"\n      }\n    ],\n    \"arithmetic\": \"0.025\
    \ g / (1000 mL / 1000 mL per L) = 0.025 g/L on the provider basis; this is not\
    \ a measured final-volume claim.\",\n    \"primary_source_evidence_id\": \"dsmz923\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"(NH4)2SO4\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz923\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 6\",\n        \"exact_source_quote\"\
    : \"(NH4)2SO4 1.000 g\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"(NH4)2SO4\\\",\\n                        \\\"compound_id\\\"\
    : 27,\\n                        \\\"amount\\\": 1,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n          \
    \              \\\"mmol_l\\\": 7.56773,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"Supported amount/unit on the provider\
    \ nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments\
    \ are verified; other layers need claim evidence. Preserve source product and\
    \ chemical-form scope.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\",\n \
    \       \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[5].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"1 g / (1000 mL / 1000 mL per L) = 1 g/L\
    \ on the provider basis; this is not a measured final-volume claim.\",\n    \"\
    primary_source_evidence_id\": \"dsmz923\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Distilled water\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz923\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, table row 7\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.000 ml\",\n        \"snapshot_sha256\": \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\"\
    ,\n        \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"The primary lists 1000 mL water; all layers\
    \ omit this quantity. Preserve it as source batch preparation, not water mass\
    \ or proof that the primary specifies adjustment to a final litre.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"We recommend that liquid media be made by autoclaving\
    \ the Na2CO3 separately, otherwise the high pH will cause ammonia to be lost.\
    \ When making media solidified with agar (20 g/l) the agar should also not be\
    \ autoclaved with the Na2CO3 otherwise the agar will be hydrolysed. When mixing\
    \ the ingredients for solid media cool all components to about 55°C otherwise\
    \ hydrolysis of the agar may occur.\"\n          }\n        ],\n        \"decision\"\
    : \"add\"\n      }\n    ],\n    \"arithmetic\": \"1000 mL = 1 L of listed water;\
    \ no density or measured final volume is inferred.\",\n    \"primary_source_evidence_id\"\
    : \"dsmz923\"\n  },\n  {\n    \"ingredient_or_context\": \"Agar\",\n    \"field_path\"\
    : \"ingredients[6].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": {\n      \"value\": \"20\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz923\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium923.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 923 page 1, preparation paragraph, solid\
    \ branch\",\n        \"exact_source_quote\": \"agar (20 g/l)\",\n        \"snapshot_sha256\"\
    : \"d8294b41c20c59e9de6a618d0925831656d95417b11eb8e4ab0bad22d512c457\",\n    \
    \    \"parsed_text_sha256\": \"9adca41843247eaba33264237a141334f7a870ae65399f03989d567523c7337c\"\
    \n      },\n      {\n        \"source_key\": \"mediadive923api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"condition\\\": \\\"for solid medium\\\",\\n     \
    \                   \\\"amount\\\": 20,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n                   \
    \     \\\"mmol_l\\\": 59.4654,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"Supported amount/unit on the provider\
    \ nominal main-recipe basis. Only the five matching existing DSMZ-owner attachments\
    \ are verified; other layers need claim evidence. Agar applies to the explicitly\
    \ selected SOLID_AGAR branch; preserve the source condition.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\",\n \
    \       \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\",\n        \"attached_evidence_path\": \"ingredients[6].evidence[0]\"\
    \n      }\n    ],\n    \"arithmetic\": \"20 g / (1000 mL / 1000 mL per L) = 20\
    \ g/L on the provider basis; this is not a measured final-volume claim.\",\n \
    \   \"primary_source_evidence_id\": \"dsmz923\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Provider nominal main volume\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive923api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1000\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the separately attributed nominal\
    \ provider volume supporting g_l; the primary lists water rather than a make-up-to-volume\
    \ instruction.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"We recommend that liquid media be made by autoclaving\
    \ the Na2CO3 separately, otherwise the high pH will cause ammonia to be lost.\
    \ When making media solidified with agar (20 g/l) the agar should also not be\
    \ autoclaved with the Na2CO3 otherwise the agar will be hydrolysed. When mixing\
    \ the ingredients for solid media cool all components to about 55°C otherwise\
    \ hydrolysis of the agar may occur.\"\n          }\n        ],\n        \"decision\"\
    : \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Solid-branch\
    \ agar in preparation\",\n    \"field_path\": \"preparation_steps\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive923api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/923\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].steps[0].step\",\n      \
    \  \"exact_source_quote\": \"agar (20 g/l)\",\n        \"snapshot_sha256\": \"\
    449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\",\n        \"\
    parsed_text_sha256\": \"6c71a3152cc325c9ee5afb1ac1c1fd65dcc022b501b7c0379c1290cf240463ea\"\
    \n      }\n    ],\n    \"rationale\": \"The complete DSMZ-owner step preserves\
    \ this literal value and stage but lacks matching preparation evidence. Target\
    \ and KOMODO owner omit the step. The 55°C value is cooling before mixing, not\
    \ an autoclave cycle or incubation temperature.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"preparation_steps\",\n       \
    \ \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"We recommend that liquid media be made by autoclaving the Na2CO3 separately,\
    \ otherwise the high pH will cause ammonia to be lost. When making media solidified\
    \ with agar (20 g/l) the agar should also not be autoclaved with the Na2CO3 otherwise\
    \ the agar will be hydrolysed. When mixing the ingredients for solid media cool\
    \ all components to about 55°C otherwise hydrolysis of the agar may occur.\",\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Cooling before combining components\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive923api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/923\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"about\
    \ 55°C\",\n        \"snapshot_sha256\": \"449972d7abc5dc2360c354d4429532e25145667319a3558b54764a4946cc2607\"\
    ,\n        \"parsed_text_sha256\": \"6c71a3152cc325c9ee5afb1ac1c1fd65dcc022b501b7c0379c1290cf240463ea\"\
    \n      }\n    ],\n    \"rationale\": \"The complete DSMZ-owner step preserves\
    \ this literal value and stage but lacks matching preparation evidence. Target\
    \ and KOMODO owner omit the step. The 55°C value is cooling before mixing, not\
    \ an autoclave cycle or incubation temperature.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"preparation_steps\",\n       \
    \ \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"We recommend that liquid media be made by autoclaving the Na2CO3 separately,\
    \ otherwise the high pH will cause ammonia to be lost. When making media solidified\
    \ with agar (20 g/l) the agar should also not be autoclaved with the Na2CO3 otherwise\
    \ the agar will be hydrolysed. When mixing the ingredients for solid media cool\
    \ all components to about 55°C otherwise hydrolysis of the agar may occur.\",\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact source and reciprocal maintained records
  outcome: supported
  summary: KOMODO 923, DSMZ 923 and MediaDive medium 923 identify the same named source
    accession. The actual two maintained contributors and reciprocal SOURCE_DUPLICATE
    paths/IDs resolve. Their ingredient objects agree apart from attached evidence;
    their preparation, reference and history content differs, so matching signatures
    do not prove lossless whole-record equivalence.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - komodo-list
  - dsmz923
  - mediadive923
- assessment_id: source-stage-consistency
  area: consistency
  topic: Every amount and declared basis
  outcome: supported
  summary: Six source masses are 10, 5, 10, 0.15, 0.025 and 1 g with 1000 mL listed
    water. The solid branch adds agar 20 g/L and is explicitly selected by the local
    physical_state and agar condition. All seven stored g/L values match the provider
    nominal 1000 mL basis. Five DSMZ-owner quantities are verified with matching evidence;
    the remaining owner quantities and all target quantities are evidence_only. No
    stock concentration, dosing volume or measured final volume is invented.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - quantity-inventory
  - quantity-local-fields
  - attached-evidence-recheck
  - dsmz923
  - mediadive923
- assessment_id: forms
  area: grounding
  topic: Source chemical forms and supplier qualifiers
  outcome: supported
  summary: 'CHEBI:64220 is generic monosodium glutamate: its definition, formula and
    structures have no specified D/L stereochemistry. Generic source Na glutamate
    supports that scope; there is no basis for a stereochemical replacement. The explicitly
    supplied magnesium sulfate heptahydrate and other source salts match their asserted
    forms. The missing Sigma and Oxoid qualifiers are source traceability gaps, not
    proof that a different chemical or yeast product was used. Yeast extract remains
    an ungrounded mixture; no pure-molecule ID is invented.'
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz923
  - mediadive923
  - chebi64220
  - chebi31795
- assessment_id: preparation
  area: completeness
  topic: Separate sterilization and component cooling
  outcome: concern
  summary: The DSMZ owner preserves the full source paragraph, but target and KOMODO
    owner omit it. Carbonate must be autoclaved separately to prevent ammonia loss;
    agar must not be autoclaved with carbonate, and components are cooled to about
    55°C before combination to avoid agar hydrolysis. This source-specific sequence
    has a stated formulation consequence. The primary provides no exact sterilization
    cycle, gas composition or numeric pH, so none is inferred.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz923
  - mediadive923
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Selected solid branch and biological scope
  outcome: supported
  summary: 'COMPLEX/UNDEFINED is consistent with yeast extract and agar; SOLID_AGAR
    denotes the explicit 20 g/L agar branch while the source also describes a liquid
    branch. No target organism, taxon/strain accession, assembly, DOI/PMID or paper-derived
    growth/variant claim is asserted. The medium title and cultivation application
    do not establish growth. Aerobic: No is attributable to the exact catalog flag,
    not primary experimental evidence.'
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz923
  - komodo-list
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: generation
  area: provenance
  topic: Later owner evidence versus generated content
  outcome: concern
  summary: Current importer/resolver/merge excerpts are hash-bound context, not a
    historical replay. The DSMZ owner has later October source evidence and a reference;
    the August-generated target retains the ingredient values but omits those additions
    and the owner preparation. Current formulation merging requires compatible complete
    formulation content and unions evidence; a prior ingredient fingerprint does not
    validate the stale output.
  target_ids:
  - CultureMech:006829
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - attached-evidence-recheck
  - history-metadata
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - writer-context-3
findings:
- finding_id: f1
  issue_key: culturemech.006829.preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Essential separate sterilization and cooling instructions are absent
  description: The target and KOMODO owner omit the complete preparation paragraph
    retained by the DSMZ owner and primary. The source explicitly links joint carbonate
    autoclaving to ammonia loss and agar hydrolysis, and specifies cooling to about
    55°C before combining solid-medium components. The omission therefore affects
    reproducing the selected formulation.
  target_ids:
  - CultureMech:006829
  field_paths:
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz923
  - mediadive923
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because the exact primary describes
    ammonia loss and agar hydrolysis if the missing preparation sequence is not followed;
    this is a concrete formulation impact rather than a generic missing-cycle suggestion.
- finding_id: f2
  issue_key: culturemech.006829.source-qualifiers
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Listed water and supplier qualifiers are omitted
  description: All layers omit the source 1000 mL distilled-water quantity and the
    Sigma sodium-glutamate/Oxoid yeast-extract qualifiers. The supported masses remain
    unchanged; a generic name does not preserve the source product provenance or its
    batch preparation context.
  target_ids:
  - CultureMech:006829
  field_paths:
  - ingredients[0]
  - ingredients[1]
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz923
  - mediadive923
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.006829.generated-evidence-loss
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The generated target lacks five verified owner amount excerpts
  description: The DSMZ owner has five matching amount snippets, exact source hash
    and bounded explanation, plus a provider reference. Target and KOMODO owner lack
    these attachments. Amount agreement is supported externally but must not be described
    as already evidenced in every layer.
  target_ids:
  - CultureMech:006829
  field_paths:
  - ingredients
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - attached-evidence-recheck
  - mediadive923
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: culturemech.006829.history-timezones
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Inherited import timestamps contain malformed and timezone-naive values
  description: The target and KOMODO owner each retain the malformed 2026-01-27T01:15:03.fZ
    import timestamp and timezone-naive 2026-02-03 resolver timestamp. These four
    instances limit historical timing, without invalidating the current source comparison.
  target_ids:
  - CultureMech:006829
  field_paths:
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.4
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Preserve the source-specific carbonate/agar sterilization separation
    and cooling stage in the maintained inputs before authorized regeneration. Retain
    the DSMZ-owner text and add scoped evidence; do not invent an unspecified sterilization
    temperature, duration or pH.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006829
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
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
  description: Restore the exact supplier qualifiers and source water quantity at
    their intended scope with evidence. Keep water volume separate from provider nominal
    volume; do not add an unsupported product code, stereochemistry or final-volume
    claim.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006829
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
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
  description: Preserve the five verified owner claims and their limits when regeneration
    is authorized; add narrow evidence for the remaining supported amounts rather
    than treating one recipe citation as evidence for all fields.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006829
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
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
  description: Keep historical events intact and append an authorized dated clarification
    if reliable timing evidence is available. Do not silently infer a timezone or
    rewrite provenance.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006829
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml
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
- The preserved exact KOMODO detail request returned HTTP 403. The identity catalog,
  complete DSMZ primary and exact provider formulation are available; this bounded
  access limit does not prevent the current formulation assessment.
- No numeric pH, autoclave duration/temperature or experimentally measured final volume
  is supplied by the exact primary. Source-specific missing preparation is assessed
  without filling these unknowns.
- Current exact API bytes authenticate the five stored snippets/hashes, not the recorded
  historical access date. Ontology cross-references were not promoted to culture citations.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-021
- generated-medium
```
