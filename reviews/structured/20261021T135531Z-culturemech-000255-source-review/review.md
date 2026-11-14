# Source and formulation review: alkalophilic_halophile_medium (CultureMech:000255)

- Review: 20261021T135531Z-culturemech-000255-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:52:35Z
- Finished UTC: 2026-10-21T13:55:31Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1431 distinguishes a liquid recipe containing 50 g sodium carbonate from agar medium prepared without that carbonate and receiving 20–30 mL sterile 10% carbonate to pH 9.0. The generated solid record and both owners combine the liquid carbonate concentration with agar. Other masses agree with the provider’s nominal 1 L basis, but the primary gives neither water/final volume nor explicit percentage bases. Chemical forms resolve; claim evidence, owner preparation and historical timestamp metadata need bounded follow-up.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 231; batch 024 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-three task batches contain 230 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 233 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000255 | data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml | generated | alkalophilic_halophile_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000255 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000255 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch024/231/strict.tsv |
| validate-terms | passed | True | CultureMech:000255 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000255 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000255 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodoMediaList | unavailable | False | CultureMech:000255 | The preserved komodoMediaList retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation. |
| Exact source content access: komodo1431 | unavailable | False | CultureMech:000255 | The preserved komodo1431 retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation. |
| Exact source content access: komodoDetail1431 | unavailable | False | CultureMech:000255 | The preserved komodoDetail1431 retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000255.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:000255.

8 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 8/10 primary and 8/10 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 10: primary 80.00%; secondary 80.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:000255.

14 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "ingredient_or_context": "Yeast extract",
    "field_path": "ingredients[0].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 1",
        "exact_source_quote": "Yeast extract                                                               10.0         g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
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
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "Casamino acids",
    "field_path": "ingredients[1].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Casamino acids\",\n                        \"compound_id\": 101,\n                        \"amount\": 7.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 2",
        "exact_source_quote": "Casamino acid                                                                7.5         g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "7.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "7.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "7.5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "Trisodium citrate",
    "field_path": "ingredients[2].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Trisodium citrate\",\n                        \"compound_id\": 1047,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 11.6248,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 3",
        "exact_source_quote": "Trisodium citrate                                                            3.0         g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "KCl",
    "field_path": "ingredients[3].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 26.8276,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 4",
        "exact_source_quote": "KCl                                                                          2.0         g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "MgSO4 x 7 H2O",
    "field_path": "ingredients[4].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 4.05719,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 5",
        "exact_source_quote": "MgSO4 x 7 H2O                                                                1.0         g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "MnCl2 x 4 H2O",
    "field_path": "ingredients[5].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00036,\n                        \"mmol_l\": 0.00181905,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 6",
        "exact_source_quote": "MnCl2 x 4 H2O                                                               0.36      mg",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.00036",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.00036",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.00036",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "0.36 mg ÷ 1000 = 0.00036 g; on the provider’s nominal 1 L basis this is 0.00036 g/L."
  },
  {
    "ingredient_or_context": "FeSO4 x 7 H2O",
    "field_path": "ingredients[6].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.179846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 7",
        "exact_source_quote": "FeSO4 x 7 H2O                                                               50.0      mg",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "50 mg ÷ 1000 = 0.05 g; on the provider’s nominal 1 L basis this is 0.05 g/L."
  },
  {
    "ingredient_or_context": "NaCl",
    "field_path": "ingredients[7].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 200,\n                        \"unit\": \"g\",\n                        \"g_l\": 200,\n                        \"mmol_l\": 3422.31,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 8",
        "exact_source_quote": "NaCl                                                                      200.0          g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The stored g/L equals the provider-declared 1000 mL recipe basis, with no attached amount evidence in any layer. The primary gives batch masses, not a measured final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "Na2CO3",
    "field_path": "ingredients[8].concentration",
    "decision": "correct",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 50,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 formulation row 9",
        "exact_source_quote": "Na2CO3                                                                      50.0         g",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "The 50 g table entry applies to the liquid branch. The agar branch explicitly omits it and adds sterile carbonate solution afterward; an unconditional 50 g/L ingredient in a solid recipe misstates scope.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "Agar",
    "field_path": "ingredients[9].concentration",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 2,\n                        \"unit\": \"%\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 59.4654,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      },
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 preparation paragraph",
        "exact_source_quote": "Agar (2%) medium",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "Provider maps 2% agar to 20 g/L, but the primary does not explicitly state w/v. Preserve the provider interpretation and source percentage separately; do not claim a verified percent conversion.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "arithmetic": "Provider g_l is copied on its declared 1 L basis; no primary final-volume inference."
  },
  {
    "ingredient_or_context": "Provider nominal volume",
    "field_path": "preparation.nominal_volume",
    "decision": "add",
    "local": null,
    "source_snippets": [
      {
        "source_key": "mediadive1431api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1431",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1000",
        "snapshot_sha256": "d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa"
      }
    ],
    "rationale": "The database declares 1000 mL; the primary table omits water and final volume. Record the source and limitation without inventing solvent or post-addition final volume.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Agar carbonate dose",
    "field_path": "preparation.Agar_carbonate_dose",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 agar preparation paragraph",
        "exact_source_quote": "Add 20-30 ml of a",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "Retain the exact agar-stage range/strength/pH and attach evidence. The carbonate percentage basis is unspecified; do not calculate carbonate mass, midpoint dose or final volume. The bacterial owner lacks the preparation paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Liquid medium may be prepared by adding all components together. Agar (2%) medium should be prepared without Na2CO3 and sterilised by autoclaving. Add 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing agar so that the final pH is 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Liquid medium may be prepared by adding all components together. Agar (2%) medium should be prepared without Na2CO3 and sterilised by autoclaving. Add 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing agar so that the final pH is 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Agar carbonate stock strength",
    "field_path": "preparation.Agar_carbonate_stock_strength",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 agar preparation paragraph",
        "exact_source_quote": "sterile 10% Na2CO3 solution",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "Retain the exact agar-stage range/strength/pH and attach evidence. The carbonate percentage basis is unspecified; do not calculate carbonate mass, midpoint dose or final volume. The bacterial owner lacks the preparation paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps[0].description",
        "stored": "Liquid medium may be prepared by adding all components together. Agar (2%) medium should be prepared without Na2CO3 and sterilised by autoclaving. Add 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing agar so that the final pH is 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Liquid medium may be prepared by adding all components together. Agar (2%) medium should be prepared without Na2CO3 and sterilised by autoclaving. Add 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing agar so that the final pH is 9.0.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ]
  },
  {
    "ingredient_or_context": "Agar final pH",
    "field_path": "preparation.Agar_final_pH",
    "decision": "evidence_only",
    "local": null,
    "source_snippets": [
      {
        "source_key": "dsmz1431",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf",
        "source_locator": "Page1 agar preparation paragraph",
        "exact_source_quote": "pH is 9.0.",
        "snapshot_sha256": "b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514",
        "parsed_text_sha256": "5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c"
      }
    ],
    "rationale": "Retain the exact agar-stage range/strength/pH and attach evidence. The carbonate percentage basis is unspecified; do not calculate carbonate mass, midpoint dose or final volume. The bacterial owner lacks the preparation paragraph.",
    "action_taken": "Review only; no recipe change.",
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.0,
        "decision": "evidence_only"
      }
    ]
  }
]

### Repeated basename with two distinct maintained contributors

identity: supported. Targets: CultureMech:000255.

The repeated merged_from/source basename resolves to archaea CM000255 (DSMZ1431) and bacterial CM004157 (KOMODO1431). Both exact paths are inspected; they must not be collapsed by basename lookup. Source title/accession agree, but ingredient-set identity does not erase preparation or source metadata.

### Liquid and agar branches versus declared g/L

consistency: concern. Targets: CultureMech:000255.

All 30 local ingredient concentrations are covered. Eight noncarbonate solute values agree with the provider’s nominal 1 L basis, including 0.36 mg manganese salt→0.00036 g and 50 mg iron salt→0.05 g. The 50 g carbonate entry belongs to the liquid recipe; the agar branch omits it before autoclaving and receives 20–30 mL sterile 10% carbonate. Primary percentage bases and final volume remain unspecified.

### Exact salts and undefined mixtures

grounding: supported. Targets: CultureMech:000255.

Trisodium citrate matches CHEBI:53258’s trisodium definition; potassium chloride, magnesium sulfate heptahydrate, manganese chloride tetrahydrate, iron sulfate heptahydrate, sodium chloride and carbonate match the explicitly stated forms. No citrate hydrate is inferred. Yeast extract and casamino acids remain mixtures; missing optional IDs do not justify assigning pure molecules. Agar is an undefined polysaccharide mixture.

### Correct retained prose with an incompatible unconditional formula

completeness: concern. Targets: CultureMech:000255.

The target and DSMZ owner preserve the source’s complete liquid/agar paragraph, including the final pH 9.0. The KOMODO owner lacks it. The prose does not reconcile an unconditional 50 g/L carbonate plus agar formula. Autoclaving is specified for agar; temperature and duration are not. No cycle is invented.

### Physical branch, category labels and high_metal

scope: concern. Targets: CultureMech:000255.

COMPLEX/UNDEFINED fits yeast extract and casamino acids. SOLID_AGAR selects the agar branch but the carbonate formula does not follow that branch. Both filing categories are retained; no taxon, strain, DOI/PMID, assembly or growth outcome is asserted. On the provider’s nominal 1 L basis, sodium chloride alone is about 3422 mM (200 g/L ÷ 58.443 g/mol ×1000), compatible with the schema’s inclusive high_metal threshold; this is neither heavy-metal toxicity nor growth evidence. KOMODO Aerobic:No is catalog metadata, not a primary atmosphere protocol.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:000255.

28 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Source-copy and current conservative merge boundaries

provenance: concern. Targets: CultureMech:000255.

Both owners retain identical ten ingredient values, but only the DSMZ owner has preparation. Historical copying/merge events explain the provenance claims without proving exact source equivalence. Current formulation merging requires scientific fields and preparation to agree and retains scoped evidence; the old ingredient-set fingerprint is insufficient. No generator was run.

## Findings

### f1: Agar medium retains the liquid branch carbonate amount

major / open / confirmed; issue key: culturemech.000255.liquid-agar-carbonate-scope.

The source explicitly distinguishes liquid components from agar prepared without carbonate followed by a 20–30 mL sterile 10% carbonate addition. The solid record and both owners instead assert 50 g/L carbonate alongside agar. Preserved prose in two layers does not repair the unconditional ingredient claim; the KOMODO owner lacks the preparation.

### f2: Nominal concentration basis lacks claim-level source evidence

minor / open / confirmed; issue key: culturemech.000255.amount-evidence-basis.

All local amounts lack attached concentration evidence. The primary supplies batch masses but no water/final-volume quantity, while the provider declares 1000 mL and interprets 2% agar as 20 g/L. Those distinct support levels must remain explicit.

### f3: KOMODO history contains malformed and timezone-naive timestamps

minor / open / confirmed; issue key: culturemech.000255.history-timestamps.

The bacterial owner’s import timestamp ends in .fZ and its composition-copy timestamp lacks a timezone. Other chronology remains contextual, not authenticated historical source retrieval.

## Recommended Actions And Acceptance Checks

### a1

Represent the liquid and agar branches explicitly in maintained inputs, retain the correct carbonate addition stage and range, and preserve the unspecified percentage/final-volume basis. Add exact claim evidence and reconcile the missing KOMODO preparation before separately authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Attach exact source rows and provider basis to each supported amount. Preserve the primary’s original units and unidentified percentage basis; do not manufacture a final water amount or verified percent conversion.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve append-only history and add a bounded clarification if original timing can be established; do not silently invent or rewrite old timestamps.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch024/231/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch024/231/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml:1:id: CultureMech:000255<br>./data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml:1:id: CultureMech:000255<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch024/source-preflight-bound/231/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 14 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch024/source-preflight-bound/231/evidence-context-original.json; Complete frozen source context rebound to every fresh native input | context_only | All context input hashes match the fresh native inspection. The preflight remains historical preparation; this assessment uses the current bound record catalog and native input hashes. |
| dsmz1431 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf; Whole single-page primary, table and liquid/agar preparation; PDF page image also inspected | supports | Nine stated masses, two preparation branches, 2% agar, 20–30 mL of sterile 10% carbonate and agar final pH 9.0 inspected. No water/final-volume statement or explicit percent basis is present. |
| mediadive1431api | https://mediadive.dsmz.de/rest/medium/1431; Complete medium1431 and solution2929, all ten recipe rows and preparation | supports | Provider declares volume 1000 mL and reported g_l; these are nominal database values, not measured final volume from the primary. |
| komodo1431-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact byte-literal HTML table row for MediaInfo=1431 | supports | Source catalog identity, DSMZ cross-reference and encoded metadata only. This does not authenticate the historical copied formulation or establish growth/atmosphere. |
| komodoMediaList-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaList; Preserved exact public retrieval result | context_only | The preserved komodoMediaList retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation. |
| komodo1431-attempt | https://komodo.modelseed.org/servlet/Komodo?medium=1431; Preserved exact public retrieval result | context_only | The preserved komodo1431 retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation. |
| komodoDetail1431-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1431; Preserved exact public retrieval result | context_only | The preserved komodoDetail1431 retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53258 resolves to sodium citrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate", "match_type": "preferred_term", "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id": "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| quantity-inventory | /private/tmp/culturemech-review-work-batch024/231/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| quantity-local-fields | /private/tmp/culturemech-review-work-batch024/231/quantity-local-field-audit.json; All quantity layer paths and exact stored values against full inspected YAML | context_only | Every local concentration is covered; every layer locator resolves to its exact stored value or explicitly absent intended container. Source locators remain in source_snippets. |
| schema-metal | src/culturemech/schema/culturemech.yaml; MediaRecipe.high_metal definition | context_only | Threshold is total included metal concentration ≥1049.84 mM and includes Na/K/Mg; it is an automated composition annotation, not demonstrated metal tolerance. |
| writer-context-0 | src/culturemech/merge/formulation.py; formulation_content lines 48–70; merge_formulation_evidence lines 92–128 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-1 | src/culturemech/import/mediadive_importer.py; _parse_api_composition lines 455–537; _is_api_stock_addition lines 563–570; _parse_api_solutions lines 593–621; _normalize_unit lines 623–651; _parse_preparation_steps lines 653–721 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| writer-context-2 | scripts/cleanup_media_quality.py; normalize_name lines 76–82; _merge_ingredient_group lines 148–216 | context_only | Exact current source/import/resolver/merge excerpts were read and rechecked against native input hashes. Current behavior is implementation context, not a replay of historical imports. |
| history-metadata | data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml; data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml; data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:09.356457"}]}] |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The preserved komodoMediaList retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation.
- The preserved komodo1431 retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation.
- The preserved komodoDetail1431 retrieval returned HTTP403. Exact DSMZ1431 primary and provider are available; the KOMODO catalog supports identity only, not an independently inspected detailed formulation.
- No exact final volume is given by the primary, and neither agar 2% nor carbonate 10% explicitly names a mass/volume basis. No liquid density, carbonate mass or replacement concentration is inferred.
- Failed KOMODO detail attempts are retained as optional source-access limits because the exact DSMZ primary and provider supply the assessed base formulation; the catalog is used only for identity/encoded metadata.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135531Z-culturemech-000255-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkalophilic_halophile_medium (CultureMech:000255)'
started_at: '2026-10-21T13:52:35Z'
finished_at: '2026-10-21T13:55:31Z'
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
summary: DSMZ 1431 distinguishes a liquid recipe containing 50 g sodium carbonate
  from agar medium prepared without that carbonate and receiving 20–30 mL sterile
  10% carbonate to pH 9.0. The generated solid record and both owners combine the
  liquid carbonate concentration with agar. Other masses agree with the provider’s
  nominal 1 L basis, but the primary gives neither water/final volume nor explicit
  percentage bases. Chemical forms resolve; claim evidence, owner preparation and
  historical timestamp metadata need bounded follow-up.
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
  - path: data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
    sha256: 87b4c80d58a2d6e4d00e983b92f03aab585b695cb189b6de0908495c9d348121
    role: target
  - path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    sha256: fb61f9ab1e39298e710a106a78127c9d6bbc09122883ccfced5c9271d858fb01
    role: context
  - path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
    sha256: 9d45a336ab8c211ba3540369d64b8013ade39c6310ac166beda7fd9fb37d8729
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
  selection: Task review 231; batch 024 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-three task batches
    contain 230 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 233 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000255
targets:
- target_id: CultureMech:000255
  path: data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  label: alkalophilic_halophile_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch024/231/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch024/231/strict.tsv"
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000255
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
  - CultureMech:000255
- check_id: komodoMediaList-source-access
  name: 'Exact source content access: komodoMediaList'
  required: false
  status: unavailable
  summary: The preserved komodoMediaList retrieval returned HTTP403. Exact DSMZ1431
    primary and provider are available; the KOMODO catalog supports identity only,
    not an independently inspected detailed formulation.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - komodoMediaList-attempt
- check_id: komodo1431-source-access
  name: 'Exact source content access: komodo1431'
  required: false
  status: unavailable
  summary: The preserved komodo1431 retrieval returned HTTP403. Exact DSMZ1431 primary
    and provider are available; the KOMODO catalog supports identity only, not an
    independently inspected detailed formulation.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - komodo1431-attempt
- check_id: komodoDetail1431-source-access
  name: 'Exact source content access: komodoDetail1431'
  required: false
  status: unavailable
  summary: The preserved komodoDetail1431 retrieval returned HTTP403. Exact DSMZ1431
    primary and provider are available; the KOMODO catalog supports identity only,
    not an independently inspected detailed formulation.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - komodoDetail1431-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:52:51.888365Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch024/231/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:52:55.439183Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-024/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch024/231/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:52:57.897279Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:52:59.113318Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:55:29Z'
  support: supports
  summary: './data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml:1:id:
    CultureMech:000255

    ./data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml:1:id: CultureMech:000255

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/source-preflight-bound/231/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:55:29Z'
  support: supports
  summary: 14 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 57aa6ba2e75d731e058e243fd2e6f7da9d6c677d13e5276605a05657bde0cec0
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/source-preflight-bound/231/evidence-context-original.json
  locator: Complete frozen source context rebound to every fresh native input
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: All context input hashes match the fresh native inspection. The preflight
    remains historical preparation; this assessment uses the current bound record
    catalog and native input hashes.
  snapshot_sha256: 010297deae8f3e3e2cc3b4e905a0b2b930aac399236bf3d5c8e7086c6f7ff2c9
- evidence_id: dsmz1431
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf
  locator: Whole single-page primary, table and liquid/agar preparation; PDF page
    image also inspected
  accessed_at: '2026-10-21T13:41:00.637365Z'
  support: supports
  summary: Nine stated masses, two preparation branches, 2% agar, 20–30 mL of sterile
    10% carbonate and agar final pH 9.0 inspected. No water/final-volume statement
    or explicit percent basis is present.
  snapshot_sha256: b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514
- evidence_id: mediadive1431api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1431
  locator: Complete medium1431 and solution2929, all ten recipe rows and preparation
  accessed_at: '2026-10-21T13:40:59.775201Z'
  support: supports
  summary: Provider declares volume 1000 mL and reported g_l; these are nominal database
    values, not measured final volume from the primary.
  snapshot_sha256: d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa
- evidence_id: komodo1431-catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact byte-literal HTML table row for MediaInfo=1431
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Source catalog identity, DSMZ cross-reference and encoded metadata only.
    This does not authenticate the historical copied formulation or establish growth/atmosphere.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1431'\
    \ >1431</a></TD>\n\t\t\t\t\t<TD>ALKALOPHILIC HALOPHILE medium</TD>\n\t\t\t\t\t\
    <TD> 9.0</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodoMediaList-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaList
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:40:59.461854Z'
  support: context_only
  summary: The preserved komodoMediaList retrieval returned HTTP403. Exact DSMZ1431
    primary and provider are available; the KOMODO catalog supports identity only,
    not an independently inspected detailed formulation.
  snapshot_sha256: 6fd54c15a816e47cf87c082f1738a09522dc88f8d69043b2a2ead24ccfe4b1d4
- evidence_id: komodo1431-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?medium=1431
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:40:59.462220Z'
  support: context_only
  summary: The preserved komodo1431 retrieval returned HTTP403. Exact DSMZ1431 primary
    and provider are available; the KOMODO catalog supports identity only, not an
    independently inspected detailed formulation.
  snapshot_sha256: e0327050f533613a1edaa9ed99d94c94de756145226504beefcba0432f4eec8d
- evidence_id: komodoDetail1431-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1431
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T13:42:25.900780Z'
  support: context_only
  summary: The preserved komodoDetail1431 retrieval returned HTTP403. Exact DSMZ1431
    primary and provider are available; the KOMODO catalog supports identity only,
    not an independently inspected detailed formulation.
  snapshot_sha256: 7b501cadae74d12d67ac9ae49c9d1385375810bb2093de1f24fa22ed5734ac2f
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
- evidence_id: chebi53258
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53258
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:54.823692Z'
  support: supports
  summary: CHEBI:53258 resolves to sodium citrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2a35c6dc3532c2276c6b19aef0992260e14b1fc36423fa3eb812bb94f63c4371
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
  accessed_at: '2026-10-21T13:55:29Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:2509":
    [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
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
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:53258": [{"label": "Trisodium citrate", "match_type": "preferred_term",
    "identifier": "CHEBI:53258", "preferred_term": "Trisodium citrate", "ontology_id":
    "CHEBI:53258", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:75836":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term":
    "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/231/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 9d20e749cc94d3e6c743d6515f2030f93bd42627db76db1ab75a38239b8b753c
- evidence_id: quantity-local-fields
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch024/231/quantity-local-field-audit.json
  locator: All quantity layer paths and exact stored values against full inspected
    YAML
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Every local concentration is covered; every layer locator resolves to its
    exact stored value or explicitly absent intended container. Source locators remain
    in source_snippets.
  snapshot_sha256: e8449eea3528bc442ae973ea04852e11a665ea18b7132a2c7bc5c49647351f20
- evidence_id: schema-metal
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediaRecipe.high_metal definition
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Threshold is total included metal concentration ≥1049.84 mM and includes
    Na/K/Mg; it is an automated composition annotation, not demonstrated metal tolerance.
- evidence_id: writer-context-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content lines 48–70; merge_formulation_evidence lines 92–128
  accessed_at: '2026-10-21T13:55:29Z'
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
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-context-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: normalize_name lines 76–82; _merge_ingredient_group lines 148–216
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: Exact current source/import/resolver/merge excerpts were read and rechecked
    against native input hashes. Current behavior is implementation context, not a
    replay of historical imports.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALOPHILIC_HALOPHILE_MEDIUM.yaml; data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml;
    data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:55:29Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml", "events": 9,
    "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:02.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:09.356457"}]}]'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '8 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 8/10 primary
    and 8/10 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi2509
  - chebi26710
  - chebi29377
  - chebi31795
  - chebi32588
  - chebi53258
  - chebi75836
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 10: primary 80.00%;
    secondary 80.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 14 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"ingredient_or_context\": \"Yeast extract\",\n    \"field_path\"\
    : \"ingredients[0].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"Yeast extract\\\",\\n         \
    \               \\\"compound_id\\\": 16,\\n                        \\\"amount\\\
    \": 10,\\n                        \\\"unit\\\": \\\"g\\\",\\n                \
    \        \\\"g_l\\\": 10,\\n                        \\\"optional\\\": 0\\n   \
    \                 }\",\n        \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 1\",\n        \"exact_source_quote\"\
    : \"Yeast extract                                                            \
    \   10.0         g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"10\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Provider g_l is copied on its declared 1 L basis; no primary final-volume\
    \ inference.\"\n  },\n  {\n    \"ingredient_or_context\": \"Casamino acids\",\n\
    \    \"field_path\": \"ingredients[1].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Casamino acids\\\",\\n        \
    \                \\\"compound_id\\\": 101,\\n                        \\\"amount\\\
    \": 7.5,\\n                        \\\"unit\\\": \\\"g\\\",\\n               \
    \         \\\"g_l\\\": 7.5,\\n                        \\\"optional\\\": 0\\n \
    \                   }\",\n        \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 2\",\n        \"exact_source_quote\"\
    : \"Casamino acid                                                            \
    \    7.5         g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[1].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.5\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"7.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Provider g_l is copied on its declared 1 L basis; no primary final-volume\
    \ inference.\"\n  },\n  {\n    \"ingredient_or_context\": \"Trisodium citrate\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"decision\": \"\
    evidence_only\",\n    \"local\": null,\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 3,\\\
    n                        \\\"compound\\\": \\\"Trisodium citrate\\\",\\n     \
    \                   \\\"compound_id\\\": 1047,\\n                        \\\"\
    amount\\\": 3,\\n                        \\\"unit\\\": \\\"g\\\",\\n         \
    \               \\\"g_l\\\": 3,\\n                        \\\"mmol_l\\\": 11.6248,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 3\",\n        \"exact_source_quote\"\
    : \"Trisodium citrate                                                        \
    \    3.0         g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[2].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"3\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\": \"\
    Provider g_l is copied on its declared 1 L basis; no primary final-volume inference.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"KCl\",\n    \"field_path\": \"ingredients[3].concentration\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"mediadive1431api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/1431\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n                  \
    \      \\\"mmol_l\\\": 26.8276,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 4\",\n        \"exact_source_quote\"\
    : \"KCl                                                                      \
    \    2.0         g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[3].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"2\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\": \"\
    Provider g_l is copied on its declared 1 L basis; no primary final-volume inference.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"MgSO4 x 7 H2O\",\n    \"field_path\"\
    : \"ingredients[4].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 5,\\\
    n                        \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 8,\\n                        \\\"amount\\\
    \": 1,\\n                        \\\"unit\\\": \\\"g\\\",\\n                 \
    \       \\\"g_l\\\": 1,\\n                        \\\"mmol_l\\\": 4.05719,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 5\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O                                                            \
    \    1.0         g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[4].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\": \"\
    Provider g_l is copied on its declared 1 L basis; no primary final-volume inference.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"MnCl2 x 4 H2O\",\n    \"field_path\"\
    : \"ingredients[5].concentration\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 6,\\\
    n                        \\\"compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 36,\\n                        \\\"amount\\\
    \": 0.36,\\n                        \\\"unit\\\": \\\"mg\\\",\\n             \
    \           \\\"g_l\\\": 0.00036,\\n                        \\\"mmol_l\\\": 0.00181905,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 6\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O                                                            \
    \   0.36      mg\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[5].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.00036\",\n          \"unit\"\
    : \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00036\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00036\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"0.36 mg ÷ 1000 = 0.00036 g; on the provider’s nominal 1 L basis this is 0.00036\
    \ g/L.\"\n  },\n  {\n    \"ingredient_or_context\": \"FeSO4 x 7 H2O\",\n    \"\
    field_path\": \"ingredients[6].concentration\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 7,\\\
    n                        \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n         \
    \               \\\"compound_id\\\": 12,\\n                        \\\"amount\\\
    \": 50,\\n                        \\\"unit\\\": \\\"mg\\\",\\n               \
    \         \\\"g_l\\\": 0.05,\\n                        \\\"mmol_l\\\": 0.179846,\\\
    n                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 7\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O                                                            \
    \   50.0      mg\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[6].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\":\
    \ \"G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"50 mg ÷ 1000 = 0.05 g; on the provider’s nominal 1 L basis this is 0.05 g/L.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"NaCl\",\n    \"field_path\": \"\
    ingredients[7].concentration\",\n    \"decision\": \"evidence_only\",\n    \"\
    local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 8,\\\
    n                        \\\"compound\\\": \\\"NaCl\\\",\\n                  \
    \      \\\"compound_id\\\": 43,\\n                        \\\"amount\\\": 200,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 200,\\n                        \\\"mmol_l\\\": 3422.31,\\n        \
    \                \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 8\",\n        \"exact_source_quote\"\
    : \"NaCl                                                                     \
    \ 200.0          g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The stored g/L equals the provider-declared\
    \ 1000 mL recipe basis, with no attached amount evidence in any layer. The primary\
    \ gives batch masses, not a measured final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"ingredients[7].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"200\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\"\
    : \"Provider g_l is copied on its declared 1 L basis; no primary final-volume\
    \ inference.\"\n  },\n  {\n    \"ingredient_or_context\": \"Na2CO3\",\n    \"\
    field_path\": \"ingredients[8].concentration\",\n    \"decision\": \"correct\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 9,\\\
    n                        \\\"compound\\\": \\\"Na2CO3\\\",\\n                \
    \        \\\"compound_id\\\": 32,\\n                        \\\"amount\\\": 50,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 50,\\n                        \\\"mmol_l\\\": 471.752,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 formulation row 9\",\n        \"exact_source_quote\"\
    : \"Na2CO3                                                                   \
    \   50.0         g\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"The 50 g table entry applies to the liquid\
    \ branch. The agar branch explicitly omits it and adds sterile carbonate solution\
    \ afterward; an unconditional 50 g/L ingredient in a solid recipe misstates scope.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[8].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"50\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"correct\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"arithmetic\": \"Provider\
    \ g_l is copied on its declared 1 L basis; no primary final-volume inference.\"\
    \n  },\n  {\n    \"ingredient_or_context\": \"Agar\",\n    \"field_path\": \"\
    ingredients[9].concentration\",\n    \"decision\": \"evidence_only\",\n    \"\
    local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 10,\\\
    n                        \\\"compound\\\": \\\"Agar\\\",\\n                  \
    \      \\\"compound_id\\\": 3,\\n                        \\\"amount\\\": 2,\\\
    n                        \\\"unit\\\": \\\"%\\\",\\n                        \\\
    \"g_l\\\": 20,\\n                        \\\"mmol_l\\\": 59.4654,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\n     \
    \ },\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\":\
    \ \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n   \
    \     \"source_locator\": \"Page1 preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Agar (2%) medium\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"Provider maps 2% agar to 20 g/L, but the\
    \ primary does not explicitly state w/v. Preserve the provider interpretation\
    \ and source percentage separately; do not claim a verified percent conversion.\"\
    ,\n    \"action_taken\": \"Review only; no recipe change.\",\n    \"layer_decisions\"\
    : [\n      {\n        \"input\": \"target\",\n        \"field_path\": \"ingredients[9].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"20\",\n          \"unit\": \"\
    G_PER_L\"\n        },\n        \"decision\": \"evidence_only\"\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"evidence_only\"\n      }\n    ],\n    \"arithmetic\":\
    \ \"Provider g_l is copied on its declared 1 L basis; no primary final-volume\
    \ inference.\"\n  },\n  {\n    \"ingredient_or_context\": \"Provider nominal volume\"\
    ,\n    \"field_path\": \"preparation.nominal_volume\",\n    \"decision\": \"add\"\
    ,\n    \"local\": null,\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive1431api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1431\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1000\",\n        \"snapshot_sha256\": \"d7f63f9c6a21af60ffc8d965dd611d9d251a8d4d3fcc6c9e5abae64a649a8afa\"\
    \n      }\n    ],\n    \"rationale\": \"The database declares 1000 mL; the primary\
    \ table omits water and final volume. Record the source and limitation without\
    \ inventing solvent or post-addition final volume.\",\n    \"action_taken\": \"\
    Review only; no recipe change.\",\n    \"layer_decisions\": [\n      {\n     \
    \   \"input\": \"target\",\n        \"field_path\": \"solutions\",\n        \"\
    stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Agar carbonate dose\",\n    \"field_path\": \"preparation.Agar_carbonate_dose\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n       \
    \ \"source_locator\": \"Page1 agar preparation paragraph\",\n        \"exact_source_quote\"\
    : \"Add 20-30 ml of a\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the exact agar-stage range/strength/pH\
    \ and attach evidence. The carbonate percentage basis is unspecified; do not calculate\
    \ carbonate mass, midpoint dose or final volume. The bacterial owner lacks the\
    \ preparation paragraph.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Liquid medium may be prepared by adding all components together. Agar (2%)\
    \ medium should be prepared without Na2CO3 and sterilised by autoclaving. Add\
    \ 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing\
    \ agar so that the final pH is 9.0.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Liquid medium may be prepared by adding all components together. Agar (2%)\
    \ medium should be prepared without Na2CO3 and sterilised by autoclaving. Add\
    \ 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing\
    \ agar so that the final pH is 9.0.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Agar carbonate stock strength\",\n    \"field_path\": \"preparation.Agar_carbonate_stock_strength\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n       \
    \ \"source_locator\": \"Page1 agar preparation paragraph\",\n        \"exact_source_quote\"\
    : \"sterile 10% Na2CO3 solution\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the exact agar-stage range/strength/pH\
    \ and attach evidence. The carbonate percentage basis is unspecified; do not calculate\
    \ carbonate mass, midpoint dose or final volume. The bacterial owner lacks the\
    \ preparation paragraph.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Liquid medium may be prepared by adding all components together. Agar (2%)\
    \ medium should be prepared without Na2CO3 and sterilised by autoclaving. Add\
    \ 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing\
    \ agar so that the final pH is 9.0.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Liquid medium may be prepared by adding all components together. Agar (2%)\
    \ medium should be prepared without Na2CO3 and sterilised by autoclaving. Add\
    \ 20-30 ml of a sterile 10% Na2CO3 solution to the autoclaved medium containing\
    \ agar so that the final pH is 9.0.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ]\n  },\n  {\n    \"ingredient_or_context\"\
    : \"Agar final pH\",\n    \"field_path\": \"preparation.Agar_final_pH\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local\": null,\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1431\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf\",\n       \
    \ \"source_locator\": \"Page1 agar preparation paragraph\",\n        \"exact_source_quote\"\
    : \"pH is 9.0.\",\n        \"snapshot_sha256\": \"b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514\"\
    ,\n        \"parsed_text_sha256\": \"5533b8c3f7f46cb8e3cf2d7ec2367afe3f649314db41de453efe92657727f07c\"\
    \n      }\n    ],\n    \"rationale\": \"Retain the exact agar-stage range/strength/pH\
    \ and attach evidence. The carbonate percentage basis is unspecified; do not calculate\
    \ carbonate mass, midpoint dose or final volume. The bacterial owner lacks the\
    \ preparation paragraph.\",\n    \"action_taken\": \"Review only; no recipe change.\"\
    ,\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n     \
    \   \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ]\n  }\n]"
- assessment_id: identity
  area: identity
  topic: Repeated basename with two distinct maintained contributors
  outcome: supported
  summary: The repeated merged_from/source basename resolves to archaea CM000255 (DSMZ1431)
    and bacterial CM004157 (KOMODO1431). Both exact paths are inspected; they must
    not be collapsed by basename lookup. Source title/accession agree, but ingredient-set
    identity does not erase preparation or source metadata.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - dsmz1431
  - komodo1431-catalog
- assessment_id: source-stage-consistency
  area: consistency
  topic: Liquid and agar branches versus declared g/L
  outcome: concern
  summary: All 30 local ingredient concentrations are covered. Eight noncarbonate
    solute values agree with the provider’s nominal 1 L basis, including 0.36 mg manganese
    salt→0.00036 g and 50 mg iron salt→0.05 g. The 50 g carbonate entry belongs to
    the liquid recipe; the agar branch omits it before autoclaving and receives 20–30
    mL sterile 10% carbonate. Primary percentage bases and final volume remain unspecified.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1431
  - mediadive1431api
  - quantity-inventory
  - quantity-local-fields
- assessment_id: forms
  area: grounding
  topic: Exact salts and undefined mixtures
  outcome: supported
  summary: Trisodium citrate matches CHEBI:53258’s trisodium definition; potassium
    chloride, magnesium sulfate heptahydrate, manganese chloride tetrahydrate, iron
    sulfate heptahydrate, sodium chloride and carbonate match the explicitly stated
    forms. No citrate hydrate is inferred. Yeast extract and casamino acids remain
    mixtures; missing optional IDs do not justify assigning pure molecules. Agar is
    an undefined polysaccharide mixture.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - dsmz1431
  - chebi53258
  - chebi32588
  - chebi31795
  - chebi86368
  - chebi75836
  - chebi26710
  - chebi29377
  - chebi2509
- assessment_id: preparation
  area: completeness
  topic: Correct retained prose with an incompatible unconditional formula
  outcome: concern
  summary: The target and DSMZ owner preserve the source’s complete liquid/agar paragraph,
    including the final pH 9.0. The KOMODO owner lacks it. The prose does not reconcile
    an unconditional 50 g/L carbonate plus agar formula. Autoclaving is specified
    for agar; temperature and duration are not. No cycle is invented.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1431
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Physical branch, category labels and high_metal
  outcome: concern
  summary: COMPLEX/UNDEFINED fits yeast extract and casamino acids. SOLID_AGAR selects
    the agar branch but the carbonate formula does not follow that branch. Both filing
    categories are retained; no taxon, strain, DOI/PMID, assembly or growth outcome
    is asserted. On the provider’s nominal 1 L basis, sodium chloride alone is about
    3422 mM (200 g/L ÷ 58.443 g/mol ×1000), compatible with the schema’s inclusive
    high_metal threshold; this is neither heavy-metal toxicity nor growth evidence.
    KOMODO Aerobic:No is catalog metadata, not a primary atmosphere protocol.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1431
  - komodo1431-catalog
  - schema-metal
  - chebi26710
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 28 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: generation
  area: provenance
  topic: Source-copy and current conservative merge boundaries
  outcome: concern
  summary: Both owners retain identical ten ingredient values, but only the DSMZ owner
    has preparation. Historical copying/merge events explain the provenance claims
    without proving exact source equivalence. Current formulation merging requires
    scientific fields and preparation to agree and retains scoped evidence; the old
    ingredient-set fingerprint is insufficient. No generator was run.
  target_ids:
  - CultureMech:000255
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - history-metadata
  - writer-context-0
  - writer-context-1
  - writer-context-2
findings:
- finding_id: f1
  issue_key: culturemech.000255.liquid-agar-carbonate-scope
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Agar medium retains the liquid branch carbonate amount
  description: The source explicitly distinguishes liquid components from agar prepared
    without carbonate followed by a 20–30 mL sterile 10% carbonate addition. The solid
    record and both owners instead assert 50 g/L carbonate alongside agar. Preserved
    prose in two layers does not repair the unconditional ingredient claim; the KOMODO
    owner lacks the preparation.
  target_ids:
  - CultureMech:000255
  field_paths:
  - ingredients[8].concentration
  - ingredients[9].concentration
  - physical_state
  - preparation_steps
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1431
  - mediadive1431api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.000255.amount-evidence-basis
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Nominal concentration basis lacks claim-level source evidence
  description: All local amounts lack attached concentration evidence. The primary
    supplies batch masses but no water/final-volume quantity, while the provider declares
    1000 mL and interprets 2% agar as 20 g/L. Those distinct support levels must remain
    explicit.
  target_ids:
  - CultureMech:000255
  field_paths:
  - ingredients
  - references
  - evidence
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1431
  - mediadive1431api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4.3
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.000255.history-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO history contains malformed and timezone-naive timestamps
  description: The bacterial owner’s import timestamp ends in .fZ and its composition-copy
    timestamp lacks a timezone. Other chronology remains contextual, not authenticated
    historical source retrieval.
  target_ids:
  - CultureMech:000255
  field_paths:
  - curation_history
  evidence_ids:
  - owner-1
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P4
  native_severity: P4
  normalization_reason: P4 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Represent the liquid and agar branches explicitly in maintained inputs,
    retain the correct carbonate addition stage and range, and preserve the unspecified
    percentage/final-volume basis. Add exact claim evidence and reconcile the missing
    KOMODO preparation before separately authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000255
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
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
  description: Attach exact source rows and provider basis to each supported amount.
    Preserve the primary’s original units and unidentified percentage basis; do not
    manufacture a final water amount or verified percent conversion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000255
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
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
  description: Preserve append-only history and add a bounded clarification if original
    timing can be established; do not silently invent or rewrite old timestamps.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000255
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkalophilic_halophile_medium.yaml
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
- The preserved komodoMediaList retrieval returned HTTP403. Exact DSMZ1431 primary
  and provider are available; the KOMODO catalog supports identity only, not an independently
  inspected detailed formulation.
- The preserved komodo1431 retrieval returned HTTP403. Exact DSMZ1431 primary and
  provider are available; the KOMODO catalog supports identity only, not an independently
  inspected detailed formulation.
- The preserved komodoDetail1431 retrieval returned HTTP403. Exact DSMZ1431 primary
  and provider are available; the KOMODO catalog supports identity only, not an independently
  inspected detailed formulation.
- No exact final volume is given by the primary, and neither agar 2% nor carbonate
  10% explicitly names a mass/volume basis. No liquid density, carbonate mass or replacement
  concentration is inferred.
- Failed KOMODO detail attempts are retained as optional source-access limits because
  the exact DSMZ primary and provider supply the assessed base formulation; the catalog
  is used only for identity/encoded metadata.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-024
- generated-medium
```
