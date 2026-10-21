# Source and formulation review: amphibacillus_medium (CultureMech:001660)

- Review: 20261021T145417Z-culturemech-001660-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:47:46Z
- Finished UTC: 2026-10-21T14:54:17Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact DSMZ/KOMODO 529 source identity resolves, but the sesquicarbonate stock is flattened into direct medium ingredients. Primary 1000 mL water and ambiguous 1 mL in 10 mL supplementation differ from provider 900 mL water plus 100 mL stock; manganese heptahydrate is grounded to an anhydrous structure. Preserve source-specific scope and the literal primary formula typo.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 255; batch 026 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-five task batches contain 250 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 253 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001660 | data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml | generated | amphibacillus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001660 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001660 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/255/strict.tsv |
| validate-terms | passed | True | CultureMech:001660 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001660 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001660 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: komodoDetail529 | unavailable | False | CultureMech:001660 | KOMODO 529 detail returns HTTP 403. Current base formulation can be assessed from the exact catalogue link and primary sources 529 and 31; historical byte equivalence and a distinct KOMODO variant are not inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001660.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001660.

21 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "quantity": "Glucose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Glucose                                                                  10.000          g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 55.5062,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q2",
    "quantity": "K2HPO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "K2HPO4                                                                     1.000         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q3",
    "quantity": "NH4NO3",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "NH4NO3                                                                     2.000         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4NO3\",\n                        \"compound_id\": 178,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q4",
    "quantity": "MgSO4 x 7 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "MgSO4 x 7 H2O                                                              0.200         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q5",
    "quantity": "MnSO4 x 7 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "MnSO4 x 7 H2O                                                              0.005         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MnSO4 x 7 H2O\",\n                        \"compound_id\": 543,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0331124,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q6",
    "quantity": "FeSO4 x 7 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "FeSO4 x 7 H2O                                                              0.005         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0179846,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q7",
    "quantity": "CaCl2 x 2 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O                                                              0.100         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q8",
    "quantity": "Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Yeast extract                                                              3.000         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q9",
    "quantity": "Polypeptone",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Polypeptone (BBL)                                                          0.300         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Polypeptone\",\n                        \"compound_id\": 442,\n                        \"attribute\": \"BBL\",\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q10",
    "quantity": "Agar",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Agar                                                                     15.000          g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Existing values match provider g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve primary batch grams, original supplied forms and the primary/provider water/addition discrepancy. Do not invent a measured final concentration or resolve 1 mL in 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an optional row."
  },
  {
    "quantity_id": "q11",
    "quantity": "NaHCO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "42",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "42",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "42",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 4.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 42,\n                        \"mmol_l\": 499.958,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "42/53 g/L are provider stock strengths from 4.2/5.3 g with 100 mL water, not direct final-medium concentrations. Represent stock composition and receiving addition separately. No fixed final bicarbonate/carbonate value is invented."
  },
  {
    "quantity_id": "q12",
    "quantity": "Na2CO3 anhydrous",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "53",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "53",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2CO3 anhydrous\",\n                        \"compound_id\": 69,\n                        \"attribute\": \"anhydrous\",\n                        \"amount\": 5.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 53,\n                        \"mmol_l\": 500.057,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "42/53 g/L are provider stock strengths from 4.2/5.3 g with 100 mL water, not direct final-medium concentrations. Represent stock composition and receiving addition separately. No fixed final bicarbonate/carbonate value is invented."
  },
  {
    "quantity_id": "q13",
    "quantity": "Primary basal water versus provider water",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Main distilled-water row",
        "exact_source_quote": "Distilled water                                                       1000.000          ml",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      },
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 900,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Primary 1000 mL water conflicts with provider 900 mL water plus stock. Neither layer stores an explicit water/batch basis. Keep both versions rather than silently converting all quantities to a chosen endpoint."
  },
  {
    "quantity_id": "q14",
    "quantity": "Primary stock input: NaHCO3                                                                     4.200         g",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Na-sesquicarbonate exact named row",
        "exact_source_quote": "NaHCO3                                                                     4.200         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Separate stock recipe, preserving g and mL inputs. The literal Na2CO2 typography is not a new chemical identity; referenced source 31 and provider identify Na2CO3 anhydrous. Do not infer final medium concentration."
  },
  {
    "quantity_id": "q15",
    "quantity": "Primary stock input: Na2CO2 (anhydrous)                                                         5.300         g",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Na-sesquicarbonate exact named row",
        "exact_source_quote": "Na2CO2 (anhydrous)                                                         5.300         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Separate stock recipe, preserving g and mL inputs. The literal Na2CO2 typography is not a new chemical identity; referenced source 31 and provider identify Na2CO3 anhydrous. Do not infer final medium concentration."
  },
  {
    "quantity_id": "q16",
    "quantity": "Primary stock input: Distilled water                                                         100.000         ml",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Na-sesquicarbonate exact named row",
        "exact_source_quote": "Distilled water                                                         100.000         ml",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Separate stock recipe, preserving g and mL inputs. The literal Na2CO2 typography is not a new chemical identity; referenced source 31 and provider identify Na2CO3 anhydrous. Do not infer final medium concentration."
  },
  {
    "quantity_id": "q17",
    "quantity": "Referenced stock carbonate identity and amount",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[11].preferred_term",
        "stored": "Na2CO3 anhydrous"
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ingredients[11].preferred_term",
        "stored": "Na2CO3 anhydrous"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ingredients[11].preferred_term",
        "stored": "Na2CO3 anhydrous"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz31",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium31.pdf",
        "source_locator": "Na-sesquicarbonate carbonate row",
        "exact_source_quote": "Na2CO3 anhydrous                                                             5.3         g",
        "snapshot_sha256": "7dc9960a76f9921d94721aac3488c3b72d4252193e2e62df241ec96d6eb37705",
        "parsed_text_sha256": "921918329f48a3c6d1c348f805c3dfab12f45b150436478cb5e9e226f5b8b83a"
      },
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Na-sesquicarbonate printed Na2CO2 row",
        "exact_source_quote": "Na2CO2 (anhydrous)                                                         5.300         g",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Source 529 prints Na2CO2; its explicit reference 31 prints Na2CO3 anhydrous, consistent with the provider and existing ingredient name. Retain the discrepancy and narrow justification rather than claiming identical primary wording."
  },
  {
    "quantity_id": "q18",
    "quantity": "Receiving stock label and dose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "After sterilization add sterile 1 M Na-sesquicarbonate solution (1 ml in 10 ml) to achieve a pH of 9.7 (see medium 31)."
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "After sterilization add sterile 1 M Na-sesquicarbonate solution (1 ml in 10 ml) to achieve a pH of 9.7 (see medium 31)."
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Post-sterilization instruction",
        "exact_source_quote": "After sterilization add sterile 1 M Na-sesquicarbonate solution (1 ml in 10 ml) to achieve\na pH of 9.7 (see medium 31).",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Target and DSMZ owner preserve 1 M, 1 mL in 10 mL, post-sterilization addition and pH 9.7 without attached evidence. KOMODO owner lacks the step and requires addition. The 1 M label does not authorize multiplying both salt components or assuming a total final-volume convention."
  },
  {
    "quantity_id": "q19",
    "quantity": "Receiving target pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 9.7
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 9.7
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "ph_value",
        "stored": 9.7
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Post-sterilization pH instruction",
        "exact_source_quote": "After sterilization add sterile 1 M Na-sesquicarbonate solution (1 ml in 10 ml) to achieve\na pH of 9.7 (see medium 31).",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Existing target pH 9.7 is supported as a source target, not a measured experimental value; attach narrow evidence in all three layers."
  },
  {
    "quantity_id": "q20",
    "quantity": "Provider stock receiving volume",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive529api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/529",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Na-sesquicarbonate solution\",\n                        \"solution_id\": 1174,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152"
      }
    ],
    "source_stage_and_basis": "Provider 100 mL dose belongs to its declared 900+100 mL representation. Preserve separately from primary 1 mL in 10 mL; do not choose an unproven denominator."
  },
  {
    "quantity_id": "q21",
    "quantity": "Unspecified numerical sterilization cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "sterilization_method",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
        "field_path": "sterilization_method",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
        "field_path": "sterilization_method",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz529",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf",
        "source_locator": "Post-sterilization sentence",
        "exact_source_quote": "After sterilization add sterile 1 M Na-sesquicarbonate solution",
        "snapshot_sha256": "4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394",
        "parsed_text_sha256": "a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4"
      }
    ],
    "source_stage_and_basis": "Primary specifies sterilization before sterile stock addition, but no temperature or duration. Provider names Autoclave as equipment without a numerical cycle; no default is imported from another collection."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:001660.

10 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 10/12 primary and 10/12 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 12: primary 83.33%; secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:001660.

23 timestamp instances inspected; 2 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source, both owners and reciprocal relationships

identity: supported. Targets: CultureMech:001660.

DSMZ 529 and KOMODO 529 catalogue identity/link resolve. Both explicit normalized contributors and their reciprocal declared paths/stable IDs resolve; shared local ingredient signatures do not prove identical historical source bytes or erase owner preparation differences.

### Supplied hydrate and carbonate spelling

grounding: concern. Targets: CultureMech:001660.

Source MnSO4 x 7 H2O is mapped to CHEBI:86360, whose formula Mn.O4S and anhydrous synonym omit seven waters. Other explicit hydrate structures match their source names. Primary carbonate Na2CO2 is a printed conflict resolved narrowly by its cited source 31 and provider; no unverified replacement ID is proposed.

### Post-sterilization addition and source-specific quantities

completeness: concern. Targets: CultureMech:001660.

The target and DSMZ owner retain the single preparation sentence, but the KOMODO owner does not. All layers omit a separate stock descriptor, batch water basis and claim-level references/evidence. Stored 42 and 53 g/L conceal the stock boundary; the source/provider volume disagreement remains unresolved.

### Complex solid medium and bounded biological claims

scope: supported. Targets: CultureMech:001660.

Yeast extract/Polypeptone support complex/undefined classification; explicit agar supports solid agar. The pH is a formulation target. Catalogue aerobic=false is metadata only, and neither title nor application supplies organism-specific growth evidence. No DOI, PMID, taxonomy or KG-match assertion is present.

## Findings

### f1: Separate sesquicarbonate stock strengths are flattened

blocker / open / confirmed; issue key: cm001660-sesquicarbonate-stock.

All three local layers place 42 g/L bicarbonate and 53 g/L carbonate among direct ingredients, although they describe the separate stock. Primary 1000 mL water and 1 mL in 10 mL differ from provider 900+100 mL; no measured final denominator is established.

### f2: Manganese heptahydrate has an anhydrous ontology structure

major / open / confirmed; issue key: cm001660-manganese-hydrate.

The source and preferred name require MnSO4 x 7 H2O, while CHEBI:86360 and the copied current MIM key describe MnSO4 without hydrate waters. Matching canonical labels do not verify exact supplied form.

### f3: Scoped amount evidence and owner preparation are incomplete

major / open / confirmed; issue key: cm001660-claim-evidence-preparation.

No layer attaches evidence for its amounts, stock dose or pH; KOMODO additionally lacks the preparation sentence present in the DSMZ owner/target. A source link alone does not support the flattened stage.

### f4: KOMODO history contains malformed and naive timestamps

minor / open / confirmed; issue key: cm001660-komodo-history.

The KOMODO owner has malformed 2026-01-27T01:15:03.fZ and timezone-naive enrichment timestamps. The selected target history does not contain these specific events.

## Recommended Actions And Acceptance Checks

### a1

Preserve a separate stock with source composition and stage-specific dose in both maintained owners; reconcile primary/provider volume interpretations explicitly before regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Stock strengths do not become direct medium concentrations; all source versions and unknown final-volume assumptions remain explicit.

### a2

Verify the exact hydrate identity and source-supported ontology before changing primary and secondary links; do not guess a replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Hydrate count and structure match the supplied material.

### a3

Attach exact primary/provider evidence to the narrowest claim and retain the current owner-specific preparation and volume conflict; regenerate only compatible representations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Every amount has explicit stage/basis evidence and source-correct preparation survives merging.

### a4

Preserve old history; append source-backed clarification or repair the responsible importer for future output without inventing historical UTC.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch026/255/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/255/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml:1:id: CultureMech:001660<br>./data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml:1:id: CultureMech:001660<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/255/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 16 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf; Whole primary table, post-sterilization instruction and stock | supports | The source lists basal batch amounts, 1000 mL water and a separately prepared sesquicarbonate stock. The exact 1 mL in 10 mL wording does not independently determine whether the receiving volume includes the addition. |
| stock-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium31.pdf; Na-sesquicarbonate subsection only | supports | Referenced source 31 confirms Na2CO3 anhydrous, whereas 529 prints Na2CO2. No unrelated medium 1 formulation transfers. |
| api | https://mediadive.dsmz.de/rest/medium/529; Entire metadata, main and stock recipes and preparation | supports | Provider interpretation uses 900 mL water plus 100 mL stock on a declared 1000 mL basis; keep it distinct from the primary 1000 mL water instruction. |
| stock-api | https://mediadive.dsmz.de/rest/solution/1174; Entire exact stock endpoint | supports | 4.2 g bicarbonate and 5.3 g anhydrous carbonate with 100 mL water; provider g/L values belong to this stock. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact raw MediaInfo=529 row | supports | Accession, DSMZ link, pH 9.7 and catalogue flags are verified as metadata, not physiology. |
| catalog-header | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact column header | supports | The false flag appears under Is Aerobic; complex=true is catalogue metadata. |
| komodoDetail529-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=529; Preserved exact public retrieval result | context_only | KOMODO 529 detail returns HTTP 403. Current base formulation can be assessed from the exact catalogue link and primary sources 529 and 31; historical byte equivalence and a distinct KOMODO variant are not inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch026/255/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63038 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63038; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63038 resolves to ammonium nitrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63038": [{"label": "(NH4)NO3", "match_type": "preferred_term", "identifier": "CHEBI:63038", "preferred_term": "(NH4)NO3", "ontology_id": "CHEBI:63038", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86360": [{"label": "MnSO4", "match_type": "preferred_term", "identifier": "CHEBI:86360", "preferred_term": "MnSO4", "ontology_id": "CHEBI:86360", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml; data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:07.298172"}]}] |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current primary/stock importer, preparation collection, non-summing cleanup and formulation compatibility inspected; historical execution is not inferred from current code. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current primary/stock importer, preparation collection, non-summing cleanup and formulation compatibility inspected; historical execution is not inferred from current code. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current primary/stock importer, preparation collection, non-summing cleanup and formulation compatibility inspected; historical execution is not inferred from current code. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- KOMODO 529 detail returns HTTP 403. Current base formulation can be assessed from the exact catalogue link and primary sources 529 and 31; historical byte equivalence and a distinct KOMODO variant are not inferred.
- The dose phrase 1 mL in 10 mL is retained exactly; source text alone does not settle whether 10 mL includes the addition. Current provider 900+100 mL is a separate interpretation.
- Numerical sterilization temperature/time and the reason for the primary carbonate typo are not inferred. Completed review means the bounded source comparisons were completed, not that these scientific conflicts were resolved.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T145417Z-culturemech-001660-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: amphibacillus_medium (CultureMech:001660)'
started_at: '2026-10-21T14:47:46Z'
finished_at: '2026-10-21T14:54:17Z'
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
summary: Exact DSMZ/KOMODO 529 source identity resolves, but the sesquicarbonate stock
  is flattened into direct medium ingredients. Primary 1000 mL water and ambiguous
  1 mL in 10 mL supplementation differ from provider 900 mL water plus 100 mL stock;
  manganese heptahydrate is grounded to an anhydrous structure. Preserve source-specific
  scope and the literal primary formula typo.
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
  - path: data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
    sha256: ed01aa482f5d760e0417ef75f7f3b1f67ef35d8215017503c50e0f6984dec58f
    role: target
  - path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    sha256: 5f6c9b5b61c7698abd6a347b8db8af73444da2513ee3c15cf142a7fb6cc189d5
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
    sha256: 5c1e8b1077d606fba4bc09ce8fbc0ebd023823dcc68257cf2a1f997c394973f1
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
  - path: src/culturemech/validation/recipe_references.py
    sha256: 5d49d3db2f043a82b253e5a0bed03239004043922e1daab43c399a84d64fc237
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 255; batch 026 item 5 of 10, selected in Python lexicographic
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
  - CultureMech:001660
targets:
- target_id: CultureMech:001660
  path: data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  label: amphibacillus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch026/255/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/255/strict.tsv"
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001660
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
  - CultureMech:001660
- check_id: komodoDetail529-source-access
  name: 'Exact source content access: komodoDetail529'
  required: false
  status: unavailable
  summary: KOMODO 529 detail returns HTTP 403. Current base formulation can be assessed
    from the exact catalogue link and primary sources 529 and 31; historical byte
    equivalence and a distinct KOMODO variant are not inferred.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - komodoDetail529-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:50.739485Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch026/255/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:52.121833Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/255/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:53.774033Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:49:54.731888Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:54:15Z'
  support: supports
  summary: './data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml:1:id: CultureMech:001660

    ./data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml:1:id: CultureMech:001660

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/255/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:54:15Z'
  support: supports
  summary: 16 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 9c0497a054bbbd0b39db630b7e51b10635d90d1fd2bbf2f2f4c47ebbf66526bb
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf
  locator: Whole primary table, post-sterilization instruction and stock
  accessed_at: '2026-10-21T14:17:00.000060Z'
  support: supports
  summary: The source lists basal batch amounts, 1000 mL water and a separately prepared
    sesquicarbonate stock. The exact 1 mL in 10 mL wording does not independently
    determine whether the receiving volume includes the addition.
  snapshot_sha256: 4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394
- evidence_id: stock-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium31.pdf
  locator: Na-sesquicarbonate subsection only
  accessed_at: '2026-10-21T12:52:18.780062Z'
  support: supports
  summary: Referenced source 31 confirms Na2CO3 anhydrous, whereas 529 prints Na2CO2.
    No unrelated medium 1 formulation transfers.
  snapshot_sha256: 7dc9960a76f9921d94721aac3488c3b72d4252193e2e62df241ec96d6eb37705
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/529
  locator: Entire metadata, main and stock recipes and preparation
  accessed_at: '2026-10-21T14:16:58.559292Z'
  support: supports
  summary: Provider interpretation uses 900 mL water plus 100 mL stock on a declared
    1000 mL basis; keep it distinct from the primary 1000 mL water instruction.
  snapshot_sha256: d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152
- evidence_id: stock-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1174
  locator: Entire exact stock endpoint
  accessed_at: '2026-10-21T14:19:01.074687Z'
  support: supports
  summary: 4.2 g bicarbonate and 5.3 g anhydrous carbonate with 100 mL water; provider
    g/L values belong to this stock.
  snapshot_sha256: 8bb790b338f798560c2018b93c85c94385811a4267b9dd4911876902eda85c30
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact raw MediaInfo=529 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Accession, DSMZ link, pH 9.7 and catalogue flags are verified as metadata,
    not physiology.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=529'\
    \ >529</a></TD>\n\t\t\t\t\t<TD>AMPHIBACILLUS medium</TD>\n\t\t\t\t\t<TD> 9.7</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: catalog-header
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact column header
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The false flag appears under Is Aerobic; complex=true is catalogue metadata.
  quote: "<TR>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\" width=\"50\">ID</TD>\n\
    \t\t\t\t\t<TD valign=\"top\" align=\"left\">Name</TD>\n\t\t\t\t\t<TD valign=\"\
    top\" align=\"left\">PH Info</TD>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\"\
    >Is Complex</TD>\n\t\t\t\t\t<TD valign=\"top\" align=\"left\">Is Aerobic</TD>\n\
    \t\t\t\t\t<TD valign=\"top\" align=\"left\">Is SubMedium</TD>\n\t\t\t\t\t<TD valign=\"\
    top\" align=\"left\">Instructions</TD>\n\t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: komodoDetail529-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=529
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T14:16:58.252901Z'
  support: context_only
  summary: KOMODO 529 detail returns HTTP 403. Current base formulation can be assessed
    from the exact catalogue link and primary sources 529 and 31; historical byte
    equivalence and a distinct KOMODO variant are not inferred.
  snapshot_sha256: eb54f9cfa21dc4fdaf8094d7b2e98c2bb8f744918ebb26fe951de22c7cf6371a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/255/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: d7ec0821c56de21a26bbfe5bd42f4d827d2fbf08cd6ab6c8936d2eacf1fff8e7
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
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
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
- evidence_id: chebi63038
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63038
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T12:23:44.217684Z'
  support: supports
  summary: CHEBI:63038 resolves to ammonium nitrate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 3e84a6e44c936aaa0dd03b53fbb9592dccb6de0f8331244a80e4f2292296b2c4
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
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T14:54:15Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label":
    "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term":
    "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O",
    "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63038":
    [{"label": "(NH4)NO3", "match_type": "preferred_term", "identifier": "CHEBI:63038",
    "preferred_term": "(NH4)NO3", "ontology_id": "CHEBI:63038", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term":
    "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id":
    "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86360":
    [{"label": "MnSO4", "match_type": "preferred_term", "identifier": "CHEBI:86360",
    "preferred_term": "MnSO4", "ontology_id": "CHEBI:86360", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml; data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml;
    data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:07.298172"}]}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Current primary/stock importer, preparation collection, non-summing cleanup
    and formulation compatibility inspected; historical execution is not inferred
    from current code.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Current primary/stock importer, preparation collection, non-summing cleanup
    and formulation compatibility inspected; historical execution is not inferred
    from current code.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:54:15Z'
  support: context_only
  summary: Current primary/stock importer, preparation collection, non-summing cleanup
    and formulation compatibility inspected; historical execution is not inferred
    from current code.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 21 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"quantity\": \"Glucose\",\n\
    \    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Glucose                                                                  10.000\
    \          g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\":\
    \ 5,\\n                        \\\"amount\\\": 10,\\n                        \\\
    \"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n         \
    \               \\\"mmol_l\\\": 55.5062,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"quantity\":\
    \ \"K2HPO4\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"K2HPO4                                                                   \
    \  1.000         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 5.74132,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"quantity\":\
    \ \"NH4NO3\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"NH4NO3                                                                   \
    \  2.000         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NH4NO3\\\",\\n                        \\\"compound_id\\\": 178,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 2,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"quantity\":\
    \ \"MgSO4 x 7 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O                                                            \
    \  0.200         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n  \
    \                      \\\"mmol_l\\\": 0.811438,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"quantity\":\
    \ \"MnSO4 x 7 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"MnSO4 x 7 H2O                                                            \
    \  0.005         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 543,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0331124,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"quantity\":\
    \ \"FeSO4 x 7 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O                                                            \
    \  0.005         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n\
    \                        \\\"mmol_l\\\": 0.0179846,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"quantity\":\
    \ \"CaCl2 x 2 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O                                                            \
    \  0.100         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.1,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n  \
    \                      \\\"mmol_l\\\": 0.680203,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"quantity\":\
    \ \"Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Yeast extract                                                            \
    \  3.000         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 3,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"quantity\":\
    \ \"Polypeptone\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Polypeptone (BBL)                                                        \
    \  0.300         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Polypeptone\\\",\\n                        \\\"compound_id\\\
    \": 442,\\n                        \\\"attribute\\\": \\\"BBL\\\",\\n        \
    \                \\\"amount\\\": 0.3,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 0.3,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"quantity\"\
    : \"Agar\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Agar                                                                     15.000\
    \          g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing values match provider\
    \ g/L on its declared 1000 mL basis, with no attached evidence in any layer. Preserve\
    \ primary batch grams, original supplied forms and the primary/provider water/addition\
    \ discrepancy. Do not invent a measured final concentration or resolve 1 mL in\
    \ 10 mL by assumption. Agar is an explicit solid-medium ingredient here, not an\
    \ optional row.\"\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"quantity\"\
    : \"NaHCO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"42\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"42\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"42\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive529api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/529\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[0]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 1,\\\
    n                        \\\"compound\\\": \\\"NaHCO3\\\",\\n                \
    \        \\\"compound_id\\\": 55,\\n                        \\\"amount\\\": 4.2,\\\
    n                        \\\"unit\\\": \\\"g\\\",\\n                        \\\
    \"g_l\\\": 42,\\n                        \\\"mmol_l\\\": 499.958,\\n         \
    \               \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"42/53 g/L are provider stock strengths\
    \ from 4.2/5.3 g with 100 mL water, not direct final-medium concentrations. Represent\
    \ stock composition and receiving addition separately. No fixed final bicarbonate/carbonate\
    \ value is invented.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"quantity\"\
    : \"Na2CO3 anhydrous\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"53\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"53\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"53\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive529api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/529\"\
    ,\n        \"source_locator\": \"$.data.solutions[1].recipe[1]\",\n        \"\
    exact_source_quote\": \"{\\n                        \\\"recipe_order\\\": 2,\\\
    n                        \\\"compound\\\": \\\"Na2CO3 anhydrous\\\",\\n      \
    \                  \\\"compound_id\\\": 69,\\n                        \\\"attribute\\\
    \": \\\"anhydrous\\\",\\n                        \\\"amount\\\": 5.3,\\n     \
    \                   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 53,\\n                        \\\"mmol_l\\\": 500.057,\\n                \
    \        \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"42/53 g/L are provider stock strengths\
    \ from 4.2/5.3 g with 100 mL water, not direct final-medium concentrations. Represent\
    \ stock composition and receiving addition separately. No fixed final bicarbonate/carbonate\
    \ value is invented.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"quantity\"\
    : \"Primary basal water versus provider water\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz529\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Main distilled-water row\",\n        \"exact_source_quote\"\
    : \"Distilled water                                                       1000.000\
    \          ml\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      },\n      {\n        \"source_key\": \"mediadive529api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 900,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Primary 1000 mL water conflicts\
    \ with provider 900 mL water plus stock. Neither layer stores an explicit water/batch\
    \ basis. Keep both versions rather than silently converting all quantities to\
    \ a chosen endpoint.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"quantity\"\
    : \"Primary stock input: NaHCO3                                              \
    \                       4.200         g\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz529\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Na-sesquicarbonate exact named row\",\n     \
    \   \"exact_source_quote\": \"NaHCO3                                         \
    \                            4.200         g\",\n        \"snapshot_sha256\":\
    \ \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\",\n    \
    \    \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Separate stock recipe, preserving\
    \ g and mL inputs. The literal Na2CO2 typography is not a new chemical identity;\
    \ referenced source 31 and provider identify Na2CO3 anhydrous. Do not infer final\
    \ medium concentration.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"quantity\"\
    : \"Primary stock input: Na2CO2 (anhydrous)                                  \
    \                       5.300         g\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz529\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Na-sesquicarbonate exact named row\",\n     \
    \   \"exact_source_quote\": \"Na2CO2 (anhydrous)                             \
    \                            5.300         g\",\n        \"snapshot_sha256\":\
    \ \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\",\n    \
    \    \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Separate stock recipe, preserving\
    \ g and mL inputs. The literal Na2CO2 typography is not a new chemical identity;\
    \ referenced source 31 and provider identify Na2CO3 anhydrous. Do not infer final\
    \ medium concentration.\"\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"quantity\"\
    : \"Primary stock input: Distilled water                                     \
    \                    100.000         ml\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz529\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Na-sesquicarbonate exact named row\",\n     \
    \   \"exact_source_quote\": \"Distilled water                                \
    \                         100.000         ml\",\n        \"snapshot_sha256\":\
    \ \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\",\n    \
    \    \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Separate stock recipe, preserving\
    \ g and mL inputs. The literal Na2CO2 typography is not a new chemical identity;\
    \ referenced source 31 and provider identify Na2CO3 anhydrous. Do not infer final\
    \ medium concentration.\"\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"quantity\"\
    : \"Referenced stock carbonate identity and amount\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].preferred_term\",\n        \"stored\"\
    : \"Na2CO3 anhydrous\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].preferred_term\",\n        \"stored\"\
    : \"Na2CO3 anhydrous\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].preferred_term\",\n        \"stored\"\
    : \"Na2CO3 anhydrous\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz31\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium31.pdf\"\
    ,\n        \"source_locator\": \"Na-sesquicarbonate carbonate row\",\n       \
    \ \"exact_source_quote\": \"Na2CO3 anhydrous                                 \
    \                            5.3         g\",\n        \"snapshot_sha256\": \"\
    7dc9960a76f9921d94721aac3488c3b72d4252193e2e62df241ec96d6eb37705\",\n        \"\
    parsed_text_sha256\": \"921918329f48a3c6d1c348f805c3dfab12f45b150436478cb5e9e226f5b8b83a\"\
    \n      },\n      {\n        \"source_key\": \"dsmz529\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\",\n    \
    \    \"source_locator\": \"Na-sesquicarbonate printed Na2CO2 row\",\n        \"\
    exact_source_quote\": \"Na2CO2 (anhydrous)                                   \
    \                      5.300         g\",\n        \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source 529 prints Na2CO2;\
    \ its explicit reference 31 prints Na2CO3 anhydrous, consistent with the provider\
    \ and existing ingredient name. Retain the discrepancy and narrow justification\
    \ rather than claiming identical primary wording.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q18\",\n    \"quantity\": \"Receiving stock label and dose\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\",\n        \"field_path\": \"\
    preparation_steps[0].description\",\n        \"stored\": \"After sterilization\
    \ add sterile 1 M Na-sesquicarbonate solution (1 ml in 10 ml) to achieve a pH\
    \ of 9.7 (see medium 31).\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"After sterilization add sterile 1 M Na-sesquicarbonate solution (1 ml in 10\
    \ ml) to achieve a pH of 9.7 (see medium 31).\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Post-sterilization instruction\",\n        \"\
    exact_source_quote\": \"After sterilization add sterile 1 M Na-sesquicarbonate\
    \ solution (1 ml in 10 ml) to achieve\\na pH of 9.7 (see medium 31).\",\n    \
    \    \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Target and DSMZ owner preserve\
    \ 1 M, 1 mL in 10 mL, post-sterilization addition and pH 9.7 without attached\
    \ evidence. KOMODO owner lacks the step and requires addition. The 1 M label does\
    \ not authorize multiplying both salt components or assuming a total final-volume\
    \ convention.\"\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"quantity\": \"\
    Receiving target pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.7\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.7\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 9.7\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz529\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Post-sterilization pH instruction\",\n      \
    \  \"exact_source_quote\": \"After sterilization add sterile 1 M Na-sesquicarbonate\
    \ solution (1 ml in 10 ml) to achieve\\na pH of 9.7 (see medium 31).\",\n    \
    \    \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing target pH 9.7 is\
    \ supported as a source target, not a measured experimental value; attach narrow\
    \ evidence in all three layers.\"\n  },\n  {\n    \"quantity_id\": \"q20\",\n\
    \    \"quantity\": \"Provider stock receiving volume\",\n    \"decision\": \"\
    conflict\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadive529api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/529\",\n  \
    \      \"source_locator\": \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 12,\\n                 \
    \       \\\"solution\\\": \\\"Na-sesquicarbonate solution\\\",\\n            \
    \            \\\"solution_id\\\": 1174,\\n                        \\\"amount\\\
    \": 100,\\n                        \\\"unit\\\": \\\"ml\\\",\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"d8d1519ede784cc8aba978c185bf449da604cedff5907b3203860ad3a43c4152\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Provider 100 mL dose belongs to\
    \ its declared 900+100 mL representation. Preserve separately from primary 1 mL\
    \ in 10 mL; do not choose an unproven denominator.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q21\",\n    \"quantity\": \"Unspecified numerical sterilization cycle\",\n\
    \    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/AMPHIBACILLUS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"sterilization_method\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization_method\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization_method\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz529\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium529.pdf\"\
    ,\n        \"source_locator\": \"Post-sterilization sentence\",\n        \"exact_source_quote\"\
    : \"After sterilization add sterile 1 M Na-sesquicarbonate solution\",\n     \
    \   \"snapshot_sha256\": \"4066bfe1e0e6d8ce55a9a285215384fcd59aa0dc0365b8f97aee32110ef10394\"\
    ,\n        \"parsed_text_sha256\": \"a1d94c9187ac39b62cd8c58d4b9ffb307a9dc5d89bd2d2e164566e00d21eece4\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Primary specifies sterilization\
    \ before sterile stock addition, but no temperature or duration. Provider names\
    \ Autoclave as equipment without a numerical cycle; no default is imported from\
    \ another collection.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '10 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 10/12
    primary and 10/12 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi17234
  - chebi2509
  - chebi29377
  - chebi31795
  - chebi32139
  - chebi63038
  - chebi75836
  - chebi86158
  - chebi86360
  details: 'Instance coverage on a 0–100 percent scale, denominator 12: primary 83.33%;
    secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 2 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Exact source, both owners and reciprocal relationships
  outcome: supported
  summary: DSMZ 529 and KOMODO 529 catalogue identity/link resolve. Both explicit
    normalized contributors and their reciprocal declared paths/stable IDs resolve;
    shared local ingredient signatures do not prove identical historical source bytes
    or erase owner preparation differences.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - catalog
  - catalog-header
- assessment_id: forms
  area: grounding
  topic: Supplied hydrate and carbonate spelling
  outcome: concern
  summary: Source MnSO4 x 7 H2O is mapped to CHEBI:86360, whose formula Mn.O4S and
    anhydrous synonym omit seven waters. Other explicit hydrate structures match their
    source names. Primary carbonate Na2CO2 is a printed conflict resolved narrowly
    by its cited source 31 and provider; no unverified replacement ID is proposed.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - primary
  - stock-primary
  - api
  - chebi86360
  - chebi29377
- assessment_id: preparation
  area: completeness
  topic: Post-sterilization addition and source-specific quantities
  outcome: concern
  summary: The target and DSMZ owner retain the single preparation sentence, but the
    KOMODO owner does not. All layers omit a separate stock descriptor, batch water
    basis and claim-level references/evidence. Stored 42 and 53 g/L conceal the stock
    boundary; the source/provider volume disagreement remains unresolved.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Complex solid medium and bounded biological claims
  outcome: supported
  summary: Yeast extract/Polypeptone support complex/undefined classification; explicit
    agar supports solid agar. The pH is a formulation target. Catalogue aerobic=false
    is metadata only, and neither title nor application supplies organism-specific
    growth evidence. No DOI, PMID, taxonomy or KG-match assertion is present.
  target_ids:
  - CultureMech:001660
  evidence_ids:
  - record
  - primary
  - catalog
  - catalog-header
findings:
- finding_id: f1
  issue_key: cm001660-sesquicarbonate-stock
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Separate sesquicarbonate stock strengths are flattened
  description: All three local layers place 42 g/L bicarbonate and 53 g/L carbonate
    among direct ingredients, although they describe the separate stock. Primary 1000
    mL water and 1 mL in 10 mL differ from provider 900+100 mL; no measured final
    denominator is established.
  target_ids:
  - CultureMech:001660
  field_paths:
  - ingredients[10].concentration
  - ingredients[11].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - stock-primary
  - api
  - stock-api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  issue_key: cm001660-manganese-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Manganese heptahydrate has an anhydrous ontology structure
  description: The source and preferred name require MnSO4 x 7 H2O, while CHEBI:86360
    and the copied current MIM key describe MnSO4 without hydrate waters. Matching
    canonical labels do not verify exact supplied form.
  target_ids:
  - CultureMech:001660
  field_paths:
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - chebi86360
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  issue_key: cm001660-claim-evidence-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Scoped amount evidence and owner preparation are incomplete
  description: No layer attaches evidence for its amounts, stock dose or pH; KOMODO
    additionally lacks the preparation sentence present in the DSMZ owner/target.
    A source link alone does not support the flattened stage.
  target_ids:
  - CultureMech:001660
  field_paths:
  - ingredients
  - preparation_steps
  - ph_value
  - references
  - evidence
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  issue_key: cm001660-komodo-history
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO history contains malformed and naive timestamps
  description: The KOMODO owner has malformed 2026-01-27T01:15:03.fZ and timezone-naive
    enrichment timestamps. The selected target history does not contain these specific
    events.
  target_ids:
  - CultureMech:001660
  field_paths:
  - curation_history
  evidence_ids:
  - owner-1
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  description: Preserve a separate stock with source composition and stage-specific
    dose in both maintained owners; reconcile primary/provider volume interpretations
    explicitly before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001660
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  - Stock strengths do not become direct medium concentrations; all source versions
    and unknown final-volume assumptions remain explicit.
- action_id: a2
  description: Verify the exact hydrate identity and source-supported ontology before
    changing primary and secondary links; do not guess a replacement.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001660
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  - Hydrate count and structure match the supplied material.
- action_id: a3
  description: Attach exact primary/provider evidence to the narrowest claim and retain
    the current owner-specific preparation and volume conflict; regenerate only compatible
    representations.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001660
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
  - Every amount has explicit stage/basis evidence and source-correct preparation
    survives merging.
- action_id: a4
  description: Preserve old history; append source-backed clarification or repair
    the responsible importer for future output without inventing historical UTC.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001660
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml
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
- KOMODO 529 detail returns HTTP 403. Current base formulation can be assessed from
  the exact catalogue link and primary sources 529 and 31; historical byte equivalence
  and a distinct KOMODO variant are not inferred.
- The dose phrase 1 mL in 10 mL is retained exactly; source text alone does not settle
  whether 10 mL includes the addition. Current provider 900+100 mL is a separate interpretation.
- Numerical sterilization temperature/time and the reason for the primary carbonate
  typo are not inferred. Completed review means the bounded source comparisons were
  completed, not that these scientific conflicts were resolved.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-026
- generated-medium
```
