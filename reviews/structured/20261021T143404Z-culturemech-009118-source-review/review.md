# Source and formulation review: aminomonas_medium (CultureMech:009118)

- Review: 20261021T143404Z-culturemech-009118-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:22:46Z
- Finished UTC: 2026-10-21T14:34:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact TOGO M2549 and DSMZ846 identify Aminomonas medium. Both local layers flatten stock recipes and mix liquid, milligram and main-batch quantities; the vitamin endpoint 5788 is not the source-specific vitamin formulation. Available primary and provider sources permit a completed review while preserving their stock-strength differences and scoped strain variants.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 250; batch 025 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-four task batches contain 240 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 243 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009118 | data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml | generated | aminomonas_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009118 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009118 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/250/strict.tsv |
| validate-terms | passed | True | CultureMech:009118 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009118 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009118 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009118.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009118.

82 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "quantity": "Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3990.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "3990.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q2",
    "quantity": "Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "Yeast extract 2.00 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q3",
    "quantity": "NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "NaCl 1.00 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q4",
    "quantity": "CaCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "CaCl2 x 2 H2O 0.15 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"CaCl2 x 2 H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q5",
    "quantity": "KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "KH2PO4 0.30 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q6",
    "quantity": "NH4Cl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "NH4Cl 0.30 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q7",
    "quantity": "K2HPO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "K2HPO4 0.20 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q8",
    "quantity": "MgCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "MgCl2 x 6 H2O 0.40 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"MgCl2 x 6 H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q9",
    "quantity": "Na2S x 9 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2S x 9 H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q10",
    "quantity": "KCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "KCl 0.50 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[10]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q11",
    "quantity": "Na2CO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "Na2CO3 1.50 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[11]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q12",
    "quantity": "L-Serine",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "L-Serine 1.05 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[12]",
        "exact_source_quote": "\"component_name\": \"L-Serine\",\n          \"volume\": 1.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q13",
    "quantity": "L-Cysteine-HCl x H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe table: exact named row",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.50 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[13]",
        "exact_source_quote": "\"component_name\": \"L-Cysteine-HCl x H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Main receiving-batch input, retaining source g or mL with 1000 mL water and separate stocks. No measured final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three stock waters; do not sum these stages. The other main numeric amounts agree as batch grams, but their asserted final G_PER_L basis lacks support."
  },
  {
    "quantity_id": "q14",
    "quantity": "Carbon dioxide gas",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation: sparging gas sentence",
        "exact_source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Explicit main gas-mixture proportion 20% CO2, not a VARIABLE ingredient concentration or absolute gas dose. Preserve mixture and preparation scope; no extra percentage basis is invented."
  },
  {
    "quantity_id": "q15",
    "quantity": "Nitrogen gas",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation: sparging gas sentence",
        "exact_source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Explicit main gas-mixture proportion 80% N2, not a VARIABLE ingredient concentration or absolute gas dose. Preserve mixture and preparation scope; no extra percentage basis is invented."
  },
  {
    "quantity_id": "q16",
    "quantity": "Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "36",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q17",
    "quantity": "H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q18",
    "quantity": "MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2 x 4 H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q19",
    "quantity": "CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "190",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2 x 6 H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q20",
    "quantity": "NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "24",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2 x 6 H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q21",
    "quantity": "CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2 x 2 H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q22",
    "quantity": "ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "70",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "70",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q23",
    "quantity": "HCl (25%; 7.7 M)",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q24",
    "quantity": "FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 stock table: exact named row",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"FeCl2 x 4 H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "SL-10 stock input, not a main-medium concentration. Preserve source mg, g or mL and the separate explicit make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount or HCl liquid dose as G_PER_L in the medium."
  },
  {
    "quantity_id": "q25",
    "quantity": "Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Selenite-tungstate stock table: exact named row",
        "exact_source_quote": "Na2SeO3 x 5 H2O 3.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2SeO3 x 5 H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Separate selenite-tungstate stock input with 1000 mL water, dosed at 1 mL into the main recipe. Preserve mg/g and stage; do not transfer stock amounts directly to final G_PER_L."
  },
  {
    "quantity_id": "q26",
    "quantity": "Na2WO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Selenite-tungstate stock table: exact named row",
        "exact_source_quote": "Na2WO4 x 2 H2O 4.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2WO4 x 2 H2O\",\n          \"volume\": 4,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Separate selenite-tungstate stock input with 1000 mL water, dosed at 1 mL into the main recipe. Preserve mg/g and stage; do not transfer stock amounts directly to final G_PER_L."
  },
  {
    "quantity_id": "q27",
    "quantity": "NaOH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Selenite-tungstate stock table: exact named row",
        "exact_source_quote": "NaOH 0.50 g",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Separate selenite-tungstate stock input with 1000 mL water, dosed at 1 mL into the main recipe. Preserve mg/g and stage; do not transfer stock amounts directly to final G_PER_L."
  },
  {
    "quantity_id": "q28",
    "quantity": "Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q29",
    "quantity": "p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q30",
    "quantity": "Thiamine-HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q31",
    "quantity": "Pyridoxine-HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q32",
    "quantity": "Folic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q33",
    "quantity": "Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[32].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q34",
    "quantity": "Riboflavin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[33].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q35",
    "quantity": "Nicotinic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[34].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[34].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q36",
    "quantity": "Lipoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[35].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[35].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q37",
    "quantity": "D-Ca-pantothenate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[36].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[36].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Wolin tenfold vitamin stock table: exact named row",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[10]",
        "exact_source_quote": "\"component_name\": \"D-Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Preserve both source versions: TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree, but this does not authenticate endpoint 5788 or erase chemical-form and version distinctions. These stock milligram quantities are not direct main-medium G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies DL-alpha-lipoic acid."
  },
  {
    "quantity_id": "q38",
    "quantity": "Vitamin-stock nitrogen atmosphere",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[37].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[37].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[11]",
        "exact_source_quote": "\"component_name\": \"N2 gas\",\n          \"conc_value\": 100,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      },
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation: separately prepared later stocks",
        "exact_source_quote": "sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "The TOGO vitamin-stock row explicitly specifies 100% N2 and the primary separately gives this atmosphere for later serine/vitamin/cysteine/sulfide stocks. Preserve stock atmosphere rather than a duplicate unqualified main ingredient; no absolute gas quantity is stated."
  },
  {
    "quantity_id": "q39",
    "quantity": "Na-resazurin solution (0.1% w/v)",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe: exact stock-addition row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Receiving-batch liquid dose in mL; current G_PER_L is incompatible with the source unit. Preserve source stock definition separately, with no density or measured-final-volume assumption."
  },
  {
    "quantity_id": "q40",
    "quantity": "Trace element solution SL-10",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe: exact stock-addition row",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[14]",
        "exact_source_quote": "\"component_name\": \"Trace element solution SL-10\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Receiving-batch liquid dose in mL; current G_PER_L is incompatible with the source unit. Preserve source stock definition separately, with no density or measured-final-volume assumption."
  },
  {
    "quantity_id": "q41",
    "quantity": "Selenite-tungstate solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe: exact stock-addition row",
        "exact_source_quote": "Selenite-tungstate solution 1.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[15]",
        "exact_source_quote": "\"component_name\": \"Selenite-tungstate solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Receiving-batch liquid dose in mL; current G_PER_L is incompatible with the source unit. Preserve source stock definition separately, with no density or measured-final-volume assumption."
  },
  {
    "quantity_id": "q42",
    "quantity": "Vitamin receiving dose and source version",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe vitamin addition",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[16]",
        "exact_source_quote": "\"component_name\": \"Vitamins solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "TOGO explicitly uses 10 mL of its onefold stock; DSMZ uses 1 mL of the defined tenfold stock. Local 10 G_PER_L is wrong as a unit, and linking 10 mL to endpoint 5788 silently changes source strength/forms. Retain the source-version choice and stock-dose pair; do not combine one source dose with another stock."
  },
  {
    "quantity_id": "q43",
    "quantity": "SL-10 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 water: exact stock table water row",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Separate stock solvent input missing from the receiving solution structure. Existing 3990 water aggregates incompatible stages and is not this exact scoped field. Do not infer measured final volume from water input alone."
  },
  {
    "quantity_id": "q44",
    "quantity": "Selenite-tungstate water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[2].composition",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Selenite-tungstate water: exact stock table water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Separate stock solvent input missing from the receiving solution structure. Existing 3990 water aggregates incompatible stages and is not this exact scoped field. Do not infer measured final volume from water input alone."
  },
  {
    "quantity_id": "q45",
    "quantity": "Vitamin stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[3].composition",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[3].composition",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Vitamin stock water: exact stock table water row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Separate stock solvent input missing from the receiving solution structure. Existing 3990 water aggregates incompatible stages and is not this exact scoped field. Do not infer measured final volume from water input alone."
  },
  {
    "quantity_id": "q46",
    "quantity": "SL-10 final make-up volume",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[1].preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[1].preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 preparation: final make-up sentence",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Explicit stock make-up to 1000 mL; distinct from the 990 mL initial water and receiving 1 mL dose."
  },
  {
    "quantity_id": "q47",
    "quantity": "Sodium resazurin stock strength",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "Na-resazurin solution (0.1% w/v)"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "Na-resazurin solution (0.1% w/v)"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main recipe stock-addition row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "Existing stock name correctly preserves 0.1% w/v but lacks attached evidence. This is stock strength; dose 0.50 mL is separately assessed."
  },
  {
    "quantity_id": "q48",
    "quantity": "SL-10 hydrochloric acid percentage",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[22].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[22].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "SL-10 acid row",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "The name preserves 25% reagent strength; percentage basis is not specified by either source. It is not final-medium concentration and does not independently support provider 2.5 g/L HCl."
  },
  {
    "quantity_id": "q49",
    "quantity": "TOGO hydrochloric acid molarity",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ingredients[22].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ingredients[22].preferred_term",
        "stored": "HCl (25%; 7.7 M)"
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM2549",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec"
      }
    ],
    "source_stage_and_basis": "TOGO explicitly names 7.7 M in the reagent description. Preserve that source-specific assertion and its stock stage; DSMZ846 prints 25% only and no molarity is inferred from percentage."
  },
  {
    "quantity_id": "q50",
    "quantity": "Main sparging duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation sparging sentence",
        "exact_source_quote": "sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Source-only scoped condition or variant. Preserve range, conditional language, denominator and strain label exactly. The two strain variants do not alter the base recipe for all uses and are not independent experimental growth assertions."
  },
  {
    "quantity_id": "q51",
    "quantity": "Main vessel filling fraction",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation distribution sentence",
        "exact_source_quote": "serum vials to 30% of their volume and autoclave.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Source-only scoped condition or variant. Preserve range, conditional language, denominator and strain label exactly. The two strain variants do not alter the base recipe for all uses and are not independent experimental growth assertions."
  },
  {
    "quantity_id": "q52",
    "quantity": "Carbonate-stock gas atmosphere",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation carbonate-stock sentence",
        "exact_source_quote": "from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Source-only scoped condition or variant. Preserve range, conditional language, denominator and strain label exactly. The two strain variants do not alter the base recipe for all uses and are not independent experimental growth assertions."
  },
  {
    "quantity_id": "q53",
    "quantity": "Base complete-medium pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation complete-medium pH sentence",
        "exact_source_quote": "medium to 7.2, if necessary.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Source-only scoped condition or variant. Preserve range, conditional language, denominator and strain label exactly. The two strain variants do not alter the base recipe for all uses and are not independent experimental growth assertions."
  },
  {
    "quantity_id": "q54",
    "quantity": "DSM12260 replacement substrate",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "DSM12260-specific variant sentence",
        "exact_source_quote": "For DSM 12260: Replace L-Serine with 1.74 g/l L-Arginine x HCl.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Source-only scoped condition or variant. Preserve range, conditional language, denominator and strain label exactly. The two strain variants do not alter the base recipe for all uses and are not independent experimental growth assertions."
  },
  {
    "quantity_id": "q55",
    "quantity": "DSM27871 variant pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "DSM27871-specific variant sentence",
        "exact_source_quote": "For DSM 27871: Adjust the pH of the complete medium to 7.8.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "Source-only scoped condition or variant. Preserve range, conditional language, denominator and strain label exactly. The two strain variants do not alter the base recipe for all uses and are not independent experimental growth assertions."
  },
  {
    "quantity_id": "q56",
    "quantity": "Unspecified autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "sterilization_method",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "sterilization_method",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation autoclave instruction",
        "exact_source_quote": "serum vials to 30% of their volume and autoclave.",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "The source states autoclaving but supplies no numerical temperature/time. Vitamin filtration is separate. No cycle from parent media is transferred."
  },
  {
    "quantity_id": "q57",
    "quantity": "Unspecified later-stock strengths and doses",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation later-additions sentence",
        "exact_source_quote": "serum vials to 30% of their volume and autoclave. Add serine, vitamins, cysteine, and",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      },
      {
        "source_key": "dsmz846",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf",
        "source_locator": "Main preparation later stock atmosphere",
        "exact_source_quote": "sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and carbonate",
        "snapshot_sha256": "83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b",
        "parsed_text_sha256": "ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b"
      }
    ],
    "source_stage_and_basis": "The main table provides amounts of serine, cysteine, sulfide and carbonate, but their separately prepared stock concentrations and liquid injection volumes are not specified. The vitamin stock and dose are separately quantified; no missing stock strength or volume is invented."
  },
  {
    "quantity_id": "q58",
    "quantity": "Provider declared main volume",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadive846api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/846",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1003",
        "snapshot_sha256": "cac25c80f54f1fc9388bc9ebb10776d1d498fe035d8b24df8bf4f13662c7f532"
      }
    ],
    "source_stage_and_basis": "This provider metadata is not a measured final-medium volume. It must not override explicit source batch inputs, stock make-up or source-specific vitamin dosage."
  },
  {
    "quantity_id": "q59",
    "quantity": "solution4178: HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q60",
    "quantity": "solution4178: FeCl2 x 4 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q61",
    "quantity": "solution4178: ZnCl2",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q62",
    "quantity": "solution4178: MnCl2 x 4 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q63",
    "quantity": "solution4178: H3BO3",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q64",
    "quantity": "solution4178: CoCl2 x 6 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q65",
    "quantity": "solution4178: CuCl2 x 2 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q66",
    "quantity": "solution4178: NiCl2 x 6 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q67",
    "quantity": "solution4178: Na2MoO4 x 2 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[8].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q68",
    "quantity": "solution4178: Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml",
        "field_path": "composition[9].concentration",
        "stored": {
          "value": "990",
          "unit": "PERCENT_V_V"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution4178",
        "source_url": "https://mediadive.dsmz.de/rest/solution/4178",
        "source_locator": "$.data.recipe[9]",
        "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q69",
    "quantity": "solution5543: NaOH",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q70",
    "quantity": "solution5543: Na2SeO3 x 5 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q71",
    "quantity": "solution5543: Na2WO4 x 2 H2O",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q72",
    "quantity": "solution5543: Distilled water",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5543",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5543",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q73",
    "quantity": "solution5788: Biotin",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[0].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[0]",
        "exact_source_quote": "{\n                \"recipe_order\": 1,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q74",
    "quantity": "solution5788: Folic acid",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[1].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[1]",
        "exact_source_quote": "{\n                \"recipe_order\": 2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\": 138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q75",
    "quantity": "solution5788: Pyridoxine hydrochloride",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[2]",
        "exact_source_quote": "{\n                \"recipe_order\": 3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"B6\",\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q76",
    "quantity": "solution5788: Riboflavine",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[3].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[3]",
        "exact_source_quote": "{\n                \"recipe_order\": 4,\n                \"compound\": \"Riboflavine\",\n                \"compound_id\": 616,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"B2\",\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q77",
    "quantity": "solution5788: Thiamine",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[4].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[4]",
        "exact_source_quote": "{\n                \"recipe_order\": 5,\n                \"compound\": \"Thiamine\",\n                \"compound_id\": 666,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"B1\",\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.188423,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q78",
    "quantity": "solution5788: Nicotinic acid",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[5].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[5]",
        "exact_source_quote": "{\n                \"recipe_order\": 6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"PP\",\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q79",
    "quantity": "solution5788: Pantothenic acid",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[6].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[6]",
        "exact_source_quote": "{\n                \"recipe_order\": 7,\n                \"compound\": \"Pantothenic acid\",\n                \"compound_id\": 135,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.228071,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q80",
    "quantity": "solution5788: Cobalamin",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[7].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[7]",
        "exact_source_quote": "{\n                \"recipe_order\": 8,\n                \"compound\": \"Cobalamin\",\n                \"compound_id\": 2157,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"B12\",\n                \"amount\": 1,\n                \"unit\": \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": []
  },
  {
    "quantity_id": "q81",
    "quantity": "solution5788: p-Aminobenzoic acid",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[8].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[8]",
        "exact_source_quote": "{\n                \"recipe_order\": 9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  },
  {
    "quantity_id": "q82",
    "quantity": "solution5788: Lipoic acid",
    "decision": "verified",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml",
        "field_path": "composition[9].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "solution5788",
        "source_url": "https://mediadive.dsmz.de/rest/solution/5788",
        "source_locator": "$.data.recipe[9]",
        "exact_source_quote": "{\n                \"recipe_order\": 10,\n                \"compound\": \"Lipoic acid\",\n                \"compound_id\": 368,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\": 0\n            }",
        "snapshot_sha256": "3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d"
      }
    ],
    "source_stage_and_basis": "Context dependency only. Existing matching evidence supports the provider-declared within-stock basis, or water batch dose, at this exact composition field. It does not establish receiving-medium concentration or source-stock interchangeability. Unattached otherwise matching provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally distinct from both source vitamin recipes.",
    "existing_evidence_indices": [
      0
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:009118.

35 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 35/38 primary and 32/38 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 38: primary 92.11%; secondary 84.21%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009118.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accession and single maintained contributor

identity: supported. Targets: CultureMech:009118.

TOGO M2549 names DSMZ846 and the same Aminomonas medium. The generated target and exact maintained contributor share the stable CultureMech ID. Exact dependency files and endpoint IDs resolve; their composition and transfer scope are separately assessed. No historical variant identity or experimental organism-growth assertion is inferred from a name.

### Source-specific salt, hydrate and stereochemical forms

grounding: concern. Targets: CultureMech:009118.

Most named hydrates, L-serine and L-cysteine hydrochloride hydrate agree with their asserted forms. Nickel hexahydrate is mapped to anhydrous CHEBI:34887 in both medium layers and local SL-10 context. Both TOGO and DSMZ explicitly support D-calcium pantothenate; its source-specific D naming is not an unresolved stereochemical issue. Generic lipoic acid grounding does not preserve DSMZ explicit DL-alpha mixture wording, which should remain in source notes rather than an invented single-enantiomer ID. Source vitamin B12 remains generic. Endpoint5788 pantothenic acid and thiamine forms differ from the source calcium salt and hydrochloride.

### Named stock references, existing evidence and vitamin version

representation: concern. Targets: CultureMech:009118.

Local SL-10 and selenite-tungstate files contain real compositions despite placeholder ingredients and historical incomplete flags. Their 17 audited evidence objects support only exact existing stock fields. Endpoint5788 has tenfold-scale numbers but pantothenic acid and thiamine forms and no water recipe row; it is not established as TOGO onefold stock or DSMZ Wolin10x5980. Numeric stock-dose scaling alone cannot establish chemical identity.

### Ordered preparation and conditional variant coverage

completeness: concern. Targets: CultureMech:009118.

Both medium layers omit preparation, pH and amount evidence. Main gas mixture, sparging duration, vessel fraction, late additions under separate gas atmospheres, vitamin filtration and complete-medium pH are explicitly available. DSM12260 substrate replacement and DSM27871 pH are separate source variants, not universal base changes. Only named stock sections of DSM320/385/120 transfer.

### Physical class, application and composition-derived metadata

scope: concern. Targets: CultureMech:009118.

Bacterial, liquid, complex/undefined classification is consistent with the yeast-containing base recipe. Generic cultivation application is not an experimental strain-growth claim. No taxonomy, DOI, PMID or KG match is asserted. high_metal requires reassessment only after stock and final-medium quantities are reconstructed under its schema contract; the current true flag is not independently supported by these flattened values.

## Findings

### f1: Stock amounts, liquid units and water stages are flattened

blocker / open / confirmed; issue key: cm009118-stock-flattening.

Both medium layers flatten SL-10, selenite-tungstate and vitamin stock inputs into main ingredients. Milligram stock amounts are stored as G_PER_L, liquid additions are G_PER_L, and 3990 G_PER_L water combines four distinct stages. Even otherwise matching main gram values need their source batch basis rather than an assumed measured final liter.

### f2: The vitamin endpoint does not establish the source stock

major / open / confirmed; issue key: cm009118-vitamin-endpoint.

Local endpoint5788 is attached to a TOGO dose of 10 with a mass unit. TOGO defines onefold vitamin amounts at 10 mL; DSMZ defines Wolin tenfold5980 at 1 mL. Endpoint5788 uses distinct pantothenic acid and thiamine forms. Its existing amount evidence validates its own recipe, not this medium link.

### f3: Nickel hexahydrate is grounded to anhydrous nickel dichloride

major / open / confirmed; issue key: cm009118-nickel-hydrate.

The exact primary and TOGO SL-10 rows specify NiCl2 x 6 H2O. Both medium layers assert CHEBI:34887 and the same secondary key, whose captured ontology formula is Cl2Ni. The local SL-10 dependency has the same supplied-form mismatch. Canonical label validity does not cure this structural mismatch.

### f4: Preparation, pH and conditional source variants are absent

major / open / confirmed; issue key: cm009118-preparation-evidence.

Both local layers omit available ordered preparation, scoped gas conditions, pH and variant distinctions. Unknown solution names obscure supported definitions. Source-only DSM12260 and DSM27871 instructions must remain distinct from the base recipe; a generic cultivation application is not growth evidence.

### f5: Composition-derived high-metal flag lacks a reliable quantity basis

minor / open / confirmed; issue key: cm009118-derived-metal-flag.

The high_metal flag is asserted in both medium layers while stock inputs and units are materially malformed. Its schema-defined quantitative criterion cannot be authenticated from this representation. This review does not infer a corrected total or boolean.

## Recommended Actions And Acceptance Checks

### a1

Reconcile the maintained owner with explicit source units and stock stages, then regenerate the merged record. Preserve source-version stock-dose pairs, actual make-up instructions and all unresolved final-volume bases without inventing densities.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Every target and owner concentration is reconciled to its source-stage inventory decision.

### a2

Resolve the intended source version and exact vitamin stock identity before attaching a stock ID. Preserve D-calcium pantothenate, thiamine hydrochloride and source mixture wording; keep original source-dose relationships and attach claim-level evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- No cross-source stock strength or form is inferred solely from matching names or numeric scaling.

### a3

Ground the source hexahydrate to a verified exact form or retain an explicit unresolved form without the contradictory identity. Reconcile the corresponding secondary mapping and scoped stock context; do not invent a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- A valid source-to-hydrate correspondence supports the eventual primary and secondary terms.

### a4

Represent the available preparation stages and variant-specific instructions with exact source evidence in the maintained owner. Attach amount evidence at the correct layer; retain unspecified cycle/doses and avoid importing unrelated parent media.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Base conditions and both source variants remain distinguishable and every preparation quantity retains its exact denominator.

### a5

Reassess the derived classification after source-grounded stock and receiving-medium quantities are represented; retain the numerical criterion and calculation provenance.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Derived classification is tied to corrected source-scoped quantities rather than flattened stock values.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch025/250/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/250/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml:1:id: CultureMech:009118<br>./data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml:1:id: CultureMech:009118<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/250/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 51 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf; Both pages: main table, complete preparation, two DSM strain variants, SL-10, selenite-tungstate and Wolin tenfold stock tables | supports | The exact primary defines all source stages and conditional variants. Stock tables are separate from their receiving doses. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549; $.meta; all four component tables and comments | supports | The source-specific TOGO vitamin recipe has onefold amounts and a 10 mL dose. Its exact D-Ca-pantothenate wording supports D naming; the frozen preflight summary wording to the contrary is not adopted. |
| api | https://mediadive.dsmz.de/rest/medium/846; $.data.medium; four solution recipes and all preparation steps | supports | Current DSMZ provider uses tenfold vitamin stock 5980 at 1 mL, not local endpoint 5788. Declared main volume 1003 mL is provider bookkeeping, not an independently measured final volume. |
| dsmz320 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; SL-10 subsection only | supports | This exact parent source confirms the named transferred stock only. Parent basal recipes, other stocks, preparation defaults and strain variants are outside this target. |
| dsmz385 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf; Selenite-tungstate subsection only | supports | This exact parent source confirms the named transferred stock only. Parent basal recipes, other stocks, preparation defaults and strain variants are outside this target. |
| dsmz120 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf; Wolin tenfold vitamin subsection only | supports | This exact parent source confirms the named transferred stock only. Parent basal recipes, other stocks, preparation defaults and strain variants are outside this target. |
| solution4178 | https://mediadive.dsmz.de/rest/solution/4178; Exact endpoint identity, entire recipe and stock-specific preparation | supports | Endpoint existence and exact recipe checked. Matching names do not establish interchangeability; the inventory separates existing local stock claims from target/owner claims. |
| solution5543 | https://mediadive.dsmz.de/rest/solution/5543; Exact endpoint identity, entire recipe and stock-specific preparation | supports | Endpoint existence and exact recipe checked. Matching names do not establish interchangeability; the inventory separates existing local stock claims from target/owner claims. |
| solution5788 | https://mediadive.dsmz.de/rest/solution/5788; Exact endpoint identity, entire recipe and stock-specific preparation | supports | Endpoint existence and exact recipe checked. Matching names do not establish interchangeability; the inventory separates existing local stock claims from target/owner claims. |
| solution595 | https://mediadive.dsmz.de/rest/solution/595; Exact endpoint identity, entire recipe and stock-specific preparation | supports | Endpoint existence and exact recipe checked. Matching names do not establish interchangeability; the inventory separates existing local stock claims from target/owner claims. |
| solution777 | https://mediadive.dsmz.de/rest/solution/777; Exact endpoint identity, entire recipe and stock-specific preparation | supports | Endpoint existence and exact recipe checked. Matching names do not establish interchangeability; the inventory separates existing local stock claims from target/owner claims. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; Exact endpoint identity, entire recipe and stock-specific preparation | supports | Endpoint existence and exact recipe checked. Matching names do not establish interchangeability; the inventory separates existing local stock claims from target/owner claims. |
| dependency-claims | /private/tmp/culturemech-review-work-batch025/250/dependency-evidence-audit.json; All 17 existing attached composition claims in three named stock files | supports | Eight SL-10, four selenite-tungstate and five vitamin-endpoint claims have exact literal raw snippets and matching historical/current response hashes. Their original access times and narrow stock denominators remain intact; none is attached to the target or maintained medium owner. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch025/250/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17115 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17115; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17115 resolves to L-serine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17115": [{"label": "L-Serine", "match_type": "preferred_term", "identifier": "CHEBI:17115", "preferred_term": "L-Serine", "ontology_id": "CHEBI:17115", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| context-chebi18385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18385; Exact OLS label, formula, charge and structure of local endpoint5788 term | supports | Context endpoint forms are not substitutes for source thiamine hydrochloride, calcium D-pantothenate or unspecified vitamin B12. No replacement ontology ID is inferred. |
| context-chebi7916 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_7916; Exact OLS label, formula, charge and structure of local endpoint5788 term | supports | Context endpoint forms are not substitutes for source thiamine hydrochloride, calcium D-pantothenate or unspecified vitamin B12. No replacement ontology ID is inferred. |
| context-chebi28911 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28911; Exact OLS label, formula, charge and structure of local endpoint5788 term | supports | Context endpoint forms are not substitutes for source thiamine hydrochloride, calcium D-pantothenate or unspecified vitamin B12. No replacement ontology ID is inferred. |
| high-metal-contract | src/culturemech/schema/culturemech.yaml; MediaRecipe.high_metal slot description; threshold and counted elements | context_only | The schema defines a numerical composition-derived metal threshold. Current malformed stock/final quantities cannot authenticate this derived annotation. No replacement boolean or total is guessed. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, stock handling, cleanup and formulation guards read. Current cleanup does not sum duplicates; this code is contextual and does not prove the exact historical transformation. Preserve old events and append any later authorized correction. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, stock handling, cleanup and formulation guards read. Current cleanup does not sum duplicates; this code is contextual and does not prove the exact historical transformation. Preserve old events and append any later authorized correction. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, stock handling, cleanup and formulation guards read. Current cleanup does not sum duplicates; this code is contextual and does not prove the exact historical transformation. Preserve old events and append any later authorized correction. |
| writer-3 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer, stock handling, cleanup and formulation guards read. Current cleanup does not sum duplicates; this code is contextual and does not prove the exact historical transformation. Preserve old events and append any later authorized correction. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Available primary and provider evidence resolves the scientific source scope sufficiently for completed review. Source-version differences remain explicit; completion does not mean the local formulation is correct.
- Neither source supplies a measured final-medium volume, a numerical main autoclave cycle, or every separately prepared stock strength/injection volume. HCl 25% has no explicit percentage basis. No such values are inferred.
- Both exact TOGO and DSMZ sources support D-calcium pantothenate. A contradictory provisional summary was superseded by the independent raw-source audit; frozen captures remain unchanged.
- Dependency files are context only: their attached evidence and historical timestamps are not inherited by the target. Existing placeholder ingredients and incomplete flags do not imply that their populated composition arrays are absent. No parent-medium conditions or unrelated legacy ingredient claims transfer.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143404Z-culturemech-009118-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aminomonas_medium (CultureMech:009118)'
started_at: '2026-10-21T14:22:46Z'
finished_at: '2026-10-21T14:34:04Z'
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
summary: Exact TOGO M2549 and DSMZ846 identify Aminomonas medium. Both local layers
  flatten stock recipes and mix liquid, milligram and main-batch quantities; the vitamin
  endpoint 5788 is not the source-specific vitamin formulation. Available primary
  and provider sources permit a completed review while preserving their stock-strength
  differences and scoped strain variants.
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
  - path: data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
    sha256: 4742d02a506ecf48ebf626dbddea07f1e3822cdac0071ed55f8a25bae69655e0
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
    sha256: 524bec08c535cdf414b2f312f09e7f157558995497de3c41ce12c7275b652ade
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
    sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml
    sha256: 8af8e33a13d8ef0de04decee6f5f1191c2f3263bb1cd10204c53770ed4122c1d
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
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
  selection: Task review 250; batch 025 item 10 of 10, selected in Python lexicographic
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
  - CultureMech:009118
targets:
- target_id: CultureMech:009118
  path: data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  label: aminomonas_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch025/250/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/250/strict.tsv"
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009118
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
  - CultureMech:009118
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:24:01.523689Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch025/250/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:24:03.118122Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/250/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:24:04.859358Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:24:06.150654Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:34:02Z'
  support: supports
  summary: './data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml:1:id: CultureMech:009118

    ./data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml:1:id: CultureMech:009118

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/250/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:34:02Z'
  support: supports
  summary: 51 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: d970ad93c1ab10c0f3294f26fe32dfc42d86229f04cdd51326e458f5897fb5dc
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf
  locator: 'Both pages: main table, complete preparation, two DSM strain variants,
    SL-10, selenite-tungstate and Wolin tenfold stock tables'
  accessed_at: '2026-10-21T14:01:45.859252Z'
  support: supports
  summary: The exact primary defines all source stages and conditional variants. Stock
    tables are separate from their receiving doses.
  quote: Wolin's vitamin solution (10x) 1.00 ml
  snapshot_sha256: 83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549
  locator: $.meta; all four component tables and comments
  accessed_at: '2026-10-21T14:01:45.056072Z'
  support: supports
  summary: The source-specific TOGO vitamin recipe has onefold amounts and a 10 mL
    dose. Its exact D-Ca-pantothenate wording supports D naming; the frozen preflight
    summary wording to the contrary is not adopted.
  quote: '"component_name": "D-Ca-pantothenate"'
  snapshot_sha256: 1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/846
  locator: $.data.medium; four solution recipes and all preparation steps
  accessed_at: '2026-10-21T14:01:43.149014Z'
  support: supports
  summary: Current DSMZ provider uses tenfold vitamin stock 5980 at 1 mL, not local
    endpoint 5788. Declared main volume 1003 mL is provider bookkeeping, not an independently
    measured final volume.
  snapshot_sha256: cac25c80f54f1fc9388bc9ebb10776d1d498fe035d8b24df8bf4f13662c7f532
- evidence_id: dsmz320
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: SL-10 subsection only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: supports
  summary: This exact parent source confirms the named transferred stock only. Parent
    basal recipes, other stocks, preparation defaults and strain variants are outside
    this target.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: dsmz385
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf
  locator: Selenite-tungstate subsection only
  accessed_at: '2026-10-21T13:20:08.153235Z'
  support: supports
  summary: This exact parent source confirms the named transferred stock only. Parent
    basal recipes, other stocks, preparation defaults and strain variants are outside
    this target.
  snapshot_sha256: d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22
- evidence_id: dsmz120
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf
  locator: Wolin tenfold vitamin subsection only
  accessed_at: '2026-10-21T13:16:27.298931Z'
  support: supports
  summary: This exact parent source confirms the named transferred stock only. Parent
    basal recipes, other stocks, preparation defaults and strain variants are outside
    this target.
  snapshot_sha256: e1f85e4a546abc825218226bbb18d78bd9c054b7e11399aa7161ad259a3b663f
- evidence_id: solution4178
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4178
  locator: Exact endpoint identity, entire recipe and stock-specific preparation
  accessed_at: '2026-10-21T14:01:44.522797Z'
  support: supports
  summary: Endpoint existence and exact recipe checked. Matching names do not establish
    interchangeability; the inventory separates existing local stock claims from target/owner
    claims.
  snapshot_sha256: 7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da
- evidence_id: solution5543
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5543
  locator: Exact endpoint identity, entire recipe and stock-specific preparation
  accessed_at: '2026-10-21T14:01:44.555275Z'
  support: supports
  summary: Endpoint existence and exact recipe checked. Matching names do not establish
    interchangeability; the inventory separates existing local stock claims from target/owner
    claims.
  snapshot_sha256: 7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882
- evidence_id: solution5788
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5788
  locator: Exact endpoint identity, entire recipe and stock-specific preparation
  accessed_at: '2026-10-21T14:01:44.560559Z'
  support: supports
  summary: Endpoint existence and exact recipe checked. Matching names do not establish
    interchangeability; the inventory separates existing local stock claims from target/owner
    claims.
  snapshot_sha256: 3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d
- evidence_id: solution595
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/595
  locator: Exact endpoint identity, entire recipe and stock-specific preparation
  accessed_at: '2026-10-21T11:03:05.357684Z'
  support: supports
  summary: Endpoint existence and exact recipe checked. Matching names do not establish
    interchangeability; the inventory separates existing local stock claims from target/owner
    claims.
  snapshot_sha256: 5dd4cef59e15c0ab7d35e8a89039c7f7133ff8cd08ab6c414cf52d5e48c9aeab
- evidence_id: solution777
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/777
  locator: Exact endpoint identity, entire recipe and stock-specific preparation
  accessed_at: '2026-10-21T13:20:07.510517Z'
  support: supports
  summary: Endpoint existence and exact recipe checked. Matching names do not establish
    interchangeability; the inventory separates existing local stock claims from target/owner
    claims.
  snapshot_sha256: 3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: Exact endpoint identity, entire recipe and stock-specific preparation
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Endpoint existence and exact recipe checked. Matching names do not establish
    interchangeability; the inventory separates existing local stock claims from target/owner
    claims.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: dependency-claims
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/250/dependency-evidence-audit.json
  locator: All 17 existing attached composition claims in three named stock files
  accessed_at: '2026-10-21T14:34:02Z'
  support: supports
  summary: Eight SL-10, four selenite-tungstate and five vitamin-endpoint claims have
    exact literal raw snippets and matching historical/current response hashes. Their
    original access times and narrow stock denominators remain intact; none is attached
    to the target or maintained medium owner.
  snapshot_sha256: f1a375f7dc9986a63df9c44eaf247580605dd910dea60e03a239700d3dfa99eb
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/250/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 44c6865a8e5741301977f6e6d4937c3b4704dfccd84bb6bf68df239920bdb270
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
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
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
- evidence_id: chebi17115
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17115
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T14:01:45.898684Z'
  support: supports
  summary: CHEBI:17115 resolves to L-serine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 76fbf17336bdbaf863b725127c24ac48cf7a9be179ce1f38553e53147e1599fd
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
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
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
- evidence_id: chebi32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.263004Z'
  support: supports
  summary: CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
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
- evidence_id: chebi49976
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:04:44.168295Z'
  support: supports
  summary: CHEBI:49976 resolves to zinc dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
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
- evidence_id: chebi86249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.693358Z'
  support: supports
  summary: CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
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
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T14:34:02Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid",
    "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term":
    "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label":
    "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494",
    "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type":
    "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin",
    "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17115": [{"label": "L-Serine", "match_type": "preferred_term", "identifier":
    "CHEBI:17115", "preferred_term": "L-Serine", "ontology_id": "CHEBI:17115", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid",
    "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier":
    "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type":
    "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate
    solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id":
    "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961":
    [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier":
    "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label":
    "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term":
    "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label":
    "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term":
    "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term",
    "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id":
    "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976":
    [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976",
    "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate",
    "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term":
    "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type":
    "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id":
    "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345":
    [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier":
    "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248":
    [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml", "events":
    13, "timestamp_issues": []}]'
- evidence_id: context-chebi18385
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_18385
  locator: Exact OLS label, formula, charge and structure of local endpoint5788 term
  accessed_at: '2026-10-21T14:01:46.554275Z'
  support: supports
  summary: Context endpoint forms are not substitutes for source thiamine hydrochloride,
    calcium D-pantothenate or unspecified vitamin B12. No replacement ontology ID
    is inferred.
  snapshot_sha256: 381bccc107dc0fa306b0cdf5f01bdda3c10bd305626ec808c79beb7a8cc440dc
- evidence_id: context-chebi7916
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_7916
  locator: Exact OLS label, formula, charge and structure of local endpoint5788 term
  accessed_at: '2026-10-21T09:01:28.387666Z'
  support: supports
  summary: Context endpoint forms are not substitutes for source thiamine hydrochloride,
    calcium D-pantothenate or unspecified vitamin B12. No replacement ontology ID
    is inferred.
  snapshot_sha256: 7b057eb0f384350a666b22dce9bd0529405271e968b5fe5fb69c63d74cc14122
- evidence_id: context-chebi28911
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28911
  locator: Exact OLS label, formula, charge and structure of local endpoint5788 term
  accessed_at: '2026-10-21T14:01:46.583110Z'
  support: supports
  summary: Context endpoint forms are not substitutes for source thiamine hydrochloride,
    calcium D-pantothenate or unspecified vitamin B12. No replacement ontology ID
    is inferred.
  snapshot_sha256: 1512161433dff94b331ccbfa1b7a32ff1b8fbc7913ccf4c0c5a5d625eba3b617
- evidence_id: high-metal-contract
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediaRecipe.high_metal slot description; threshold and counted elements
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: The schema defines a numerical composition-derived metal threshold. Current
    malformed stock/final quantities cannot authenticate this derived annotation.
    No replacement boolean or total is guessed.
  snapshot_sha256: 64a778108fd3197a8cc08082f80c1de3ec33eda58350cee5df612ab61d23cea1
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Current importer, stock handling, cleanup and formulation guards read.
    Current cleanup does not sum duplicates; this code is contextual and does not
    prove the exact historical transformation. Preserve old events and append any
    later authorized correction.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Current importer, stock handling, cleanup and formulation guards read.
    Current cleanup does not sum duplicates; this code is contextual and does not
    prove the exact historical transformation. Preserve old events and append any
    later authorized correction.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Current importer, stock handling, cleanup and formulation guards read.
    Current cleanup does not sum duplicates; this code is contextual and does not
    prove the exact historical transformation. Preserve old events and append any
    later authorized correction.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:34:02Z'
  support: context_only
  summary: Current importer, stock handling, cleanup and formulation guards read.
    Current cleanup does not sum duplicates; this code is contextual and does not
    prove the exact historical transformation. Preserve old events and append any
    later authorized correction.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 82 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"quantity\": \"Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"3990.0\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3990.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input, retaining\
    \ source g or mL with 1000 mL water and separate stocks. No measured final-liter\
    \ denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three\
    \ stock waters; do not sum these stages. The other main numeric amounts agree\
    \ as batch grams, but their asserted final G_PER_L basis lacks support.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q2\",\n    \"quantity\": \"Yeast extract\",\n   \
    \ \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"Yeast extract 2.00 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"quantity\": \"NaCl\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"NaCl 1.00 g\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"quantity\": \"CaCl2 x 2 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.15\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"CaCl2 x 2 H2O 0.15 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 0.15,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input, retaining\
    \ source g or mL with 1000 mL water and separate stocks. No measured final-liter\
    \ denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three\
    \ stock waters; do not sum these stages. The other main numeric amounts agree\
    \ as batch grams, but their asserted final G_PER_L basis lacks support.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q5\",\n    \"quantity\": \"KH2PO4\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"KH2PO4 0.30 g\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"quantity\": \"NH4Cl\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"NH4Cl 0.30 g\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.3,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"quantity\": \"K2HPO4\",\n   \
    \ \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"K2HPO4 0.20 g\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"quantity\": \"MgCl2 x 6 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"MgCl2 x 6 H2O 0.40 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2 x 6 H2O\\\",\\n          \\\"volume\\\"\
    : 0.4,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input, retaining\
    \ source g or mL with 1000 mL water and separate stocks. No measured final-liter\
    \ denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three\
    \ stock waters; do not sum these stages. The other main numeric amounts agree\
    \ as batch grams, but their asserted final G_PER_L basis lacks support.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q9\",\n    \"quantity\": \"Na2S x 9 H2O\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S x 9 H2O\\\",\\n          \\\"volume\\\":\
    \ 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input, retaining\
    \ source g or mL with 1000 mL water and separate stocks. No measured final-liter\
    \ denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three\
    \ stock waters; do not sum these stages. The other main numeric amounts agree\
    \ as batch grams, but their asserted final G_PER_L basis lacks support.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q10\",\n    \"quantity\": \"KCl\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"KCl 0.50 g\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.5,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"quantity\": \"Na2CO3\",\n  \
    \  \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"Na2CO3 1.50 g\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"quantity\": \"L-Serine\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.05\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"L-Serine 1.05 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[12]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L-Serine\\\",\\n          \\\"volume\\\": 1.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input,\
    \ retaining source g or mL with 1000 mL water and separate stocks. No measured\
    \ final-liter denominator is supplied. Water 3990 G_PER_L incorrectly combines\
    \ main and three stock waters; do not sum these stages. The other main numeric\
    \ amounts agree as batch grams, but their asserted final G_PER_L basis lacks support.\"\
    \n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"quantity\": \"L-Cysteine-HCl\
    \ x H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[12].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe table: exact named row\",\n     \
    \   \"exact_source_quote\": \"L-Cysteine HCl x H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[13]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L-Cysteine-HCl x H2O\\\",\\n          \\\"volume\\\
    \": 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Main receiving-batch input, retaining\
    \ source g or mL with 1000 mL water and separate stocks. No measured final-liter\
    \ denominator is supplied. Water 3990 G_PER_L incorrectly combines main and three\
    \ stock waters; do not sum these stages. The other main numeric amounts agree\
    \ as batch grams, but their asserted final G_PER_L basis lacks support.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q14\",\n    \"quantity\": \"Carbon dioxide gas\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[13].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation: sparging gas sentence\",\n\
    \        \"exact_source_quote\": \"sparge medium with 80% N2 and 20% CO2 gas mixture\
    \ for 30 - 45 min to make it anoxic.\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Explicit main gas-mixture\
    \ proportion 20% CO2, not a VARIABLE ingredient concentration or absolute gas\
    \ dose. Preserve mixture and preparation scope; no extra percentage basis is invented.\"\
    \n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"quantity\": \"Nitrogen gas\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"variable\",\n          \"unit\": \"VARIABLE\"\n        }\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation: sparging gas sentence\",\n\
    \        \"exact_source_quote\": \"sparge medium with 80% N2 and 20% CO2 gas mixture\
    \ for 30 - 45 min to make it anoxic.\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Explicit main gas-mixture\
    \ proportion 80% N2, not a VARIABLE ingredient concentration or absolute gas dose.\
    \ Preserve mixture and preparation scope; no extra percentage basis is invented.\"\
    \n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"quantity\": \"Na2MoO4 x 2 H2O\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"36\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q17\",\n    \"quantity\": \"H3BO3\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a\
    \ main-medium concentration. Preserve source mg, g or mL and the separate explicit\
    \ make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock\
    \ amount or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q18\",\n    \"quantity\": \"MnCl2 x 4 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2 x 4 H2O\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q19\",\n    \"quantity\": \"CoCl2 x 6 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"190\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2 x 6 H2O\\\",\\n          \\\"volume\\\"\
    : 190,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q20\",\n    \"quantity\": \"NiCl2 x 6 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"24\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2 x 6 H2O\\\",\\n          \\\"volume\\\"\
    : 24,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q21\",\n    \"quantity\": \"CuCl2 x 2 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 2,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q22\",\n    \"quantity\": \"ZnCl2\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"70\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"70\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\":\
    \ \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 70,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a\
    \ main-medium concentration. Preserve source mg, g or mL and the separate explicit\
    \ make-up to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock\
    \ amount or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q23\",\n    \"quantity\": \"HCl (25%; 7.7 M)\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%; 7.7 M)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q24\",\n    \"quantity\": \"FeCl2 x 4 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 stock table: exact named row\",\n     \
    \   \"exact_source_quote\": \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2 x 4 H2O\\\",\\n          \\\"volume\\\"\
    : 1.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"SL-10 stock input, not a main-medium\
    \ concentration. Preserve source mg, g or mL and the separate explicit make-up\
    \ to 1000 mL; receiving dose is 1 mL. Do not reinterpret a milligram stock amount\
    \ or HCl liquid dose as G_PER_L in the medium.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q25\",\n    \"quantity\": \"Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table: exact named row\"\
    ,\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 3.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO3 x 5 H2O\\\",\\n          \\\"volume\\\"\
    : 3,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Separate selenite-tungstate stock input\
    \ with 1000 mL water, dosed at 1 mL into the main recipe. Preserve mg/g and stage;\
    \ do not transfer stock amounts directly to final G_PER_L.\"\n  },\n  {\n    \"\
    quantity_id\": \"q26\",\n    \"quantity\": \"Na2WO4 x 2 H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table: exact named row\"\
    ,\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 4.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4 x 2 H2O\\\",\\n          \\\"volume\\\"\
    : 4,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Separate selenite-tungstate stock input\
    \ with 1000 mL water, dosed at 1 mL into the main recipe. Preserve mg/g and stage;\
    \ do not transfer stock amounts directly to final G_PER_L.\"\n  },\n  {\n    \"\
    quantity_id\": \"q27\",\n    \"quantity\": \"NaOH\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table: exact named row\"\
    ,\n        \"exact_source_quote\": \"NaOH 0.50 g\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"volume\\\": 0.5,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Separate selenite-tungstate\
    \ stock input with 1000 mL water, dosed at 1 mL into the main recipe. Preserve\
    \ mg/g and stage; do not transfer stock amounts directly to final G_PER_L.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q28\",\n    \"quantity\": \"Biotin\",\n   \
    \ \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\":\
    \ \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Preserve both source versions:\
    \ TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than\
    \ 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products\
    \ agree, but this does not authenticate endpoint 5788 or erase chemical-form and\
    \ version distinctions. These stock milligram quantities are not direct main-medium\
    \ G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally\
    \ specifies DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q29\",\n\
    \    \"quantity\": \"p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n\
    \        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p-Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Preserve both source versions: TOGO\
    \ has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1\
    \ mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree,\
    \ but this does not authenticate endpoint 5788 or erase chemical-form and version\
    \ distinctions. These stock milligram quantities are not direct main-medium G_PER_L.\
    \ Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies\
    \ DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"quantity\"\
    : \"Thiamine-HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n       \
    \ \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine-HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Preserve both source versions: TOGO\
    \ has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1\
    \ mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree,\
    \ but this does not authenticate endpoint 5788 or erase chemical-form and version\
    \ distinctions. These stock milligram quantities are not direct main-medium G_PER_L.\
    \ Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies\
    \ DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"quantity\"\
    : \"Pyridoxine-HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\"\
    ,\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine-HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Preserve both source versions: TOGO\
    \ has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1\
    \ mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree,\
    \ but this does not authenticate endpoint 5788 or erase chemical-form and version\
    \ distinctions. These stock milligram quantities are not direct main-medium G_PER_L.\
    \ Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies\
    \ DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"quantity\"\
    : \"Folic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"\
    snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Preserve both source versions:\
    \ TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than\
    \ 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products\
    \ agree, but this does not authenticate endpoint 5788 or erase chemical-form and\
    \ version distinctions. These stock milligram quantities are not direct main-medium\
    \ G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally\
    \ specifies DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q33\",\n\
    \    \"quantity\": \"Vitamin B12\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[32].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"\
    snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Preserve both source versions:\
    \ TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than\
    \ 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products\
    \ agree, but this does not authenticate endpoint 5788 or erase chemical-form and\
    \ version distinctions. These stock milligram quantities are not direct main-medium\
    \ G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally\
    \ specifies DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q34\",\n\
    \    \"quantity\": \"Riboflavin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[33].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"\
    snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Preserve both source versions:\
    \ TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than\
    \ 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products\
    \ agree, but this does not authenticate endpoint 5788 or erase chemical-form and\
    \ version distinctions. These stock milligram quantities are not direct main-medium\
    \ G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally\
    \ specifies DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q35\",\n\
    \    \"quantity\": \"Nicotinic acid\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[34].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[34].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n     \
    \   \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Preserve both source versions: TOGO\
    \ has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1\
    \ mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree,\
    \ but this does not authenticate endpoint 5788 or erase chemical-form and version\
    \ distinctions. These stock milligram quantities are not direct main-medium G_PER_L.\
    \ Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies\
    \ DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"quantity\"\
    : \"Lipoic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[35].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[35].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\"\
    ,\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Preserve both source versions:\
    \ TOGO has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than\
    \ 1 mL. Both use 1000 mL stock water. Their named numeric amount-dose products\
    \ agree, but this does not authenticate endpoint 5788 or erase chemical-form and\
    \ version distinctions. These stock milligram quantities are not direct main-medium\
    \ G_PER_L. Both sources explicitly support D-calcium pantothenate; DSMZ additionally\
    \ specifies DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q37\",\n\
    \    \"quantity\": \"D-Ca-pantothenate\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[36].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[36].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Wolin tenfold vitamin stock table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\"\
    ,\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"D-Ca-pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Preserve both source versions: TOGO\
    \ has one-tenth of the DSMZ tenfold stock amount and doses 10 mL rather than 1\
    \ mL. Both use 1000 mL stock water. Their named numeric amount-dose products agree,\
    \ but this does not authenticate endpoint 5788 or erase chemical-form and version\
    \ distinctions. These stock milligram quantities are not direct main-medium G_PER_L.\
    \ Both sources explicitly support D-calcium pantothenate; DSMZ additionally specifies\
    \ DL-alpha-lipoic acid.\"\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"quantity\"\
    : \"Vitamin-stock nitrogen atmosphere\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[37].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[37].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM2549\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\"\
    ,\n        \"source_locator\": \"$.components[3].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"N2 gas\\\",\\n          \\\"conc_value\\\": 100,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      },\n      {\n        \"source_key\": \"dsmz846\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\",\n    \
    \    \"source_locator\": \"Main preparation: separately prepared later stocks\"\
    ,\n        \"exact_source_quote\": \"sulfide from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas and carbonate\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The TOGO vitamin-stock row\
    \ explicitly specifies 100% N2 and the primary separately gives this atmosphere\
    \ for later serine/vitamin/cysteine/sulfide stocks. Preserve stock atmosphere\
    \ rather than a duplicate unqualified main ingredient; no absolute gas quantity\
    \ is stated.\"\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"quantity\": \"\
    Na-resazurin solution (0.1% w/v)\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe: exact stock-addition row\",\n  \
    \      \"exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n    \
    \    \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na-resazurin solution (0.1% w/v)\\\",\\n     \
    \     \\\"volume\\\": 0.5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 0.1,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n     \
    \   \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Receiving-batch liquid dose\
    \ in mL; current G_PER_L is incompatible with the source unit. Preserve source\
    \ stock definition separately, with no density or measured-final-volume assumption.\"\
    \n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"quantity\": \"Trace element\
    \ solution SL-10\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe: exact stock-addition row\",\n  \
    \      \"exact_source_quote\": \"Trace element solution SL-10 1.00 ml\",\n   \
    \     \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[14]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution SL-10\\\",\\n         \
    \ \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Receiving-batch liquid dose in\
    \ mL; current G_PER_L is incompatible with the source unit. Preserve source stock\
    \ definition separately, with no density or measured-final-volume assumption.\"\
    \n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"quantity\": \"Selenite-tungstate\
    \ solution\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n \
    \       \"field_path\": \"solutions[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe: exact stock-addition row\",\n  \
    \      \"exact_source_quote\": \"Selenite-tungstate solution 1.00 ml\",\n    \
    \    \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[15]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Selenite-tungstate solution\\\",\\n          \\\
    \"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Receiving-batch liquid dose in\
    \ mL; current G_PER_L is incompatible with the source unit. Preserve source stock\
    \ definition separately, with no density or measured-final-volume assumption.\"\
    \n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"quantity\": \"Vitamin receiving\
    \ dose and source version\",\n    \"decision\": \"conflict\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main recipe vitamin addition\",\n        \"exact_source_quote\"\
    : \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[16]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamins solution\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"TOGO explicitly uses 10 mL of its\
    \ onefold stock; DSMZ uses 1 mL of the defined tenfold stock. Local 10 G_PER_L\
    \ is wrong as a unit, and linking 10 mL to endpoint 5788 silently changes source\
    \ strength/forms. Retain the source-version choice and stock-dose pair; do not\
    \ combine one source dose with another stock.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q43\",\n    \"quantity\": \"SL-10 water\",\n    \"decision\": \"add\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ null\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 water: exact stock table water row\",\n\
    \        \"exact_source_quote\": \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 990,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Separate stock solvent input missing\
    \ from the receiving solution structure. Existing 3990 water aggregates incompatible\
    \ stages and is not this exact scoped field. Do not infer measured final volume\
    \ from water input alone.\"\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"\
    quantity\": \"Selenite-tungstate water\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ null\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Selenite-tungstate water: exact stock table water\
    \ row\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n  \
    \      \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Separate stock solvent input missing\
    \ from the receiving solution structure. Existing 3990 water aggregates incompatible\
    \ stages and is not this exact scoped field. Do not infer measured final volume\
    \ from water input alone.\"\n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"\
    quantity\": \"Vitamin stock water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].composition\",\n        \"stored\":\
    \ null\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Vitamin stock water: exact stock table water\
    \ row\",\n        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n  \
    \      \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Separate stock solvent input missing\
    \ from the receiving solution structure. Existing 3990 water aggregates incompatible\
    \ stages and is not this exact scoped field. Do not infer measured final volume\
    \ from water input alone.\"\n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"\
    quantity\": \"SL-10 final make-up volume\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].preparation_steps\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].preparation_steps\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 preparation: final make-up sentence\",\n\
    \        \"exact_source_quote\": \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\"\
    : \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n    \
    \    \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Explicit stock make-up to\
    \ 1000 mL; distinct from the 990 mL initial water and receiving 1 mL dose.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q47\",\n    \"quantity\": \"Sodium resazurin\
    \ stock strength\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preferred_term\",\n        \"stored\"\
    : \"Na-resazurin solution (0.1% w/v)\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\",\n    \
    \    \"field_path\": \"solutions[0].preferred_term\",\n        \"stored\": \"\
    Na-resazurin solution (0.1% w/v)\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz846\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\",\n        \"\
    source_locator\": \"Main recipe stock-addition row\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na-resazurin solution (0.1% w/v)\\\",\\n     \
    \     \\\"volume\\\": 0.5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\
    \"conc_value\\\": 0.1,\\n          \\\"conc_unit\\\": \\\"(w/v)\\\"\",\n     \
    \   \"snapshot_sha256\": \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing stock name correctly\
    \ preserves 0.1% w/v but lacks attached evidence. This is stock strength; dose\
    \ 0.50 mL is separately assessed.\"\n  },\n  {\n    \"quantity_id\": \"q48\",\n\
    \    \"quantity\": \"SL-10 hydrochloric acid percentage\",\n    \"decision\":\
    \ \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\": \"ingredients[22].preferred_term\"\
    ,\n        \"stored\": \"HCl (25%; 7.7 M)\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[22].preferred_term\",\n        \"stored\":\
    \ \"HCl (25%; 7.7 M)\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"SL-10 acid row\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"togoM2549\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\",\n\
    \        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%; 7.7 M)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"The name preserves 25% reagent\
    \ strength; percentage basis is not specified by either source. It is not final-medium\
    \ concentration and does not independently support provider 2.5 g/L HCl.\"\n \
    \ },\n  {\n    \"quantity_id\": \"q49\",\n    \"quantity\": \"TOGO hydrochloric\
    \ acid molarity\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].preferred_term\",\n        \"stored\"\
    : \"HCl (25%; 7.7 M)\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].preferred_term\",\n        \"stored\"\
    : \"HCl (25%; 7.7 M)\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM2549\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2549\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"HCl (25%; 7.7 M)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"1fb01050c7eee844e76e16407682656feb4655e0920711c49493fcbafbc742ec\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"TOGO explicitly names 7.7 M in\
    \ the reagent description. Preserve that source-specific assertion and its stock\
    \ stage; DSMZ846 prints 25% only and no molarity is inferred from percentage.\"\
    \n  },\n  {\n    \"quantity_id\": \"q50\",\n    \"quantity\": \"Main sparging\
    \ duration\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"preparation_steps\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation sparging sentence\",\n     \
    \   \"exact_source_quote\": \"sparge medium with 80% N2 and 20% CO2 gas mixture\
    \ for 30 - 45 min to make it anoxic.\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only scoped condition\
    \ or variant. Preserve range, conditional language, denominator and strain label\
    \ exactly. The two strain variants do not alter the base recipe for all uses and\
    \ are not independent experimental growth assertions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q51\",\n    \"quantity\": \"Main vessel filling fraction\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation distribution sentence\",\n \
    \       \"exact_source_quote\": \"serum vials to 30% of their volume and autoclave.\"\
    ,\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only scoped condition\
    \ or variant. Preserve range, conditional language, denominator and strain label\
    \ exactly. The two strain variants do not alter the base recipe for all uses and\
    \ are not independent experimental growth assertions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q52\",\n    \"quantity\": \"Carbonate-stock gas atmosphere\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation carbonate-stock sentence\",\n\
    \        \"exact_source_quote\": \"from a sterile anoxic stock solution prepared\
    \ under 80% N2 and 20% CO2 gas atmosphere.\",\n        \"snapshot_sha256\": \"\
    83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\",\n        \"\
    parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only scoped condition\
    \ or variant. Preserve range, conditional language, denominator and strain label\
    \ exactly. The two strain variants do not alter the base recipe for all uses and\
    \ are not independent experimental growth assertions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q53\",\n    \"quantity\": \"Base complete-medium pH\",\n    \"decision\":\
    \ \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz846\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation complete-medium pH sentence\"\
    ,\n        \"exact_source_quote\": \"medium to 7.2, if necessary.\",\n       \
    \ \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only scoped condition\
    \ or variant. Preserve range, conditional language, denominator and strain label\
    \ exactly. The two strain variants do not alter the base recipe for all uses and\
    \ are not independent experimental growth assertions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q54\",\n    \"quantity\": \"DSM12260 replacement substrate\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"DSM12260-specific variant sentence\",\n     \
    \   \"exact_source_quote\": \"For DSM 12260: Replace L-Serine with 1.74 g/l L-Arginine\
    \ x HCl.\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only scoped condition\
    \ or variant. Preserve range, conditional language, denominator and strain label\
    \ exactly. The two strain variants do not alter the base recipe for all uses and\
    \ are not independent experimental growth assertions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q55\",\n    \"quantity\": \"DSM27871 variant pH\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"DSM27871-specific variant sentence\",\n     \
    \   \"exact_source_quote\": \"For DSM 27871: Adjust the pH of the complete medium\
    \ to 7.8.\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only scoped condition\
    \ or variant. Preserve range, conditional language, denominator and strain label\
    \ exactly. The two strain variants do not alter the base recipe for all uses and\
    \ are not independent experimental growth assertions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q56\",\n    \"quantity\": \"Unspecified autoclave cycle\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n        \"field_path\": \"sterilization_method\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization_method\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation autoclave instruction\",\n \
    \       \"exact_source_quote\": \"serum vials to 30% of their volume and autoclave.\"\
    ,\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The source states autoclaving\
    \ but supplies no numerical temperature/time. Vitamin filtration is separate.\
    \ No cycle from parent media is transferred.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q57\",\n    \"quantity\": \"Unspecified later-stock strengths and doses\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"preparation_steps\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz846\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\"\
    ,\n        \"source_locator\": \"Main preparation later-additions sentence\",\n\
    \        \"exact_source_quote\": \"serum vials to 30% of their volume and autoclave.\
    \ Add serine, vitamins, cysteine, and\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz846\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium846.pdf\",\n    \
    \    \"source_locator\": \"Main preparation later stock atmosphere\",\n      \
    \  \"exact_source_quote\": \"sulfide from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas and carbonate\",\n        \"snapshot_sha256\": \"83063d153921bd6f44b9feb180f4821dece4684b1dcfc14b8b3e55367b1df30b\"\
    ,\n        \"parsed_text_sha256\": \"ddfb058d496cf1e62b6a3951dff47591300b20d86459f226a59fa99eecdc203b\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The main table provides amounts\
    \ of serine, cysteine, sulfide and carbonate, but their separately prepared stock\
    \ concentrations and liquid injection volumes are not specified. The vitamin stock\
    \ and dose are separately quantified; no missing stock strength or volume is invented.\"\
    \n  },\n  {\n    \"quantity_id\": \"q58\",\n    \"quantity\": \"Provider declared\
    \ main volume\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINOMONAS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadive846api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/846\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1003\",\n        \"snapshot_sha256\": \"cac25c80f54f1fc9388bc9ebb10776d1d498fe035d8b24df8bf4f13662c7f532\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"This provider metadata is\
    \ not a measured final-medium volume. It must not override explicit source batch\
    \ inputs, stock make-up or source-specific vitamin dosage.\"\n  },\n  {\n    \"\
    quantity_id\": \"q59\",\n    \"quantity\": \"solution4178: HCl\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"HCl\\\",\\n                \\\"compound_id\\\": 68,\\n               \
    \ \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n    \
    \            \\\"condition\\\": null,\\n                \\\"attribute\\\": \\\"\
    25%, 7.7 M\\\",\\n                \\\"amount\\\": 10,\\n                \\\"unit\\\
    \": \\\"ml\\\",\\n                \\\"g_l\\\": 2.5,\\n                \\\"mmol_l\\\
    \": 68.5683,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q60\",\n    \"quantity\": \"solution4178:\
    \ FeCl2 x 4 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"FeCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 260,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1.5,\\n                \\\"unit\\\"\
    : \\\"g\\\",\\n                \\\"g_l\\\": 1.5,\\n                \\\"mmol_l\\\
    \": 7.54482,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q61\",\n    \"quantity\"\
    : \"solution4178: ZnCl2\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"ZnCl2\\\",\\n                \\\"compound_id\\\": 64,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 70,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.07,\\n                \\\"mmol_l\\\": 0.513573,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only. Existing\
    \ matching evidence supports the provider-declared within-stock basis, or water\
    \ batch dose, at this exact composition field. It does not establish receiving-medium\
    \ concentration or source-stock interchangeability. Unattached otherwise matching\
    \ provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require\
    \ source-unit correction; vitamin endpoint 5788 remains compositionally distinct\
    \ from both source vitamin recipes.\",\n    \"existing_evidence_indices\": [\n\
    \      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q62\",\n    \"quantity\": \"\
    solution4178: MnCl2 x 4 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"MnCl2 x 4 H2O\\\",\\n                \\\"compound_id\\\": 36,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 100,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\"mmol_l\\\
    \": 0.505293,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q63\",\n    \"quantity\"\
    : \"solution4178: H3BO3\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"H3BO3\\\",\\n                \\\"compound_id\\\": 37,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 6,\\n                \\\"unit\\\": \\\"mg\\\"\
    ,\\n                \\\"g_l\\\": 0.006,\\n                \\\"mmol_l\\\": 0.0970246,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only. Existing\
    \ matching evidence supports the provider-declared within-stock basis, or water\
    \ batch dose, at this exact composition field. It does not establish receiving-medium\
    \ concentration or source-stock interchangeability. Unattached otherwise matching\
    \ provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require\
    \ source-unit correction; vitamin endpoint 5788 remains compositionally distinct\
    \ from both source vitamin recipes.\",\n    \"existing_evidence_indices\": [\n\
    \      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q64\",\n    \"quantity\": \"\
    solution4178: CoCl2 x 6 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"CoCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 38,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 190,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.19,\\n                \\\"mmol_l\\\
    \": 1.46335,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q65\",\n    \"quantity\"\
    : \"solution4178: CuCl2 x 2 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"CuCl2 x 2 H2O\\\",\\n                \\\"compound_id\\\": 39,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 2,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.002,\\n                \\\"mmol_l\\\
    \": 0.0117314,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q66\",\n    \"quantity\"\
    : \"solution4178: NiCl2 x 6 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"NiCl2 x 6 H2O\\\",\\n                \\\"compound_id\\\": 40,\\n     \
    \           \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 24,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.024,\\n                \\\"mmol_l\\\
    \": 0.185187,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q67\",\n    \"quantity\"\
    : \"solution4178: Na2MoO4 x 2 H2O\",\n    \"decision\": \"verified\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 9,\\n                \\\"compound\\\
    \": \\\"Na2MoO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 9,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 36,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.036,\\n                \\\"mmol_l\\\
    \": 0.148791,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q68\",\n    \"quantity\"\
    : \"solution4178: Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml\"\
    ,\n        \"field_path\": \"composition[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"990\",\n          \"unit\": \"PERCENT_V_V\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution4178\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/4178\"\
    ,\n        \"source_locator\": \"$.data.recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 10,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 990,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q69\",\n    \"quantity\": \"solution5543:\
    \ NaOH\",\n    \"decision\": \"verified\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5543\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"NaOH\\\",\\n                \\\"compound_id\\\": 256,\\n             \
    \   \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n  \
    \              \\\"condition\\\": null,\\n                \\\"attribute\\\": null,\\\
    n                \\\"amount\\\": 0.5,\\n                \\\"unit\\\": \\\"g\\\"\
    ,\\n                \\\"g_l\\\": 0.5,\\n                \\\"mmol_l\\\": 12.5009,\\\
    n                \\\"optional\\\": 0\\n            }\",\n        \"snapshot_sha256\"\
    : \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only. Existing\
    \ matching evidence supports the provider-declared within-stock basis, or water\
    \ batch dose, at this exact composition field. It does not establish receiving-medium\
    \ concentration or source-stock interchangeability. Unattached otherwise matching\
    \ provider values are evidence_only. SL-10 HCl g/L and water PERCENT_V_V require\
    \ source-unit correction; vitamin endpoint 5788 remains compositionally distinct\
    \ from both source vitamin recipes.\",\n    \"existing_evidence_indices\": [\n\
    \      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q70\",\n    \"quantity\": \"\
    solution5543: Na2SeO3 x 5 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5543\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Na2SeO3 x 5 H2O\\\",\\n                \\\"compound_id\\\": 107,\\n  \
    \              \\\"solution\\\": null,\\n                \\\"solution_id\\\":\
    \ null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 3,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.003,\\n                \\\"mmol_l\\\
    \": 0.0114062,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q71\",\n    \"quantity\"\
    : \"solution5543: Na2WO4 x 2 H2O\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5543\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"Na2WO4 x 2 H2O\\\",\\n                \\\"compound_id\\\": 249,\\n   \
    \             \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 4,\\n                \\\"unit\\\": \\\
    \"mg\\\",\\n                \\\"g_l\\\": 0.004,\\n                \\\"mmol_l\\\
    \": 0.0121267,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q72\",\n    \"quantity\"\
    : \"solution5543: Distilled water\",\n    \"decision\": \"verified\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n     \
    \ }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"solution5543\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5543\",\n\
    \        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"Distilled water\\\",\\n                \\\"compound_id\\\": 4,\\n    \
    \            \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 1000,\\n                \\\"unit\\\"\
    : \\\"ml\\\",\\n                \\\"g_l\\\": null,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q73\",\n    \"quantity\"\
    : \"solution5788: Biotin\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[0]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 1,\\n                \\\"compound\\\
    \": \\\"Biotin\\\",\\n                \\\"compound_id\\\": 46,\\n            \
    \    \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\n \
    \               \\\"condition\\\": null,\\n                \\\"attribute\\\":\
    \ null,\\n                \\\"amount\\\": 20,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\
    \": 0.0818632,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q74\",\n    \"quantity\"\
    : \"solution5788: Folic acid\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[1]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 2,\\n                \\\"compound\\\
    \": \\\"Folic acid\\\",\\n                \\\"compound_id\\\": 138,\\n       \
    \         \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 20,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.02,\\n                \\\"mmol_l\\\
    \": 0.0453104,\\n                \\\"optional\\\": 0\\n            }\",\n    \
    \    \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q75\",\n    \"quantity\"\
    : \"solution5788: Pyridoxine hydrochloride\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[2]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 3,\\n                \\\"compound\\\
    \": \\\"Pyridoxine hydrochloride\\\",\\n                \\\"compound_id\\\": 519,\\\
    n                \\\"solution\\\": null,\\n                \\\"solution_id\\\"\
    : null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": \\\"B6\\\",\\n                \\\"amount\\\": 100,\\n                \\\"\
    unit\\\": \\\"mg\\\",\\n                \\\"g_l\\\": 0.1,\\n                \\\
    \"mmol_l\\\": 0.486287,\\n                \\\"optional\\\": 0\\n            }\"\
    ,\n        \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q76\",\n    \"quantity\": \"solution5788:\
    \ Riboflavine\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[3]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 4,\\n                \\\"compound\\\
    \": \\\"Riboflavine\\\",\\n                \\\"compound_id\\\": 616,\\n      \
    \          \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : \\\"B2\\\",\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\
    \": \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.132837,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q77\",\n    \"quantity\": \"solution5788:\
    \ Thiamine\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[4]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 5,\\n                \\\"compound\\\
    \": \\\"Thiamine\\\",\\n                \\\"compound_id\\\": 666,\\n         \
    \       \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : \\\"B1\\\",\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\
    \": \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.188423,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q78\",\n    \"quantity\": \"solution5788:\
    \ Nicotinic acid\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[5]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 6,\\n                \\\"compound\\\
    \": \\\"Nicotinic acid\\\",\\n                \\\"compound_id\\\": 139,\\n   \
    \             \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : \\\"PP\\\",\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\
    \": \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.406141,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q79\",\n    \"quantity\": \"solution5788:\
    \ Pantothenic acid\",\n    \"decision\": \"verified\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[6]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 7,\\n                \\\"compound\\\
    \": \\\"Pantothenic acid\\\",\\n                \\\"compound_id\\\": 135,\\n \
    \               \\\"solution\\\": null,\\n                \\\"solution_id\\\"\
    : null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.228071,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q80\",\n    \"quantity\"\
    : \"solution5788: Cobalamin\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[7]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 8,\\n                \\\"compound\\\
    \": \\\"Cobalamin\\\",\\n                \\\"compound_id\\\": 2157,\\n       \
    \         \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : \\\"B12\\\",\\n                \\\"amount\\\": 1,\\n                \\\"unit\\\
    \": \\\"mg\\\",\\n                \\\"g_l\\\": 0.001,\\n                \\\"mmol_l\\\
    \": null,\\n                \\\"optional\\\": 0\\n            }\",\n        \"\
    snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : []\n  },\n  {\n    \"quantity_id\": \"q81\",\n    \"quantity\": \"solution5788:\
    \ p-Aminobenzoic acid\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[8]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 9,\\n                \\\"compound\\\
    \": \\\"p-Aminobenzoic acid\\\",\\n                \\\"compound_id\\\": 47,\\\
    n                \\\"solution\\\": null,\\n                \\\"solution_id\\\"\
    : null,\\n                \\\"condition\\\": null,\\n                \\\"attribute\\\
    \": null,\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\"\
    : \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.364591,\\n                \\\"optional\\\": 0\\n            }\",\n     \
    \   \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  },\n  {\n    \"quantity_id\": \"q82\",\n    \"quantity\"\
    : \"solution5788: Lipoic acid\",\n    \"decision\": \"verified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/mediadive_5788_Vitamins_solution.yaml\"\
    ,\n        \"field_path\": \"composition[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"solution5788\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/solution/5788\"\
    ,\n        \"source_locator\": \"$.data.recipe[9]\",\n        \"exact_source_quote\"\
    : \"{\\n                \\\"recipe_order\\\": 10,\\n                \\\"compound\\\
    \": \\\"Lipoic acid\\\",\\n                \\\"compound_id\\\": 368,\\n      \
    \          \\\"solution\\\": null,\\n                \\\"solution_id\\\": null,\\\
    n                \\\"condition\\\": null,\\n                \\\"attribute\\\"\
    : null,\\n                \\\"amount\\\": 50,\\n                \\\"unit\\\":\
    \ \\\"mg\\\",\\n                \\\"g_l\\\": 0.05,\\n                \\\"mmol_l\\\
    \": 0.24233,\\n                \\\"optional\\\": 0\\n            }\",\n      \
    \  \"snapshot_sha256\": \"3aa677cc23fc3ac5231f9e7553b23d6e115fc7ef8a8fc0fda4440ac738fa823d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Context dependency only.\
    \ Existing matching evidence supports the provider-declared within-stock basis,\
    \ or water batch dose, at this exact composition field. It does not establish\
    \ receiving-medium concentration or source-stock interchangeability. Unattached\
    \ otherwise matching provider values are evidence_only. SL-10 HCl g/L and water\
    \ PERCENT_V_V require source-unit correction; vitamin endpoint 5788 remains compositionally\
    \ distinct from both source vitamin recipes.\",\n    \"existing_evidence_indices\"\
    : [\n      0\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '35 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 35/38
    primary and 32/38 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi131527
  - chebi15377
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi16526
  - chebi17015
  - chebi17115
  - chebi176843
  - chebi17997
  - chebi26710
  - chebi27470
  - chebi29377
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32145
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 38: primary 92.11%;
    secondary 84.21%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 27 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact accession and single maintained contributor
  outcome: supported
  summary: TOGO M2549 names DSMZ846 and the same Aminomonas medium. The generated
    target and exact maintained contributor share the stable CultureMech ID. Exact
    dependency files and endpoint IDs resolve; their composition and transfer scope
    are separately assessed. No historical variant identity or experimental organism-growth
    assertion is inferred from a name.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - api
  - solution4178
  - solution5543
  - solution5788
- assessment_id: source-forms
  area: grounding
  topic: Source-specific salt, hydrate and stereochemical forms
  outcome: concern
  summary: Most named hydrates, L-serine and L-cysteine hydrochloride hydrate agree
    with their asserted forms. Nickel hexahydrate is mapped to anhydrous CHEBI:34887
    in both medium layers and local SL-10 context. Both TOGO and DSMZ explicitly support
    D-calcium pantothenate; its source-specific D naming is not an unresolved stereochemical
    issue. Generic lipoic acid grounding does not preserve DSMZ explicit DL-alpha
    mixture wording, which should remain in source notes rather than an invented single-enantiomer
    ID. Source vitamin B12 remains generic. Endpoint5788 pantothenic acid and thiamine
    forms differ from the source calcium salt and hydrochloride.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - chebi34887
  - chebi31345
  - chebi16494
  - solution5788
  - context-chebi18385
  - context-chebi7916
  - context-chebi28911
- assessment_id: stocks
  area: representation
  topic: Named stock references, existing evidence and vitamin version
  outcome: concern
  summary: Local SL-10 and selenite-tungstate files contain real compositions despite
    placeholder ingredients and historical incomplete flags. Their 17 audited evidence
    objects support only exact existing stock fields. Endpoint5788 has tenfold-scale
    numbers but pantothenic acid and thiamine forms and no water recipe row; it is
    not established as TOGO onefold stock or DSMZ Wolin10x5980. Numeric stock-dose
    scaling alone cannot establish chemical identity.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - primary
  - togo
  - api
  - solution4178
  - solution5543
  - solution5788
  - solution595
  - solution777
  - solution5980
  - dependency-claims
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Ordered preparation and conditional variant coverage
  outcome: concern
  summary: Both medium layers omit preparation, pH and amount evidence. Main gas mixture,
    sparging duration, vessel fraction, late additions under separate gas atmospheres,
    vitamin filtration and complete-medium pH are explicitly available. DSM12260 substrate
    replacement and DSM27871 pH are separate source variants, not universal base changes.
    Only named stock sections of DSM320/385/120 transfer.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - quantity-inventory
  - dsmz320
  - dsmz385
  - dsmz120
- assessment_id: classification
  area: scope
  topic: Physical class, application and composition-derived metadata
  outcome: concern
  summary: Bacterial, liquid, complex/undefined classification is consistent with
    the yeast-containing base recipe. Generic cultivation application is not an experimental
    strain-growth claim. No taxonomy, DOI, PMID or KG match is asserted. high_metal
    requires reassessment only after stock and final-medium quantities are reconstructed
    under its schema contract; the current true flag is not independently supported
    by these flattened values.
  target_ids:
  - CultureMech:009118
  evidence_ids:
  - record
  - owner-0
  - primary
  - high-metal-contract
findings:
- finding_id: f1
  issue_key: cm009118-stock-flattening
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock amounts, liquid units and water stages are flattened
  description: Both medium layers flatten SL-10, selenite-tungstate and vitamin stock
    inputs into main ingredients. Milligram stock amounts are stored as G_PER_L, liquid
    additions are G_PER_L, and 3990 G_PER_L water combines four distinct stages. Even
    otherwise matching main gram values need their source batch basis rather than
    an assumed measured final liter.
  target_ids:
  - CultureMech:009118
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  issue_key: cm009118-vitamin-endpoint
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The vitamin endpoint does not establish the source stock
  description: Local endpoint5788 is attached to a TOGO dose of 10 with a mass unit.
    TOGO defines onefold vitamin amounts at 10 mL; DSMZ defines Wolin tenfold5980
    at 1 mL. Endpoint5788 uses distinct pantothenic acid and thiamine forms. Its existing
    amount evidence validates its own recipe, not this medium link.
  target_ids:
  - CultureMech:009118
  field_paths:
  - solutions[3]
  - ingredients[27:38]
  evidence_ids:
  - record
  - primary
  - togo
  - api
  - solution5788
  - solution5980
  - dependency-claims
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  issue_key: cm009118-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is grounded to anhydrous nickel dichloride
  description: The exact primary and TOGO SL-10 rows specify NiCl2 x 6 H2O. Both medium
    layers assert CHEBI:34887 and the same secondary key, whose captured ontology
    formula is Cl2Ni. The local SL-10 dependency has the same supplied-form mismatch.
    Canonical label validity does not cure this structural mismatch.
  target_ids:
  - CultureMech:009118
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - chebi34887
  - solution4178
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  issue_key: cm009118-preparation-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation, pH and conditional source variants are absent
  description: Both local layers omit available ordered preparation, scoped gas conditions,
    pH and variant distinctions. Unknown solution names obscure supported definitions.
    Source-only DSM12260 and DSM27871 instructions must remain distinct from the base
    recipe; a generic cultivation application is not growth evidence.
  target_ids:
  - CultureMech:009118
  field_paths:
  - preparation_steps
  - ph_value
  - solutions
  - references
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  issue_key: cm009118-derived-metal-flag
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Composition-derived high-metal flag lacks a reliable quantity basis
  description: The high_metal flag is asserted in both medium layers while stock inputs
    and units are materially malformed. Its schema-defined quantitative criterion
    cannot be authenticated from this representation. This review does not infer a
    corrected total or boolean.
  target_ids:
  - CultureMech:009118
  field_paths:
  - high_metal
  evidence_ids:
  - record
  - owner-0
  - high-metal-contract
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  description: Reconcile the maintained owner with explicit source units and stock
    stages, then regenerate the merged record. Preserve source-version stock-dose
    pairs, actual make-up instructions and all unresolved final-volume bases without
    inventing densities.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  - Every target and owner concentration is reconciled to its source-stage inventory
    decision.
- action_id: a2
  description: Resolve the intended source version and exact vitamin stock identity
    before attaching a stock ID. Preserve D-calcium pantothenate, thiamine hydrochloride
    and source mixture wording; keep original source-dose relationships and attach
    claim-level evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  - No cross-source stock strength or form is inferred solely from matching names
    or numeric scaling.
- action_id: a3
  description: Ground the source hexahydrate to a verified exact form or retain an
    explicit unresolved form without the contradictory identity. Reconcile the corresponding
    secondary mapping and scoped stock context; do not invent a replacement ID.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  - A valid source-to-hydrate correspondence supports the eventual primary and secondary
    terms.
- action_id: a4
  description: Represent the available preparation stages and variant-specific instructions
    with exact source evidence in the maintained owner. Attach amount evidence at
    the correct layer; retain unspecified cycle/doses and avoid importing unrelated
    parent media.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  - Base conditions and both source variants remain distinguishable and every preparation
    quantity retains its exact denominator.
- action_id: a5
  description: Reassess the derived classification after source-grounded stock and
    receiving-medium quantities are represented; retain the numerical criterion and
    calculation provenance.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009118
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2549_Aminomonas_Medium.yaml
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
  - Derived classification is tied to corrected source-scoped quantities rather than
    flattened stock values.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Available primary and provider evidence resolves the scientific source scope sufficiently
  for completed review. Source-version differences remain explicit; completion does
  not mean the local formulation is correct.
- Neither source supplies a measured final-medium volume, a numerical main autoclave
  cycle, or every separately prepared stock strength/injection volume. HCl 25% has
  no explicit percentage basis. No such values are inferred.
- Both exact TOGO and DSMZ sources support D-calcium pantothenate. A contradictory
  provisional summary was superseded by the independent raw-source audit; frozen captures
  remain unchanged.
- 'Dependency files are context only: their attached evidence and historical timestamps
  are not inherited by the target. Existing placeholder ingredients and incomplete
  flags do not imply that their populated composition arrays are absent. No parent-medium
  conditions or unrelated legacy ingredient claims transfer.'
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-025
- generated-medium
```
