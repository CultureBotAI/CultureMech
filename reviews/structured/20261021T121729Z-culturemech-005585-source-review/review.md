# Source and formulation review: alcaligenes_xylosoxydans_medium_with_benzoate (CultureMech:005585)

- Review: 20261021T121729Z-culturemech-005585-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:11:53Z
- Finished UTC: 2026-10-21T12:17:29Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 471 is identifiable, but the generated record and sole KOMODO owner present solution A/B and nested SL-4/SL-6 stock strengths as final-medium ingredients and place solution A pH 9 at medium level. The exact primary requires separate preparation and final adjustment to pH 8.2. Chemical-form, evidence and legacy-link issues remain; the historical legacy MIM correspondence is unavailable.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 195; batch 020 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding nineteen task batches contain 190 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 193 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005585 | data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml | generated | alcaligenes_xylosoxydans_medium_with_benzoate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005585 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:005585 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/195/strict.tsv |
| validate-terms | passed | True | CultureMech:005585 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:005585 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:005585 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodo471 | unavailable | False | CultureMech:005585 | The exact KOMODO detail request returned HTTP 403. Its response is preserved; the accessible exact catalog and complete official DSMZ formulation support current identity/formulation, not a replay of the historical import. |
| Historical legacy MIM identifier correspondence | unavailable | True | CultureMech:005585 | MediaIngredientMech:000170 remains unresolved after completed bounded current lookups; no authoritative historical correspondence is captured. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:005585.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:005585.

17 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 17/17 primary and 16/17 secondary instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 17: primary 100.00%; secondary 94.12%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:005585.

40 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main medium: Solution A",
    "field_path": "source.solution_965.recipe[0]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 966,\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      },
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; combined preparation",
        "exact_source_quote": "Autoclave solutions A, B and C separately, combine, adjust pH to 8.2.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      }
    ],
    "arithmetic": "Source amount: 500 ml; provider-declared stage volume 1002 mL. "
  },
  {
    "ingredient_or_context": "Main medium: Solution B",
    "field_path": "source.solution_965.recipe[1]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 967,\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      },
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; combined preparation",
        "exact_source_quote": "Autoclave solutions A, B and C separately, combine, adjust pH to 8.2.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      }
    ],
    "arithmetic": "Source amount: 500 ml; provider-declared stage volume 1002 mL. "
  },
  {
    "ingredient_or_context": "Main medium: Solution C",
    "field_path": "source.solution_965.recipe[2]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 968,\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      },
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; combined preparation",
        "exact_source_quote": "Autoclave solutions A, B and C separately, combine, adjust pH to 8.2.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      }
    ],
    "arithmetic": "Source amount: 2 ml; provider-declared stage volume 1002 mL. "
  },
  {
    "ingredient_or_context": "Solution A: K2HPO4",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": {
      "value": "10.24",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution A table, row 1",
        "exact_source_quote": "K2HPO4 5.12 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 5.12,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.24,\n                        \"mmol_l\": 58.7911,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "decision": "correct",
        "stored": {
          "value": "10.24",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[0].concentration",
        "decision": "correct",
        "stored": {
          "value": "10.24",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "10.24",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 5.12 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 10.24 g/L × 0.5 L equivalent stock per listed batch = 5.120 g; division by provider main 1.002 L gives 5.109780439121756487025948104 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution A: KH2PO4",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": {
      "value": "3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution A table, row 2",
        "exact_source_quote": "KH2PO4 1.50 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 22.045,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "decision": "correct",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[1].concentration",
        "decision": "correct",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 1.5 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 3 g/L × 0.5 L equivalent stock per listed batch = 1.5 g; division by provider main 1.002 L gives 1.497005988023952095808383234 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution A: Distilled water",
    "field_path": "source.solution_966.recipe[2]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution A table, row 3",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred. The standalone dependency retains an incorrect water percentage; correct its source water volume before reuse.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "PERCENT_V_V"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Source amount: 500 ml; provider-declared stage volume 500 mL. "
  },
  {
    "ingredient_or_context": "Solution B: NH4Cl",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "local": {
      "value": "0.6",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B table, row 1",
        "exact_source_quote": "NH4Cl 0.30 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.6,\n                        \"mmol_l\": 11.217,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[2].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.3 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 0.6 g/L × 0.5 L equivalent stock per listed batch = 0.30 g; division by provider main 1.002 L gives 0.2994011976047904191616766467 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution B: CaCl2",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B table, row 2",
        "exact_source_quote": "CaCl2 0.01 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"CaCl2\",\n                        \"compound_id\": 81,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.180213,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[3].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.01 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 0.02 g/L × 0.5 L equivalent stock per listed batch = 0.010 g; division by provider main 1.002 L gives 0.009980039920159680638722554890 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution B: MgSO4 x 7 H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "local": {
      "value": "0.4",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B table, row 3",
        "exact_source_quote": "MgSO4 x 7 H2O 0.20 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.4,\n                        \"mmol_l\": 1.62288,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[4].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.2 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 0.4 g/L × 0.5 L equivalent stock per listed batch = 0.20 g; division by provider main 1.002 L gives 0.1996007984031936127744510978 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution B: KNO3",
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "local": {
      "value": "4",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B table, row 4",
        "exact_source_quote": "KNO3 2.00 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 39.5636,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "decision": "correct",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[5].concentration",
        "decision": "correct",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 2 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 4 g/L × 0.5 L equivalent stock per listed batch = 2.0 g; division by provider main 1.002 L gives 1.996007984031936127744510978 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution B: Na-benzoate",
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "local": {
      "value": "1.84",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B table, row 5",
        "exact_source_quote": "Na-benzoate 0.92 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na-benzoate\",\n                        \"compound_id\": 295,\n                        \"amount\": 0.92,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.84,\n                        \"mmol_l\": 12.7686,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "decision": "correct",
        "stored": {
          "value": "1.84",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[6].concentration",
        "decision": "correct",
        "stored": {
          "value": "1.84",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "1.84",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.92 g; provider-declared stage volume 500 mL. Conditional provider-basis check only: 1.84 g/L × 0.5 L equivalent stock per listed batch = 0.920 g; division by provider main 1.002 L gives 0.9181636726546906187624750499 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Solution B: Distilled water",
    "field_path": "source.solution_967.recipe[5]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B table, row 6",
        "exact_source_quote": "Distilled water 500.00 ml",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 500,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.5",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 500 ml; provider-declared stage volume 500 mL. "
  },
  {
    "ingredient_or_context": "Solution C: Trace element solution SL-4",
    "field_path": "source.solution_968.recipe[0]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution C table, row 1",
        "exact_source_quote": "Trace element solution SL-4 2.00 ml",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Trace element solution SL-4\",\n                        \"solution_id\": 969,\n                        \"amount\": 2,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      }
    ],
    "arithmetic": "Source amount: 2 ml; provider-declared stage volume 2 mL. "
  },
  {
    "ingredient_or_context": "Trace element solution SL-4: EDTA",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-4 table, row 1",
        "exact_source_quote": "EDTA 0.50 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[4].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"EDTA\",\n                        \"compound_id\": 271,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.71092,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[7].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.5 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.5 g/L × 0.002 L equivalent stock per listed batch = 0.0010 g; division by provider main 1.002 L gives 0.0009980039920159680638722554890 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-4: FeSO4 x 7 H2O",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-4 table, row 2",
        "exact_source_quote": "FeSO4 x 7 H2O 0.20 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[4].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.719386,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[8].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.2 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.2 g/L × 0.002 L equivalent stock per listed batch = 0.0004 g; division by provider main 1.002 L gives 0.0003992015968063872255489021956 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-4: Trace element solution SL-6",
    "field_path": "source.solution_969.recipe[2]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-4 table, row 3",
        "exact_source_quote": "Trace element solution SL-6 100.00 ml",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[4].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Trace element solution SL-6\",\n                        \"solution_id\": 25,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "solutions",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "arithmetic": "Source amount: 100 ml; provider-declared stage volume 1000 mL. "
  },
  {
    "ingredient_or_context": "Trace element solution SL-4: Distilled water",
    "field_path": "source.solution_969.recipe[3]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-4 table, row 4",
        "exact_source_quote": "Distilled water 900.00 ml",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[4].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 900,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred. The standalone dependency retains an incorrect water percentage; correct its source water volume before reuse.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "900",
          "unit": "PERCENT_V_V"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Source amount: 900 ml; provider-declared stage volume 1000 mL. "
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: ZnSO4 x 7 H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": {
      "value": "0.1",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 1",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[9].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.1 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.1 g/L × 0.0002 L equivalent stock per listed batch = 0.00002 g; division by provider main 1.002 L gives 0.00001996007984031936127744510978 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: MnCl2 x 4 H2O",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 2",
        "exact_source_quote": "MnCl2 x 4 H2O 0.03 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[10].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.03 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.03 g/L × 0.0002 L equivalent stock per listed batch = 0.000006 g; division by provider main 1.002 L gives 0.000005988023952095808383233532934 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: H3BO3",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": {
      "value": "0.3",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 3",
        "exact_source_quote": "H3BO3 0.30 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[11].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.3 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.3 g/L × 0.0002 L equivalent stock per listed batch = 0.00006 g; division by provider main 1.002 L gives 0.00005988023952095808383233532934 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: CoCl2 x 6 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": {
      "value": "0.2",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 4",
        "exact_source_quote": "CoCl2 x 6 H2O 0.20 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[12].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.2 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.2 g/L × 0.0002 L equivalent stock per listed batch = 0.00004 g; division by provider main 1.002 L gives 0.00003992015968063872255489021956 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: CuCl2 x 2 H2O",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": {
      "value": "0.01",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 5",
        "exact_source_quote": "CuCl2 x 2 H2O 0.01 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[13].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.01 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.01 g/L × 0.0002 L equivalent stock per listed batch = 0.000002 g; division by provider main 1.002 L gives 0.000001996007984031936127744510978 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: NiCl2 x 6 H2O",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": {
      "value": "0.02",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 6",
        "exact_source_quote": "NiCl2 x 6 H2O 0.02 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[14].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.02 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.02 g/L × 0.0002 L equivalent stock per listed batch = 0.000004 g; division by provider main 1.002 L gives 0.000003992015968063872255489021956 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: Na2MoO4 x 2 H2O",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": {
      "value": "0.03",
      "unit": "G_PER_L"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 7",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.03 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "The local number matches a provider stock strength but is asserted as a direct medium concentration. Restore the named source solution and nested receiving doses; attach evidence at that stage. Keep the source stock number distinct from any conditional final calculation.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[15].concentration",
        "decision": "correct",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 0.03 g; provider-declared stage volume 1000 mL. Conditional provider-basis check only: 0.03 g/L × 0.0002 L equivalent stock per listed batch = 0.000006 g; division by provider main 1.002 L gives 0.000005988023952095808383233532934 g/L. This is not an independently measured final volume or an instruction to replace the source stock formulation."
  },
  {
    "ingredient_or_context": "Trace element solution SL-6: Distilled water",
    "field_path": "source.solution_25.recipe[7]",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 table, row 8",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Preserve this original amount and unit at its named source stage. It is absent as a distinct stock-dose/water claim in target and owner; no density or final volume is inferred.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified"
      }
    ],
    "arithmetic": "Source amount: 1000 ml; provider-declared stage volume 1000 mL. "
  },
  {
    "ingredient_or_context": "Provider declared volume: Main sol. 471",
    "field_path": "source.solution_965.declared_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1002",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Record the source-declared volume as provenance for its stage. It is not an independently measured final volume and does not erase unquantified pH-adjustment additions.",
    "action_taken": "Review only; no recipe change.",
    "arithmetic": "1002 mL; no conversion to a measured final volume."
  },
  {
    "ingredient_or_context": "Provider declared volume: Solution A",
    "field_path": "source.solution_966.declared_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[1].volume",
        "exact_source_quote": "\"volume\": 500",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Record the source-declared volume as provenance for its stage. It is not an independently measured final volume and does not erase unquantified pH-adjustment additions.",
    "action_taken": "Review only; no recipe change.",
    "arithmetic": "500 mL; no conversion to a measured final volume."
  },
  {
    "ingredient_or_context": "Provider declared volume: Solution B",
    "field_path": "source.solution_967.declared_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[2].volume",
        "exact_source_quote": "\"volume\": 500",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Record the source-declared volume as provenance for its stage. It is not an independently measured final volume and does not erase unquantified pH-adjustment additions.",
    "action_taken": "Review only; no recipe change.",
    "arithmetic": "500 mL; no conversion to a measured final volume."
  },
  {
    "ingredient_or_context": "Provider declared volume: Solution C",
    "field_path": "source.solution_968.declared_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[3].volume",
        "exact_source_quote": "\"volume\": 2",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Record the source-declared volume as provenance for its stage. It is not an independently measured final volume and does not erase unquantified pH-adjustment additions.",
    "action_taken": "Review only; no recipe change.",
    "arithmetic": "2 mL; no conversion to a measured final volume."
  },
  {
    "ingredient_or_context": "Provider declared volume: Trace element solution SL-4",
    "field_path": "source.solution_969.declared_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[4].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Record the source-declared volume as provenance for its stage. It is not an independently measured final volume and does not erase unquantified pH-adjustment additions.",
    "action_taken": "Review only; no recipe change.",
    "arithmetic": "1000 mL; no conversion to a measured final volume."
  },
  {
    "ingredient_or_context": "Provider declared volume: Trace element solution SL-6",
    "field_path": "source.solution_25.declared_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive471api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/471",
        "source_locator": "$.data.solutions[5].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7"
      }
    ],
    "rationale": "Record the source-declared volume as provenance for its stage. It is not an independently measured final volume and does not erase unquantified pH-adjustment additions.",
    "action_taken": "Review only; no recipe change.",
    "arithmetic": "1000 mL; no conversion to a measured final volume."
  },
  {
    "ingredient_or_context": "KOH adjustment amount",
    "field_path": "ingredients[16].concentration",
    "decision": "not_quantified",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution A preparation",
        "exact_source_quote": "Adjust pH to 9.0 with KOH.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "The collection does not specify a KOH dose. Retain nonnumeric quantity but restore solution A scope and evidence; do not invent a strength or final-medium concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "decision": "correct",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ingredients[16].concentration",
        "decision": "correct",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A pH endpoint versus local medium pH",
    "field_path": "ph_value",
    "decision": "correct",
    "local": 9.0,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution A preparation",
        "exact_source_quote": "Adjust pH to 9.0 with KOH.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      },
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; combined preparation",
        "exact_source_quote": "Autoclave solutions A, B and C separately, combine, adjust pH to 8.2.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "Local scalar 9.0 is the preparation endpoint of A, not the combined medium. Preserve A pH 9.0 separately and represent combined pH 8.2.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "decision": "correct",
        "stored": 9.0
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "ph_value",
        "decision": "correct",
        "stored": 9.0
      }
    ]
  },
  {
    "ingredient_or_context": "SL-4 pH range",
    "field_path": "source.sl4.preparation.pH",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; SL-4 preparation",
        "exact_source_quote": "First dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution \nof NaOH; then add ferrous sulfate and the trace element solution SL–6.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "Add the source pH 7.0–8.0 range at SL-4 preparation, not at medium level.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "preparation_notes",
        "stored": "First dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution of NaOH; then add ferrous sulfate and the trace element solution SL-6. \nFirst dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution\r\nof NaOH; then add ferrous sulfate and the trace element solution SL–6.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "SL-4 NaOH reagent strength",
    "field_path": "source.sl4.preparation.NaOH_strength",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; SL-4 preparation",
        "exact_source_quote": "First dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution \nof NaOH; then add ferrous sulfate and the trace element solution SL–6.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "Add the source 2 M reagent strength, which is not its addition amount.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "add",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "preparation_notes",
        "stored": "First dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution of NaOH; then add ferrous sulfate and the trace element solution SL-6. \nFirst dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution\r\nof NaOH; then add ferrous sulfate and the trace element solution SL–6.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "SL-4 NaOH addition amount",
    "field_path": "source.sl4.preparation.NaOH_amount",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; SL-4 preparation",
        "exact_source_quote": "First dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution \nof NaOH; then add ferrous sulfate and the trace element solution SL–6.",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "The source fixes reagent strength and pH range but gives no NaOH dose; leave the dose unquantified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "decision": "not_quantified",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
        "field_path": "preparation_steps",
        "decision": "not_quantified",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "preparation_notes",
        "stored": "First dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution of NaOH; then add ferrous sulfate and the trace element solution SL-6. \nFirst dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2 M solution\r\nof NaOH; then add ferrous sulfate and the trace element solution SL–6.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Contextual stock placeholder: Solution A",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution A first composition row",
        "exact_source_quote": "K2HPO4 5.12 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "The contextual dependency still has a See source placeholder and VARIABLE concentration despite a populated composition. It is not a quantified extra ingredient and must not enter the receiving recipe. No fixed placeholder dose can be supplied.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Contextual stock placeholder: Solution B",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Solution B first composition row",
        "exact_source_quote": "NH4Cl 0.30 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "The contextual dependency still has a See source placeholder and VARIABLE concentration despite a populated composition. It is not a quantified extra ingredient and must not enter the receiving recipe. No fixed placeholder dose can be supplied.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Contextual stock placeholder: Trace element solution SL-4",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-4 first composition row",
        "exact_source_quote": "EDTA 0.50 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "The contextual dependency still has a See source placeholder and VARIABLE concentration despite a populated composition. It is not a quantified extra ingredient and must not enter the receiving recipe. No fixed placeholder dose can be supplied.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported"
      }
    ]
  },
  {
    "ingredient_or_context": "Contextual stock placeholder: Trace element solution SL-6",
    "field_path": "ingredients[0].concentration",
    "decision": "unsupported",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_snippets": [
      {
        "source_key": "dsmz471",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf",
        "source_locator": "DSMZ 471 page 1; Trace element solution SL-6 first composition row",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d",
        "parsed_text_sha256": "1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0"
      }
    ],
    "rationale": "The contextual dependency still has a See source placeholder and VARIABLE concentration despite a populated composition. It is not a quantified extra ingredient and must not enter the receiving recipe. No fixed placeholder dose can be supplied.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "unsupported"
      }
    ]
  }
]

### Exact DSMZ/KOMODO 471 identity and maintained ownership

identity: supported. Targets: CultureMech:005585.

The complete primary, exact provider accession and catalog row resolve this one named liquid medium. The generated target has one explicitly named KOMODO owner with the same 17 ingredient nodes and pH. No source accession, title, organism name or fingerprint is treated as independent growth evidence.

### A/B/C and SL-4/SL-6 hierarchy

consistency: concern. Targets: CultureMech:005585.

All sixteen fixed local ingredient values correspond to a stock-stage provider g/L value. A and B are 500 mL preparations; C adds 2 mL SL-4, which itself contains 100 mL SL-6 in 900 mL water. Flattening these values changes the named formulation. The inventory retains every source row, every direct local concentration, both serial doses and conditional nominal-basis arithmetic separately. Existing evidence in contextual stocks supports only those stocks.

### Separate autoclaving and stage-specific pH

completeness: concern. Targets: CultureMech:005585.

Neither target nor owner preserves preparation steps. Source A uses KOH to pH 9.0; the separately autoclaved A/B/C preparations are combined and adjusted to pH 8.2. SL-4 separately uses 2 M NaOH to pH 7.0–8.0 with an ordered dissolution/addition sequence. The primary states no autoclave temperature or duration and no fixed adjustment volumes; none is inferred.

### Supplied forms and valid-but-wrong nickel identity

grounding: concern. Targets: CultureMech:005585.

The exact source explicitly specifies the listed magnesium, iron, zinc, manganese, cobalt, copper and molybdate hydrates. Nickel is also explicitly hexahydrate, whereas CHEBI:34887 has Cl2Ni and mass 129.599. Both primary and current secondary local nickel links therefore omit the supplied hydrate. Other named forms are consistent at the source level; no unspecified calcium hydration or EDTA salt is invented. Provider mmol/L values were not used as source authority; for example its cobalt and nickel calculations do not establish the stated hydrated masses.

### Source category and biological evidence limits

scope: supported. Targets: CultureMech:005585.

DEFINED composition and liquid state agree with the listed chemically specified recipe. The Aerobic: No note is attributable catalog metadata; the primary does not establish growth conditions, tested strains, a growth optimum or oxygen dependence. No taxon IDs, assembly accessions, DOI/PMID or organism-growth claims are present. Generic cultivation application is not a new experimental claim.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:005585.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source enrichment and current generation context

provenance: concern. Targets: CultureMech:005585.

The KOMODO owner records DSMZ composition copying and later pH-buffer extraction. Current importer distinguishes primary stock-addition rows and later stock sections, while its preparation parser still gathers steps from all sections. The current resolver copies ingredients/solutions and only fills a missing scalar pH; these current methods were read but not executed or claimed as historical replay. The generated record reproduces its sole maintained owner.

## Findings

### f1: Stock strengths are presented as the complete medium formula

blocker / open / confirmed; issue key: culturemech.005585.stock-strengths-as-medium.

The sixteen fixed ingredient values are solution A/B and nested SL-4/SL-6 concentrations, without their required preparation volumes and receiving doses. For example the two-step SL-6 → SL-4 → medium dilution is entirely absent. This is a formulation-identity defect despite schema-valid G_PER_L fields.

### f2: Solution A pH is used for the medium and preparation is absent

major / open / confirmed; issue key: culturemech.005585.preparation-ph-scope.

Local ph_value 9.0 belongs to A; the primary and API specify combined pH 8.2. Separate autoclaving of A/B/C and SL-4 dissolution/pH adjustment are missing. Loss of these source-specific stages materially changes preparation, justifying major normalization of native P3.5.

### f3: Nickel hexahydrate is grounded to anhydrous nickel dichloride

major / open / confirmed; issue key: culturemech.005585.nickel-hydrate.

Source and local preferred name explicitly state NiCl2 × 6 H2O, but both term and current secondary link use CHEBI:34887 with anhydrous Cl2Ni. Valid canonical labels and a current MIM row do not validate this source form.

### f4: The retained legacy nitrate identifier is unresolved

major / open / confirmed; issue key: culturemech.005585.legacy-nitrate-key.

The potassium nitrate primary CHEBI:63043 identity is valid, but the retained MediaIngredientMech:000170 has no captured authoritative historical correspondence. Current index/catalog/tree misses and repeated local assertions do not prove the legacy key invalid or justify an automatic replacement.

### f5: Claim-level evidence is missing and four timestamp instances are malformed or naive

minor / open / confirmed; issue key: culturemech.005585.evidence-history.

The target and owner lack attached formulation evidence despite exact accessible primary/provider sources. Each repeats a malformed KOMODO timestamp and a timezone-naive resolver timestamp. The independently evidenced stock compositions are not attachments to this receiving record.

## Recommended Actions And Acceptance Checks

### a1

Restore the named A/B/C and SL-4/SL-6 hierarchy in the maintained owner with exact source amounts, units and batch/dose scope. Preserve conditional provider-volume arithmetic separately. Verify contextual stock records before reuse, including their water percentage artifacts, absent nested SL-6 dose and placeholders.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain A pH 9, combined pH 8.2 and SL-4 pH 7–8 at their own stages, with unquantified KOH/NaOH amounts and 2 M NaOH strength. Add source-specific preparation without inventing an autoclave cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve a source-exact hydrate identifier or explicitly leave the identity unresolved. Preserve the supported 0.02 g stock amount and never derive hydrated molarity from an anhydrous mass.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover authoritative historical correspondence or explicitly retire/reconcile this legacy link through the maintained identifier workflow. Do not change the valid primary nitrate identity merely to increase linkage coverage.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach exact source claims at their corrected solution/ingredient/preparation scope. Preserve historical bytes and append a bounded clarification only when authorized; do not fabricate timezone offsets or transfer stock evidence without receiving-dose scope.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch020/195/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch020/195/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml:1:id: CultureMech:005585<br>./data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml:1:id: CultureMech:005585<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/195/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 29 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| fresh-context-binding | /private/tmp/culturemech-review-work-batch020/source-preflight-bound/195/source-context-current.json; Fresh bound input manifest and explicit old-to-new context transition | context_only | The original preflight evidence context retains its 24a1 provenance. Current native inputs use fresh 033ef569; the two reviewed schema/justfile changes are explicitly bound. Source recipe bytes, captures, timestamps and writer excerpts remain unchanged. |
| dsmz471 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf; Complete one-page official recipe; Solution A, B, C, SL-4 and SL-6 tables and preparation; PDF page visually inspected | supports | The collection specifies five distinct preparation scopes, unquantified adjustment reagents and a combined-medium pH of 8.2. |
| mediadive471 | https://mediadive.dsmz.de/rest/medium/471; $.data.medium and all six solutions, recipe rows, declared volumes and steps | supports | Provider main volume is 1002 mL, with A 500 mL, B 500 mL and C 2 mL; this is a provider nominal basis, not measured final volume. |
| solution966 | https://mediadive.dsmz.de/rest/solution/966; Complete exact solution ID/name, recipe, declared volume and preparation | supports | The independent solution endpoint agrees with the corresponding medium-API scientific fields. Its formulation evidence remains scoped to that stock. |
| solution967 | https://mediadive.dsmz.de/rest/solution/967; Complete exact solution ID/name, recipe, declared volume and preparation | supports | The independent solution endpoint agrees with the corresponding medium-API scientific fields. Its formulation evidence remains scoped to that stock. |
| solution968 | https://mediadive.dsmz.de/rest/solution/968; Complete exact solution ID/name, recipe, declared volume and preparation | supports | The independent solution endpoint agrees with the corresponding medium-API scientific fields. Its formulation evidence remains scoped to that stock. |
| solution969 | https://mediadive.dsmz.de/rest/solution/969; Complete exact solution ID/name, recipe, declared volume and preparation | supports | The independent solution endpoint agrees with the corresponding medium-API scientific fields. Its formulation evidence remains scoped to that stock. |
| solution25 | https://mediadive.dsmz.de/rest/solution/25; Complete exact solution ID/name, recipe, declared volume and preparation | supports | The independent solution endpoint agrees with the corresponding medium-API scientific fields. Its formulation evidence remains scoped to that stock. |
| komodo-list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact catalog row 471 and ID/name/PHInfo/IsComplex/IsAerobic/IsSubMedium headers | supports | KOMODO maps the exact name and accession to DSMZ 471. The catalog oxygen flag is source metadata, not experimental growth evidence. |
| komodo471-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=471; Preserved exact public retrieval result | context_only | The exact KOMODO detail request returned HTTP 403. Its response is preserved; the accessible exact catalog and complete official DSMZ formulation support current identity/formulation, not a replay of the historical import. |
| chebi113455 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_113455; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:113455 resolves to sodium benzoate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32035 resolves to potassium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3312 resolves to calcium dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_4735; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:4735 resolves to ethylenediaminetetraacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63043 resolves to potassium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:113455": [{"label": "Na-benzoate", "match_type": "preferred_term", "identifier": "CHEBI:113455", "preferred_term": "Na-benzoate", "ontology_id": "CHEBI:113455", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32035": [{"label": "KOH", "match_type": "preferred_term", "identifier": "CHEBI:32035", "preferred_term": "KOH", "ontology_id": "CHEBI:32035", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312": [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312", "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:4735": [{"label": "EDTA", "match_type": "preferred_term", "identifier": "CHEBI:4735", "preferred_term": "EDTA", "ontology_id": "CHEBI:4735", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| mim-public-catalog | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Complete pinned public catalog; exact legacy identifier lookup | supports | The current public catalog was inspected for the exact legacy identity; current chemical labels do not authenticate a historical numeric key. |
| mim-public-tree | https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1; Complete untruncated pinned Git tree; exact numeric filename token | supports | The bounded public tree was checked without inferring deletion or universal absence. |
| legacy-lookup | /private/tmp/culturemech-review-work-batch020/195/legacy-identity-context.json; Exact current packaged-index, pinned public catalog/tree and ignored-inclusive local references | context_only | MediaIngredientMech:000170: 0 current exact-key index rows, 0 catalog matches and 0 tree filename matches. Local repeated assertions are not historical identity authority. |
| stock-local-1 | data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml; Entire standalone stock YAML, composition, evidence, references and history | context_only | Bounded contextual dependency only. Existing stock evidence does not transfer to the target or owner. Water percentage artifacts and placeholder fields must not be inherited. |
| stock-local-2 | data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml; Entire standalone stock YAML, composition, evidence, references and history | context_only | Bounded contextual dependency only. Existing stock evidence does not transfer to the target or owner. Water percentage artifacts and placeholder fields must not be inherited. |
| stock-local-4 | data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml; Entire standalone stock YAML, composition, evidence, references and history | context_only | Bounded contextual dependency only. Existing stock evidence does not transfer to the target or owner. Water percentage artifacts and placeholder fields must not be inherited. |
| stock-local-5 | data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml; Entire standalone stock YAML, composition, evidence, references and history | context_only | Bounded contextual dependency only. Existing stock evidence does not transfer to the target or owner. Water percentage artifacts and placeholder fields must not be inherited. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch020/195/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| writer-context-3 | src/culturemech/enrich/dsmz_resolver.py; _build_dsmz_index lines 43–76; merge_composition lines 112–166; _add_enrichment_metadata lines 195–212 | context_only | Exact current source/merge/writer excerpts were read and rechecked against fresh captured inputs. Current implementation is not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 12, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.361707"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml", "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:18:59.361707"}]}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact KOMODO detail request returned HTTP 403. Its response is preserved; the accessible exact catalog and complete official DSMZ formulation support current identity/formulation, not a replay of the historical import.
- Required historical correspondence for MediaIngredientMech:000170 remains unavailable. The completed current lookup does not prove that the old identifier never existed or that the valid current primary CHEBI identity is wrong.
- All four canonical checks passed. Partial completion is due to the unresolved required historical legacy MIM identity, not the assessed current primary formulation or optional KOMODO detail 403.
- The four standalone stocks are contextual dependencies, not separately reviewed targets. No amount, water-percentage artifact, placeholder or quantity evidence is automatically inherited into the medium.
- No final measured volume, adjustment dose, sterilization temperature/duration, growth phenotype or replacement ontology ID was inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121729Z-culturemech-005585-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alcaligenes_xylosoxydans_medium_with_benzoate
  (CultureMech:005585)'
started_at: '2026-10-21T12:11:53Z'
finished_at: '2026-10-21T12:17:29Z'
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
summary: DSMZ 471 is identifiable, but the generated record and sole KOMODO owner
  present solution A/B and nested SL-4/SL-6 stock strengths as final-medium ingredients
  and place solution A pH 9 at medium level. The exact primary requires separate preparation
  and final adjustment to pH 8.2. Chemical-form, evidence and legacy-link issues remain;
  the historical legacy MIM correspondence is unavailable.
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
  - path: data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    sha256: e3ff772c3f60e027dea6180e791f9f0d072f7801299469f7c94ad6caa3090bae
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    sha256: 881f4fdb0258866df28b1fcd7648be616af4696c9bff5f8e8fa2a96c7d521911
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
    sha256: bcf1021fe1ddfe3465a791093ff7f36ad1dbf687017dd085638e82026174c9ce
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml
    sha256: c0f38d4cb23a82ba66c9d48099ae617f360e168d49c221a4af7cf667da7c8ad0
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml
    sha256: dc6fd73ba2f1980ead6de1f347634e6efb7a18b93e8e3facb00fb58653c26bf7
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml
    sha256: 88c0dd4292c4f7a5e3cfa5af0ce58107f8029cef5184b540a661c04f5c87bfb7
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
  selection: Task review 195; batch 020 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding nineteen task batches
    contain 190 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 193 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005585
targets:
- target_id: CultureMech:005585
  path: data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  label: alcaligenes_xylosoxydans_medium_with_benzoate
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch020/195/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/195/strict.tsv"
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:005585
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
  - CultureMech:005585
- check_id: komodo471-source-access
  name: 'Exact source content access: komodo471'
  required: false
  status: unavailable
  summary: The exact KOMODO detail request returned HTTP 403. Its response is preserved;
    the accessible exact catalog and complete official DSMZ formulation support current
    identity/formulation, not a replay of the historical import.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - komodo471-attempt
- check_id: legacy-historical-identity
  name: Historical legacy MIM identifier correspondence
  required: true
  status: unavailable
  summary: MediaIngredientMech:000170 remains unresolved after completed bounded current
    lookups; no authoritative historical correspondence is captured.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - legacy-lookup
  - mim-public-catalog
  - mim-public-tree
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:51.579867Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch020/195/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:52.895796Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-020/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch020/195/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:55.821500Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:12:57.413914Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:17:27Z'
  support: supports
  summary: './data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml:1:id:
    CultureMech:005585

    ./data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml:1:id:
    CultureMech:005585

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/195/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:17:27Z'
  support: supports
  summary: 29 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2d04456d10a9cecbdfc5ae6f1d166d9685dda47d8d9a0bff122a5895b4600549
- evidence_id: fresh-context-binding
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/source-preflight-bound/195/source-context-current.json
  locator: Fresh bound input manifest and explicit old-to-new context transition
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: The original preflight evidence context retains its 24a1 provenance. Current
    native inputs use fresh 033ef569; the two reviewed schema/justfile changes are
    explicitly bound. Source recipe bytes, captures, timestamps and writer excerpts
    remain unchanged.
  snapshot_sha256: c610c855e442b4feb22fecf23ce14852d55feb9b49e2f072355e60b8abb269b9
- evidence_id: dsmz471
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf
  locator: Complete one-page official recipe; Solution A, B, C, SL-4 and SL-6 tables
    and preparation; PDF page visually inspected
  accessed_at: '2026-10-21T11:55:11.392738Z'
  support: supports
  summary: The collection specifies five distinct preparation scopes, unquantified
    adjustment reagents and a combined-medium pH of 8.2.
  snapshot_sha256: 4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d
- evidence_id: mediadive471
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/471
  locator: $.data.medium and all six solutions, recipe rows, declared volumes and
    steps
  accessed_at: '2026-10-21T11:55:10.652131Z'
  support: supports
  summary: Provider main volume is 1002 mL, with A 500 mL, B 500 mL and C 2 mL; this
    is a provider nominal basis, not measured final volume.
  snapshot_sha256: 52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7
- evidence_id: solution966
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/966
  locator: Complete exact solution ID/name, recipe, declared volume and preparation
  accessed_at: '2026-10-21T11:55:47.054034Z'
  support: supports
  summary: The independent solution endpoint agrees with the corresponding medium-API
    scientific fields. Its formulation evidence remains scoped to that stock.
  snapshot_sha256: f414d81544dfd0190d4f142588a9f7dca223f662d4989b046016fb8d20b96225
- evidence_id: solution967
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/967
  locator: Complete exact solution ID/name, recipe, declared volume and preparation
  accessed_at: '2026-10-21T11:55:47.058052Z'
  support: supports
  summary: The independent solution endpoint agrees with the corresponding medium-API
    scientific fields. Its formulation evidence remains scoped to that stock.
  snapshot_sha256: 1de7760bf30db516ef31866d67fa167d002ace198017ef538b3acdbdbee49764
- evidence_id: solution968
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/968
  locator: Complete exact solution ID/name, recipe, declared volume and preparation
  accessed_at: '2026-10-21T11:55:47.679430Z'
  support: supports
  summary: The independent solution endpoint agrees with the corresponding medium-API
    scientific fields. Its formulation evidence remains scoped to that stock.
  snapshot_sha256: bbe7f48a8c64263bbef37f3747d139b8089bb8f135858d5ab5659bcb46df9392
- evidence_id: solution969
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/969
  locator: Complete exact solution ID/name, recipe, declared volume and preparation
  accessed_at: '2026-10-21T11:55:47.686948Z'
  support: supports
  summary: The independent solution endpoint agrees with the corresponding medium-API
    scientific fields. Its formulation evidence remains scoped to that stock.
  snapshot_sha256: 4f223236f3752f3d3b8dc56e873ea633a449771b5fe5388b505a53d61f8a4192
- evidence_id: solution25
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/25
  locator: Complete exact solution ID/name, recipe, declared volume and preparation
  accessed_at: '2026-10-21T11:55:47.053559Z'
  support: supports
  summary: The independent solution endpoint agrees with the corresponding medium-API
    scientific fields. Its formulation evidence remains scoped to that stock.
  snapshot_sha256: eaab23d6c5742d3f51b713dcfd5f1c9717eabcc01e8b035fa6f1a478148c0f4c
- evidence_id: komodo-list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact catalog row 471 and ID/name/PHInfo/IsComplex/IsAerobic/IsSubMedium
    headers
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: KOMODO maps the exact name and accession to DSMZ 471. The catalog oxygen
    flag is source metadata, not experimental growth evidence.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodo471-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=471
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T11:55:10.651303Z'
  support: context_only
  summary: The exact KOMODO detail request returned HTTP 403. Its response is preserved;
    the accessible exact catalog and complete official DSMZ formulation support current
    identity/formulation, not a replay of the historical import.
  snapshot_sha256: 0cb8f5388c7c9389c906bb7e982dd854dd2bf1731e9a87efc7052d85ca9784a0
- evidence_id: chebi113455
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_113455
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:55:11.910151Z'
  support: supports
  summary: CHEBI:113455 resolves to sodium benzoate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ae57ed1c4e8ffdd7909332b3bbe6dcc356a0f03ae779de5a761626ccb6cebfba
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
- evidence_id: chebi32035
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:47.017507Z'
  support: supports
  summary: CHEBI:32035 resolves to potassium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 6ed3df00965b4707265cfced80411c4b1937b727f8c2093addbc467f88ce2ec8
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
- evidence_id: chebi4735
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_4735
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.659368Z'
  support: supports
  summary: CHEBI:4735 resolves to ethylenediaminetetraacetic acid. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: ef8713e257a5e52aa813d8a43a26ed321ff04a475591ff238c00a47758f96717
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
  accessed_at: '2026-10-21T12:17:27Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:113455":
    [{"label": "Na-benzoate", "match_type": "preferred_term", "identifier": "CHEBI:113455",
    "preferred_term": "Na-benzoate", "ontology_id": "CHEBI:113455", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32035": [{"label": "KOH", "match_type":
    "preferred_term", "identifier": "CHEBI:32035", "preferred_term": "KOH", "ontology_id":
    "CHEBI:32035", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312":
    [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3312":
    [{"label": "CaCl2", "match_type": "preferred_term", "identifier": "CHEBI:3312",
    "preferred_term": "CaCl2", "ontology_id": "CHEBI:3312", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:4735": [{"label":
    "EDTA", "match_type": "preferred_term", "identifier": "CHEBI:4735", "preferred_term":
    "EDTA", "ontology_id": "CHEBI:4735", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type":
    "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride
    hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-public-catalog
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Complete pinned public catalog; exact legacy identifier lookup
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: The current public catalog was inspected for the exact legacy identity;
    current chemical labels do not authenticate a historical numeric key.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: mim-public-tree
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/MediaIngredientMech/git/trees/6643131b0f12ab40b66f98135245fca04027e0e9?recursive=1
  locator: Complete untruncated pinned Git tree; exact numeric filename token
  accessed_at: '2026-10-21T09:51:04.602158Z'
  support: supports
  summary: The bounded public tree was checked without inferring deletion or universal
    absence.
  snapshot_sha256: 71721421c6e8100b080d4ee3140f6e0bb4bcd21b57964ceeb61399ca4a2844ec
- evidence_id: legacy-lookup
  kind: search
  reference: /private/tmp/culturemech-review-work-batch020/195/legacy-identity-context.json
  locator: Exact current packaged-index, pinned public catalog/tree and ignored-inclusive
    local references
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: 'MediaIngredientMech:000170: 0 current exact-key index rows, 0 catalog
    matches and 0 tree filename matches. Local repeated assertions are not historical
    identity authority.'
  snapshot_sha256: 3874141e1b0b00d988c7d85dee103065af06423309f066620d2e799029896ad4
  search_scope: Whole current pinned label index, whole captured public catalog and
    untruncated tree; fresh local data/normalized_yaml and src/culturemech/data/mediaingredientmech
    searched with rg --no-ignore --hidden. No unbounded historical/remote absence
    claim.
- evidence_id: stock-local-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml
  locator: Entire standalone stock YAML, composition, evidence, references and history
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Bounded contextual dependency only. Existing stock evidence does not transfer
    to the target or owner. Water percentage artifacts and placeholder fields must
    not be inherited.
  snapshot_sha256: c0f38d4cb23a82ba66c9d48099ae617f360e168d49c221a4af7cf667da7c8ad0
- evidence_id: stock-local-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml
  locator: Entire standalone stock YAML, composition, evidence, references and history
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Bounded contextual dependency only. Existing stock evidence does not transfer
    to the target or owner. Water percentage artifacts and placeholder fields must
    not be inherited.
  snapshot_sha256: dc6fd73ba2f1980ead6de1f347634e6efb7a18b93e8e3facb00fb58653c26bf7
- evidence_id: stock-local-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml
  locator: Entire standalone stock YAML, composition, evidence, references and history
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Bounded contextual dependency only. Existing stock evidence does not transfer
    to the target or owner. Water percentage artifacts and placeholder fields must
    not be inherited.
  snapshot_sha256: 88c0dd4292c4f7a5e3cfa5af0ce58107f8029cef5184b540a661c04f5c87bfb7
- evidence_id: stock-local-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml
  locator: Entire standalone stock YAML, composition, evidence, references and history
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Bounded contextual dependency only. Existing stock evidence does not transfer
    to the target or owner. Water percentage artifacts and placeholder fields must
    not be inherited.
  snapshot_sha256: bcf1021fe1ddfe3465a791093ff7f36ad1dbf687017dd085638e82026174c9ce
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch020/195/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 0b70011d834eb41e827725d23879b3632c11d4dd9faf90adddd77a3995f69e7e
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-context-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570;
    _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps
    lines 653–721
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-context-3
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: _build_dsmz_index lines 43–76; merge_composition lines 112–166; _add_enrichment_metadata
    lines 195–212
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: Exact current source/merge/writer excerpts were read and rechecked against
    fresh captured inputs. Current implementation is not a replay of historical imports.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml;
    data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:17:27Z'
  support: context_only
  summary: '[{"input": "target", "events": 12, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:18:59.361707"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml",
    "events": 11, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:18:59.361707"}]}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '17 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 17/17 primary and 16/17 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Exact supplied-form
    mismatch is addressed separately; valid IDs and labels do not establish correct
    source grounding.'
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi113455
  - chebi131527
  - chebi31206
  - chebi31795
  - chebi32035
  - chebi32312
  - chebi33118
  - chebi3312
  - chebi34887
  - chebi4735
  - chebi53503
  - chebi63036
  - chebi63043
  - chebi75213
  - chebi75836
  - chebi86318
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 17: primary 100.00%;
    secondary 94.12%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 40 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main medium: Solution A\",\n\
    \    \"field_path\": \"source.solution_965.recipe[0]\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"mediadive471api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/471\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"solution\\\": \\\"Solution A\\\",\\n            \
    \            \\\"solution_id\\\": 966,\\n                        \\\"amount\\\"\
    : 500,\\n                        \\\"unit\\\": \\\"ml\\\",\\n                \
    \        \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n        \"\
    source_locator\": \"DSMZ 471 page 1; combined preparation\",\n        \"exact_source_quote\"\
    : \"Autoclave solutions A, B and C separately, combine, adjust pH to 8.2.\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"decision\": \"add\",\n  \
    \      \"stored\": null\n      }\n    ],\n    \"arithmetic\": \"Source amount:\
    \ 500 ml; provider-declared stage volume 1002 mL. \"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main medium: Solution B\",\n    \"field_path\": \"source.solution_965.recipe[1]\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Solution B\\\",\\n                        \\\"solution_id\\\"\
    : 967,\\n                        \\\"amount\\\": 500,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n    \
    \    \"source_locator\": \"DSMZ 471 page 1; combined preparation\",\n        \"\
    exact_source_quote\": \"Autoclave solutions A, B and C separately, combine, adjust\
    \ pH to 8.2.\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"decision\": \"add\",\n  \
    \      \"stored\": null\n      }\n    ],\n    \"arithmetic\": \"Source amount:\
    \ 500 ml; provider-declared stage volume 1002 mL. \"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main medium: Solution C\",\n    \"field_path\": \"source.solution_965.recipe[2]\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    solution\\\": \\\"Solution C\\\",\\n                        \\\"solution_id\\\"\
    : 968,\\n                        \\\"amount\\\": 2,\\n                       \
    \ \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n \
    \                   }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      },\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n    \
    \    \"source_locator\": \"DSMZ 471 page 1; combined preparation\",\n        \"\
    exact_source_quote\": \"Autoclave solutions A, B and C separately, combine, adjust\
    \ pH to 8.2.\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"decision\": \"add\",\n  \
    \      \"stored\": null\n      }\n    ],\n    \"arithmetic\": \"Source amount:\
    \ 2 ml; provider-declared stage volume 1002 mL. \"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A: K2HPO4\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"10.24\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution A table, row 1\",\n\
    \        \"exact_source_quote\": \"K2HPO4 5.12 g\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 5.12,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10.24,\\n        \
    \                \\\"mmol_l\\\": 58.7911,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"10.24\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"10.24\",\n     \
    \     \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml\",\n        \"\
    field_path\": \"composition[0].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"10.24\",\n          \"unit\": \"G_PER_L\"\n        },\n   \
    \     \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 5.12 g; provider-declared stage volume 500 mL. Conditional provider-basis\
    \ check only: 10.24 g/L × 0.5 L equivalent stock per listed batch = 5.120 g; division\
    \ by provider main 1.002 L gives 5.109780439121756487025948104 g/L. This is not\
    \ an independently measured final volume or an instruction to replace the source\
    \ stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A:\
    \ KH2PO4\",\n    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"3\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution A table, row 2\",\n\
    \        \"exact_source_quote\": \"KH2PO4 1.50 g\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n                  \
    \      \\\"mmol_l\\\": 22.045,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"3\",\n         \
    \ \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 1.5 g; provider-declared stage volume 500 mL. Conditional provider-basis\
    \ check only: 3 g/L × 0.5 L equivalent stock per listed batch = 1.5 g; division\
    \ by provider main 1.002 L gives 1.497005988023952095808383234 g/L. This is not\
    \ an independently measured final volume or an instruction to replace the source\
    \ stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution A:\
    \ Distilled water\",\n    \"field_path\": \"source.solution_966.recipe[2]\",\n\
    \    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution A table, row 3\",\n\
    \        \"exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 500,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred. The standalone\
    \ dependency retains an incorrect water percentage; correct its source water volume\
    \ before reuse.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\",\n   \
    \     \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"PERCENT_V_V\"\n \
    \       },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Source amount: 500 ml; provider-declared stage volume 500 mL. \"\n  },\n \
    \ {\n    \"ingredient_or_context\": \"Solution B: NH4Cl\",\n    \"field_path\"\
    : \"ingredients[2].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.6\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n        \"\
    source_locator\": \"DSMZ 471 page 1; Solution B table, row 1\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.30 g\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 0.3,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.6,\\n                \
    \        \\\"mmol_l\\\": 11.217,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.6\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.6\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\",\n        \"field_path\"\
    : \"composition[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.6\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source amount: 0.3 g; provider-declared\
    \ stage volume 500 mL. Conditional provider-basis check only: 0.6 g/L × 0.5 L\
    \ equivalent stock per listed batch = 0.30 g; division by provider main 1.002\
    \ L gives 0.2994011976047904191616766467 g/L. This is not an independently measured\
    \ final volume or an instruction to replace the source stock formulation.\"\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Solution B: CaCl2\",\n    \"field_path\"\
    : \"ingredients[3].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"0.02\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n        \"\
    source_locator\": \"DSMZ 471 page 1; Solution B table, row 2\",\n        \"exact_source_quote\"\
    : \"CaCl2 0.01 g\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"CaCl2\\\",\\n                        \\\"compound_id\\\": 81,\\\
    n                        \\\"amount\\\": 0.01,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\n         \
    \               \\\"mmol_l\\\": 0.180213,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.02\",\n      \
    \    \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\",\n        \"field_path\"\
    : \"composition[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source amount: 0.01 g;\
    \ provider-declared stage volume 500 mL. Conditional provider-basis check only:\
    \ 0.02 g/L × 0.5 L equivalent stock per listed batch = 0.010 g; division by provider\
    \ main 1.002 L gives 0.009980039920159680638722554890 g/L. This is not an independently\
    \ measured final volume or an instruction to replace the source stock formulation.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Solution B: MgSO4 x 7 H2O\",\n \
    \   \"field_path\": \"ingredients[4].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": {\n      \"value\": \"0.4\",\n      \"unit\": \"G_PER_L\"\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz471\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution B table, row 3\",\n\
    \        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.20 g\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.4,\\n  \
    \                      \\\"mmol_l\\\": 1.62288,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.4\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\",\n        \"field_path\"\
    : \"composition[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source amount: 0.2 g; provider-declared\
    \ stage volume 500 mL. Conditional provider-basis check only: 0.4 g/L × 0.5 L\
    \ equivalent stock per listed batch = 0.20 g; division by provider main 1.002\
    \ L gives 0.1996007984031936127744510978 g/L. This is not an independently measured\
    \ final volume or an instruction to replace the source stock formulation.\"\n\
    \  },\n  {\n    \"ingredient_or_context\": \"Solution B: KNO3\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : {\n      \"value\": \"4\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n        \"\
    source_locator\": \"DSMZ 471 page 1; Solution B table, row 4\",\n        \"exact_source_quote\"\
    : \"KNO3 2.00 g\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KNO3\\\",\\n                        \\\"compound_id\\\": 191,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 4,\\n                  \
    \      \\\"mmol_l\\\": 39.5636,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"4\",\n         \
    \ \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 2 g; provider-declared stage volume 500 mL. Conditional provider-basis\
    \ check only: 4 g/L × 0.5 L equivalent stock per listed batch = 2.0 g; division\
    \ by provider main 1.002 L gives 1.996007984031936127744510978 g/L. This is not\
    \ an independently measured final volume or an instruction to replace the source\
    \ stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"Solution B:\
    \ Na-benzoate\",\n    \"field_path\": \"ingredients[6].concentration\",\n    \"\
    decision\": \"correct\",\n    \"local\": {\n      \"value\": \"1.84\",\n     \
    \ \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution B table, row 5\",\n\
    \        \"exact_source_quote\": \"Na-benzoate 0.92 g\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Na-benzoate\\\",\\n                        \\\"compound_id\\\
    \": 295,\\n                        \\\"amount\\\": 0.92,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1.84,\\\
    n                        \\\"mmol_l\\\": 12.7686,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n      }\n\
    \    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"1.84\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"1.84\",\n      \
    \    \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\",\n        \"field_path\"\
    : \"composition[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.84\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source amount: 0.92 g;\
    \ provider-declared stage volume 500 mL. Conditional provider-basis check only:\
    \ 1.84 g/L × 0.5 L equivalent stock per listed batch = 0.920 g; division by provider\
    \ main 1.002 L gives 0.9181636726546906187624750499 g/L. This is not an independently\
    \ measured final volume or an instruction to replace the source stock formulation.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Solution B: Distilled water\",\n\
    \    \"field_path\": \"source.solution_967.recipe[5]\",\n    \"decision\": \"\
    add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution B table, row 6\",\n\
    \        \"exact_source_quote\": \"Distilled water 500.00 ml\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 500,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"L\"\n        },\n  \
    \      \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 500 ml; provider-declared stage volume 500 mL. \"\n  },\n  {\n    \"\
    ingredient_or_context\": \"Solution C: Trace element solution SL-4\",\n    \"\
    field_path\": \"source.solution_968.recipe[0]\",\n    \"decision\": \"add\",\n\
    \    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution C table, row 1\",\n\
    \        \"exact_source_quote\": \"Trace element solution SL-4 2.00 ml\",\n  \
    \      \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-4\\\",\\n                        \\\
    \"solution_id\\\": 969,\\n                        \\\"amount\\\": 2,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"decision\": \"add\",\n  \
    \      \"stored\": null\n      }\n    ],\n    \"arithmetic\": \"Source amount:\
    \ 2 ml; provider-declared stage volume 2 mL. \"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-4: EDTA\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.5\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-4\
    \ table, row 1\",\n        \"exact_source_quote\": \"EDTA 0.50 g\",\n        \"\
    snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"EDTA\\\",\\n                        \\\"compound_id\\\": 271,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n                \
    \        \\\"mmol_l\\\": 1.71092,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.5\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 0.5 g; provider-declared stage volume 1000 mL. Conditional provider-basis\
    \ check only: 0.5 g/L × 0.002 L equivalent stock per listed batch = 0.0010 g;\
    \ division by provider main 1.002 L gives 0.0009980039920159680638722554890 g/L.\
    \ This is not an independently measured final volume or an instruction to replace\
    \ the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Trace element solution SL-4: FeSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[8].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.2\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-4\
    \ table, row 2\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 0.20 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 0.719386,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n      }\n\
    \    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.2\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 0.2 g; provider-declared stage volume 1000 mL. Conditional provider-basis\
    \ check only: 0.2 g/L × 0.002 L equivalent stock per listed batch = 0.0004 g;\
    \ division by provider main 1.002 L gives 0.0003992015968063872255489021956 g/L.\
    \ This is not an independently measured final volume or an instruction to replace\
    \ the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Trace element solution SL-4: Trace element solution SL-6\",\n    \"field_path\"\
    : \"source.solution_969.recipe[2]\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz471\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-4\
    \ table, row 3\",\n        \"exact_source_quote\": \"Trace element solution SL-6\
    \ 100.00 ml\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    solution\\\": \\\"Trace element solution SL-6\\\",\\n                        \\\
    \"solution_id\\\": 25,\\n                        \\\"amount\\\": 100,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"decision\": \"add\",\n  \
    \      \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"arithmetic\": \"Source amount:\
    \ 100 ml; provider-declared stage volume 1000 mL. \"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-4: Distilled water\",\n    \"field_path\": \"source.solution_969.recipe[3]\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n        \"\
    source_locator\": \"DSMZ 471 page 1; Trace element solution SL-4 table, row 4\"\
    ,\n        \"exact_source_quote\": \"Distilled water 900.00 ml\",\n        \"\
    snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 900,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred. The standalone\
    \ dependency retains an incorrect water percentage; correct its source water volume\
    \ before reuse.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n\
    \    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n       \
    \ \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\",\n   \
    \     \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"PERCENT_V_V\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Source amount: 900 ml; provider-declared stage volume 1000 mL. \"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Trace element solution SL-6: ZnSO4 x 7\
    \ H2O\",\n    \"field_path\": \"ingredients[9].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": {\n      \"value\": \"0.1\",\n      \"unit\": \"\
    G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 1\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.10 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.347752,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n      }\n\
    \    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.1\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 0.1 g; provider-declared stage volume 1000 mL. Conditional provider-basis\
    \ check only: 0.1 g/L × 0.0002 L equivalent stock per listed batch = 0.00002 g;\
    \ division by provider main 1.002 L gives 0.00001996007984031936127744510978 g/L.\
    \ This is not an independently measured final volume or an instruction to replace\
    \ the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Trace element solution SL-6: MnCl2 x 4 H2O\",\n    \"field_path\": \"ingredients[10].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.03\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 2\",\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 0.03 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 0.03,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.03,\\\
    n                        \\\"mmol_l\\\": 0.151588,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n      }\n\
    \    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.03\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.03\",\n      \
    \    \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Source amount: 0.03 g; provider-declared stage volume 1000 mL. Conditional\
    \ provider-basis check only: 0.03 g/L × 0.0002 L equivalent stock per listed batch\
    \ = 0.000006 g; division by provider main 1.002 L gives 0.000005988023952095808383233532934\
    \ g/L. This is not an independently measured final volume or an instruction to\
    \ replace the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-6: H3BO3\",\n    \"field_path\": \"ingredients[11].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.3\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 3\",\n        \"exact_source_quote\": \"H3BO3 0.30 g\",\n       \
    \ \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 0.3,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n                \
    \        \\\"mmol_l\\\": 4.85123,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.3\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 0.3 g; provider-declared stage volume 1000 mL. Conditional provider-basis\
    \ check only: 0.3 g/L × 0.0002 L equivalent stock per listed batch = 0.00006 g;\
    \ division by provider main 1.002 L gives 0.00005988023952095808383233532934 g/L.\
    \ This is not an independently measured final volume or an instruction to replace\
    \ the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Trace element solution SL-6: CoCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[12].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.2\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 4\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 0.20 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.54037,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"The local number matches a provider stock\
    \ strength but is asserted as a direct medium concentration. Restore the named\
    \ source solution and nested receiving doses; attach evidence at that stage. Keep\
    \ the source stock number distinct from any conditional final calculation.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.2\",\n       \
    \   \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 0.2 g; provider-declared stage volume 1000 mL. Conditional provider-basis\
    \ check only: 0.2 g/L × 0.0002 L equivalent stock per listed batch = 0.00004 g;\
    \ division by provider main 1.002 L gives 0.00003992015968063872255489021956 g/L.\
    \ This is not an independently measured final volume or an instruction to replace\
    \ the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\": \"\
    Trace element solution SL-6: CuCl2 x 2 H2O\",\n    \"field_path\": \"ingredients[13].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.01\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 5\",\n        \"exact_source_quote\": \"CuCl2 x 2 H2O 0.01 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 0.01,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.01,\\\
    n                        \\\"mmol_l\\\": 0.0586569,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n     \
    \ }\n    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.01\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.01\",\n      \
    \    \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Source amount: 0.01 g; provider-declared stage volume 1000 mL. Conditional\
    \ provider-basis check only: 0.01 g/L × 0.0002 L equivalent stock per listed batch\
    \ = 0.000002 g; division by provider main 1.002 L gives 0.000001996007984031936127744510978\
    \ g/L. This is not an independently measured final volume or an instruction to\
    \ replace the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-6: NiCl2 x 6 H2O\",\n    \"field_path\": \"ingredients[14].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.02\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 6\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 0.02 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 0.02,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.154322,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n      }\n\
    \    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.02\",\n      \
    \    \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Source amount: 0.02 g; provider-declared stage volume 1000 mL. Conditional\
    \ provider-basis check only: 0.02 g/L × 0.0002 L equivalent stock per listed batch\
    \ = 0.000004 g; division by provider main 1.002 L gives 0.000003992015968063872255489021956\
    \ g/L. This is not an independently measured final volume or an instruction to\
    \ replace the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-6: Na2MoO4 x 2 H2O\",\n    \"field_path\": \"ingredients[15].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": {\n      \"value\": \"0.03\"\
    ,\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ table, row 7\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.03 g\"\
    ,\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.03,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.03,\\n\
    \                        \\\"mmol_l\\\": 0.123993,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\n      }\n\
    \    ],\n    \"rationale\": \"The local number matches a provider stock strength\
    \ but is asserted as a direct medium concentration. Restore the named source solution\
    \ and nested receiving doses; attach evidence at that stage. Keep the source stock\
    \ number distinct from any conditional final calculation.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"0.03\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"0.03\",\n      \
    \    \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Source amount: 0.03 g; provider-declared stage volume 1000 mL. Conditional\
    \ provider-basis check only: 0.03 g/L × 0.0002 L equivalent stock per listed batch\
    \ = 0.000006 g; division by provider main 1.002 L gives 0.000005988023952095808383233532934\
    \ g/L. This is not an independently measured final volume or an instruction to\
    \ replace the source stock formulation.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Trace element solution SL-6: Distilled water\",\n    \"field_path\": \"source.solution_25.recipe[7]\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n        \"\
    source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6 table, row 8\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"\
    snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"mediadive471api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve this original amount and unit\
    \ at its named source stage. It is absent as a distinct stock-dose/water claim\
    \ in target and owner; no density or final volume is inferred.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"decision\": \"add\",\n        \"stored\": null\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        },\n    \
    \    \"decision\": \"verified\"\n      }\n    ],\n    \"arithmetic\": \"Source\
    \ amount: 1000 ml; provider-declared stage volume 1000 mL. \"\n  },\n  {\n   \
    \ \"ingredient_or_context\": \"Provider declared volume: Main sol. 471\",\n  \
    \  \"field_path\": \"source.solution_965.declared_volume\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive471api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/471\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1002\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Record the source-declared volume as provenance\
    \ for its stage. It is not an independently measured final volume and does not\
    \ erase unquantified pH-adjustment additions.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"arithmetic\": \"1002 mL; no conversion to\
    \ a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Provider\
    \ declared volume: Solution A\",\n    \"field_path\": \"source.solution_966.declared_volume\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[1].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 500\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Record the source-declared volume as provenance\
    \ for its stage. It is not an independently measured final volume and does not\
    \ erase unquantified pH-adjustment additions.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"arithmetic\": \"500 mL; no conversion to a\
    \ measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Provider\
    \ declared volume: Solution B\",\n    \"field_path\": \"source.solution_967.declared_volume\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[2].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 500\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Record the source-declared volume as provenance\
    \ for its stage. It is not an independently measured final volume and does not\
    \ erase unquantified pH-adjustment additions.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"arithmetic\": \"500 mL; no conversion to a\
    \ measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Provider\
    \ declared volume: Solution C\",\n    \"field_path\": \"source.solution_968.declared_volume\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[3].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 2\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Record the source-declared volume as provenance\
    \ for its stage. It is not an independently measured final volume and does not\
    \ erase unquantified pH-adjustment additions.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"arithmetic\": \"2 mL; no conversion to a measured\
    \ final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Provider declared\
    \ volume: Trace element solution SL-4\",\n    \"field_path\": \"source.solution_969.declared_volume\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[4].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1000\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Record the source-declared volume as provenance\
    \ for its stage. It is not an independently measured final volume and does not\
    \ erase unquantified pH-adjustment additions.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"arithmetic\": \"1000 mL; no conversion to\
    \ a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"Provider\
    \ declared volume: Trace element solution SL-6\",\n    \"field_path\": \"source.solution_25.declared_volume\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive471api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/471\",\n        \"source_locator\":\
    \ \"$.data.solutions[5].volume\",\n        \"exact_source_quote\": \"\\\"volume\\\
    \": 1000\",\n        \"snapshot_sha256\": \"52bc32e777a598c99d98e45743790c0377342f7355e7cbb04580173a2c4df3a7\"\
    \n      }\n    ],\n    \"rationale\": \"Record the source-declared volume as provenance\
    \ for its stage. It is not an independently measured final volume and does not\
    \ erase unquantified pH-adjustment additions.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"arithmetic\": \"1000 mL; no conversion to\
    \ a measured final volume.\"\n  },\n  {\n    \"ingredient_or_context\": \"KOH\
    \ adjustment amount\",\n    \"field_path\": \"ingredients[16].concentration\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local\": {\n      \"value\": \"\
    variable\",\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution A preparation\",\n\
    \        \"exact_source_quote\": \"Adjust pH to 9.0 with KOH.\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"The collection does not specify a KOH\
    \ dose. Retain nonnumeric quantity but restore solution A scope and evidence;\
    \ do not invent a strength or final-medium concentration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"decision\": \"correct\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"decision\"\
    : \"correct\",\n        \"stored\": {\n          \"value\": \"variable\",\n  \
    \        \"unit\": \"VARIABLE\"\n        }\n      }\n    ]\n  },\n  {\n    \"\
    ingredient_or_context\": \"Solution A pH endpoint versus local medium pH\",\n\
    \    \"field_path\": \"ph_value\",\n    \"decision\": \"correct\",\n    \"local\"\
    : 9.0,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz471\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution A preparation\",\n\
    \        \"exact_source_quote\": \"Adjust pH to 9.0 with KOH.\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      },\n      {\n        \"source_key\": \"dsmz471\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\",\n    \
    \    \"source_locator\": \"DSMZ 471 page 1; combined preparation\",\n        \"\
    exact_source_quote\": \"Autoclave solutions A, B and C separately, combine, adjust\
    \ pH to 8.2.\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"Local scalar 9.0 is the preparation endpoint\
    \ of A, not the combined medium. Preserve A pH 9.0 separately and represent combined\
    \ pH 8.2.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"\
    layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"field_path\"\
    : \"ph_value\",\n        \"decision\": \"correct\",\n        \"stored\": 9.0\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"decision\": \"correct\",\n\
    \        \"stored\": 9.0\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"SL-4 pH range\",\n    \"field_path\": \"source.sl4.preparation.pH\",\n   \
    \ \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; SL-4 preparation\",\n      \
    \  \"exact_source_quote\": \"First dissolve EDTA in distilled water by adjusting\
    \ the pH to 7.0 - 8.0 using a 2 M solution \\nof NaOH; then add ferrous sulfate\
    \ and the trace element solution SL–6.\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"Add the source pH 7.0–8.0 range at SL-4\
    \ preparation, not at medium level.\",\n    \"action_taken\": \"Review only; no\
    \ recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"decision\"\
    : \"add\",\n        \"stored\": null\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"First\
    \ dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2\
    \ M solution of NaOH; then add ferrous sulfate and the trace element solution\
    \ SL-6. \\nFirst dissolve EDTA in distilled water by adjusting the pH to 7.0 -\
    \ 8.0 using a 2 M solution\\r\\nof NaOH; then add ferrous sulfate and the trace\
    \ element solution SL–6.\",\n        \"decision\": \"evidence_only\"\n      }\n\
    \    ]\n  },\n  {\n    \"ingredient_or_context\": \"SL-4 NaOH reagent strength\"\
    ,\n    \"field_path\": \"source.sl4.preparation.NaOH_strength\",\n    \"decision\"\
    : \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; SL-4 preparation\",\n      \
    \  \"exact_source_quote\": \"First dissolve EDTA in distilled water by adjusting\
    \ the pH to 7.0 - 8.0 using a 2 M solution \\nof NaOH; then add ferrous sulfate\
    \ and the trace element solution SL–6.\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"Add the source 2 M reagent strength, which\
    \ is not its addition amount.\",\n    \"action_taken\": \"Review only; no recipe\
    \ change.\",\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"add\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"First\
    \ dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2\
    \ M solution of NaOH; then add ferrous sulfate and the trace element solution\
    \ SL-6. \\nFirst dissolve EDTA in distilled water by adjusting the pH to 7.0 -\
    \ 8.0 using a 2 M solution\\r\\nof NaOH; then add ferrous sulfate and the trace\
    \ element solution SL–6.\",\n        \"decision\": \"evidence_only\"\n      }\n\
    \    ]\n  },\n  {\n    \"ingredient_or_context\": \"SL-4 NaOH addition amount\"\
    ,\n    \"field_path\": \"source.sl4.preparation.NaOH_amount\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; SL-4 preparation\",\n      \
    \  \"exact_source_quote\": \"First dissolve EDTA in distilled water by adjusting\
    \ the pH to 7.0 - 8.0 using a 2 M solution \\nof NaOH; then add ferrous sulfate\
    \ and the trace element solution SL–6.\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"The source fixes reagent strength and\
    \ pH range but gives no NaOH dose; leave the dose unquantified.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps\"\
    ,\n        \"decision\": \"not_quantified\",\n        \"stored\": null\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"decision\": \"not_quantified\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"preparation_notes\",\n        \"stored\": \"First\
    \ dissolve EDTA in distilled water by adjusting the pH to 7.0 - 8.0 using a 2\
    \ M solution of NaOH; then add ferrous sulfate and the trace element solution\
    \ SL-6. \\nFirst dissolve EDTA in distilled water by adjusting the pH to 7.0 -\
    \ 8.0 using a 2 M solution\\r\\nof NaOH; then add ferrous sulfate and the trace\
    \ element solution SL–6.\",\n        \"decision\": \"evidence_only\"\n      }\n\
    \    ]\n  },\n  {\n    \"ingredient_or_context\": \"Contextual stock placeholder:\
    \ Solution A\",\n    \"field_path\": \"ingredients[0].concentration\",\n    \"\
    decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"variable\"\
    ,\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution A first composition\
    \ row\",\n        \"exact_source_quote\": \"K2HPO4 5.12 g\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"The contextual dependency still has a\
    \ See source placeholder and VARIABLE concentration despite a populated composition.\
    \ It is not a quantified extra ingredient and must not enter the receiving recipe.\
    \ No fixed placeholder dose can be supplied.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/mediadive_966_Solution_A.yaml\",\n \
    \       \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Contextual stock placeholder: Solution B\",\n\
    \    \"field_path\": \"ingredients[0].concentration\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz471\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Solution B first composition\
    \ row\",\n        \"exact_source_quote\": \"NH4Cl 0.30 g\",\n        \"snapshot_sha256\"\
    : \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\",\n    \
    \    \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"The contextual dependency still has a\
    \ See source placeholder and VARIABLE concentration despite a populated composition.\
    \ It is not a quantified extra ingredient and must not enter the receiving recipe.\
    \ No fixed placeholder dose can be supplied.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/mediadive_967_Solution_B.yaml\",\n \
    \       \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Contextual stock placeholder: Trace element\
    \ solution SL-4\",\n    \"field_path\": \"ingredients[0].concentration\",\n  \
    \  \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"variable\"\
    ,\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-4\
    \ first composition row\",\n        \"exact_source_quote\": \"EDTA 0.50 g\",\n\
    \        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"The contextual dependency still has a\
    \ See source placeholder and VARIABLE concentration despite a populated composition.\
    \ It is not a quantified extra ingredient and must not enter the receiving recipe.\
    \ No fixed placeholder dose can be supplied.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/mediadive_969_Trace_element_solution_SL-4.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  },\n  {\n\
    \    \"ingredient_or_context\": \"Contextual stock placeholder: Trace element\
    \ solution SL-6\",\n    \"field_path\": \"ingredients[0].concentration\",\n  \
    \  \"decision\": \"unsupported\",\n    \"local\": {\n      \"value\": \"variable\"\
    ,\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz471\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium471.pdf\"\
    ,\n        \"source_locator\": \"DSMZ 471 page 1; Trace element solution SL-6\
    \ first composition row\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.10\
    \ g\",\n        \"snapshot_sha256\": \"4fd2d7af6099afcc47920d83bd46e865018bf380dea6abcd232621695a4a066d\"\
    ,\n        \"parsed_text_sha256\": \"1a38c512693443972b54fe994f6a87002c77da303aaea457897eacf51a8fffe0\"\
    \n      }\n    ],\n    \"rationale\": \"The contextual dependency still has a\
    \ See source placeholder and VARIABLE concentration despite a populated composition.\
    \ It is not a quantified extra ingredient and must not enter the receiving recipe.\
    \ No fixed placeholder dose can be supplied.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"unsupported\"\n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact DSMZ/KOMODO 471 identity and maintained ownership
  outcome: supported
  summary: The complete primary, exact provider accession and catalog row resolve
    this one named liquid medium. The generated target has one explicitly named KOMODO
    owner with the same 17 ingredient nodes and pH. No source accession, title, organism
    name or fingerprint is treated as independent growth evidence.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - mediadive471
  - komodo-list
- assessment_id: stock-scope
  area: consistency
  topic: A/B/C and SL-4/SL-6 hierarchy
  outcome: concern
  summary: All sixteen fixed local ingredient values correspond to a stock-stage provider
    g/L value. A and B are 500 mL preparations; C adds 2 mL SL-4, which itself contains
    100 mL SL-6 in 900 mL water. Flattening these values changes the named formulation.
    The inventory retains every source row, every direct local concentration, both
    serial doses and conditional nominal-basis arithmetic separately. Existing evidence
    in contextual stocks supports only those stocks.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - mediadive471
  - quantity-inventory
  - stock-local-1
  - stock-local-2
  - stock-local-4
  - stock-local-5
- assessment_id: preparation
  area: completeness
  topic: Separate autoclaving and stage-specific pH
  outcome: concern
  summary: Neither target nor owner preserves preparation steps. Source A uses KOH
    to pH 9.0; the separately autoclaved A/B/C preparations are combined and adjusted
    to pH 8.2. SL-4 separately uses 2 M NaOH to pH 7.0–8.0 with an ordered dissolution/addition
    sequence. The primary states no autoclave temperature or duration and no fixed
    adjustment volumes; none is inferred.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Supplied forms and valid-but-wrong nickel identity
  outcome: concern
  summary: The exact source explicitly specifies the listed magnesium, iron, zinc,
    manganese, cobalt, copper and molybdate hydrates. Nickel is also explicitly hexahydrate,
    whereas CHEBI:34887 has Cl2Ni and mass 129.599. Both primary and current secondary
    local nickel links therefore omit the supplied hydrate. Other named forms are
    consistent at the source level; no unspecified calcium hydration or EDTA salt
    is invented. Provider mmol/L values were not used as source authority; for example
    its cobalt and nickel calculations do not establish the stated hydrated masses.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - chebi34887
  - chebi53503
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Source category and biological evidence limits
  outcome: supported
  summary: 'DEFINED composition and liquid state agree with the listed chemically
    specified recipe. The Aerobic: No note is attributable catalog metadata; the primary
    does not establish growth conditions, tested strains, a growth optimum or oxygen
    dependence. No taxon IDs, assembly accessions, DOI/PMID or organism-growth claims
    are present. Generic cultivation application is not a new experimental claim.'
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - owner-0
  - dsmz471
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
  - CultureMech:005585
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: generation
  area: provenance
  topic: Source enrichment and current generation context
  outcome: concern
  summary: The KOMODO owner records DSMZ composition copying and later pH-buffer extraction.
    Current importer distinguishes primary stock-addition rows and later stock sections,
    while its preparation parser still gathers steps from all sections. The current
    resolver copies ingredients/solutions and only fills a missing scalar pH; these
    current methods were read but not executed or claimed as historical replay. The
    generated record reproduces its sole maintained owner.
  target_ids:
  - CultureMech:005585
  evidence_ids:
  - record
  - owner-0
  - writer-context-0
  - writer-context-1
  - writer-context-2
  - writer-context-3
findings:
- finding_id: f1
  issue_key: culturemech.005585.stock-strengths-as-medium
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock strengths are presented as the complete medium formula
  description: The sixteen fixed ingredient values are solution A/B and nested SL-4/SL-6
    concentrations, without their required preparation volumes and receiving doses.
    For example the two-step SL-6 → SL-4 → medium dilution is entirely absent. This
    is a formulation-identity defect despite schema-valid G_PER_L fields.
  target_ids:
  - CultureMech:005585
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - mediadive471
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  issue_key: culturemech.005585.preparation-ph-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Solution A pH is used for the medium and preparation is absent
  description: Local ph_value 9.0 belongs to A; the primary and API specify combined
    pH 8.2. Separate autoclaving of A/B/C and SL-4 dissolution/pH adjustment are missing.
    Loss of these source-specific stages materially changes preparation, justifying
    major normalization of native P3.5.
  target_ids:
  - CultureMech:005585
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[16]
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.005585.nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel dichloride
  description: Source and local preferred name explicitly state NiCl2 × 6 H2O, but
    both term and current secondary link use CHEBI:34887 with anhydrous Cl2Ni. Valid
    canonical labels and a current MIM row do not validate this source form.
  target_ids:
  - CultureMech:005585
  field_paths:
  - ingredients[14].term
  - ingredients[14].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  issue_key: culturemech.005585.legacy-nitrate-key
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The retained legacy nitrate identifier is unresolved
  description: The potassium nitrate primary CHEBI:63043 identity is valid, but the
    retained MediaIngredientMech:000170 has no captured authoritative historical correspondence.
    Current index/catalog/tree misses and repeated local assertions do not prove the
    legacy key invalid or justify an automatic replacement.
  target_ids:
  - CultureMech:005585
  field_paths:
  - ingredients[5].mediaingredientmech_term
  evidence_ids:
  - record
  - owner-0
  - chebi63043
  - legacy-lookup
  - mim-public-catalog
  - mim-public-tree
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.1
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.005585.evidence-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Claim-level evidence is missing and four timestamp instances are malformed
    or naive
  description: The target and owner lack attached formulation evidence despite exact
    accessible primary/provider sources. Each repeats a malformed KOMODO timestamp
    and a timezone-naive resolver timestamp. The independently evidenced stock compositions
    are not attachments to this receiving record.
  target_ids:
  - CultureMech:005585
  field_paths:
  - ingredients
  - evidence
  - references
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - record
  - owner-0
  - dsmz471
  - quantity-inventory
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  description: Restore the named A/B/C and SL-4/SL-6 hierarchy in the maintained owner
    with exact source amounts, units and batch/dose scope. Preserve conditional provider-volume
    arithmetic separately. Verify contextual stock records before reuse, including
    their water percentage artifacts, absent nested SL-6 dose and placeholders.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005585
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  description: Retain A pH 9, combined pH 8.2 and SL-4 pH 7–8 at their own stages,
    with unquantified KOH/NaOH amounts and 2 M NaOH strength. Add source-specific
    preparation without inventing an autoclave cycle.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005585
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  description: Resolve a source-exact hydrate identifier or explicitly leave the identity
    unresolved. Preserve the supported 0.02 g stock amount and never derive hydrated
    molarity from an anhydrous mass.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005585
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  description: Recover authoritative historical correspondence or explicitly retire/reconcile
    this legacy link through the maintained identifier workflow. Do not change the
    valid primary nitrate identity merely to increase linkage coverage.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005585
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
  description: Attach exact source claims at their corrected solution/ingredient/preparation
    scope. Preserve historical bytes and append a bounded clarification only when
    authorized; do not fabricate timezone offsets or transfer stock evidence without
    receiving-dose scope.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005585
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml
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
- The exact KOMODO detail request returned HTTP 403. Its response is preserved; the
  accessible exact catalog and complete official DSMZ formulation support current
  identity/formulation, not a replay of the historical import.
- Required historical correspondence for MediaIngredientMech:000170 remains unavailable.
  The completed current lookup does not prove that the old identifier never existed
  or that the valid current primary CHEBI identity is wrong.
- All four canonical checks passed. Partial completion is due to the unresolved required
  historical legacy MIM identity, not the assessed current primary formulation or
  optional KOMODO detail 403.
- The four standalone stocks are contextual dependencies, not separately reviewed
  targets. No amount, water-percentage artifact, placeholder or quantity evidence
  is automatically inherited into the medium.
- No final measured volume, adjustment dose, sterilization temperature/duration, growth
  phenotype or replacement ontology ID was inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-020
- generated-medium
```
