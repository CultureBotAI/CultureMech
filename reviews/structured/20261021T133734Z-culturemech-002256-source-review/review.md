# Source and formulation review: alkaliphilus_lact_medium (CultureMech:002256)

- Review: 20261021T133734Z-culturemech-002256-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:27:11Z
- Finished UTC: 2026-10-21T13:37:34Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM 1076 identity and existing pH/gas instructions resolve, but both layers convert four later liquid additions into mass concentrations and expose a separately dosed trace stock as main ingredients. Nickel hexahydrate has an anhydrous identifier. Correct main rates need evidence for the declared provider basis; missing stock strengths, water and numeric sterilization details require source-scoped representation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 223; batch 023 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-two task batches contain 220 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 223 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002256 | data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml | generated | alkaliphilus_lact_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002256 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002256 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/223/strict.tsv |
| validate-terms | passed | True | CultureMech:002256 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002256 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002256 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002256.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002256.

38 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "NaCl main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "19.861",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "19.861",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NaCl 20.0 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "NaCl 20.0 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 19.861,\n                        \"mmol_l\": 339.852,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q2",
    "claim": "NH4Cl main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.993049",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.993049",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NH 4 Cl 1.0 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "NH 4 Cl 1.0 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.993049,\n                        \"mmol_l\": 18.5651,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q3",
    "claim": "KH2PO4 main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "KH 2 PO 4 0.1 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "KH 2 PO 4 0.1 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0993049,\n                        \"mmol_l\": 0.729721,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q4",
    "claim": "K2HPO4 main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "K 2 HPO 4 0.1 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "K 2 HPO 4 0.1 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0993049,\n                        \"mmol_l\": 0.570141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q5",
    "claim": "KCl main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "KCl 0.1 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "KCl 0.1 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0993049,\n                        \"mmol_l\": 1.33206,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q6",
    "claim": "MgCl2 x 6 H2O main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.0993049",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "MgCl 2 ·6H 2 O 0.1 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "MgCl 2 ·6H 2 O 0.1 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0993049,\n                        \"mmol_l\": 0.488457,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q7",
    "claim": "Tris base main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.97915",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.97915",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Tris base 3.0 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "Tris base 3.0 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Tris base\",\n                        \"compound_id\": 1698,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.97915,\n                        \"mmol_l\": 24.5926,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q8",
    "claim": "Na2S2O3 x 5 H2O main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.97915",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.97915",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 S 2 O 3 ·5H 2 O 3.0 g",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "Na 2 S 2 O 3 ·5H 2 O 3.0 g",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.97915,\n                        \"mmol_l\": 12.0037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q9",
    "claim": "Resazurin main amount",
    "decision": "evidence_only",
    "stage": "Main recipe, provider-declared 1007 mL table basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.000993049",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.000993049",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Resazurin 1.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main exact ingredient row",
        "exact_source_quote": "Resazurin 1.0 mg",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000993049,\n                        \"mmol_l\": 0.00433286,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The existing rate matches the provider g/L on its declared basis, but neither local layer has attached evidence. Preserve the primary batch mass and original unit, including 1 mg resazurin. Listed liquid additions sum to 1007 mL; this is not a source statement of measured final volume or an instruction to make up to that volume."
  },
  {
    "decision_id": "q10",
    "claim": "Yeast extract later liquid dose",
    "decision": "correct",
    "stage": "Post-cooling addition from a separately sterilized anaerobic stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "10 mL",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition exact row",
        "exact_source_quote": "10% (w/v) Yeast extract solution 10.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"w/v, 10%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The local G_PER_L value copies a liquid amount in mL, not a final mass concentration. Preserve stock identity, liquid dose, strength and addition stage; no density, hydrate or unspecified percentage-basis conversion is justified."
  },
  {
    "decision_id": "q11",
    "claim": "Yeast extract stock strength",
    "decision": "add",
    "stage": "Later-addition stock before dilution into the main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "10% (w/v)",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition stock qualification",
        "exact_source_quote": "10% (w/v) Yeast extract solution 10.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"w/v, 10%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The strength is absent from the local representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate and sulfide specify percent without its basis. Keep these qualifications distinct rather than treating all percentages as w/v or deriving a mass concentration."
  },
  {
    "decision_id": "q12",
    "claim": "Maltose later liquid dose",
    "decision": "correct",
    "stage": "Post-cooling addition from a separately sterilized anaerobic stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "20 mL",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition exact row",
        "exact_source_quote": "0.5 M Maltose solution 20.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Maltose\",\n                        \"compound_id\": 171,\n                        \"attribute\": \"0.5 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The local G_PER_L value copies a liquid amount in mL, not a final mass concentration. Preserve stock identity, liquid dose, strength and addition stage; no density, hydrate or unspecified percentage-basis conversion is justified."
  },
  {
    "decision_id": "q13",
    "claim": "Maltose stock strength",
    "decision": "add",
    "stage": "Later-addition stock before dilution into the main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "0.5 M",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition stock qualification",
        "exact_source_quote": "0.5 M Maltose solution 20.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Maltose\",\n                        \"compound_id\": 171,\n                        \"attribute\": \"0.5 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The strength is absent from the local representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate and sulfide specify percent without its basis. Keep these qualifications distinct rather than treating all percentages as w/v or deriving a mass concentration."
  },
  {
    "decision_id": "q14",
    "claim": "Na2CO3 later liquid dose",
    "decision": "correct",
    "stage": "Post-cooling addition from a separately sterilized anaerobic stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "20 mL",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition exact row",
        "exact_source_quote": "8% Na 2 CO 3 solution 20.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"attribute\": \"8%\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The local G_PER_L value copies a liquid amount in mL, not a final mass concentration. Preserve stock identity, liquid dose, strength and addition stage; no density, hydrate or unspecified percentage-basis conversion is justified."
  },
  {
    "decision_id": "q15",
    "claim": "Na2CO3 stock strength",
    "decision": "add",
    "stage": "Later-addition stock before dilution into the main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "8%, basis unspecified",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition stock qualification",
        "exact_source_quote": "8% Na 2 CO 3 solution 20.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"attribute\": \"8%\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The strength is absent from the local representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate and sulfide specify percent without its basis. Keep these qualifications distinct rather than treating all percentages as w/v or deriving a mass concentration."
  },
  {
    "decision_id": "q16",
    "claim": "Na2S x 9 H2O later liquid dose",
    "decision": "correct",
    "stage": "Post-cooling addition from a separately sterilized anaerobic stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "6 mL",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition exact row",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution 6.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 6,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The local G_PER_L value copies a liquid amount in mL, not a final mass concentration. Preserve stock identity, liquid dose, strength and addition stage; no density, hydrate or unspecified percentage-basis conversion is justified."
  },
  {
    "decision_id": "q17",
    "claim": "Na2S x 9 H2O stock strength",
    "decision": "add",
    "stage": "Later-addition stock before dilution into the main recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "5%, basis unspecified",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition stock qualification",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution 6.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[14]",
        "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 6,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The strength is absent from the local representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate and sulfide specify percent without its basis. Keep these qualifications distinct rather than treating all percentages as w/v or deriving a mass concentration."
  },
  {
    "decision_id": "q18",
    "claim": "HCl trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "12.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "HCl (25%) 12.5 ml",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "HCl (25%) 12.5 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 12.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. HCl is 12.5 mL of a 25% solution, not 12.5 g/L; the percentage basis is unspecified."
  },
  {
    "decision_id": "q19",
    "claim": "FeSO4 x 7 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "2.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "FeSO 4 ·7H 2 O 2.1 g",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "FeSO 4 ·7H 2 O 2.1 g",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.1,\n                        \"mmol_l\": 7.55355,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q20",
    "claim": "H3BO3 trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.03",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "H 3 BO 3 30.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "H 3 BO 3 30.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 30,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.485123,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q21",
    "claim": "MnCl2 x 4 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "MnCl 2 ·4H 2 O 100.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "MnCl 2 ·4H 2 O 100.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q22",
    "claim": "CoCl2 x 6 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "CoCl 2 ·6H 2 O 190.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "CoCl 2 ·6H 2 O 190.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q23",
    "claim": "NiCl2 x 6 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NiCl 2 ·6H 2 O 24.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "NiCl 2 ·6H 2 O 24.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q24",
    "claim": "CuCl2 x 2 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "CuCl 2 ·2H 2 O 2.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "CuCl 2 ·2H 2 O 2.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q25",
    "claim": "ZnSO4 x 7 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.144",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.144",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "ZnSO 4 ·7H 2 O 144.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 144.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 144,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.144,\n                        \"mmol_l\": 0.500763,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q26",
    "claim": "Na2MoO4 x 2 H2O trace-stock input",
    "decision": "correct",
    "stage": "JCM439 trace stock only; receiving JCM1076 dose 1 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution exact ingredient row",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "This is a separately prepared stock input, not a direct main-medium amount. Preserve source mg/g units and supplied hydrates. The current stock-rate number must not be used undiluted as a main-medium concentration."
  },
  {
    "decision_id": "q27",
    "claim": "Trace hydrochloric acid strength",
    "decision": "add",
    "stage": "HCl reagent used to prepare the trace stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "25%, basis unspecified",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 Trace element solution acid row",
        "exact_source_quote": "HCl (25%) 12.5 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 12.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "Retain the source solution qualification independently of the hydrogen chloride molecule identifier. No concentration basis, density or pure-compound mass is inferred."
  },
  {
    "decision_id": "q28",
    "claim": "Main water input",
    "decision": "add",
    "stage": "Main recipe before later stock additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "19.861",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "0.993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "Tris base",
            "term": {
              "id": "CHEBI:9754",
              "label": "tris"
            },
            "concentration": {
              "value": "2.97915",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:9754",
              "label": "tris"
            }
          },
          {
            "preferred_term": "Na2S2O3 x 5 H2O",
            "term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "concentration": {
              "value": "2.97915",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            }
          },
          {
            "preferred_term": "Resazurin",
            "term": {
              "id": "CHEBI:8806",
              "label": "Resazurin"
            },
            "concentration": {
              "value": "0.000993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:8806",
              "label": "Resazurin"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Maltose",
            "term": {
              "id": "CHEBI:17306",
              "label": "maltose"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17306",
              "label": "maltose"
            }
          },
          {
            "preferred_term": "Na2CO3",
            "term": {
              "id": "CHEBI:29377",
              "label": "sodium carbonate"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:29377",
              "label": "sodium carbonate"
            }
          },
          {
            "preferred_term": "Na2S x 9 H2O",
            "term": {
              "id": "CHEBI:76209",
              "label": "sodium sulfide nonahydrate"
            },
            "concentration": {
              "value": "6",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:76209",
              "label": "sodium sulfide nonahydrate"
            }
          },
          {
            "preferred_term": "HCl",
            "term": {
              "id": "CHEBI:17883",
              "label": "hydrogen chloride"
            },
            "concentration": {
              "value": "12.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17883",
              "label": "hydrogen chloride"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "2.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.03",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "MnCl2 x 4 H2O",
            "term": {
              "id": "CHEBI:86368",
              "label": "manganese(II) chloride tetrahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86368",
              "label": "manganese(II) chloride tetrahydrate"
            }
          },
          {
            "preferred_term": "CoCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            },
            "concentration": {
              "value": "0.19",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.024",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "CuCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86318",
              "label": "copper(II) chloride dihydrate"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86318",
              "label": "copper(II) chloride dihydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.144",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.036",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "NaCl",
            "term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            },
            "concentration": {
              "value": "19.861",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:26710",
              "label": "sodium chloride"
            }
          },
          {
            "preferred_term": "NH4Cl",
            "term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            },
            "concentration": {
              "value": "0.993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31206",
              "label": "ammonium chloride"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            }
          },
          {
            "preferred_term": "KCl",
            "term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32588",
              "label": "potassium chloride"
            }
          },
          {
            "preferred_term": "MgCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            },
            "concentration": {
              "value": "0.0993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86345",
              "label": "magnesium dichloride hexahydrate"
            }
          },
          {
            "preferred_term": "Tris base",
            "term": {
              "id": "CHEBI:9754",
              "label": "tris"
            },
            "concentration": {
              "value": "2.97915",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:9754",
              "label": "tris"
            }
          },
          {
            "preferred_term": "Na2S2O3 x 5 H2O",
            "term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            },
            "concentration": {
              "value": "2.97915",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32150",
              "label": "sodium thiosulfate pentahydrate"
            }
          },
          {
            "preferred_term": "Resazurin",
            "term": {
              "id": "CHEBI:8806",
              "label": "Resazurin"
            },
            "concentration": {
              "value": "0.000993049",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:8806",
              "label": "Resazurin"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "10",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Maltose",
            "term": {
              "id": "CHEBI:17306",
              "label": "maltose"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17306",
              "label": "maltose"
            }
          },
          {
            "preferred_term": "Na2CO3",
            "term": {
              "id": "CHEBI:29377",
              "label": "sodium carbonate"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:29377",
              "label": "sodium carbonate"
            }
          },
          {
            "preferred_term": "Na2S x 9 H2O",
            "term": {
              "id": "CHEBI:76209",
              "label": "sodium sulfide nonahydrate"
            },
            "concentration": {
              "value": "6",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:76209",
              "label": "sodium sulfide nonahydrate"
            }
          },
          {
            "preferred_term": "HCl",
            "term": {
              "id": "CHEBI:17883",
              "label": "hydrogen chloride"
            },
            "concentration": {
              "value": "12.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17883",
              "label": "hydrogen chloride"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "2.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "H3BO3",
            "term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            },
            "concentration": {
              "value": "0.03",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:33118",
              "label": "boric acid"
            }
          },
          {
            "preferred_term": "MnCl2 x 4 H2O",
            "term": {
              "id": "CHEBI:86368",
              "label": "manganese(II) chloride tetrahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86368",
              "label": "manganese(II) chloride tetrahydrate"
            }
          },
          {
            "preferred_term": "CoCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            },
            "concentration": {
              "value": "0.19",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:53503",
              "label": "cobalt chloride hexahydrate"
            }
          },
          {
            "preferred_term": "NiCl2 x 6 H2O",
            "term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            },
            "concentration": {
              "value": "0.024",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:34887",
              "label": "nickel dichloride"
            }
          },
          {
            "preferred_term": "CuCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86318",
              "label": "copper(II) chloride dihydrate"
            },
            "concentration": {
              "value": "0.002",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86318",
              "label": "copper(II) chloride dihydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.144",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:32312",
              "label": "zinc sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.036",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          }
        ]
      }
    ],
    "source_amount": "950 mL",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main water row",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "Water is absent from both local recipes. Preserve the main input rather than summing it with the water used to prepare a separate trace-stock batch."
  },
  {
    "decision_id": "q29",
    "claim": "Trace-stock addition",
    "decision": "add",
    "stage": "Main recipe assembly",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "1 mL",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 trace-stock reference and dose",
        "exact_source_quote": "Trace element solution (see Medium No. 439 ) 1.0 ml",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 4186,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The exact stock addition and reference are missing. Transfer only the named trace subsection, not the whole JCM439 medium or its other stocks."
  },
  {
    "decision_id": "q30",
    "claim": "Trace-stock water input",
    "decision": "add",
    "stage": "JCM439 Trace element solution batch",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "987 mL",
    "source_snippets": [
      {
        "source_key": "jcm439",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439",
        "source_locator": "JCM439 terminal trace-stock water row",
        "exact_source_quote": "Distilled water 987.0 ml",
        "snapshot_sha256": "2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda",
        "parsed_text_sha256": "d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b"
      },
      {
        "source_key": "mediadiveJ1076api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J1076",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 987,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5"
      }
    ],
    "explanation": "The provider declares a 1000 mL stock basis, while the listed liquid inputs are 987 mL water and 12.5 mL acid. Their arithmetic sum is 999.5 mL, not a measured final volume; the source does not instruct a make-up volume. Keep the 987 mL input unchanged and record the denominator distinction."
  },
  {
    "decision_id": "q31",
    "claim": "Initial main pH",
    "decision": "evidence_only",
    "stage": "Before main autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      }
    ],
    "source_amount": "9.0",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main preparation before autoclaving",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "The existing preparation already retains this pH stage and NaOH identity. Add claim evidence without replacing the later pH target."
  },
  {
    "decision_id": "q32",
    "claim": "Final pH check",
    "decision": "evidence_only",
    "stage": "After the later stock additions",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 8.2
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "ph_value",
        "stored": 8.2
      },
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "MIX",
          "description": "Check final pH be around 8.2."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps[1]",
        "stored": {
          "step_number": 2,
          "action": "MIX",
          "description": "Check final pH be around 8.2."
        }
      }
    ],
    "source_amount": "around 8.2",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 last preparation sentence",
        "exact_source_quote": "Check final pH be around 8.2.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "Both local layers already retain the target value and final-check instruction. This does not assert an experimentally measured result or a growth optimum."
  },
  {
    "decision_id": "q33",
    "claim": "Post-cooling gas ratio",
    "decision": "evidence_only",
    "stage": "Gas-phase replacement before later stocks",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      }
    ],
    "source_amount": "N2:CO2 4:1, v/v",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 post-cooling gas sentence",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "The existing preparation includes the exact ratio and basis; retain its timing. Do not apply the mixed gas to stocks that are separately autoclaved and stored under N2."
  },
  {
    "decision_id": "q34",
    "claim": "Autoclave temperature",
    "decision": "add",
    "stage": "JCM1076 displayed default for the stated autoclaving steps",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "Check final pH be around 8.2."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "Check final pH be around 8.2."
          }
        ]
      }
    ],
    "source_amount": "121°C",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 displayed default above the exact recipe",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "The source page itself displays this default and the recipe does not override it. Existing instructions name autoclaving but omit the numerical default; retain the main and later-stock stages without transferring unrelated parent-medium procedures."
  },
  {
    "decision_id": "q35",
    "claim": "Autoclave duration",
    "decision": "add",
    "stage": "JCM1076 displayed default for the stated autoclaving steps",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "Check final pH be around 8.2."
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
          },
          {
            "step_number": 2,
            "action": "MIX",
            "description": "Check final pH be around 8.2."
          }
        ]
      }
    ],
    "source_amount": "15 min",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 displayed default above the exact recipe",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "The source page itself displays this default and the recipe does not override it. Existing instructions name autoclaving but omit the numerical default; retain the main and later-stock stages without transferring unrelated parent-medium procedures."
  },
  {
    "decision_id": "q36",
    "claim": "NaOH dose and strength",
    "decision": "not_quantified",
    "stage": "Initial main pH adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      }
    ],
    "source_amount": "No fixed dose or strength",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main pH-adjustment sentence",
        "exact_source_quote": "adjust pH to 9.0 with NaOH",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "The existing instruction names NaOH but the source does not quantify it. Do not supply a typical strength or treat the unstated amount as zero."
  },
  {
    "decision_id": "q37",
    "claim": "Nitrogen atmosphere purity",
    "decision": "not_quantified",
    "stage": "Main autoclaving and separate stock preparation/storage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      }
    ],
    "source_amount": "N2 atmosphere; numeric purity not stated",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 main autoclaving sentence",
        "exact_source_quote": "autoclave under a N 2 atmosphere.",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-stock handling parenthesis",
        "exact_source_quote": "autoclaved and stored under a N 2 atmosphere",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "Both stages are retained in existing preparation. Do not rewrite the source as an explicit 100% purity claim or confuse it with the later 4:1 gas mixture."
  },
  {
    "decision_id": "q38",
    "claim": "Cooling endpoint and stock preparation volumes",
    "decision": "not_quantified",
    "stage": "Post-autoclave transition and separately prepared later stocks",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "preparation_steps[0]",
        "stored": {
          "step_number": 1,
          "action": "AUTOCLAVE",
          "description": "Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):"
        }
      },
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_amount": "No numerical cooling endpoint or stock-batch volumes",
    "source_snippets": [
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 preparation transition",
        "exact_source_quote": "After cooling, replace the gas phase",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      },
      {
        "source_key": "jcm1076",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076",
        "source_locator": "JCM1076 later-addition introduction",
        "exact_source_quote": "Add the following solutions from sterile anaerobic stocks",
        "snapshot_sha256": "cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2",
        "parsed_text_sha256": "06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9"
      }
    ],
    "explanation": "The exact source gives receiving doses and stock strengths, but not a cooling temperature or stock preparation batch volumes. Preserve these unknowns without importing another medium procedure."
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:002256.

21 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 21/22 primary and 21/22 secondary instances; all asserted CHEBI-keyed secondary IDs have exact pinned MIM rows; no legacy MIM identifier is asserted in the target or maintained owner. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 22: primary 95.45%; secondary 95.45%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002256.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact medium and trace-subsection identity

identity: supported. Targets: CultureMech:002256.

CM002256 and its sole maintained owner resolve to JCM1076 and provider main solution 5141. The source names the JCM439 trace stock and provider solution 4186. Only that subsection transfers; unrelated JCM439 basal, vitamin, lactate and selenite/tungstate content is excluded.

### Retained instructions and missing later-stock details

completeness: concern. Targets: CultureMech:002256.

The two existing preparation steps retain initial pH 9, N2 autoclaving, post-cooling 4:1 gas replacement, stock handling and final pH around 8.2. However, the first step ends with a colon and the four stock identities, strengths and liquid doses are absent as such; numeric sterilization defaults and water are also missing.

### Hydrates and unspecified solution qualifications

grounding: concern. Targets: CultureMech:002256.

The source-specific Mg, thiosulfate, Fe, Mn, Co, Cu, Zn, Mo and sulfide hydrate forms agree with their asserted structures. Cobalt CHEBI:53503 explicitly encodes six waters; its unrelated synonym text is not a reason to reject the correct structure. Nickel CHEBI:34887 lacks the six source waters. Maltose molarity does not authorize assuming a hydrate or mass, and hydrogen chloride identity does not encode the 25% stock solution.

### Recipe class and biological claims

scope: supported. Targets: CultureMech:002256.

Yeast extract supports complex and undefined classifications; liquid is consistent with no gelling ingredient. Generic bacterial filing and cultivation application do not assert a named strain or growth experiment. No growth assertion is inferred from the medium title or parent-stock source.

### Maintained source and generated target

ownership: supported. Targets: CultureMech:002256.

Both layers contain the same 22 concentrations and two preparation steps. Curate the normalized owner and demonstrated conversion issue first, then regenerate separately; preserve existing history rather than rewriting it to claim source verification.

## Findings

### f1: Liquid stock additions and trace inputs are flattened into main concentrations

blocker / open / confirmed; issue key: cm002256-stock-representation.

Four later doses of 10, 20, 20 and 6 mL become G_PER_L values, and nine trace-stock inputs are exposed without the 1 mL receiving dose. The HCl stock input is likewise 12.5 mL, not 12.5 g/L. Missing stage and strength metadata materially change the recipe.

### f2: Nickel hexahydrate is grounded to anhydrous nickel dichloride

major / open / confirmed; issue key: cm002256-nickel-hydrate.

The trace source and local preferred term specify NiCl2·6H2O, but both primary and secondary CHEBI:34887 assertions encode nickel dichloride without those six waters. Label correctness does not establish supplied-form correspondence.

### f3: The preparation omits the list introduced by its final colon and numeric defaults

major / open / confirmed; issue key: cm002256-preparation-completeness.

The existing main method preserves the gas and pH sequence but has no corresponding four-stock list or structured stock equivalents. It also omits the displayed 121°C/15 min default and main/trace water inputs. Existing pH values and gas ratio are supported and should remain.

### f4: Supported main rates and existing pH/gas instructions lack claim evidence

minor / open / confirmed; issue key: cm002256-claim-evidence.

The unchanged main rates match the provider-declared 1007 mL basis, and existing pH/gas instructions match the primary, but neither layer attaches evidence to these claims. A record-level source link alone does not distinguish main and stock bases.

## Recommended Actions And Acceptance Checks

### a1

Restore source-scoped stocks, original liquid units, strengths and receiving doses; preserve original trace masses and water. Keep unspecified percent bases unresolved and do not infer final concentrations from flattened values.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Resolve a source-specific supplied-form identifier or explicitly retain unresolved grounding; do not change the source stock mass or infer a replacement secondary mapping.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Complete the missing stock list and scoped water/default details using exact source evidence, retaining the existing timing and distinct atmospheres. Do not invent cooling endpoints, NaOH strength or stock-batch volumes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach exact original quantities, provider basis and stage-specific snippets to the corrected and unchanged claims. Keep the provider basis distinct from measured final volume and preserve source percentage qualifications.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch023/223/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/223/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml:1:id: CultureMech:002256<br>./data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml:1:id: CultureMech:002256<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/223/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 25 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/223/evidence-context-original.json; Complete frozen source context compared with fresh native input hashes | context_only | Every contextual input hash matches the fresh inspection at the same base. Preflight remains provisional provenance; this review supplies its own single-target judgment. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076; Complete main table, later-addition list, preparation and displayed sterilization default | supports | Source masses, 950 mL water, 1 mL trace stock and four later liquid doses remain distinct. Only yeast stock explicitly states w/v; other percentage bases remain unspecified. |
| provider | https://mediadive.dsmz.de/rest/medium/J1076; data.medium; complete main solution 5141 and trace solution 4186 | supports | Main provider basis is 1007 mL; trace basis is 1000 mL. Liquid stock doses have no g_l. Provider normalization does not establish a measured final volume. |
| trace-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439; Only Trace element solution subsection at end of page | supports | Transfers the nine trace inputs and 987 mL water only. Parent basal ingredients, lactate, vitamins, selenite/tungstate and conditions are outside JCM1076 transfer. |
| trace-api | https://mediadive.dsmz.de/rest/solution/4186; Complete exact solution 4186 endpoint | supports | Separate stock identity, original units and declared volume corroborate the linked trace recipe; molecular weights and provider mmol values are not substituted for source forms. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch023/223/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17306 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17306; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17306 resolves to maltose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi9754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:9754 resolves to tris. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17306": [{"label": "Maltose", "match_type": "preferred_term", "identifier": "CHEBI:17306", "preferred_term": "Maltose", "ontology_id": "CHEBI:17306", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754": [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754", "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml; data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current parser and formulation/cleanup code are context only. Present source solutions retain separate recipes, liquid amounts and attributes; historical import/enrichment notes do not prove that the current implementation produced these flattened values. No script is rerun. |
| writer-1 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current parser and formulation/cleanup code are context only. Present source solutions retain separate recipes, liquid amounts and attributes; historical import/enrichment notes do not prove that the current implementation produced these flattened values. No script is rerun. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current parser and formulation/cleanup code are context only. Present source solutions retain separate recipes, liquid amounts and attributes; historical import/enrichment notes do not prove that the current implementation produced these flattened values. No script is rerun. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact primary and provider sources needed for this bounded review are available. Unspecified percentage bases, NaOH dose/strength, cooling endpoint, stock preparation volumes and measured final volumes remain unknown; the provider 1000 mL trace basis is retained separately from 999.5 mL listed liquid inputs. Parent JCM439 content outside its named trace subsection supplies no cultivation or formulation evidence for this record.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133734Z-culturemech-002256-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilus_lact_medium (CultureMech:002256)'
started_at: '2026-10-21T13:27:11Z'
finished_at: '2026-10-21T13:37:34Z'
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
summary: The exact JCM 1076 identity and existing pH/gas instructions resolve, but
  both layers convert four later liquid additions into mass concentrations and expose
  a separately dosed trace stock as main ingredients. Nickel hexahydrate has an anhydrous
  identifier. Correct main rates need evidence for the declared provider basis; missing
  stock strengths, water and numeric sterilization details require source-scoped representation.
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
  - path: data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
    sha256: d76dc27dbe7b66f4fee6ab4c6be087bca1861d5af9fe87ca0005819e5d2bb284
    role: target
  - path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
    sha256: 53c22ad74ed1c77ad648c5a11ac3881df566ab7554de88463cd6592462b934d2
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
  selection: Task review 223; batch 023 item 3 of 10, selected in Python lexicographic
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
  - CultureMech:002256
targets:
- target_id: CultureMech:002256
  path: data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  label: alkaliphilus_lact_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/223/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/223/strict.tsv"
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002256
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
  - CultureMech:002256
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:36.579139Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/223/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:38.173948Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/223/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:39.980439Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:41.240329Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml:1:id: CultureMech:002256

    ./data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml:1:id: CultureMech:002256

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/223/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: 25 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 0c213cc1e9ae36db04a149cba88779e7684e8c9a7ba362905f09172d81d07d30
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/223/evidence-context-original.json
  locator: Complete frozen source context compared with fresh native input hashes
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Every contextual input hash matches the fresh inspection at the same base.
    Preflight remains provisional provenance; this review supplies its own single-target
    judgment.
  snapshot_sha256: 221bd064baf7f7bfe5cf2c49f835c997a814162c442f861f7d6e451a52465d1b
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076
  locator: Complete main table, later-addition list, preparation and displayed sterilization
    default
  accessed_at: '2026-10-21T13:13:22.044257Z'
  support: supports
  summary: Source masses, 950 mL water, 1 mL trace stock and four later liquid doses
    remain distinct. Only yeast stock explicitly states w/v; other percentage bases
    remain unspecified.
  snapshot_sha256: cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1076
  locator: data.medium; complete main solution 5141 and trace solution 4186
  accessed_at: '2026-10-21T13:13:18.386812Z'
  support: supports
  summary: Main provider basis is 1007 mL; trace basis is 1000 mL. Liquid stock doses
    have no g_l. Provider normalization does not establish a measured final volume.
  snapshot_sha256: 53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5
- evidence_id: trace-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439
  locator: Only Trace element solution subsection at end of page
  accessed_at: '2026-10-21T13:13:22.895121Z'
  support: supports
  summary: Transfers the nine trace inputs and 987 mL water only. Parent basal ingredients,
    lactate, vitamins, selenite/tungstate and conditions are outside JCM1076 transfer.
  snapshot_sha256: 2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda
- evidence_id: trace-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4186
  locator: Complete exact solution 4186 endpoint
  accessed_at: '2026-10-21T13:16:27.281710Z'
  support: supports
  summary: Separate stock identity, original units and declared volume corroborate
    the linked trace recipe; molecular weights and provider mmol values are not substituted
    for source forms.
  snapshot_sha256: 104475acbfd9e199735303c55a1b511736ad3e5675d752d771afb58d0fa151c0
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/223/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: bf80df3420326d99774e8a96a91e3d482053f727206af337c3592b2559fa367a
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
- evidence_id: chebi17306
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17306
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:13:21.553511Z'
  support: supports
  summary: CHEBI:17306 resolves to maltose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 3ce67048c1fb5137f13f7effdd8dcb3dee6224ee3886441aa45c873652c0ca66
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
- evidence_id: chebi32150
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:01:47.429763Z'
  support: supports
  summary: CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 910d65eb9be29c9371cb79a32bcbe81bdb57d8143d21fbf7c4a1a915b5a79999
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
- evidence_id: chebi9754
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_9754
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:13.713319Z'
  support: supports
  summary: CHEBI:9754 resolves to tris. Identifier existence and label metadata do
    not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b9f921dfa34f343d4ef51ee217fc47702a8f03e2b9a8353effa10de89e9c6659
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17306": [{"label": "Maltose", "match_type": "preferred_term",
    "identifier": "CHEBI:17306", "preferred_term": "Maltose", "ontology_id": "CHEBI:17306",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17883": [{"label":
    "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term":
    "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label":
    "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32150": [{"label": "Na2S2O3 x 5 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5
    H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
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
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318":
    [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318",
    "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type":
    "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id":
    "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:9754":
    [{"label": "Tris base", "match_type": "preferred_term", "identifier": "CHEBI:9754",
    "preferred_term": "Tris base", "ontology_id": "CHEBI:9754", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml; data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Current parser and formulation/cleanup code are context only. Present source
    solutions retain separate recipes, liquid amounts and attributes; historical import/enrichment
    notes do not prove that the current implementation produced these flattened values.
    No script is rerun.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Current parser and formulation/cleanup code are context only. Present source
    solutions retain separate recipes, liquid amounts and attributes; historical import/enrichment
    notes do not prove that the current implementation produced these flattened values.
    No script is rerun.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Current parser and formulation/cleanup code are context only. Present source
    solutions retain separate recipes, liquid amounts and attributes; historical import/enrichment
    notes do not prove that the current implementation produced these flattened values.
    No script is rerun.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 38 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"NaCl main amount\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Main recipe, provider-declared\
    \ 1007 mL table basis\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"19.861\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"19.861\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"NaCl 20.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 main exact ingredient row\",\n        \"exact_source_quote\": \"NaCl\
    \ 20.0 g\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 20,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 19.861,\\n             \
    \           \\\"mmol_l\\\": 339.852,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The existing rate matches the provider\
    \ g/L on its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q2\",\n    \"claim\": \"NH4Cl main amount\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Main recipe, provider-declared 1007 mL table basis\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.993049\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.993049\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_amount\": \"NH 4 Cl 1.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 main exact ingredient row\",\n        \"exact_source_quote\": \"NH\
    \ 4 Cl 1.0 g\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.993049,\\n           \
    \             \\\"mmol_l\\\": 18.5651,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The existing rate matches the provider\
    \ g/L on its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"claim\": \"KH2PO4 main amount\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Main recipe, provider-declared 1007 mL table basis\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"KH 2 PO 4 0.1 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n \
    \       \"source_locator\": \"JCM1076 main exact ingredient row\",\n        \"\
    exact_source_quote\": \"KH 2 PO 4 0.1 g\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0993049,\\n          \
    \              \\\"mmol_l\\\": 0.729721,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The existing rate matches the provider\
    \ g/L on its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q4\",\n    \"claim\": \"K2HPO4 main amount\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Main recipe, provider-declared 1007 mL table basis\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"K 2 HPO 4 0.1 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n \
    \       \"source_locator\": \"JCM1076 main exact ingredient row\",\n        \"\
    exact_source_quote\": \"K 2 HPO 4 0.1 g\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0993049,\\n          \
    \              \\\"mmol_l\\\": 0.570141,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The existing rate matches the provider\
    \ g/L on its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"claim\": \"KCl main amount\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Main recipe, provider-declared 1007 mL table basis\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"KCl 0.1 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 main exact ingredient row\",\n        \"exact_source_quote\": \"KCl\
    \ 0.1 g\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"KCl\\\",\\n                        \\\"compound_id\\\": 61,\\\
    n                        \\\"amount\\\": 0.1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0993049,\\n          \
    \              \\\"mmol_l\\\": 1.33206,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The existing rate matches the provider\
    \ g/L on its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"claim\": \"MgCl2 x 6 H2O main amount\",\n    \"decision\": \"\
    evidence_only\",\n    \"stage\": \"Main recipe, provider-declared 1007 mL table\
    \ basis\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0993049\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"MgCl 2 ·6H 2 O 0.1 g\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 main exact ingredient row\",\n      \
    \  \"exact_source_quote\": \"MgCl 2 ·6H 2 O 0.1 g\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.0993049,\\\
    n                        \\\"mmol_l\\\": 0.488457,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing rate matches the provider g/L on\
    \ its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"claim\": \"Tris base main amount\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Main recipe, provider-declared 1007 mL table basis\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.97915\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.97915\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_amount\": \"Tris base 3.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 main exact ingredient row\",\n        \"exact_source_quote\": \"Tris\
    \ base 3.0 g\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Tris base\\\",\\n                        \\\"compound_id\\\"\
    : 1698,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.97915,\\\
    n                        \\\"mmol_l\\\": 24.5926,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing rate matches the provider g/L on\
    \ its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"claim\": \"Na2S2O3 x 5 H2O main amount\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"stage\": \"Main recipe, provider-declared 1007 mL\
    \ table basis\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.97915\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.97915\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_amount\": \"Na 2 S 2 O 3 ·5H 2 O 3.0 g\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 main exact ingredient row\",\n      \
    \  \"exact_source_quote\": \"Na 2 S 2 O 3 ·5H 2 O 3.0 g\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2S2O3 x 5 H2O\\\",\\n                        \\\"compound_id\\\
    \": 65,\\n                        \\\"amount\\\": 3,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.97915,\\\
    n                        \\\"mmol_l\\\": 12.0037,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"The existing rate matches the provider g/L on\
    \ its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"claim\": \"Resazurin main amount\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Main recipe, provider-declared 1007 mL table basis\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000993049\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000993049\",\n          \"unit\": \"G_PER_L\"\n\
    \        }\n      }\n    ],\n    \"source_amount\": \"Resazurin 1.0 mg\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 main exact ingredient row\",\n      \
    \  \"exact_source_quote\": \"Resazurin 1.0 mg\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Resazurin\\\",\\n                        \\\"compound_id\\\
    \": 25,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.000993049,\\\
    n                        \\\"mmol_l\\\": 0.00433286,\\n                      \
    \  \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n     \
    \ }\n    ],\n    \"explanation\": \"The existing rate matches the provider g/L\
    \ on its declared basis, but neither local layer has attached evidence. Preserve\
    \ the primary batch mass and original unit, including 1 mg resazurin. Listed liquid\
    \ additions sum to 1007 mL; this is not a source statement of measured final volume\
    \ or an instruction to make up to that volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"claim\": \"Yeast extract later liquid dose\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Post-cooling addition from a separately sterilized\
    \ anaerobic stock\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"10 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-addition exact row\",\n        \"exact_source_quote\": \"10%\
    \ (w/v) Yeast extract solution 10.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"w/v, 10%\\\",\\n    \
    \                    \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n               \
    \     }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The local G_PER_L value copies a liquid\
    \ amount in mL, not a final mass concentration. Preserve stock identity, liquid\
    \ dose, strength and addition stage; no density, hydrate or unspecified percentage-basis\
    \ conversion is justified.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"\
    claim\": \"Yeast extract stock strength\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"Later-addition stock before dilution into the main recipe\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"10% (w/v)\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 later-addition stock qualification\"\
    ,\n        \"exact_source_quote\": \"10% (w/v) Yeast extract solution 10.0 ml\"\
    ,\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"w/v, 10%\\\",\\n    \
    \                    \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"ml\\\",\\n                        \\\"optional\\\": 0\\n               \
    \     }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The strength is absent from the local\
    \ representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate\
    \ and sulfide specify percent without its basis. Keep these qualifications distinct\
    \ rather than treating all percentages as w/v or deriving a mass concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"claim\": \"Maltose later liquid\
    \ dose\",\n    \"decision\": \"correct\",\n    \"stage\": \"Post-cooling addition\
    \ from a separately sterilized anaerobic stock\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"20 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-addition exact row\",\n        \"exact_source_quote\": \"0.5\
    \ M Maltose solution 20.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Maltose\\\",\\n                        \\\"compound_id\\\"\
    : 171,\\n                        \\\"attribute\\\": \\\"0.5 M\\\",\\n        \
    \                \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\
    \"ml\\\",\\n                        \\\"optional\\\": 0\\n                   \
    \ }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The local G_PER_L value copies a liquid\
    \ amount in mL, not a final mass concentration. Preserve stock identity, liquid\
    \ dose, strength and addition stage; no density, hydrate or unspecified percentage-basis\
    \ conversion is justified.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"\
    claim\": \"Maltose stock strength\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Later-addition stock before dilution into the main recipe\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"0.5 M\",\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 later-addition stock qualification\"\
    ,\n        \"exact_source_quote\": \"0.5 M Maltose solution 20.0 ml\",\n     \
    \   \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Maltose\\\",\\n                        \\\"compound_id\\\"\
    : 171,\\n                        \\\"attribute\\\": \\\"0.5 M\\\",\\n        \
    \                \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\
    \"ml\\\",\\n                        \\\"optional\\\": 0\\n                   \
    \ }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The strength is absent from the local\
    \ representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate\
    \ and sulfide specify percent without its basis. Keep these qualifications distinct\
    \ rather than treating all percentages as w/v or deriving a mass concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"claim\": \"Na2CO3 later liquid\
    \ dose\",\n    \"decision\": \"correct\",\n    \"stage\": \"Post-cooling addition\
    \ from a separately sterilized anaerobic stock\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"20 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-addition exact row\",\n        \"exact_source_quote\": \"8%\
    \ Na 2 CO 3 solution 20.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\"\
    : 32,\\n                        \\\"attribute\\\": \\\"8%\\\",\\n            \
    \            \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The local G_PER_L value copies a liquid\
    \ amount in mL, not a final mass concentration. Preserve stock identity, liquid\
    \ dose, strength and addition stage; no density, hydrate or unspecified percentage-basis\
    \ conversion is justified.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"\
    claim\": \"Na2CO3 stock strength\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Later-addition stock before dilution into the main recipe\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"8%, basis unspecified\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-addition stock qualification\",\n        \"exact_source_quote\"\
    : \"8% Na 2 CO 3 solution 20.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\"\
    : 32,\\n                        \\\"attribute\\\": \\\"8%\\\",\\n            \
    \            \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The strength is absent from the local\
    \ representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate\
    \ and sulfide specify percent without its basis. Keep these qualifications distinct\
    \ rather than treating all percentages as w/v or deriving a mass concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q16\",\n    \"claim\": \"Na2S x 9 H2O later\
    \ liquid dose\",\n    \"decision\": \"correct\",\n    \"stage\": \"Post-cooling\
    \ addition from a separately sterilized anaerobic stock\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"6 mL\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 later-addition exact row\",\n       \
    \ \"exact_source_quote\": \"5% Na 2 S·9H 2 O solution 6.0 ml\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"attribute\\\": \\\"5%\\\",\\n          \
    \              \\\"amount\\\": 6,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The local G_PER_L value copies a liquid\
    \ amount in mL, not a final mass concentration. Preserve stock identity, liquid\
    \ dose, strength and addition stage; no density, hydrate or unspecified percentage-basis\
    \ conversion is justified.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"\
    claim\": \"Na2S x 9 H2O stock strength\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"Later-addition stock before dilution into the main recipe\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"5%, basis unspecified\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-addition stock qualification\",\n        \"exact_source_quote\"\
    : \"5% Na 2 S·9H 2 O solution 6.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[14]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 15,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"attribute\\\": \\\"5%\\\",\\n          \
    \              \\\"amount\\\": 6,\\n                        \\\"unit\\\": \\\"\
    ml\\\",\\n                        \\\"optional\\\": 0\\n                    }\"\
    ,\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The strength is absent from the local\
    \ representation. Yeast explicitly uses w/v and maltose uses molarity; carbonate\
    \ and sulfide specify percent without its basis. Keep these qualifications distinct\
    \ rather than treating all percentages as w/v or deriving a mass concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q18\",\n    \"claim\": \"HCl trace-stock input\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM439 trace stock only; receiving\
    \ JCM1076 dose 1 mL\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"12.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.5\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"HCl (25%) 12.5 ml\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm439\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\",\n        \"source_locator\"\
    : \"JCM439 Trace element solution exact ingredient row\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 12.5 ml\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 12.5,\\n                        \\\"unit\\\": \\\"ml\\\"\
    ,\\n                        \\\"optional\\\": 0\\n                    }\",\n \
    \       \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"This is a separately prepared stock\
    \ input, not a direct main-medium amount. Preserve source mg/g units and supplied\
    \ hydrates. HCl is 12.5 mL of a 25% solution, not 12.5 g/L; the percentage basis\
    \ is unspecified.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"claim\":\
    \ \"FeSO4 x 7 H2O trace-stock input\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"JCM439 trace stock only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"FeSO 4 ·7H 2 O 2.1 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm439\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\",\n        \"source_locator\"\
    : \"JCM439 Trace element solution exact ingredient row\",\n        \"exact_source_quote\"\
    : \"FeSO 4 ·7H 2 O 2.1 g\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 12,\\n                        \\\"amount\\\": 2.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.1,\\n \
    \                       \\\"mmol_l\\\": 7.55355,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"This is a separately prepared stock\
    \ input, not a direct main-medium amount. Preserve source mg/g units and supplied\
    \ hydrates. The current stock-rate number must not be used undiluted as a main-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"claim\": \"\
    H3BO3 trace-stock input\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    JCM439 trace stock only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.03\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"H 3 BO 3 30.0 mg\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm439\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\",\n        \"source_locator\"\
    : \"JCM439 Trace element solution exact ingredient row\",\n        \"exact_source_quote\"\
    : \"H 3 BO 3 30.0 mg\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"H3BO3\\\",\\n                        \\\"compound_id\\\": 37,\\\
    n                        \\\"amount\\\": 30,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.03,\\n              \
    \          \\\"mmol_l\\\": 0.485123,\\n                        \\\"optional\\\"\
    : 0\\n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"This is a separately prepared stock\
    \ input, not a direct main-medium amount. Preserve source mg/g units and supplied\
    \ hydrates. The current stock-rate number must not be used undiluted as a main-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"claim\": \"\
    MnCl2 x 4 H2O trace-stock input\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"JCM439 trace stock only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"MnCl 2 ·4H 2 O 100.0 mg\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm439\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\",\n  \
    \      \"source_locator\": \"JCM439 Trace element solution exact ingredient row\"\
    ,\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 100.0 mg\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"MnCl2 x 4 H2O\\\",\\n                        \\\"compound_id\\\
    \": 36,\\n                        \\\"amount\\\": 100,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.1,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"This is a separately prepared stock\
    \ input, not a direct main-medium amount. Preserve source mg/g units and supplied\
    \ hydrates. The current stock-rate number must not be used undiluted as a main-medium\
    \ concentration.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"claim\": \"\
    CoCl2 x 6 H2O trace-stock input\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"JCM439 trace stock only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"CoCl 2 ·6H 2 O 190.0 mg\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 Trace element solution exact ingredient\
    \ row\",\n        \"exact_source_quote\": \"CoCl 2 ·6H 2 O 190.0 mg\",\n     \
    \   \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 190,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.19,\\\
    n                        \\\"mmol_l\\\": 1.46335,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"This is a separately prepared stock input, not\
    \ a direct main-medium amount. Preserve source mg/g units and supplied hydrates.\
    \ The current stock-rate number must not be used undiluted as a main-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q23\",\n    \"claim\": \"NiCl2 x 6 H2O trace-stock\
    \ input\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM439 trace stock\
    \ only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n \
    \       \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": \"NiCl 2 ·6H 2 O 24.0 mg\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 Trace element solution exact ingredient\
    \ row\",\n        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 24.0 mg\",\n      \
    \  \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 24,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.024,\\\
    n                        \\\"mmol_l\\\": 0.185187,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"This is a separately prepared stock input, not\
    \ a direct main-medium amount. Preserve source mg/g units and supplied hydrates.\
    \ The current stock-rate number must not be used undiluted as a main-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q24\",\n    \"claim\": \"CuCl2 x 2 H2O trace-stock\
    \ input\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM439 trace stock\
    \ only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n \
    \       \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": \"CuCl 2 ·2H 2 O 2.0 mg\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 Trace element solution exact ingredient\
    \ row\",\n        \"exact_source_quote\": \"CuCl 2 ·2H 2 O 2.0 mg\",\n       \
    \ \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 2,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n\
    \                        \\\"mmol_l\\\": 0.0117314,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n     \
    \ }\n    ],\n    \"explanation\": \"This is a separately prepared stock input,\
    \ not a direct main-medium amount. Preserve source mg/g units and supplied hydrates.\
    \ The current stock-rate number must not be used undiluted as a main-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q25\",\n    \"claim\": \"ZnSO4 x 7 H2O trace-stock\
    \ input\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM439 trace stock\
    \ only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n \
    \       \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.144\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.144\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": \"ZnSO 4 ·7H 2 O 144.0 mg\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 Trace element solution exact ingredient\
    \ row\",\n        \"exact_source_quote\": \"ZnSO 4 ·7H 2 O 144.0 mg\",\n     \
    \   \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 144,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.144,\\\
    n                        \\\"mmol_l\\\": 0.500763,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"This is a separately prepared stock input, not\
    \ a direct main-medium amount. Preserve source mg/g units and supplied hydrates.\
    \ The current stock-rate number must not be used undiluted as a main-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q26\",\n    \"claim\": \"Na2MoO4 x 2 H2O trace-stock\
    \ input\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM439 trace stock\
    \ only; receiving JCM1076 dose 1 mL\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n \
    \       \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": \"Na 2 MoO 4 ·2H 2 O 36.0 mg\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm439\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 Trace element solution exact ingredient\
    \ row\",\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 36.0 mg\",\n  \
    \      \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 36,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.036,\\n\
    \                        \\\"mmol_l\\\": 0.148791,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\n      }\n\
    \    ],\n    \"explanation\": \"This is a separately prepared stock input, not\
    \ a direct main-medium amount. Preserve source mg/g units and supplied hydrates.\
    \ The current stock-rate number must not be used undiluted as a main-medium concentration.\"\
    \n  },\n  {\n    \"decision_id\": \"q27\",\n    \"claim\": \"Trace hydrochloric\
    \ acid strength\",\n    \"decision\": \"add\",\n    \"stage\": \"HCl reagent used\
    \ to prepare the trace stock\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions\",\n        \"stored\": null\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"25%, basis unspecified\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm439\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\",\n        \"source_locator\"\
    : \"JCM439 Trace element solution acid row\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 12.5 ml\",\n        \"snapshot_sha256\": \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\"\
    ,\n        \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"HCl\\\",\\n                        \\\"compound_id\\\": 68,\\\
    n                        \\\"attribute\\\": \\\"25%\\\",\\n                  \
    \      \\\"amount\\\": 12.5,\\n                        \\\"unit\\\": \\\"ml\\\"\
    ,\\n                        \\\"optional\\\": 0\\n                    }\",\n \
    \       \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the source solution qualification\
    \ independently of the hydrogen chloride molecule identifier. No concentration\
    \ basis, density or pure-compound mass is inferred.\"\n  },\n  {\n    \"decision_id\"\
    : \"q28\",\n    \"claim\": \"Main water input\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Main recipe before later stock additions\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"NaCl\",\n            \"term\": {\n    \
    \          \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium chloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    19.861\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:26710\",\n\
    \              \"label\": \"sodium chloride\"\n            }\n          },\n \
    \         {\n            \"preferred_term\": \"NH4Cl\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium\
    \ chloride\"\n            },\n            \"concentration\": {\n             \
    \ \"value\": \"0.993049\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:31206\"\
    ,\n              \"label\": \"ammonium chloride\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.0993049\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"K2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:131527\"\
    ,\n              \"label\": \"dipotassium hydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0993049\",\n \
    \             \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            }\n          },\n          {\n           \
    \ \"preferred_term\": \"KCl\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:32588\",\n              \"label\": \"potassium chloride\"\n        \
    \    },\n            \"concentration\": {\n              \"value\": \"0.0993049\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32588\",\n              \"label\": \"potassium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86345\"\
    ,\n              \"label\": \"magnesium dichloride hexahydrate\"\n           \
    \ },\n            \"concentration\": {\n              \"value\": \"0.0993049\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"Tris base\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:9754\",\n              \"label\": \"tris\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"2.97915\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:9754\",\n              \"label\": \"tris\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2S2O3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:32150\"\
    ,\n              \"label\": \"sodium thiosulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"2.97915\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32150\",\n              \"label\": \"sodium\
    \ thiosulfate pentahydrate\"\n            }\n          },\n          {\n     \
    \       \"preferred_term\": \"Resazurin\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:8806\",\n              \"label\": \"Resazurin\"\n     \
    \       },\n            \"concentration\": {\n              \"value\": \"0.000993049\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:8806\",\n              \"label\": \"Resazurin\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Yeast extract\",\n            \"concentration\": {\n              \"value\": \"\
    10\",\n              \"unit\": \"G_PER_L\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"Maltose\",\n            \"term\":\
    \ {\n              \"id\": \"CHEBI:17306\",\n              \"label\": \"maltose\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    20\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:17306\",\n              \"label\": \"maltose\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2CO3\",\n            \"term\": {\n              \"id\": \"CHEBI:29377\",\n \
    \             \"label\": \"sodium carbonate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"20\",\n              \"unit\":\
    \ \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:29377\",\n              \"label\": \"sodium\
    \ carbonate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2S x 9 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:76209\"\
    ,\n              \"label\": \"sodium sulfide nonahydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"6\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:76209\",\n              \"label\": \"sodium\
    \ sulfide nonahydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"HCl\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:17883\",\n              \"label\": \"hydrogen chloride\"\n         \
    \   },\n            \"concentration\": {\n              \"value\": \"12.5\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:17883\",\n              \"label\": \"hydrogen\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\"\
    ,\n              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"2.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"H3BO3\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.03\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:33118\",\n              \"label\": \"boric\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MnCl2 x 4 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86368\"\
    ,\n              \"label\": \"manganese(II) chloride tetrahydrate\"\n        \
    \    },\n            \"concentration\": {\n              \"value\": \"0.1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86368\",\n              \"label\": \"manganese(II)\
    \ chloride tetrahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"CoCl2 x 6 H2O\",\n            \"term\": {\n       \
    \       \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt chloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.19\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt\
    \ chloride hexahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"NiCl2 x 6 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.024\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:34887\",\n\
    \              \"label\": \"nickel dichloride\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"CuCl2 x 2 H2O\",\n           \
    \ \"term\": {\n              \"id\": \"CHEBI:86318\",\n              \"label\"\
    : \"copper(II) chloride dihydrate\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:86318\",\n              \"label\": \"copper(II) chloride\
    \ dihydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:32312\"\
    ,\n              \"label\": \"zinc sulfate heptahydrate\"\n            },\n  \
    \          \"concentration\": {\n              \"value\": \"0.144\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2MoO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\"\
    ,\n              \"label\": \"sodium molybdate dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.036\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          }\n        ]\n      },\n   \
    \   {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"NaCl\",\n            \"term\": {\n    \
    \          \"id\": \"CHEBI:26710\",\n              \"label\": \"sodium chloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    19.861\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:26710\",\n\
    \              \"label\": \"sodium chloride\"\n            }\n          },\n \
    \         {\n            \"preferred_term\": \"NH4Cl\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:31206\",\n              \"label\": \"ammonium\
    \ chloride\"\n            },\n            \"concentration\": {\n             \
    \ \"value\": \"0.993049\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:31206\"\
    ,\n              \"label\": \"ammonium chloride\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            },\n            \"concentration\": {\n \
    \             \"value\": \"0.0993049\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"K2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:131527\"\
    ,\n              \"label\": \"dipotassium hydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0993049\",\n \
    \             \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            }\n          },\n          {\n           \
    \ \"preferred_term\": \"KCl\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:32588\",\n              \"label\": \"potassium chloride\"\n        \
    \    },\n            \"concentration\": {\n              \"value\": \"0.0993049\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32588\",\n              \"label\": \"potassium\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgCl2 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86345\"\
    ,\n              \"label\": \"magnesium dichloride hexahydrate\"\n           \
    \ },\n            \"concentration\": {\n              \"value\": \"0.0993049\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86345\",\n              \"label\": \"magnesium\
    \ dichloride hexahydrate\"\n            }\n          },\n          {\n       \
    \     \"preferred_term\": \"Tris base\",\n            \"term\": {\n          \
    \    \"id\": \"CHEBI:9754\",\n              \"label\": \"tris\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"2.97915\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:9754\",\n              \"label\": \"tris\"\n\
    \            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2S2O3 x 5 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:32150\"\
    ,\n              \"label\": \"sodium thiosulfate pentahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"2.97915\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32150\",\n              \"label\": \"sodium\
    \ thiosulfate pentahydrate\"\n            }\n          },\n          {\n     \
    \       \"preferred_term\": \"Resazurin\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:8806\",\n              \"label\": \"Resazurin\"\n     \
    \       },\n            \"concentration\": {\n              \"value\": \"0.000993049\"\
    ,\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:8806\",\n              \"label\": \"Resazurin\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Yeast extract\",\n            \"concentration\": {\n              \"value\": \"\
    10\",\n              \"unit\": \"G_PER_L\"\n            }\n          },\n    \
    \      {\n            \"preferred_term\": \"Maltose\",\n            \"term\":\
    \ {\n              \"id\": \"CHEBI:17306\",\n              \"label\": \"maltose\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    20\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:17306\",\n              \"label\": \"maltose\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2CO3\",\n            \"term\": {\n              \"id\": \"CHEBI:29377\",\n \
    \             \"label\": \"sodium carbonate\"\n            },\n            \"\
    concentration\": {\n              \"value\": \"20\",\n              \"unit\":\
    \ \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:29377\",\n              \"label\": \"sodium\
    \ carbonate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2S x 9 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:76209\"\
    ,\n              \"label\": \"sodium sulfide nonahydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"6\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:76209\",\n              \"label\": \"sodium\
    \ sulfide nonahydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"HCl\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:17883\",\n              \"label\": \"hydrogen chloride\"\n         \
    \   },\n            \"concentration\": {\n              \"value\": \"12.5\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:17883\",\n              \"label\": \"hydrogen\
    \ chloride\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"FeSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\"\
    ,\n              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"2.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"H3BO3\",\n            \"term\": {\n              \"\
    id\": \"CHEBI:33118\",\n              \"label\": \"boric acid\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.03\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:33118\",\n              \"label\": \"boric\
    \ acid\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MnCl2 x 4 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86368\"\
    ,\n              \"label\": \"manganese(II) chloride tetrahydrate\"\n        \
    \    },\n            \"concentration\": {\n              \"value\": \"0.1\",\n\
    \              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86368\",\n              \"label\": \"manganese(II)\
    \ chloride tetrahydrate\"\n            }\n          },\n          {\n        \
    \    \"preferred_term\": \"CoCl2 x 6 H2O\",\n            \"term\": {\n       \
    \       \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt chloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.19\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:53503\",\n              \"label\": \"cobalt\
    \ chloride hexahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"NiCl2 x 6 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:34887\",\n              \"label\": \"nickel dichloride\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.024\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:34887\",\n\
    \              \"label\": \"nickel dichloride\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"CuCl2 x 2 H2O\",\n           \
    \ \"term\": {\n              \"id\": \"CHEBI:86318\",\n              \"label\"\
    : \"copper(II) chloride dihydrate\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.002\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:86318\",\n              \"label\": \"copper(II) chloride\
    \ dihydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"ZnSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:32312\"\
    ,\n              \"label\": \"zinc sulfate heptahydrate\"\n            },\n  \
    \          \"concentration\": {\n              \"value\": \"0.144\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:32312\",\n              \"label\": \"zinc sulfate\
    \ heptahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Na2MoO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\"\
    ,\n              \"label\": \"sodium molybdate dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.036\",\n      \
    \        \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          }\n        ]\n      }\n    ],\n\
    \    \"source_amount\": \"950 mL\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 950,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"Water is absent from both local recipes.\
    \ Preserve the main input rather than summing it with the water used to prepare\
    \ a separate trace-stock batch.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n\
    \    \"claim\": \"Trace-stock addition\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"Main recipe assembly\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"1 mL\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 trace-stock reference and dose\",\n \
    \       \"exact_source_quote\": \"Trace element solution (see Medium No. 439 )\
    \ 1.0 ml\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    solution\\\": \\\"Trace element solution\\\",\\n                        \\\"solution_id\\\
    \": 4186,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The exact stock addition and reference\
    \ are missing. Transfer only the named trace subsection, not the whole JCM439\
    \ medium or its other stocks.\"\n  },\n  {\n    \"decision_id\": \"q30\",\n  \
    \  \"claim\": \"Trace-stock water input\",\n    \"decision\": \"add\",\n    \"\
    stage\": \"JCM439 Trace element solution batch\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"987 mL\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"jcm439\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439\"\
    ,\n        \"source_locator\": \"JCM439 terminal trace-stock water row\",\n  \
    \      \"exact_source_quote\": \"Distilled water 987.0 ml\",\n        \"snapshot_sha256\"\
    : \"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda\",\n    \
    \    \"parsed_text_sha256\": \"d678d0e3ec848ea6d029f04800693f55fdbfab8dbb3b45924645cfff6e24b74b\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ1076api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J1076\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 987,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"53ec1a540b136bd6b5eb3cdd399341a852764be9291919c35772cd5b7aeb74a5\"\
    \n      }\n    ],\n    \"explanation\": \"The provider declares a 1000 mL stock\
    \ basis, while the listed liquid inputs are 987 mL water and 12.5 mL acid. Their\
    \ arithmetic sum is 999.5 mL, not a measured final volume; the source does not\
    \ instruct a make-up volume. Keep the 987 mL input unchanged and record the denominator\
    \ distinction.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"claim\": \"\
    Initial main pH\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Before\
    \ main autoclaving\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0]\",\n        \"stored\": {\n          \"step_number\"\
    : 1,\n          \"action\": \"AUTOCLAVE\",\n          \"description\": \"Mix components\
    \ thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere.\
    \ After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add\
    \ the following solutions from sterile anaerobic stocks (autoclaved and stored\
    \ under a N2 atmosphere):\"\n        }\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\",\n        \"\
    field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n          \"step_number\"\
    : 1,\n          \"action\": \"AUTOCLAVE\",\n          \"description\": \"Mix components\
    \ thoroughly, adjust pH to 9.0 with NaOH and autoclave under a N2 atmosphere.\
    \ After cooling, replace the gas phase with a N2-CO2 (4:1, v/v) gas mixture. Add\
    \ the following solutions from sterile anaerobic stocks (autoclaved and stored\
    \ under a N2 atmosphere):\"\n        }\n      }\n    ],\n    \"source_amount\"\
    : \"9.0\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 main preparation before autoclaving\"\
    ,\n        \"exact_source_quote\": \"adjust pH to 9.0 with NaOH\",\n        \"\
    snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"The existing preparation already retains\
    \ this pH stage and NaOH identity. Add claim evidence without replacing the later\
    \ pH target.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n    \"claim\": \"Final\
    \ pH check\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"After the\
    \ later stock additions\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": 8.2\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\",\n        \"\
    field_path\": \"ph_value\",\n        \"stored\": 8.2\n      },\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n    \
    \      \"step_number\": 2,\n          \"action\": \"MIX\",\n          \"description\"\
    : \"Check final pH be around 8.2.\"\n        }\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\",\n \
    \       \"field_path\": \"preparation_steps[1]\",\n        \"stored\": {\n   \
    \       \"step_number\": 2,\n          \"action\": \"MIX\",\n          \"description\"\
    : \"Check final pH be around 8.2.\"\n        }\n      }\n    ],\n    \"source_amount\"\
    : \"around 8.2\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 last preparation sentence\",\n      \
    \  \"exact_source_quote\": \"Check final pH be around 8.2.\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"Both local layers already retain the\
    \ target value and final-check instruction. This does not assert an experimentally\
    \ measured result or a growth optimum.\"\n  },\n  {\n    \"decision_id\": \"q33\"\
    ,\n    \"claim\": \"Post-cooling gas ratio\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"Gas-phase replacement before later stocks\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      }\n\
    \    ],\n    \"source_amount\": \"N2:CO2 4:1, v/v\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 post-cooling gas sentence\",\n        \"exact_source_quote\": \"N\
    \ 2 -CO 2 (4:1, v/v) gas mixture.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"The existing preparation includes the\
    \ exact ratio and basis; retain its timing. Do not apply the mixed gas to stocks\
    \ that are separately autoclaved and stored under N2.\"\n  },\n  {\n    \"decision_id\"\
    : \"q34\",\n    \"claim\": \"Autoclave temperature\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM1076 displayed default for the stated autoclaving steps\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components thoroughly, adjust pH to 9.0\
    \ with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas\
    \ phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from\
    \ sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):\"\n\
    \          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"MIX\",\n            \"description\": \"Check final pH be around 8.2.\"\n \
    \         }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components thoroughly, adjust pH to 9.0\
    \ with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas\
    \ phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from\
    \ sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):\"\n\
    \          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"MIX\",\n            \"description\": \"Check final pH be around 8.2.\"\n \
    \         }\n        ]\n      }\n    ],\n    \"source_amount\": \"121°C\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 displayed default above the exact recipe\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"The source page itself displays this\
    \ default and the recipe does not override it. Existing instructions name autoclaving\
    \ but omit the numerical default; retain the main and later-stock stages without\
    \ transferring unrelated parent-medium procedures.\"\n  },\n  {\n    \"decision_id\"\
    : \"q35\",\n    \"claim\": \"Autoclave duration\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM1076 displayed default for the stated autoclaving steps\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components thoroughly, adjust pH to 9.0\
    \ with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas\
    \ phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from\
    \ sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):\"\n\
    \          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"MIX\",\n            \"description\": \"Check final pH be around 8.2.\"\n \
    \         }\n        ]\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Mix components thoroughly, adjust pH to 9.0\
    \ with NaOH and autoclave under a N2 atmosphere. After cooling, replace the gas\
    \ phase with a N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from\
    \ sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):\"\n\
    \          },\n          {\n            \"step_number\": 2,\n            \"action\"\
    : \"MIX\",\n            \"description\": \"Check final pH be around 8.2.\"\n \
    \         }\n        ]\n      }\n    ],\n    \"source_amount\": \"15 min\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 displayed default above the exact recipe\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"The source page itself displays this\
    \ default and the recipe does not override it. Existing instructions name autoclaving\
    \ but omit the numerical default; retain the main and later-stock stages without\
    \ transferring unrelated parent-medium procedures.\"\n  },\n  {\n    \"decision_id\"\
    : \"q36\",\n    \"claim\": \"NaOH dose and strength\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"stage\": \"Initial main pH adjustment\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      }\n\
    \    ],\n    \"source_amount\": \"No fixed dose or strength\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 main pH-adjustment sentence\",\n        \"exact_source_quote\": \"\
    adjust pH to 9.0 with NaOH\",\n        \"snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"The existing instruction names NaOH\
    \ but the source does not quantify it. Do not supply a typical strength or treat\
    \ the unstated amount as zero.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n \
    \   \"claim\": \"Nitrogen atmosphere purity\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"stage\": \"Main autoclaving and separate stock preparation/storage\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      }\n\
    \    ],\n    \"source_amount\": \"N2 atmosphere; numeric purity not stated\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm1076\",\n \
    \       \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 main autoclaving sentence\",\n      \
    \  \"exact_source_quote\": \"autoclave under a N 2 atmosphere.\",\n        \"\
    snapshot_sha256\": \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\"\
    ,\n        \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-stock handling parenthesis\",\n        \"exact_source_quote\"\
    : \"autoclaved and stored under a N 2 atmosphere\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"Both stages are retained in existing\
    \ preparation. Do not rewrite the source as an explicit 100% purity claim or confuse\
    \ it with the later 4:1 gas mixture.\"\n  },\n  {\n    \"decision_id\": \"q38\"\
    ,\n    \"claim\": \"Cooling endpoint and stock preparation volumes\",\n    \"\
    decision\": \"not_quantified\",\n    \"stage\": \"Post-autoclave transition and\
    \ separately prepared later stocks\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n    \
    \      \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n          \"\
    description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and autoclave\
    \ under a N2 atmosphere. After cooling, replace the gas phase with a N2-CO2 (4:1,\
    \ v/v) gas mixture. Add the following solutions from sterile anaerobic stocks\
    \ (autoclaved and stored under a N2 atmosphere):\"\n        }\n      },\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0]\",\n        \"stored\": {\n\
    \          \"step_number\": 1,\n          \"action\": \"AUTOCLAVE\",\n       \
    \   \"description\": \"Mix components thoroughly, adjust pH to 9.0 with NaOH and\
    \ autoclave under a N2 atmosphere. After cooling, replace the gas phase with a\
    \ N2-CO2 (4:1, v/v) gas mixture. Add the following solutions from sterile anaerobic\
    \ stocks (autoclaved and stored under a N2 atmosphere):\"\n        }\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_LACT_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"No numerical cooling endpoint or stock-batch\
    \ volumes\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm1076\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\"\
    ,\n        \"source_locator\": \"JCM1076 preparation transition\",\n        \"\
    exact_source_quote\": \"After cooling, replace the gas phase\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      },\n      {\n        \"source_key\": \"jcm1076\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1076\",\n        \"source_locator\"\
    : \"JCM1076 later-addition introduction\",\n        \"exact_source_quote\": \"\
    Add the following solutions from sterile anaerobic stocks\",\n        \"snapshot_sha256\"\
    : \"cefedc1478c15726eb583327516e53d7029191e14d9c0fb52fcc55202b9266e2\",\n    \
    \    \"parsed_text_sha256\": \"06dd1bcded57eae86952b90050c2ce32d875dcfc75af36e113a898a868ec6dd9\"\
    \n      }\n    ],\n    \"explanation\": \"The exact source gives receiving doses\
    \ and stock strengths, but not a cooling temperature or stock preparation batch\
    \ volumes. Preserve these unknowns without importing another medium procedure.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '21 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 21/22 primary and 21/22 secondary
    instances; all asserted CHEBI-keyed secondary IDs have exact pinned MIM rows;
    no legacy MIM identifier is asserted in the target or maintained owner. Exact
    supplied-form mismatch is addressed separately; valid IDs and labels do not establish
    correct source grounding.'
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi17306
  - chebi17883
  - chebi26710
  - chebi29377
  - chebi31206
  - chebi32150
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi53503
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi9754
  details: 'Instance coverage on a 0–100 percent scale, denominator 22: primary 95.45%;
    secondary 95.45%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact medium and trace-subsection identity
  outcome: supported
  summary: CM002256 and its sole maintained owner resolve to JCM1076 and provider
    main solution 5141. The source names the JCM439 trace stock and provider solution
    4186. Only that subsection transfers; unrelated JCM439 basal, vitamin, lactate
    and selenite/tungstate content is excluded.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - provider
  - trace-primary
  - trace-api
- assessment_id: preparation
  area: completeness
  topic: Retained instructions and missing later-stock details
  outcome: concern
  summary: The two existing preparation steps retain initial pH 9, N2 autoclaving,
    post-cooling 4:1 gas replacement, stock handling and final pH around 8.2. However,
    the first step ends with a colon and the four stock identities, strengths and
    liquid doses are absent as such; numeric sterilization defaults and water are
    also missing.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
- assessment_id: supplied-forms
  area: grounding
  topic: Hydrates and unspecified solution qualifications
  outcome: concern
  summary: The source-specific Mg, thiosulfate, Fe, Mn, Co, Cu, Zn, Mo and sulfide
    hydrate forms agree with their asserted structures. Cobalt CHEBI:53503 explicitly
    encodes six waters; its unrelated synonym text is not a reason to reject the correct
    structure. Nickel CHEBI:34887 lacks the six source waters. Maltose molarity does
    not authorize assuming a hydrate or mass, and hydrogen chloride identity does
    not encode the 25% stock solution.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - primary
  - trace-primary
  - chebi53503
  - chebi34887
  - chebi17306
  - chebi17883
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Recipe class and biological claims
  outcome: supported
  summary: Yeast extract supports complex and undefined classifications; liquid is
    consistent with no gelling ingredient. Generic bacterial filing and cultivation
    application do not assert a named strain or growth experiment. No growth assertion
    is inferred from the medium title or parent-stock source.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
- assessment_id: ownership
  area: ownership
  topic: Maintained source and generated target
  outcome: supported
  summary: Both layers contain the same 22 concentrations and two preparation steps.
    Curate the normalized owner and demonstrated conversion issue first, then regenerate
    separately; preserve existing history rather than rewriting it to claim source
    verification.
  target_ids:
  - CultureMech:002256
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: cm002256-stock-representation
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Liquid stock additions and trace inputs are flattened into main concentrations
  description: Four later doses of 10, 20, 20 and 6 mL become G_PER_L values, and
    nine trace-stock inputs are exposed without the 1 mL receiving dose. The HCl stock
    input is likewise 12.5 mL, not 12.5 g/L. Missing stage and strength metadata materially
    change the recipe.
  target_ids:
  - CultureMech:002256
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - trace-primary
  - trace-api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  issue_key: cm002256-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel dichloride
  description: The trace source and local preferred term specify NiCl2·6H2O, but both
    primary and secondary CHEBI:34887 assertions encode nickel dichloride without
    those six waters. Label correctness does not establish supplied-form correspondence.
  target_ids:
  - CultureMech:002256
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - trace-primary
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  issue_key: cm002256-preparation-completeness
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The preparation omits the list introduced by its final colon and numeric
    defaults
  description: The existing main method preserves the gas and pH sequence but has
    no corresponding four-stock list or structured stock equivalents. It also omits
    the displayed 121°C/15 min default and main/trace water inputs. Existing pH values
    and gas ratio are supported and should remain.
  target_ids:
  - CultureMech:002256
  field_paths:
  - preparation_steps
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - trace-primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  issue_key: cm002256-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported main rates and existing pH/gas instructions lack claim evidence
  description: The unchanged main rates match the provider-declared 1007 mL basis,
    and existing pH/gas instructions match the primary, but neither layer attaches
    evidence to these claims. A record-level source link alone does not distinguish
    main and stock bases.
  target_ids:
  - CultureMech:002256
  field_paths:
  - ingredients
  - ph_value
  - preparation_steps
  - references
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  description: Restore source-scoped stocks, original liquid units, strengths and
    receiving doses; preserve original trace masses and water. Keep unspecified percent
    bases unresolved and do not infer final concentrations from flattened values.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  description: Resolve a source-specific supplied-form identifier or explicitly retain
    unresolved grounding; do not change the source stock mass or infer a replacement
    secondary mapping.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  description: Complete the missing stock list and scoped water/default details using
    exact source evidence, retaining the existing timing and distinct atmospheres.
    Do not invent cooling endpoints, NaOH strength or stock-batch volumes.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
  description: Attach exact original quantities, provider basis and stage-specific
    snippets to the corrected and unchanged claims. Keep the provider basis distinct
    from measured final volume and preserve source percentage qualifications.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:002256
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaliphilus_lact_medium.yaml
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
- Exact primary and provider sources needed for this bounded review are available.
  Unspecified percentage bases, NaOH dose/strength, cooling endpoint, stock preparation
  volumes and measured final volumes remain unknown; the provider 1000 mL trace basis
  is retained separately from 999.5 mL listed liquid inputs. Parent JCM439 content
  outside its named trace subsection supplies no cultivation or formulation evidence
  for this record.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-023
- generated-medium
```
