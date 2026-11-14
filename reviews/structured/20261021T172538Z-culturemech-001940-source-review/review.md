# Source and formulation review: archaeoglobus_veneficus_medium (CultureMech:001940)

- Review: 20261021T172538Z-culturemech-001940-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T17:21:17Z
- Finished UTC: 2026-10-21T17:25:38Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 796 supports the exact identity and full main/trace formulation. The target retains 23 flattened ingredients; its later owner nests only four of thirteen trace solutes and retains mixed main/stock sums. Primary stock doses, explicit percent strengths and original waters differ from the stored final-rate representation. Trace pH 1 is incorrectly retained as a root preparation step. Chemical form assessment distinguishes a sodium-resazurin mismatch from ambiguous phosphate/nickel hydrate support; no measured final-volume normalization is assumed.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 302; batch 031 item 2 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty task batches contain 300 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 303 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001940 | data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml | generated | archaeoglobus_veneficus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001940 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001940 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch031/302/strict.tsv |
| validate-terms | passed | True | CultureMech:001940 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001940 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001940 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive796api | unavailable | False | CultureMech:001940 | Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary exists; historical provider normalization remains unauthenticated, without preventing the bounded primary comparison. |
| Exact source content access: mediadive796api_retry | unavailable | False | CultureMech:001940 | Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary exists; historical provider normalization remains unauthenticated, without preventing the bounded primary comparison. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001940.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001940.

38 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "NaCl main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "27.9462",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "27.9462",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "18.00",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored value explicitly includes an undiluted stock amount and has the wrong scope.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: NaCl",
        "exact_source_quote": "NaCl 18.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "KCl main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329013",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.329013",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.33",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: KCl",
        "exact_source_quote": "KCl 0.33 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "MgCl2 x 6 H2O main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "7.12861",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "7.12861",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "7.15",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: MgCl2 x 6 H2O",
        "exact_source_quote": "MgCl2 x 6 H2O 7.15 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "NH4Cl main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.249252",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.25",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: NH4Cl",
        "exact_source_quote": "NH4Cl 0.25 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "CaCl2 x 2 H2O main input",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.139581",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.139581",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.14",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored value explicitly includes an undiluted stock amount and has the wrong scope.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 0.14 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "K2HPO4 x 3 H2O main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.179462",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.179462",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.18",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: K2HPO4 x 3 H2O",
        "exact_source_quote": "K2HPO4 x 3 H2O 0.18 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "NaHCO3 main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3.98804",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3.98804",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "4.00",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: NaHCO3",
        "exact_source_quote": "NaHCO3 4.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Na2SO3 main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.997009",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.997009",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "1.00",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: Na2SO3",
        "exact_source_quote": "Na2SO3 1.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Na-acetate main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.997009",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.997009",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "1.00",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: Na-acetate",
        "exact_source_quote": "Na-acetate 1.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Na2S x 9 H2O main input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.498504",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.498504",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "batch_amount_g": "0.50",
      "final_medium_volume_ml": null
    },
    "rationale": "Preserve the literal main batch amount and separate stock contributions. The stored g/L normalization is not verified by primary input water; current API content is unavailable.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table: Na2S x 9 H2O",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Fe(NH4)2(SO4)2 x 6 H2O stock strength and receiving dose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.00199402",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.00199402",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": "2.00",
      "strength_percent_w_v": 0.1,
      "derived_delivered_mass_mg": 2,
      "final_medium_rate": null
    },
    "rationale": "0.1 g/100 mL times the stated volume supports delivered mass only. It does not independently establish the current g/L denominator or erase the stock representation.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main stock-addition row",
        "exact_source_quote": "Fe(NH4)2(SO4)2 x 6 H2O (0.1% w/v) 2.00 ml",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Sodium resazurin stock strength and receiving dose",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.000498504",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": "0.50",
      "strength_percent_w_v": 0.1,
      "derived_delivered_mass_mg": 0.5,
      "final_medium_rate": null
    },
    "rationale": "0.1 g/100 mL times the stated volume supports delivered mass only. It does not independently establish the current g/L denominator or erase the stock representation.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main stock-addition row",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Trace stock: MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "5.8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "5.8",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "5.80",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: MnCl2 x 4 H2O",
        "exact_source_quote": "MnCl2 x 4 H2O 5.80 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Trace stock: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "27.9462",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "27.9462",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "10.00",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: NaCl",
        "exact_source_quote": "NaCl 10.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Trace stock: (NH4)2Ni(SO4)2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "2.00",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: (NH4)2Ni(SO4)2",
        "exact_source_quote": "(NH4)2Ni(SO4)2 2.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Trace stock: FeSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].composition[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "1.00",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: FeSO4 x 7 H2O",
        "exact_source_quote": "FeSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Trace stock: CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].composition[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "1.00",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: CoCl2 x 6 H2O",
        "exact_source_quote": "CoCl2 x 6 H2O 1.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Trace stock: CaCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.139581",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "1.139581",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "1.00",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: CaCl2 x 2 H2O",
        "exact_source_quote": "CaCl2 x 2 H2O 1.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Trace stock: ZnSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].composition[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "1.00",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Trace stock: CuSO4 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "0.10",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO4 x 5 H2O 0.10 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Trace stock: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "0.10",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: H3BO3",
        "exact_source_quote": "H3BO3 0.10 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "Trace stock: AlK(SO4)2 x 12 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "0.10",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: AlK(SO4)2 x 12 H2O",
        "exact_source_quote": "AlK(SO4)2 x 12 H2O 0.10 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Trace stock: Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "0.10",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: Na2MoO4 x 2 H2O",
        "exact_source_quote": "Na2MoO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Trace stock: Na2WO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "0.10",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: Na2WO4 x 2 H2O",
        "exact_source_quote": "Na2WO4 x 2 H2O 0.10 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Trace stock: Na2SeO3 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount_g": "0.10",
      "stock_water_input_ml": 1000,
      "main_dose_ml": 1,
      "measured_stock_or_medium_volume": null
    },
    "rationale": "The target and remaining direct-owner values have the wrong stock/main scope. Four owner components already have stock membership; for those the original amount matches, but the final stock-volume basis and attached evidence remain unverified, so their individual decision is unsupported rather than a repeated scope correction.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace element solution: Na2SeO3 x 5 H2O",
        "exact_source_quote": "Na2SeO3 x 5 H2O 0.10 g",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Trace solution receiving amount",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "ML_PER_L"
        },
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 1,
      "receiving_batch_final_volume": null
    },
    "rationale": "The target lacks the dose. The owner has 1 mL/L; primary states 1 mL for this batch, not a measured final-litre denominator. Preserve the source batch dose and the separately unresolved normalization.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table",
        "exact_source_quote": "Trace element solution 1.00 ml",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Main input water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "water_input_ml": 1000,
      "source_stage": "Main input water",
      "measured_final_volume_ml": null
    },
    "rationale": "This source water quantity is absent. The locator denotes a proposed absent row, not an existing list object; water input alone does not establish final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main table final row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Trace-stock input water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "solutions[0].composition[13].concentration",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].composition[13].concentration",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "water_input_ml": 1000,
      "source_stage": "Trace-stock input water",
      "measured_final_volume_ml": null
    },
    "rationale": "This source water quantity is absent. The locator denotes a proposed absent row, not an existing list object; water input alone does not establish final volume.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 2, trace table final row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Owner trace preparation-volume assertion",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null,
        "decision": "unsupported"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).",
        "decision": "unsupported"
      }
    ],
    "proposed_source_representation": {
      "stock_water_input_ml": 1000,
      "measured_final_stock_volume_ml": null
    },
    "rationale": "The owner note claims a prepared 1000 mL stock and per-litre addition from MediaDive. The current primary states water input only; unavailable API content does not authenticate that additional volume interpretation.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 2, trace final table row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Initial gas and sparging duration",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "N2_percent": 80,
      "CO2_percent": 20,
      "percent_basis": null,
      "minutes": [
        30,
        45
      ]
    },
    "rationale": "Preserve the exact stage and qualifying language. The existing prose is supported but lacks claim-level evidence; it is not an independent growth or optimization assertion.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Initial gas and sparging duration",
        "exact_source_quote": "medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Equilibrated main pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "pH": 7,
      "stage": "After bicarbonate and gas equilibration"
    },
    "rationale": "Preserve the exact stage and qualifying language. The existing prose is supported but lacks claim-level evidence; it is not an independent growth or optimization assertion.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Equilibrated main pH",
        "exact_source_quote": "20% CO2 gas mixture to achieve a medium pH of 7.0.",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Illustrative vessel quantities",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "example_medium_ml": 25,
      "example_bottle_ml": 100,
      "mandatory_scale": false
    },
    "rationale": "Preserve the exact stage and qualifying language. The existing prose is supported but lacks claim-level evidence; it is not an independent growth or optimization assertion.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Illustrative vessel quantities",
        "exact_source_quote": "e.g., 25 ml per 100 ml bottle",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "Post-autoclave stock atmosphere",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "N2_percent": 100,
      "stocks": [
        "sulfite",
        "acetate",
        "sulfide"
      ]
    },
    "rationale": "Preserve the exact stage and qualifying language. The existing prose is supported but lacks claim-level evidence; it is not an independent growth or optimization assertion.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Post-autoclave stock atmosphere",
        "exact_source_quote": "under 100% N2 gas.",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Conditional complete-medium pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle) and autoclave. After sterilization add sulfite, acetate and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite should be freshly prepared and sterilized by filtration. Prior to inoculation check pH of complete medium and adjust to 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "pH": 7,
      "conditional": true
    },
    "rationale": "Preserve the exact stage and qualifying language. The existing prose is supported but lacks claim-level evidence; it is not an independent growth or optimization assertion.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Conditional complete-medium pH",
        "exact_source_quote": "adjust to 7.0, if\nnecessary.",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "Later pressure and gas stage",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "After inoculation, pressurize bottles to 1 bar overpressure with sterile 80% H2 and 20% CO2 gas mixture.",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "After inoculation, pressurize bottles to 1 bar overpressure with sterile 80% H2 and 20% CO2 gas mixture.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "pressure_bar_overpressure": 1,
      "H2_percent": 80,
      "CO2_percent": 20,
      "percent_basis": null,
      "stage": "Source explicitly after inoculation"
    },
    "rationale": "Preserve the exact stage and qualifying language. The existing prose is supported but lacks claim-level evidence; it is not an independent growth or optimization assertion.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Later pressure and gas stage",
        "exact_source_quote": "pressurize bottles to 1 bar overpressure with sterile 80% H2 and 20%",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Trace-stock pH",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Adjust pH to 1.0 with HCl.",
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Adjust pH to 1.0 with HCl.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "pH": 1,
      "stage": "Trace element stock only"
    },
    "rationale": "Preserve the exact stage and qualifying language. The source pH 1 belongs only to the trace stock and must not remain an unscoped root-medium adjustment.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Pages 1–2, Trace-stock pH",
        "exact_source_quote": "Adjust pH to 1.0 with HCl.",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Typed main pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "ph_value",
        "stored": 7.0,
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "pH": 7,
      "scope": "Main mixture, distinct from trace pH 1"
    },
    "rationale": "Retain the supported main value with its source stage and conditional later readjustment.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 1, main preparation",
        "exact_source_quote": "20% CO2 gas mixture to achieve a medium pH of 7.0.",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Trace HCl titration quantity",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null,
        "decision": "not_quantified"
      },
      {
        "input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition and volume from MediaDive (#150).",
        "decision": "not_quantified"
      }
    ],
    "proposed_source_representation": {
      "reagent": "HCl",
      "fixed_amount": null
    },
    "rationale": "The source states a pH target, not an HCl amount or strength; no fixed dose is invented.",
    "source_snippets": [
      {
        "source_key": "dsmz796",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf",
        "source_locator": "Page 2, trace final sentence",
        "exact_source_quote": "Adjust pH to 1.0 with HCl.",
        "snapshot_sha256": "e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22",
        "parsed_text_sha256": "824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99",
        "accessed_at": "2026-10-21T17:04:22.523340Z"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:001940.

23 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 23/23 primary and 22/23 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 23: primary 100.00%; secondary 95.65%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001940.

18 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact DSMZ accession and maintained owner

identity: supported. Targets: CultureMech:001940.

The generated target and exact archaeal owner share CultureMech:001940 and DSMZ 796. The owner records a later four-component stock-nesting event, while the generated target remains fully flattened; this recorded local chronology does not authenticate unavailable historical API bytes.

### Salt/hydrate support and ontology internal tension

grounding: concern. Targets: CultureMech:001940.

Neutral CHEBI:8806 does not represent the explicit sodium-resazurin salt. Source K2HPO4 is trihydrate, whereas CHEBI:131527 has an anhydrous formula/structure despite a trihydrate synonym; that internal tension requires exact-form resolution, not a synonym-only assurance. Source nickel ammonium sulfate hydration is unspecified, so CHEBI:86149 hexahydrate is not established but is not proven false. Sodium acetate hydration is likewise unspecified. Other explicit hydrates match captured term formulae.

### Main and stock stages

completeness: concern. Targets: CultureMech:001940.

Both layers preserve main gases, examples, conditional pH and explicit 1 bar overpressure. The trace pH 1 instruction is at the root and lacks its stock scope. Fresh sulfite filtration is explicit; the primary gives no numerical autoclave cycle. No preparation quantity is recast as a growth condition.

### Defined formulation and application scope

scope: supported. Targets: CultureMech:001940.

The source contains named chemicals and a defined trace stock without an undefined extract. DEFINED and LIQUID are consistent, subject to exact supplied-form caveats. Title and generic cultivation application establish no new organism-specific growth outcome or optimum.

### Current writers and follow-up ownership

provenance: concern. Targets: CultureMech:001940.

The current importer separates primary and stock rows; cleanup avoids summing conflicting duplicates. The nesting writer selects name/value matches, and plan_record returns early when solutions already exist; rerunning it is not proof of a complete repair for this owner with four nested components. Reassess the full maintained stock and source-stage fields, preserve the historical event and regenerate only after authorized corrections.

## Findings

### f1: Stock flattening remains after a partial owner repair

blocker / open / confirmed; issue key: culturemech.001940.incomplete-stock-restoration.

The target has 23 direct components; the owner has 19 direct and four nested trace components. Nine of thirteen trace solutes remain direct or combined with main NaCl/calcium, and source stock/water boundaries are incomplete. Main g/L rates lack a verified final-volume basis.

### f2: Trace pH 1 is represented as a root-medium adjustment

major / open / confirmed; issue key: culturemech.001940.trace-ph-at-root.

preparation_steps[2] in both layers contains the trace-stock pH 1 instruction without a stock boundary, while the main medium is pH 7. This scope error persists despite later partial nesting.

### f3: Salt identity and hydrate assertions require source-specific correction

major / open / confirmed; issue key: culturemech.001940.supplied-chemical-form.

The explicit sodium-resazurin salt is linked to neutral resazurin. The phosphate trihydrate is linked to an ontology entry with anhydrous structure but a conflicting hydrate synonym. Nickel-salt and acetate hydrate qualifiers remain unestablished rather than disproven.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct all thirteen trace solutes and source water, separate main and stock contributions and preserve the 1 mL receiving amount. Retain the four correctly nested identities while qualifying unsupported rate bases; do not treat an existing solution node as proof of completeness.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Move or explicitly qualify this instruction as trace-stock preparation, preserving unquantified HCl and the existing main gas/pH stages. Keep the complete source scope when regenerating.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the explicit sodium salt and phosphate hydrate with exact authoritative evidence, preserving the ontology tension. Qualify unresolved nickel/acetate hydration without guessing replacement IDs or molecular-weight conversions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch031/302/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch031/302/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml:1:id: CultureMech:001940<br>./data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml:1:id: CultureMech:001940<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch031/source-preflight-bound/302/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 26 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch031/source-preflight-bound/302/evidence-context-original.json; Whole target, all maintained owners and scoped dependencies | context_only | All frozen local-record objects match fresh inspected YAML. Source interpretations are separately checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf; Pages 1–2, complete main and trace tables and all preparation paragraphs | supports | Exact primary supplies main batch amounts, a 1 mL trace dose, two explicitly w/v stocks, trace composition and distinct gas/pH stages. Input water is not a measured final-volume declaration. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch031/302/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131361 resolves to disodium selenite pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32954 resolves to sodium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63939 resolves to sodium tungstate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76181 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86477 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86477; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86477 resolves to sodium sulfite. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76181": [{"label": "Fe(NH4)2(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76181", "preferred_term": "Fe(NH4)2(SO4)2 x 6 H2O", "ontology_id": "CHEBI:76181", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86477": [{"label": "Na2SO3", "match_type": "preferred_term", "identifier": "CHEBI:86477", "preferred_term": "Na2SO3", "ontology_id": "CHEBI:86477", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na2SO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86477", "preferred_term": "Na2SO3 x 5 H2O", "ontology_id": "CHEBI:86477", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml; data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml", "events": 9, "timestamp_issues": []}] |
| current-code-0 | src/culturemech/import/mediadive_importer.py; Current scoped code; no historical-version inference | context_only | The current importer separates primary and stock rows; cleanup avoids summing conflicting duplicates. The nesting writer selects name/value matches, and plan_record returns early when solutions already exist; rerunning it is not proof of a complete repair for this owner with four nested components. Reassess the full maintained stock and source-stage fields, preserve the historical event and regenerate only after authorized corrections. |
| current-code-1 | scripts/cleanup_media_quality.py; Current scoped code; no historical-version inference | context_only | The current importer separates primary and stock rows; cleanup avoids summing conflicting duplicates. The nesting writer selects name/value matches, and plan_record returns early when solutions already exist; rerunning it is not proof of a complete repair for this owner with four nested components. Reassess the full maintained stock and source-stage fields, preserve the historical event and regenerate only after authorized corrections. |
| current-code-2 | scripts/apply_cocktail_nesting.py; Current scoped code; no historical-version inference | context_only | The current importer separates primary and stock rows; cleanup avoids summing conflicting duplicates. The nesting writer selects name/value matches, and plan_record returns early when solutions already exist; rerunning it is not proof of a complete repair for this owner with four nested components. Reassess the full maintained stock and source-stage fields, preserve the historical event and regenerate only after authorized corrections. |
| current-code-3 | src/culturemech/merge/merge_recipes.py; Current scoped code; no historical-version inference | context_only | The current importer separates primary and stock rows; cleanup avoids summing conflicting duplicates. The nesting writer selects name/value matches, and plan_record returns early when solutions already exist; rerunning it is not proof of a complete repair for this owner with four nested components. Reassess the full maintained stock and source-stage fields, preserve the historical event and regenerate only after authorized corrections. |
| mediadive796api-attempt | https://mediadive.dsmz.de/rest/medium/796; Preserved exact public retrieval result | context_only | Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary exists; historical provider normalization remains unauthenticated, without preventing the bounded primary comparison. |
| mediadive796api_retry-attempt | https://mediadive.dsmz.de/rest/medium/796; Preserved exact public retrieval result | context_only | Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary exists; historical provider normalization remains unauthenticated, without preventing the bounded primary comparison. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary exists; historical provider normalization remains unauthenticated, without preventing the bounded primary comparison.
- Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary exists; historical provider normalization remains unauthenticated, without preventing the bounded primary comparison.
- Listed main liquids sum to 1003.5 mL before further unquantified stock volumes. Neither that sum nor the source 1000 mL water establishes final main volume or the historical 1.003 L normalization.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172538Z-culturemech-001940-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: archaeoglobus_veneficus_medium (CultureMech:001940)'
started_at: '2026-10-21T17:21:17Z'
finished_at: '2026-10-21T17:25:38Z'
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
summary: DSMZ 796 supports the exact identity and full main/trace formulation. The
  target retains 23 flattened ingredients; its later owner nests only four of thirteen
  trace solutes and retains mixed main/stock sums. Primary stock doses, explicit percent
  strengths and original waters differ from the stored final-rate representation.
  Trace pH 1 is incorrectly retained as a root preparation step. Chemical form assessment
  distinguishes a sodium-resazurin mismatch from ambiguous phosphate/nickel hydrate
  support; no measured final-volume normalization is assumed.
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
  - path: data/import_tracking/researched_stock_volumes.json
    sha256: 27c4cfe55b6309acf2faa608340747f1db483d510bd926b5c90795787ae6767f
    role: context
  - path: data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
    sha256: ccfa2afabde6857f6c0645f1235c812c191654ac6fed5122bcb8fffa0169e3c2
    role: target
  - path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
    sha256: 9a28724f88f22f3eeb96d81ff253d7a628cc55b6e3484d38da7711122ca370f0
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
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
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
  - path: scripts/identify_cocktail_stocks.py
    sha256: 8811249ada4a931e1d0c616648ac91a5a81aba728babf6436462c577a40f0638
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
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  selection: Task review 302; batch 031 item 2 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty task batches contain
    300 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 303 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001940
targets:
- target_id: CultureMech:001940
  path: data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  label: archaeoglobus_veneficus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch031/302/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch031/302/strict.tsv"
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001940
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
  - CultureMech:001940
- check_id: mediadive796api-source-access
  name: 'Exact source content access: mediadive796api'
  required: false
  status: unavailable
  summary: Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ
    primary exists; historical provider normalization remains unauthenticated, without
    preventing the bounded primary comparison.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - mediadive796api-attempt
- check_id: mediadive796api_retry-source-access
  name: 'Exact source content access: mediadive796api_retry'
  required: false
  status: unavailable
  summary: Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ
    primary exists; historical provider normalization remains unauthenticated, without
    preventing the bounded primary comparison.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - mediadive796api_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:36.342715Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch031/302/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:37.504719Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-031/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch031/302/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:38.868094Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:21:39.735145Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T17:25:36Z'
  support: supports
  summary: './data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml:1:id:
    CultureMech:001940

    ./data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml:1:id: CultureMech:001940

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/source-preflight-bound/302/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T17:25:36Z'
  support: supports
  summary: 26 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 4284a2b99cc5f5f05ae24bb03c9b0baba6342ba41825f5022cd8551ba8d01240
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/source-preflight-bound/302/evidence-context-original.json
  locator: Whole target, all maintained owners and scoped dependencies
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: All frozen local-record objects match fresh inspected YAML. Source interpretations
    are separately checked against actual bound raw/text bytes.
  snapshot_sha256: 4c092dd031d1f7072c5bf35edc7811356fdf02a6d9b68a58d40948ad08db9adb
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf
  locator: Pages 1–2, complete main and trace tables and all preparation paragraphs
  accessed_at: '2026-10-21T17:04:22.523340Z'
  support: supports
  summary: Exact primary supplies main batch amounts, a 1 mL trace dose, two explicitly
    w/v stocks, trace composition and distinct gas/pH stages. Input water is not a
    measured final-volume declaration.
  snapshot_sha256: e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch031/302/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: a23e8122660b5a50dcef89181246bfeaab5ec0a7a90c5dd81a69e9bce83e6086
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
- evidence_id: chebi32954
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:48.206583Z'
  support: supports
  summary: CHEBI:32954 resolves to sodium acetate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
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
- evidence_id: chebi76181
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:28:27.017914Z'
  support: supports
  summary: CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 1ca5b1ee73ce8d8fd35e60c7f45baacd870b6f5fdce0a02345be62e7622dbaa5
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
- evidence_id: chebi86149
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:08.844455Z'
  support: supports
  summary: CHEBI:86149 resolves to ammonium nickel sulfate hexahydrate. Identifier
    existence and label metadata do not establish source-specific hydrate, stereochemistry
    or product identity.
  snapshot_sha256: 930d93c33f6115f19153868ae36f0153b69406fd555708237a7ccccfb010cd97
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
- evidence_id: chebi86477
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86477
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T16:34:01.002738Z'
  support: supports
  summary: CHEBI:86477 resolves to sodium sulfite. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 30bc14ca6bced2833a5eb78d182f7d1197dc81480ba320d09e80c9185319fb36
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
  accessed_at: '2026-10-21T17:25:36Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:131527": [{"label": "K2HPO4", "match_type":
    "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term",
    "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label":
    "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type":
    "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id":
    "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312":
    [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312",
    "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954":
    [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954",
    "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503":
    [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier":
    "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id":
    "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939":
    [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939",
    "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term":
    "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76181":
    [{"label": "Fe(NH4)2(SO4)2 x 6 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:76181", "preferred_term": "Fe(NH4)2(SO4)2 x 6 H2O", "ontology_id": "CHEBI:76181",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label":
    "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term":
    "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86149": [{"label": "(NH4)2Ni(SO4)2", "match_type": "preferred_term",
    "identifier": "CHEBI:86149", "preferred_term": "(NH4)2Ni(SO4)2", "ontology_id":
    "CHEBI:86149", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "(NH4)2Ni(SO4)2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86149", "preferred_term":
    "(NH4)2Ni(SO4)2 x 6 H2O", "ontology_id": "CHEBI:86149", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O",
    "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2
    x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465":
    [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86477": [{"label":
    "Na2SO3", "match_type": "preferred_term", "identifier": "CHEBI:86477", "preferred_term":
    "Na2SO3", "ontology_id": "CHEBI:86477", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Na2SO3 x 5 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86477", "preferred_term": "Na2SO3 x 5 H2O", "ontology_id": "CHEBI:86477",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml; data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": []}, {"input": "data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml",
    "events": 9, "timestamp_issues": []}]'
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: The current importer separates primary and stock rows; cleanup avoids summing
    conflicting duplicates. The nesting writer selects name/value matches, and plan_record
    returns early when solutions already exist; rerunning it is not proof of a complete
    repair for this owner with four nested components. Reassess the full maintained
    stock and source-stage fields, preserve the historical event and regenerate only
    after authorized corrections.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: The current importer separates primary and stock rows; cleanup avoids summing
    conflicting duplicates. The nesting writer selects name/value matches, and plan_record
    returns early when solutions already exist; rerunning it is not proof of a complete
    repair for this owner with four nested components. Reassess the full maintained
    stock and source-stage fields, preserve the historical event and regenerate only
    after authorized corrections.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: current-code-2
  kind: record_content
  reference: scripts/apply_cocktail_nesting.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: The current importer separates primary and stock rows; cleanup avoids summing
    conflicting duplicates. The nesting writer selects name/value matches, and plan_record
    returns early when solutions already exist; rerunning it is not proof of a complete
    repair for this owner with four nested components. Reassess the full maintained
    stock and source-stage fields, preserve the historical event and regenerate only
    after authorized corrections.
  snapshot_sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
- evidence_id: current-code-3
  kind: record_content
  reference: src/culturemech/merge/merge_recipes.py
  locator: Current scoped code; no historical-version inference
  accessed_at: '2026-10-21T17:25:36Z'
  support: context_only
  summary: The current importer separates primary and stock rows; cleanup avoids summing
    conflicting duplicates. The nesting writer selects name/value matches, and plan_record
    returns early when solutions already exist; rerunning it is not proof of a complete
    repair for this owner with four nested components. Reassess the full maintained
    stock and source-stage fields, preserve the historical event and regenerate only
    after authorized corrections.
  snapshot_sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
- evidence_id: mediadive796api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/796
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:04:21.601078Z'
  support: context_only
  summary: Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ
    primary exists; historical provider normalization remains unauthenticated, without
    preventing the bounded primary comparison.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive796api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/796
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:05:12.836673Z'
  support: context_only
  summary: Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ
    primary exists; historical provider normalization remains unauthenticated, without
    preventing the bounded primary comparison.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001940
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
  - CultureMech:001940
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    NaCl main input\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27.9462\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"27.9462\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"18.00\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored value explicitly includes an undiluted stock\
    \ amount and has the wrong scope.\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main table: NaCl\",\n        \"exact_source_quote\"\
    : \"NaCl 18.00 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\": \"KCl\
    \ main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329013\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.329013\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"0.33\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: KCl\",\n        \"exact_source_quote\"\
    : \"KCl 0.33 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\": \"MgCl2\
    \ x 6 H2O main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.12861\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7.12861\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"7.15\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: MgCl2 x 6 H2O\",\n        \"exact_source_quote\"\
    : \"MgCl2 x 6 H2O 7.15 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\": \"NH4Cl\
    \ main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.249252\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"0.25\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: NH4Cl\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.25 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\": \"CaCl2\
    \ x 2 H2O main input\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.139581\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.139581\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"0.14\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored value explicitly includes an undiluted stock\
    \ amount and has the wrong scope.\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main table: CaCl2 x 2 H2O\",\n      \
    \  \"exact_source_quote\": \"CaCl2 x 2 H2O 0.14 g\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\": \"K2HPO4\
    \ x 3 H2O main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.179462\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.179462\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"0.18\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: K2HPO4 x 3 H2O\",\n        \"exact_source_quote\"\
    : \"K2HPO4 x 3 H2O 0.18 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\": \"NaHCO3\
    \ main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.98804\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.98804\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"4.00\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: NaHCO3\",\n        \"exact_source_quote\"\
    : \"NaHCO3 4.00 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\": \"Na2SO3\
    \ main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.997009\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.997009\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"1.00\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: Na2SO3\",\n        \"exact_source_quote\"\
    : \"Na2SO3 1.00 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\": \"Na-acetate\
    \ main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.997009\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.997009\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"1.00\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: Na-acetate\",\n        \"exact_source_quote\"\
    : \"Na-acetate 1.00 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\": \"Na2S\
    \ x 9 H2O main input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.498504\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.498504\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"batch_amount_g\": \"0.50\",\n      \"final_medium_volume_ml\": null\n\
    \    },\n    \"rationale\": \"Preserve the literal main batch amount and separate\
    \ stock contributions. The stored g/L normalization is not verified by primary\
    \ input water; current API content is unavailable.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 1, main table: Na2S x 9 H2O\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\": \"Fe(NH4)2(SO4)2\
    \ x 6 H2O stock strength and receiving dose\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00199402\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"unsupported\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.00199402\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": \"2.00\",\n      \"strength_percent_w_v\": 0.1,\n    \
    \  \"derived_delivered_mass_mg\": 2,\n      \"final_medium_rate\": null\n    },\n\
    \    \"rationale\": \"0.1 g/100 mL times the stated volume supports delivered\
    \ mass only. It does not independently establish the current g/L denominator or\
    \ erase the stock representation.\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main stock-addition row\",\n        \"\
    exact_source_quote\": \"Fe(NH4)2(SO4)2 x 6 H2O (0.1% w/v) 2.00 ml\",\n       \
    \ \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\": \"Sodium\
    \ resazurin stock strength and receiving dose\",\n    \"decision\": \"unsupported\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\"\n      },\n      {\n      \
    \  \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000498504\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": \"0.50\",\n      \"strength_percent_w_v\": 0.1,\n    \
    \  \"derived_delivered_mass_mg\": 0.5,\n      \"final_medium_rate\": null\n  \
    \  },\n    \"rationale\": \"0.1 g/100 mL times the stated volume supports delivered\
    \ mass only. It does not independently establish the current g/L denominator or\
    \ erase the stock representation.\",\n    \"source_snippets\": [\n      {\n  \
    \      \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main stock-addition row\",\n        \"\
    exact_source_quote\": \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\": \"Trace\
    \ stock: MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"5.8\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"5.80\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: MnCl2 x 4\
    \ H2O\",\n        \"exact_source_quote\": \"MnCl2 x 4 H2O 5.80 g\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\": \"Trace\
    \ stock: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27.9462\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"27.9462\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"10.00\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: NaCl\",\n\
    \        \"exact_source_quote\": \"NaCl 10.00 g\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\": \"Trace\
    \ stock: (NH4)2Ni(SO4)2\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"2.00\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: (NH4)2Ni(SO4)2\"\
    ,\n        \"exact_source_quote\": \"(NH4)2Ni(SO4)2 2.00 g\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\": \"Trace\
    \ stock: FeSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"1.00\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: FeSO4 x 7\
    \ H2O\",\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 1.00 g\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\": \"Trace\
    \ stock: CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[2].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"1.00\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: CoCl2 x 6\
    \ H2O\",\n        \"exact_source_quote\": \"CoCl2 x 6 H2O 1.00 g\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\": \"Trace\
    \ stock: CaCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.139581\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.139581\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"1.00\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: CaCl2 x 2\
    \ H2O\",\n        \"exact_source_quote\": \"CaCl2 x 2 H2O 1.00 g\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\": \"Trace\
    \ stock: ZnSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[3].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"1.00\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: ZnSO4 x 7\
    \ H2O\",\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 1.00 g\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\": \"Trace\
    \ stock: CuSO4 x 5 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"0.10\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: CuSO4 x 5\
    \ H2O\",\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 0.10 g\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\": \"Trace\
    \ stock: H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"0.10\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: H3BO3\",\n\
    \        \"exact_source_quote\": \"H3BO3 0.10 g\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\": \"Trace\
    \ stock: AlK(SO4)2 x 12 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"0.10\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: AlK(SO4)2\
    \ x 12 H2O\",\n        \"exact_source_quote\": \"AlK(SO4)2 x 12 H2O 0.10 g\",\n\
    \        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\": \"Trace\
    \ stock: Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"0.10\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: Na2MoO4 x\
    \ 2 H2O\",\n        \"exact_source_quote\": \"Na2MoO4 x 2 H2O 0.10 g\",\n    \
    \    \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\": \"Trace\
    \ stock: Na2WO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"0.10\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: Na2WO4 x 2\
    \ H2O\",\n        \"exact_source_quote\": \"Na2WO4 x 2 H2O 0.10 g\",\n       \
    \ \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\": \"Trace\
    \ stock: Na2SeO3 x 5 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount_g\": \"0.10\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"main_dose_ml\": 1,\n      \"measured_stock_or_medium_volume\"\
    : null\n    },\n    \"rationale\": \"The target and remaining direct-owner values\
    \ have the wrong stock/main scope. Four owner components already have stock membership;\
    \ for those the original amount matches, but the final stock-volume basis and\
    \ attached evidence remain unverified, so their individual decision is unsupported\
    \ rather than a repeated scope correction.\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Trace element solution: Na2SeO3 x\
    \ 5 H2O\",\n        \"exact_source_quote\": \"Na2SeO3 x 5 H2O 0.10 g\",\n    \
    \    \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\": \"Trace\
    \ solution receiving amount\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\",\n    \
    \    \"field_path\": \"solutions[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"ML_PER_L\"\n        },\n \
    \       \"decision\": \"unsupported\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 1,\n      \"receiving_batch_final_volume\": null\n   \
    \ },\n    \"rationale\": \"The target lacks the dose. The owner has 1 mL/L; primary\
    \ states 1 mL for this batch, not a measured final-litre denominator. Preserve\
    \ the source batch dose and the separately unresolved normalization.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz796\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main table\",\n        \"exact_source_quote\"\
    : \"Trace element solution 1.00 ml\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\": \"Main\
    \ input water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\",\n    \
    \    \"field_path\": \"ingredients[23].concentration\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"water_input_ml\": 1000,\n      \"source_stage\": \"Main input water\"\
    ,\n      \"measured_final_volume_ml\": null\n    },\n    \"rationale\": \"This\
    \ source water quantity is absent. The locator denotes a proposed absent row,\
    \ not an existing list object; water input alone does not establish final volume.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz796\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main table final row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\": \"Trace-stock\
    \ input water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[13].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[13].concentration\",\n \
    \       \"stored\": null,\n        \"decision\": \"add\"\n      }\n    ],\n  \
    \  \"proposed_source_representation\": {\n      \"water_input_ml\": 1000,\n  \
    \    \"source_stage\": \"Trace-stock input water\",\n      \"measured_final_volume_ml\"\
    : null\n    },\n    \"rationale\": \"This source water quantity is absent. The\
    \ locator denotes a proposed absent row, not an existing list object; water input\
    \ alone does not establish final volume.\",\n    \"source_snippets\": [\n    \
    \  {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 2, trace table final row\",\n        \"\
    exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\": \"Owner\
    \ trace preparation-volume assertion\",\n    \"decision\": \"unsupported\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : null,\n        \"decision\": \"unsupported\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition\
    \ and volume from MediaDive (#150).\",\n        \"decision\": \"unsupported\"\n\
    \      }\n    ],\n    \"proposed_source_representation\": {\n      \"stock_water_input_ml\"\
    : 1000,\n      \"measured_final_stock_volume_ml\": null\n    },\n    \"rationale\"\
    : \"The owner note claims a prepared 1000 mL stock and per-litre addition from\
    \ MediaDive. The current primary states water input only; unavailable API content\
    \ does not authenticate that additional volume interpretation.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Page 2, trace final table row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\": \"Initial\
    \ gas and sparging duration\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"N2_percent\": 80,\n      \"CO2_percent\": 20,\n      \"percent_basis\"\
    : null,\n      \"minutes\": [\n        30,\n        45\n      ]\n    },\n    \"\
    rationale\": \"Preserve the exact stage and qualifying language. The existing\
    \ prose is supported but lacks claim-level evidence; it is not an independent\
    \ growth or optimization assertion.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Initial gas and sparging duration\"\
    ,\n        \"exact_source_quote\": \"medium with 80% N2 and 20% CO2 gas mixture\
    \ for 30 - 45 min\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\": \"Equilibrated\
    \ main pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"pH\": 7,\n      \"stage\": \"After bicarbonate and gas equilibration\"\
    \n    },\n    \"rationale\": \"Preserve the exact stage and qualifying language.\
    \ The existing prose is supported but lacks claim-level evidence; it is not an\
    \ independent growth or optimization assertion.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Equilibrated main pH\",\n        \"\
    exact_source_quote\": \"20% CO2 gas mixture to achieve a medium pH of 7.0.\",\n\
    \        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\": \"Illustrative\
    \ vessel quantities\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"example_medium_ml\": 25,\n      \"example_bottle_ml\": 100,\n   \
    \   \"mandatory_scale\": false\n    },\n    \"rationale\": \"Preserve the exact\
    \ stage and qualifying language. The existing prose is supported but lacks claim-level\
    \ evidence; it is not an independent growth or optimization assertion.\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz796\",\n   \
    \     \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Illustrative vessel quantities\",\n\
    \        \"exact_source_quote\": \"e.g., 25 ml per 100 ml bottle\",\n        \"\
    snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\": \"Post-autoclave\
    \ stock atmosphere\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"N2_percent\": 100,\n      \"stocks\": [\n        \"sulfite\",\n \
    \       \"acetate\",\n        \"sulfide\"\n      ]\n    },\n    \"rationale\"\
    : \"Preserve the exact stage and qualifying language. The existing prose is supported\
    \ but lacks claim-level evidence; it is not an independent growth or optimization\
    \ assertion.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Post-autoclave stock atmosphere\"\
    ,\n        \"exact_source_quote\": \"under 100% N2 gas.\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\": \"Conditional\
    \ complete-medium pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve ingredients (except bicarbonate, sulfite, acetate and sulfide), then\
    \ sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it\
    \ anoxic. Thereafter, add and dissolve bicarbonate and equilibrate the medium\
    \ with the 80% N2 and 20% CO2 gas mixture to achieve a medium pH of 7.0. Dispense\
    \ medium under same gas atmosphere into serum vials (e.g., 25 ml per 100 ml bottle)\
    \ and autoclave. After sterilization add sulfite, acetate and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. The stock solution of sulfite\
    \ should be freshly prepared and sterilized by filtration. Prior to inoculation\
    \ check pH of complete medium and adjust to 7.0, if necessary.\",\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"pH\": 7,\n      \"conditional\": true\n    },\n    \"rationale\"\
    : \"Preserve the exact stage and qualifying language. The existing prose is supported\
    \ but lacks claim-level evidence; it is not an independent growth or optimization\
    \ assertion.\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Conditional complete-medium pH\",\n\
    \        \"exact_source_quote\": \"adjust to 7.0, if\\nnecessary.\",\n       \
    \ \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\": \"Later\
    \ pressure and gas stage\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"After inoculation, pressurize bottles to 1 bar overpressure with sterile 80%\
    \ H2 and 20% CO2 gas mixture.\",\n        \"decision\": \"evidence_only\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"After inoculation, pressurize bottles to 1 bar overpressure with sterile 80%\
    \ H2 and 20% CO2 gas mixture.\",\n        \"decision\": \"evidence_only\"\n  \
    \    }\n    ],\n    \"proposed_source_representation\": {\n      \"pressure_bar_overpressure\"\
    : 1,\n      \"H2_percent\": 80,\n      \"CO2_percent\": 20,\n      \"percent_basis\"\
    : null,\n      \"stage\": \"Source explicitly after inoculation\"\n    },\n  \
    \  \"rationale\": \"Preserve the exact stage and qualifying language. The existing\
    \ prose is supported but lacks claim-level evidence; it is not an independent\
    \ growth or optimization assertion.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Pages 1–2, Later pressure and gas stage\",\n\
    \        \"exact_source_quote\": \"pressurize bottles to 1 bar overpressure with\
    \ sterile 80% H2 and 20%\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\": \"Trace-stock\
    \ pH\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"Adjust pH to 1.0 with HCl.\",\n        \"decision\": \"correct\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"Adjust pH to 1.0 with HCl.\",\n        \"decision\": \"correct\"\n      }\n\
    \    ],\n    \"proposed_source_representation\": {\n      \"pH\": 1,\n      \"\
    stage\": \"Trace element stock only\"\n    },\n    \"rationale\": \"Preserve the\
    \ exact stage and qualifying language. The source pH 1 belongs only to the trace\
    \ stock and must not remain an unscoped root-medium adjustment.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\",\n        \"\
    source_locator\": \"Pages 1–2, Trace-stock pH\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 1.0 with HCl.\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\": \"Typed\
    \ main pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.0,\n        \"\
    decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"pH\": 7,\n      \"scope\": \"Main mixture, distinct from trace pH\
    \ 1\"\n    },\n    \"rationale\": \"Retain the supported main value with its source\
    \ stage and conditional later readjustment.\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"dsmz796\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 1, main preparation\",\n        \"exact_source_quote\"\
    : \"20% CO2 gas mixture to achieve a medium pH of 7.0.\",\n        \"snapshot_sha256\"\
    : \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\",\n    \
    \    \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\": \"Trace\
    \ HCl titration quantity\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : null,\n        \"decision\": \"not_quantified\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Stock prepared in 1000 ml; added at 1 ml per litre of medium. Composition\
    \ and volume from MediaDive (#150).\",\n        \"decision\": \"not_quantified\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"reagent\"\
    : \"HCl\",\n      \"fixed_amount\": null\n    },\n    \"rationale\": \"The source\
    \ states a pH target, not an HCl amount or strength; no fixed dose is invented.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz796\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium796.pdf\"\
    ,\n        \"source_locator\": \"Page 2, trace final sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 1.0 with HCl.\",\n        \"snapshot_sha256\": \"e0fdc2a0e22fe31b9060a715ec01a69780ba0f517bfbf33a49697e86d7cc6f22\"\
    ,\n        \"parsed_text_sha256\": \"824ded9100bc4f78d3c4c608147f81bbc380157c70c8382cf0a458a136a08b99\"\
    ,\n        \"accessed_at\": \"2026-10-21T17:04:22.523340Z\"\n      }\n    ]\n\
    \  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '23 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 23/23
    primary and 22/23 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131361
  - chebi131527
  - chebi26710
  - chebi31206
  - chebi31440
  - chebi32139
  - chebi32312
  - chebi32588
  - chebi32954
  - chebi33118
  - chebi53503
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76181
  - chebi76209
  - chebi86149
  - chebi86158
  - chebi86345
  - chebi86368
  - chebi86465
  - chebi86477
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 23: primary 100.00%;
    secondary 95.65%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 18 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact DSMZ accession and maintained owner
  outcome: supported
  summary: The generated target and exact archaeal owner share CultureMech:001940
    and DSMZ 796. The owner records a later four-component stock-nesting event, while
    the generated target remains fully flattened; this recorded local chronology does
    not authenticate unavailable historical API bytes.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - record
  - owner-0
  - primary
  - history-metadata
- assessment_id: forms
  area: grounding
  topic: Salt/hydrate support and ontology internal tension
  outcome: concern
  summary: Neutral CHEBI:8806 does not represent the explicit sodium-resazurin salt.
    Source K2HPO4 is trihydrate, whereas CHEBI:131527 has an anhydrous formula/structure
    despite a trihydrate synonym; that internal tension requires exact-form resolution,
    not a synonym-only assurance. Source nickel ammonium sulfate hydration is unspecified,
    so CHEBI:86149 hexahydrate is not established but is not proven false. Sodium
    acetate hydration is likewise unspecified. Other explicit hydrates match captured
    term formulae.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - primary
  - chebi8806
  - chebi131527
  - chebi86149
  - chebi32954
- assessment_id: preparation
  area: completeness
  topic: Main and stock stages
  outcome: concern
  summary: Both layers preserve main gases, examples, conditional pH and explicit
    1 bar overpressure. The trace pH 1 instruction is at the root and lacks its stock
    scope. Fresh sulfite filtration is explicit; the primary gives no numerical autoclave
    cycle. No preparation quantity is recast as a growth condition.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Defined formulation and application scope
  outcome: supported
  summary: The source contains named chemicals and a defined trace stock without an
    undefined extract. DEFINED and LIQUID are consistent, subject to exact supplied-form
    caveats. Title and generic cultivation application establish no new organism-specific
    growth outcome or optimum.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - primary
  - record
- assessment_id: current-writers
  area: provenance
  topic: Current writers and follow-up ownership
  outcome: concern
  summary: The current importer separates primary and stock rows; cleanup avoids summing
    conflicting duplicates. The nesting writer selects name/value matches, and plan_record
    returns early when solutions already exist; rerunning it is not proof of a complete
    repair for this owner with four nested components. Reassess the full maintained
    stock and source-stage fields, preserve the historical event and regenerate only
    after authorized corrections.
  target_ids:
  - CultureMech:001940
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
  - current-code-3
findings:
- finding_id: f1
  issue_key: culturemech.001940.incomplete-stock-restoration
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock flattening remains after a partial owner repair
  description: The target has 23 direct components; the owner has 19 direct and four
    nested trace components. Nine of thirteen trace solutes remain direct or combined
    with main NaCl/calcium, and source stock/water boundaries are incomplete. Main
    g/L rates lack a verified final-volume basis.
  target_ids:
  - CultureMech:001940
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
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
  issue_key: culturemech.001940.trace-ph-at-root
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Trace pH 1 is represented as a root-medium adjustment
  description: preparation_steps[2] in both layers contains the trace-stock pH 1 instruction
    without a stock boundary, while the main medium is pH 7. This scope error persists
    despite later partial nesting.
  target_ids:
  - CultureMech:001940
  field_paths:
  - preparation_steps[2]
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
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
  issue_key: culturemech.001940.supplied-chemical-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Salt identity and hydrate assertions require source-specific correction
  description: The explicit sodium-resazurin salt is linked to neutral resazurin.
    The phosphate trihydrate is linked to an ontology entry with anhydrous structure
    but a conflicting hydrate synonym. Nickel-salt and acetate hydrate qualifiers
    remain unestablished rather than disproven.
  target_ids:
  - CultureMech:001940
  field_paths:
  - ingredients[5].term
  - ingredients[5].mediaingredientmech_chebi_term
  - ingredients[7].term
  - ingredients[13].term
  evidence_ids:
  - primary
  - chebi8806
  - chebi131527
  - chebi86149
  - chebi32954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
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
  description: Reconstruct all thirteen trace solutes and source water, separate main
    and stock contributions and preserve the 1 mL receiving amount. Retain the four
    correctly nested identities while qualifying unsupported rate bases; do not treat
    an existing solution node as proof of completeness.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001940
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
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
  description: Move or explicitly qualify this instruction as trace-stock preparation,
    preserving unquantified HCl and the existing main gas/pH stages. Keep the complete
    source scope when regenerating.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001940
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
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
  description: Resolve the explicit sodium salt and phosphate hydrate with exact authoritative
    evidence, preserving the ontology tension. Qualify unresolved nickel/acetate hydration
    without guessing replacement IDs or molecular-weight conversions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001940
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml
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
- Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary
  exists; historical provider normalization remains unauthenticated, without preventing
  the bounded primary comparison.
- Exact optional MediaDive attempt returned HTTP 503. Complete current DSMZ primary
  exists; historical provider normalization remains unauthenticated, without preventing
  the bounded primary comparison.
- Listed main liquids sum to 1003.5 mL before further unquantified stock volumes.
  Neither that sum nor the source 1000 mL water establishes final main volume or the
  historical 1.003 L normalization.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-031
- generated-medium
```
