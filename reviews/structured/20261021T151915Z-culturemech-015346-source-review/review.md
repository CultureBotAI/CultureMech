# Source and formulation review: anaerobic_azospirillum_medium (CultureMech:015346)

- Review: 20261021T151915Z-culturemech-015346-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:15:03Z
- Finished UTC: 2026-10-21T15:19:15Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 1701 identity is supported, but both local layers flatten solutions A, C, D, E and SL-10 into one concentration list. Stock strengths and a 940 mL water-based normalization are not final-medium concentrations. Sodium-resazurin and nickel-hydrate grounding and the high_metal assertion need correction or qualification. Required receiving-dose/final-volume clarification remains unresolved.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 264; batch 027 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-six task batches contain 260 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 263 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015346 | data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml | generated | anaerobic_azospirillum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015346 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:015346 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/264/strict.tsv |
| validate-terms | passed | True | CultureMech:015346 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:015346 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:015346 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required source assembly/denominator clarification | unavailable | True | CultureMech:015346 | Required numerical C/D/E receiving doses and the assembled final-volume basis are not supplied by the inspected primary; both exact provider attempts returned 503. The source-defined stages and confirmed errors are reviewable, but reconstructing exact final concentrations remains unavailable. This partial scope does not imply the source masses are wrong. |
| Exact source content access: mediadive1701api | unavailable | False | CultureMech:015346 | Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation. Primary DSMZ 1701 is available; the response is not formulation or historical-absence evidence. |
| Exact source content access: mediadive1701apiRetry | unavailable | False | CultureMech:015346 | Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation. Primary DSMZ 1701 is available; the response is not formulation or historical-absence evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:015346.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:015346.

35 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "KH2PO4 in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.744681",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.744681",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 0.7,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "KH2PO4 0.70 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "NH4Cl in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.319149",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.319149",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 0.3,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "NH4Cl 0.30 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Na2SO4 in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.97872",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.97872",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 2.8,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "Na2SO4 2.80 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "MgCl2 x 6 H2O in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.80851",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1.80851",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 1.7,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "MgCl2 x 6 H2O 1.70 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "CaCl2 x 2 H2O in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0531915",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0531915",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 0.05,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "CaCl2 x 2 H2O 0.05 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "NaCl in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "10.6383",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "10.6383",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 10,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Yeast extract in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.531915",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.531915",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "Solution A",
      "source_amount_g": 0.5,
      "listed_water_ml": 940,
      "assembled_final_concentration": null
    },
    "rationale": "Stored g/L equals approximately the source mass divided by 0.940 L water; water alone is not the finished A volume or assembled medium denominator. Preserve the original batch mass and source stage, without claiming the unavailable provider response verifies its history.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A table",
        "exact_source_quote": "Yeast extrakt 0.5 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Sodium resazurin in A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.0005",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "A",
      "stock_dose_ml": 0.5,
      "stock_strength": "0.1% w/v",
      "batch_mass_g": 0.0005,
      "final_g_per_l": null
    },
    "rationale": "The numeric stored 0.0005 equals the batch mass from 0.5 mL of 0.1% w/v stock, but the final g/L denominator is unestablished. Preserve sodium-salt identity and the explicit w/v basis.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A",
        "exact_source_quote": "Na-resazurin solution (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Solution C solute",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "162",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "162",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "C",
      "source_mass_g": 1.62,
      "listed_water_ml": 10,
      "receiving_dose": null,
      "assembled_final_concentration": null
    },
    "rationale": "Stored 162 g/L reflects stock mass divided by listed stock water, then appears among main ingredients. Retain stock mass and water separately; do not assume the entire stock batch is added. The primary does not resolve the receiving amount.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution C",
        "exact_source_quote": "Na-succinat 1.62  g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Solution D solute",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "D",
      "source_mass_g": 1,
      "listed_water_ml": 20,
      "receiving_dose": null,
      "assembled_final_concentration": null
    },
    "rationale": "Stored 50 g/L reflects stock mass divided by listed stock water, then appears among main ingredients. Retain stock mass and water separately; do not assume the entire stock batch is added. The primary does not resolve the receiving amount.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution D",
        "exact_source_quote": "Na2CO3 1.00 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Solution E solute",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "E",
      "source_mass_g": 0.3,
      "listed_water_ml": 10,
      "receiving_dose": null,
      "assembled_final_concentration": null
    },
    "rationale": "Stored 30 g/L reflects stock mass divided by listed stock water, then appears among main ingredients. Retain stock mass and water separately; do not assume the entire stock batch is added. The primary does not resolve the receiving amount.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution E",
        "exact_source_quote": "Na2S x 9 H2O 0.30 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "SL-10: HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 10,
      "source_unit": "ml",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": "25%; 7.7 M"
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The 25% basis is unspecified; 7.7 M is explicit. Do not convert the 10 mL acid dose into the stored 2.5 g/L using an invented mass/volume percentage.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "HCl (25%; 7.7 M) 10.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "SL-10: FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 1.5,
      "source_unit": "g",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "SL-10: ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 70,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "SL-10: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 100,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "SL-10: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 6,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "SL-10: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 190,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "SL-10: CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 2,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "SL-10: NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 24,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "SL-10: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "source_amount": 36,
      "source_unit": "mg",
      "stock_final_makeup_ml": 1000,
      "A_receiving_dose_ml": 1,
      "acid_strength": null
    },
    "rationale": "SL-10 composition is not a direct main-medium concentration. Restore its 1 mL receiving addition and explicit 1000 mL stock make-up. The listed hydrate and original stock mass remain distinct from any later diluted quantity.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Trace element solution SL-10",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "A listed water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "A",
      "water_ml": 940
    },
    "rationale": "Restore stage-specific solvent volume; it is not a g/L ingredient and does not independently establish assembled final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, A water row",
        "exact_source_quote": "Distilled water 940.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "C listed water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "C",
      "water_ml": 10
    },
    "rationale": "Restore stage-specific solvent volume; it is not a g/L ingredient and does not independently establish assembled final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, C water row",
        "exact_source_quote": "Distilled water 10.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "D listed water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "D",
      "water_ml": 20
    },
    "rationale": "Restore stage-specific solvent volume; it is not a g/L ingredient and does not independently establish assembled final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, D water row",
        "exact_source_quote": "Distilled water 20.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "E listed water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "E",
      "water_ml": 10
    },
    "rationale": "Restore stage-specific solvent volume; it is not a g/L ingredient and does not independently establish assembled final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, E water row",
        "exact_source_quote": "Distilled water 10.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "SL-10 listed water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "water_ml": 990
    },
    "rationale": "Restore stage-specific solvent volume; it is not a g/L ingredient and does not independently establish assembled final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, SL-10 water row",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "SL-10 receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "A",
      "stock": "SL-10",
      "dose_ml": 1
    },
    "rationale": "This explicit receiving stock amount is absent as a structured solution addition in both layers.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Sodium-resazurin receiving stock",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "A",
      "dose_ml": 0.5,
      "strength": "0.1% w/v"
    },
    "rationale": "Retain the stock addition and supplied sodium identity instead of only an unsupported final g/L scalar.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1, Solution A",
        "exact_source_quote": "Na-resazurin solution (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "A gas and acidification",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "A",
      "N2_percent": 80,
      "CO2_percent": 20,
      "pH_condition": "below 6"
    },
    "rationale": "Existing source-derived preparation context is retained with exact stage and qualifier. Gas percentage basis is not independently expanded to v/v, and no sterilization temperature or duration is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 main preparation",
        "exact_source_quote": "Solution A is sparged with 80% N 2 and 20% CO2 gas mixture to reach a pH below  6 (at",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "A sparging duration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "A",
      "minimum_minutes": 30
    },
    "rationale": "Existing source-derived preparation context is retained with exact stage and qualifier. Gas percentage basis is not independently expanded to v/v, and no sterilization temperature or duration is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 main preparation",
        "exact_source_quote": "least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "C/E gas",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": [
        "C",
        "E"
      ],
      "N2_percent": 100
    },
    "rationale": "Existing source-derived preparation context is retained with exact stage and qualifier. Gas percentage basis is not independently expanded to v/v, and no sterilization temperature or duration is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 main preparation",
        "exact_source_quote": "100% N 2 gas atmosphere. Solution D is autoclaved under 80% N 2 and 20% CO 2 gas",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "D gas",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "D",
      "N2_percent": 80,
      "CO2_percent": 20
    },
    "rationale": "Existing source-derived preparation context is retained with exact stage and qualifier. Gas percentage basis is not independently expanded to v/v, and no sterilization temperature or duration is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 main preparation",
        "exact_source_quote": "100% N 2 gas atmosphere. Solution D is autoclaved under 80% N 2 and 20% CO 2 gas",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Final main pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.2,
          "max": 7.4
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 7.2,
          "max": 7.4
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "assembled medium",
      "pH_range": [
        7.2,
        7.4
      ]
    },
    "rationale": "Existing source-derived preparation context is retained with exact stage and qualifier. Gas percentage basis is not independently expanded to v/v, and no sterilization temperature or duration is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 main preparation",
        "exact_source_quote": "Final pH of the medium should be 7.2 –",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      },
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 following line",
        "exact_source_quote": "7.4.",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "SL-10 final make-up",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.0 ml.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.0 ml.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "final_makeup_ml": 1000
    },
    "rationale": "Existing source-derived preparation context is retained with exact stage and qualifier. Move the existing SL-10 make-up instruction from main-root preparation into the restored stock; do not interpret it as main final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 1 SL-10 preparation",
        "exact_source_quote": "Finally make up to 1000.0 ml.",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "C/D/E receiving amounts",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "receiving_amount_C": null,
      "receiving_amount_D": null,
      "receiving_amount_E": null,
      "assembled_final_volume": null
    },
    "rationale": "The primary leaves these receiving amounts unquantified. Preserve this limitation instead of assuming whole stock batches or a one-liter endpoint.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 assembly paragraph",
        "exact_source_quote": "appropriate amounts of solutions C to E",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80% N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of solutions C to E are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 - 7.4.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "temperature": null,
      "duration": null
    },
    "rationale": "Autoclaving and the separate gas stages are stated; a numeric cycle is not supplied and must not be invented.",
    "source_snippets": [
      {
        "source_key": "dsmz1701",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf",
        "source_locator": "Page 2 preparation",
        "exact_source_quote": "tubes or serum vials and autoclaved.",
        "snapshot_sha256": "1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3",
        "parsed_text_sha256": "127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:015346.

19 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 19/20 primary and 18/20 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 20: primary 95.00%; secondary 90.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact collection identity and sole maintained owner

identity: supported. Targets: CultureMech:015346.

Stable CultureMech:015346, DSMZ/MediaDive 1701 and the complete primary title agree. The specialized normalized owner has the same scientific fields; the target adds one merge event and bookkeeping. No unrelated Azospirillum medium is substituted.

### Claim-level source support

evidence: concern. Targets: CultureMech:015346.

Neither local layer attaches ingredient quantity evidence. Every local concentration is inventoried against literal primary text; source-stage facts remain separate from arithmetic. The unavailable API cannot corroborate its historical normalization.

### Separate stocks and preserved main preparation

completeness: concern. Targets: CultureMech:015346.

Both layers retain the main gas, below-pH-6 stage, minimum 30-minute interval, separate C/E and D handling and final pH 7.2–7.4. SL-10 iron-first dissolution and final 1000 mL make-up are incorrectly stored at the main root. Solutions, water and receiving amounts must be scoped; absent numerical C–E doses remain unresolved.

### Sodium salt, hydrate and unspecified succinate hydration

grounding: concern. Targets: CultureMech:015346.

Primary Na-resazurin is a sodium salt, while CHEBI:8806 is neutral C12H7NO4. Primary nickel hexahydrate conflicts with CHEBI:34887 Cl2Ni. CHEBI:63675 specifies anhydrous disodium succinate, while Na-succinat is not hydrate-qualified; that is unverified specificity, not evidence for a different replacement. Other asserted salt hydrates are source-compatible; yeast extract remains an ungrounded mixture.

### Composition, physical state and high-metal flag

scope: concern. Targets: CultureMech:015346.

COMPLEX/UNDEFINED is compatible with yeast extract and LIQUID with no solidifier. Both layers assert high_metal true. The schema defines a total-metal threshold, but the flattened stocks and unresolved assembly denominator do not establish that threshold for this medium. No low-metal or false replacement is inferred.

### Biological and graph claim boundaries

scope: not_applicable. Targets: CultureMech:015346.

Title, specialized filing and generic Microbial cultivation are catalog metadata, not experimental growth support. Neither layer asserts an organism CURIE, growth condition object, internal variant graph or graph match requiring biological extrapolation. No phenotype or new growth assertion is introduced.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:015346.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current writers and maintained input follow-up

provenance: concern. Targets: CultureMech:015346.

Current MediaDive composition parsing restricts direct ingredients to the first solution and records receiving stock references separately, but preparation parsing gathers all solution steps at the main root. Current lossless merging preserves scientific differences and does not repair chemistry. The metal analyzer scans direct ingredients, approximates mass units without molecular-weight/stoichiometric conversion and uses a distribution threshold; the label writer copies its classifications by basename. Neither implementation proves this record’s historical writer version or a source-grounded final metal total. The two metal scripts are included in the supplementary native inspection input manifest; their current bytes are also separately hash-pinned in the code evidence.

## Findings

### f1: Four solution stages and SL-10 are flattened into false final concentrations

blocker / open / confirmed; issue key: culturemech.015346.stock-stage-collapse.

Both layers place A water-normalized salts, C succinate 162 g/L, D carbonate 50 g/L, E sulfide 30 g/L and SL-10 stock concentrations in one direct ingredient list. The primary supplies stage-specific masses/water and only appropriate receiving amounts for C–E. HCl 2.5 g/L also assumes an unstated percentage basis. This flat formula does not denote a supported assembled medium.

### f2: Sodium salt and nickel hydrate are mapped to different supplied forms

major / open / confirmed; issue key: culturemech.015346.supplied-form-grounding.

ingredients[7].term identifies neutral resazurin despite source sodium resazurin; ingredients[18].term and its current secondary slot identify Cl2Ni despite source nickel hexahydrate. Valid canonical labels do not resolve these mismatches. Succinate’s anhydrous specificity remains unverified separately.

### f3: SL-10 make-up is detached from its stock

major / open / confirmed; issue key: culturemech.015346.stock-preparation-scope.

preparation_steps[1] retains iron-first acid dissolution and make-up to 1000 mL at the main root. The primary assigns this instruction to SL-10; the assembled medium has no explicit final-volume statement.

### f4: High-metal flag lacks a valid final-medium basis

major / open / confirmed; issue key: culturemech.015346.unsupported-high-metal.

high_metal true is asserted in both layers, while the available formulation has flattened stock concentrations and no quantified C–E receiving doses/final denominator. Neither the source nor the current heuristic writers provides a valid metal-total calculation for this assembled medium.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the maintained specialized owner with separate A/C/D/E and SL-10 stages, literal masses, water and explicit A stock doses. Preserve unquantified receiving amounts/final-volume uncertainty; do not normalize stock recipes as final medium. Attach narrow evidence before authorized regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Verify and correct source-compatible sodium-salt and nickel-hydrate identities in the maintained owner, assessing primary and secondary links independently. Qualify unverified succinate hydration without inventing a replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Move the intact SL-10 preparation into its stock container while retaining the already-supported main preparation and all stage-specific gas/pH qualifiers. Do not substitute 1000 mL as the assembled final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Qualify or withdraw the unsupported flag in the maintained owner pending stage-correct, molecular-form-aware total-metal calculation against the schema criterion. Do not replace it with false or infer a biological phenotype.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch027/264/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch027/264/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml:1:id: CultureMech:015346<br>./data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml:1:id: CultureMech:015346<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/264/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 22 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch027/source-preflight-bound/264/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf; Pages 1–2, complete A/C/D/E and SL-10 tables and separate preparation paragraphs | supports | The primary separates four named solutions and SL-10. It supplies appropriate amounts of C–E without numerical receiving doses or an explicit assembled final volume. A has 940 mL water, 1 mL SL-10 and 0.5 mL resazurin stock. No solution B is printed or inferred. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch027/264/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32149 resolves to sodium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63675 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63675 resolves to sodium succinate (anhydrous). Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term", "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63675": [{"label": "Sodium succinate", "match_type": "preferred_term", "identifier": "CHEBI:63675", "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml; data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml", "events": 7, "timestamp_issues": []}] |
| current-code-0 | src/culturemech/import/mediadive_importer.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive composition parsing restricts direct ingredients to the first solution and records receiving stock references separately, but preparation parsing gathers all solution steps at the main root. Current lossless merging preserves scientific differences and does not repair chemistry. The metal analyzer scans direct ingredients, approximates mass units without molecular-weight/stoichiometric conversion and uses a distribution threshold; the label writer copies its classifications by basename. Neither implementation proves this record’s historical writer version or a source-grounded final metal total. The two metal scripts are included in the supplementary native inspection input manifest; their current bytes are also separately hash-pinned in the code evidence. |
| current-code-1 | src/culturemech/merge/formulation.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive composition parsing restricts direct ingredients to the first solution and records receiving stock references separately, but preparation parsing gathers all solution steps at the main root. Current lossless merging preserves scientific differences and does not repair chemistry. The metal analyzer scans direct ingredients, approximates mass units without molecular-weight/stoichiometric conversion and uses a distribution threshold; the label writer copies its classifications by basename. Neither implementation proves this record’s historical writer version or a source-grounded final metal total. The two metal scripts are included in the supplementary native inspection input manifest; their current bytes are also separately hash-pinned in the code evidence. |
| current-code-2 | scripts/analyze_metal_concentrations.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive composition parsing restricts direct ingredients to the first solution and records receiving stock references separately, but preparation parsing gathers all solution steps at the main root. Current lossless merging preserves scientific differences and does not repair chemistry. The metal analyzer scans direct ingredients, approximates mass units without molecular-weight/stoichiometric conversion and uses a distribution threshold; the label writer copies its classifications by basename. Neither implementation proves this record’s historical writer version or a source-grounded final metal total. The two metal scripts are included in the supplementary native inspection input manifest; their current bytes are also separately hash-pinned in the code evidence. |
| current-code-3 | scripts/add_metal_ree_labels.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive composition parsing restricts direct ingredients to the first solution and records receiving stock references separately, but preparation parsing gathers all solution steps at the main root. Current lossless merging preserves scientific differences and does not repair chemistry. The metal analyzer scans direct ingredients, approximates mass units without molecular-weight/stoichiometric conversion and uses a distribution threshold; the label writer copies its classifications by basename. Neither implementation proves this record’s historical writer version or a source-grounded final metal total. The two metal scripts are included in the supplementary native inspection input manifest; their current bytes are also separately hash-pinned in the code evidence. |
| mediadive1701api-attempt | https://mediadive.dsmz.de/rest/medium/1701; Preserved exact public retrieval result | context_only | Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation. Primary DSMZ 1701 is available; the response is not formulation or historical-absence evidence. |
| mediadive1701apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/1701; Preserved exact public retrieval result | context_only | Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation. Primary DSMZ 1701 is available; the response is not formulation or historical-absence evidence. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Required numerical C/D/E receiving doses and the assembled final-volume basis are not supplied by the inspected primary; both exact provider attempts returned 503. The source-defined stages and confirmed errors are reviewable, but reconstructing exact final concentrations remains unavailable. This partial scope does not imply the source masses are wrong.
- Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation. Primary DSMZ 1701 is available; the response is not formulation or historical-absence evidence.
- Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation. Primary DSMZ 1701 is available; the response is not formulation or historical-absence evidence.
- The complete primary is available, but missing assembly doses are genuine source limits. No missing solution B, whole-stock transfer, percentage basis or sterilization cycle is invented.
- Current provider unavailability prevents a live provider-normalization comparison; it does not establish source chronology or invalidate the primary.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T151915Z-culturemech-015346-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerobic_azospirillum_medium (CultureMech:015346)'
started_at: '2026-10-21T15:15:03Z'
finished_at: '2026-10-21T15:19:15Z'
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
summary: DSMZ 1701 identity is supported, but both local layers flatten solutions
  A, C, D, E and SL-10 into one concentration list. Stock strengths and a 940 mL water-based
  normalization are not final-medium concentrations. Sodium-resazurin and nickel-hydrate
  grounding and the high_metal assertion need correction or qualification. Required
  receiving-dose/final-volume clarification remains unresolved.
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
  - path: data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
    sha256: 257833d187628357681c72a47b2d1f6213eb1a0ced85b3390f474c7c9f2a02ff
    role: target
  - path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
    sha256: 05ff387a0dd0df0eb4af4356ae1a53595e19208b146a7eaf48394621cfbbb7e6
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
  selection: Task review 264; batch 027 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-six task batches
    contain 260 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 263 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015346
targets:
- target_id: CultureMech:015346
  path: data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  label: anaerobic_azospirillum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/264/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/264/strict.tsv"
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:015346
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
  - CultureMech:015346
- check_id: source-assembly-basis
  name: Required source assembly/denominator clarification
  required: true
  status: unavailable
  summary: Required numerical C/D/E receiving doses and the assembled final-volume
    basis are not supplied by the inspected primary; both exact provider attempts
    returned 503. The source-defined stages and confirmed errors are reviewable, but
    reconstructing exact final concentrations remains unavailable. This partial scope
    does not imply the source masses are wrong.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - primary
  - quantity-inventory
- check_id: mediadive1701api-source-access
  name: 'Exact source content access: mediadive1701api'
  required: false
  status: unavailable
  summary: Exact MediaDive 1701 request returned HTTP 503; retained as provider-access
    limitation. Primary DSMZ 1701 is available; the response is not formulation or
    historical-absence evidence.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - mediadive1701api-attempt
- check_id: mediadive1701apiRetry-source-access
  name: 'Exact source content access: mediadive1701apiRetry'
  required: false
  status: unavailable
  summary: Exact MediaDive 1701 request returned HTTP 503; retained as provider-access
    limitation. Primary DSMZ 1701 is available; the response is not formulation or
    historical-absence evidence.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - mediadive1701apiRetry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:26.412617Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch027/264/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:27.419887Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-027/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch027/264/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:28.560135Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:15:29.332249Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:19:14Z'
  support: supports
  summary: './data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml:1:id:
    CultureMech:015346

    ./data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml:1:id: CultureMech:015346

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/264/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:19:14Z'
  support: supports
  summary: 22 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 1fdfbaad500fd02ef253520daf807134ae12dfe76c832291d10dd5bb3d23af3d
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/source-preflight-bound/264/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: 28a95e5f6eb335e73d93516bf03790459d980852e5a26ceee7d0f42bea32bfb6
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf
  locator: Pages 1–2, complete A/C/D/E and SL-10 tables and separate preparation paragraphs
  accessed_at: '2026-10-21T15:02:34.260361Z'
  support: supports
  summary: The primary separates four named solutions and SL-10. It supplies appropriate
    amounts of C–E without numerical receiving doses or an explicit assembled final
    volume. A has 940 mL water, 1 mL SL-10 and 0.5 mL resazurin stock. No solution
    B is printed or inferred.
  snapshot_sha256: 1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch027/264/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 60d539bf72deac01cd24042324dd04a630cb8c48caf9326010822183f6e4e02d
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
- evidence_id: chebi32149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:18:34.792120Z'
  support: supports
  summary: CHEBI:32149 resolves to sodium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
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
- evidence_id: chebi63675
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63675
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:27:41.075057Z'
  support: supports
  summary: CHEBI:63675 resolves to sodium succinate (anhydrous). Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 4c54df9f2d63f54dea26d64e4ec9fedeb486c2c2abe44b70c5c621512f1fdd3c
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:19:14Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:17883":
    [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883",
    "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label":
    "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32149": [{"label": "Na2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:32149", "preferred_term": "Na2SO4", "ontology_id": "CHEBI:32149",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label":
    "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term":
    "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label":
    "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term":
    "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type":
    "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride
    hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63675": [{"label":
    "Sodium succinate", "match_type": "preferred_term", "identifier": "CHEBI:63675",
    "preferred_term": "Sodium succinate", "ontology_id": "CHEBI:63675", "mapping_status":
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
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml; data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Current MediaDive composition parsing restricts direct ingredients to the
    first solution and records receiving stock references separately, but preparation
    parsing gathers all solution steps at the main root. Current lossless merging
    preserves scientific differences and does not repair chemistry. The metal analyzer
    scans direct ingredients, approximates mass units without molecular-weight/stoichiometric
    conversion and uses a distribution threshold; the label writer copies its classifications
    by basename. Neither implementation proves this record’s historical writer version
    or a source-grounded final metal total. The two metal scripts are included in
    the supplementary native inspection input manifest; their current bytes are also
    separately hash-pinned in the code evidence.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-1
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Current MediaDive composition parsing restricts direct ingredients to the
    first solution and records receiving stock references separately, but preparation
    parsing gathers all solution steps at the main root. Current lossless merging
    preserves scientific differences and does not repair chemistry. The metal analyzer
    scans direct ingredients, approximates mass units without molecular-weight/stoichiometric
    conversion and uses a distribution threshold; the label writer copies its classifications
    by basename. Neither implementation proves this record’s historical writer version
    or a source-grounded final metal total. The two metal scripts are included in
    the supplementary native inspection input manifest; their current bytes are also
    separately hash-pinned in the code evidence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: current-code-2
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Current MediaDive composition parsing restricts direct ingredients to the
    first solution and records receiving stock references separately, but preparation
    parsing gathers all solution steps at the main root. Current lossless merging
    preserves scientific differences and does not repair chemistry. The metal analyzer
    scans direct ingredients, approximates mass units without molecular-weight/stoichiometric
    conversion and uses a distribution threshold; the label writer copies its classifications
    by basename. Neither implementation proves this record’s historical writer version
    or a source-grounded final metal total. The two metal scripts are included in
    the supplementary native inspection input manifest; their current bytes are also
    separately hash-pinned in the code evidence.
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: current-code-3
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:19:14Z'
  support: context_only
  summary: Current MediaDive composition parsing restricts direct ingredients to the
    first solution and records receiving stock references separately, but preparation
    parsing gathers all solution steps at the main root. Current lossless merging
    preserves scientific differences and does not repair chemistry. The metal analyzer
    scans direct ingredients, approximates mass units without molecular-weight/stoichiometric
    conversion and uses a distribution threshold; the label writer copies its classifications
    by basename. Neither implementation proves this record’s historical writer version
    or a source-grounded final metal total. The two metal scripts are included in
    the supplementary native inspection input manifest; their current bytes are also
    separately hash-pinned in the code evidence.
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
- evidence_id: mediadive1701api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1701
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:02:33.449332Z'
  support: context_only
  summary: Exact MediaDive 1701 request returned HTTP 503; retained as provider-access
    limitation. Primary DSMZ 1701 is available; the response is not formulation or
    historical-absence evidence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive1701apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1701
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:03:39.702271Z'
  support: context_only
  summary: Exact MediaDive 1701 request returned HTTP 503; retained as provider-access
    limitation. Primary DSMZ 1701 is available; the response is not formulation or
    historical-absence evidence.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 35 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    KH2PO4 in A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.744681\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.744681\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 0.7,\n     \
    \ \"listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n \
    \   },\n    \"rationale\": \"Stored g/L equals approximately the source mass divided\
    \ by 0.940 L water; water alone is not the finished A volume or assembled medium\
    \ denominator. Preserve the original batch mass and source stage, without claiming\
    \ the unavailable provider response verifies its history.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.70 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"NH4Cl in A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.319149\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.319149\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 0.3,\n     \
    \ \"listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n \
    \   },\n    \"rationale\": \"Stored g/L equals approximately the source mass divided\
    \ by 0.940 L water; water alone is not the finished A volume or assembled medium\
    \ denominator. Preserve the original batch mass and source stage, without claiming\
    \ the unavailable provider response verifies its history.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.30 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Na2SO4 in A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.97872\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.97872\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 2.8,\n     \
    \ \"listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n \
    \   },\n    \"rationale\": \"Stored g/L equals approximately the source mass divided\
    \ by 0.940 L water; water alone is not the finished A volume or assembled medium\
    \ denominator. Preserve the original batch mass and source stage, without claiming\
    \ the unavailable provider response verifies its history.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"Na2SO4 2.80 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"MgCl2 x 6 H2O in A\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.80851\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.80851\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 1.7,\n     \
    \ \"listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n \
    \   },\n    \"rationale\": \"Stored g/L equals approximately the source mass divided\
    \ by 0.940 L water; water alone is not the finished A volume or assembled medium\
    \ denominator. Preserve the original batch mass and source stage, without claiming\
    \ the unavailable provider response verifies its history.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 1.70 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O in A\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0531915\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0531915\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 0.05,\n    \
    \  \"listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n\
    \    },\n    \"rationale\": \"Stored g/L equals approximately the source mass\
    \ divided by 0.940 L water; water alone is not the finished A volume or assembled\
    \ medium denominator. Preserve the original batch mass and source stage, without\
    \ claiming the unavailable provider response verifies its history.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1701\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.05 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"NaCl in A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.6383\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.6383\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 10,\n      \"\
    listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n    },\n\
    \    \"rationale\": \"Stored g/L equals approximately the source mass divided\
    \ by 0.940 L water; water alone is not the finished A volume or assembled medium\
    \ denominator. Preserve the original batch mass and source stage, without claiming\
    \ the unavailable provider response verifies its history.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"NaCl 10.00 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Yeast extract in A\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.531915\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.531915\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Solution A\",\n      \"source_amount_g\": 0.5,\n     \
    \ \"listed_water_ml\": 940,\n      \"assembled_final_concentration\": null\n \
    \   },\n    \"rationale\": \"Stored g/L equals approximately the source mass divided\
    \ by 0.940 L water; water alone is not the finished A volume or assembled medium\
    \ denominator. Preserve the original batch mass and source stage, without claiming\
    \ the unavailable provider response verifies its history.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A table\",\n        \"exact_source_quote\"\
    : \"Yeast extrakt 0.5 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Sodium resazurin in A\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0005\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"A\",\n      \"stock_dose_ml\": 0.5,\n      \"stock_strength\"\
    : \"0.1% w/v\",\n      \"batch_mass_g\": 0.0005,\n      \"final_g_per_l\": null\n\
    \    },\n    \"rationale\": \"The numeric stored 0.0005 equals the batch mass\
    \ from 0.5 mL of 0.1% w/v stock, but the final g/L denominator is unestablished.\
    \ Preserve sodium-salt identity and the explicit w/v basis.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A\",\n        \"exact_source_quote\"\
    : \"Na-resazurin solution (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\":\
    \ \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\",\n    \
    \    \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Solution C solute\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"162\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"162\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"C\",\n      \"source_mass_g\": 1.62,\n      \"listed_water_ml\"\
    : 10,\n      \"receiving_dose\": null,\n      \"assembled_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Stored 162 g/L reflects stock mass divided\
    \ by listed stock water, then appears among main ingredients. Retain stock mass\
    \ and water separately; do not assume the entire stock batch is added. The primary\
    \ does not resolve the receiving amount.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution C\",\n        \"exact_source_quote\"\
    : \"Na-succinat 1.62  g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Solution D solute\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"D\",\n      \"source_mass_g\": 1,\n      \"listed_water_ml\"\
    : 20,\n      \"receiving_dose\": null,\n      \"assembled_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Stored 50 g/L reflects stock mass divided\
    \ by listed stock water, then appears among main ingredients. Retain stock mass\
    \ and water separately; do not assume the entire stock batch is added. The primary\
    \ does not resolve the receiving amount.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution D\",\n        \"exact_source_quote\"\
    : \"Na2CO3 1.00 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"Solution E solute\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"E\",\n      \"source_mass_g\": 0.3,\n      \"listed_water_ml\"\
    : 10,\n      \"receiving_dose\": null,\n      \"assembled_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Stored 30 g/L reflects stock mass divided\
    \ by listed stock water, then appears among main ingredients. Retain stock mass\
    \ and water separately; do not assume the entire stock batch is added. The primary\
    \ does not resolve the receiving amount.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution E\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.30 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"SL-10: HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 10,\n      \"source_unit\"\
    : \"ml\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": \"25%; 7.7 M\"\n    },\n    \"rationale\": \"SL-10\
    \ composition is not a direct main-medium concentration. Restore its 1 mL receiving\
    \ addition and explicit 1000 mL stock make-up. The 25% basis is unspecified; 7.7\
    \ M is explicit. Do not convert the 10 mL acid dose into the stored 2.5 g/L using\
    \ an invented mass/volume percentage.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Trace element solution SL-10\",\n   \
    \     \"exact_source_quote\": \"HCl (25%; 7.7 M) 10.00 ml\",\n        \"snapshot_sha256\"\
    : \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\",\n    \
    \    \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"SL-10: FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 1.5,\n      \"source_unit\"\
    : \"g\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"SL-10: ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 70,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"SL-10: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 100,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"SL-10: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 6,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"SL-10: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 190,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"SL-10: CuCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 2,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"SL-10: NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 24,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"SL-10: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"source_amount\": 36,\n      \"source_unit\"\
    : \"mg\",\n      \"stock_final_makeup_ml\": 1000,\n      \"A_receiving_dose_ml\"\
    : 1,\n      \"acid_strength\": null\n    },\n    \"rationale\": \"SL-10 composition\
    \ is not a direct main-medium concentration. Restore its 1 mL receiving addition\
    \ and explicit 1000 mL stock make-up. The listed hydrate and original stock mass\
    \ remain distinct from any later diluted quantity.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Trace element solution SL-10\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"A listed water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"A\",\n      \"water_ml\": 940\n    },\n    \"rationale\"\
    : \"Restore stage-specific solvent volume; it is not a g/L ingredient and does\
    \ not independently establish assembled final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, A water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 940.00 ml\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"C listed water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"C\",\n      \"water_ml\": 10\n    },\n    \"rationale\"\
    : \"Restore stage-specific solvent volume; it is not a g/L ingredient and does\
    \ not independently establish assembled final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, C water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 10.00 ml\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"D listed water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"D\",\n      \"water_ml\": 20\n    },\n    \"rationale\"\
    : \"Restore stage-specific solvent volume; it is not a g/L ingredient and does\
    \ not independently establish assembled final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, D water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 20.00 ml\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"E listed water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"E\",\n      \"water_ml\": 10\n    },\n    \"rationale\"\
    : \"Restore stage-specific solvent volume; it is not a g/L ingredient and does\
    \ not independently establish assembled final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, E water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 10.00 ml\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"SL-10 listed water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"water_ml\": 990\n    },\n    \"rationale\"\
    : \"Restore stage-specific solvent volume; it is not a g/L ingredient and does\
    \ not independently establish assembled final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, SL-10 water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"SL-10 receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"A\",\n      \"stock\": \"SL-10\",\n      \"dose_ml\":\
    \ 1\n    },\n    \"rationale\": \"This explicit receiving stock amount is absent\
    \ as a structured solution addition in both layers.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1, Solution A\",\n        \"exact_source_quote\"\
    : \"Trace element solution SL-10 1.00 ml\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Sodium-resazurin receiving stock\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"A\",\n      \"dose_ml\": 0.5,\n      \"strength\": \"\
    0.1% w/v\"\n    },\n    \"rationale\": \"Retain the stock addition and supplied\
    \ sodium identity instead of only an unsupported final g/L scalar.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1701\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 1, Solution A\",\n        \"exact_source_quote\"\
    : \"Na-resazurin solution (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\":\
    \ \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\",\n    \
    \    \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"A gas and acidification\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"A\",\n      \"N2_percent\": 80,\n      \"CO2_percent\": 20,\n      \"pH_condition\"\
    : \"below 6\"\n    },\n    \"rationale\": \"Existing source-derived preparation\
    \ context is retained with exact stage and qualifier. Gas percentage basis is\
    \ not independently expanded to v/v, and no sterilization temperature or duration\
    \ is supplied.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 2 main preparation\",\n        \"exact_source_quote\"\
    : \"Solution A is sparged with 80% N 2 and 20% CO2 gas mixture to reach a pH below\
    \  6 (at\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"A sparging duration\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"A\",\n      \"minimum_minutes\": 30\n    },\n    \"rationale\": \"Existing\
    \ source-derived preparation context is retained with exact stage and qualifier.\
    \ Gas percentage basis is not independently expanded to v/v, and no sterilization\
    \ temperature or duration is supplied.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 2 main preparation\",\n        \"exact_source_quote\"\
    : \"least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"C/E gas\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : [\n        \"C\",\n        \"E\"\n      ],\n      \"N2_percent\": 100\n    },\n\
    \    \"rationale\": \"Existing source-derived preparation context is retained\
    \ with exact stage and qualifier. Gas percentage basis is not independently expanded\
    \ to v/v, and no sterilization temperature or duration is supplied.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz1701\",\n       \
    \ \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 2 main preparation\",\n        \"exact_source_quote\"\
    : \"100% N 2 gas atmosphere. Solution D is autoclaved under 80% N 2 and 20% CO\
    \ 2 gas\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"D gas\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"D\",\n      \"N2_percent\": 80,\n      \"CO2_percent\": 20\n    },\n    \"\
    rationale\": \"Existing source-derived preparation context is retained with exact\
    \ stage and qualifier. Gas percentage basis is not independently expanded to v/v,\
    \ and no sterilization temperature or duration is supplied.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 2 main preparation\",\n        \"exact_source_quote\"\
    : \"100% N 2 gas atmosphere. Solution D is autoclaved under 80% N 2 and 20% CO\
    \ 2 gas\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Final main pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.2,\n          \"max\": 7.4\n        },\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 7.2,\n          \"max\": 7.4\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"assembled medium\",\n      \"pH_range\": [\n        7.2,\n        7.4\n  \
    \    ]\n    },\n    \"rationale\": \"Existing source-derived preparation context\
    \ is retained with exact stage and qualifier. Gas percentage basis is not independently\
    \ expanded to v/v, and no sterilization temperature or duration is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz1701\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 2 main preparation\",\n        \"exact_source_quote\"\
    : \"Final pH of the medium should be 7.2 –\",\n        \"snapshot_sha256\": \"\
    1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\",\n        \"\
    parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      },\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\"\
    : \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n   \
    \     \"source_locator\": \"Page 2 following line\",\n        \"exact_source_quote\"\
    : \"7.4.\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"SL-10 final make-up\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.0 ml.\",\n        \"decision\": \"correct\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the\
    \ other salts. Finally make up to 1000.0 ml.\",\n        \"decision\": \"correct\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"SL-10\",\n      \"final_makeup_ml\": 1000\n    },\n    \"rationale\": \"Existing\
    \ source-derived preparation context is retained with exact stage and qualifier.\
    \ Move the existing SL-10 make-up instruction from main-root preparation into\
    \ the restored stock; do not interpret it as main final volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 1 SL-10 preparation\",\n        \"exact_source_quote\"\
    : \"Finally make up to 1000.0 ml.\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"C/D/E receiving amounts\",\n    \"decision\": \"not_quantified\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"receiving_amount_C\"\
    : null,\n      \"receiving_amount_D\": null,\n      \"receiving_amount_E\": null,\n\
    \      \"assembled_final_volume\": null\n    },\n    \"rationale\": \"The primary\
    \ leaves these receiving amounts unquantified. Preserve this limitation instead\
    \ of assuming whole stock batches or a one-liter endpoint.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz1701\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\",\n       \
    \ \"source_locator\": \"Page 2 assembly paragraph\",\n        \"exact_source_quote\"\
    : \"appropriate amounts of solutions C to E\",\n        \"snapshot_sha256\": \"\
    1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\",\n        \"\
    parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"Autoclave cycle\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below\
    \ 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic\
    \ Hungate-type tubes or serum vials and autoclaved. Solutions C and E are autoclaved\
    \ separately under 100% N2 gas atmosphere. Solution D is autoclaved under 80%\
    \ N2 and 20% CO2 gas atmosphere. To complete the medium appropriate amounts of\
    \ solutions C to E are added to the sterile solution A in the sequence as indicated.\
    \ Final pH of the medium should be 7.2 - 7.4.\",\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"temperature\"\
    : null,\n      \"duration\": null\n    },\n    \"rationale\": \"Autoclaving and\
    \ the separate gas stages are stated; a numeric cycle is not supplied and must\
    \ not be invented.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz1701\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf\"\
    ,\n        \"source_locator\": \"Page 2 preparation\",\n        \"exact_source_quote\"\
    : \"tubes or serum vials and autoclaved.\",\n        \"snapshot_sha256\": \"1f8e94d802fae6bb1d85f81085b0de5e1c495b677000048b6efbce507cbf7dc3\"\
    ,\n        \"parsed_text_sha256\": \"127fc3ac38e309ca3cfa7ab3f8e9fccc43f44881ec2e52bcc6b0ff6980821f5b\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '19 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 19/20
    primary and 18/20 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi17883
  - chebi26710
  - chebi29377
  - chebi31206
  - chebi32149
  - chebi33118
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi63036
  - chebi63675
  - chebi75213
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86345
  - chebi86368
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 20: primary 95.00%;
    secondary 90.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact collection identity and sole maintained owner
  outcome: supported
  summary: Stable CultureMech:015346, DSMZ/MediaDive 1701 and the complete primary
    title agree. The specialized normalized owner has the same scientific fields;
    the target adds one merge event and bookkeeping. No unrelated Azospirillum medium
    is substituted.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - bound-owner-context
- assessment_id: evidence-scope
  area: evidence
  topic: Claim-level source support
  outcome: concern
  summary: Neither local layer attaches ingredient quantity evidence. Every local
    concentration is inventoried against literal primary text; source-stage facts
    remain separate from arithmetic. The unavailable API cannot corroborate its historical
    normalization.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Separate stocks and preserved main preparation
  outcome: concern
  summary: Both layers retain the main gas, below-pH-6 stage, minimum 30-minute interval,
    separate C/E and D handling and final pH 7.2–7.4. SL-10 iron-first dissolution
    and final 1000 mL make-up are incorrectly stored at the main root. Solutions,
    water and receiving amounts must be scoped; absent numerical C–E doses remain
    unresolved.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - primary
  - quantity-inventory
- assessment_id: forms
  area: grounding
  topic: Sodium salt, hydrate and unspecified succinate hydration
  outcome: concern
  summary: Primary Na-resazurin is a sodium salt, while CHEBI:8806 is neutral C12H7NO4.
    Primary nickel hexahydrate conflicts with CHEBI:34887 Cl2Ni. CHEBI:63675 specifies
    anhydrous disodium succinate, while Na-succinat is not hydrate-qualified; that
    is unverified specificity, not evidence for a different replacement. Other asserted
    salt hydrates are source-compatible; yeast extract remains an ungrounded mixture.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - primary
  - chebi8806
  - chebi34887
  - chebi63675
- assessment_id: classification
  area: scope
  topic: Composition, physical state and high-metal flag
  outcome: concern
  summary: COMPLEX/UNDEFINED is compatible with yeast extract and LIQUID with no solidifier.
    Both layers assert high_metal true. The schema defines a total-metal threshold,
    but the flattened stocks and unresolved assembly denominator do not establish
    that threshold for this medium. No low-metal or false replacement is inferred.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: growth
  area: scope
  topic: Biological and graph claim boundaries
  outcome: not_applicable
  summary: Title, specialized filing and generic Microbial cultivation are catalog
    metadata, not experimental growth support. Neither layer asserts an organism CURIE,
    growth condition object, internal variant graph or graph match requiring biological
    extrapolation. No phenotype or new growth assertion is introduced.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: current-writers
  area: provenance
  topic: Current writers and maintained input follow-up
  outcome: concern
  summary: Current MediaDive composition parsing restricts direct ingredients to the
    first solution and records receiving stock references separately, but preparation
    parsing gathers all solution steps at the main root. Current lossless merging
    preserves scientific differences and does not repair chemistry. The metal analyzer
    scans direct ingredients, approximates mass units without molecular-weight/stoichiometric
    conversion and uses a distribution threshold; the label writer copies its classifications
    by basename. Neither implementation proves this record’s historical writer version
    or a source-grounded final metal total. The two metal scripts are included in
    the supplementary native inspection input manifest; their current bytes are also
    separately hash-pinned in the code evidence.
  target_ids:
  - CultureMech:015346
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
  - current-code-3
findings:
- finding_id: f1
  issue_key: culturemech.015346.stock-stage-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Four solution stages and SL-10 are flattened into false final concentrations
  description: Both layers place A water-normalized salts, C succinate 162 g/L, D
    carbonate 50 g/L, E sulfide 30 g/L and SL-10 stock concentrations in one direct
    ingredient list. The primary supplies stage-specific masses/water and only appropriate
    receiving amounts for C–E. HCl 2.5 g/L also assumes an unstated percentage basis.
    This flat formula does not denote a supported assembled medium.
  target_ids:
  - CultureMech:015346
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
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
  issue_key: culturemech.015346.supplied-form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium salt and nickel hydrate are mapped to different supplied forms
  description: ingredients[7].term identifies neutral resazurin despite source sodium
    resazurin; ingredients[18].term and its current secondary slot identify Cl2Ni
    despite source nickel hexahydrate. Valid canonical labels do not resolve these
    mismatches. Succinate’s anhydrous specificity remains unverified separately.
  target_ids:
  - CultureMech:015346
  field_paths:
  - ingredients[7].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - ingredients[8].term
  evidence_ids:
  - primary
  - chebi8806
  - chebi34887
  - chebi63675
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.2
  native_severity: P3
  normalization_reason: P3 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: culturemech.015346.stock-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SL-10 make-up is detached from its stock
  description: preparation_steps[1] retains iron-first acid dissolution and make-up
    to 1000 mL at the main root. The primary assigns this instruction to SL-10; the
    assembled medium has no explicit final-volume statement.
  target_ids:
  - CultureMech:015346
  field_paths:
  - preparation_steps[1]
  - solutions
  evidence_ids:
  - record
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
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
  issue_key: culturemech.015346.unsupported-high-metal
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: High-metal flag lacks a valid final-medium basis
  description: high_metal true is asserted in both layers, while the available formulation
    has flattened stock concentrations and no quantified C–E receiving doses/final
    denominator. Neither the source nor the current heuristic writers provides a valid
    metal-total calculation for this assembled medium.
  target_ids:
  - CultureMech:015346
  field_paths:
  - high_metal
  - ingredients
  evidence_ids:
  - record
  - primary
  - current-code-2
  - current-code-3
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Reconstruct the maintained specialized owner with separate A/C/D/E
    and SL-10 stages, literal masses, water and explicit A stock doses. Preserve unquantified
    receiving amounts/final-volume uncertainty; do not normalize stock recipes as
    final medium. Attach narrow evidence before authorized regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
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
  description: Verify and correct source-compatible sodium-salt and nickel-hydrate
    identities in the maintained owner, assessing primary and secondary links independently.
    Qualify unverified succinate hydration without inventing a replacement.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
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
  description: Move the intact SL-10 preparation into its stock container while retaining
    the already-supported main preparation and all stage-specific gas/pH qualifiers.
    Do not substitute 1000 mL as the assembled final volume.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
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
  description: Qualify or withdraw the unsupported flag in the maintained owner pending
    stage-correct, molecular-form-aware total-metal calculation against the schema
    criterion. Do not replace it with false or infer a biological phenotype.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:015346
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml
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
- Required numerical C/D/E receiving doses and the assembled final-volume basis are
  not supplied by the inspected primary; both exact provider attempts returned 503.
  The source-defined stages and confirmed errors are reviewable, but reconstructing
  exact final concentrations remains unavailable. This partial scope does not imply
  the source masses are wrong.
- Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation.
  Primary DSMZ 1701 is available; the response is not formulation or historical-absence
  evidence.
- Exact MediaDive 1701 request returned HTTP 503; retained as provider-access limitation.
  Primary DSMZ 1701 is available; the response is not formulation or historical-absence
  evidence.
- The complete primary is available, but missing assembly doses are genuine source
  limits. No missing solution B, whole-stock transfer, percentage basis or sterilization
  cycle is invented.
- Current provider unavailability prevents a live provider-normalization comparison;
  it does not establish source chronology or invalidate the primary.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-027
- generated-medium
```
