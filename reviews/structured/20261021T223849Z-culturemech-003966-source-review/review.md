# Source and formulation review: beijerinckia_doebereinerae_medium (CultureMech:003966)

- Review: 20261021T223849Z-culturemech-003966-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T22:32:20Z
- Finished UTC: 2026-10-21T22:38:49Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact DSMZ 1215 and recovered historical API bytes support all eight local provider-normalized amounts, including conditional agar. Both maintained owners have authenticated amount evidence absent from the generated target. Every layer omits 1000 ml source water; only the DSMZ owner retains the pH/solid-medium preparation paragraph. Explicit source hydrates match the asserted terms and source-unqualified glucose does not establish a racemate.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 399; batch 040 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-nine task batches contain 390 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 393 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003966 | data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml | generated | beijerinckia_doebereinerae_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003966 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003966 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/399/strict.tsv |
| validate-terms | passed | True | CultureMech:003966 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003966 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003966 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1215api | unavailable | False | CultureMech:003966 | Current mediadive1215api returned HTTP 503. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants. |
| Exact source content access: mediadive1215api_retry | unavailable | False | CultureMech:003966 | Current mediadive1215api_retry returned HTTP 503. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants. |
| Exact source content access: komodo1215detail | unavailable | False | CultureMech:003966 | Current komodo1215detail returned HTTP 403. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003966.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003966.

30 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "KH2PO4",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.8",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "KH2PO4 0.80 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.8,\n                        \"mmol_l\": 5.87868,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q2",
    "name": "KH2PO4",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.8",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "KH2PO4 0.80 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.8,\n                        \"mmol_l\": 5.87868,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q3",
    "name": "KH2PO4",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.8",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "KH2PO4 0.80 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.8,\n                        \"mmol_l\": 5.87868,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q4",
    "name": "K2HPO4",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "K2HPO4 0.20 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q5",
    "name": "K2HPO4",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "K2HPO4 0.20 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q6",
    "name": "K2HPO4",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.2",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "K2HPO4 0.20 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q7",
    "name": "MgSO4 x 7 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.5",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q8",
    "name": "MgSO4 x 7 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.5",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q9",
    "name": "MgSO4 x 7 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.5",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q10",
    "name": "FeCl3 x 6 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.1",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "FeCl3 x 6 H2O 0.10 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.369965,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q11",
    "name": "FeCl3 x 6 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.1",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "FeCl3 x 6 H2O 0.10 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.369965,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q12",
    "name": "FeCl3 x 6 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.1",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "FeCl3 x 6 H2O 0.10 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.369965,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q13",
    "name": "CaCl2 x 2 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.05",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "CaCl2 x 2 H2O 0.05 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q14",
    "name": "CaCl2 x 2 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.05",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "CaCl2 x 2 H2O 0.05 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q15",
    "name": "CaCl2 x 2 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.05",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "CaCl2 x 2 H2O 0.05 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q16",
    "name": "Na2MoO4 x 7 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Na2MoO4 x 7 H2O 5.00 mg",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2MoO4 x 7 H2O\",\n                        \"compound_id\": 950,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0150593,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. The 5 mg source amount converts to 0.005 g on the declared 1 L provider basis. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q17",
    "name": "Na2MoO4 x 7 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Na2MoO4 x 7 H2O 5.00 mg",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2MoO4 x 7 H2O\",\n                        \"compound_id\": 950,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0150593,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. The 5 mg source amount converts to 0.005 g on the declared 1 L provider basis. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q18",
    "name": "Na2MoO4 x 7 H2O",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.005",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "0.005",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Na2MoO4 x 7 H2O 5.00 mg",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2MoO4 x 7 H2O\",\n                        \"compound_id\": 950,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0150593,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. The 5 mg source amount converts to 0.005 g on the declared 1 L provider basis. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q19",
    "name": "Glucose",
    "stage": "Main provider-declared recipe",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "20",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Glucose 20.00 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 111.012,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q20",
    "name": "Glucose",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "20",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Glucose 20.00 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 111.012,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q21",
    "name": "Glucose",
    "stage": "Main provider-declared recipe",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "20",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Glucose 20.00 g",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 111.012,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q22",
    "name": "Agar",
    "stage": "Solid branch",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "15",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": "for solid medium"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "This target field has no attached amount evidence; externally supported values require evidence-only follow-up. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q23",
    "name": "Agar",
    "stage": "Solid branch",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "15",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": "for solid medium"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q24",
    "name": "Agar",
    "stage": "Solid branch",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "value": "15",
      "unit": "G_PER_L",
      "provider_declared_volume_ml": 1000,
      "source_condition": "for solid medium"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary composition/conditional agar paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Matching attached amount evidence exists in this owner only. Provider declaration is not independent measurement or proof of supplied chemical form. Preserve the agar condition and all exact hydrates."
  },
  {
    "decision_id": "q25",
    "name": "Distilled water",
    "stage": "Main solvent",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.8",
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
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "FeCl3 x 6 H2O",
            "term": {
              "id": "CHEBI:86254",
              "label": "iron trichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86254",
              "label": "iron trichloride hexahydrate"
            }
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 7 H2O",
            "term": {
              "id": "CHEBI:86473",
              "label": "sodium molybdate heptahydrate"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86473",
              "label": "sodium molybdate heptahydrate"
            }
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "notes": " (for solid medium)",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.8,\n                        \"mmol_l\": 5.87868,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (KH2PO4) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=0.8; check: 0.8 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.8 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (K2HPO4) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "FeCl3 x 6 H2O",
            "term": {
              "id": "CHEBI:86254",
              "label": "iron trichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86254",
              "label": "iron trichloride hexahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.369965,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (FeCl3 x 6 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (CaCl2 x 2 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Na2MoO4 x 7 H2O",
            "term": {
              "id": "CHEBI:86473",
              "label": "sodium molybdate heptahydrate"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86473",
              "label": "sodium molybdate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2MoO4 x 7 H2O\",\n                        \"compound_id\": 950,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0150593,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Na2MoO4 x 7 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.005; check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 111.012,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Glucose) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "notes": " (for solid medium)",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[7].concentration (Agar) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[8]. Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f. KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a. The mapping supports identity only, not ingredient quantities or variants."
              }
            ]
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.8",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.8,\n                        \"mmol_l\": 5.87868,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[0].concentration (KH2PO4) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[0]. Provider explicitly reports g_l=0.8; check: 0.8 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.8 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.2",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.14826,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[1].concentration (K2HPO4) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.5",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "FeCl3 x 6 H2O",
            "term": {
              "id": "CHEBI:86254",
              "label": "iron trichloride hexahydrate"
            },
            "concentration": {
              "value": "0.1",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86254",
              "label": "iron trichloride hexahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.369965,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[3].concentration (FeCl3 x 6 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[3]. Provider explicitly reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "CaCl2 x 2 H2O",
            "term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "concentration": {
              "value": "0.05",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86158",
              "label": "calcium chloride dihydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.340101,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[4].concentration (CaCl2 x 2 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[4]. Provider explicitly reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "Na2MoO4 x 7 H2O",
            "term": {
              "id": "CHEBI:86473",
              "label": "sodium molybdate heptahydrate"
            },
            "concentration": {
              "value": "0.005",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:86473",
              "label": "sodium molybdate heptahydrate"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2MoO4 x 7 H2O\",\n                        \"compound_id\": 950,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0150593,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[5].concentration (Na2MoO4 x 7 H2O) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[5]. Provider explicitly reports g_l=0.005; check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "20",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 20,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 111.012,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[6].concentration (Glucose) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[6]. Provider explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15",
              "unit": "G_PER_L"
            },
            "notes": " (for solid medium)",
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "evidence": [
              {
                "reference": "https://mediadive.dsmz.de/rest/medium/1215",
                "supports": "SUPPORT",
                "snippet": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
                "explanation": "Concentration evidence for ingredients[7].concentration (Agar) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[8]. Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L. This supports the provider-declared main-recipe concentration, not an independently measured final volume, a stock composition, or a downstream assay dilution. Water alone does not establish final volume. Exact source ingredient labels/forms are matched; secondary ontology mappings are not validated by this evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f."
              }
            ]
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 1000,
      "source_unit": "ml"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Primary final table row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      },
      {
        "source_key": "mediadive1215Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/1215",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f"
      }
    ],
    "interpretation": "Every layer omits the source solvent input. Add it in the appropriate preparation scope; do not turn water volume into mass or independently measured final volume."
  },
  {
    "decision_id": "q26",
    "name": "Final pH",
    "stage": "Main medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      }
    ],
    "desired": {
      "value": 6.5
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Final primary paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      }
    ],
    "interpretation": "All stored pH values agree. Ingredient-specific evidence does not authenticate this separate field automatically."
  },
  {
    "decision_id": "q27",
    "name": "Solid-branch agar qualifier",
    "stage": "Optional branch",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[7].notes",
        "stored": " (for solid medium)"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "ingredients[7].notes",
        "stored": " (for solid medium)"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "ingredients[7].notes",
        "stored": " (for solid medium)"
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "physical_state",
        "stored": "SOLID_AGAR"
      }
    ],
    "desired": {
      "agar_rate_g_per_l": 15,
      "condition": "for solid media"
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Final primary paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      }
    ],
    "interpretation": "All ingredient notes already retain the solid-medium condition. SOLID_AGAR represents that branch; the source also permits the no-agar formulation."
  },
  {
    "decision_id": "q28",
    "name": "Existing DSMZ preparation",
    "stage": "DSMZ maintained owner",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Final pH is 6.5. Add 15.0 g/l agar for solid media."
      }
    ],
    "desired": {
      "source_text": "Final pH is 6.5. Add 15.0 g/l agar for solid media."
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Final primary paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      }
    ],
    "interpretation": "The DSMZ owner already retains pH and conditional agar instructions; preserve its preparation and attached amount evidence."
  },
  {
    "decision_id": "q29",
    "name": "Missing preparation context",
    "stage": "Target and KOMODO owner",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "desired": {
      "source_text": "Final pH is 6.5. Add 15.0 g/l agar for solid media."
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Final primary paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      }
    ],
    "interpretation": "Only these two layers omit the preparation paragraph. This does not mean their existing pH or agar qualifier is absent."
  },
  {
    "decision_id": "q30",
    "name": "Unspecified preparation/growth numbers",
    "stage": "Whole medium",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "desired": {
      "cycle": null,
      "titrant_dose_strength": null,
      "cultivation_temperature_duration": null,
      "measured_final_volume": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz1215",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf",
        "source_locator": "Final primary paragraph",
        "exact_source_quote": "Final pH is 6.5. Add 15.0 g/l agar for solid media.",
        "snapshot_sha256": "c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76",
        "parsed_text_sha256": "785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13"
      }
    ],
    "interpretation": "No numerical sterilization cycle, titrant specification or growth condition is given. The provider volume declaration remains distinct from a measured final volume."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:003966.

8 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 8/8 primary and 8/8 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%; secondary 100.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003966.

24 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact 1215 accession and owner relationship

identity: supported. Targets: CultureMech:003966.

Exact catalog, primary title, historical medium metadata and reciprocal maintained relationships establish the source identity. Formula fingerprints alone do not establish equivalence. No organism-specific growth or taxonomy mapping is inferred from the title.

### Source chemical forms and generic glucose

grounding: supported. Targets: CultureMech:003966.

KH2PO4/K2HPO4 and the explicit Mg heptahydrate, Fe hexahydrate, Ca dihydrate and sodium molybdate heptahydrate agree with asserted names/formulae. Preserve the unusual heptahydrate rather than replacing it with a common dihydrate. Generic glucose agrees with the generic term; its DL synonym does not prove a racemate was supplied. The CHEBI:131527 trihydrate synonym does not establish hydration absent from the source. Agar is a complex solidifying material.

### Owner authentication and generated lag

evidence: concern. Targets: CultureMech:003966.

All sixteen maintained ingredient claims authenticate narrowly to their own fields and provider normalization. The generated target lacks these claims, references and later concentration history. The catalog identity claim cannot support quantities or oxygen physiology.

### Source solvent and preserved conditional agar

completeness: concern. Targets: CultureMech:003966.

The 1000 ml solvent is absent in all layers. Only DSMZ owner retains preparation prose, while pH 6.5 and conditional agar notes already exist in all layers. Source supplies no numerical cycle or incubation conditions.

### Defined basal medium and solid branch

scope: supported. Targets: CultureMech:003966.

The listed chemical basal composition supports the defined classification; agar is an optional solidifying branch already qualified locally. No nitrogen fixation, oxygen physiology or species growth is inferred from the name or KOMODO flags.

## Findings

### f1: Solvent and layer-specific preparation are incomplete

major / open / confirmed; issue key: culturemech.003966.missing-solvent-and-preparation-context.

All layers omit 1000 ml source water; target and KOMODO lack preparation retained by DSMZ. Existing pH and agar condition are already correct and must be preserved.

### f2: Generated target omits authenticated owner evidence

major / open / confirmed; issue key: culturemech.003966.generated-evidence-lag.

The sixteen attached owner amount claims and catalog identity claim are absent from the target. This observed difference is not proof of universal loss by the current guarded merger.

### f3: KOMODO history retains malformed and naive times

minor / open / confirmed; issue key: culturemech.003966.malformed-import-times.

The .fZ import timestamp and timezone-naive resolver timestamp occur in target and KOMODO history. Exact replacements are not established.

## Recommended Actions And Acceptance Checks

### a1

Restore exact solvent input and missing preparation ownership without duplicating the DSMZ instruction or inferring a numerical cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve authenticated owner evidence and later history, verify source formulation compatibility and regenerate only via the supported guarded path after authorization.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve original events and append only an independently supported clarification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch040/399/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/399/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml:1:id: CultureMech:003966<br>./data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml:1:id: CultureMech:003966<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch040/source-preflight-bound/399/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 14 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf; Complete DSMZ 1215 table and conditional agar/pH paragraph | supports | The primary supplies seven main batch masses, 1000 ml water, pH 6.5 and 15.0 g/l agar for the solid branch. |
| historical-raw | https://mediadive.dsmz.de/rest/medium/1215; Historical $.data.medium and $.data.solutions[0], complete recipe/volume/steps | supports | Exact historical response hash and original October 7 timestamp are recovered. Declared volume is 1000 ml and amounts are provider g_l, not a measured final volume. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 1215 row | supports | Catalog supplies source identity and DSMZ link only, not ingredient amounts or equivalence of all historical variants. |
| mediadive1215api-attempt | https://mediadive.dsmz.de/rest/medium/1215; Preserved exact public retrieval result | context_only | Current mediadive1215api returned HTTP 503. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants. |
| mediadive1215api_retry-attempt | https://mediadive.dsmz.de/rest/medium/1215; Preserved exact public retrieval result | context_only | Current mediadive1215api_retry returned HTTP 503. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants. |
| komodo1215detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1215; Preserved exact public retrieval result | context_only | Current komodo1215detail returned HTTP 403. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch040/399/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86254 resolves to iron trichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86473 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86473; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86473 resolves to sodium molybdate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86254": [{"label": "FeCl3 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86254", "preferred_term": "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86473": [{"label": "Na2MoO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86473", "preferred_term": "Na2MoO4 x 7 H2O", "ontology_id": "CHEBI:86473", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:14.429895"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:14.429895"}]}, {"input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml", "events": 7, "timestamp_issues": []}] |
| history-inventory | /private/tmp/culturemech-review-work-batch040/399/history-inventory.json; All seventeen attached owner claims and scoped historical reports | context_only | Sixteen amount claims match the historical API hash and literal objects; the catalog claim matches its separate source/hash. None of that attached evidence is present in the generated target. Reports do not replace raw authentication. |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer/guarded merger is context only; observed older target evidence/preparation omissions do not demonstrate execution of the present guarded logic. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer/guarded merger is context only; observed older target evidence/preparation omissions do not demonstrate execution of the present guarded logic. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer/guarded merger is context only; observed older target evidence/preparation omissions do not demonstrate execution of the present guarded logic. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current mediadive1215api returned HTTP 503. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants.
- Current mediadive1215api_retry returned HTTP 503. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants.
- Current komodo1215detail returned HTTP 403. Exact primary and historical raw resolve the material claims; unavailable optional detail does not itself require partial completion or establish unseen variants.
- Required current primary and historical amount sources are available. Optional current API/detail failures remain preserved without forcing partial completion. No complete historical-variant equivalence, measured final volume or growth condition is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T223849Z-culturemech-003966-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: beijerinckia_doebereinerae_medium (CultureMech:003966)'
started_at: '2026-10-21T22:32:20Z'
finished_at: '2026-10-21T22:38:49Z'
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
summary: Exact DSMZ 1215 and recovered historical API bytes support all eight local
  provider-normalized amounts, including conditional agar. Both maintained owners
  have authenticated amount evidence absent from the generated target. Every layer
  omits 1000 ml source water; only the DSMZ owner retains the pH/solid-medium preparation
  paragraph. Explicit source hydrates match the asserted terms and source-unqualified
  glucose does not establish a racemate.
source:
  git_revision: 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
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
  - path: data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    sha256: 054d16df3cc4a958787ef820b5c6ab1fcf93130a254826fe6a0576538df48d14
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    sha256: d2a94fa33730cb0c0cd312943b412e5cd15e22de57c7a84ad14682ddfecf6bc4
    role: context
  - path: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
    sha256: 47b7ceed2b34ec84250f7e7c5017ce1bc4397561c3cf27ab84f238f079f6ef52
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/plan.json
    sha256: 94e89303f14558d9b0d485aa6cb4eb646050837864ab920d759763a3a483b94f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/beijerinckia_doebereinerae_medium.yaml.md
    sha256: c933233fb494d46372c6b1f6f140bfdbde0c42cf1407c1f0962934b8182f9952
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/inspected-candidate-context.json
    sha256: bef58d348ed78c4694bd9876429eea22eed599556ff8a9f9b79f4858745bd02e
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/plan.json
    sha256: 0fc7158ec48d1b0c75efa149070b46b677bb3389d969a1440267f43e21b3d3c8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml.md
    sha256: 23fe70a8251c470548c19feb5d7dc85e377450a1ee9db01a90c53777179b6404
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
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
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
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
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 399; batch 040 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-nine task batches
    contain 390 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 393 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003966
targets:
- target_id: CultureMech:003966
  path: data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  label: beijerinckia_doebereinerae_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch040/399/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/399/strict.tsv"
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003966
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
  - CultureMech:003966
- check_id: mediadive1215api-source-access
  name: 'Exact source content access: mediadive1215api'
  required: false
  status: unavailable
  summary: Current mediadive1215api returned HTTP 503. Exact primary and historical
    raw resolve the material claims; unavailable optional detail does not itself require
    partial completion or establish unseen variants.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - mediadive1215api-attempt
- check_id: mediadive1215api_retry-source-access
  name: 'Exact source content access: mediadive1215api_retry'
  required: false
  status: unavailable
  summary: Current mediadive1215api_retry returned HTTP 503. Exact primary and historical
    raw resolve the material claims; unavailable optional detail does not itself require
    partial completion or establish unseen variants.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - mediadive1215api_retry-attempt
- check_id: komodo1215detail-source-access
  name: 'Exact source content access: komodo1215detail'
  required: false
  status: unavailable
  summary: Current komodo1215detail returned HTTP 403. Exact primary and historical
    raw resolve the material claims; unavailable optional detail does not itself require
    partial completion or establish unseen variants.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - komodo1215detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:53.403063Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch040/399/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:54.601843Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/399/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:56.084707Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:56.932721Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:38:48Z'
  support: supports
  summary: './data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml:1:id:
    CultureMech:003966

    ./data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml:1:id:
    CultureMech:003966

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/source-preflight-bound/399/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:38:48Z'
  support: supports
  summary: 14 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 67d0273beb6046a685044dde5df4e1a66c9fa003a7a166aa3136ee3f46287486
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf
  locator: Complete DSMZ 1215 table and conditional agar/pH paragraph
  accessed_at: '2026-10-21T22:02:48.498901Z'
  support: supports
  summary: The primary supplies seven main batch masses, 1000 ml water, pH 6.5 and
    15.0 g/l agar for the solid branch.
  quote: 1215. BEIJERINCKIA DOEBEREINERAE MEDIUM
  snapshot_sha256: c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76
- evidence_id: historical-raw
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1215
  locator: Historical $.data.medium and $.data.solutions[0], complete recipe/volume/steps
  accessed_at: '2026-10-07T13:18:59.369659Z'
  support: supports
  summary: Exact historical response hash and original October 7 timestamp are recovered.
    Declared volume is 1000 ml and amounts are provider g_l, not a measured final
    volume.
  quote: '"volume": 1000'
  snapshot_sha256: fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 1215 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Catalog supplies source identity and DSMZ link only, not ingredient amounts
    or equivalence of all historical variants.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1215'\
    \ >1215</a></TD>\n\t\t\t\t\t<TD>BEIJERINCKIA DOEBEREINERAE MEDIUM</TD>\n\t\t\t\
    \t\t<TD> 6.5</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\
    \t<TD>false</TD>\n<TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive1215api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1215
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:02:47.965346Z'
  support: context_only
  summary: Current mediadive1215api returned HTTP 503. Exact primary and historical
    raw resolve the material claims; unavailable optional detail does not itself require
    partial completion or establish unseen variants.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1215api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1215
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:03:45.468694Z'
  support: context_only
  summary: Current mediadive1215api_retry returned HTTP 503. Exact primary and historical
    raw resolve the material claims; unavailable optional detail does not itself require
    partial completion or establish unseen variants.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo1215detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1215
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:02:47.727886Z'
  support: context_only
  summary: Current komodo1215detail returned HTTP 403. Exact primary and historical
    raw resolve the material claims; unavailable optional detail does not itself require
    partial completion or establish unseen variants.
  snapshot_sha256: b1261c3c7fdb08cd24acd41c6f9a575cc671ed98f4a458aef38a7b82ce6774f8
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/399/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a8589334c83b122f6e8c1655e2812c0d7e73284d70075e849efbd9076d7793a6
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
- evidence_id: chebi86254
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86254
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:30.289392Z'
  support: supports
  summary: CHEBI:86254 resolves to iron trichloride hexahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 89afba545ad02f24a850933df154af25dee37357b583f82de13866b44f18d683
- evidence_id: chebi86473
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86473
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T22:02:50.000664Z'
  support: supports
  summary: CHEBI:86473 resolves to sodium molybdate heptahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: cd11e1f2b42954c0f7aa44b831d8941d446aa8d71df584a701fd6d36aa657937
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T22:38:48Z'
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
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label":
    "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86254": [{"label": "FeCl3 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86254", "preferred_term":
    "FeCl3 x 6 H2O", "ontology_id": "CHEBI:86254", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86473": [{"label": "Na2MoO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86473", "preferred_term": "Na2MoO4 x 7 H2O", "ontology_id":
    "CHEBI:86473", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml;
    data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:14.429895"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:14.429895"}]}, {"input": "data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/399/history-inventory.json
  locator: All seventeen attached owner claims and scoped historical reports
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Sixteen amount claims match the historical API hash and literal objects;
    the catalog claim matches its separate source/hash. None of that attached evidence
    is present in the generated target. Reports do not replace raw authentication.
  snapshot_sha256: cb49de3cfc8ed53a71976f6d81c66a2d478a172f356df3190ee195c248308400
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Current importer/guarded merger is context only; observed older target
    evidence/preparation omissions do not demonstrate execution of the present guarded
    logic.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Current importer/guarded merger is context only; observed older target
    evidence/preparation omissions do not demonstrate execution of the present guarded
    logic.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:38:48Z'
  support: context_only
  summary: Current importer/guarded merger is context only; observed older target
    evidence/preparation omissions do not demonstrate execution of the present guarded
    logic.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 30 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"KH2PO4\",\n    \"\
    stage\": \"Main provider-declared recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.8\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"KH2PO4 0.80 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.8,\\n \
    \                       \\\"mmol_l\\\": 5.87868,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"This target field has no attached\
    \ amount evidence; externally supported values require evidence-only follow-up.\
    \ Provider declaration is not independent measurement or proof of supplied chemical\
    \ form. Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q2\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"Main provider-declared\
    \ recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.8\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"KH2PO4 0.80 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.8,\\n \
    \                       \\\"mmol_l\\\": 5.87868,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"name\": \"KH2PO4\"\
    ,\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.8\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"KH2PO4 0.80 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.8,\\n \
    \                       \\\"mmol_l\\\": 5.87868,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"name\": \"K2HPO4\"\
    ,\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 0.20 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.14826,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"This target field has no attached\
    \ amount evidence; externally supported values require evidence-only follow-up.\
    \ Provider declaration is not independent measurement or proof of supplied chemical\
    \ form. Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q5\",\n    \"name\": \"K2HPO4\",\n    \"stage\": \"Main provider-declared\
    \ recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 0.20 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.14826,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"name\": \"K2HPO4\"\
    ,\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.2\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"K2HPO4 0.20 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.14826,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"name\": \"MgSO4\
    \ x 7 H2O\",\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\",\n      \"\
    provider_declared_volume_ml\": 1000,\n      \"source_condition\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1215\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.5,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.5,\\n                        \\\"mmol_l\\\": 2.02859,\\n                 \
    \       \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This target field has no attached amount\
    \ evidence; externally supported values require evidence-only follow-up. Provider\
    \ declaration is not independent measurement or proof of supplied chemical form.\
    \ Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"name\": \"MgSO4 x 7 H2O\",\n    \"stage\": \"Main provider-declared\
    \ recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.5\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.5,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.5,\\n                        \\\"mmol_l\\\": 2.02859,\\n                 \
    \       \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"name\": \"MgSO4 x 7 H2O\",\n\
    \    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.5\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.5,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.5,\\n                        \\\"mmol_l\\\": 2.02859,\\n                 \
    \       \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"name\": \"FeCl3 x 6 H2O\",\n\
    \    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"FeCl3 x 6 H2O 0.10 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 82,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.369965,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This target field has no attached amount\
    \ evidence; externally supported values require evidence-only follow-up. Provider\
    \ declaration is not independent measurement or proof of supplied chemical form.\
    \ Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"FeCl3 x 6 H2O\",\n    \"stage\": \"Main provider-declared\
    \ recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"FeCl3 x 6 H2O 0.10 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 82,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.369965,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q12\",\n    \"name\": \"FeCl3 x 6 H2O\",\n\
    \    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"0.1\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"FeCl3 x 6 H2O 0.10 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 82,\\n                        \\\"amount\\\": 0.1,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.1,\\n                        \\\"mmol_l\\\": 0.369965,\\n              \
    \          \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q13\",\n    \"name\": \"CaCl2 x 2 H2O\",\n\
    \    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.05\",\n      \"\
    unit\": \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.05 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.05,\\n                        \\\"mmol_l\\\": 0.340101,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This target field has no attached amount\
    \ evidence; externally supported values require evidence-only follow-up. Provider\
    \ declaration is not independent measurement or proof of supplied chemical form.\
    \ Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"name\": \"CaCl2 x 2 H2O\",\n    \"stage\": \"Main provider-declared\
    \ recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.05\",\n      \"\
    unit\": \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.05 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.05,\\n                        \\\"mmol_l\\\": 0.340101,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"name\": \"CaCl2 x 2 H2O\",\n\
    \    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.05\",\n      \"\
    unit\": \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 0.05 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"\
    compound_id\\\": 7,\\n                        \\\"amount\\\": 0.05,\\n       \
    \                 \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\
    \": 0.05,\\n                        \\\"mmol_l\\\": 0.340101,\\n             \
    \           \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q16\",\n    \"name\": \"Na2MoO4 x 7 H2O\"\
    ,\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.005\",\n     \
    \ \"unit\": \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n     \
    \ \"source_condition\": null\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Na2MoO4 x 7 H2O 5.00 mg\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 7 H2O\\\",\\n                        \\\
    \"compound_id\\\": 950,\\n                        \\\"amount\\\": 5,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.005,\\n                        \\\"mmol_l\\\": 0.0150593,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"This target field has no attached amount\
    \ evidence; externally supported values require evidence-only follow-up. The 5\
    \ mg source amount converts to 0.005 g on the declared 1 L provider basis. Provider\
    \ declaration is not independent measurement or proof of supplied chemical form.\
    \ Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"name\": \"Na2MoO4 x 7 H2O\",\n    \"stage\": \"Main provider-declared\
    \ recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.005\",\n     \
    \ \"unit\": \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n     \
    \ \"source_condition\": null\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Na2MoO4 x 7 H2O 5.00 mg\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 7 H2O\\\",\\n                        \\\
    \"compound_id\\\": 950,\\n                        \\\"amount\\\": 5,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.005,\\n                        \\\"mmol_l\\\": 0.0150593,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. The 5 mg source amount converts to 0.005 g on the declared\
    \ 1 L provider basis. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q18\",\n    \"name\": \"Na2MoO4 x 7 H2O\"\
    ,\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.005\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"desired\": {\n      \"value\": \"0.005\",\n     \
    \ \"unit\": \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n     \
    \ \"source_condition\": null\n    },\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Na2MoO4 x 7 H2O 5.00 mg\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 7 H2O\\\",\\n                        \\\
    \"compound_id\\\": 950,\\n                        \\\"amount\\\": 5,\\n      \
    \                  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.005,\\n                        \\\"mmol_l\\\": 0.0150593,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\n     \
    \ }\n    ],\n    \"interpretation\": \"Matching attached amount evidence exists\
    \ in this owner only. The 5 mg source amount converts to 0.005 g on the declared\
    \ 1 L provider basis. Provider declaration is not independent measurement or proof\
    \ of supplied chemical form. Preserve the agar condition and all exact hydrates.\"\
    \n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"Glucose\",\n    \"\
    stage\": \"Main provider-declared recipe\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"20\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Glucose 20.00 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\
    \": 5,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n    \
    \                    \\\"mmol_l\\\": 111.012,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"This target field has no attached\
    \ amount evidence; externally supported values require evidence-only follow-up.\
    \ Provider declaration is not independent measurement or proof of supplied chemical\
    \ form. Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q20\",\n    \"name\": \"Glucose\",\n    \"stage\": \"Main\
    \ provider-declared recipe\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"20\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Glucose 20.00 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\
    \": 5,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n    \
    \                    \\\"mmol_l\\\": 111.012,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"name\": \"Glucose\"\
    ,\n    \"stage\": \"Main provider-declared recipe\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"20\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Glucose 20.00 g\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\
    \": 5,\\n                        \\\"amount\\\": 20,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n    \
    \                    \\\"mmol_l\\\": 111.012,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"name\": \"Agar\"\
    ,\n    \"stage\": \"Solid branch\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"15\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : \"for solid medium\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Final pH is 6.5. Add 15.0 g/l agar for solid\
    \ media.\",\n        \"snapshot_sha256\": \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\"\
    ,\n        \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"This target field has no attached\
    \ amount evidence; externally supported values require evidence-only follow-up.\
    \ Provider declaration is not independent measurement or proof of supplied chemical\
    \ form. Preserve the agar condition and all exact hydrates.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q23\",\n    \"name\": \"Agar\",\n    \"stage\": \"Solid branch\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"15\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : \"for solid medium\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Final pH is 6.5. Add 15.0 g/l agar for solid\
    \ media.\",\n        \"snapshot_sha256\": \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\"\
    ,\n        \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"name\": \"Agar\"\
    ,\n    \"stage\": \"Solid branch\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"value\": \"15\",\n      \"unit\"\
    : \"G_PER_L\",\n      \"provider_declared_volume_ml\": 1000,\n      \"source_condition\"\
    : \"for solid medium\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary composition/conditional agar paragraph\"\
    ,\n        \"exact_source_quote\": \"Final pH is 6.5. Add 15.0 g/l agar for solid\
    \ media.\",\n        \"snapshot_sha256\": \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\"\
    ,\n        \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached amount evidence\
    \ exists in this owner only. Provider declaration is not independent measurement\
    \ or proof of supplied chemical form. Preserve the agar condition and all exact\
    \ hydrates.\"\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"name\": \"Distilled\
    \ water\",\n    \"stage\": \"Main solvent\",\n    \"decision\": \"add\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.8\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            }\n\
    \          },\n          {\n            \"preferred_term\": \"K2HPO4\",\n    \
    \        \"term\": {\n              \"id\": \"CHEBI:131527\",\n              \"\
    label\": \"dipotassium hydrogen phosphate\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"0.2\",\n              \"unit\": \"G_PER_L\"\n\
    \            },\n            \"mediaingredientmech_chebi_term\": {\n         \
    \     \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium hydrogen\
    \ phosphate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"FeCl3 x 6 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:86254\",\n              \"label\": \"iron trichloride hexahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.1\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86254\",\n              \"label\": \"iron trichloride\
    \ hexahydrate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"CaCl2 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.05\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium\
    \ chloride dihydrate\"\n            }\n          },\n          {\n           \
    \ \"preferred_term\": \"Na2MoO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:86473\",\n              \"label\": \"sodium molybdate heptahydrate\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    0.005\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:86473\",\n\
    \              \"label\": \"sodium molybdate heptahydrate\"\n            }\n \
    \         },\n          {\n            \"preferred_term\": \"Glucose\",\n    \
    \        \"term\": {\n              \"id\": \"CHEBI:17234\",\n              \"\
    label\": \"glucose\"\n            },\n            \"concentration\": {\n     \
    \         \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n          \
    \  },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:17234\",\n              \"label\": \"glucose\"\n            }\n    \
    \      },\n          {\n            \"preferred_term\": \"Agar\",\n          \
    \  \"term\": {\n              \"id\": \"CHEBI:2509\",\n              \"label\"\
    : \"agar\"\n            },\n            \"concentration\": {\n              \"\
    value\": \"15\",\n              \"unit\": \"G_PER_L\"\n            },\n      \
    \      \"notes\": \" (for solid medium)\",\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            }\n          }\n        ]\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.8\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/1215\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 1,\\n                        \\\"compound\\\": \\\"KH2PO4\\\"\
    ,\\n                        \\\"compound_id\\\": 11,\\n                      \
    \  \\\"amount\\\": 0.8,\\n                        \\\"unit\\\": \\\"g\\\",\\n\
    \                        \\\"g_l\\\": 0.8,\\n                        \\\"mmol_l\\\
    \": 5.87868,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[0].concentration\
    \ (KH2PO4) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[0]. Provider\
    \ explicitly reports g_l=0.8; check: 0.8 g * 1 g/g / (1000 ml / 1000 ml per L)\
    \ = 0.8 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"K2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:131527\"\
    ,\n              \"label\": \"dipotassium hydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.2\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.14826,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[1].concentration (K2HPO4) in MediaDive\
    \ medium 1215; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports\
    \ g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive\
    \ medium 1215; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"FeCl3 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86254\"\
    ,\n              \"label\": \"iron trichloride hexahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86254\",\n              \"label\": \"iron trichloride\
    \ hexahydrate\"\n            },\n            \"evidence\": [\n              {\n\
    \                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 82,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.369965,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (FeCl3 x 6 H2O) in\
    \ MediaDive medium 1215; locator=$.data.solutions[0].recipe[3]. Provider explicitly\
    \ reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"CaCl2 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.05\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium\
    \ chloride dihydrate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.05,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n\
    \                        \\\"mmol_l\\\": 0.340101,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[4].concentration (CaCl2 x 2 H2O) in\
    \ MediaDive medium 1215; locator=$.data.solutions[0].recipe[4]. Provider explicitly\
    \ reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na2MoO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86473\"\
    ,\n              \"label\": \"sodium molybdate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.005\",\n     \
    \         \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86473\",\n              \"label\": \"sodium\
    \ molybdate heptahydrate\"\n            },\n            \"evidence\": [\n    \
    \          {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"Na2MoO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 950,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0150593,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[5].concentration (Na2MoO4 x 7 H2O)\
    \ in MediaDive medium 1215; locator=$.data.solutions[0].recipe[5]. Provider explicitly\
    \ reports g_l=0.005; check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n        \
    \    },\n            \"evidence\": [\n              {\n                \"reference\"\
    : \"https://mediadive.dsmz.de/rest/medium/1215\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 7,\\n                        \\\"compound\\\": \\\"Glucose\\\
    \",\\n                        \\\"compound_id\\\": 5,\\n                     \
    \   \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\"g\\\",\\n\
    \                        \\\"g_l\\\": 20,\\n                        \\\"mmol_l\\\
    \": 111.012,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[6].concentration\
    \ (Glucose) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[6]. Provider\
    \ explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 20 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \" (for solid medium)\",\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            },\n            \"evidence\": [\n\
    \              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 9,\\n                      \
    \  \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n                \"explanation\": \"Concentration evidence\
    \ for ingredients[7].concentration (Agar) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[8].\
    \ Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml\
    \ per L) = 15 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\
    \ KOMODO accession 1215 is mapped to the same DSMZ accession by https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;\
    \ mapping response SHA256=d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a.\
    \ The mapping supports identity only, not ingredient quantities or variants.\"\
    \n              }\n            ]\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"KH2PO4\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium dihydrogen\
    \ phosphate\"\n            },\n            \"concentration\": {\n            \
    \  \"value\": \"0.8\",\n              \"unit\": \"G_PER_L\"\n            },\n\
    \            \"mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"evidence\": [\n              {\n                \"reference\":\
    \ \"https://mediadive.dsmz.de/rest/medium/1215\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 1,\\n                        \\\"compound\\\": \\\"KH2PO4\\\"\
    ,\\n                        \\\"compound_id\\\": 11,\\n                      \
    \  \\\"amount\\\": 0.8,\\n                        \\\"unit\\\": \\\"g\\\",\\n\
    \                        \\\"g_l\\\": 0.8,\\n                        \\\"mmol_l\\\
    \": 5.87868,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[0].concentration\
    \ (KH2PO4) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[0]. Provider\
    \ explicitly reports g_l=0.8; check: 0.8 g * 1 g/g / (1000 ml / 1000 ml per L)\
    \ = 0.8 g/L. This supports the provider-declared main-recipe concentration, not\
    \ an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"K2HPO4\",\n            \"term\": {\n              \"id\": \"CHEBI:131527\"\
    ,\n              \"label\": \"dipotassium hydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.2\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 2,\\n                      \
    \  \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.14826,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[1].concentration (K2HPO4) in MediaDive\
    \ medium 1215; locator=$.data.solutions[0].recipe[1]. Provider explicitly reports\
    \ g_l=0.2; check: 0.2 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.2 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"MgSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:31795\"\
    ,\n              \"label\": \"magnesium sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.5\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium\
    \ sulfate heptahydrate\"\n            },\n            \"evidence\": [\n      \
    \        {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 3,\\n                      \
    \  \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.5,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.5,\\n  \
    \                      \\\"mmol_l\\\": 2.02859,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n                \"explanation\": \"\
    Concentration evidence for ingredients[2].concentration (MgSO4 x 7 H2O) in MediaDive\
    \ medium 1215; locator=$.data.solutions[0].recipe[2]. Provider explicitly reports\
    \ g_l=0.5; check: 0.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.5 g/L. This supports\
    \ the provider-declared main-recipe concentration, not an independently measured\
    \ final volume, a stock composition, or a downstream assay dilution. Water alone\
    \ does not establish final volume. Exact source ingredient labels/forms are matched;\
    \ secondary ontology mappings are not validated by this evidence. Additional exact\
    \ value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"FeCl3 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86254\"\
    ,\n              \"label\": \"iron trichloride hexahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.1\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86254\",\n              \"label\": \"iron trichloride\
    \ hexahydrate\"\n            },\n            \"evidence\": [\n              {\n\
    \                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 4,\\n                      \
    \  \\\"compound\\\": \\\"FeCl3 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 82,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.1,\\n \
    \                       \\\"mmol_l\\\": 0.369965,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[3].concentration (FeCl3 x 6 H2O) in\
    \ MediaDive medium 1215; locator=$.data.solutions[0].recipe[3]. Provider explicitly\
    \ reports g_l=0.1; check: 0.1 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.1 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"CaCl2 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86158\"\
    ,\n              \"label\": \"calcium chloride dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.05\",\n       \
    \       \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86158\",\n              \"label\": \"calcium\
    \ chloride dihydrate\"\n            },\n            \"evidence\": [\n        \
    \      {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 5,\\n                      \
    \  \\\"compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.05,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.05,\\n\
    \                        \\\"mmol_l\\\": 0.340101,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[4].concentration (CaCl2 x 2 H2O) in\
    \ MediaDive medium 1215; locator=$.data.solutions[0].recipe[4]. Provider explicitly\
    \ reports g_l=0.05; check: 0.05 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.05 g/L.\
    \ This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Na2MoO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:86473\"\
    ,\n              \"label\": \"sodium molybdate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.005\",\n     \
    \         \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:86473\",\n              \"label\": \"sodium\
    \ molybdate heptahydrate\"\n            },\n            \"evidence\": [\n    \
    \          {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 6,\\n                      \
    \  \\\"compound\\\": \\\"Na2MoO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 950,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0150593,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n                \"explanation\"\
    : \"Concentration evidence for ingredients[5].concentration (Na2MoO4 x 7 H2O)\
    \ in MediaDive medium 1215; locator=$.data.solutions[0].recipe[5]. Provider explicitly\
    \ reports g_l=0.005; check: 5 mg * 0.001 g/mg / (1000 ml / 1000 ml per L) = 0.005\
    \ g/L. This supports the provider-declared main-recipe concentration, not an independently\
    \ measured final volume, a stock composition, or a downstream assay dilution.\
    \ Water alone does not establish final volume. Exact source ingredient labels/forms\
    \ are matched; secondary ontology mappings are not validated by this evidence.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Glucose\",\n            \"term\": {\n              \"id\": \"CHEBI:17234\"\
    ,\n              \"label\": \"glucose\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"20\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"mediaingredientmech_chebi_term\": {\n          \
    \    \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n        \
    \    },\n            \"evidence\": [\n              {\n                \"reference\"\
    : \"https://mediadive.dsmz.de/rest/medium/1215\",\n                \"supports\"\
    : \"SUPPORT\",\n                \"snippet\": \"{\\n                        \\\"\
    recipe_order\\\": 7,\\n                        \\\"compound\\\": \\\"Glucose\\\
    \",\\n                        \\\"compound_id\\\": 5,\\n                     \
    \   \\\"amount\\\": 20,\\n                        \\\"unit\\\": \\\"g\\\",\\n\
    \                        \\\"g_l\\\": 20,\\n                        \\\"mmol_l\\\
    \": 111.012,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n                \"explanation\": \"Concentration evidence for ingredients[6].concentration\
    \ (Glucose) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[6]. Provider\
    \ explicitly reports g_l=20; check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) =\
    \ 20 g/L. This supports the provider-declared main-recipe concentration, not an\
    \ independently measured final volume, a stock composition, or a downstream assay\
    \ dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved\
    \ 2026-10-07T13:18:59.369659+00:00; response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          },\n          {\n            \"preferred_term\"\
    : \"Agar\",\n            \"term\": {\n              \"id\": \"CHEBI:2509\",\n\
    \              \"label\": \"agar\"\n            },\n            \"concentration\"\
    : {\n              \"value\": \"15\",\n              \"unit\": \"G_PER_L\"\n \
    \           },\n            \"notes\": \" (for solid medium)\",\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            },\n            \"evidence\": [\n\
    \              {\n                \"reference\": \"https://mediadive.dsmz.de/rest/medium/1215\"\
    ,\n                \"supports\": \"SUPPORT\",\n                \"snippet\": \"\
    {\\n                        \\\"recipe_order\\\": 9,\\n                      \
    \  \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"condition\\\": \\\"for solid medium\\\",\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n                \"explanation\": \"Concentration evidence\
    \ for ingredients[7].concentration (Agar) in MediaDive medium 1215; locator=$.data.solutions[0].recipe[8].\
    \ Provider explicitly reports g_l=15; check: 15 g * 1 g/g / (1000 ml / 1000 ml\
    \ per L) = 15 g/L. This supports the provider-declared main-recipe concentration,\
    \ not an independently measured final volume, a stock composition, or a downstream\
    \ assay dilution. Water alone does not establish final volume. Exact source ingredient\
    \ labels/forms are matched; secondary ontology mappings are not validated by this\
    \ evidence. Source condition 'for solid medium' matches local physical_state=SOLID_AGAR.\
    \ Additional exact value at $.data.solutions[0].volume (ml): 1000. Retrieved 2026-10-07T13:18:59.369659+00:00;\
    \ response SHA256=fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f.\"\
    \n              }\n            ]\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 1000,\n      \"source_unit\": \"ml\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1215\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Primary final table row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\"\
    ,\n        \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      },\n      {\n        \"source_key\": \"mediadive1215Historical\",\n  \
    \      \"source_url\": \"https://mediadive.dsmz.de/rest/medium/1215\",\n     \
    \   \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 1000,\\n     \
    \                   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"fae7aaa71e71a35ec36f9377dea50755a59bce785ffd9e2b11d1f4fcfa4fdc0f\"\
    \n      }\n    ],\n    \"interpretation\": \"Every layer omits the source solvent\
    \ input. Add it in the appropriate preparation scope; do not turn water volume\
    \ into mass or independently measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q26\",\n    \"name\": \"Final pH\",\n    \"stage\": \"Main medium\",\n   \
    \ \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      }\n \
    \   ],\n    \"desired\": {\n      \"value\": 6.5\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1215\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\",\n       \
    \ \"source_locator\": \"Final primary paragraph\",\n        \"exact_source_quote\"\
    : \"Final pH is 6.5. Add 15.0 g/l agar for solid media.\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      }\n    ],\n    \"interpretation\": \"All stored pH values agree. Ingredient-specific\
    \ evidence does not authenticate this separate field automatically.\"\n  },\n\
    \  {\n    \"decision_id\": \"q27\",\n    \"name\": \"Solid-branch agar qualifier\"\
    ,\n    \"stage\": \"Optional branch\",\n    \"decision\": \"evidence_only\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \" (for\
    \ solid medium)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \" (for\
    \ solid medium)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \" (for\
    \ solid medium)\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"physical_state\",\n        \"stored\": \"SOLID_AGAR\"\
    \n      }\n    ],\n    \"desired\": {\n      \"agar_rate_g_per_l\": 15,\n    \
    \  \"condition\": \"for solid media\"\n    },\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Final primary paragraph\",\n        \"exact_source_quote\"\
    : \"Final pH is 6.5. Add 15.0 g/l agar for solid media.\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      }\n    ],\n    \"interpretation\": \"All ingredient notes already retain\
    \ the solid-medium condition. SOLID_AGAR represents that branch; the source also\
    \ permits the no-agar formulation.\"\n  },\n  {\n    \"decision_id\": \"q28\"\
    ,\n    \"name\": \"Existing DSMZ preparation\",\n    \"stage\": \"DSMZ maintained\
    \ owner\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Final pH is 6.5. Add 15.0 g/l agar for solid media.\"\n      }\n    ],\n \
    \   \"desired\": {\n      \"source_text\": \"Final pH is 6.5. Add 15.0 g/l agar\
    \ for solid media.\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Final primary paragraph\",\n        \"exact_source_quote\"\
    : \"Final pH is 6.5. Add 15.0 g/l agar for solid media.\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      }\n    ],\n    \"interpretation\": \"The DSMZ owner already retains pH\
    \ and conditional agar instructions; preserve its preparation and attached amount\
    \ evidence.\"\n  },\n  {\n    \"decision_id\": \"q29\",\n    \"name\": \"Missing\
    \ preparation context\",\n    \"stage\": \"Target and KOMODO owner\",\n    \"\
    decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps\",\n        \"stored\": null\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_text\": \"Final pH is 6.5.\
    \ Add 15.0 g/l agar for solid media.\"\n    },\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Final primary paragraph\",\n        \"exact_source_quote\"\
    : \"Final pH is 6.5. Add 15.0 g/l agar for solid media.\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      }\n    ],\n    \"interpretation\": \"Only these two layers omit the preparation\
    \ paragraph. This does not mean their existing pH or agar qualifier is absent.\"\
    \n  },\n  {\n    \"decision_id\": \"q30\",\n    \"name\": \"Unspecified preparation/growth\
    \ numbers\",\n    \"stage\": \"Whole medium\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"desired\": {\n      \"cycle\": null,\n      \"titrant_dose_strength\"\
    : null,\n      \"cultivation_temperature_duration\": null,\n      \"measured_final_volume\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1215\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1215.pdf\"\
    ,\n        \"source_locator\": \"Final primary paragraph\",\n        \"exact_source_quote\"\
    : \"Final pH is 6.5. Add 15.0 g/l agar for solid media.\",\n        \"snapshot_sha256\"\
    : \"c5668f79f925b1a8e98b97ff86bdefa08965ea8516b8dd7d394cdf3a0e791e76\",\n    \
    \    \"parsed_text_sha256\": \"785d296546cee9ddbe0ab371af60b1533b7e7d38e6544f3f3e9ae90ad60a6d13\"\
    \n      }\n    ],\n    \"interpretation\": \"No numerical sterilization cycle,\
    \ titrant specification or growth condition is given. The provider volume declaration\
    \ remains distinct from a measured final volume.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '8 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 8/8 primary
    and 8/8 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi17234
  - chebi2509
  - chebi31795
  - chebi63036
  - chebi86158
  - chebi86254
  - chebi86473
  details: 'Instance coverage on a 0–100 percent scale, denominator 8: primary 100.00%;
    secondary 100.00%. These are linkage metrics, not correctness scores. Missing
    optional links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 24 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Exact 1215 accession and owner relationship
  outcome: supported
  summary: Exact catalog, primary title, historical medium metadata and reciprocal
    maintained relationships establish the source identity. Formula fingerprints alone
    do not establish equivalence. No organism-specific growth or taxonomy mapping
    is inferred from the title.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - catalog
  - historical-raw
- assessment_id: forms
  area: grounding
  topic: Source chemical forms and generic glucose
  outcome: supported
  summary: KH2PO4/K2HPO4 and the explicit Mg heptahydrate, Fe hexahydrate, Ca dihydrate
    and sodium molybdate heptahydrate agree with asserted names/formulae. Preserve
    the unusual heptahydrate rather than replacing it with a common dihydrate. Generic
    glucose agrees with the generic term; its DL synonym does not prove a racemate
    was supplied. The CHEBI:131527 trihydrate synonym does not establish hydration
    absent from the source. Agar is a complex solidifying material.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - primary
  - chebi131527
  - chebi17234
  - chebi2509
  - chebi31795
  - chebi63036
  - chebi86158
  - chebi86254
  - chebi86473
- assessment_id: layer-evidence
  area: evidence
  topic: Owner authentication and generated lag
  outcome: concern
  summary: All sixteen maintained ingredient claims authenticate narrowly to their
    own fields and provider normalization. The generated target lacks these claims,
    references and later concentration history. The catalog identity claim cannot
    support quantities or oxygen physiology.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - historical-raw
  - history-inventory
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Source solvent and preserved conditional agar
  outcome: concern
  summary: The 1000 ml solvent is absent in all layers. Only DSMZ owner retains preparation
    prose, while pH 6.5 and conditional agar notes already exist in all layers. Source
    supplies no numerical cycle or incubation conditions.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - primary
  - quantity-inventory
  - owner-1
- assessment_id: classification
  area: scope
  topic: Defined basal medium and solid branch
  outcome: supported
  summary: The listed chemical basal composition supports the defined classification;
    agar is an optional solidifying branch already qualified locally. No nitrogen
    fixation, oxygen physiology or species growth is inferred from the name or KOMODO
    flags.
  target_ids:
  - CultureMech:003966
  evidence_ids:
  - record
  - primary
  - catalog
findings:
- finding_id: f1
  issue_key: culturemech.003966.missing-solvent-and-preparation-context
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Solvent and layer-specific preparation are incomplete
  description: All layers omit 1000 ml source water; target and KOMODO lack preparation
    retained by DSMZ. Existing pH and agar condition are already correct and must
    be preserved.
  target_ids:
  - CultureMech:003966
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - primary
  - quantity-inventory
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech.003966.generated-evidence-lag
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits authenticated owner evidence
  description: The sixteen attached owner amount claims and catalog identity claim
    are absent from the target. This observed difference is not proof of universal
    loss by the current guarded merger.
  target_ids:
  - CultureMech:003966
  field_paths:
  - ingredients[*].evidence
  - evidence
  - references
  - curation_history
  evidence_ids:
  - history-inventory
  - historical-raw
  - record
  - owner-0
  - owner-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
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
  issue_key: culturemech.003966.malformed-import-times
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO history retains malformed and naive times
  description: The .fZ import timestamp and timezone-naive resolver timestamp occur
    in target and KOMODO history. Exact replacements are not established.
  target_ids:
  - CultureMech:003966
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
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
  description: Restore exact solvent input and missing preparation ownership without
    duplicating the DSMZ instruction or inferring a numerical cycle.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
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
  description: Preserve authenticated owner evidence and later history, verify source
    formulation compatibility and regenerate only via the supported guarded path after
    authorization.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml
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
  description: Preserve original events and append only an independently supported
    clarification.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003966
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml
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
- Current mediadive1215api returned HTTP 503. Exact primary and historical raw resolve
  the material claims; unavailable optional detail does not itself require partial
  completion or establish unseen variants.
- Current mediadive1215api_retry returned HTTP 503. Exact primary and historical raw
  resolve the material claims; unavailable optional detail does not itself require
  partial completion or establish unseen variants.
- Current komodo1215detail returned HTTP 403. Exact primary and historical raw resolve
  the material claims; unavailable optional detail does not itself require partial
  completion or establish unseen variants.
- Required current primary and historical amount sources are available. Optional current
  API/detail failures remain preserved without forcing partial completion. No complete
  historical-variant equivalence, measured final volume or growth condition is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-040
- generated-medium
```
