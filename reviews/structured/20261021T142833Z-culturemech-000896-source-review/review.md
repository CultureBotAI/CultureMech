# Source and formulation review: alteromonas_medium (CultureMech:000896)

- Review: 20261021T142833Z-culturemech-000896-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:22:36Z
- Finished UTC: 2026-10-21T14:28:33Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The 15-ingredient DSMZ 1434 record exposes seven trace-stock concentrations and the B12-stock concentration as final medium g/L. The primary itself gives conflicting B12 quantities: 0.1 mg in its table versus 1 mL of 0.1 mg/100 mL stock in its instructions. Main salts and required agar agree on the provider nominal basis; methanol is a provider mass conversion of a literal volume. Preparation retains the key conditions, but its single filtration action overstates the base-medium sterilization method.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 242; batch 025 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-four task batches contain 240 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 243 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000896 | data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml | generated | alteromonas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000896 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000896 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/242/strict.tsv |
| validate-terms | passed | True | CultureMech:000896 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000896 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000896 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000896.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:000896.

15 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 15/15 primary and 15/15 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 15: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000896.

30 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main sol. 1434 / (NH4)2SO4",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 15.1355,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " (NH4)2SO4                                                                     2.0         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The main amount agrees with the provider nominal 1 L basis and lacks attached evidence. Preserve the source literal amount and required agar without inferring a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs; this is not measured final volume or a replacement denominator."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / K2HPO4",
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 11.4826,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " K2HPO4                                                                        2.0         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The main amount agrees with the provider nominal 1 L basis and lacks attached evidence. Preserve the source literal amount and required agar without inferring a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs; this is not measured final volume or a replacement denominator."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / KH2PO4",
    "field_path": "ingredients[2].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 7.34835,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " KH2PO4                                                                        1.0         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The main amount agrees with the provider nominal 1 L basis and lacks attached evidence. Preserve the source literal amount and required agar without inferring a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs; this is not measured final volume or a replacement denominator."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / NaCl",
    "field_path": "ingredients[3].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 342.231,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " NaCl                                                                         20.0         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The main amount agrees with the provider nominal 1 L basis and lacks attached evidence. Preserve the source literal amount and required agar without inferring a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs; this is not measured final volume or a replacement denominator."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / MgSO4 x 7 H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.21716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " MgSO4 x 7 H2O                                                                 0.3         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The main amount agrees with the provider nominal 1 L basis and lacks attached evidence. Preserve the source literal amount and required agar without inferring a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs; this is not measured final volume or a replacement denominator."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / Vitamin B12 solution 0.001 g/L",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Vitamin B12 solution 0.001 g/L\",\n                        \"solution_id\": 2936,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": "1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml)",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "This source stock receiving dose or solvent quantity is absent from structured local scope; restore the exact amount within the intended stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1434 / Trace elements",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace elements\",\n                        \"solution_id\": 2935,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " Trace elements (see below)                                                    1.0       ml",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "This source stock receiving dose or solvent quantity is absent from structured local scope; restore the exact amount within the intended stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1434 / Methanol",
    "field_path": "ingredients[5].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Methanol\",\n                        \"compound_id\": 226,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 7.92,\n                        \"mmol_l\": 247.176,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " Methanol                                                                     10.0       ml",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "Source methanol is 10 mL per liter; local 7.92 g/L agrees with the provider conversion only. Preserve the literal volume, source-per-liter wording and conversion provenance; density/temperature were not independently established.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "7.92",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "7.92",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "7.92 g per 10 mL implies provider density 0.792 g/mL. This is a description of its conversion, not independent physical verification."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / Agar",
    "field_path": "ingredients[6].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " Agar                                                                         15.0         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The main amount agrees with the provider nominal 1 L basis and lacks attached evidence. Preserve the source literal amount and required agar without inferring a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs; this is not measured final volume or a replacement denominator."
  },
  {
    "ingredient_or_context": "Main sol. 1434 / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main sol. 1434: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " Distilled water                                                           1000.0        ml",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "This source stock receiving dose or solvent quantity is absent from structured local scope; restore the exact amount within the intended stage.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Trace elements / MnSO4 x H2O",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 760,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.76,\n                        \"mmol_l\": 4.49662,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " MnSO4 x H2O                                                                76.00        mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.76",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.76",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 760 mg is ten times the corresponding primary input. On the provider nominal stock basis, 0.76 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / CuSO4 x 5 H2O",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 250,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.00126,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " CuSO4 x 5 H2O                                                              25.00        mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 250 mg is ten times the corresponding primary input. On the provider nominal stock basis, 0.25 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / FeSO4 x 7 H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 280,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.28,\n                        \"mmol_l\": 1.00714,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " FeSO4 x 7 H2O                                                              28.00        mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.28",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.28",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 280 mg is ten times the corresponding primary input. On the provider nominal stock basis, 0.28 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / ZnSO4 x 7 H2O",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 1.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.4,\n                        \"mmol_l\": 4.86853,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " ZnSO4 x 7 H2O                                                                0.14         g",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.4",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.4",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 1.4 g is ten times the corresponding primary input. On the provider nominal stock basis, 1.4 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / CaCl2 x 2 H2O",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 150,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 1.0203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " CaCl2 x 2 H2O                                                              15.00        mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 150 mg is ten times the corresponding primary input. On the provider nominal stock basis, 0.15 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / CoCl2 x 6 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 240,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.24,\n                        \"mmol_l\": 1.84844,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " CoCl2 x 6 H2O                                                              24.00        mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.24",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.24",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 240 mg is ten times the corresponding primary input. On the provider nominal stock basis, 0.24 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / Na2MoO4 x 2 H2O",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 240,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.24,\n                        \"mmol_l\": 0.99194,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " Na2MoO4 x 2H2O                                                             24.00        mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.24",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.24",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider stock input 240 mg is ten times the corresponding primary input. On the provider nominal stock basis, 0.24 g/L × 0.001 L gives delivered grams only; no measured final-medium denominator is inferred."
  },
  {
    "ingredient_or_context": "Trace elements / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Trace elements: corresponding primary row or B12 preparation clause",
        "exact_source_quote": " Distilled water                                                           100.00        ml",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The provider scales the primary 100 mL trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios; the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented as final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "Primary 100 mL water and provider 1000 mL water represent differently scaled stock batches, not a disagreement of stock ratios."
  },
  {
    "ingredient_or_context": "Vitamin B12 solution 0.001 g/L / Vitamin B12",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Vitamin B12 solution 0.001 g/L: corresponding primary row or B12 preparation clause",
        "exact_source_quote": "Vitamin B12 stock solution (0.1mg/100ml)",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "Restore the paragraph-defined B12 stock separately from its 1 mL receiving dose, retaining the conflicting primary table amount. Local 0.001 g/L is stock strength and is supported by neither final-dose interpretation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "0.1 mg / 100 mL × 1 mL = 0.001 mg supplied by the paragraph-defined stock. The main table gives 0.1 mg, 100 times that mass. Local 0.001 g/L = 1 mg/L; no interpretation is silently selected."
  },
  {
    "ingredient_or_context": "Vitamin B12 solution 0.001 g/L / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1434api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1434",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Vitamin B12 solution 0.001 g/L: corresponding primary row or B12 preparation clause",
        "exact_source_quote": "Vitamin B12 stock solution (0.1mg/100ml)",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "Restore the paragraph-defined B12 stock separately from its 1 mL receiving dose, retaining the conflicting primary table amount. Local 0.001 g/L is stock strength and is supported by neither final-dose interpretation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "0.1 mg / 100 mL × 1 mL = 0.001 mg supplied by the paragraph-defined stock. The main table gives 0.1 mg, 100 times that mass. Local 0.001 g/L = 1 mg/L; no interpretation is silently selected."
  },
  {
    "ingredient_or_context": "B12 primary table versus paragraph",
    "field_path": "ingredients[14].concentration",
    "decision": "conflict",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Main table vitamin row",
        "exact_source_quote": " Vitamin B12                                                                0.1          mg",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      },
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Preparation paragraph B12 addition",
        "exact_source_quote": "1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml)",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "Two exact primary statements disagree by 100-fold. Provider selection of the paragraph is not independent resolution. Correct the local stock-strength representation, while retaining the unresolved intended dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "conflict"
      }
    ],
    "arithmetic": "0.1 mg table versus 1 × 0.1/100 = 0.001 mg paragraph; ratio100."
  },
  {
    "ingredient_or_context": "Main pH",
    "field_path": "preparation.Main_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "pH 7.0",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Initial pH step",
    "field_path": "preparation.Initial_pH_step",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "pH 7.0",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 7.0",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "pH 7.0",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Headspace lower ratio",
    "field_path": "preparation.Headspace_lower_ratio",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "1:5 to 1:10",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Headspace upper ratio",
    "field_path": "preparation.Headspace_upper_ratio",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "1:5 to 1:10",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Cooling temperature",
    "field_path": "preparation.Cooling_temperature",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "45°C before adding",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "B12 receiving dose",
    "field_path": "preparation.B12_receiving_dose",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "1mL filter-sterilized Vitamin B12",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "B12 stock mass/volume",
    "field_path": "preparation.B12_stock_mass/volume",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "(0.1mg/100ml)",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Methanol receiving volume",
    "field_path": "preparation.Methanol_receiving_volume",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Exact main preparation paragraph",
        "exact_source_quote": "10 mL filter-sterilized methanol per liter medium.",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The literal condition is retained without attached evidence. Preserve stage and units; the B12 conflict is independently inventoried and is not resolved by quoting this paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "pH-adjustment dose",
    "field_path": "preparation.titrant",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1434",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf",
        "source_locator": "Preparation paragraph",
        "exact_source_quote": "Adjust pH to 7.0 and sterilize.",
        "snapshot_sha256": "754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86",
        "parsed_text_sha256": "0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa"
      }
    ],
    "rationale": "The source supplies an endpoint but no reagent identity or amount; no fixed dose is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Prepare the medium without methanol and vitamin B12 in closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre medium.",
        "decision": "not_quantified"
      }
    ]
  }
]

### Exact DSMZ1434 and stock scaling

identity: supported. Targets: CultureMech:000896.

The target and unique CM000896 owner identify DSMZ 1434. Provider trace2935 scales every primary 100 mL stock row by ten without changing nominal stock ratios. Provider B12 2936 implements the paragraph-defined stock, not an independent resolution of its table conflict.

### Trace transfer and conflicting B12 quantities

consistency: concern. Targets: CultureMech:000896.

Seven local trace rates reproduce undiluted stock g/L despite a 1 mL receiving dose. B12 0.001 g/L also repeats stock strength. Primary table 0.1 mg and paragraph 0.001 mg delivered differ 100-fold; both are preserved. Main salts/agar agree on provider nominal 1 L basis, while methanol7.92 g/L is the provider conversion of10 mL. Explicit liquid inputs and per-liter wording do not justify inventing a measured final denominator.

### Explicit hydrate and vitamin-class scope

grounding: supported. Targets: CultureMech:000896.

All explicit mono-, di-, penta-, hexa- and heptahydrate names correspond to the asserted term definitions/formulas. The B12 class term preserves the unspecified vitamer; no cyanocobalamin identity is invented. Methanol and the main salts agree with source identities. Canonical labels alone are not treated as proof of concentration or stock scope.

### Base sterilization and later filtered additions

completeness: concern. Targets: CultureMech:000896.

The full paragraph retains closed vessels, 1:5–1:10 medium:headspace, pH 7, cooling to about 45°C and separate filtered B12/methanol additions. FILTER_STERILIZE labels the entire combined step, although the primary only says sterilize for the base. Restore staged actions without inventing an autoclave cycle; retain the B12 uncertainty.

### Source agar branch and biological boundaries

scope: supported. Targets: CultureMech:000896.

The exact source requires 15 g agar, supporting SOLID_AGAR. Its salts/methanol/vitamin nutritional formulation supports the recorded defined-medium categorization within the source convention; no alternative agar-free branch is asserted. There are no strain/taxon/assembly/DOI/PMID or specific growth claims.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000896.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Shared current owner defects and writer context

provenance: concern. Targets: CultureMech:000896.

Target and owner retain the same stock flattening and B12 stock rate. Current importer separates primary rows and referenced stocks, but these functions are not a replay of the historical import. Curate the owner with explicit conflict evidence before regeneration.

## Findings

### f1: Trace and vitamin stock strengths are presented as final concentrations

blocker / open / confirmed; issue key: culturemech.000896.stock-scope.

Seven trace rows and B12 are undiluted stock g/L, while structured stock definitions and both 1 mL receiving doses are absent. The resulting 15-row formulation is not the source formulation.

### f2: The primary gives incompatible B12 doses

major / open / confirmed; issue key: culturemech.000896.b12-conflict.

The table specifies 0.1 mg B12, whereas 1 mL of 0.1 mg/100 mL stock supplies 0.001 mg. The provider adopts the paragraph; local 0.001 g/L is the stock rate and is neither intended final amount.

### f3: One filtration action covers a mixed sterilization sequence

minor / open / confirmed; issue key: culturemech.000896.sterilization-action.

The description correctly separates base sterilization from filtered later additions, but action FILTER_STERILIZE applies to the entire combined step. The source does not specify filtration for the base.

## Recommended Actions And Acceptance Checks

### a1

Restore trace and B12 stock hierarchies with original batch scales and exact receiving doses. Preserve main literal masses, methanol volume, nominal provider bases and unresolved final volume. Attach source evidence and regenerate only after explicit owner curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain both source statements with exact locators and seek source clarification before selecting the intended B12 dose. Do not treat provider repetition as independent adjudication or silently replace one primary statement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Separate base sterilization from the later filtered additions and attach the exact paragraph. Preserve all ratios, temperature, pH and conditional B12 scope without inventing a cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alteromonas_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch025/242/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/242/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml:1:id: CultureMech:000896<br>./data/normalized_yaml/bacterial/alteromonas_medium.yaml:1:id: CultureMech:000896<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/242/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 19 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/242/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| dsmz1434 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf; Full exact main recipe, trace/B12 stocks and preparation | supports | All source amounts and stock stages compared. The provider follows the B12 paragraph and does not resolve the primary table-versus-paragraph conflict. |
| mediadive1434api | https://mediadive.dsmz.de/rest/medium/1434; Full exact main recipe, trace/B12 stocks and preparation | supports | All source amounts and stock stages compared. The provider follows the B12 paragraph and does not resolve the primary table-versus-paragraph conflict. |
| solution2935 | https://mediadive.dsmz.de/rest/solution/2935; Full exact main recipe, trace/B12 stocks and preparation | supports | All source amounts and stock stages compared. The provider follows the B12 paragraph and does not resolve the primary table-versus-paragraph conflict. |
| solution2936 | https://mediadive.dsmz.de/rest/solution/2936; Full exact main recipe, trace/B12 stocks and preparation | supports | All source amounts and stock stages compared. The provider follows the B12 paragraph and does not resolve the primary table-versus-paragraph conflict. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17790 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17790 resolves to methanol. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62946 resolves to ammonium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17790": [{"label": "Methanol", "match_type": "preferred_term", "identifier": "CHEBI:17790", "preferred_term": "Methanol", "ontology_id": "CHEBI:17790", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label": "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term": "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch025/242/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch025/242/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/alteromonas_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml", "events": 6, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The complete primary is accessible; its B12 conflict is an assessed scientific uncertainty, not unavailable required evidence. No intended dose is selected.
- Source per-liter language, 1000 mL water and later additions are preserved separately; no measured final volume or independently verified methanol density is claimed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T142833Z-culturemech-000896-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alteromonas_medium (CultureMech:000896)'
started_at: '2026-10-21T14:22:36Z'
finished_at: '2026-10-21T14:28:33Z'
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
summary: 'The 15-ingredient DSMZ 1434 record exposes seven trace-stock concentrations
  and the B12-stock concentration as final medium g/L. The primary itself gives conflicting
  B12 quantities: 0.1 mg in its table versus 1 mL of 0.1 mg/100 mL stock in its instructions.
  Main salts and required agar agree on the provider nominal basis; methanol is a
  provider mass conversion of a literal volume. Preparation retains the key conditions,
  but its single filtration action overstates the base-medium sterilization method.'
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
  - path: data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
    sha256: 8d79224177b4e88bbb6c5489efc52d07a49ecea16a2fb0d9ecad1214e66e176c
    role: target
  - path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
    sha256: 91039378cc0a9f5cbcaf927ed6dc0b53f5ce879cb84b2cbdf4ce06a6c3b9c203
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
  selection: Task review 242; batch 025 item 2 of 10, selected in Python lexicographic
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
  - CultureMech:000896
targets:
- target_id: CultureMech:000896
  path: data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  label: alteromonas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch025/242/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/242/strict.tsv"
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000896
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
  - CultureMech:000896
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alteromonas_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:04.844004Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch025/242/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:06.625290Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/242/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:11.551208Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:13.544752Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:28:32Z'
  support: supports
  summary: './data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml:1:id: CultureMech:000896

    ./data/normalized_yaml/bacterial/alteromonas_medium.yaml:1:id: CultureMech:000896

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/242/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:28:32Z'
  support: supports
  summary: 19 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 6b57260201700c251a2ee313d2e653c67a1ef5d6a004e3025a29a4ec6684f7b6
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/242/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: c4a379d4b3f29218950e22bdbde7d014d04597bff0cb10e0d53139a917780546
- evidence_id: dsmz1434
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf
  locator: Full exact main recipe, trace/B12 stocks and preparation
  accessed_at: '2026-10-21T14:05:43.683549Z'
  support: supports
  summary: All source amounts and stock stages compared. The provider follows the
    B12 paragraph and does not resolve the primary table-versus-paragraph conflict.
  snapshot_sha256: 754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86
- evidence_id: mediadive1434api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1434
  locator: Full exact main recipe, trace/B12 stocks and preparation
  accessed_at: '2026-10-21T14:05:42.867445Z'
  support: supports
  summary: All source amounts and stock stages compared. The provider follows the
    B12 paragraph and does not resolve the primary table-versus-paragraph conflict.
  snapshot_sha256: 3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf
- evidence_id: solution2935
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2935
  locator: Full exact main recipe, trace/B12 stocks and preparation
  accessed_at: '2026-10-21T14:06:47.271390Z'
  support: supports
  summary: All source amounts and stock stages compared. The provider follows the
    B12 paragraph and does not resolve the primary table-versus-paragraph conflict.
  snapshot_sha256: bd1b991b857007ec3be8e549400858589090623142eebb57ce7935e7ccefcbd4
- evidence_id: solution2936
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2936
  locator: Full exact main recipe, trace/B12 stocks and preparation
  accessed_at: '2026-10-21T14:06:47.271469Z'
  support: supports
  summary: All source amounts and stock stages compared. The provider follows the
    B12 paragraph and does not resolve the primary table-versus-paragraph conflict.
  snapshot_sha256: ac6b3322fa0e28531313765f44b0b6fd6d4e56528b6b87ea67b5773964ec6d67
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
- evidence_id: chebi17790
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17790
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:47.448030Z'
  support: supports
  summary: CHEBI:17790 resolves to methanol. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 9954cafff5982d415d5fbed82fa4630ac9958247ed636b3c770976752ebd50de
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T14:28:32Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:17790": [{"label": "Methanol", "match_type": "preferred_term", "identifier":
    "CHEBI:17790", "preferred_term": "Methanol", "ontology_id": "CHEBI:17790", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
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
    "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62946": [{"label":
    "(NH4)2SO4", "match_type": "preferred_term", "identifier": "CHEBI:62946", "preferred_term":
    "(NH4)2SO4", "ontology_id": "CHEBI:62946", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364":
    [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364",
    "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/242/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 4e6a26c0e62d0c0183bf040cefe71d13b35fa24e8215282a6a76fe9f6ab0c3d4
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/242/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: b879fcc699e1e00083c7baf355901c3fa631332368fbf41f6a7802c3b52dbb4e
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T14:28:32Z'
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
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALTEROMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/alteromonas_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:28:32Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alteromonas_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '15 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 15/15
    primary and 15/15 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi176843
  - chebi17790
  - chebi2509
  - chebi26710
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi53503
  - chebi62946
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi86158
  - chebi86364
  details: 'Instance coverage on a 0–100 percent scale, denominator 15: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 30 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main sol. 1434 / (NH4)2SO4\"\
    ,\n    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"(NH4)2SO4\\\",\\n             \
    \           \\\"compound_id\\\": 27,\\n                        \\\"amount\\\"\
    : 2,\\n                        \\\"unit\\\": \\\"g\\\",\\n                   \
    \     \\\"g_l\\\": 2,\\n                        \\\"mmol_l\\\": 15.1355,\\n  \
    \                      \\\"optional\\\": 0\\n                    }\",\n      \
    \  \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" (NH4)2SO4                    \
    \                                                 2.0         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The main amount agrees with the provider\
    \ nominal 1 L basis and lacks attached evidence. Preserve the source literal amount\
    \ and required agar without inferring a measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL\
    \ trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs;\
    \ this is not measured final volume or a replacement denominator.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main sol. 1434 / K2HPO4\",\n    \"field_path\"\
    : \"ingredients[1].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"K2HPO4\\\",\\n                \
    \        \\\"compound_id\\\": 10,\\n                        \\\"amount\\\": 2,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 2,\\n                        \\\"mmol_l\\\": 11.4826,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" K2HPO4                       \
    \                                                 2.0         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The main amount agrees with the provider\
    \ nominal 1 L basis and lacks attached evidence. Preserve the source literal amount\
    \ and required agar without inferring a measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL\
    \ trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs;\
    \ this is not measured final volume or a replacement denominator.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main sol. 1434 / KH2PO4\",\n    \"field_path\"\
    : \"ingredients[2].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"KH2PO4\\\",\\n                \
    \        \\\"compound_id\\\": 11,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 1,\\n                        \\\"mmol_l\\\": 7.34835,\\n          \
    \              \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" KH2PO4                       \
    \                                                 1.0         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The main amount agrees with the provider\
    \ nominal 1 L basis and lacks attached evidence. Preserve the source literal amount\
    \ and required agar without inferring a measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL\
    \ trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs;\
    \ this is not measured final volume or a replacement denominator.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main sol. 1434 / NaCl\",\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 4,\\\
    n                        \\\"compound\\\": \\\"NaCl\\\",\\n                  \
    \      \\\"compound_id\\\": 43,\\n                        \\\"amount\\\": 20,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 20,\\n                        \\\"mmol_l\\\": 342.231,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" NaCl                         \
    \                                                20.0         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The main amount agrees with the provider\
    \ nominal 1 L basis and lacks attached evidence. Preserve the source literal amount\
    \ and required agar without inferring a measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL\
    \ trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs;\
    \ this is not measured final volume or a replacement denominator.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main sol. 1434 / MgSO4 x 7 H2O\",\n    \"field_path\"\
    : \"ingredients[4].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 8,\\n                        \\\"amount\\\
    \": 0.3,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.3,\\n                        \\\"mmol_l\\\": 1.21716,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" MgSO4 x 7 H2O                \
    \                                                 0.3         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The main amount agrees with the provider\
    \ nominal 1 L basis and lacks attached evidence. Preserve the source literal amount\
    \ and required agar without inferring a measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL\
    \ trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs;\
    \ this is not measured final volume or a replacement denominator.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main sol. 1434 / Vitamin B12 solution 0.001\
    \ g/L\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n   \
    \ \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"solution\\\": \\\"Vitamin B12 solution 0.001 g/L\\\
    \",\\n                        \\\"solution_id\\\": 2936,\\n                  \
    \      \\\"amount\\\": 1,\\n                        \\\"unit\\\": \\\"ml\\\",\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \"1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml)\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"This source stock receiving dose or solvent\
    \ quantity is absent from structured local scope; restore the exact amount within\
    \ the intended stage.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1434 / Trace elements\",\n    \"field_path\": \"solutions\",\n \
    \   \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    solution\\\": \\\"Trace elements\\\",\\n                        \\\"solution_id\\\
    \": 2935,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" Trace elements (see below)   \
    \                                                 1.0       ml\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"This source stock receiving dose or solvent\
    \ quantity is absent from structured local scope; restore the exact amount within\
    \ the intended stage.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1434 / Methanol\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Methanol\\\",\\n                        \\\"compound_id\\\"\
    : 226,\\n                        \\\"amount\\\": 10,\\n                      \
    \  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"g_l\\\": 7.92,\\n \
    \                       \\\"mmol_l\\\": 247.176,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" Methanol                     \
    \                                                10.0       ml\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"Source methanol is 10 mL per liter; local\
    \ 7.92 g/L agrees with the provider conversion only. Preserve the literal volume,\
    \ source-per-liter wording and conversion provenance; density/temperature were\
    \ not independently established.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.92\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"7.92\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"arithmetic\": \"7.92 g per 10 mL implies\
    \ provider density 0.792 g/mL. This is a description of its conversion, not independent\
    \ physical verification.\"\n  },\n  {\n    \"ingredient_or_context\": \"Main sol.\
    \ 1434 / Agar\",\n    \"field_path\": \"ingredients[6].concentration\",\n    \"\
    decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" Agar                         \
    \                                                15.0         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The main amount agrees with the provider\
    \ nominal 1 L basis and lacks attached evidence. Preserve the source literal amount\
    \ and required agar without inferring a measured final volume.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"15\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Declared provider main volume is 1000 mL. Literal 1000 mL water plus 1 mL\
    \ trace, 1 mL paragraph-defined B12 and 10 mL methanol totals 1012 mL inputs;\
    \ this is not measured final volume or a replacement denominator.\"\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Main sol. 1434 / Distilled water\",\n    \"\
    field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\": null,\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1434api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1434: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" Distilled water              \
    \                                             1000.0        ml\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"This source stock receiving dose or solvent\
    \ quantity is absent from structured local scope; restore the exact amount within\
    \ the intended stage.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace elements / MnSO4 x H2O\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 760,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.76,\\\
    n                        \\\"mmol_l\\\": 4.49662,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Trace elements: corresponding primary row or\
    \ B12 preparation clause\",\n        \"exact_source_quote\": \" MnSO4 x H2O  \
    \                                                              76.00        mg\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.76\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.76\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider stock input 760\
    \ mg is ten times the corresponding primary input. On the provider nominal stock\
    \ basis, 0.76 g/L × 0.001 L gives delivered grams only; no measured final-medium\
    \ denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace\
    \ elements / CuSO4 x 5 H2O\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 121,\\n                        \\\"amount\\\": 250,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.25,\\\
    n                        \\\"mmol_l\\\": 1.00126,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Trace elements: corresponding primary row or\
    \ B12 preparation clause\",\n        \"exact_source_quote\": \" CuSO4 x 5 H2O\
    \                                                              25.00        mg\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.25\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider stock input 250\
    \ mg is ten times the corresponding primary input. On the provider nominal stock\
    \ basis, 0.25 g/L × 0.001 L gives delivered grams only; no measured final-medium\
    \ denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace\
    \ elements / FeSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[9].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 280,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.28,\\\
    n                        \\\"mmol_l\\\": 1.00714,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Trace elements: corresponding primary row or\
    \ B12 preparation clause\",\n        \"exact_source_quote\": \" FeSO4 x 7 H2O\
    \                                                              28.00        mg\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.28\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.28\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider stock input 280\
    \ mg is ten times the corresponding primary input. On the provider nominal stock\
    \ basis, 0.28 g/L × 0.001 L gives delivered grams only; no measured final-medium\
    \ denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace\
    \ elements / ZnSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 1.4,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.4,\\n \
    \                       \\\"mmol_l\\\": 4.86853,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Trace elements: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" ZnSO4 x 7 H2O                \
    \                                                0.14         g\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ stock input 1.4 g is ten times the corresponding primary input. On the provider\
    \ nominal stock basis, 1.4 g/L × 0.001 L gives delivered grams only; no measured\
    \ final-medium denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace elements / CaCl2 x 2 H2O\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 150,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.15,\\n\
    \                        \\\"mmol_l\\\": 1.0203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Trace elements: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" CaCl2 x 2 H2O                \
    \                                              15.00        mg\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.15\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider stock input 150\
    \ mg is ten times the corresponding primary input. On the provider nominal stock\
    \ basis, 0.15 g/L × 0.001 L gives delivered grams only; no measured final-medium\
    \ denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace\
    \ elements / CoCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 240,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.24,\\\
    n                        \\\"mmol_l\\\": 1.84844,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Trace elements: corresponding primary row or\
    \ B12 preparation clause\",\n        \"exact_source_quote\": \" CoCl2 x 6 H2O\
    \                                                              24.00        mg\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.24\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider stock input 240\
    \ mg is ten times the corresponding primary input. On the provider nominal stock\
    \ basis, 0.24 g/L × 0.001 L gives delivered grams only; no measured final-medium\
    \ denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace\
    \ elements / Na2MoO4 x 2 H2O\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 240,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.24,\\n\
    \                        \\\"mmol_l\\\": 0.99194,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Trace elements: corresponding primary row or\
    \ B12 preparation clause\",\n        \"exact_source_quote\": \" Na2MoO4 x 2H2O\
    \                                                             24.00        mg\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.24\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.24\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider stock input 240\
    \ mg is ten times the corresponding primary input. On the provider nominal stock\
    \ basis, 0.24 g/L × 0.001 L gives delivered grams only; no measured final-medium\
    \ denominator is inferred.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trace\
    \ elements / Distilled water\",\n    \"field_path\": \"solutions\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1434api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1434\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Trace elements: corresponding primary row or B12 preparation\
    \ clause\",\n        \"exact_source_quote\": \" Distilled water              \
    \                                             100.00        ml\",\n        \"\
    snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The provider scales the primary 100 mL\
    \ trace batch by ten to a nominal 1000 mL stock. This preserves stock ratios;\
    \ the 1 mL receiving dose is still required. Undiluted stock g/L cannot be presented\
    \ as final-medium concentration.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"Primary 100 mL\
    \ water and provider 1000 mL water represent differently scaled stock batches,\
    \ not a disagreement of stock ratios.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin B12 solution 0.001 g/L / Vitamin B12\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.001,\\\
    n                        \\\"mmol_l\\\": 0.00073779,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Vitamin B12 solution 0.001 g/L: corresponding primary\
    \ row or B12 preparation clause\",\n        \"exact_source_quote\": \"Vitamin\
    \ B12 stock solution (0.1mg/100ml)\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the paragraph-defined B12 stock\
    \ separately from its 1 mL receiving dose, retaining the conflicting primary table\
    \ amount. Local 0.001 g/L is stock strength and is supported by neither final-dose\
    \ interpretation.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.1 mg / 100 mL × 1 mL = 0.001 mg supplied by the paragraph-defined stock.\
    \ The main table gives 0.1 mg, 100 times that mass. Local 0.001 g/L = 1 mg/L;\
    \ no interpretation is silently selected.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Vitamin B12 solution 0.001 g/L / Distilled water\",\n    \"field_path\": \"\
    solutions\",\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1434api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1434\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 100,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"3152060f3355043a7eb62bf14f76e809633a0b9c7252fd07e8e05dff20b8bedf\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Vitamin B12 solution 0.001 g/L: corresponding primary\
    \ row or B12 preparation clause\",\n        \"exact_source_quote\": \"Vitamin\
    \ B12 stock solution (0.1mg/100ml)\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"Restore the paragraph-defined B12 stock\
    \ separately from its 1 mL receiving dose, retaining the conflicting primary table\
    \ amount. Local 0.001 g/L is stock strength and is supported by neither final-dose\
    \ interpretation.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"0.1 mg / 100 mL\
    \ × 1 mL = 0.001 mg supplied by the paragraph-defined stock. The main table gives\
    \ 0.1 mg, 100 times that mass. Local 0.001 g/L = 1 mg/L; no interpretation is\
    \ silently selected.\"\n  },\n  {\n    \"ingredient_or_context\": \"B12 primary\
    \ table versus paragraph\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"conflict\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n       \
    \ \"source_locator\": \"Main table vitamin row\",\n        \"exact_source_quote\"\
    : \" Vitamin B12                                                             \
    \   0.1          mg\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n   \
    \     \"source_locator\": \"Preparation paragraph B12 addition\",\n        \"\
    exact_source_quote\": \"1mL filter-sterilized Vitamin B12 stock solution (0.1mg/100ml)\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"Two exact primary statements disagree\
    \ by 100-fold. Provider selection of the paragraph is not independent resolution.\
    \ Correct the local stock-strength representation, while retaining the unresolved\
    \ intended dose.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ingredients[14].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"conflict\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/alteromonas_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"conflict\"\n      }\n    ],\n    \"arithmetic\": \"0.1 mg table versus 1 ×\
    \ 0.1/100 = 0.001 mg paragraph; ratio100.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main pH\",\n    \"field_path\": \"preparation.Main_pH\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"pH 7.0\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ph_value\",\n      \
    \  \"stored\": 7.0,\n        \"decision\": \"evidence_only\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Initial pH step\",\n    \"field_path\": \"preparation.Initial_pH_step\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1434\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation paragraph\",\n        \"exact_source_quote\"\
    : \"pH 7.0\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"pH 7.0\",\n        \"decision\": \"evidence_only\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"pH 7.0\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Headspace lower ratio\",\n    \"field_path\"\
    : \"preparation.Headspace_lower_ratio\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"1:5 to 1:10\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"evidence_only\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Headspace upper ratio\",\n    \"field_path\"\
    : \"preparation.Headspace_upper_ratio\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"1:5 to 1:10\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"evidence_only\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Cooling temperature\",\n    \"field_path\"\
    : \"preparation.Cooling_temperature\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"45°C before adding\",\n        \"snapshot_sha256\"\
    : \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\",\n    \
    \    \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"evidence_only\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"B12 receiving dose\",\n    \"field_path\"\
    : \"preparation.B12_receiving_dose\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"1mL filter-sterilized Vitamin B12\",\n        \"snapshot_sha256\"\
    : \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\",\n    \
    \    \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"evidence_only\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"B12 stock mass/volume\",\n    \"field_path\"\
    : \"preparation.B12_stock_mass/volume\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"(0.1mg/100ml)\",\n        \"snapshot_sha256\": \"\
    754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\",\n        \"\
    parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"evidence_only\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Methanol receiving volume\",\n    \"field_path\"\
    : \"preparation.Methanol_receiving_volume\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1434\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation paragraph\",\n       \
    \ \"exact_source_quote\": \"10 mL filter-sterilized methanol per liter medium.\"\
    ,\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The literal condition is retained without\
    \ attached evidence. Preserve stage and units; the B12 conflict is independently\
    \ inventoried and is not resolved by quoting this paragraph.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"evidence_only\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"evidence_only\"\n      }\n    ]\n  },\n\
    \  {\n    \"ingredient_or_context\": \"pH-adjustment dose\",\n    \"field_path\"\
    : \"preparation.titrant\",\n    \"decision\": \"not_quantified\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1434\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1434.pdf\"\
    ,\n        \"source_locator\": \"Preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.0 and sterilize.\",\n        \"snapshot_sha256\": \"754f53ae81a63c105686d3b1ff94157786cfb32bc13b031a0b5cec14d76ded86\"\
    ,\n        \"parsed_text_sha256\": \"0efacf7f737851d4a54b66bc64f9ad544d0eec7e99f2ed3dd1c5a050bb4290aa\"\
    \n      }\n    ],\n    \"rationale\": \"The source supplies an endpoint but no\
    \ reagent identity or amount; no fixed dose is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[1].description\"\
    ,\n        \"stored\": \"Prepare the medium without methanol and vitamin B12 in\
    \ closed vessels with a medium to headspace ratio of 1:5 to 1:10. Adjust pH to\
    \ 7.0 and sterilize. Allow to cool to about 45°C before adding 1mL filter-sterilized\
    \ Vitamin B12 stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol\
    \ per litre medium.\",\n        \"decision\": \"not_quantified\"\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/alteromonas_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Prepare the medium without methanol and vitamin B12 in closed vessels with\
    \ a medium to headspace ratio of 1:5 to 1:10. Adjust pH to 7.0 and sterilize.\
    \ Allow to cool to about 45°C before adding 1mL filter-sterilized Vitamin B12\
    \ stock solution (0.1mg/100ml) and 10 mL filter-sterilized methanol per litre\
    \ medium.\",\n        \"decision\": \"not_quantified\"\n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact DSMZ1434 and stock scaling
  outcome: supported
  summary: The target and unique CM000896 owner identify DSMZ 1434. Provider trace2935
    scales every primary 100 mL stock row by ten without changing nominal stock ratios.
    Provider B12 2936 implements the paragraph-defined stock, not an independent resolution
    of its table conflict.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - owner-0
  - id-search
  - dsmz1434
  - mediadive1434api
  - solution2935
  - solution2936
- assessment_id: source-stage-consistency
  area: consistency
  topic: Trace transfer and conflicting B12 quantities
  outcome: concern
  summary: Seven local trace rates reproduce undiluted stock g/L despite a 1 mL receiving
    dose. B12 0.001 g/L also repeats stock strength. Primary table 0.1 mg and paragraph
    0.001 mg delivered differ 100-fold; both are preserved. Main salts/agar agree
    on provider nominal 1 L basis, while methanol7.92 g/L is the provider conversion
    of10 mL. Explicit liquid inputs and per-liter wording do not justify inventing
    a measured final denominator.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
  - mediadive1434api
  - quantity-inventory
  - quantity-local-fields
- assessment_id: forms
  area: grounding
  topic: Explicit hydrate and vitamin-class scope
  outcome: supported
  summary: All explicit mono-, di-, penta-, hexa- and heptahydrate names correspond
    to the asserted term definitions/formulas. The B12 class term preserves the unspecified
    vitamer; no cyanocobalamin identity is invented. Methanol and the main salts agree
    with source identities. Canonical labels alone are not treated as proof of concentration
    or stock scope.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
  - chebi131527
  - chebi176843
  - chebi17790
  - chebi2509
  - chebi26710
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi53503
  - chebi62946
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi86158
  - chebi86364
- assessment_id: preparation
  area: completeness
  topic: Base sterilization and later filtered additions
  outcome: concern
  summary: The full paragraph retains closed vessels, 1:5–1:10 medium:headspace, pH
    7, cooling to about 45°C and separate filtered B12/methanol additions. FILTER_STERILIZE
    labels the entire combined step, although the primary only says sterilize for
    the base. Restore staged actions without inventing an autoclave cycle; retain
    the B12 uncertainty.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Source agar branch and biological boundaries
  outcome: supported
  summary: The exact source requires 15 g agar, supporting SOLID_AGAR. Its salts/methanol/vitamin
    nutritional formulation supports the recorded defined-medium categorization within
    the source convention; no alternative agar-free branch is asserted. There are
    no strain/taxon/assembly/DOI/PMID or specific growth claims.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: generation
  area: provenance
  topic: Shared current owner defects and writer context
  outcome: concern
  summary: Target and owner retain the same stock flattening and B12 stock rate. Current
    importer separates primary rows and referenced stocks, but these functions are
    not a replay of the historical import. Curate the owner with explicit conflict
    evidence before regeneration.
  target_ids:
  - CultureMech:000896
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - writer-context-0
  - writer-context-1
  - writer-context-2
findings:
- finding_id: f1
  issue_key: culturemech.000896.stock-scope
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Trace and vitamin stock strengths are presented as final concentrations
  description: Seven trace rows and B12 are undiluted stock g/L, while structured
    stock definitions and both 1 mL receiving doses are absent. The resulting 15-row
    formulation is not the source formulation.
  target_ids:
  - CultureMech:000896
  field_paths:
  - ingredients[7]
  - ingredients[8]
  - ingredients[9]
  - ingredients[10]
  - ingredients[11]
  - ingredients[12]
  - ingredients[13]
  - ingredients[14]
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
  - mediadive1434api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
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
  issue_key: culturemech.000896.b12-conflict
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The primary gives incompatible B12 doses
  description: The table specifies 0.1 mg B12, whereas 1 mL of 0.1 mg/100 mL stock
    supplies 0.001 mg. The provider adopts the paragraph; local 0.001 g/L is the stock
    rate and is neither intended final amount.
  target_ids:
  - CultureMech:000896
  field_paths:
  - ingredients[14].concentration
  - preparation_steps[1].description
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
  - solution2936
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
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
  issue_key: culturemech.000896.sterilization-action
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: One filtration action covers a mixed sterilization sequence
  description: The description correctly separates base sterilization from filtered
    later additions, but action FILTER_STERILIZE applies to the entire combined step.
    The source does not specify filtration for the base.
  target_ids:
  - CultureMech:000896
  field_paths:
  - preparation_steps[1].action
  - preparation_steps[1].description
  evidence_ids:
  - record
  - owner-0
  - dsmz1434
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore trace and B12 stock hierarchies with original batch scales
    and exact receiving doses. Preserve main literal masses, methanol volume, nominal
    provider bases and unresolved final volume. Attach source evidence and regenerate
    only after explicit owner curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000896
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
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
  description: Retain both source statements with exact locators and seek source clarification
    before selecting the intended B12 dose. Do not treat provider repetition as independent
    adjudication or silently replace one primary statement.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000896
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
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
  description: Separate base sterilization from the later filtered additions and attach
    the exact paragraph. Preserve all ratios, temperature, pH and conditional B12
    scope without inventing a cycle.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000896
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alteromonas_medium.yaml
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
- The complete primary is accessible; its B12 conflict is an assessed scientific uncertainty,
  not unavailable required evidence. No intended dose is selected.
- Source per-liter language, 1000 mL water and later additions are preserved separately;
  no measured final volume or independently verified methanol density is claimed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-025
- generated-medium
```
