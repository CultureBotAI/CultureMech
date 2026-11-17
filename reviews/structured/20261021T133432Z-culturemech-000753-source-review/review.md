# Source and formulation review: alkaliphilus_medium (CultureMech:000753)

- Review: 20261021T133432Z-culturemech-000753-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:27:12Z
- Finished UTC: 2026-10-21T13:34:32Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The 31-ingredient flat record combines concentrations from solutions A, B and D and undiluted mineral/vitamin stocks, including two summed salts, instead of preserving DSMZ 1290’s staged 950/25/1/25 mL assembly. Nickel hexahydrate is grounded to an anhydrous term, and mineral-stock pH instructions are flattened into the main preparation. Current source amounts and product qualifiers support bounded curation without treating the 1001 mL declared basis as measured final volume.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 225; batch 023 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-two task batches contain 220 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 223 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000753 | data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml | generated | alkaliphilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000753 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000753 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/225/strict.tsv |
| validate-terms | passed | True | CultureMech:000753 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000753 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000753 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000753.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:000753.

29 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 29/31 primary and 28/31 secondary instances; all asserted mediaingredientmech_chebi_term keys have exact pinned MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 31: primary 93.55%; secondary 90.32%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000753.

56 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Main sol. 1290 / Solution A",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 2585,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Main sol. 1290 subsection, recipe row 1",
        "exact_source_quote": "Solution A 950.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1290 / Solution B",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 2586,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Main sol. 1290 subsection, recipe row 2",
        "exact_source_quote": "Solution B 25.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1290 / Solution C",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 5986,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Main sol. 1290 subsection, recipe row 3",
        "exact_source_quote": "Solution C 1.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Main sol. 1290 / Solution D",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 2587,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Main sol. 1290 subsection, recipe row 4",
        "exact_source_quote": "Solution D 25.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A / NaCl",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 75,\n                        \"unit\": \"g\",\n                        \"g_l\": 78.9474,\n                        \"mmol_l\": 1350.91,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 1",
        "exact_source_quote": "NaCl 75.00 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local merged salt value adds concentrations from solution A and undiluted mineral stock. Preserve both source rows separately, then apply only the documented 10 mL stock transfer. Neither summing unlike stage concentrations nor silently choosing a duplicate is valid.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "79.9474",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "79.9474",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L mineral-stock basis, for NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered. For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally delivered. These conditional delivered masses depend on the provider stock-volume declaration; the primary lists water and titration without a measured final stock volume. Final medium g/L is not asserted."
  },
  {
    "ingredient_or_context": "Solution A / MgSO4 x 7 H2O",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 8.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.26316,\n                        \"mmol_l\": 37.5824,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 2",
        "exact_source_quote": "MgSO4 x 7 H2O 8.80 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local merged salt value adds concentrations from solution A and undiluted mineral stock. Preserve both source rows separately, then apply only the documented 10 mL stock transfer. Neither summing unlike stage concentrations nor silently choosing a duplicate is valid.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "12.26316",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "12.26316",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L mineral-stock basis, for NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered. For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally delivered. These conditional delivered masses depend on the provider stock-volume declaration; the primary lists water and titration without a measured final stock volume. Final medium g/L is not asserted."
  },
  {
    "ingredient_or_context": "Solution A / KCl",
    "field_path": "ingredients[2].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.05263,\n                        \"mmol_l\": 14.1198,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 3",
        "exact_source_quote": "KCl 1.00 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.05263",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1.05263",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "1 g in the declared 950 mL solution A is carried into the listed assembly; its stock g/L is not final medium g/L."
  },
  {
    "ingredient_or_context": "Solution A / Yeast extract",
    "field_path": "ingredients[3].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"OXOID\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.5263,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 4",
        "exact_source_quote": "Yeast extract (OXOID) 10.00 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.5263",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "10.5263",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "10 g in the declared 950 mL solution A is carried into the listed assembly; its stock g/L is not final medium g/L."
  },
  {
    "ingredient_or_context": "Solution A / Trypticase peptone",
    "field_path": "ingredients[4].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.5263,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 5",
        "exact_source_quote": "Trypticase peptone (BD BBL) 10.00 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "10.5263",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "10.5263",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "10 g in the declared 950 mL solution A is carried into the listed assembly; its stock g/L is not final medium g/L."
  },
  {
    "ingredient_or_context": "Solution A / Modified Wolin's mineral solution",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 6",
        "exact_source_quote": "Modified Wolin's mineral solution 10.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution A / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 940,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution A subsection, recipe row 7",
        "exact_source_quote": "Distilled water 940.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution B / D-Glucose",
    "field_path": "ingredients[5].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 100,\n                        \"mmol_l\": 555.062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution B subsection, recipe row 1",
        "exact_source_quote": "D-Glucose 2.50 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "2.5 g in 25 mL component solution is transferred with that solution; local stock strength 100 g/L is not final medium concentration."
  },
  {
    "ingredient_or_context": "Solution B / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution B subsection, recipe row 2",
        "exact_source_quote": "Distilled water 25.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution C / Wolin's vitamin solution (10x)",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[3].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution C subsection, recipe row 1",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Solution D / Na-thioglycolate",
    "field_path": "ingredients[6].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[4].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-thioglycolate\",\n                        \"compound_id\": 30,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 175.286,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution D subsection, recipe row 1",
        "exact_source_quote": "Na-thioglycolate 0.50 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "0.5 g in 25 mL component solution is transferred with that solution; local stock strength 20 g/L is not final medium concentration."
  },
  {
    "ingredient_or_context": "Solution D / Na-ascorbate",
    "field_path": "ingredients[7].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[4].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na-ascorbate\",\n                        \"compound_id\": 311,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 100.956,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution D subsection, recipe row 2",
        "exact_source_quote": "Na-ascorbate 0.50 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "0.5 g in 25 mL component solution is transferred with that solution; local stock strength 20 g/L is not final medium concentration."
  },
  {
    "ingredient_or_context": "Solution D / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[4].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Solution D subsection, recipe row 3",
        "exact_source_quote": "Distilled water 25.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / Nitrilotriacetic acid",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 1",
        "exact_source_quote": "Nitrilotriacetic acid 1.50 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 1.5 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / MgSO4 x 7 H2O",
    "field_path": "ingredients[1].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 2",
        "exact_source_quote": "MgSO4 x 7 H2O 3.00 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local merged salt value adds concentrations from solution A and undiluted mineral stock. Preserve both source rows separately, then apply only the documented 10 mL stock transfer. Neither summing unlike stage concentrations nor silently choosing a duplicate is valid.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "12.26316",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "12.26316",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L mineral-stock basis, for NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered. For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally delivered. These conditional delivered masses depend on the provider stock-volume declaration; the primary lists water and titration without a measured final stock volume. Final medium g/L is not asserted."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / MnSO4 x H2O",
    "field_path": "ingredients[9].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 3",
        "exact_source_quote": "MnSO4 x H2O 0.50 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.5 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / NaCl",
    "field_path": "ingredients[0].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 4",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local merged salt value adds concentrations from solution A and undiluted mineral stock. Preserve both source rows separately, then apply only the documented 10 mL stock transfer. Neither summing unlike stage concentrations nor silently choosing a duplicate is valid.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "79.9474",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "79.9474",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L mineral-stock basis, for NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered. For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally delivered. These conditional delivered masses depend on the provider stock-volume declaration; the primary lists water and titration without a measured final stock volume. Final medium g/L is not asserted."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / FeSO4 x 7 H2O",
    "field_path": "ingredients[10].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 5",
        "exact_source_quote": "FeSO4 x 7 H2O 0.10 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.1 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / CoSO4 x 7 H2O",
    "field_path": "ingredients[11].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 6",
        "exact_source_quote": "CoSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.18 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / CaCl2 x 2 H2O",
    "field_path": "ingredients[12].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 7",
        "exact_source_quote": "CaCl2 x 2 H2O 0.10 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.1 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / ZnSO4 x 7 H2O",
    "field_path": "ingredients[13].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 8",
        "exact_source_quote": "ZnSO4 x 7 H2O 0.18 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.18",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.18 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / CuSO4 x 5 H2O",
    "field_path": "ingredients[14].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 9",
        "exact_source_quote": "CuSO4 x 5 H2O 0.01 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.01 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / AlK(SO4)2 x 12 H2O",
    "field_path": "ingredients[15].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 10",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.02 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.02 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / H3BO3",
    "field_path": "ingredients[16].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 11",
        "exact_source_quote": "H3BO3 0.01 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.01 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / Na2MoO4 x 2 H2O",
    "field_path": "ingredients[17].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 12",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.01 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.01 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / NiCl2 x 6 H2O",
    "field_path": "ingredients[18].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 13",
        "exact_source_quote": "NiCl2 x 6 H2O 0.03 g",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.03 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / Na2SeO3 x 5 H2O",
    "field_path": "ingredients[19].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 14",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.30 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.0003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.0003 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / Na2WO4 x 2 H2O",
    "field_path": "ingredients[20].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 15",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.40 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.0004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.0004 × 0.010 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Modified Wolin's mineral solution / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[5].recipe[15]",
        "exact_source_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Modified Wolin's mineral solution subsection, recipe row 16",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Biotin",
    "field_path": "ingredients[21].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 1",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.02 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Folic acid",
    "field_path": "ingredients[22].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 2",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.02 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Pyridoxine hydrochloride",
    "field_path": "ingredients[23].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 3",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.1 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Thiamine HCl",
    "field_path": "ingredients[24].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 4",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Riboflavin",
    "field_path": "ingredients[25].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 5",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Nicotinic acid",
    "field_path": "ingredients[26].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 6",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Calcium D-(+)-pantothenate",
    "field_path": "ingredients[27].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 7",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Vitamin B12",
    "field_path": "ingredients[28].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 8",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.001 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / p-Aminobenzoic acid",
    "field_path": "ingredients[29].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 9",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / (DL)-alpha-Lipoic acid",
    "field_path": "ingredients[30].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 10",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The local g/L value belongs to a component solution or undiluted nested stock, not the completed medium. Restore the original batch amount, stock volume and receiving dose; retain current rounding as historical local data, not an exact final concentration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Conditional on the provider-declared nominal 1 L stock basis: reported stock g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured final stock and medium volumes after pH adjustment are unspecified."
  },
  {
    "ingredient_or_context": "Wolin's vitamin solution (10x) / Distilled water",
    "field_path": "solutions",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1290api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1290",
        "source_locator": "$.data.solutions[6].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2"
      },
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Wolin's vitamin solution (10x) subsection, recipe row 11",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "This explicit stock receiving dose or solvent quantity is absent from a source-scoped local representation. Restore it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient. Existing preparation text is preserved separately.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Initial A pH",
    "field_path": "preparation.Initial_A_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "adjust pH to 8.0 with 1 N NaOH",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Preserved initial pH and 1 N reagent strength need attached evidence; actual titrant dose is unspecified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Boiling duration",
    "field_path": "preparation.Boiling_duration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "boil medium for 1\nmin",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "One-minute boiling applies to solution A before cooling, not a fabricated autoclave duration.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "A cooling gas",
    "field_path": "preparation.A_cooling_gas",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "cool to room temperature under 100% N2 gas atmosphere",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Preserved 100% N2 atmosphere needs claim evidence; absolute gas volume/flow is unspecified.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "B/C/D preparation gas",
    "field_path": "preparation.B/C/D_preparation_gas",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "solutions B, C and D prepared under 100% N2 gas",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Preserve separate stocks and filtration under the stated gas; this is not autoclaving every component together.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Completed-medium pH",
    "field_path": "preparation.Completed-medium_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "the completed medium to 8.0",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Main pH 8.0 is present but lacks attached source evidence; stock endpoints differ.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 8.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.0,
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Final acid strength",
    "field_path": "preparation.Final_acid_strength",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "0.1 N HCl",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Retain conditional sterile anoxic acid strength without inventing its dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Final base strength",
    "field_path": "preparation.Final_base_strength",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "0.1 N NaOH",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Retain conditional sterile anoxic base strength without inventing its dose.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "evidence_only"
      }
    ]
  },
  {
    "ingredient_or_context": "Mineral initial pH",
    "field_path": "preparation.Mineral_initial_pH",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "adjust pH to 6.5 with KOH",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Literal endpoint is preserved in main preparation but belongs to the mineral stock; restore stock scope and attach evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Mineral final pH",
    "field_path": "preparation.Mineral_final_pH",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "final to pH 7.0 with KOH",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Literal endpoint is preserved in main preparation but belongs to the mineral stock; restore stock scope and attach evidence.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "correct"
      }
    ]
  },
  {
    "ingredient_or_context": "Vitamin concentration factor",
    "field_path": "preparation.Vitamin_concentration_factor",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Exact main preparation or named stock subsection",
        "exact_source_quote": "Wolin's vitamin solution (10x)",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "Restore exact 10x stock identity separately from its 1 mL dose; do not substitute the tenfold weaker DSMZ141 vitamin stock.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Titration dose",
    "field_path": "preparation.Titration_dose",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Conditional adjustment prose",
        "exact_source_quote": "if\nnecessary.",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The source specifies endpoints/conditions rather than a fixed titrant amount. No mass, volume or normality is inferred for unspecified KOH.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete the medium by adding appropriate amounts of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.",
        "decision": "not_quantified"
      }
    ]
  },
  {
    "ingredient_or_context": "Mineral KOH dose",
    "field_path": "preparation.Mineral_KOH_dose",
    "decision": "not_quantified",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1290",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf",
        "source_locator": "Conditional adjustment prose",
        "exact_source_quote": "with KOH, then add minerals. Adjust",
        "snapshot_sha256": "ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d",
        "parsed_text_sha256": "c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4"
      }
    ],
    "rationale": "The source specifies endpoints/conditions rather than a fixed titrant amount. No mass, volume or normality is inferred for unspecified KOH.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.",
        "decision": "not_quantified"
      }
    ]
  }
]

### Exact DSMZ1290 identity and nested-stock dependencies

identity: supported. Targets: CultureMech:000753.

The target and unique maintained CM000753 owner resolve to DSMZ1290. Main assembly uses A 950, B 25, C 1 and D 25 mL. Exact mineral241 and vitamin5980 sources are scoped to DSMZ141 mineral and DSMZ120 tenfold vitamin subsections; parent organisms, recipes and variants are not inherited.

### Every flat concentration versus its actual source stage

consistency: concern. Targets: CultureMech:000753.

All 62 local concentrations are covered by 44 source recipe rows plus quantitative preparation decisions. Local NaCl 79.9474 and magnesium sulfate 12.26316 g/L explicitly sum solution-A concentrations and undiluted mineral strengths. On the provider’s nominal 1 L mineral-stock basis, 75.01 g NaCl and 8.83 g magnesium sulfate heptahydrate would be delivered from listed A plus 10 mL stock. The primary water/titration description does not independently establish measured final stock volume. D-glucose 100 and both reducing-agent 20 g/L values are component-stock strengths. Mineral and vitamin rows likewise require 10 mL and 1 mL transfers. The 950+25+1+25=1001 mL sum agrees with the provider declaration but does not establish measured post-titration volume.

### Hydrates, stereochemistry and product qualifiers

grounding: concern. Targets: CultureMech:000753.

NiCl2·6H2O source and preferred name conflict with CHEBI:34887, whose 2Cl.Ni formula has no crystal water. The other explicit salt hydrates, D-glucose, calcium D-(+)-pantothenate and stereochemically unspecified lipoic-acid term do not establish a comparable contradiction. The source says generic Na-ascorbate while CHEBI:113451 has L-specific structure; that specificity is not independently established by the recipe text. Current source yeast extract OXOID and trypticase BD BBL qualifiers should remain attached to the intended products. No unverified replacement identifier or supplier equivalence is proposed.

### Preserved main prose with missing solution hierarchy

completeness: concern. Targets: CultureMech:000753.

The main pH 8.0, 1 N NaOH, one-minute boil, 100% N2, autoclaving A, filtration of B/C/D and conditional final 0.1 N acid/base are retained but unlinked to evidence. A/B/C/D are not represented, and mineral-stock pH 6.5→7.0 is placed as a main-medium step. Restore source scope without replacing final pH 8.0 or inventing an autoclave cycle.

### Complex liquid and biological claim boundaries

scope: supported. Targets: CultureMech:000753.

COMPLEX/UNDEFINED and LIQUID fit the yeast/trypticase liquid formulation. No specific strain, taxon, assembly, DOI/PMID or growth claim is asserted. Dependency parent media provide only the named stock definitions.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:000753.

17 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Inherited flattening and cleanup history

provenance: concern. Targets: CultureMech:000753.

Both local layers retain the same 31 flat ingredients and duplicate-sum notes. Current importer separates the primary formulation from later stock definitions, while its preparation reader iterates solution steps; current cleanup no longer silently sums conflicting quantities. These current functions explain maintenance boundaries, not historical replay. Stock hierarchy and source evidence require explicit owner curation before regeneration.

## Findings

### f1: Different solution concentrations are flattened and summed

blocker / open / confirmed; issue key: culturemech.000753.stock-flattening.

The record represents four component solutions and nested mineral/vitamin stocks as one undiluted ingredient list. It sums two salts across incompatible stages and exposes component glucose100 g/L and reducing agents 20 g/L as final medium concentrations. The required assembly doses and solvent stages are absent.

### f2: Nickel hexahydrate is grounded to an unhydrated term

major / open / confirmed; issue key: culturemech.000753.nickel-form.

The source and local name specify NiCl2·6H2O, but the asserted primary and secondary CHEBI:34887 term has formula 2Cl.Ni without water. Correct labels and resolver passes do not support the supplied hydrate.

### f3: Stock pH instructions are presented as main-medium preparation

major / open / confirmed; issue key: culturemech.000753.preparation-scope.

The second step gives mineral pH 6.5→7.0 without a mineral-stock object, while the first refers to undefined A/B/C/D. Correct literal numbers lack the scope needed for faithful preparation.

### f4: Product and ascorbate specificity lack direct source linkage

minor / open / confirmed; issue key: culturemech.000753.source-specificity.

Source OXOID yeast and BD BBL trypticase qualifiers are omitted; generic Na-ascorbate is associated with an L-specific structural term without a product specification establishing that choice. These bounded provenance limits should remain visible alongside the material stock errors.

## Recommended Actions And Acceptance Checks

### a1

Restore A/B/C/D and both nested stocks with exact batch amounts, solvent quantities and receiving doses, removing unsupported cross-stage sums through explicit curation. Preserve nominal provider bases, rounding limits and unknown post-titration volume. Attach exact evidence before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve the exact source hydrate before assigning a supported identifier in both linkage fields. Preserve the 0.03 g stock batch mass and proper stock dilution; do not substitute anhydrous mass or invent a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the main pH 8.0 sequence and move mineral instructions into the restored stock definition with evidence. Retain separate autoclaving/filtration stages and unquantified titrant doses; no generic cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach source product qualifiers and exact amount evidence; confirm the intended ascorbate specificity before asserting a product-level match. Preserve generic source wording and do not infer an alternative isomer.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkaliphilus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch023/225/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/225/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml:1:id: CultureMech:000753<br>./data/normalized_yaml/bacterial/alkaliphilus_medium.yaml:1:id: CultureMech:000753<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/225/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 39 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/225/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| dsmz1290 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf; Complete exact main recipe, A/B/C/D and both nested stock definitions; all preparation | supports | All source stages, original amounts, declared provider volumes, supplier qualifiers and preparation compared. |
| mediadive1290api | https://mediadive.dsmz.de/rest/medium/1290; Complete exact main recipe, A/B/C/D and both nested stock definitions; all preparation | supports | All source stages, original amounts, declared provider volumes, supplier qualifiers and preparation compared. |
| dsmz141 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf; Modified Wolin mineral subsection only | supports | Exact stock dependency; parent-medium recipes and variants are not transferred. |
| dsmz120 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf; Wolin vitamin solution (10x) subsection only | supports | Exact stock dependency; parent-medium recipes and variants are not transferred. |
| solution2585 | https://mediadive.dsmz.de/rest/solution/2585; Complete exact stock endpoint | supports | Identity and recipe correspond to the explicitly nested DSMZ1290 stock; standalone stock concentration is not final medium concentration. |
| solution2586 | https://mediadive.dsmz.de/rest/solution/2586; Complete exact stock endpoint | supports | Identity and recipe correspond to the explicitly nested DSMZ1290 stock; standalone stock concentration is not final medium concentration. |
| solution5986 | https://mediadive.dsmz.de/rest/solution/5986; Complete exact stock endpoint | supports | Identity and recipe correspond to the explicitly nested DSMZ1290 stock; standalone stock concentration is not final medium concentration. |
| solution2587 | https://mediadive.dsmz.de/rest/solution/2587; Complete exact stock endpoint | supports | Identity and recipe correspond to the explicitly nested DSMZ1290 stock; standalone stock concentration is not final medium concentration. |
| solution241 | https://mediadive.dsmz.de/rest/solution/241; Complete exact stock endpoint | supports | Identity and recipe correspond to the explicitly nested DSMZ1290 stock; standalone stock concentration is not final medium concentration. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; Complete exact stock endpoint | supports | Identity and recipe correspond to the explicitly nested DSMZ1290 stock; standalone stock concentration is not final medium concentration. |
| chebi113451 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_113451; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:113451 resolves to sodium ascorbate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86481 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86481 resolves to sodium thioglycolate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:113451": [{"label": "Na-ascorbate", "match_type": "preferred_term", "identifier": "CHEBI:113451", "preferred_term": "Na-ascorbate", "ontology_id": "CHEBI:113451", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86481": [{"label": "Na-thioglycolate", "match_type": "preferred_term", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch023/225/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch023/225/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/alkaliphilus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml", "events": 8, "timestamp_issues": []}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The 1001 mL component sum/provider declaration is a nominal basis, not measured final volume after pH adjustment. No exact final concentration or titrant dose is invented.
- DSMZ141 and DSMZ120 contribute only the explicitly named mineral and 10x vitamin subsections. Their main recipes, other stocks and strain variants are outside this record.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133432Z-culturemech-000753-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilus_medium (CultureMech:000753)'
started_at: '2026-10-21T13:27:12Z'
finished_at: '2026-10-21T13:34:32Z'
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
summary: The 31-ingredient flat record combines concentrations from solutions A, B
  and D and undiluted mineral/vitamin stocks, including two summed salts, instead
  of preserving DSMZ 1290’s staged 950/25/1/25 mL assembly. Nickel hexahydrate is
  grounded to an anhydrous term, and mineral-stock pH instructions are flattened into
  the main preparation. Current source amounts and product qualifiers support bounded
  curation without treating the 1001 mL declared basis as measured final volume.
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
  - path: data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
    sha256: e6c937b678ac55da02994345bae88970b167f9439b9d256448ed5217804c69f4
    role: target
  - path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
    sha256: 2c27f77f97f98d909957b6c474bb84728f463896352d5c897b50732aeecb318b
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
  selection: Task review 225; batch 023 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-two task batches
    contain 220 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 223 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000753
targets:
- target_id: CultureMech:000753
  path: data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  label: alkaliphilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch023/225/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/225/strict.tsv"
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000753
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
  - CultureMech:000753
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:48.421022Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/225/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:50.027018Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/225/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:51.934662Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:53.099905Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:34:31Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml:1:id: CultureMech:000753

    ./data/normalized_yaml/bacterial/alkaliphilus_medium.yaml:1:id: CultureMech:000753

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/225/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:34:31Z'
  support: supports
  summary: 39 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a2ff23f86eeb9ba759a0ce37e720a4b73e0be47b110343dd3a898b74eedf7726
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/225/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 605c466e9a973e7fa243efe799173359266814e4608ef1cf8883fc8df6a78810
- evidence_id: dsmz1290
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf
  locator: Complete exact main recipe, A/B/C/D and both nested stock definitions;
    all preparation
  accessed_at: '2026-10-21T13:13:20.671556Z'
  support: supports
  summary: All source stages, original amounts, declared provider volumes, supplier
    qualifiers and preparation compared.
  snapshot_sha256: ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d
- evidence_id: mediadive1290api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1290
  locator: Complete exact main recipe, A/B/C/D and both nested stock definitions;
    all preparation
  accessed_at: '2026-10-21T13:13:18.385897Z'
  support: supports
  summary: All source stages, original amounts, declared provider volumes, supplier
    qualifiers and preparation compared.
  snapshot_sha256: f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2
- evidence_id: dsmz141
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf
  locator: Modified Wolin mineral subsection only
  accessed_at: '2026-10-21T10:13:12.306566Z'
  support: supports
  summary: Exact stock dependency; parent-medium recipes and variants are not transferred.
  snapshot_sha256: 8d5190815050377b0f25907bf14c294bc3301fe968697b37c66eb9db5a287ac8
- evidence_id: dsmz120
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf
  locator: Wolin vitamin solution (10x) subsection only
  accessed_at: '2026-10-21T13:16:27.298931Z'
  support: supports
  summary: Exact stock dependency; parent-medium recipes and variants are not transferred.
  snapshot_sha256: e1f85e4a546abc825218226bbb18d78bd9c054b7e11399aa7161ad259a3b663f
- evidence_id: solution2585
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2585
  locator: Complete exact stock endpoint
  accessed_at: '2026-10-21T13:16:26.639177Z'
  support: supports
  summary: Identity and recipe correspond to the explicitly nested DSMZ1290 stock;
    standalone stock concentration is not final medium concentration.
  snapshot_sha256: 8c8a9f011902bec9b3e2765d7b9916dce6e253814402e29ebc895ea7364d4e96
- evidence_id: solution2586
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2586
  locator: Complete exact stock endpoint
  accessed_at: '2026-10-21T13:16:26.639125Z'
  support: supports
  summary: Identity and recipe correspond to the explicitly nested DSMZ1290 stock;
    standalone stock concentration is not final medium concentration.
  snapshot_sha256: dd02c6463a9daac7cb62e5cfc55d7f1e7148ecfaefb704fe9acb8f36460cbbc5
- evidence_id: solution5986
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5986
  locator: Complete exact stock endpoint
  accessed_at: '2026-10-21T13:16:27.284943Z'
  support: supports
  summary: Identity and recipe correspond to the explicitly nested DSMZ1290 stock;
    standalone stock concentration is not final medium concentration.
  snapshot_sha256: 9a7b10344c212b56fcd049dd194bdd8602edc6ec66d034477356df68e9351d03
- evidence_id: solution2587
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/2587
  locator: Complete exact stock endpoint
  accessed_at: '2026-10-21T13:16:26.639250Z'
  support: supports
  summary: Identity and recipe correspond to the explicitly nested DSMZ1290 stock;
    standalone stock concentration is not final medium concentration.
  snapshot_sha256: f335f5ec006f6dfcf7ee1cbe7a0ab8fd4eb96a70a8b9746edf10fddc8941113c
- evidence_id: solution241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/241
  locator: Complete exact stock endpoint
  accessed_at: '2026-10-21T10:37:16.846684Z'
  support: supports
  summary: Identity and recipe correspond to the explicitly nested DSMZ1290 stock;
    standalone stock concentration is not final medium concentration.
  snapshot_sha256: 50cc42c209f550b7abc4a5f48b455553516220b6ef9613f481941f9e15f0b25d
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: Complete exact stock endpoint
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Identity and recipe correspond to the explicitly nested DSMZ1290 stock;
    standalone stock concentration is not final medium concentration.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: chebi113451
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_113451
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:13:21.400613Z'
  support: supports
  summary: CHEBI:113451 resolves to sodium ascorbate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2ee1727c4615c7e3df0efc6c2ec9cf5eb507aa5d27e97433b74e83ee68c1e9fc
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
- evidence_id: chebi86481
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:41.310467Z'
  support: supports
  summary: CHEBI:86481 resolves to sodium thioglycolate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 444afd61f333b50a1be0a902c67c78c7b97483187e4fb554b6f7deeb009cd966
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
  accessed_at: '2026-10-21T13:34:31Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:113451":
    [{"label": "Na-ascorbate", "match_type": "preferred_term", "identifier": "CHEBI:113451",
    "preferred_term": "Na-ascorbate", "ontology_id": "CHEBI:113451", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term":
    "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED",
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
    "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:176843": [{"label": "Vitamin
    B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
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
    "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O",
    "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id":
    "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86481":
    [{"label": "Na-thioglycolate", "match_type": "preferred_term", "identifier": "CHEBI:86481",
    "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/225/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 9b58d14f1af37ad37fe3a0636ed04abc446417d7bf9a1ad87646a9f859893a79
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/225/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: 81ee6b0c706e01b5e8b6fce338a0808d74d1ad9d0fb5d79fa90d28ad026f24bc
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T13:34:31Z'
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
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_MEDIUM.yaml; data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:34:31Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaliphilus_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '29 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 29/31 primary and 28/31 secondary
    instances; all asserted mediaingredientmech_chebi_term keys have exact pinned
    MIM rows. Exact supplied-form mismatch is addressed separately; valid IDs and
    labels do not establish correct source grounding.'
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi113451
  - chebi131361
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17634
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi49105
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi86158
  - chebi86364
  - chebi86465
  - chebi86481
  - chebi91244
  details: 'Instance coverage on a 0–100 percent scale, denominator 31: primary 93.55%;
    secondary 90.32%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 56 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Main sol. 1290 / Solution A\"\
    ,\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"solution\\\": \\\"Solution A\\\",\\n                        \\\"solution_id\\\
    \": 2585,\\n                        \\\"amount\\\": 950,\\n                  \
    \      \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1290 subsection, recipe row 1\",\n     \
    \   \"exact_source_quote\": \"Solution A 950.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1290 / Solution B\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"solution\\\
    \": \\\"Solution B\\\",\\n                        \\\"solution_id\\\": 2586,\\\
    n                        \\\"amount\\\": 25,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1290 subsection, recipe row 2\",\n     \
    \   \"exact_source_quote\": \"Solution B 25.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1290 / Solution C\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 3,\\n                        \\\"solution\\\
    \": \\\"Solution C\\\",\\n                        \\\"solution_id\\\": 5986,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1290 subsection, recipe row 3\",\n     \
    \   \"exact_source_quote\": \"Solution C 1.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Main sol. 1290 / Solution D\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\": \"\
    $.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 4,\\n                        \\\"solution\\\
    \": \\\"Solution D\\\",\\n                        \\\"solution_id\\\": 2587,\\\
    n                        \\\"amount\\\": 25,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Main sol. 1290 subsection, recipe row 4\",\n     \
    \   \"exact_source_quote\": \"Solution D 25.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / NaCl\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 75,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 78.9474,\\n            \
    \            \\\"mmol_l\\\": 1350.91,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution A subsection, recipe row 1\",\n        \"\
    exact_source_quote\": \"NaCl 75.00 g\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local merged salt value adds concentrations\
    \ from solution A and undiluted mineral stock. Preserve both source rows separately,\
    \ then apply only the documented 10 mL stock transfer. Neither summing unlike\
    \ stage concentrations nor silently choosing a duplicate is valid.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"79.9474\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"79.9474\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L mineral-stock basis, for\
    \ NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered.\
    \ For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally\
    \ delivered. These conditional delivered masses depend on the provider stock-volume\
    \ declaration; the primary lists water and titration without a measured final\
    \ stock volume. Final medium g/L is not asserted.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / MgSO4 x 7 H2O\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 8.8,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 9.26316,\\\
    n                        \\\"mmol_l\\\": 37.5824,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Solution A subsection, recipe row 2\",\n    \
    \    \"exact_source_quote\": \"MgSO4 x 7 H2O 8.80 g\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local merged salt value adds concentrations\
    \ from solution A and undiluted mineral stock. Preserve both source rows separately,\
    \ then apply only the documented 10 mL stock transfer. Neither summing unlike\
    \ stage concentrations nor silently choosing a duplicate is valid.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"12.26316\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.26316\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L mineral-stock basis, for\
    \ NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered.\
    \ For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally\
    \ delivered. These conditional delivered masses depend on the provider stock-volume\
    \ declaration; the primary lists water and titration without a measured final\
    \ stock volume. Final medium g/L is not asserted.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / KCl\",\n    \"field_path\": \"ingredients[2].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.05263,\\n            \
    \            \\\"mmol_l\\\": 14.1198,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution A subsection, recipe row 3\",\n        \"\
    exact_source_quote\": \"KCl 1.00 g\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.05263\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.05263\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"1 g in the declared 950 mL solution A is carried into the listed assembly;\
    \ its stock g/L is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / Yeast extract\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"OXOID\\\",\\n       \
    \                 \\\"amount\\\": 10,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 10.5263,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution A subsection, recipe row 4\",\n        \"\
    exact_source_quote\": \"Yeast extract (OXOID) 10.00 g\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10.5263\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.5263\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"10 g in the declared 950 mL solution A is carried into the listed assembly;\
    \ its stock g/L is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / Trypticase peptone\",\n    \"field_path\": \"ingredients[4].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Trypticase peptone\\\",\\n                        \\\"compound_id\\\
    \": 124,\\n                        \\\"attribute\\\": \\\"BD BBL\\\",\\n     \
    \                   \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 10.5263,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution A subsection, recipe row 5\",\n        \"\
    exact_source_quote\": \"Trypticase peptone (BD BBL) 10.00 g\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10.5263\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.5263\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"10 g in the declared 950 mL solution A is carried into the listed assembly;\
    \ its stock g/L is not final medium g/L.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / Modified Wolin's mineral solution\",\n    \"field_path\": \"\
    solutions\",\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    solution\\\": \\\"Modified Wolin's mineral solution\\\",\\n                  \
    \      \\\"solution_id\\\": 241,\\n                        \\\"amount\\\": 10,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Solution A subsection, recipe row 6\",\n    \
    \    \"exact_source_quote\": \"Modified Wolin's mineral solution 10.00 ml\",\n\
    \        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution A / Distilled water\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\": \"\
    $.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 8,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 940,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution A subsection, recipe row 7\",\n        \"\
    exact_source_quote\": \"Distilled water 940.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution B / D-Glucose\",\n    \"field_path\": \"ingredients[5].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"D-Glucose\\\",\\n                        \\\"compound_id\\\"\
    : 211,\\n                        \\\"amount\\\": 2.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 100,\\n  \
    \                      \\\"mmol_l\\\": 555.062,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution B subsection, recipe row 1\",\n        \"\
    exact_source_quote\": \"D-Glucose 2.50 g\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"100\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"2.5\
    \ g in 25 mL component solution is transferred with that solution; local stock\
    \ strength 100 g/L is not final medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution B / Distilled water\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\": \"\
    $.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 2,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 25,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution B subsection, recipe row 2\",\n        \"\
    exact_source_quote\": \"Distilled water 25.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution C / Wolin's vitamin solution (10x)\",\n    \"field_path\": \"solutions\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[3].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    solution\\\": \\\"Wolin's vitamin solution (10x)\\\",\\n                     \
    \   \\\"solution_id\\\": 5980,\\n                        \\\"amount\\\": 1,\\\
    n                        \\\"unit\\\": \\\"ml\\\",\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Solution C subsection, recipe row 1\",\n    \
    \    \"exact_source_quote\": \"Wolin's vitamin solution (10x) 1.00 ml\",\n   \
    \     \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution D / Na-thioglycolate\",\n    \"field_path\": \"ingredients[6].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Na-thioglycolate\\\",\\n                        \\\"compound_id\\\
    \": 30,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n  \
    \                      \\\"mmol_l\\\": 175.286,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution D subsection, recipe row 1\",\n        \"\
    exact_source_quote\": \"Na-thioglycolate 0.50 g\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"0.5\
    \ g in 25 mL component solution is transferred with that solution; local stock\
    \ strength 20 g/L is not final medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution D / Na-ascorbate\",\n    \"field_path\": \"ingredients[7].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[4].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Na-ascorbate\\\",\\n                        \\\"compound_id\\\
    \": 311,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n \
    \                       \\\"mmol_l\\\": 100.956,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution D subsection, recipe row 2\",\n        \"\
    exact_source_quote\": \"Na-ascorbate 0.50 g\",\n        \"snapshot_sha256\": \"\
    ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n        \"\
    parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"0.5\
    \ g in 25 mL component solution is transferred with that solution; local stock\
    \ strength 20 g/L is not final medium concentration.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Solution D / Distilled water\",\n    \"field_path\": \"solutions\",\n    \"\
    decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"\
    https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\": \"\
    $.data.solutions[4].recipe[2]\",\n        \"exact_source_quote\": \"{\\n     \
    \                   \\\"recipe_order\\\": 3,\\n                        \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\": 4,\\\
    n                        \\\"amount\\\": 25,\\n                        \\\"unit\\\
    \": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n             \
    \       }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Solution D subsection, recipe row 3\",\n        \"\
    exact_source_quote\": \"Distilled water 25.00 ml\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / Nitrilotriacetic acid\",\n    \"field_path\"\
    : \"ingredients[8].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[5].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                   \
    \     \\\"compound_id\\\": 189,\\n                        \\\"amount\\\": 1.5,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 1.5,\\n                        \\\"mmol_l\\\": 7.84765,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 1\",\n        \"exact_source_quote\": \"Nitrilotriacetic acid 1.50 g\",\n\
    \        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Conditional\
    \ on the provider-declared nominal 1 L stock basis: reported stock g/L 1.5 × 0.010\
    \ L receiving dose gives nominal delivered grams only; measured final stock and\
    \ medium volumes after pH adjustment are unspecified.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / MgSO4 x 7 H2O\",\n    \"field_path\":\
    \ \"ingredients[1].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[5].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 3,\\n          \
    \              \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 3,\\n                        \\\"mmol_l\\\": 12.1716,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 2\",\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 3.00 g\",\n      \
    \  \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local merged salt value adds concentrations\
    \ from solution A and undiluted mineral stock. Preserve both source rows separately,\
    \ then apply only the documented 10 mL stock transfer. Neither summing unlike\
    \ stage concentrations nor silently choosing a duplicate is valid.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"12.26316\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.26316\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L mineral-stock basis, for\
    \ NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered.\
    \ For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally\
    \ delivered. These conditional delivered masses depend on the provider stock-volume\
    \ declaration; the primary lists water and titration without a measured final\
    \ stock volume. Final medium g/L is not asserted.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / MnSO4 x H2O\",\n    \"field_path\": \"\
    ingredients[9].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[5].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MnSO4 x H2O\\\",\\n                        \\\"compound_id\\\
    \": 14,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n \
    \                       \\\"mmol_l\\\": 2.9583,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 3\",\n        \"exact_source_quote\": \"MnSO4 x H2O 0.50 g\",\n        \"\
    snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Conditional\
    \ on the provider-declared nominal 1 L stock basis: reported stock g/L 0.5 × 0.010\
    \ L receiving dose gives nominal delivered grams only; measured final stock and\
    \ medium volumes after pH adjustment are unspecified.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / NaCl\",\n    \"field_path\": \"ingredients[0].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 17.1116,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 4\",\n        \"exact_source_quote\": \"NaCl 1.00 g\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local merged salt value adds concentrations\
    \ from solution A and undiluted mineral stock. Preserve both source rows separately,\
    \ then apply only the documented 10 mL stock transfer. Neither summing unlike\
    \ stage concentrations nor silently choosing a duplicate is valid.\",\n    \"\
    action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\":\
    \ [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"79.9474\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"79.9474\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L mineral-stock basis, for\
    \ NaCl: 75 g in A + (1 g/L mineral stock × 0.010 L) = 75.01 g nominally delivered.\
    \ For magnesium sulfate heptahydrate: 8.8 g + (3 g/L × 0.010 L) = 8.83 g nominally\
    \ delivered. These conditional delivered masses depend on the provider stock-volume\
    \ declaration; the primary lists water and titration without a measured final\
    \ stock volume. Final medium g/L is not asserted.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / FeSO4 x 7 H2O\",\n    \"field_path\":\
    \ \"ingredients[10].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[5].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 12,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.359693,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 5\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 0.10 g\",\n      \
    \  \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[10].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Conditional\
    \ on the provider-declared nominal 1 L stock basis: reported stock g/L 0.1 × 0.010\
    \ L receiving dose gives nominal delivered grams only; measured final stock and\
    \ medium volumes after pH adjustment are unspecified.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / CoSO4 x 7 H2O\",\n    \"field_path\":\
    \ \"ingredients[11].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[5].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"CoSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 198,\\n                        \\\"amount\\\": 0.18,\\n     \
    \                   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.18,\\n                        \\\"mmol_l\\\": 1.16132,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 6\",\n        \"exact_source_quote\": \"CoSO4 x 7 H2O 0.18 g\",\n      \
    \  \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[11].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.18 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / CaCl2\
    \ x 2 H2O\",\n    \"field_path\": \"ingredients[12].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 7,\\n                        \\\"amount\\\
    \": 0.1,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 0.1,\\n                        \\\"mmol_l\\\": 0.680203,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 7\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.10 g\",\n      \
    \  \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[12].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Conditional\
    \ on the provider-declared nominal 1 L stock basis: reported stock g/L 0.1 × 0.010\
    \ L receiving dose gives nominal delivered grams only; measured final stock and\
    \ medium volumes after pH adjustment are unspecified.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Modified Wolin's mineral solution / ZnSO4 x 7 H2O\",\n    \"field_path\":\
    \ \"ingredients[13].concentration\",\n    \"decision\": \"correct\",\n    \"local\"\
    : null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive1290api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\",\n \
    \       \"source_locator\": \"$.data.solutions[5].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 35,\\n                        \\\"amount\\\": 0.18,\\n      \
    \                  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.18,\\n                        \\\"mmol_l\\\": 0.625954,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 8\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 0.18 g\",\n      \
    \  \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[13].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.18\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.18\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.18 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / CuSO4\
    \ x 5 H2O\",\n    \"field_path\": \"ingredients[14].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"CuSO4 x 5 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 121,\\n                        \\\"amount\\\
    \": 0.01,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.0400503,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 9\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.01 g\",\n      \
    \  \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[14].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.01 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / AlK(SO4)2\
    \ x 12 H2O\",\n    \"field_path\": \"ingredients[15].concentration\",\n    \"\
    decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[5].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"AlK(SO4)2 x 12 H2O\\\",\\n                        \\\"compound_id\\\
    \": 908,\\n                        \\\"amount\\\": 0.02,\\n                  \
    \      \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.0421596,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 10\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.02 g\",\n\
    \        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[15].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.02 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / H3BO3\"\
    ,\n    \"field_path\": \"ingredients[16].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"compound\\\": \\\"H3BO3\\\",\\n                 \
    \       \\\"compound_id\\\": 37,\\n                        \\\"amount\\\": 0.01,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.161708,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 11\",\n        \"exact_source_quote\": \"H3BO3 0.01 g\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[16].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.01 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / Na2MoO4\
    \ x 2 H2O\",\n    \"field_path\": \"ingredients[17].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[11]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 12,\\\
    n                        \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 9,\\n                        \\\"amount\\\
    \": 0.01,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.01,\\n                        \\\"mmol_l\\\": 0.0413309,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 12\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.01 g\",\n   \
    \     \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[17].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.01 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / NiCl2\
    \ x 6 H2O\",\n    \"field_path\": \"ingredients[18].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[12]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 13,\\\
    n                        \\\"compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 40,\\n                        \\\"amount\\\
    \": 0.03,\\n                        \\\"unit\\\": \\\"g\\\",\\n              \
    \          \\\"g_l\\\": 0.03,\\n                        \\\"mmol_l\\\": 0.231483,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 13\",\n        \"exact_source_quote\": \"NiCl2 x 6 H2O 0.03 g\",\n     \
    \   \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[18].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.03\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.03 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / Na2SeO3\
    \ x 5 H2O\",\n    \"field_path\": \"ingredients[19].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[13]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 14,\\\
    n                        \\\"compound\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n       \
    \                 \\\"compound_id\\\": 107,\\n                        \\\"amount\\\
    \": 0.3,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.0003,\\n                        \\\"mmol_l\\\": 0.00114062,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 14\",\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 0.30 mg\",\n  \
    \      \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[19].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0003\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0003\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.0003 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / Na2WO4\
    \ x 2 H2O\",\n    \"field_path\": \"ingredients[20].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[14]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 15,\\\
    n                        \\\"compound\\\": \\\"Na2WO4 x 2 H2O\\\",\\n        \
    \                \\\"compound_id\\\": 249,\\n                        \\\"amount\\\
    \": 0.4,\\n                        \\\"unit\\\": \\\"mg\\\",\\n              \
    \          \\\"g_l\\\": 0.0004,\\n                        \\\"mmol_l\\\": 0.00121267,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 15\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.40 mg\",\n   \
    \     \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[20].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.0004\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0004\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.0004 × 0.010 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Modified Wolin's mineral solution / Distilled\
    \ water\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[5].recipe[15]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 16,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Modified Wolin's mineral solution subsection, recipe\
    \ row 16\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n\
    \        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x) / Biotin\",\n    \"field_path\": \"ingredients[21].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 20,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.02,\\n              \
    \          \\\"mmol_l\\\": 0.0818632,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 1\",\n        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[21].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.02 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Folic\
    \ acid\",\n    \"field_path\": \"ingredients[22].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Folic acid\\\",\\n            \
    \            \\\"compound_id\\\": 138,\\n                        \\\"amount\\\"\
    : 20,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.02,\\n                        \\\"mmol_l\\\": 0.0453104,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 2\",\n        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n       \
    \ \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[22].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.02\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.02 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Pyridoxine\
    \ hydrochloride\",\n    \"field_path\": \"ingredients[23].concentration\",\n \
    \   \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                        \\\"\
    compound_id\\\": 519,\\n                        \\\"amount\\\": 100,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.486287,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 3\",\n        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00\
    \ mg\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[23].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Conditional\
    \ on the provider-declared nominal 1 L stock basis: reported stock g/L 0.1 × 0.001\
    \ L receiving dose gives nominal delivered grams only; measured final stock and\
    \ medium volumes after pH adjustment are unspecified.\"\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Wolin's vitamin solution (10x) / Thiamine HCl\",\n    \"field_path\": \"ingredients[24].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Thiamine HCl\\\",\\n                        \\\"compound_id\\\
    \": 1207,\\n                        \\\"amount\\\": 50,\\n                   \
    \     \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\\
    n                        \\\"mmol_l\\\": 0.148236,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n      },\n\
    \      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 4\",\n        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n     \
    \   \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[24].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Riboflavin\"\
    ,\n    \"field_path\": \"ingredients[25].concentration\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"Riboflavin\\\",\\n            \
    \            \\\"compound_id\\\": 136,\\n                        \\\"amount\\\"\
    : 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                 \
    \       \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.132837,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 5\",\n        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n       \
    \ \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[25].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Nicotinic\
    \ acid\",\n    \"field_path\": \"ingredients[26].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"Nicotinic acid\\\",\\n        \
    \                \\\"compound_id\\\": 139,\\n                        \\\"amount\\\
    \": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.406141,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 6\",\n        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n   \
    \     \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[26].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Calcium\
    \ D-(+)-pantothenate\",\n    \"field_path\": \"ingredients[27].concentration\"\
    ,\n    \"decision\": \"correct\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1290api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1290\",\n        \"source_locator\"\
    : \"$.data.solutions[6].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Calcium D-(+)-pantothenate\\\",\\n                        \\\
    \"compound_id\\\": 1512,\\n                        \\\"amount\\\": 50,\\n    \
    \                    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"\
    g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.209846,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 7\",\n        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00\
    \ mg\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[27].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Vitamin\
    \ B12\",\n    \"field_path\": \"ingredients[28].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"Vitamin B12\\\",\\n           \
    \             \\\"compound_id\\\": 18,\\n                        \\\"amount\\\"\
    : 1,\\n                        \\\"unit\\\": \\\"mg\\\",\\n                  \
    \      \\\"g_l\\\": 0.001,\\n                        \\\"mmol_l\\\": 0.00073779,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 8\",\n        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n       \
    \ \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[28].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.001\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.001 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / p-Aminobenzoic\
    \ acid\",\n    \"field_path\": \"ingredients[29].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"p-Aminobenzoic acid\\\",\\n   \
    \                     \\\"compound_id\\\": 47,\\n                        \\\"\
    amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n       \
    \                 \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\"\
    : 0.364591,\\n                        \\\"optional\\\": 0\\n                 \
    \   }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 9\",\n        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n\
    \        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[29].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / (DL)-alpha-Lipoic\
    \ acid\",\n    \"field_path\": \"ingredients[30].concentration\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"(DL)-alpha-Lipoic acid\\\",\\n\
    \                        \\\"compound_id\\\": 252,\\n                        \\\
    \"amount\\\": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n     \
    \                   \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\"\
    : 0.24233,\\n                        \\\"optional\\\": 0\\n                  \
    \  }\",\n        \"snapshot_sha256\": \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 10\",\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\"\
    ,\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The local g/L value belongs to a component\
    \ solution or undiluted nested stock, not the completed medium. Restore the original\
    \ batch amount, stock volume and receiving dose; retain current rounding as historical\
    \ local data, not an exact final concentration.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ingredients[30].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Conditional on the provider-declared nominal 1 L stock basis: reported stock\
    \ g/L 0.05 × 0.001 L receiving dose gives nominal delivered grams only; measured\
    \ final stock and medium volumes after pH adjustment are unspecified.\"\n  },\n\
    \  {\n    \"ingredient_or_context\": \"Wolin's vitamin solution (10x) / Distilled\
    \ water\",\n    \"field_path\": \"solutions\",\n    \"decision\": \"add\",\n \
    \   \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1290api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1290\"\
    ,\n        \"source_locator\": \"$.data.solutions[6].recipe[10]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 11,\\\
    n                        \\\"compound\\\": \\\"Distilled water\\\",\\n       \
    \                 \\\"compound_id\\\": 4,\\n                        \\\"amount\\\
    \": 1000,\\n                        \\\"unit\\\": \\\"ml\\\",\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"f9b64c7619cc52b99299a11e1c9e23855cc54c2e1831eeac97d15c746ccda1a2\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n   \
    \     \"source_locator\": \"Wolin's vitamin solution (10x) subsection, recipe\
    \ row 11\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n\
    \        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"This explicit stock receiving dose or\
    \ solvent quantity is absent from a source-scoped local representation. Restore\
    \ it within the correct A/B/C/D or nested stock stage, not as a direct neat ingredient.\
    \ Existing preparation text is preserved separately.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"solutions\",\n     \
    \   \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Initial A pH\",\n    \"field_path\": \"preparation.Initial_A_pH\",\n    \"\
    decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"adjust pH to 8.0 with 1 N NaOH\",\n       \
    \ \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Preserved initial pH and 1 N reagent strength\
    \ need attached evidence; actual titrant dose is unspecified.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients of solution A, adjust pH to 8.0\
    \ with 1 N NaOH and boil medium for 1 min, then cool to room temperature under\
    \ 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic\
    \ culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation\
    \ complete the medium by adding appropriate amounts of solutions B, C and D prepared\
    \ under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium\
    \ to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Boiling duration\"\
    ,\n    \"field_path\": \"preparation.Boiling_duration\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"boil medium for 1\\nmin\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"One-minute boiling applies to solution\
    \ A before cooling, not a fabricated autoclave duration.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients of solution A, adjust pH to 8.0\
    \ with 1 N NaOH and boil medium for 1 min, then cool to room temperature under\
    \ 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic\
    \ culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation\
    \ complete the medium by adding appropriate amounts of solutions B, C and D prepared\
    \ under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium\
    \ to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"A cooling gas\"\
    ,\n    \"field_path\": \"preparation.A_cooling_gas\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"cool to room temperature under 100% N2 gas\
    \ atmosphere\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Preserved 100% N2 atmosphere needs claim\
    \ evidence; absolute gas volume/flow is unspecified.\",\n    \"action_taken\"\
    : \"Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n \
    \       \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients of solution A, adjust pH to 8.0\
    \ with 1 N NaOH and boil medium for 1 min, then cool to room temperature under\
    \ 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic\
    \ culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation\
    \ complete the medium by adding appropriate amounts of solutions B, C and D prepared\
    \ under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium\
    \ to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"B/C/D preparation\
    \ gas\",\n    \"field_path\": \"preparation.B/C/D_preparation_gas\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"solutions B, C and D prepared under 100%\
    \ N2 gas\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Preserve separate stocks and filtration\
    \ under the stated gas; this is not autoclaving every component together.\",\n\
    \    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"preparation_steps[0].description\"\
    ,\n        \"stored\": \"Dissolve ingredients of solution A, adjust pH to 8.0\
    \ with 1 N NaOH and boil medium for 1 min, then cool to room temperature under\
    \ 100% N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic\
    \ culture vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation\
    \ complete the medium by adding appropriate amounts of solutions B, C and D prepared\
    \ under 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium\
    \ to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Completed-medium\
    \ pH\",\n    \"field_path\": \"preparation.Completed-medium_pH\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"the completed medium to 8.0\",\n        \"\
    snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Main pH 8.0 is present but lacks attached\
    \ source evidence; stock endpoints differ.\",\n    \"action_taken\": \"Review\
    \ only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"\
    input\": \"target\",\n        \"field_path\": \"ph_value\",\n        \"stored\"\
    : 8.0,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n      \
    \  \"field_path\": \"ph_value\",\n        \"stored\": 8.0,\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Final acid strength\",\n    \"field_path\": \"preparation.Final_acid_strength\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"0.1 N HCl\",\n        \"snapshot_sha256\":\
    \ \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Retain conditional sterile anoxic acid\
    \ strength without inventing its dose.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation_steps[0].description\",\n\
    \        \"stored\": \"Dissolve ingredients of solution A, adjust pH to 8.0 with\
    \ 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100%\
    \ N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture\
    \ vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete\
    \ the medium by adding appropriate amounts of solutions B, C and D prepared under\
    \ 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium\
    \ to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Final base strength\"\
    ,\n    \"field_path\": \"preparation.Final_base_strength\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"0.1 N NaOH\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Retain conditional sterile anoxic base\
    \ strength without inventing its dose.\",\n    \"action_taken\": \"Review only;\
    \ no recipe change.\",\n    \"layer_decisions\": [\n      {\n        \"input\"\
    : \"target\",\n        \"field_path\": \"preparation_steps[0].description\",\n\
    \        \"stored\": \"Dissolve ingredients of solution A, adjust pH to 8.0 with\
    \ 1 N NaOH and boil medium for 1 min, then cool to room temperature under 100%\
    \ N2 gas atmosphere. Dispense solution A under same gas atmosphere in anoxic culture\
    \ vessels (e.g., Hungate-type tubes) and autoclave. Prior to inoculation complete\
    \ the medium by adding appropriate amounts of solutions B, C and D prepared under\
    \ 100% N2 gas and sterilized by filtration. Adjust pH of the completed medium\
    \ to 8.0 with a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Mineral initial\
    \ pH\",\n    \"field_path\": \"preparation.Mineral_initial_pH\",\n    \"decision\"\
    : \"correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"adjust pH to 6.5 with KOH\",\n        \"\
    snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Literal endpoint is preserved in main\
    \ preparation but belongs to the mineral stock; restore stock scope and attach\
    \ evidence.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"preparation_steps[1].description\",\n        \"stored\": \"First\
    \ dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals.\
    \ Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Mineral final pH\"\
    ,\n    \"field_path\": \"preparation.Mineral_final_pH\",\n    \"decision\": \"\
    correct\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n      \
    \  \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Exact main preparation or named stock subsection\"\
    ,\n        \"exact_source_quote\": \"final to pH 7.0 with KOH\",\n        \"snapshot_sha256\"\
    : \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\",\n    \
    \    \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Literal endpoint is preserved in main\
    \ preparation but belongs to the mineral stock; restore stock scope and attach\
    \ evidence.\",\n    \"action_taken\": \"Review only; no recipe change.\",\n  \
    \  \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n        \"\
    field_path\": \"preparation_steps[1].description\",\n        \"stored\": \"First\
    \ dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals.\
    \ Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"correct\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Vitamin concentration\
    \ factor\",\n    \"field_path\": \"preparation.Vitamin_concentration_factor\"\
    ,\n    \"decision\": \"add\",\n    \"local\": null,\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n       \
    \ \"source_locator\": \"Exact main preparation or named stock subsection\",\n\
    \        \"exact_source_quote\": \"Wolin's vitamin solution (10x)\",\n       \
    \ \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"Restore exact 10x stock identity separately\
    \ from its 1 mL dose; do not substitute the tenfold weaker DSMZ141 vitamin stock.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"solutions\"\
    ,\n        \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Titration dose\",\n    \"field_path\": \"preparation.Titration_dose\",\n \
    \   \"decision\": \"not_quantified\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\",\n       \
    \ \"source_locator\": \"Conditional adjustment prose\",\n        \"exact_source_quote\"\
    : \"if\\nnecessary.\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The source specifies endpoints/conditions\
    \ rather than a fixed titrant amount. No mass, volume or normality is inferred\
    \ for unspecified KOH.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients of solution A, adjust pH to 8.0 with 1 N NaOH and boil\
    \ medium for 1 min, then cool to room temperature under 100% N2 gas atmosphere.\
    \ Dispense solution A under same gas atmosphere in anoxic culture vessels (e.g.,\
    \ Hungate-type tubes) and autoclave. Prior to inoculation complete the medium\
    \ by adding appropriate amounts of solutions B, C and D prepared under 100% N2\
    \ gas and sterilized by filtration. Adjust pH of the completed medium to 8.0 with\
    \ a sterile anoxic solution of 0.1 N HCl or 0.1 N NaOH, if necessary.\",\n   \
    \     \"decision\": \"not_quantified\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ of solution A, adjust pH to 8.0 with 1 N NaOH and boil medium for 1 min, then\
    \ cool to room temperature under 100% N2 gas atmosphere. Dispense solution A under\
    \ same gas atmosphere in anoxic culture vessels (e.g., Hungate-type tubes) and\
    \ autoclave. Prior to inoculation complete the medium by adding appropriate amounts\
    \ of solutions B, C and D prepared under 100% N2 gas and sterilized by filtration.\
    \ Adjust pH of the completed medium to 8.0 with a sterile anoxic solution of 0.1\
    \ N HCl or 0.1 N NaOH, if necessary.\",\n        \"decision\": \"not_quantified\"\
    \n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\": \"Mineral KOH dose\"\
    ,\n    \"field_path\": \"preparation.Mineral_KOH_dose\",\n    \"decision\": \"\
    not_quantified\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1290\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1290.pdf\"\
    ,\n        \"source_locator\": \"Conditional adjustment prose\",\n        \"exact_source_quote\"\
    : \"with KOH, then add minerals. Adjust\",\n        \"snapshot_sha256\": \"ee893b0b840804b2db4502db47560557460313c36bb0f8271388024d21290f2d\"\
    ,\n        \"parsed_text_sha256\": \"c481d72c432c590e4146fc0ea6e6690e54132b13930e868e7bcc21811d0e3aa4\"\
    \n      }\n    ],\n    \"rationale\": \"The source specifies endpoints/conditions\
    \ rather than a fixed titrant amount. No mass, volume or normality is inferred\
    \ for unspecified KOH.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"not_quantified\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add\
    \ minerals. Adjust final to pH 7.0 with KOH.\",\n        \"decision\": \"not_quantified\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Exact DSMZ1290 identity and nested-stock dependencies
  outcome: supported
  summary: The target and unique maintained CM000753 owner resolve to DSMZ1290. Main
    assembly uses A 950, B 25, C 1 and D 25 mL. Exact mineral241 and vitamin5980 sources
    are scoped to DSMZ141 mineral and DSMZ120 tenfold vitamin subsections; parent
    organisms, recipes and variants are not inherited.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - owner-0
  - id-search
  - dsmz1290
  - mediadive1290api
  - dsmz141
  - dsmz120
- assessment_id: source-stage-consistency
  area: consistency
  topic: Every flat concentration versus its actual source stage
  outcome: concern
  summary: All 62 local concentrations are covered by 44 source recipe rows plus quantitative
    preparation decisions. Local NaCl 79.9474 and magnesium sulfate 12.26316 g/L explicitly
    sum solution-A concentrations and undiluted mineral strengths. On the provider’s
    nominal 1 L mineral-stock basis, 75.01 g NaCl and 8.83 g magnesium sulfate heptahydrate
    would be delivered from listed A plus 10 mL stock. The primary water/titration
    description does not independently establish measured final stock volume. D-glucose
    100 and both reducing-agent 20 g/L values are component-stock strengths. Mineral
    and vitamin rows likewise require 10 mL and 1 mL transfers. The 950+25+1+25=1001
    mL sum agrees with the provider declaration but does not establish measured post-titration
    volume.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - owner-0
  - quantity-inventory
  - quantity-local-fields
  - dsmz1290
  - mediadive1290api
- assessment_id: forms
  area: grounding
  topic: Hydrates, stereochemistry and product qualifiers
  outcome: concern
  summary: NiCl2·6H2O source and preferred name conflict with CHEBI:34887, whose 2Cl.Ni
    formula has no crystal water. The other explicit salt hydrates, D-glucose, calcium
    D-(+)-pantothenate and stereochemically unspecified lipoic-acid term do not establish
    a comparable contradiction. The source says generic Na-ascorbate while CHEBI:113451
    has L-specific structure; that specificity is not independently established by
    the recipe text. Current source yeast extract OXOID and trypticase BD BBL qualifiers
    should remain attached to the intended products. No unverified replacement identifier
    or supplier equivalence is proposed.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
  - chebi34887
  - chebi31345
  - chebi16494
  - chebi113451
- assessment_id: preparation
  area: completeness
  topic: Preserved main prose with missing solution hierarchy
  outcome: concern
  summary: The main pH 8.0, 1 N NaOH, one-minute boil, 100% N2, autoclaving A, filtration
    of B/C/D and conditional final 0.1 N acid/base are retained but unlinked to evidence.
    A/B/C/D are not represented, and mineral-stock pH 6.5→7.0 is placed as a main-medium
    step. Restore source scope without replacing final pH 8.0 or inventing an autoclave
    cycle.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Complex liquid and biological claim boundaries
  outcome: supported
  summary: COMPLEX/UNDEFINED and LIQUID fit the yeast/trypticase liquid formulation.
    No specific strain, taxon, assembly, DOI/PMID or growth claim is asserted. Dependency
    parent media provide only the named stock definitions.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 17 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: generation
  area: provenance
  topic: Inherited flattening and cleanup history
  outcome: concern
  summary: Both local layers retain the same 31 flat ingredients and duplicate-sum
    notes. Current importer separates the primary formulation from later stock definitions,
    while its preparation reader iterates solution steps; current cleanup no longer
    silently sums conflicting quantities. These current functions explain maintenance
    boundaries, not historical replay. Stock hierarchy and source evidence require
    explicit owner curation before regeneration.
  target_ids:
  - CultureMech:000753
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - writer-context-0
  - writer-context-1
  - writer-context-2
findings:
- finding_id: f1
  issue_key: culturemech.000753.stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Different solution concentrations are flattened and summed
  description: The record represents four component solutions and nested mineral/vitamin
    stocks as one undiluted ingredient list. It sums two salts across incompatible
    stages and exposes component glucose100 g/L and reducing agents 20 g/L as final
    medium concentrations. The required assembly doses and solvent stages are absent.
  target_ids:
  - CultureMech:000753
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
  - mediadive1290api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
  issue_key: culturemech.000753.nickel-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to an unhydrated term
  description: The source and local name specify NiCl2·6H2O, but the asserted primary
    and secondary CHEBI:34887 term has formula 2Cl.Ni without water. Correct labels
    and resolver passes do not support the supplied hydrate.
  target_ids:
  - CultureMech:000753
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
  issue_key: culturemech.000753.preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stock pH instructions are presented as main-medium preparation
  description: The second step gives mineral pH 6.5→7.0 without a mineral-stock object,
    while the first refers to undefined A/B/C/D. Correct literal numbers lack the
    scope needed for faithful preparation.
  target_ids:
  - CultureMech:000753
  field_paths:
  - preparation_steps
  - solutions
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 is normalized to major because the missing hierarchy
    misassigns source-specific pH and preparation stages.
- finding_id: f4
  issue_key: culturemech.000753.source-specificity
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Product and ascorbate specificity lack direct source linkage
  description: Source OXOID yeast and BD BBL trypticase qualifiers are omitted; generic
    Na-ascorbate is associated with an L-specific structural term without a product
    specification establishing that choice. These bounded provenance limits should
    remain visible alongside the material stock errors.
  target_ids:
  - CultureMech:000753
  field_paths:
  - ingredients[3]
  - ingredients[4]
  - ingredients[7]
  - references
  evidence_ids:
  - record
  - owner-0
  - dsmz1290
  - chebi113451
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
  description: Restore A/B/C/D and both nested stocks with exact batch amounts, solvent
    quantities and receiving doses, removing unsupported cross-stage sums through
    explicit curation. Preserve nominal provider bases, rounding limits and unknown
    post-titration volume. Attach exact evidence before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000753
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
  description: Resolve the exact source hydrate before assigning a supported identifier
    in both linkage fields. Preserve the 0.03 g stock batch mass and proper stock
    dilution; do not substitute anhydrous mass or invent a replacement ID.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000753
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
  description: Preserve the main pH 8.0 sequence and move mineral instructions into
    the restored stock definition with evidence. Retain separate autoclaving/filtration
    stages and unquantified titrant doses; no generic cycle.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000753
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
  description: Attach source product qualifiers and exact amount evidence; confirm
    the intended ascorbate specificity before asserting a product-level match. Preserve
    generic source wording and do not infer an alternative isomer.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000753
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_medium.yaml
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
- The 1001 mL component sum/provider declaration is a nominal basis, not measured
  final volume after pH adjustment. No exact final concentration or titrant dose is
  invented.
- DSMZ141 and DSMZ120 contribute only the explicitly named mineral and 10x vitamin
  subsections. Their main recipes, other stocks and strain variants are outside this
  record.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-023
- generated-medium
```
