# Source and formulation review: anaerolinea_medium (CultureMech:003504)

- Review: 20261021T154841Z-culturemech-003504-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:43:30Z
- Finished UTC: 2026-10-21T15:48:41Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The complete DSMZ1004 source supports the base formula and explicit strain branches, but all five owners flatten three stocks and the three KOMODO strain wrappers still retain the unchanged base quantities. Later topology repairs are absent from the generated merge and do not cure formulation differences. Declared1003 mL and listed 1003.5 mL are preserved separately; sodium-resazurin and nickel-hydrate mappings and preparation scope require curation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 275; batch 028 item 5 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-seven task batches contain 270 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 273 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003504 | data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml | generated | anaerolinea_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003504 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:003504 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/275/strict.tsv |
| validate-terms | passed | True | CultureMech:003504 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:003504 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:003504 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive1004api | unavailable | False | CultureMech:003504 | Exact mediadive1004api access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: mediadive1004apiRetry | unavailable | False | CultureMech:003504 | Exact mediadive1004apiRetry access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004detail | unavailable | False | CultureMech:003504 | Exact komodo1004detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004actual | unavailable | False | CultureMech:003504 | Exact komodo1004actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004_1detail | unavailable | False | CultureMech:003504 | Exact komodo1004_1detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004_1actual | unavailable | False | CultureMech:003504 | Exact komodo1004_1actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004_2detail | unavailable | False | CultureMech:003504 | Exact komodo1004_2detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004_2actual | unavailable | False | CultureMech:003504 | Exact komodo1004_2actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004_3detail | unavailable | False | CultureMech:003504 | Exact komodo1004_3detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: komodo1004_3actual | unavailable | False | CultureMech:003504 | Exact komodo1004_3actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| Exact source content access: solution1474 | unavailable | False | CultureMech:003504 | Exact solution1474 access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:003504.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:003504.

56 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Base KH2PO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.139581",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.139581",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.139581",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.139581",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.139581",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.139581",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.14,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.1395812562313060817547357926"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "KH2PO4 0.14 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Base MgCl2 x 6 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.199402",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.2,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.1994017946161515453639082752"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "MgCl2 x 6 H2O 0.20 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Base CaCl2 x 2 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.149551",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.149551",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.149551",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.149551",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.149551",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.149551",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.15,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.1495513459621136590229312064"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "CaCl2 x 2 H2O 0.15 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Base NH4Cl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.538385",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.538385",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.538385",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.538385",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.538385",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.538385",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.54,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.5383848454636091724825523430"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "NH4Cl 0.54 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Base Sodium resazurin",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.0005,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.0004985044865403788634097706879"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. The source 0.5 mL of 0.1% w/v stock yields 0.0005 g before normalization; preserve sodium-salt identity.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Base NaHCO3",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "2.49252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 2.5,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "2.492522432701894317048853440"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "NaHCO3 2.50 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Base Yeast extract",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.29312",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.29312",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.29312",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.29312",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 2.3,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "2.293120638085742771684945165"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "Yeast extract 2.30 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Base D-Glucose",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.19342",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.19342",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.19342",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 2.2,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "2.193419740777666999002991027"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "D-Glucose 2.20 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Base L-Cysteine HCl x H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.25,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.2492522432701894317048853440"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.25 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Base Na2S x 9 H2O",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "base receiving batch",
      "source_mass_g": 0.25,
      "source_declared_final_ml": 1003,
      "derived_g_per_l": "0.2492522432701894317048853440"
    },
    "rationale": "The existing base rate agrees to stored rounding with the literal mass divided by the source-declared 1.003 L. No attached local evidence exists, so the decision is evidence_only. Do not replace the declared basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific override.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 base main table",
        "exact_source_quote": "Na2S x 9 H2O 0.25 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "SL-11: Na2-EDTA x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "5.2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 5.2,
      "source_unit": "g",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "Na2-EDTA x 2 H2O 5.20 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "SL-11: FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 1.5,
      "source_unit": "g",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "SL-11: ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 70,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "SL-11: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 100,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "SL-11: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 6,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "SL-11: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 190,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "SL-11: CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 2,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "SL-11: NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 24,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "SL-11: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "source_amount": 36,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": 1000,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, SL-11 subsection",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Selenite-tungstate: NaOH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Selenite-tungstate",
      "source_amount": 0.5,
      "source_unit": "g",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Selenite-tungstate subsection",
        "exact_source_quote": "NaOH 0.50 g",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Selenite-tungstate: Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.003",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Selenite-tungstate",
      "source_amount": 3,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Selenite-tungstate subsection",
        "exact_source_quote": "Na2SeO3 x 5 H2O 3.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Selenite-tungstate: Na2WO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.004",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Selenite-tungstate",
      "source_amount": 4,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Selenite-tungstate subsection",
        "exact_source_quote": "Na2WO4 x 2 H2O 4.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Wolin10x vitamins: Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 20,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Biotin 20.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Wolin10x vitamins: Folic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 20,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Folic acid 20.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Wolin10x vitamins: Pyridoxine hydrochloride",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 100,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Pyridoxine hydrochloride 100.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Wolin10x vitamins: Thiamine HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 50,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Thiamine HCl 50.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Wolin10x vitamins: Riboflavin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 50,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Riboflavin 50.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Wolin10x vitamins: Nicotinic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 50,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Nicotinic acid 50.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Wolin10x vitamins: Calcium D-(+)-pantothenate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 50,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Calcium D-(+)-pantothenate 50.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Wolin10x vitamins: Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 1,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "Vitamin B12 1.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Wolin10x vitamins: p-Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[30].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 50,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "p-Aminobenzoic acid 50.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Wolin10x vitamins: (DL)-alpha-Lipoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[31].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "source_amount": 50,
      "source_unit": "mg",
      "water_ml": 1000,
      "stock_final_makeup_ml": null,
      "main_receiving_dose_ml": 1
    },
    "rationale": "The existing scalar is a stock-level numerical amount/rate, not a main ingredient concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final make-up; the other stock tables state water input, not a measured finished volume. No arbitrary whole-stock transfer is allowed.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, Wolin10x vitamins subsection",
        "exact_source_quote": "(DL)-alpha-Lipoic acid 50.00 mg",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "base main",
      "water_ml": 1000
    },
    "rationale": "Restore the separate solvent input in its named scope; do not sum stock preparation water into the receiving medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Exact Main water table row; repeated text distinguished by subsection",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "SL-11 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "water_ml": 1000,
      "final_makeup_ml": 1000
    },
    "rationale": "Restore the separate solvent input in its named scope; do not sum stock preparation water into the receiving medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Exact SL-11 water table row; repeated text distinguished by subsection",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Selenite-tungstate water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "selenite-tungstate",
      "water_ml": 1000
    },
    "rationale": "Restore the separate solvent input in its named scope; do not sum stock preparation water into the receiving medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Exact Selenite-tungstate water table row; repeated text distinguished by subsection",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Wolin10x water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "Wolin10x vitamins",
      "water_ml": 1000
    },
    "rationale": "Restore the separate solvent input in its named scope; do not sum stock preparation water into the receiving medium.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Exact Wolin10x water table row; repeated text distinguished by subsection",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Base stock dose SL-11",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "SL-11",
      "dose_ml": 1
    },
    "rationale": "Restore the explicit receiving stock addition, distinct from the stock recipe and the declared 1003 mL final-volume header.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Trace element solution SL-11 1.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Base stock dose selenite-tungstate",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "selenite-tungstate",
      "dose_ml": 1
    },
    "rationale": "Restore the explicit receiving stock addition, distinct from the stock recipe and the declared 1003 mL final-volume header.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Selenite-tungstate solution 1.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Base stock dose sodium resazurin",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "sodium resazurin",
      "dose_ml": 0.5,
      "strength": "0.1% w/v"
    },
    "rationale": "Restore the explicit receiving stock addition, distinct from the stock recipe and the declared 1003 mL final-volume header.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Base stock dose Wolin10x vitamins",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stock": "Wolin10x vitamins",
      "dose_ml": 1
    },
    "rationale": "Restore the explicit receiving stock addition, distinct from the stock recipe and the declared 1003 mL final-volume header.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Wolin's vitamin solution (10x) 1.00 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "Variant komodo.medium:1004.1 Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.29312",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "variant": "komodo.medium:1004.1",
      "yeast_extract_g_per_l": 0.1
    },
    "rationale": "The current primary explicitly resolves this branch. Preserve its g/L instruction as printed; do not divide it again by 1.003 or alter the base recipe. Later topology-only repair and ingredients_curated flag do not establish that the unchanged child amounts were scientifically corrected.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 exact named strain clause",
        "exact_source_quote": "reduce amount of yeast extract to 0.10 g/l.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "Variant komodo.medium:1004.1 D-Glucose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.19342",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "variant": "komodo.medium:1004.1",
      "glucose": "replace",
      "sucrose_g_per_l": 7.2
    },
    "rationale": "The current primary explicitly resolves this branch. Preserve its g/L instruction as printed; do not divide it again by 1.003 or alter the base recipe. Later topology-only repair and ingredients_curated flag do not establish that the unchanged child amounts were scientifically corrected.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 exact named strain clause",
        "exact_source_quote": "For DSM 16554, DSM 16555, DSM 17877: Replace glucose with 7.20 g/l sucrose and",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "Variant komodo.medium:1004.2 Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2.29312",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "variant": "komodo.medium:1004.2",
      "yeast_extract_g_per_l": 0.1
    },
    "rationale": "The current primary explicitly resolves this branch. Preserve its g/L instruction as printed; do not divide it again by 1.003 or alter the base recipe. Later topology-only repair and ingredients_curated flag do not establish that the unchanged child amounts were scientifically corrected.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 exact named strain clause",
        "exact_source_quote": "For DSM 16556: Omit glucose and reduce amount of yeast extract to 0.10 g/l.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Variant komodo.medium:1004.2 D-Glucose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.19342",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "variant": "komodo.medium:1004.2",
      "glucose": "omit, not a numeric zero concentration"
    },
    "rationale": "The current primary explicitly resolves this branch. Preserve its g/L instruction as printed; do not divide it again by 1.003 or alter the base recipe. Later topology-only repair and ingredients_curated flag do not establish that the unchanged child amounts were scientifically corrected.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 exact named strain clause",
        "exact_source_quote": "For DSM 16556: Omit glucose and reduce amount of yeast extract to 0.10 g/l.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q45",
    "component_or_context": "Variant komodo.medium:1004.3 D-Glucose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "2.19342",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "variant": "komodo.medium:1004.3",
      "glucose_g_per_l": 5
    },
    "rationale": "The current primary explicitly resolves this branch. Preserve its g/L instruction as printed; do not divide it again by 1.003 or alter the base recipe. Later topology-only repair and ingredients_curated flag do not establish that the unchanged child amounts were scientifically corrected.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 exact named strain clause",
        "exact_source_quote": "For DSM 22659: Increase amount of glucose to 5.00 g/l.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q46",
    "component_or_context": "Source-only DSM23815",
    "decision": "add",
    "local_fields": [],
    "proposed_source_representation": {
      "branch": "DSM23815",
      "cellobiose_g_per_l": 2,
      "glucose": "replace",
      "preparation": "sterile anoxic, filter-sterilized stock after autoclaving"
    },
    "rationale": "Source-only variant context: not one of the three current local child wrappers and not a universal base adjustment. Retain separately when documenting source scope; no growth result is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 additional source branch",
        "exact_source_quote": "For DSM 23815: Replace glucose with 2.00 g/l cellobiose added after autoclaving from a",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 continuation of DSM23815 clause",
        "exact_source_quote": "sterile anoxic stock solution sterilized by filtration.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q47",
    "component_or_context": "Source-only DSM103421",
    "decision": "add",
    "local_fields": [],
    "proposed_source_representation": {
      "branch": "DSM103421",
      "yeast_extract_g_per_l": 0.1
    },
    "rationale": "Source-only variant context: not one of the three current local child wrappers and not a universal base adjustment. Retain separately when documenting source scope; no growth result is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 additional source branch",
        "exact_source_quote": "For DSM 103421: Reduce amount of yeast extract to 0.1 g/l",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q48",
    "component_or_context": "Main sparging",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "N2_percent": 80,
      "CO2_percent": 20,
      "minutes": [
        30,
        45
      ]
    },
    "rationale": "Restore missing target/KOMODO procedure while retaining source-derived DSMZ main context; move SL-11 instructions into the restored stock. Preserve conditional wording and stage; do not infer an unstated gas percentage basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, main or SL-11 preparation",
        "exact_source_quote": "with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q49",
    "component_or_context": "Initial main pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "before dispensing",
      "pH": [
        6.4,
        6.8
      ]
    },
    "rationale": "Restore missing target/KOMODO procedure while retaining source-derived DSMZ main context; move SL-11 instructions into the restored stock. Preserve conditional wording and stage; do not infer an unstated gas percentage basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, main or SL-11 preparation",
        "exact_source_quote": "make it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q50",
    "component_or_context": "Late-stock gas",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "late additions",
      "N2_percent": 100
    },
    "rationale": "Restore missing target/KOMODO procedure while retaining source-derived DSMZ main context; move SL-11 instructions into the restored stock. Preserve conditional wording and stage; do not infer an unstated gas percentage basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, main or SL-11 preparation",
        "exact_source_quote": "cysteine from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q51",
    "component_or_context": "Complete medium pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "complete medium",
      "pH": 7,
      "conditional": true
    },
    "rationale": "Restore missing target/KOMODO procedure while retaining source-derived DSMZ main context; move SL-11 instructions into the restored stock. Preserve conditional wording and stage; do not infer an unstated gas percentage basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, main or SL-11 preparation",
        "exact_source_quote": "the complete medium to 7.0, if necessary.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q52",
    "component_or_context": "SL-11 initial solvent",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "initial_water_ml": 800,
      "initial_pH": 7,
      "NaOH_normality": 2,
      "NaOH_dose": null
    },
    "rationale": "Restore missing target/KOMODO procedure while retaining source-derived DSMZ main context; move SL-11 instructions into the restored stock. Preserve conditional wording and stage; do not infer an unstated gas percentage basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, main or SL-11 preparation",
        "exact_source_quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q53",
    "component_or_context": "SL-11 final pH and volume",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-11",
      "final_pH": 6,
      "final_makeup_ml": 1000
    },
    "rationale": "Restore missing target/KOMODO procedure while retaining source-derived DSMZ main context; move SL-11 instructions into the restored stock. Preserve conditional wording and stage; do not infer an unstated gas percentage basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Pages1–2, main or SL-11 preparation",
        "exact_source_quote": "and bring volume to 1000 ml.",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      },
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 2 preceding SL-11 instruction",
        "exact_source_quote": "chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q54",
    "component_or_context": "SL-11 NaOH titration",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "reagent": "2 N NaOH",
      "dose": null
    },
    "rationale": "The source quantifies strength and target pH, not an amount of titrant.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 2 SL-11 preparation",
        "exact_source_quote": "adjust pH to 7 using 2 N NaOH",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q55",
    "component_or_context": "Main final-volume declaration and liquid-sum discrepancy",
    "decision": "evidence_only",
    "local_fields": [],
    "proposed_source_representation": {
      "declared_final_ml": 1003,
      "sum_of_listed_liquids_ml": 1003.5,
      "additional_late_stock_volumes": null
    },
    "rationale": "1000+1+1+0.5+1=1003.5 mL; source separately declares1003 mL. Preserve both rather than presenting the liquid sum as a measured final volume or silently changing the published denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 header",
        "exact_source_quote": "Final volume: 1003 ml",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  },
  {
    "quantity_id": "q56",
    "component_or_context": "Autoclaving and filter sterilization without numeric cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary."
          },
          {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."
          }
        ],
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "autoclave_temperature": null,
      "autoclave_duration": null,
      "vitamins": "filter sterilized"
    },
    "rationale": "Source method/order is explicit but no numeric autoclave cycle is given; missing layers need the exact method, not a guessed time or temperature.",
    "source_snippets": [
      {
        "source_key": "dsmz1004",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose, sulfide, and",
        "snapshot_sha256": "763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e",
        "parsed_text_sha256": "6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:003504.

31 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 31/32 primary and 29/32 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 32: primary 96.88%; secondary 90.62%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:003504.

53 timestamp instances inspected; 10 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Base source and five distinct maintained contributors

identity: concern. Targets: CultureMech:003504.

DSMZ1004 and KOMODO1004 identify the base; three KOMODO child accessions identify strain-specific branches. Current normalized topology correctly labels those children as variants, but their 32 ingredient quantities remain identical to the base. The older generated merge still collapses them as SOURCE_DUPLICATE and synonyms. Current primary clauses resolve the three formulation differences.

### Claim-level amount support and history

evidence: concern. Targets: CultureMech:003504.

All 192 local ingredient concentrations are covered by exact primary snippets and owner-specific decisions. Existing values have no attached quantity evidence. The ten base rates agree with the declared 1003 mL denominator to stored rounding; stock values and child overrides require separate scope. Historical reports are derivative only and current 503 responses do not verify their past graph assignments.

### Exact salts and stock ingredients

grounding: concern. Targets: CultureMech:003504.

Source sodium resazurin differs from neutral CHEBI:8806, and source nickel hexahydrate differs from anhydrous CHEBI:34887. The source EDTA dihydrate matches CHEBI:64758; calcium D-(+)-pantothenate is compatible with CHEBI:31345. Generic lipoic acid CHEBI:16494 is not contradicted solely by the source DL label. Vitamin and mineral identities remain stock-scoped.

### Main procedure, three stock preparations and variant clauses

completeness: concern. Targets: CultureMech:003504.

Only the DSMZ owner retains main anaerobic preparation and SL-11 titration/make-up. Target and KOMODO layers omit this preparation; stock instructions need nested scope. The complete primary resolves stock quantities and current strain branches despite optional live-provider access limits. Its declared final volume and listed-liquid arithmetic discrepancy are retained explicitly.

### Medium classification, catalog atmosphere and growth scope

scope: concern. Targets: CultureMech:003504.

COMPLEX/UNDEFINED and LIQUID fit the yeast-extract base. Imported Aerobic: Yes must remain catalog provenance and cannot override anoxic preparation. The three child ingredients_curated flags and repaired topology do not certify formula correctness. Strain-specific source recipe clauses are not experimental growth results or taxonomic ID assignments.

### Current writers and maintained input follow-up

provenance: concern. Targets: CultureMech:003504.

The current KOMODO1004 repair hardcodes the same 32 ingredient signature and modifies relationships/history/flags, not formula quantities. Its September events are later than the generated August merge, so only this directly recorded local chronology is asserted. Current MediaDive parser separates stock additions but collects solution steps at root. Current lossless merging does not scientifically correct retained inputs; repair all five owner formulas/variant scopes before regeneration.

## Findings

### f1: Three stock recipes are flattened as direct main concentrations

blocker / open / confirmed; issue key: culturemech.003504.stock-collapse.

All six local layers place 22 SL-11, selenite-tungstate and Wolin10x constituents at stock-level quantities among main ingredients, without receiving-dose or water containers.

### f2: Three strain wrappers retain the base formula despite explicit overrides

blocker / open / confirmed; issue key: culturemech.003504.erased-strain-formulas.

KOMODO1004.1 still contains base glucose and yeast instead of 7.2 g/L sucrose plus 0.1 g/L yeast;1004.2 retains glucose and base yeast instead of omission plus 0.1 g/L yeast;1004.3 retains base glucose instead of 5 g/L. The target additionally merges the distinct branches as duplicates/synonyms.

### f3: Dye salt and nickel hydrate are mapped to different forms

major / open / confirmed; issue key: culturemech.003504.supplied-form-mismatch.

Sodium resazurin is asserted as neutral CHEBI:8806 and nickel hexahydrate as Cl2Ni CHEBI:34887 in all layers. These are supplied-form conflicts, unlike the compatible calcium D-pantothenate and generic DL-lipoic mappings.

### f4: Preparation is missing outside the DSMZ owner and stock instructions remain at root

major / open / confirmed; issue key: culturemech.003504.preparation-and-flag-scope.

Target/KOMODO layers lose source anaerobic preparation and filtration qualifiers. The DSMZ owner retains SL-11 solvent/pH/make-up instructions at main root, and repaired child flags overstate unchanged formulation curation.

### f5: Historical KOMODO timestamps are malformed or timezone-naive

minor / open / confirmed; issue key: culturemech.003504.historical-timestamp-shape.

The target and four KOMODO maintained records retain malformed import timestamps and naive enrichment timestamps; later repair history is preserved separately.

## Recommended Actions And Acceptance Checks

### a1

Restore the three stocks, exact stock preparation and 1 mL doses in all five maintained owners while keeping base amounts on the declared 1003 mL basis. Preserve the separately reported liquid-sum discrepancy and attach narrow evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Correct each exact child owner using its own current primary strain clause, preserve source IDs and later topology repair history, and regenerate only after variant-aware formulation comparison. Keep source-only DSM23815/103421 branches separate from these wrappers and the base.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify source-compatible identifiers for the sodium dye and nickel hydrate in every owner, independently check secondary mappings and preserve exact source forms without inventing IDs.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Retain main and variant procedures in the correct owners, nest stock instructions, qualify unsupported ingredients_curated flags and imported aerobic metadata, and preserve all source stage qualifiers. No numeric sterilization cycle is supplied.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Append an exact dated clarification when authorized instead of rewriting historical events; improve future timestamp writers separately.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anaerolinea_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-2 | data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-3 | data/normalized_yaml/bacterial/for_dsm_16556.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-4 | data/normalized_yaml/bacterial/for_dsm_22659.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch028/275/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/275/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml:1:id: CultureMech:003504<br>./data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml:1:id: CultureMech:003504<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/275/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 52 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/275/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf; Pages 1–2, header, main table, five strain clauses and three stock subsections | supports | The exact primary declares final pH 7 and final volume 1003 mL. Listed water and liquid additions total 1003.5 mL before unspecified late-stock volumes. The declared basis is explicit; it is not replaced by the liquid sum. Three local strain wrappers and two additional source-only branches are distinguished. |
| sl11-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium722.pdf; SL-11 subsection only | supports | Only the stock explicitly referenced by DSMZ1004 is in scope; no parent basal medium, unrelated preparation or growth claim transfers. |
| selenite-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf; Selenite-tungstate subsection only | supports | Only the stock explicitly referenced by DSMZ1004 is in scope; no parent basal medium, unrelated preparation or growth claim transfers. |
| vitamin-parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf; Wolin's vitamin solution 10x subsection only | supports | Only the stock explicitly referenced by DSMZ1004 is in scope; no parent basal medium, unrelated preparation or growth claim transfers. |
| stock777 | https://mediadive.dsmz.de/rest/solution/777; $.data.id/name/recipe | supports | Current endpoint 777 describes selenite-tungstate, not SL-11. Any historical report assignment is derivative context; no current raw medium graph was retrieved, and no chronology is inferred. |
| stock5980 | https://mediadive.dsmz.de/rest/solution/5980; $.data.recipe, vitamin stock only | supports | Current Wolin10x stock is scoped as corroborating stock identity; the exact DSMZ1004 subsection controls this review. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch028/275/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15940 resolves to nicotinic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16494 resolves to lipoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17015 resolves to riboflavin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27470 resolves to folic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30961 resolves to pyridoxine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31345 resolves to Calcium pantothenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:64758 resolves to EDTA disodium salt dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64758": [{"label": "Na2EDTA·2H2O", "match_type": "preferred_term", "identifier": "CHEBI:64758", "preferred_term": "Na2EDTA·2H2O", "ontology_id": "CHEBI:64758", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml; data/normalized_yaml/bacterial/anaerolinea_medium.yaml; data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml; data/normalized_yaml/bacterial/for_dsm_16556.yaml; data/normalized_yaml/bacterial/for_dsm_22659.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:02.269851"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:02.269851"}]}, {"input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.173469"}]}, {"input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:01.398658"}]}, {"input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:10.307730"}]}] |
| current-code-0 | scripts/repair_komodo_1004_anaerolinea_score10.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | The current KOMODO1004 repair hardcodes the same 32 ingredient signature and modifies relationships/history/flags, not formula quantities. Its September events are later than the generated August merge, so only this directly recorded local chronology is asserted. Current MediaDive parser separates stock additions but collects solution steps at root. Current lossless merging does not scientifically correct retained inputs; repair all five owner formulas/variant scopes before regeneration. |
| current-code-1 | src/culturemech/import/mediadive_importer.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | The current KOMODO1004 repair hardcodes the same 32 ingredient signature and modifies relationships/history/flags, not formula quantities. Its September events are later than the generated August merge, so only this directly recorded local chronology is asserted. Current MediaDive parser separates stock additions but collects solution steps at root. Current lossless merging does not scientifically correct retained inputs; repair all five owner formulas/variant scopes before regeneration. |
| current-code-2 | src/culturemech/merge/formulation.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | The current KOMODO1004 repair hardcodes the same 32 ingredient signature and modifies relationships/history/flags, not formula quantities. Its September events are later than the generated August merge, so only this directly recorded local chronology is asserted. Current MediaDive parser separates stock additions but collects solution steps at root. Current lossless merging does not scientifically correct retained inputs; repair all five owner formulas/variant scopes before regeneration. |
| mediadive1004api-attempt | https://mediadive.dsmz.de/rest/medium/1004; Preserved exact public retrieval result | context_only | Exact mediadive1004api access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| mediadive1004apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/1004; Preserved exact public retrieval result | context_only | Exact mediadive1004apiRetry access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004; Preserved exact public retrieval result | context_only | Exact komodo1004detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004; Preserved exact public retrieval result | context_only | Exact komodo1004actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004_1detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004.1; Preserved exact public retrieval result | context_only | Exact komodo1004_1detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004_1actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004.1; Preserved exact public retrieval result | context_only | Exact komodo1004_1actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004_2detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004.2; Preserved exact public retrieval result | context_only | Exact komodo1004_2detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004_2actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004.2; Preserved exact public retrieval result | context_only | Exact komodo1004_2actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004_3detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004.3; Preserved exact public retrieval result | context_only | Exact komodo1004_3detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| komodo1004_3actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004.3; Preserved exact public retrieval result | context_only | Exact komodo1004_3actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |
| solution1474-attempt | https://mediadive.dsmz.de/rest/solution/1474; Preserved exact public retrieval result | context_only | Exact solution1474 access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact mediadive1004api access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact mediadive1004apiRetry access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004_1detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004_1actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004_2detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004_2actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004_3detail access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact komodo1004_3actual access returned 403. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Exact solution1474 access returned 503. This limits live/historical provider corroboration but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Completed means the current source-scoped comparison is complete, not that the recipe is correct. Optional provider 403/503 failures are retained; no historical response or temporal priority between sources is fabricated.
- Source-declared 1003 mL, listed 1003.5 mL and unquantified late-stock volumes remain distinct. No strain clause is generalized into a growth claim.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T154841Z-culturemech-003504-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerolinea_medium (CultureMech:003504)'
started_at: '2026-10-21T15:43:30Z'
finished_at: '2026-10-21T15:48:41Z'
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
summary: The complete DSMZ1004 source supports the base formula and explicit strain
  branches, but all five owners flatten three stocks and the three KOMODO strain wrappers
  still retain the unchanged base quantities. Later topology repairs are absent from
  the generated merge and do not cure formulation differences. Declared1003 mL and
  listed 1003.5 mL are preserved separately; sodium-resazurin and nickel-hydrate mappings
  and preparation scope require curation.
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
  - path: data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
    sha256: 6a1b44ea1f6e402df62b6a33ee4f52918965cce6678954dccc96af4986b9691b
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    sha256: 256727b084931b70bc93b1381bacaacb4a2126a63f8415dbe7e4ab21653cc91f
    role: context
  - path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    sha256: 3113ba80f6c2b4927c6093234d7b01c286904ea9d8c6976132bc47546ea7c089
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    sha256: f01d415134eccf7413cc404ff9d3ab39941e4fa3160fd856ac435c27bc40454e
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    sha256: 44710ae88ca6e98a29f3841144218dce51f3b8fc72bc7445b75fb7f2036bdaca
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
    sha256: 3eee5ac3f2451904b86c3da2b8751a93b80ac3ed549f685991db65cac10969ad
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/anaerolinea_medium.yaml.md
    sha256: cec29d6ec024d3172930711473410b8216c9b644a94abd4f674d97fe5174c007
    role: context
  - path: reports/ingredient_concentration_curation/20261007-medium-source-fetch-1000-1500.json
    sha256: 761d2a33438aa346d4b1056044434672c73b3827429924ffec621f3c23f582f3
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_komodo_1004_anaerolinea_score10.py
    sha256: 8874edb2e719b82347dbe8ce7b407a0a2bb219f8253cac9a2debc44a7557ddbb
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
  selection: Task review 275; batch 028 item 5 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-seven task batches
    contain 270 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 273 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003504
targets:
- target_id: CultureMech:003504
  path: data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  label: anaerolinea_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch028/275/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/275/strict.tsv"
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:003504
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
  - CultureMech:003504
- check_id: mediadive1004api-source-access
  name: 'Exact source content access: mediadive1004api'
  required: false
  status: unavailable
  summary: Exact mediadive1004api access returned 503. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - mediadive1004api-attempt
- check_id: mediadive1004apiRetry-source-access
  name: 'Exact source content access: mediadive1004apiRetry'
  required: false
  status: unavailable
  summary: Exact mediadive1004apiRetry access returned 503. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - mediadive1004apiRetry-attempt
- check_id: komodo1004detail-source-access
  name: 'Exact source content access: komodo1004detail'
  required: false
  status: unavailable
  summary: Exact komodo1004detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004detail-attempt
- check_id: komodo1004actual-source-access
  name: 'Exact source content access: komodo1004actual'
  required: false
  status: unavailable
  summary: Exact komodo1004actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004actual-attempt
- check_id: komodo1004_1detail-source-access
  name: 'Exact source content access: komodo1004_1detail'
  required: false
  status: unavailable
  summary: Exact komodo1004_1detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004_1detail-attempt
- check_id: komodo1004_1actual-source-access
  name: 'Exact source content access: komodo1004_1actual'
  required: false
  status: unavailable
  summary: Exact komodo1004_1actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004_1actual-attempt
- check_id: komodo1004_2detail-source-access
  name: 'Exact source content access: komodo1004_2detail'
  required: false
  status: unavailable
  summary: Exact komodo1004_2detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004_2detail-attempt
- check_id: komodo1004_2actual-source-access
  name: 'Exact source content access: komodo1004_2actual'
  required: false
  status: unavailable
  summary: Exact komodo1004_2actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004_2actual-attempt
- check_id: komodo1004_3detail-source-access
  name: 'Exact source content access: komodo1004_3detail'
  required: false
  status: unavailable
  summary: Exact komodo1004_3detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004_3detail-attempt
- check_id: komodo1004_3actual-source-access
  name: 'Exact source content access: komodo1004_3actual'
  required: false
  status: unavailable
  summary: Exact komodo1004_3actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - komodo1004_3actual-attempt
- check_id: solution1474-source-access
  name: 'Exact source content access: solution1474'
  required: false
  status: unavailable
  summary: Exact solution1474 access returned 503. This limits live/historical provider
    corroboration but does not make the complete current DSMZ1004 base and named strain
    clauses unavailable.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - solution1474-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_16556.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_22659.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:01.436161Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch028/275/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:02.815417Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/275/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:04.413744Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:05.470957Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:48:40Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml:1:id: CultureMech:003504

    ./data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml:1:id: CultureMech:003504

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/275/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:48:40Z'
  support: supports
  summary: 52 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 38969e4d9b2c7ce3afa9f41c2b97e53de442fe6f138b7129a5b4f23c0066aa6d
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/275/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: 5b401f8a74572b82120ac4cf26a784d85eb2bfb4f546fe63f666320ff73fa89b
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf
  locator: Pages 1–2, header, main table, five strain clauses and three stock subsections
  accessed_at: '2026-10-21T15:16:37.305051Z'
  support: supports
  summary: The exact primary declares final pH 7 and final volume 1003 mL. Listed
    water and liquid additions total 1003.5 mL before unspecified late-stock volumes.
    The declared basis is explicit; it is not replaced by the liquid sum. Three local
    strain wrappers and two additional source-only branches are distinguished.
  snapshot_sha256: 763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e
- evidence_id: sl11-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium722.pdf
  locator: SL-11 subsection only
  accessed_at: '2026-10-21T15:19:01.126368Z'
  support: supports
  summary: Only the stock explicitly referenced by DSMZ1004 is in scope; no parent
    basal medium, unrelated preparation or growth claim transfers.
  snapshot_sha256: 94de358595d83bc207746f65465493947bb0f4217ad5f2224843c9f6a953a9f8
- evidence_id: selenite-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium385.pdf
  locator: Selenite-tungstate subsection only
  accessed_at: '2026-10-21T13:20:08.153235Z'
  support: supports
  summary: Only the stock explicitly referenced by DSMZ1004 is in scope; no parent
    basal medium, unrelated preparation or growth claim transfers.
  snapshot_sha256: d660a2e55a1d419557c01f865afb7182891ad859743bc686f53b95d3643eec22
- evidence_id: vitamin-parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium120.pdf
  locator: Wolin's vitamin solution 10x subsection only
  accessed_at: '2026-10-21T13:16:27.298931Z'
  support: supports
  summary: Only the stock explicitly referenced by DSMZ1004 is in scope; no parent
    basal medium, unrelated preparation or growth claim transfers.
  snapshot_sha256: e1f85e4a546abc825218226bbb18d78bd9c054b7e11399aa7161ad259a3b663f
- evidence_id: stock777
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/777
  locator: $.data.id/name/recipe
  accessed_at: '2026-10-21T13:20:07.510517Z'
  support: supports
  summary: Current endpoint 777 describes selenite-tungstate, not SL-11. Any historical
    report assignment is derivative context; no current raw medium graph was retrieved,
    and no chronology is inferred.
  snapshot_sha256: 3845d8e8d84cc22cea487e32868daa4343a41eb10d3ca6c1bf4cc94edc8459f2
- evidence_id: stock5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  locator: $.data.recipe, vitamin stock only
  accessed_at: '2026-10-21T11:03:05.362213Z'
  support: supports
  summary: Current Wolin10x stock is scoped as corroborating stock identity; the exact
    DSMZ1004 subsection controls this review.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/275/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 3f0662cb7a8cb9ed291571ffde97756266b613e684e5d7b26761b28f7b705cc2
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
- evidence_id: chebi64758
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:16:38.372353Z'
  support: supports
  summary: CHEBI:64758 resolves to EDTA disodium salt dihydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 5432921ff4fea3479e93ce6392a2654e3d5560255beb96022793102e776d9647
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
  accessed_at: '2026-10-21T15:48:40Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
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
    "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:176843": [{"label": "Vitamin
    B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term":
    "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity":
    "resolved:owned"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label":
    "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753",
    "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride",
    "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term":
    "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label":
    "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label":
    "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term":
    "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label":
    "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503",
    "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id":
    "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:64758":
    [{"label": "Na2EDTA·2H2O", "match_type": "preferred_term", "identifier": "CHEBI:64758",
    "preferred_term": "Na2EDTA·2H2O", "ontology_id": "CHEBI:64758", "mapping_status":
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
  reference: data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml;
    data/normalized_yaml/bacterial/anaerolinea_medium.yaml; data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml;
    data/normalized_yaml/bacterial/for_dsm_16556.yaml; data/normalized_yaml/bacterial/for_dsm_22659.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: '[{"input": "target", "events": 10, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:02.269851"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:02.269851"}]}, {"input": "data/normalized_yaml/bacterial/anaerolinea_medium.yaml",
    "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:10.173469"}]}, {"input": "data/normalized_yaml/bacterial/for_dsm_16556.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:01.398658"}]}, {"input": "data/normalized_yaml/bacterial/for_dsm_22659.yaml",
    "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:01.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:10.307730"}]}]'
- evidence_id: current-code-0
  kind: record_content
  reference: scripts/repair_komodo_1004_anaerolinea_score10.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: The current KOMODO1004 repair hardcodes the same 32 ingredient signature
    and modifies relationships/history/flags, not formula quantities. Its September
    events are later than the generated August merge, so only this directly recorded
    local chronology is asserted. Current MediaDive parser separates stock additions
    but collects solution steps at root. Current lossless merging does not scientifically
    correct retained inputs; repair all five owner formulas/variant scopes before
    regeneration.
  snapshot_sha256: 8874edb2e719b82347dbe8ce7b407a0a2bb219f8253cac9a2debc44a7557ddbb
- evidence_id: current-code-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: The current KOMODO1004 repair hardcodes the same 32 ingredient signature
    and modifies relationships/history/flags, not formula quantities. Its September
    events are later than the generated August merge, so only this directly recorded
    local chronology is asserted. Current MediaDive parser separates stock additions
    but collects solution steps at root. Current lossless merging does not scientifically
    correct retained inputs; repair all five owner formulas/variant scopes before
    regeneration.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:48:40Z'
  support: context_only
  summary: The current KOMODO1004 repair hardcodes the same 32 ingredient signature
    and modifies relationships/history/flags, not formula quantities. Its September
    events are later than the generated August merge, so only this directly recorded
    local chronology is asserted. Current MediaDive parser separates stock additions
    but collects solution steps at root. Current lossless merging does not scientifically
    correct retained inputs; repair all five owner formulas/variant scopes before
    regeneration.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: mediadive1004api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1004
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.733561Z'
  support: context_only
  summary: Exact mediadive1004api access returned 503. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1004apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1004
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.505323Z'
  support: context_only
  summary: Exact mediadive1004apiRetry access returned 503. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo1004detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.096908Z'
  support: context_only
  summary: Exact komodo1004detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: a89c5e06651ed5121a89da19bc77efcb33707a6492cf06ad22a0b21d5e6fde2f
- evidence_id: komodo1004actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:18:59.960357Z'
  support: context_only
  summary: Exact komodo1004actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 93983ff00eb1b5c993114ca9ab1cfa270dbc542755d5393e5006077dad0445cf
- evidence_id: komodo1004_1detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.096592Z'
  support: context_only
  summary: Exact komodo1004_1detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 0de5ef5aa85678a6d3c826162b6605affca7c6c0f9a16590747a2b88751d4ee8
- evidence_id: komodo1004_1actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004.1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:18:59.960876Z'
  support: context_only
  summary: Exact komodo1004_1actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 7f3c27d3139e4f0f4a471d701b393fc651acaf9898aca0f3766d06c7e06c293b
- evidence_id: komodo1004_2detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004.2
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.097502Z'
  support: context_only
  summary: Exact komodo1004_2detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 2d839117f623359df7a3199fc14b80a8b49befec7b170807a60f344c60e9fb57
- evidence_id: komodo1004_2actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004.2
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:18:59.961117Z'
  support: context_only
  summary: Exact komodo1004_2actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 7454fd679c9195746ed9c3f714d6c609380e1fc9ecb8d2b1d800f19e16785635
- evidence_id: komodo1004_3detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=1004.3
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.097946Z'
  support: context_only
  summary: Exact komodo1004_3detail access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 06360f687b13a76eaeacb5d1792f727e80700946250e3d999db579d17fc9bb42
- evidence_id: komodo1004_3actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1004.3
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:18:59.961515Z'
  support: context_only
  summary: Exact komodo1004_3actual access returned 403. This limits live/historical
    provider corroboration but does not make the complete current DSMZ1004 base and
    named strain clauses unavailable.
  snapshot_sha256: 0fce144c1b2d9909f8bf44d58200e9dc8bb39aef09fb6d5159bf0754b8ab505c
- evidence_id: solution1474-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/1474
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:20:32.862654Z'
  support: context_only
  summary: Exact solution1474 access returned 503. This limits live/historical provider
    corroboration but does not make the complete current DSMZ1004 base and named strain
    clauses unavailable.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 56 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Base KH2PO4\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.139581\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.139581\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.139581\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.139581\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"\
    field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.139581\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.139581\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.14,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.1395812562313060817547357926\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.14 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Base MgCl2 x 6 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.199402\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.199402\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.199402\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.199402\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"\
    field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.199402\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.199402\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.2,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.1994017946161515453639082752\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 0.20 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Base CaCl2 x 2 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.149551\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.149551\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.149551\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.149551\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.149551\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.149551\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.15,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.1495513459621136590229312064\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.15 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Base NH4Cl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.538385\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.538385\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.538385\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.538385\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.538385\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.538385\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.54,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.5383848454636091724825523430\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.54 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Base Sodium resazurin\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"evidence_only\"\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n     \
    \   \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.0005,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.0004985044865403788634097706879\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. The source 0.5 mL of 0.1%\
    \ w/v stock yields 0.0005 g before normalization; preserve sodium-salt identity.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Base NaHCO3\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.49252\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.49252\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.49252\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.49252\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2.49252\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.49252\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 2.5,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"2.492522432701894317048853440\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"NaHCO3 2.50 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Base Yeast extract\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.29312\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.29312\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.29312\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2.29312\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 2.3,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"2.293120638085742771684945165\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 2.30 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Base D-Glucose\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.19342\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.19342\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"2.19342\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 2.2,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"2.193419740777666999002991027\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"D-Glucose 2.20 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Base L-Cysteine HCl x H2O\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"\
    field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[8].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.249252\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.25,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.2492522432701894317048853440\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"L-Cysteine HCl x H2O 0.25 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Base Na2S x 9 H2O\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"evidence_only\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"\
    field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.249252\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"base receiving batch\",\n      \"source_mass_g\": 0.25,\n\
    \      \"source_declared_final_ml\": 1003,\n      \"derived_g_per_l\": \"0.2492522432701894317048853440\"\
    \n    },\n    \"rationale\": \"The existing base rate agrees to stored rounding\
    \ with the literal mass divided by the source-declared 1.003 L. No attached local\
    \ evidence exists, so the decision is evidence_only. Do not replace the declared\
    \ basis with the 1003.5 mL liquid sum or apply this base row over a strain-specific\
    \ override.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 base main table\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.25 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\":\
    \ \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"SL-11: Na2-EDTA x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 5.2,\n      \"source_unit\"\
    : \"g\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"Na2-EDTA x 2 H2O 5.20 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"SL-11: FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 1.5,\n      \"source_unit\"\
    : \"g\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"SL-11: ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 70,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"SL-11: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 100,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"SL-11: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[14].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 6,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"SL-11: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 190,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"SL-11: CuCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[16].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 2,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"SL-11: NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 24,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"SL-11: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"source_amount\": 36,\n      \"source_unit\"\
    : \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\": 1000,\n\
    \      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The existing\
    \ scalar is a stock-level numerical amount/rate, not a main ingredient concentration.\
    \ Restore the exact stock recipe and 1 mL receiving dose. SL-11 has explicit final\
    \ make-up; the other stock tables state water input, not a measured finished volume.\
    \ No arbitrary whole-stock transfer is allowed.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, SL-11 subsection\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"Selenite-tungstate: NaOH\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Selenite-tungstate\",\n      \"source_amount\": 0.5,\n\
    \      \"source_unit\": \"g\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Selenite-tungstate subsection\",\n\
    \        \"exact_source_quote\": \"NaOH 0.50 g\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Selenite-tungstate: Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.003\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.003\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Selenite-tungstate\",\n      \"source_amount\": 3,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Selenite-tungstate subsection\",\n\
    \        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 3.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"Selenite-tungstate: Na2WO4 x 2 H2O\",\n    \"decision\": \"correct\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.004\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.004\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Selenite-tungstate\",\n      \"source_amount\": 4,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Selenite-tungstate subsection\",\n\
    \        \"exact_source_quote\": \"Na2WO4 x 2 H2O 4.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Biotin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[22].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 20,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Biotin 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Folic acid\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.02\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 20,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Folic acid 20.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Pyridoxine hydrochloride\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 100,\n\
    \      \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Pyridoxine hydrochloride 100.00 mg\",\n    \
    \    \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Thiamine HCl\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Thiamine HCl 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Riboflavin\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[26].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Riboflavin 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Nicotinic acid\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[27].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Nicotinic acid 50.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Calcium D-(+)-pantothenate\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[28].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[28].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Calcium D-(+)-pantothenate 50.00 mg\",\n   \
    \     \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: Vitamin B12\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[29].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[29].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 1,\n  \
    \    \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"Vitamin B12 1.00 mg\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: p-Aminobenzoic acid\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[30].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[30].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[30].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"p-Aminobenzoic acid 50.00 mg\",\n        \"\
    snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Wolin10x vitamins: (DL)-alpha-Lipoic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[31].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"ingredients[31].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.05\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[31].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"source_amount\": 50,\n \
    \     \"source_unit\": \"mg\",\n      \"water_ml\": 1000,\n      \"stock_final_makeup_ml\"\
    : null,\n      \"main_receiving_dose_ml\": 1\n    },\n    \"rationale\": \"The\
    \ existing scalar is a stock-level numerical amount/rate, not a main ingredient\
    \ concentration. Restore the exact stock recipe and 1 mL receiving dose. SL-11\
    \ has explicit final make-up; the other stock tables state water input, not a\
    \ measured finished volume. No arbitrary whole-stock transfer is allowed.\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, Wolin10x vitamins subsection\",\n \
    \       \"exact_source_quote\": \"(DL)-alpha-Lipoic acid 50.00 mg\",\n       \
    \ \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"base main\",\n      \"water_ml\": 1000\n    },\n    \"\
    rationale\": \"Restore the separate solvent input in its named scope; do not sum\
    \ stock preparation water into the receiving medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Exact Main water table row; repeated text distinguished\
    \ by subsection\",\n        \"exact_source_quote\": \"Distilled water 1000.00\
    \ ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"SL-11 water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"water_ml\": 1000,\n      \"final_makeup_ml\"\
    : 1000\n    },\n    \"rationale\": \"Restore the separate solvent input in its\
    \ named scope; do not sum stock preparation water into the receiving medium.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Exact SL-11 water table row; repeated text distinguished\
    \ by subsection\",\n        \"exact_source_quote\": \"Distilled water 1000.00\
    \ ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Selenite-tungstate water\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"selenite-tungstate\",\n      \"water_ml\": 1000\n    },\n\
    \    \"rationale\": \"Restore the separate solvent input in its named scope; do\
    \ not sum stock preparation water into the receiving medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Exact Selenite-tungstate water table row; repeated text\
    \ distinguished by subsection\",\n        \"exact_source_quote\": \"Distilled\
    \ water 1000.00 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Wolin10x water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Wolin10x vitamins\",\n      \"water_ml\": 1000\n    },\n\
    \    \"rationale\": \"Restore the separate solvent input in its named scope; do\
    \ not sum stock preparation water into the receiving medium.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Exact Wolin10x water table row; repeated text distinguished\
    \ by subsection\",\n        \"exact_source_quote\": \"Distilled water 1000.00\
    \ ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"Base stock dose SL-11\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"SL-11\",\n      \"dose_ml\": 1\n    },\n    \"rationale\"\
    : \"Restore the explicit receiving stock addition, distinct from the stock recipe\
    \ and the declared 1003 mL final-volume header.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-11 1.00 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"Base stock dose selenite-tungstate\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"selenite-tungstate\",\n      \"dose_ml\": 1\n    },\n\
    \    \"rationale\": \"Restore the explicit receiving stock addition, distinct\
    \ from the stock recipe and the declared 1003 mL final-volume header.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Selenite-tungstate solution 1.00 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Base stock dose sodium resazurin\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"sodium resazurin\",\n      \"dose_ml\": 0.5,\n      \"\
    strength\": \"0.1% w/v\"\n    },\n    \"rationale\": \"Restore the explicit receiving\
    \ stock addition, distinct from the stock recipe and the declared 1003 mL final-volume\
    \ header.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Base stock dose Wolin10x vitamins\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock\": \"Wolin10x vitamins\",\n      \"dose_ml\": 1\n    },\n \
    \   \"rationale\": \"Restore the explicit receiving stock addition, distinct from\
    \ the stock recipe and the declared 1003 mL final-volume header.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\":\
    \ \"Wolin's vitamin solution (10x) 1.00 ml\",\n        \"snapshot_sha256\": \"\
    763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n        \"\
    parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"Variant komodo.medium:1004.1 Yeast extract\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.29312\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"variant\": \"komodo.medium:1004.1\",\n      \"yeast_extract_g_per_l\"\
    : 0.1\n    },\n    \"rationale\": \"The current primary explicitly resolves this\
    \ branch. Preserve its g/L instruction as printed; do not divide it again by 1.003\
    \ or alter the base recipe. Later topology-only repair and ingredients_curated\
    \ flag do not establish that the unchanged child amounts were scientifically corrected.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 exact named strain clause\",\n       \
    \ \"exact_source_quote\": \"reduce amount of yeast extract to 0.10 g/l.\",\n \
    \       \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"Variant komodo.medium:1004.1 D-Glucose\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.19342\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"variant\": \"komodo.medium:1004.1\",\n      \"glucose\": \"replace\"\
    ,\n      \"sucrose_g_per_l\": 7.2\n    },\n    \"rationale\": \"The current primary\
    \ explicitly resolves this branch. Preserve its g/L instruction as printed; do\
    \ not divide it again by 1.003 or alter the base recipe. Later topology-only repair\
    \ and ingredients_curated flag do not establish that the unchanged child amounts\
    \ were scientifically corrected.\",\n    \"source_snippets\": [\n      {\n   \
    \     \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 exact named strain clause\",\n       \
    \ \"exact_source_quote\": \"For DSM 16554, DSM 16555, DSM 17877: Replace glucose\
    \ with 7.20 g/l sucrose and\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"Variant komodo.medium:1004.2 Yeast extract\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.29312\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"variant\": \"komodo.medium:1004.2\",\n      \"yeast_extract_g_per_l\"\
    : 0.1\n    },\n    \"rationale\": \"The current primary explicitly resolves this\
    \ branch. Preserve its g/L instruction as printed; do not divide it again by 1.003\
    \ or alter the base recipe. Later topology-only repair and ingredients_curated\
    \ flag do not establish that the unchanged child amounts were scientifically corrected.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 exact named strain clause\",\n       \
    \ \"exact_source_quote\": \"For DSM 16556: Omit glucose and reduce amount of yeast\
    \ extract to 0.10 g/l.\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Variant komodo.medium:1004.2 D-Glucose\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.19342\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"variant\": \"komodo.medium:1004.2\",\n      \"glucose\": \"omit,\
    \ not a numeric zero concentration\"\n    },\n    \"rationale\": \"The current\
    \ primary explicitly resolves this branch. Preserve its g/L instruction as printed;\
    \ do not divide it again by 1.003 or alter the base recipe. Later topology-only\
    \ repair and ingredients_curated flag do not establish that the unchanged child\
    \ amounts were scientifically corrected.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 exact named strain clause\",\n       \
    \ \"exact_source_quote\": \"For DSM 16556: Omit glucose and reduce amount of yeast\
    \ extract to 0.10 g/l.\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"component_or_context\"\
    : \"Variant komodo.medium:1004.3 D-Glucose\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.19342\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"variant\": \"komodo.medium:1004.3\",\n      \"glucose_g_per_l\":\
    \ 5\n    },\n    \"rationale\": \"The current primary explicitly resolves this\
    \ branch. Preserve its g/L instruction as printed; do not divide it again by 1.003\
    \ or alter the base recipe. Later topology-only repair and ingredients_curated\
    \ flag do not establish that the unchanged child amounts were scientifically corrected.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 exact named strain clause\",\n       \
    \ \"exact_source_quote\": \"For DSM 22659: Increase amount of glucose to 5.00\
    \ g/l.\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"component_or_context\"\
    : \"Source-only DSM23815\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"proposed_source_representation\": {\n      \"branch\": \"DSM23815\"\
    ,\n      \"cellobiose_g_per_l\": 2,\n      \"glucose\": \"replace\",\n      \"\
    preparation\": \"sterile anoxic, filter-sterilized stock after autoclaving\"\n\
    \    },\n    \"rationale\": \"Source-only variant context: not one of the three\
    \ current local child wrappers and not a universal base adjustment. Retain separately\
    \ when documenting source scope; no growth result is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Page 1 additional source branch\",\n        \"exact_source_quote\"\
    : \"For DSM 23815: Replace glucose with 2.00 g/l cellobiose added after autoclaving\
    \ from a\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 1 continuation of DSM23815 clause\",\n      \
    \  \"exact_source_quote\": \"sterile anoxic stock solution sterilized by filtration.\"\
    ,\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q47\",\n    \"component_or_context\"\
    : \"Source-only DSM103421\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"proposed_source_representation\": {\n      \"branch\": \"DSM103421\"\
    ,\n      \"yeast_extract_g_per_l\": 0.1\n    },\n    \"rationale\": \"Source-only\
    \ variant context: not one of the three current local child wrappers and not a\
    \ universal base adjustment. Retain separately when documenting source scope;\
    \ no growth result is inferred.\",\n    \"source_snippets\": [\n      {\n    \
    \    \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 additional source branch\",\n        \"\
    exact_source_quote\": \"For DSM 103421: Reduce amount of yeast extract to 0.1\
    \ g/l\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q48\",\n    \"component_or_context\"\
    : \"Main sparging\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium\
    \ under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, vitamins (sterilized by filtration),\
    \ glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"N2_percent\": 80,\n      \"CO2_percent\": 20,\n      \"minutes\"\
    : [\n        30,\n        45\n      ]\n    },\n    \"rationale\": \"Restore missing\
    \ target/KOMODO procedure while retaining source-derived DSMZ main context; move\
    \ SL-11 instructions into the restored stock. Preserve conditional wording and\
    \ stage; do not infer an unstated gas percentage basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Pages1–2, main or SL-11 preparation\",\n        \"exact_source_quote\"\
    : \"with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q49\",\n    \"component_or_context\"\
    : \"Initial main pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium\
    \ under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, vitamins (sterilized by filtration),\
    \ glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"before dispensing\",\n      \"pH\": [\n        6.4,\n\
    \        6.8\n      ]\n    },\n    \"rationale\": \"Restore missing target/KOMODO\
    \ procedure while retaining source-derived DSMZ main context; move SL-11 instructions\
    \ into the restored stock. Preserve conditional wording and stage; do not infer\
    \ an unstated gas percentage basis.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, main or SL-11 preparation\",\n    \
    \    \"exact_source_quote\": \"make it anoxic. Add solid bicarbonate and adjust\
    \ pH to 6.4 - 6.8.\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q50\",\n    \"component_or_context\"\
    : \"Late-stock gas\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium\
    \ under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, vitamins (sterilized by filtration),\
    \ glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"late additions\",\n      \"N2_percent\": 100\n    },\n\
    \    \"rationale\": \"Restore missing target/KOMODO procedure while retaining\
    \ source-derived DSMZ main context; move SL-11 instructions into the restored\
    \ stock. Preserve conditional wording and stage; do not infer an unstated gas\
    \ percentage basis.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, main or SL-11 preparation\",\n    \
    \    \"exact_source_quote\": \"cysteine from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas. Adjust the pH of\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q51\",\n    \"component_or_context\"\
    : \"Complete medium pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ (except bicarbonate, yeast extract, vitamins, glucose, and reducing agents),\
    \ then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make\
    \ it anoxic. Add solid bicarbonate and adjust pH to 6.4 - 6.8. Dispense medium\
    \ under 80% N2 and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum\
    \ vials and autoclave. Add yeast extract, vitamins (sterilized by filtration),\
    \ glucose, sulfide, and cysteine from sterile anoxic stock solutions prepared\
    \ under 100% N2 gas. Adjust the pH of the complete medium to 7.0, if necessary.\"\
    ,\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ph_value\",\n        \"stored\": 7.0,\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"complete medium\",\n      \"pH\": 7,\n      \"conditional\"\
    : true\n    },\n    \"rationale\": \"Restore missing target/KOMODO procedure while\
    \ retaining source-derived DSMZ main context; move SL-11 instructions into the\
    \ restored stock. Preserve conditional wording and stage; do not infer an unstated\
    \ gas percentage basis.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, main or SL-11 preparation\",\n    \
    \    \"exact_source_quote\": \"the complete medium to 7.0, if necessary.\",\n\
    \        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q52\",\n    \"component_or_context\"\
    : \"SL-11 initial solvent\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": \"Dissolve EDTA in\
    \ 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride.\
    \ After ferrous chloride has dissolved add other compounds. Finally adjust pH\
    \ to 6.0 and bring volume to 1000 ml.\",\n        \"decision\": \"correct\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"initial_water_ml\": 800,\n      \"initial_pH\"\
    : 7,\n      \"NaOH_normality\": 2,\n      \"NaOH_dose\": null\n    },\n    \"\
    rationale\": \"Restore missing target/KOMODO procedure while retaining source-derived\
    \ DSMZ main context; move SL-11 instructions into the restored stock. Preserve\
    \ conditional wording and stage; do not infer an unstated gas percentage basis.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, main or SL-11 preparation\",\n    \
    \    \"exact_source_quote\": \"Dissolve EDTA in 800 ml distilled water, adjust\
    \ pH to 7 using 2 N NaOH and add ferrous\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q53\",\n    \"component_or_context\"\
    : \"SL-11 final pH and volume\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": \"Dissolve EDTA in\
    \ 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride.\
    \ After ferrous chloride has dissolved add other compounds. Finally adjust pH\
    \ to 6.0 and bring volume to 1000 ml.\",\n        \"decision\": \"correct\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-11\",\n      \"final_pH\": 6,\n      \"final_makeup_ml\"\
    : 1000\n    },\n    \"rationale\": \"Restore missing target/KOMODO procedure while\
    \ retaining source-derived DSMZ main context; move SL-11 instructions into the\
    \ restored stock. Preserve conditional wording and stage; do not infer an unstated\
    \ gas percentage basis.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Pages1–2, main or SL-11 preparation\",\n    \
    \    \"exact_source_quote\": \"and bring volume to 1000 ml.\",\n        \"snapshot_sha256\"\
    : \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\",\n    \
    \    \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n   \
    \     \"source_locator\": \"Page 2 preceding SL-11 instruction\",\n        \"\
    exact_source_quote\": \"chloride. After ferrous chloride has dissolved add other\
    \ compounds. Finally adjust pH to 6.0\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q54\",\n    \"component_or_context\"\
    : \"SL-11 NaOH titration\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"reagent\": \"2 N NaOH\",\n      \"dose\": null\n    },\n    \"rationale\"\
    : \"The source quantifies strength and target pH, not an amount of titrant.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1004\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 2 SL-11 preparation\",\n        \"exact_source_quote\"\
    : \"adjust pH to 7 using 2 N NaOH\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q55\",\n    \"component_or_context\"\
    : \"Main final-volume declaration and liquid-sum discrepancy\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [],\n    \"proposed_source_representation\"\
    : {\n      \"declared_final_ml\": 1003,\n      \"sum_of_listed_liquids_ml\": 1003.5,\n\
    \      \"additional_late_stock_volumes\": null\n    },\n    \"rationale\": \"\
    1000+1+1+0.5+1=1003.5 mL; source separately declares1003 mL. Preserve both rather\
    \ than presenting the liquid sum as a measured final volume or silently changing\
    \ the published denominator.\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"dsmz1004\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\"\
    ,\n        \"source_locator\": \"Page 1 header\",\n        \"exact_source_quote\"\
    : \"Final volume: 1003 ml\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q56\",\n    \"component_or_context\"\
    : \"Autoclaving and filter sterilization without numeric cycle\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml\",\n        \"field_path\": \"\
    preparation_steps\",\n        \"stored\": null,\n        \"decision\": \"add\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerolinea_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve ingredients (except bicarbonate, yeast\
    \ extract, vitamins, glucose, and reducing agents), then sparge medium with 80%\
    \ N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add solid bicarbonate\
    \ and adjust pH to 6.4 - 6.8. Dispense medium under 80% N2 and 20% CO2 gas atmosphere\
    \ into anoxic Hungate-type tubes or serum vials and autoclave. Add yeast extract,\
    \ vitamins (sterilized by filtration), glucose, sulfide, and cysteine from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Adjust the pH of the complete\
    \ medium to 7.0, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"ADJUST_PH\",\n            \"description\": \"\
    Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add\
    \ ferrous chloride. After ferrous chloride has dissolved add other compounds.\
    \ Finally adjust pH to 6.0 and bring volume to 1000 ml.\"\n          }\n     \
    \   ],\n        \"decision\": \"evidence_only\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_16556.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/for_dsm_22659.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"autoclave_temperature\": null,\n      \"autoclave_duration\": null,\n\
    \      \"vitamins\": \"filter sterilized\"\n    },\n    \"rationale\": \"Source\
    \ method/order is explicit but no numeric autoclave cycle is given; missing layers\
    \ need the exact method, not a guessed time or temperature.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1004\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1004.pdf\",\n       \
    \ \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"autoclave. Add yeast extract, vitamins (sterilized by filtration), glucose,\
    \ sulfide, and\",\n        \"snapshot_sha256\": \"763e9486dd0519c45d89c9925f552e44be47a95eba02e994192125db1a73b29e\"\
    ,\n        \"parsed_text_sha256\": \"6b70121800cb301118e6adb55c8053bc45343985c22bff6c13e59ea12b444605\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '31 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 31/32
    primary and 29/32 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - chebi131361
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi17634
  - chebi176843
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi32139
  - chebi32145
  - chebi33118
  - chebi34887
  - chebi49105
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63939
  - chebi64758
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 32: primary 96.88%;
    secondary 90.62%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 53 timestamp instances inspected; 10 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
  - owner-2
  - owner-3
  - owner-4
- assessment_id: identity
  area: identity
  topic: Base source and five distinct maintained contributors
  outcome: concern
  summary: DSMZ1004 and KOMODO1004 identify the base; three KOMODO child accessions
    identify strain-specific branches. Current normalized topology correctly labels
    those children as variants, but their 32 ingredient quantities remain identical
    to the base. The older generated merge still collapses them as SOURCE_DUPLICATE
    and synonyms. Current primary clauses resolve the three formulation differences.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - primary
  - bound-owner-context
  - id-search
- assessment_id: evidence
  area: evidence
  topic: Claim-level amount support and history
  outcome: concern
  summary: All 192 local ingredient concentrations are covered by exact primary snippets
    and owner-specific decisions. Existing values have no attached quantity evidence.
    The ten base rates agree with the declared 1003 mL denominator to stored rounding;
    stock values and child overrides require separate scope. Historical reports are
    derivative only and current 503 responses do not verify their past graph assignments.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - primary
  - quantity-inventory
  - record
- assessment_id: forms
  area: grounding
  topic: Exact salts and stock ingredients
  outcome: concern
  summary: Source sodium resazurin differs from neutral CHEBI:8806, and source nickel
    hexahydrate differs from anhydrous CHEBI:34887. The source EDTA dihydrate matches
    CHEBI:64758; calcium D-(+)-pantothenate is compatible with CHEBI:31345. Generic
    lipoic acid CHEBI:16494 is not contradicted solely by the source DL label. Vitamin
    and mineral identities remain stock-scoped.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - primary
  - chebi8806
  - chebi34887
  - chebi64758
  - chebi31345
  - chebi16494
- assessment_id: preparation
  area: completeness
  topic: Main procedure, three stock preparations and variant clauses
  outcome: concern
  summary: Only the DSMZ owner retains main anaerobic preparation and SL-11 titration/make-up.
    Target and KOMODO layers omit this preparation; stock instructions need nested
    scope. The complete primary resolves stock quantities and current strain branches
    despite optional live-provider access limits. Its declared final volume and listed-liquid
    arithmetic discrepancy are retained explicitly.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - owner-1
  - primary
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Medium classification, catalog atmosphere and growth scope
  outcome: concern
  summary: 'COMPLEX/UNDEFINED and LIQUID fit the yeast-extract base. Imported Aerobic:
    Yes must remain catalog provenance and cannot override anoxic preparation. The
    three child ingredients_curated flags and repaired topology do not certify formula
    correctness. Strain-specific source recipe clauses are not experimental growth
    results or taxonomic ID assignments.'
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - primary
  - bound-owner-context
- assessment_id: current-writers
  area: provenance
  topic: Current writers and maintained input follow-up
  outcome: concern
  summary: The current KOMODO1004 repair hardcodes the same 32 ingredient signature
    and modifies relationships/history/flags, not formula quantities. Its September
    events are later than the generated August merge, so only this directly recorded
    local chronology is asserted. Current MediaDive parser separates stock additions
    but collects solution steps at root. Current lossless merging does not scientifically
    correct retained inputs; repair all five owner formulas/variant scopes before
    regeneration.
  target_ids:
  - CultureMech:003504
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
findings:
- finding_id: f1
  issue_key: culturemech.003504.stock-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Three stock recipes are flattened as direct main concentrations
  description: All six local layers place 22 SL-11, selenite-tungstate and Wolin10x
    constituents at stock-level quantities among main ingredients, without receiving-dose
    or water containers.
  target_ids:
  - CultureMech:003504
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  issue_key: culturemech.003504.erased-strain-formulas
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Three strain wrappers retain the base formula despite explicit overrides
  description: KOMODO1004.1 still contains base glucose and yeast instead of 7.2 g/L
    sucrose plus 0.1 g/L yeast;1004.2 retains glucose and base yeast instead of omission
    plus 0.1 g/L yeast;1004.3 retains base glucose instead of 5 g/L. The target additionally
    merges the distinct branches as duplicates/synonyms.
  target_ids:
  - CultureMech:003504
  field_paths:
  - variant_children
  - synonyms
  - parent_media
  - ingredients[6]
  - ingredients[7]
  evidence_ids:
  - primary
  - quantity-inventory
  - bound-owner-context
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.003504.supplied-form-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Dye salt and nickel hydrate are mapped to different forms
  description: Sodium resazurin is asserted as neutral CHEBI:8806 and nickel hexahydrate
    as Cl2Ni CHEBI:34887 in all layers. These are supplied-form conflicts, unlike
    the compatible calcium D-pantothenate and generic DL-lipoic mappings.
  target_ids:
  - CultureMech:003504
  field_paths:
  - ingredients[4].term
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  evidence_ids:
  - primary
  - chebi8806
  - chebi34887
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  issue_key: culturemech.003504.preparation-and-flag-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation is missing outside the DSMZ owner and stock instructions remain
    at root
  description: Target/KOMODO layers lose source anaerobic preparation and filtration
    qualifiers. The DSMZ owner retains SL-11 solvent/pH/make-up instructions at main
    root, and repaired child flags overstate unchanged formulation curation.
  target_ids:
  - CultureMech:003504
  field_paths:
  - preparation_steps
  - solutions
  - notes
  evidence_ids:
  - primary
  - owner-1
  - quantity-inventory
  - current-code-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.4
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: culturemech.003504.historical-timestamp-shape
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical KOMODO timestamps are malformed or timezone-naive
  description: The target and four KOMODO maintained records retain malformed import
    timestamps and naive enrichment timestamps; later repair history is preserved
    separately.
  target_ids:
  - CultureMech:003504
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  description: Restore the three stocks, exact stock preparation and 1 mL doses in
    all five maintained owners while keeping base amounts on the declared 1003 mL
    basis. Preserve the separately reported liquid-sum discrepancy and attach narrow
    evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  description: Correct each exact child owner using its own current primary strain
    clause, preserve source IDs and later topology repair history, and regenerate
    only after variant-aware formulation comparison. Keep source-only DSM23815/103421
    branches separate from these wrappers and the base.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  description: Verify source-compatible identifiers for the sodium dye and nickel
    hydrate in every owner, independently check secondary mappings and preserve exact
    source forms without inventing IDs.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  description: Retain main and variant procedures in the correct owners, nest stock
    instructions, qualify unsupported ingredients_curated flags and imported aerobic
    metadata, and preserve all source stage qualifiers. No numeric sterilization cycle
    is supplied.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
  description: Append an exact dated clarification when authorized instead of rewriting
    historical events; improve future timestamp writers separately.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003504
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerolinea_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16556.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_22659.yaml
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
- Exact mediadive1004api access returned 503. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact mediadive1004apiRetry access returned 503. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004detail access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004actual access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004_1detail access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004_1actual access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004_2detail access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004_2actual access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004_3detail access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact komodo1004_3actual access returned 403. This limits live/historical provider
  corroboration but does not make the complete current DSMZ1004 base and named strain
  clauses unavailable.
- Exact solution1474 access returned 503. This limits live/historical provider corroboration
  but does not make the complete current DSMZ1004 base and named strain clauses unavailable.
- Completed means the current source-scoped comparison is complete, not that the recipe
  is correct. Optional provider 403/503 failures are retained; no historical response
  or temporal priority between sources is fabricated.
- Source-declared 1003 mL, listed 1003.5 mL and unquantified late-stock volumes remain
  distinct. No strain clause is generalized into a growth claim.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-028
- generated-medium
```
