# Source and formulation review: beijerinckia_medium (CultureMech:003822)

- Review: 20261021T224024Z-culturemech-003822-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T22:32:21Z
- Finished UTC: 2026-10-21T22:40:24Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated DSMZ/KOMODO 111 target predates the source-specific repair already present in both maintained owners. Those owners correctly distinguish 950 ml basal water and 10 g glucose prepared separately in 50 ml water, retain qualified provider rates, and authenticate 27 narrow claims. The target still has the withdrawn 10.5263 g/L glucose rate and omits the stock, solvent inputs, preparation, qualifications and evidence. No 200 g/L stock strength, 10 g/L final glucose or measured 1 L volume is inferred.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 400; batch 040 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-nine task batches contain 390 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 393 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003822 | data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml | generated | beijerinckia_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003822 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003822 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/400/strict.tsv |
| validate-terms | passed | True | CultureMech:003822 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003822 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003822 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive111api | unavailable | False | CultureMech:003822 | Current mediadive111api returned HTTP 503. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred. |
| Exact source content access: mediadive111api_retry | unavailable | False | CultureMech:003822 | Current mediadive111api_retry returned HTTP 503. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred. |
| Exact source content access: komodo111detail | unavailable | False | CultureMech:003822 | Current komodo111detail returned HTTP 403. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003822.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003822.

40 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Glucose",
    "stage": "Stale generated main ingredient",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10.5263",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount_g": 10,
      "source_water_input_ml": 50,
      "stock_concentration": null,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Main table glucose row",
        "exact_source_quote": "Glucose 10.0 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Separate glucose preparation",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.5263,\n                        \"mmol_l\": 58.4276,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target rate divides glucose mass by the unrelated 950 ml basal-water field. Both maintained owners already withdraw this rate and retain the supported batch amount in the separate preparation. Do not reinstate it or infer 200 g/L stock or 10 g/L final glucose."
  },
  {
    "decision_id": "q2",
    "name": "K2HPO4",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.842105",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.842105",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.8,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 2",
        "exact_source_quote": "K2HPO4 0.8 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.842105,\n                        \"mmol_l\": 4.83479,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q3",
    "name": "K2HPO4",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.842105",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[0].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "Source batch input: 0.8 g. The retained 0.842105 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[0].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.842105",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.8,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 2",
        "exact_source_quote": "K2HPO4 0.8 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.842105,\n                        \"mmol_l\": 4.83479,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q4",
    "name": "K2HPO4",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.842105",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[0].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "Source batch input: 0.8 g. The retained 0.842105 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[0].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.842105",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.8,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 2",
        "exact_source_quote": "K2HPO4 0.8 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.842105,\n                        \"mmol_l\": 4.83479,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q5",
    "name": "KH2PO4",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.210526",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.2,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 3",
        "exact_source_quote": "KH2PO4 0.2 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210526,\n                        \"mmol_l\": 1.54701,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q6",
    "name": "KH2PO4",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.210526",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[1].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "Source batch input: 0.2 g. The retained 0.210526 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[1].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.2,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 3",
        "exact_source_quote": "KH2PO4 0.2 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210526,\n                        \"mmol_l\": 1.54701,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q7",
    "name": "KH2PO4",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.210526",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[1].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "Source batch input: 0.2 g. The retained 0.210526 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[1].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.2,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 3",
        "exact_source_quote": "KH2PO4 0.2 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.210526,\n                        \"mmol_l\": 1.54701,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q8",
    "name": "MgSO4 x 7 H2O",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.105263",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.105263",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.1,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 4",
        "exact_source_quote": "MgSO4 x 7 H2O 0.1 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.105263,\n                        \"mmol_l\": 0.427073,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q9",
    "name": "MgSO4 x 7 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.105263",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[2].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Source batch input: 0.1 g. The retained 0.105263 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[2].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.105263",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.1,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 4",
        "exact_source_quote": "MgSO4 x 7 H2O 0.1 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.105263,\n                        \"mmol_l\": 0.427073,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q10",
    "name": "MgSO4 x 7 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.105263",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[2].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[2].notes",
        "stored": "Source batch input: 0.1 g. The retained 0.105263 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[2].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.105263",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 0.1,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 4",
        "exact_source_quote": "MgSO4 x 7 H2O 0.1 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.105263,\n                        \"mmol_l\": 0.427073,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q11",
    "name": "FeSO4 x 7 H2O",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0210526",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.0210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 20,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 5",
        "exact_source_quote": "FeSO4 x 7 H2O 20.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0210526,\n                        \"mmol_l\": 0.0757248,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q12",
    "name": "FeSO4 x 7 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0210526",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[3].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Source batch input: 20 mg. The retained 0.0210526 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[3].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.0210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 20,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 5",
        "exact_source_quote": "FeSO4 x 7 H2O 20.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0210526,\n                        \"mmol_l\": 0.0757248,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q13",
    "name": "FeSO4 x 7 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.0210526",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[3].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[3].notes",
        "stored": "Source batch input: 20 mg. The retained 0.0210526 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[3].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.0210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 20,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 5",
        "exact_source_quote": "FeSO4 x 7 H2O 20.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0210526,\n                        \"mmol_l\": 0.0757248,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q14",
    "name": "MnSO4 x 6 H2O",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.00210526",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 2,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 6",
        "exact_source_quote": "MnSO4 x 6 H2O 2.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MnSO4 x 6 H2O\",\n                        \"compound_id\": 216,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00210526,\n                        \"mmol_l\": 0.00812551,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q15",
    "name": "MnSO4 x 6 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.00210526",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[4].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Source batch input: 2 mg. The retained 0.00210526 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[4].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 2,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 6",
        "exact_source_quote": "MnSO4 x 6 H2O 2.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MnSO4 x 6 H2O\",\n                        \"compound_id\": 216,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00210526,\n                        \"mmol_l\": 0.00812551,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q16",
    "name": "MnSO4 x 6 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.00210526",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[4].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[4].notes",
        "stored": "Source batch input: 2 mg. The retained 0.00210526 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[4].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00210526",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 2,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 6",
        "exact_source_quote": "MnSO4 x 6 H2O 2.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MnSO4 x 6 H2O\",\n                        \"compound_id\": 216,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00210526,\n                        \"mmol_l\": 0.00812551,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q17",
    "name": "ZnSO4 x 6 H2O",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.00526316",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00526316",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 5,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 7",
        "exact_source_quote": "ZnSO4 x 6 H2O 5.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 6 H2O\",\n                        \"compound_id\": 217,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00526316,\n                        \"mmol_l\": 0.0195256,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q18",
    "name": "ZnSO4 x 6 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.00526316",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[5].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Source batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[5].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00526316",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 5,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 7",
        "exact_source_quote": "ZnSO4 x 6 H2O 5.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 6 H2O\",\n                        \"compound_id\": 217,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00526316,\n                        \"mmol_l\": 0.0195256,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q19",
    "name": "ZnSO4 x 6 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.00526316",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[5].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[5].notes",
        "stored": "Source batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[5].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00526316",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 5,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 7",
        "exact_source_quote": "ZnSO4 x 6 H2O 5.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 6 H2O\",\n                        \"compound_id\": 217,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00526316,\n                        \"mmol_l\": 0.0195256,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q20",
    "name": "CuSO4 x 6 H2O",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00421053",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00421053",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 4,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 8",
        "exact_source_quote": "CuSO4 x 6 H2O 4.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuSO4 x 6 H2O\",\n                        \"compound_id\": 218,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00421053,\n                        \"mmol_l\": 0.0157285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q21",
    "name": "CuSO4 x 6 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.00421053",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[6].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Source batch input: 4 mg. The retained 0.00421053 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[6].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00421053",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 4,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 8",
        "exact_source_quote": "CuSO4 x 6 H2O 4.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuSO4 x 6 H2O\",\n                        \"compound_id\": 218,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00421053,\n                        \"mmol_l\": 0.0157285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q22",
    "name": "CuSO4 x 6 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.00421053",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[6].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[6].notes",
        "stored": "Source batch input: 4 mg. The retained 0.00421053 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[6].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00421053",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 4,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 8",
        "exact_source_quote": "CuSO4 x 6 H2O 4.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CuSO4 x 6 H2O\",\n                        \"compound_id\": 218,\n                        \"amount\": 4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00421053,\n                        \"mmol_l\": 0.0157285,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q23",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.00526316",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00526316",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 5,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 9",
        "exact_source_quote": "Na2MoO4 x 2 H2O 5.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00526316,\n                        \"mmol_l\": 0.0217531,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q24",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00526316",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[7].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Source batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[7].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00526316",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 5,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 9",
        "exact_source_quote": "Na2MoO4 x 2 H2O 5.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00526316,\n                        \"mmol_l\": 0.0217531,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q25",
    "name": "Na2MoO4 x 2 H2O",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.00526316",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[7].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[7].notes",
        "stored": "Source batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[7].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "0.00526316",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 5,
      "source_unit": "mg",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 9",
        "exact_source_quote": "Na2MoO4 x 2 H2O 5.0 mg",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00526316,\n                        \"mmol_l\": 0.0217531,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q26",
    "name": "Agar",
    "stage": "Generated provider-normalized basal row",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "15.7895",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "15.7895",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 15,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 10",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15.7895,\n                        \"mmol_l\": 46.9464,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target numeral agrees with the provider table but lacks its preparation-stage qualification and attached evidence. Preserve the batch input and 950 ml normalization limitation, not a claimed final-medium concentration."
  },
  {
    "decision_id": "q27",
    "name": "Agar",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15.7895",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[8].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "Source batch input: 15 g. The retained 15.7895 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[8].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "15.7895",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 15,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 10",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15.7895,\n                        \"mmol_l\": 46.9464,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q28",
    "name": "Agar",
    "stage": "Maintained qualified basal row",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "15.7895",
          "unit": "G_PER_L"
        },
        "evidence_field_path": "ingredients[8].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[8].notes",
        "stored": "Source batch input: 15 g. The retained 15.7895 g/L is the provider-declared rate normalized to its 950 ml main-preparation field, not an independently verified concentration after adding the separately prepared glucose. No final volume is inferred.",
        "evidence_field_path": "ingredients[8].evidence"
      }
    ],
    "desired": {
      "provider_rate_g_per_l": "15.7895",
      "provider_volume_field_ml": 950,
      "source_batch_amount": 15,
      "source_unit": "g",
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal table row 10",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15.7895,\n                        \"mmol_l\": 46.9464,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "This exact owner field has attached authenticated evidence and explicitly preserves the source batch input and denominator limitation. Verification applies to this qualified provider declaration only, not final-medium concentration or secondary grounding."
  },
  {
    "decision_id": "q29",
    "name": "Basal water",
    "stage": "Generated target missing input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "Glucose",
            "term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            },
            "concentration": {
              "value": "10.5263",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:17234",
              "label": "glucose"
            }
          },
          {
            "preferred_term": "K2HPO4",
            "term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            },
            "concentration": {
              "value": "0.842105",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131527",
              "label": "dipotassium hydrogen phosphate"
            }
          },
          {
            "preferred_term": "KH2PO4",
            "term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            },
            "concentration": {
              "value": "0.210526",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:63036",
              "label": "potassium dihydrogen phosphate"
            }
          },
          {
            "preferred_term": "MgSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.105263",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:31795",
              "label": "magnesium sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "FeSO4 x 7 H2O",
            "term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            },
            "concentration": {
              "value": "0.0210526",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75836",
              "label": "iron(2+) sulfate heptahydrate"
            }
          },
          {
            "preferred_term": "MnSO4 x 6 H2O",
            "term": {
              "id": "CHEBI:131523",
              "label": "manganese(II) sulfate hexahydrate"
            },
            "concentration": {
              "value": "0.00210526",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:131523",
              "label": "manganese(II) sulfate hexahydrate"
            }
          },
          {
            "preferred_term": "ZnSO4 x 6 H2O",
            "term": {
              "id": "CHEBI:132762",
              "label": "zinc sulfate hexahydrate"
            },
            "concentration": {
              "value": "0.00526316",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132762",
              "label": "zinc sulfate hexahydrate"
            }
          },
          {
            "preferred_term": "CuSO4 x 6 H2O",
            "term": {
              "id": "CHEBI:91246",
              "label": "copper(II) sulfate hexahydrate"
            },
            "concentration": {
              "value": "0.00421053",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91246",
              "label": "copper(II) sulfate hexahydrate"
            }
          },
          {
            "preferred_term": "Na2MoO4 x 2 H2O",
            "term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            },
            "concentration": {
              "value": "0.00526316",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:75213",
              "label": "sodium molybdate dihydrate"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "15.7895",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          }
        ]
      }
    ],
    "desired": {
      "source_amount_ml": 950,
      "representation": "0.95 L water input; not final-volume makeup"
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal solvent row",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "The target lacks the solvent; both maintained owners already store and authenticate this exact input."
  },
  {
    "decision_id": "q30",
    "name": "Basal distilled water",
    "stage": "Maintained basal input",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.95",
          "unit": "L"
        },
        "evidence_field_path": "ingredients[9].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "950 ml distilled-water input per basal batch, not a final-volume makeup instruction.",
        "evidence_field_path": "ingredients[9].evidence"
      }
    ],
    "desired": {
      "value": "0.95",
      "unit": "L",
      "source_amount_ml": 950
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal solvent row",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "Attached evidence supports 950 ml / 1000 = 0.95 L as input only. The owner expressly denies a final-volume makeup instruction."
  },
  {
    "decision_id": "q31",
    "name": "Glucose batch amount",
    "stage": "Maintained separate preparation",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].composition[0].notes",
        "stored": "Source batch input: 10 g glucose in 50 ml H2O, sterilized separately and mixed after cooling. The former 10.5263 g/L divides by the unrelated 950 ml basal-water input and is withdrawn. No 200 g/L stock strength or 10 g/L final-medium concentration is asserted: neither final volume is specified.",
        "evidence_field_path": "solutions[0].composition[0].evidence"
      }
    ],
    "desired": {
      "source_batch_amount_g": 10,
      "source_water_input_ml": 50,
      "numeric_stock_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Separate preparation",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.5263,\n                        \"mmol_l\": 58.4276,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "Attached object and additional preparation excerpt authenticate the withdrawal and batch-mass note. Historical explanations are preserved as superseded where their stage differs, not silently treated as current final concentration."
  },
  {
    "decision_id": "q32",
    "name": "Glucose water",
    "stage": "Maintained separate preparation",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "0.05",
          "unit": "L"
        },
        "evidence_field_path": "solutions[0].composition[1].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].composition[1].notes",
        "stored": "50 ml H2O input for the separately sterilized glucose; water purity and final stock volume are not specified.",
        "evidence_field_path": "solutions[0].composition[1].evidence"
      }
    ],
    "desired": {
      "value": "0.05",
      "unit": "L",
      "source_amount_ml": 50
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Separate glucose preparation",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "50 ml / 1000 = 0.05 L water input is authenticated. H2O alone does not prove distilled purity, final stock volume or a per-liter dose."
  },
  {
    "decision_id": "q33",
    "name": "Retained preparation qualifications",
    "stage": "Maintained whole record and stock",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "notes",
        "stored": "Source: KOMODO ModelSEED &#124; ID: 111 &#124; DSMZ Medium: 111 (mediadive.medium:111) &#124; Aerobic: No\n\nPreparation scope: basal input is 950 ml distilled water plus the listed salts and agar; glucose (10 g in 50 ml H2O) is sterilized separately and mixed after cooling. The retained basal g/L values are provider-reported normalizations, not final-medium concentrations. The two water inputs do not establish a measured 1 L final volume. Historical import annotations and ontology mappings are retained, not revalidated.",
        "evidence_field_path": "evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "evidence_field_path": "evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].notes",
        "stored": "Mix the separately prepared glucose with the cooled basal preparation. The 50 ml is water input, not a measured stock volume or a per-liter dose; no numeric stock addition concentration is asserted.",
        "evidence_field_path": "evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "evidence_field_path": "evidence"
      }
    ],
    "desired": {
      "pH": 6.5,
      "glucose_g": 10,
      "glucose_water_ml": 50,
      "mixing": "after cooling",
      "no_final_volume_inference": true
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary preparation sentence",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal input",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      }
    ],
    "interpretation": "Matching attached record-level evidence explicitly supports these named fields. Preserve the existing repair; numerical stock dose, sterilization method/cycle and final volumes remain unspecified."
  },
  {
    "decision_id": "q34",
    "name": "Basal distilled water",
    "stage": "Maintained basal input",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.95",
          "unit": "L"
        },
        "evidence_field_path": "ingredients[9].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ingredients[9].notes",
        "stored": "950 ml distilled-water input per basal batch, not a final-volume makeup instruction.",
        "evidence_field_path": "ingredients[9].evidence"
      }
    ],
    "desired": {
      "value": "0.95",
      "unit": "L",
      "source_amount_ml": 950
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal solvent row",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 950,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "Attached evidence supports 950 ml / 1000 = 0.95 L as input only. The owner expressly denies a final-volume makeup instruction."
  },
  {
    "decision_id": "q35",
    "name": "Glucose batch amount",
    "stage": "Maintained separate preparation",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].composition[0].notes",
        "stored": "Source batch input: 10 g glucose in 50 ml H2O, sterilized separately and mixed after cooling. The former 10.5263 g/L divides by the unrelated 950 ml basal-water input and is withdrawn. No 200 g/L stock strength or 10 g/L final-medium concentration is asserted: neither final volume is specified.",
        "evidence_field_path": "solutions[0].composition[0].evidence"
      }
    ],
    "desired": {
      "source_batch_amount_g": 10,
      "source_water_input_ml": 50,
      "numeric_stock_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Separate preparation",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.5263,\n                        \"mmol_l\": 58.4276,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "Attached object and additional preparation excerpt authenticate the withdrawal and batch-mass note. Historical explanations are preserved as superseded where their stage differs, not silently treated as current final concentration."
  },
  {
    "decision_id": "q36",
    "name": "Glucose water",
    "stage": "Maintained separate preparation",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "0.05",
          "unit": "L"
        },
        "evidence_field_path": "solutions[0].composition[1].evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].composition[1].notes",
        "stored": "50 ml H2O input for the separately sterilized glucose; water purity and final stock volume are not specified.",
        "evidence_field_path": "solutions[0].composition[1].evidence"
      }
    ],
    "desired": {
      "value": "0.05",
      "unit": "L",
      "source_amount_ml": 50
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Separate glucose preparation",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      }
    ],
    "interpretation": "50 ml / 1000 = 0.05 L water input is authenticated. H2O alone does not prove distilled purity, final stock volume or a per-liter dose."
  },
  {
    "decision_id": "q37",
    "name": "Retained preparation qualifications",
    "stage": "Maintained whole record and stock",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "notes",
        "stored": "Source: DSMZ &#124; Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\n\nPreparation scope: basal input is 950 ml distilled water plus the listed salts and agar; glucose (10 g in 50 ml H2O) is sterilized separately and mixed after cooling. The retained basal g/L values are provider-reported normalizations, not final-medium concentrations. The two water inputs do not establish a measured 1 L final volume. Historical import annotations and ontology mappings are retained, not revalidated.",
        "evidence_field_path": "evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "evidence_field_path": "evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].notes",
        "stored": "Mix the separately prepared glucose with the cooled basal preparation. The 50 ml is water input, not a measured stock volume or a per-liter dose; no numeric stock addition concentration is asserted.",
        "evidence_field_path": "evidence"
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "evidence_field_path": "evidence"
      }
    ],
    "desired": {
      "pH": 6.5,
      "glucose_g": 10,
      "glucose_water_ml": 50,
      "mixing": "after cooling",
      "no_final_volume_inference": true
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary preparation sentence",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary basal input",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      }
    ],
    "interpretation": "Matching attached record-level evidence explicitly supports these named fields. Preserve the existing repair; numerical stock dose, sterilization method/cycle and final volumes remain unspecified."
  },
  {
    "decision_id": "q38",
    "name": "Missing staged preparation",
    "stage": "Generated target",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "notes",
        "stored": "Source: KOMODO ModelSEED &#124; ID: 111 &#124; DSMZ Medium: 111 (mediadive.medium:111) &#124; Aerobic: No"
      }
    ],
    "desired": {
      "separate_glucose_g": 10,
      "separate_water_ml": 50,
      "basal_water_ml": 950,
      "mixing": "after cooling"
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary preparation sentence",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      },
      {
        "source_key": "mediadive111Historical",
        "source_url": "https://mediadive.dsmz.de/rest/medium/111",
        "source_locator": "$.data.solutions[0].steps[0]",
        "exact_source_quote": "{\n                        \"step\": \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\n                    }",
        "snapshot_sha256": "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b"
      },
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Basal water row",
        "exact_source_quote": "Distilled water 950.0 ml",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      }
    ],
    "interpretation": "The maintained records already contain this structure and scope. Restore it through separately authorized guarded regeneration; do not create duplicate stock records or redo the owner repair."
  },
  {
    "decision_id": "q39",
    "name": "pH",
    "stage": "Main preparation",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "ph_value",
        "stored": 6.5
      }
    ],
    "desired": {
      "value": 6.5
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary preparation sentence",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      }
    ],
    "interpretation": "The stored pH agrees in all layers. No titrant identity, strength or dose follows from this sentence; the record-level owner preparation evidence is authenticated separately."
  },
  {
    "decision_id": "q40",
    "name": "Unquantified stock dose and final concentrations",
    "stage": "Main and glucose preparation",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "desired": {
      "stock_receiving_dose": null,
      "stock_final_volume": null,
      "medium_final_volume": null,
      "glucose_concentration": null,
      "sterilization_method_cycle": null,
      "cooling_temperature": null,
      "growth_conditions": null
    },
    "source_snippets": [
      {
        "source_key": "dsmz111",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf",
        "source_locator": "Primary preparation sentence",
        "exact_source_quote": "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.",
        "snapshot_sha256": "0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8",
        "parsed_text_sha256": "856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6"
      }
    ],
    "interpretation": "The absence of these owner numerical slots is intentional and source-faithful. No 50 ml/L dose, 200 g/L stock, 10 g/L final glucose or 1 L measured final volume may be inferred."
  }
]

### Complete local linkage and exact supplied forms

grounding: supported. Targets: CultureMech:003822.

The target has ten primary and ten CHEBI-keyed secondary links across ten ingredient instances (100% linkage each, not correctness). Both owners additionally retain provider-specific distilled-water identity and generic nested glucose; water stock has no fabricated chemical ID. All asserted CHEBI labels/current MIM keys resolve, while the water provider ID resolves to the exact recipe object. Explicit Mg/Fe heptahydrates, Mn/Zn/Cu hexahydrates and sodium molybdate dihydrate agree with the source. Phosphate formulae agree; CHEBI:131527 synonym tension does not prove a hydrate. Generic glucose does not prove DL composition.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003822.

25 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accession and repaired source contributors

identity: supported. Targets: CultureMech:003822.

DSMZ 111 primary, recovered medium metadata, exact KOMODO mapping and reciprocal owner relationships identify the same source medium. Ingredient fingerprints alone do not establish historical equivalence, and unrelated similarly named reports are excluded.

### Existing stage repair and generated lag

quantity: concern. Targets: CultureMech:003822.

Both maintained owners already withdraw the mis-staged glucose rate, preserve 10 g in 50 ml water, store 950 ml basal water, retain qualified provider basal rates and separately mix after cooling. These 27 attached claims authenticate to original raw. The target predates that repair and must be reconciled without duplicating or undoing it.

### Staged water, required agar and unavailable conditions

completeness: concern. Targets: CultureMech:003822.

Agar 15 g is required in this primary table, unlike conditional agar in medium 1215; no neighboring rule transfers. Both owner preparations are present; the target lacks them. Source does not quantify a final glucose stock volume, receiving dose, measured final-medium volume, sterilization method/time/temperature or cooling endpoint.

### Classification and growth boundaries

scope: supported. Targets: CultureMech:003822.

The chemical basal formulation and required agar support the selected defined solid preparation. No species-specific growth, nitrogen fixation or oxygen physiology is inferred from the medium title or catalog metadata.

## Findings

### f1: Generated target retains a withdrawn glucose rate

major / open / confirmed; issue key: culturemech.003822.stale-glucose-and-preparation.

The target stores 10.5263 g/L glucose without the separate preparation, two water inputs or basal denominator limits. Both maintained owners already contain the authenticated source-specific correction.

### f2: Generated target omits authenticated repair evidence

major / open / confirmed; issue key: culturemech.003822.generated-evidence-history-lag.

The target lacks all 27 attached owner claims, source references and later repair history. This is an observed layer difference, not a universal defect assigned to the current guarded merger.

### f3: KOMODO history has malformed and timezone-naive times

minor / open / confirmed; issue key: culturemech.003822.malformed-import-times.

Target and KOMODO owner retain .fZ and timezone-naive import/resolver timestamps. The source-specific repair correctly preserves those historical bytes; no replacement time is established.

## Recommended Actions And Acceptance Checks

### a1

Preserve the repaired owners, verify their full formulation compatibility and regenerate the target through the current guarded path. Confirm separate glucose mass/water and basal qualifications survive; do not invent stock/final concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve every owner claim, superseded explanation and original event when reconciling the generated layer; use exact field ownership and source stages as acceptance criteria.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Keep original history and append only a supported clarification rather than fabricating timestamp precision.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/beijerinckia_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch040/400/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/400/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml:1:id: CultureMech:003822<br>./data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml:1:id: CultureMech:003822<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch040/source-preflight-bound/400/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 16 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf; Complete DSMZ 111 table and final preparation sentence | supports | The source explicitly separates glucose preparation from 950 ml basal water, then mixes after cooling. It supplies no measured final stock or medium volume. |
| historical-raw | https://mediadive.dsmz.de/rest/medium/111; Historical complete $.data.medium and $.data.solutions[0] | supports | Original October 7 raw bytes and timestamp authenticate provider recipe rows and the separate glucose instruction. Table g_l uses the declared 950 ml main-preparation field, not an independently measured receiving volume. |
| catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact accession 111 row | supports | The catalog identifies the linked DSMZ recipe; its source flags are not ingredient quantities or growth evidence. |
| mediadive111api-attempt | https://mediadive.dsmz.de/rest/medium/111; Preserved exact public retrieval result | context_only | Current mediadive111api returned HTTP 503. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred. |
| mediadive111api_retry-attempt | https://mediadive.dsmz.de/rest/medium/111; Preserved exact public retrieval result | context_only | Current mediadive111api_retry returned HTTP 503. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred. |
| komodo111detail-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=111; Preserved exact public retrieval result | context_only | Current komodo111detail returned HTTP 403. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch040/400/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| history-inventory | /private/tmp/culturemech-review-work-batch040/400/history-inventory.json; All 27 owner ingredient/stock/record claims and scoped historical reports | context_only | Exact original raw authenticates eighteen basal amount claims, two basal waters, two glucose notes, two stock waters, two record preparation claims and one catalog identity. Superseded explanations remain preserved with their scope labels. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:17234 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:131527 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:63036 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:31795 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:75836 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi131523 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131523; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:131523 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi132762 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132762; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:132762 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi91246 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91246; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:91246 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:75213 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS label, definition, synonyms, formula, charge and obsolete flag | supports | CHEBI:2509 resolves to the asserted nonobsolete canonical label. Chemical-form scope is assessed separately. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch040/400/grounding-inventory.json; All target, owner and nested-stock term instances | context_only | Ten distinct CHEBI IDs have matching canonical labels/current mapped MIM rows. Two provider water identifiers match historical compound 4 directly. No legacy secondary ID is asserted in the assessed layers. |
| history-metadata | data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml; data/normalized_yaml/bacterial/beijerinckia_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.736112"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml", "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:04.736112"}]}, {"input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml", "events": 8, "timestamp_issues": []}] |
| writer-0 | scripts/repair_dsmz111_preparation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The source-specific current DSMZ 111 repair matches the staged owner representation and preserved history, and must not be proposed again as if missing. Current guarded importer/merge code is not proof of the historical cause of the stale generated target. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The source-specific current DSMZ 111 repair matches the staged owner representation and preserved history, and must not be proposed again as if missing. Current guarded importer/merge code is not proof of the historical cause of the stale generated target. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The source-specific current DSMZ 111 repair matches the staged owner representation and preserved history, and must not be proposed again as if missing. Current guarded importer/merge code is not proof of the historical cause of the stale generated target. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The source-specific current DSMZ 111 repair matches the staged owner representation and preserved history, and must not be proposed again as if missing. Current guarded importer/merge code is not proof of the historical cause of the stale generated target. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Current mediadive111api returned HTTP 503. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred.
- Current mediadive111api_retry returned HTTP 503. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred.
- Current komodo111detail returned HTTP 403. Complete primary and exact historical response are available; no unseen detail variant or complete historical equivalence is inferred.
- Current primary and exact historical raw resolve the assessed material claims. Current API/detail failures do not themselves force partial coverage. No measured final volume, stock receiving dose, final glucose concentration or biological growth assertion is inferred.
- Historical reports are derivative. Their unrelated namesake records do not enter the ingredient inventory; current code is not historically replayed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T224024Z-culturemech-003822-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: beijerinckia_medium (CultureMech:003822)'
started_at: '2026-10-21T22:32:21Z'
finished_at: '2026-10-21T22:40:24Z'
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
summary: The generated DSMZ/KOMODO 111 target predates the source-specific repair
  already present in both maintained owners. Those owners correctly distinguish 950
  ml basal water and 10 g glucose prepared separately in 50 ml water, retain qualified
  provider rates, and authenticate 27 narrow claims. The target still has the withdrawn
  10.5263 g/L glucose rate and omits the stock, solvent inputs, preparation, qualifications
  and evidence. No 200 g/L stock strength, 10 g/L final glucose or measured 1 L volume
  is inferred.
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
  - path: data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
    sha256: 54ce5f100caf06cf045216ce49e3eb11ca94d349fffd27cfcec52c4db3ae6ef9
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
    sha256: 4d6740d46117ef7aefc3c6571eb4dab53e1fd06333c8cc9d08675366853d01e7
    role: context
  - path: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
    sha256: 26d5cf2253a725ad7623ad4626b28ac6b12cbd55ff5418aa1073c5f5da060a24
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
  - path: reports/ingredient_concentration_curation/20261007-dsmz111-preparation/dsmz-followup.md
    sha256: 1d4f15a4c84c73b49f4d9890e094b84d0ad47db1125c657fe5f002768f310fe0
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz111-preparation/komodo-followup.md
    sha256: b26b404bab08a3b138029d50e370d41bfdd69af461e4d90aa51599e78adc8ebd
    role: context
  - path: reports/ingredient_concentration_curation/20261007-dsmz111-preparation/plan.json
    sha256: 9a0531773dfcbc84558c856130401a30edd45a4b51e757eb93924464208dad5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/inspected-candidate-context.json
    sha256: 69271099db4c815f4e73c2c0b766418b96843d18688f141e215fd300f8992557
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
    sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml.md
    sha256: 6f50708ecd57836718b21525659167df62bba4edd65bcc5da4f3e7db7360c8d2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/beijerinckia_medium.yaml.md
    sha256: 56071ba81a9eb59256759728fee2b1764ce7b92cdf1990f9d949d0ca106daeb8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/plan.json
    sha256: 087b43514367d268b48e568b66203c146b81601303e5c8e3508f3c91e0fcbf26
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/beijerinckia_medium_for_isolation.yaml.md
    sha256: 81e3ce52cba661b733b014b5663c9dd0b9cdc6c31908e211ebf03161d1e8bab8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/beijerinckia_medium_lmg_18.yaml.md
    sha256: 97aefc6e090bbce6c70a051e29dfc06c496022931957e61e11cbbd3c4e874192
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
  - path: scripts/fetch_solution_concentration_sources.py
    sha256: fbaf82cc2d65fcefda6be4d2825f0c28ad0681f941e2e48d325c3ac8a1e00632
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/inventory_komodo_concentration_sources.py
    sha256: 9afef8396b73ae00a97cc7f03104e47a5549cd6bf6f813da6f2f815154ebd74b
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
  - path: scripts/repair_dsmz111_preparation.py
    sha256: 773d682e99ab0d1c6ba381ef43861980d52a55f0c04b9e845abdf29d505d2bdd
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
  - path: src/culturemech/curate/curation_event.py
    sha256: e8aa053ba6dd06485b29ca5da640f91ef96513feff18492a72adc12f40130024
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
  selection: Task review 400; batch 040 item 10 of 10, selected in Python lexicographic
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
  - CultureMech:003822
targets:
- target_id: CultureMech:003822
  path: data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  label: beijerinckia_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch040/400/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/400/strict.tsv"
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003822
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
  - CultureMech:003822
- check_id: mediadive111api-source-access
  name: 'Exact source content access: mediadive111api'
  required: false
  status: unavailable
  summary: Current mediadive111api returned HTTP 503. Complete primary and exact historical
    response are available; no unseen detail variant or complete historical equivalence
    is inferred.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - mediadive111api-attempt
- check_id: mediadive111api_retry-source-access
  name: 'Exact source content access: mediadive111api_retry'
  required: false
  status: unavailable
  summary: Current mediadive111api_retry returned HTTP 503. Complete primary and exact
    historical response are available; no unseen detail variant or complete historical
    equivalence is inferred.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - mediadive111api_retry-attempt
- check_id: komodo111detail-source-access
  name: 'Exact source content access: komodo111detail'
  required: false
  status: unavailable
  summary: Current komodo111detail returned HTTP 403. Complete primary and exact historical
    response are available; no unseen detail variant or complete historical equivalence
    is inferred.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - komodo111detail-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:57.789038Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch040/400/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:59.192388Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/400/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:33:01.078741Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:33:02.027780Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:40:23Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml:1:id:
    CultureMech:003822

    ./data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml:1:id: CultureMech:003822

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/source-preflight-bound/400/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:40:23Z'
  support: supports
  summary: 16 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 2e27eaf70dd9746573ace77000d0bd4a1e269e7dd62d8679206e0cfc3019feb6
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf
  locator: Complete DSMZ 111 table and final preparation sentence
  accessed_at: '2026-10-21T22:02:48.481964Z'
  support: supports
  summary: The source explicitly separates glucose preparation from 950 ml basal water,
    then mixes after cooling. It supplies no measured final stock or medium volume.
  quote: Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix
    after cooling.
  snapshot_sha256: 0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8
- evidence_id: historical-raw
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/111
  locator: Historical complete $.data.medium and $.data.solutions[0]
  accessed_at: '2026-10-07T10:42:16.969612Z'
  support: supports
  summary: Original October 7 raw bytes and timestamp authenticate provider recipe
    rows and the separate glucose instruction. Table g_l uses the declared 950 ml
    main-preparation field, not an independently measured receiving volume.
  quote: '"volume": 950'
  snapshot_sha256: 55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b
- evidence_id: catalog
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact accession 111 row
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The catalog identifies the linked DSMZ recipe; its source flags are not
    ingredient quantities or growth evidence.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=111'\
    \ >111</a></TD>\n\t\t\t\t\t<TD>BEIJERINCKIA MEDIUM</TD>\n\t\t\t\t\t<TD> 6.5</TD>\n\
    \t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\t\t\t\t\t<TD>false</TD>\n\
    <TD><a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf'\
    \ >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf</a></TD>\n\t\
    \t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: mediadive111api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/111
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:02:47.951950Z'
  support: context_only
  summary: Current mediadive111api returned HTTP 503. Complete primary and exact historical
    response are available; no unseen detail variant or complete historical equivalence
    is inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive111api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/111
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:03:46.083761Z'
  support: context_only
  summary: Current mediadive111api_retry returned HTTP 503. Complete primary and exact
    historical response are available; no unseen detail variant or complete historical
    equivalence is inferred.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo111detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=111
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:02:47.727540Z'
  support: context_only
  summary: Current komodo111detail returned HTTP 403. Complete primary and exact historical
    response are available; no unseen detail variant or complete historical equivalence
    is inferred.
  snapshot_sha256: ff8a742e49b5278442c12f39186e762b30d2d79aaaa8bdc5b4d8e8f7bbe2f9d9
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/400/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: b00cc46b7f94908dfc8f17f428a10936d705bbfd6674281500f748e504268b76
- evidence_id: history-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/400/history-inventory.json
  locator: All 27 owner ingredient/stock/record claims and scoped historical reports
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: Exact original raw authenticates eighteen basal amount claims, two basal
    waters, two glucose notes, two stock waters, two record preparation claims and
    one catalog identity. Superseded explanations remain preserved with their scope
    labels.
  snapshot_sha256: b98ca011606be7c45fefc1237c1f5b1a80d80371572e76f7722bbaf9c4b3b60f
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: CHEBI:63036 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: CHEBI:31795 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: CHEBI:75836 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi131523
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131523
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T22:02:49.344094Z'
  support: supports
  summary: CHEBI:131523 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: d407981c433715719a4eed5d8912c201c60cc700658d598d05c4afb77cb43f45
- evidence_id: chebi132762
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132762
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T22:02:49.405736Z'
  support: supports
  summary: CHEBI:132762 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: d976dd1163578efde5e2d4a5a1ddc4c43cfe1fa921505e3bf27ef6d51d791323
- evidence_id: chebi91246
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91246
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T22:02:50.400820Z'
  support: supports
  summary: CHEBI:91246 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: ceb6f9162d9cc04c3e78466fd39630578910cf27ee78f88907e5fa2ed0f43f81
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: CHEBI:75213 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS label, definition, synonyms, formula, charge and obsolete flag
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 resolves to the asserted nonobsolete canonical label. Chemical-form
    scope is assessed separately.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/400/grounding-inventory.json
  locator: All target, owner and nested-stock term instances
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: Ten distinct CHEBI IDs have matching canonical labels/current mapped MIM
    rows. Two provider water identifiers match historical compound 4 directly. No
    legacy secondary ID is asserted in the assessed layers.
  snapshot_sha256: a047ebb43f310ab65d2c1606ff0ac62e042f1b7ee25c3be4740462e88c837680
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml;
    data/normalized_yaml/bacterial/beijerinckia_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:04.736112"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml",
    "events": 8, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:04.736112"}]}, {"input": "data/normalized_yaml/bacterial/beijerinckia_medium.yaml",
    "events": 8, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_dsmz111_preparation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: The source-specific current DSMZ 111 repair matches the staged owner representation
    and preserved history, and must not be proposed again as if missing. Current guarded
    importer/merge code is not proof of the historical cause of the stale generated
    target.
  snapshot_sha256: 773d682e99ab0d1c6ba381ef43861980d52a55f0c04b9e845abdf29d505d2bdd
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: The source-specific current DSMZ 111 repair matches the staged owner representation
    and preserved history, and must not be proposed again as if missing. Current guarded
    importer/merge code is not proof of the historical cause of the stale generated
    target.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: The source-specific current DSMZ 111 repair matches the staged owner representation
    and preserved history, and must not be proposed again as if missing. Current guarded
    importer/merge code is not proof of the historical cause of the stale generated
    target.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:40:23Z'
  support: context_only
  summary: The source-specific current DSMZ 111 repair matches the staged owner representation
    and preserved history, and must not be proposed again as if missing. Current guarded
    importer/merge code is not proof of the historical cause of the stale generated
    target.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 40 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Glucose\",\n   \
    \ \"stage\": \"Stale generated main ingredient\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.5263\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount_g\":\
    \ 10,\n      \"source_water_input_ml\": 50,\n      \"stock_concentration\": null,\n\
    \      \"final_medium_concentration\": null\n    },\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n        \"\
    source_locator\": \"Main table glucose row\",\n        \"exact_source_quote\"\
    : \"Glucose 10.0 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n    \
    \    \"source_locator\": \"Separate glucose preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\
    \": 5,\\n                        \\\"amount\\\": 10,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10.5263,\\\
    n                        \\\"mmol_l\\\": 58.4276,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target rate divides glucose mass\
    \ by the unrelated 950 ml basal-water field. Both maintained owners already withdraw\
    \ this rate and retain the supported batch amount in the separate preparation.\
    \ Do not reinstate it or infer 200 g/L stock or 10 g/L final glucose.\"\n  },\n\
    \  {\n    \"decision_id\": \"q2\",\n    \"name\": \"K2HPO4\",\n    \"stage\":\
    \ \"Generated provider-normalized basal row\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.842105\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.842105\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 0.8,\n      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 2\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.8 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.842105,\\\
    n                        \\\"mmol_l\\\": 4.83479,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n   \
    \ \"name\": \"K2HPO4\",\n    \"stage\": \"Maintained qualified basal row\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.842105\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"evidence_field_path\": \"ingredients[0].evidence\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.8 g. The retained 0.842105 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[0].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.842105\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 0.8,\n\
    \      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 2\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.8 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.842105,\\\
    n                        \\\"mmol_l\\\": 4.83479,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q4\",\n    \"name\": \"K2HPO4\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.842105\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"evidence_field_path\": \"ingredients[0].evidence\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.8 g. The retained 0.842105 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[0].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.842105\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 0.8,\n\
    \      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 2\",\n        \"exact_source_quote\"\
    : \"K2HPO4 0.8 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 2,\\n                  \
    \      \\\"compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\
    \": 10,\\n                        \\\"amount\\\": 0.8,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.842105,\\\
    n                        \\\"mmol_l\\\": 4.83479,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q5\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"Generated\
    \ provider-normalized basal row\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.210526\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.210526\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 0.2,\n      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 3\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.2 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.210526,\\\
    n                        \\\"mmol_l\\\": 1.54701,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n   \
    \ \"name\": \"KH2PO4\",\n    \"stage\": \"Maintained qualified basal row\",\n\
    \    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.210526\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"evidence_field_path\": \"ingredients[1].evidence\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.2 g. The retained 0.210526 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[1].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.210526\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 0.2,\n\
    \      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 3\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.2 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.210526,\\\
    n                        \\\"mmol_l\\\": 1.54701,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q7\",\n    \"name\": \"KH2PO4\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.210526\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"evidence_field_path\": \"ingredients[1].evidence\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.2 g. The retained 0.210526 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[1].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.210526\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 0.2,\n\
    \      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 3\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.2 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 3,\\n                  \
    \      \\\"compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\
    \": 11,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.210526,\\\
    n                        \\\"mmol_l\\\": 1.54701,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q8\",\n    \"name\": \"MgSO4 x 7 H2O\",\n    \"stage\": \"Generated\
    \ provider-normalized basal row\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.105263\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.105263\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 0.1,\n      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 4\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.1 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.105263,\\n                        \\\"mmol_l\\\": 0.427073,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive111Historical\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n   \
    \ \"name\": \"MgSO4 x 7 H2O\",\n    \"stage\": \"Maintained qualified basal row\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.105263\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"evidence_field_path\": \"ingredients[2].evidence\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.1 g. The retained 0.105263 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[2].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.105263\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 0.1,\n\
    \      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 4\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.1 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.105263,\\n                        \\\"mmol_l\\\": 0.427073,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive111Historical\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q10\",\n    \"name\": \"MgSO4 x 7 H2O\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.105263\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"evidence_field_path\": \"ingredients[2].evidence\"\n     \
    \ },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].notes\",\n        \"stored\": \"Source\
    \ batch input: 0.1 g. The retained 0.105263 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[2].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.105263\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 0.1,\n\
    \      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 4\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.1 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 4,\\n                  \
    \      \\\"compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 8,\\n                        \\\"amount\\\": 0.1,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 0.105263,\\n                        \\\"mmol_l\\\": 0.427073,\\n           \
    \             \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive111Historical\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q11\",\n    \"name\": \"FeSO4 x 7 H2O\",\n    \"stage\": \"Generated\
    \ provider-normalized basal row\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0210526\",\n          \"unit\": \"G_PER_L\"\n  \
    \      }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.0210526\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 20,\n      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 5\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O 20.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 12,\\n                        \\\"amount\\\": 20,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.0210526,\\n                        \\\"mmol_l\\\": 0.0757248,\\n       \
    \                 \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive111Historical\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n  \
    \  \"name\": \"FeSO4 x 7 H2O\",\n    \"stage\": \"Maintained qualified basal row\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0210526\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"evidence_field_path\": \"ingredients[3].evidence\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Source\
    \ batch input: 20 mg. The retained 0.0210526 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[3].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.0210526\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 20,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 5\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O 20.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 12,\\n                        \\\"amount\\\": 20,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.0210526,\\n                        \\\"mmol_l\\\": 0.0757248,\\n       \
    \                 \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive111Historical\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q13\",\n    \"name\": \"FeSO4 x 7 H2O\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0210526\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"evidence_field_path\": \"ingredients[3].evidence\"\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].notes\",\n        \"stored\": \"Source\
    \ batch input: 20 mg. The retained 0.0210526 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[3].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.0210526\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 20,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 5\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O 20.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 5,\\n                  \
    \      \\\"compound\\\": \\\"FeSO4 x 7 H2O\\\",\\n                        \\\"\
    compound_id\\\": 12,\\n                        \\\"amount\\\": 20,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.0210526,\\n                        \\\"mmol_l\\\": 0.0757248,\\n       \
    \                 \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadive111Historical\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q14\",\n    \"name\": \"MnSO4 x 6 H2O\",\n    \"stage\": \"Generated\
    \ provider-normalized basal row\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00210526\",\n          \"unit\": \"G_PER_L\"\n \
    \       }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.00210526\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 2,\n      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 6\",\n        \"exact_source_quote\"\
    : \"MnSO4 x 6 H2O 2.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"MnSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 216,\\n                        \\\"amount\\\": 2,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00210526,\\n                        \\\"mmol_l\\\": 0.00812551,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n  \
    \  \"name\": \"MnSO4 x 6 H2O\",\n    \"stage\": \"Maintained qualified basal row\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00210526\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[4].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Source\
    \ batch input: 2 mg. The retained 0.00210526 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[4].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00210526\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 2,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 6\",\n        \"exact_source_quote\"\
    : \"MnSO4 x 6 H2O 2.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"MnSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 216,\\n                        \\\"amount\\\": 2,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00210526,\\n                        \\\"mmol_l\\\": 0.00812551,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q16\",\n    \"name\": \"MnSO4 x 6 H2O\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00210526\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[4].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].notes\",\n        \"stored\": \"Source\
    \ batch input: 2 mg. The retained 0.00210526 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[4].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00210526\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 2,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 6\",\n        \"exact_source_quote\"\
    : \"MnSO4 x 6 H2O 2.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 6,\\n                  \
    \      \\\"compound\\\": \\\"MnSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 216,\\n                        \\\"amount\\\": 2,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00210526,\\n                        \\\"mmol_l\\\": 0.00812551,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q17\",\n    \"name\": \"ZnSO4 x 6 H2O\",\n    \"stage\": \"Generated\
    \ provider-normalized basal row\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00526316\",\n          \"unit\": \"G_PER_L\"\n \
    \       }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.00526316\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 7\",\n        \"exact_source_quote\"\
    : \"ZnSO4 x 6 H2O 5.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"ZnSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 217,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00526316,\\n                        \\\"mmol_l\\\": 0.0195256,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n  \
    \  \"name\": \"ZnSO4 x 6 H2O\",\n    \"stage\": \"Maintained qualified basal row\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00526316\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[5].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Source\
    \ batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[5].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00526316\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 5,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 7\",\n        \"exact_source_quote\"\
    : \"ZnSO4 x 6 H2O 5.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"ZnSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 217,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00526316,\\n                        \\\"mmol_l\\\": 0.0195256,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q19\",\n    \"name\": \"ZnSO4 x 6 H2O\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00526316\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[5].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].notes\",\n        \"stored\": \"Source\
    \ batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[5].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00526316\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 5,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 7\",\n        \"exact_source_quote\"\
    : \"ZnSO4 x 6 H2O 5.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 7,\\n                  \
    \      \\\"compound\\\": \\\"ZnSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 217,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00526316,\\n                        \\\"mmol_l\\\": 0.0195256,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q20\",\n    \"name\": \"CuSO4 x 6 H2O\",\n    \"stage\": \"Generated\
    \ provider-normalized basal row\",\n    \"decision\": \"evidence_only\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00421053\",\n          \"unit\": \"G_PER_L\"\n \
    \       }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.00421053\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 4,\n      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 8\",\n        \"exact_source_quote\"\
    : \"CuSO4 x 6 H2O 4.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CuSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 218,\\n                        \\\"amount\\\": 4,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00421053,\\n                        \\\"mmol_l\\\": 0.0157285,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n  \
    \  \"name\": \"CuSO4 x 6 H2O\",\n    \"stage\": \"Maintained qualified basal row\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00421053\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[6].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Source\
    \ batch input: 4 mg. The retained 0.00421053 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[6].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00421053\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 4,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 8\",\n        \"exact_source_quote\"\
    : \"CuSO4 x 6 H2O 4.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CuSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 218,\\n                        \\\"amount\\\": 4,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00421053,\\n                        \\\"mmol_l\\\": 0.0157285,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q22\",\n    \"name\": \"CuSO4 x 6 H2O\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00421053\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[6].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].notes\",\n        \"stored\": \"Source\
    \ batch input: 4 mg. The retained 0.00421053 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[6].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00421053\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 4,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 8\",\n        \"exact_source_quote\"\
    : \"CuSO4 x 6 H2O 4.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 8,\\n                  \
    \      \\\"compound\\\": \\\"CuSO4 x 6 H2O\\\",\\n                        \\\"\
    compound_id\\\": 218,\\n                        \\\"amount\\\": 4,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00421053,\\n                        \\\"mmol_l\\\": 0.0157285,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q23\",\n    \"name\": \"Na2MoO4 x 2 H2O\",\n    \"stage\": \"\
    Generated provider-normalized basal row\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00526316\",\n          \"unit\": \"G_PER_L\"\n \
    \       }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\"\
    : \"0.00526316\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 5,\n      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 9\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 5.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 9,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00526316,\\n                        \\\"mmol_l\\\": 0.0217531,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q24\",\n  \
    \  \"name\": \"Na2MoO4 x 2 H2O\",\n    \"stage\": \"Maintained qualified basal\
    \ row\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00526316\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[7].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"Source\
    \ batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[7].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00526316\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 5,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 9\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 5.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 9,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00526316,\\n                        \\\"mmol_l\\\": 0.0217531,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q25\",\n    \"name\": \"Na2MoO4 x 2 H2O\",\n    \"stage\": \"\
    Maintained qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00526316\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"evidence_field_path\": \"ingredients[7].evidence\"\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].notes\",\n        \"stored\": \"Source\
    \ batch input: 5 mg. The retained 0.00526316 g/L is the provider-declared rate\
    \ normalized to its 950 ml main-preparation field, not an independently verified\
    \ concentration after adding the separately prepared glucose. No final volume\
    \ is inferred.\",\n        \"evidence_field_path\": \"ingredients[7].evidence\"\
    \n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"0.00526316\"\
    ,\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 5,\n\
    \      \"source_unit\": \"mg\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 9\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 5.0 mg\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 9,\\n                  \
    \      \\\"compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\
    \"compound_id\\\": 9,\\n                        \\\"amount\\\": 5,\\n        \
    \                \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.00526316,\\n                        \\\"mmol_l\\\": 0.0217531,\\n      \
    \                  \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q26\",\n    \"name\": \"Agar\",\n    \"stage\": \"Generated provider-normalized\
    \ basal row\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15.7895\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"provider_rate_g_per_l\":\
    \ \"15.7895\",\n      \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\"\
    : 15,\n      \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n\
    \    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 10\",\n        \"exact_source_quote\"\
    : \"Agar 15.0 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"amount\\\": 15,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 15.7895,\\\
    n                        \\\"mmol_l\\\": 46.9464,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target numeral agrees with the\
    \ provider table but lacks its preparation-stage qualification and attached evidence.\
    \ Preserve the batch input and 950 ml normalization limitation, not a claimed\
    \ final-medium concentration.\"\n  },\n  {\n    \"decision_id\": \"q27\",\n  \
    \  \"name\": \"Agar\",\n    \"stage\": \"Maintained qualified basal row\",\n \
    \   \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15.7895\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"evidence_field_path\": \"ingredients[8].evidence\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"Source\
    \ batch input: 15 g. The retained 15.7895 g/L is the provider-declared rate normalized\
    \ to its 950 ml main-preparation field, not an independently verified concentration\
    \ after adding the separately prepared glucose. No final volume is inferred.\"\
    ,\n        \"evidence_field_path\": \"ingredients[8].evidence\"\n      }\n   \
    \ ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"15.7895\",\n    \
    \  \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 15,\n  \
    \    \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 10\",\n        \"exact_source_quote\"\
    : \"Agar 15.0 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"amount\\\": 15,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 15.7895,\\\
    n                        \\\"mmol_l\\\": 46.9464,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q28\",\n    \"name\": \"Agar\",\n    \"stage\": \"Maintained\
    \ qualified basal row\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15.7895\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"evidence_field_path\": \"ingredients[8].evidence\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].notes\",\n        \"stored\": \"Source\
    \ batch input: 15 g. The retained 15.7895 g/L is the provider-declared rate normalized\
    \ to its 950 ml main-preparation field, not an independently verified concentration\
    \ after adding the separately prepared glucose. No final volume is inferred.\"\
    ,\n        \"evidence_field_path\": \"ingredients[8].evidence\"\n      }\n   \
    \ ],\n    \"desired\": {\n      \"provider_rate_g_per_l\": \"15.7895\",\n    \
    \  \"provider_volume_field_ml\": 950,\n      \"source_batch_amount\": 15,\n  \
    \    \"source_unit\": \"g\",\n      \"final_medium_concentration\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal table row 10\",\n        \"exact_source_quote\"\
    : \"Agar 15.0 g\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 10,\\n                 \
    \       \\\"compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\
    \": 3,\\n                        \\\"amount\\\": 15,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 15.7895,\\\
    n                        \\\"mmol_l\\\": 46.9464,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"This exact owner field has attached\
    \ authenticated evidence and explicitly preserves the source batch input and denominator\
    \ limitation. Verification applies to this qualified provider declaration only,\
    \ not final-medium concentration or secondary grounding.\"\n  },\n  {\n    \"\
    decision_id\": \"q29\",\n    \"name\": \"Basal water\",\n    \"stage\": \"Generated\
    \ target missing input\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients\",\n        \"stored\": [\n         \
    \ {\n            \"preferred_term\": \"Glucose\",\n            \"term\": {\n \
    \             \"id\": \"CHEBI:17234\",\n              \"label\": \"glucose\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    10.5263\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:17234\",\n\
    \              \"label\": \"glucose\"\n            }\n          },\n         \
    \ {\n            \"preferred_term\": \"K2HPO4\",\n            \"term\": {\n  \
    \            \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium\
    \ hydrogen phosphate\"\n            },\n            \"concentration\": {\n   \
    \           \"value\": \"0.842105\",\n              \"unit\": \"G_PER_L\"\n  \
    \          },\n            \"mediaingredientmech_chebi_term\": {\n           \
    \   \"id\": \"CHEBI:131527\",\n              \"label\": \"dipotassium hydrogen\
    \ phosphate\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"KH2PO4\",\n            \"term\": {\n              \"id\": \"CHEBI:63036\"\
    ,\n              \"label\": \"potassium dihydrogen phosphate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.210526\",\n  \
    \            \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:63036\",\n              \"label\": \"potassium\
    \ dihydrogen phosphate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MgSO4 x 7 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:31795\",\n              \"label\": \"magnesium sulfate\
    \ heptahydrate\"\n            },\n            \"concentration\": {\n         \
    \     \"value\": \"0.105263\",\n              \"unit\": \"G_PER_L\"\n        \
    \    },\n            \"mediaingredientmech_chebi_term\": {\n              \"id\"\
    : \"CHEBI:31795\",\n              \"label\": \"magnesium sulfate heptahydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    FeSO4 x 7 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75836\"\
    ,\n              \"label\": \"iron(2+) sulfate heptahydrate\"\n            },\n\
    \            \"concentration\": {\n              \"value\": \"0.0210526\",\n \
    \             \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75836\",\n              \"label\": \"iron(2+)\
    \ sulfate heptahydrate\"\n            }\n          },\n          {\n         \
    \   \"preferred_term\": \"MnSO4 x 6 H2O\",\n            \"term\": {\n        \
    \      \"id\": \"CHEBI:131523\",\n              \"label\": \"manganese(II) sulfate\
    \ hexahydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.00210526\",\n              \"unit\": \"G_PER_L\"\n       \
    \     },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:131523\",\n              \"label\": \"manganese(II) sulfate hexahydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    ZnSO4 x 6 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:132762\"\
    ,\n              \"label\": \"zinc sulfate hexahydrate\"\n            },\n   \
    \         \"concentration\": {\n              \"value\": \"0.00526316\",\n   \
    \           \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132762\",\n              \"label\": \"zinc\
    \ sulfate hexahydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"CuSO4 x 6 H2O\",\n            \"term\": {\n         \
    \     \"id\": \"CHEBI:91246\",\n              \"label\": \"copper(II) sulfate\
    \ hexahydrate\"\n            },\n            \"concentration\": {\n          \
    \    \"value\": \"0.00421053\",\n              \"unit\": \"G_PER_L\"\n       \
    \     },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91246\",\n              \"label\": \"copper(II) sulfate hexahydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Na2MoO4 x 2 H2O\",\n            \"term\": {\n              \"id\": \"CHEBI:75213\"\
    ,\n              \"label\": \"sodium molybdate dihydrate\"\n            },\n \
    \           \"concentration\": {\n              \"value\": \"0.00526316\",\n \
    \             \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:75213\",\n              \"label\": \"sodium\
    \ molybdate dihydrate\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"Agar\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:2509\",\n              \"label\": \"agar\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"15.7895\",\n          \
    \    \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            }\n          }\n        ]\n      }\n    ],\n    \"desired\": {\n\
    \      \"source_amount_ml\": 950,\n      \"representation\": \"0.95 L water input;\
    \ not final-volume makeup\"\n    },\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal solvent row\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 11,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 950,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"The target lacks the solvent; both\
    \ maintained owners already store and authenticate this exact input.\"\n  },\n\
    \  {\n    \"decision_id\": \"q30\",\n    \"name\": \"Basal distilled water\",\n\
    \    \"stage\": \"Maintained basal input\",\n    \"decision\": \"verified\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.95\",\n          \"unit\": \"L\"\n        },\n \
    \       \"evidence_field_path\": \"ingredients[9].evidence\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].notes\",\n        \"stored\": \"950\
    \ ml distilled-water input per basal batch, not a final-volume makeup instruction.\"\
    ,\n        \"evidence_field_path\": \"ingredients[9].evidence\"\n      }\n   \
    \ ],\n    \"desired\": {\n      \"value\": \"0.95\",\n      \"unit\": \"L\",\n\
    \      \"source_amount_ml\": 950\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal solvent row\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 11,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 950,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached evidence supports 950 ml\
    \ / 1000 = 0.95 L as input only. The owner expressly denies a final-volume makeup\
    \ instruction.\"\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"name\": \"Glucose\
    \ batch amount\",\n    \"stage\": \"Maintained separate preparation\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\",\n  \
    \      \"field_path\": \"solutions[0].composition[0].notes\",\n        \"stored\"\
    : \"Source batch input: 10 g glucose in 50 ml H2O, sterilized separately and mixed\
    \ after cooling. The former 10.5263 g/L divides by the unrelated 950 ml basal-water\
    \ input and is withdrawn. No 200 g/L stock strength or 10 g/L final-medium concentration\
    \ is asserted: neither final volume is specified.\",\n        \"evidence_field_path\"\
    : \"solutions[0].composition[0].evidence\"\n      }\n    ],\n    \"desired\":\
    \ {\n      \"source_batch_amount_g\": 10,\n      \"source_water_input_ml\": 50,\n\
    \      \"numeric_stock_concentration\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n        \"\
    source_locator\": \"Separate preparation\",\n        \"exact_source_quote\": \"\
    Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after\
    \ cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\
    \": 5,\\n                        \\\"amount\\\": 10,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10.5263,\\\
    n                        \\\"mmol_l\\\": 58.4276,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached object and additional preparation\
    \ excerpt authenticate the withdrawal and batch-mass note. Historical explanations\
    \ are preserved as superseded where their stage differs, not silently treated\
    \ as current final concentration.\"\n  },\n  {\n    \"decision_id\": \"q32\",\n\
    \    \"name\": \"Glucose water\",\n    \"stage\": \"Maintained separate preparation\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\": \"L\"\
    \n        },\n        \"evidence_field_path\": \"solutions[0].composition[1].evidence\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].notes\",\n        \"\
    stored\": \"50 ml H2O input for the separately sterilized glucose; water purity\
    \ and final stock volume are not specified.\",\n        \"evidence_field_path\"\
    : \"solutions[0].composition[1].evidence\"\n      }\n    ],\n    \"desired\":\
    \ {\n      \"value\": \"0.05\",\n      \"unit\": \"L\",\n      \"source_amount_ml\"\
    : 50\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Separate glucose preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"50 ml / 1000 = 0.05 L water input\
    \ is authenticated. H2O alone does not prove distilled purity, final stock volume\
    \ or a per-liter dose.\"\n  },\n  {\n    \"decision_id\": \"q33\",\n    \"name\"\
    : \"Retained preparation qualifications\",\n    \"stage\": \"Maintained whole\
    \ record and stock\",\n    \"decision\": \"verified\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: KOMODO ModelSEED\
    \ | ID: 111 | DSMZ Medium: 111 (mediadive.medium:111) | Aerobic: No\\n\\nPreparation\
    \ scope: basal input is 950 ml distilled water plus the listed salts and agar;\
    \ glucose (10 g in 50 ml H2O) is sterilized separately and mixed after cooling.\
    \ The retained basal g/L values are provider-reported normalizations, not final-medium\
    \ concentrations. The two water inputs do not establish a measured 1 L final volume.\
    \ Historical import annotations and ontology mappings are retained, not revalidated.\"\
    ,\n        \"evidence_field_path\": \"evidence\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\"\
    ,\n        \"evidence_field_path\": \"evidence\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].notes\",\n        \"stored\": \"Mix\
    \ the separately prepared glucose with the cooled basal preparation. The 50 ml\
    \ is water input, not a measured stock volume or a per-liter dose; no numeric\
    \ stock addition concentration is asserted.\",\n        \"evidence_field_path\"\
    : \"evidence\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"evidence_field_path\": \"evidence\"\n      }\n\
    \    ],\n    \"desired\": {\n      \"pH\": 6.5,\n      \"glucose_g\": 10,\n  \
    \    \"glucose_water_ml\": 50,\n      \"mixing\": \"after cooling\",\n      \"\
    no_final_volume_inference\": true\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n    \
    \    \"source_locator\": \"Primary basal input\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached record-level evidence\
    \ explicitly supports these named fields. Preserve the existing repair; numerical\
    \ stock dose, sterilization method/cycle and final volumes remain unspecified.\"\
    \n  },\n  {\n    \"decision_id\": \"q34\",\n    \"name\": \"Basal distilled water\"\
    ,\n    \"stage\": \"Maintained basal input\",\n    \"decision\": \"verified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.95\",\n          \"unit\": \"L\"\n        },\n \
    \       \"evidence_field_path\": \"ingredients[9].evidence\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].notes\",\n        \"stored\": \"950\
    \ ml distilled-water input per basal batch, not a final-volume makeup instruction.\"\
    ,\n        \"evidence_field_path\": \"ingredients[9].evidence\"\n      }\n   \
    \ ],\n    \"desired\": {\n      \"value\": \"0.95\",\n      \"unit\": \"L\",\n\
    \      \"source_amount_ml\": 950\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary basal solvent row\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 11,\\n                 \
    \       \\\"compound\\\": \\\"Distilled water\\\",\\n                        \\\
    \"compound_id\\\": 4,\\n                        \\\"amount\\\": 950,\\n      \
    \                  \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached evidence supports 950 ml\
    \ / 1000 = 0.95 L as input only. The owner expressly denies a final-volume makeup\
    \ instruction.\"\n  },\n  {\n    \"decision_id\": \"q35\",\n    \"name\": \"Glucose\
    \ batch amount\",\n    \"stage\": \"Maintained separate preparation\",\n    \"\
    decision\": \"verified\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\",\n        \"field_path\"\
    : \"solutions[0].composition[0].notes\",\n        \"stored\": \"Source batch input:\
    \ 10 g glucose in 50 ml H2O, sterilized separately and mixed after cooling. The\
    \ former 10.5263 g/L divides by the unrelated 950 ml basal-water input and is\
    \ withdrawn. No 200 g/L stock strength or 10 g/L final-medium concentration is\
    \ asserted: neither final volume is specified.\",\n        \"evidence_field_path\"\
    : \"solutions[0].composition[0].evidence\"\n      }\n    ],\n    \"desired\":\
    \ {\n      \"source_batch_amount_g\": 10,\n      \"source_water_input_ml\": 50,\n\
    \      \"numeric_stock_concentration\": null\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n        \"\
    source_locator\": \"Separate preparation\",\n        \"exact_source_quote\": \"\
    Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after\
    \ cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"recipe_order\\\": 1,\\n                  \
    \      \\\"compound\\\": \\\"Glucose\\\",\\n                        \\\"compound_id\\\
    \": 5,\\n                        \\\"amount\\\": 10,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 10.5263,\\\
    n                        \\\"mmol_l\\\": 58.4276,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\n      },\n\
    \      {\n        \"source_key\": \"mediadive111Historical\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/111\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\": \"{\\n  \
    \                      \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize glucose separately\
    \ (10 g in 50 ml H2O) and mix after cooling.\\\"\\n                    }\",\n\
    \        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"Attached object and additional preparation\
    \ excerpt authenticate the withdrawal and batch-mass note. Historical explanations\
    \ are preserved as superseded where their stage differs, not silently treated\
    \ as current final concentration.\"\n  },\n  {\n    \"decision_id\": \"q36\",\n\
    \    \"name\": \"Glucose water\",\n    \"stage\": \"Maintained separate preparation\"\
    ,\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\",\n  \
    \      \"field_path\": \"solutions[0].composition[1].concentration\",\n      \
    \  \"stored\": {\n          \"value\": \"0.05\",\n          \"unit\": \"L\"\n\
    \        },\n        \"evidence_field_path\": \"solutions[0].composition[1].evidence\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].notes\",\n        \"\
    stored\": \"50 ml H2O input for the separately sterilized glucose; water purity\
    \ and final stock volume are not specified.\",\n        \"evidence_field_path\"\
    : \"solutions[0].composition[1].evidence\"\n      }\n    ],\n    \"desired\":\
    \ {\n      \"value\": \"0.05\",\n      \"unit\": \"L\",\n      \"source_amount_ml\"\
    : 50\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Separate glucose preparation\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      }\n    ],\n    \"interpretation\": \"50 ml / 1000 = 0.05 L water input\
    \ is authenticated. H2O alone does not prove distilled purity, final stock volume\
    \ or a per-liter dose.\"\n  },\n  {\n    \"decision_id\": \"q37\",\n    \"name\"\
    : \"Retained preparation qualifications\",\n    \"stage\": \"Maintained whole\
    \ record and stock\",\n    \"decision\": \"verified\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: DSMZ | Link:\
    \ https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\\n\\nPreparation\
    \ scope: basal input is 950 ml distilled water plus the listed salts and agar;\
    \ glucose (10 g in 50 ml H2O) is sterilized separately and mixed after cooling.\
    \ The retained basal g/L values are provider-reported normalizations, not final-medium\
    \ concentrations. The two water inputs do not establish a measured 1 L final volume.\
    \ Historical import annotations and ontology mappings are retained, not revalidated.\"\
    ,\n        \"evidence_field_path\": \"evidence\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\",\n      \
    \  \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\": \"\
    Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling.\",\n \
    \       \"evidence_field_path\": \"evidence\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\",\n        \"field_path\"\
    : \"solutions[0].notes\",\n        \"stored\": \"Mix the separately prepared glucose\
    \ with the cooled basal preparation. The 50 ml is water input, not a measured\
    \ stock volume or a per-liter dose; no numeric stock addition concentration is\
    \ asserted.\",\n        \"evidence_field_path\": \"evidence\"\n      },\n    \
    \  {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"evidence_field_path\": \"evidence\"\n      }\n\
    \    ],\n    \"desired\": {\n      \"pH\": 6.5,\n      \"glucose_g\": 10,\n  \
    \    \"glucose_water_ml\": 50,\n      \"mixing\": \"after cooling\",\n      \"\
    no_final_volume_inference\": true\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz111\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n    \
    \    \"source_locator\": \"Primary basal input\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      }\n    ],\n    \"interpretation\": \"Matching attached record-level evidence\
    \ explicitly supports these named fields. Preserve the existing repair; numerical\
    \ stock dose, sterilization method/cycle and final volumes remain unspecified.\"\
    \n  },\n  {\n    \"decision_id\": \"q38\",\n    \"name\": \"Missing staged preparation\"\
    ,\n    \"stage\": \"Generated target\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"Source: KOMODO ModelSEED\
    \ | ID: 111 | DSMZ Medium: 111 (mediadive.medium:111) | Aerobic: No\"\n      }\n\
    \    ],\n    \"desired\": {\n      \"separate_glucose_g\": 10,\n      \"separate_water_ml\"\
    : 50,\n      \"basal_water_ml\": 950,\n      \"mixing\": \"after cooling\"\n \
    \   },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      },\n      {\n        \"source_key\": \"mediadive111Historical\",\n   \
    \     \"source_url\": \"https://mediadive.dsmz.de/rest/medium/111\",\n       \
    \ \"source_locator\": \"$.data.solutions[0].steps[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                        \\\"step\\\": \\\"Adjust pH to 6.5. Sterilize\
    \ glucose separately (10 g in 50 ml H2O) and mix after cooling.\\\"\\n       \
    \             }\",\n        \"snapshot_sha256\": \"55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n    \
    \    \"source_locator\": \"Basal water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 950.0 ml\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      }\n    ],\n    \"interpretation\": \"The maintained records already contain\
    \ this structure and scope. Restore it through separately authorized guarded regeneration;\
    \ do not create duplicate stock records or redo the owner repair.\"\n  },\n  {\n\
    \    \"decision_id\": \"q39\",\n    \"name\": \"pH\",\n    \"stage\": \"Main preparation\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.5\n      }\n \
    \   ],\n    \"desired\": {\n      \"value\": 6.5\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz111\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\",\n        \"\
    source_locator\": \"Primary preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored pH agrees in all layers.\
    \ No titrant identity, strength or dose follows from this sentence; the record-level\
    \ owner preparation evidence is authenticated separately.\"\n  },\n  {\n    \"\
    decision_id\": \"q40\",\n    \"name\": \"Unquantified stock dose and final concentrations\"\
    ,\n    \"stage\": \"Main and glucose preparation\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": null\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/beijerinckia_medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"desired\": {\n      \"stock_receiving_dose\": null,\n    \
    \  \"stock_final_volume\": null,\n      \"medium_final_volume\": null,\n     \
    \ \"glucose_concentration\": null,\n      \"sterilization_method_cycle\": null,\n\
    \      \"cooling_temperature\": null,\n      \"growth_conditions\": null\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz111\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf\"\
    ,\n        \"source_locator\": \"Primary preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix\
    \ after cooling.\",\n        \"snapshot_sha256\": \"0d5b2157ff931d8a898043364f6eceac7b58391b019feb8178247235195208d8\"\
    ,\n        \"parsed_text_sha256\": \"856dfc6e12a29587bd73fbbc5a3a1c82743b459d214c48e762426e05b651e6b6\"\
    \n      }\n    ],\n    \"interpretation\": \"The absence of these owner numerical\
    \ slots is intentional and source-faithful. No 50 ml/L dose, 200 g/L stock, 10\
    \ g/L final glucose or 1 L measured final volume may be inferred.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Complete local linkage and exact supplied forms
  outcome: supported
  summary: The target has ten primary and ten CHEBI-keyed secondary links across ten
    ingredient instances (100% linkage each, not correctness). Both owners additionally
    retain provider-specific distilled-water identity and generic nested glucose;
    water stock has no fabricated chemical ID. All asserted CHEBI labels/current MIM
    keys resolve, while the water provider ID resolves to the exact recipe object.
    Explicit Mg/Fe heptahydrates, Mn/Zn/Cu hexahydrates and sodium molybdate dihydrate
    agree with the source. Phosphate formulae agree; CHEBI:131527 synonym tension
    does not prove a hydrate. Generic glucose does not prove DL composition.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - primary
  - historical-raw
  - grounding-inventory
  - chebi17234
  - chebi131527
  - chebi63036
  - chebi31795
  - chebi75836
  - chebi131523
  - chebi132762
  - chebi91246
  - chebi75213
  - chebi2509
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 25 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: Exact accession and repaired source contributors
  outcome: supported
  summary: DSMZ 111 primary, recovered medium metadata, exact KOMODO mapping and reciprocal
    owner relationships identify the same source medium. Ingredient fingerprints alone
    do not establish historical equivalence, and unrelated similarly named reports
    are excluded.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - primary
  - historical-raw
  - catalog
  - record
  - owner-0
  - owner-1
- assessment_id: owner-repair
  area: quantity
  topic: Existing stage repair and generated lag
  outcome: concern
  summary: Both maintained owners already withdraw the mis-staged glucose rate, preserve
    10 g in 50 ml water, store 950 ml basal water, retain qualified provider basal
    rates and separately mix after cooling. These 27 attached claims authenticate
    to original raw. The target predates that repair and must be reconciled without
    duplicating or undoing it.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - historical-raw
  - history-inventory
  - quantity-inventory
  - writer-0
- assessment_id: preparation
  area: completeness
  topic: Staged water, required agar and unavailable conditions
  outcome: concern
  summary: Agar 15 g is required in this primary table, unlike conditional agar in
    medium 1215; no neighboring rule transfers. Both owner preparations are present;
    the target lacks them. Source does not quantify a final glucose stock volume,
    receiving dose, measured final-medium volume, sterilization method/time/temperature
    or cooling endpoint.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - primary
  - quantity-inventory
- assessment_id: biological-scope
  area: scope
  topic: Classification and growth boundaries
  outcome: supported
  summary: The chemical basal formulation and required agar support the selected defined
    solid preparation. No species-specific growth, nitrogen fixation or oxygen physiology
    is inferred from the medium title or catalog metadata.
  target_ids:
  - CultureMech:003822
  evidence_ids:
  - record
  - primary
  - catalog
findings:
- finding_id: f1
  issue_key: culturemech.003822.stale-glucose-and-preparation
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated target retains a withdrawn glucose rate
  description: The target stores 10.5263 g/L glucose without the separate preparation,
    two water inputs or basal denominator limits. Both maintained owners already contain
    the authenticated source-specific correction.
  target_ids:
  - CultureMech:003822
  field_paths:
  - ingredients[0].concentration
  - ingredients[*].notes
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - quantity-inventory
  - writer-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
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
  issue_key: culturemech.003822.generated-evidence-history-lag
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated target omits authenticated repair evidence
  description: The target lacks all 27 attached owner claims, source references and
    later repair history. This is an observed layer difference, not a universal defect
    assigned to the current guarded merger.
  target_ids:
  - CultureMech:003822
  field_paths:
  - ingredients[*].evidence
  - solutions
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
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
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
  issue_key: culturemech.003822.malformed-import-times
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO history has malformed and timezone-naive times
  description: Target and KOMODO owner retain .fZ and timezone-naive import/resolver
    timestamps. The source-specific repair correctly preserves those historical bytes;
    no replacement time is established.
  target_ids:
  - CultureMech:003822
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
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
  description: Preserve the repaired owners, verify their full formulation compatibility
    and regenerate the target through the current guarded path. Confirm separate glucose
    mass/water and basal qualifications survive; do not invent stock/final concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003822
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
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
  description: Preserve every owner claim, superseded explanation and original event
    when reconciling the generated layer; use exact field ownership and source stages
    as acceptance criteria.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003822
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/beijerinckia_medium.yaml
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
  description: Keep original history and append only a supported clarification rather
    than fabricating timestamp precision.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003822
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml
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
- Current mediadive111api returned HTTP 503. Complete primary and exact historical
  response are available; no unseen detail variant or complete historical equivalence
  is inferred.
- Current mediadive111api_retry returned HTTP 503. Complete primary and exact historical
  response are available; no unseen detail variant or complete historical equivalence
  is inferred.
- Current komodo111detail returned HTTP 403. Complete primary and exact historical
  response are available; no unseen detail variant or complete historical equivalence
  is inferred.
- Current primary and exact historical raw resolve the assessed material claims. Current
  API/detail failures do not themselves force partial coverage. No measured final
  volume, stock receiving dose, final glucose concentration or biological growth assertion
  is inferred.
- Historical reports are derivative. Their unrelated namesake records do not enter
  the ingredient inventory; current code is not historically replayed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-040
- generated-medium
```
