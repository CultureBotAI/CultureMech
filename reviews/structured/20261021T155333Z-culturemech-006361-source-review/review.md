# Source and formulation review: anaerofilum_medium (CultureMech:006361)

- Review: 20261021T155333Z-culturemech-006361-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T15:43:30Z
- Finished UTC: 2026-10-21T15:53:33Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 719 and the two maintained owners identify ANAEROFILUM medium, but an unrelated LB expansion replaces the source fatty-acid component, and stock recipes are flattened as direct concentrations. Main normalization lacks a verified final-volume basis. Sodium-resazurin and nickel-hydrate groundings and lost preparation scope require curation; exact historical provider correspondence remains limited.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 274; batch 028 item 4 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-seven task batches contain 270 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 273 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006361 | data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml | generated | anaerofilum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006361 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006361 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/274/strict.tsv |
| validate-terms | passed | True | CultureMech:006361 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006361 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006361 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Required source assembly/denominator clarification | unavailable | True | CultureMech:006361 | The complete current primary is available, but it supplies no main final-volume statement or late-stock volumes; both current719 API attempts failed 503. Required authentication of the historical 1.023 L normalization and exact assembled final rates remains unavailable. Source-stage masses and confirmed identity defects are supported; partial scope is not based solely on optional KOMODO access failures. |
| Exact source content access: mediadive719api | unavailable | False | CultureMech:006361 | Preserved access limitation for mediadive719api: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: mediadive719apiRetry | unavailable | False | CultureMech:006361 | Preserved access limitation for mediadive719apiRetry: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: komodo719detail | unavailable | False | CultureMech:006361 | Preserved access limitation for komodo719detail: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: komodo719actual | unavailable | False | CultureMech:006361 | Preserved access limitation for komodo719actual: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: solution209 | unavailable | False | CultureMech:006361 | Preserved access limitation for solution209: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: solution5861 | unavailable | False | CultureMech:006361 | Preserved access limitation for solution5861: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: laboratoryNotes | unavailable | False | CultureMech:006361 | Preserved access limitation for laboratoryNotes: None. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: sigmaL3522 | unavailable | False | CultureMech:006361 | Preserved access limitation for sigmaL3522: None. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| Exact source content access: bd244520 | unavailable | False | CultureMech:006361 | Preserved access limitation for bd244520: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006361.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006361.

44 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.5,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "KH2PO4 0.50 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "MgSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.4,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "MgSO4 x 7 H2O 0.40 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.4,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaCl 0.40 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "NH4Cl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.391007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.4,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NH4Cl 0.40 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "CaCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.0488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 0.05,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "CaCl2 x 2 H2O 0.05 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.977517",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.977517",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.977517",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 1,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Yeast extract 1.00 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Na-acetate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.977517",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.977517",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.977517",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 1,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na-acetate 1.00 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Na-formate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.95503",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.95503",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.95503",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main batch",
      "source_mass_g": 2,
      "main_final_volume": null
    },
    "rationale": "Restore the explicit source batch amount and distinguish the existing g/L normalization. Stored values approximate division by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock volumes, and neither sum is an explicit finished volume. Do not substitute a guessed denominator.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na-formate 2.00 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Sodium resazurin stock contribution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.000488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.000488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.000488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stock_dose_ml": 0.5,
      "stock_strength": "0.1% w/v",
      "receiving_mass_g": 0.0005,
      "final_g_per_l": null
    },
    "rationale": "0.1 g per 100 mL times 0.5 mL gives 0.0005 g per receiving batch, not a verified final g/L. Preserve sodium-salt identity and source stock dose.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "NaHCO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3.91007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3.91007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "3.91007",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main receiving batch; separate late stocks for glucose/cysteine/sulfide",
      "mass_g": 4,
      "late_stock_strength_and_volume": null,
      "final_g_per_l": null
    },
    "rationale": "Retain the batch contribution and explicit preparation order; the separate-stock volumes are not quantified. Existing final g/L cannot be authenticated by the unavailable provider graph.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "NaHCO3 4.00 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q11",
    "component_or_context": "D-Glucose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "4.88759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "4.88759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "4.88759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main receiving batch; separate late stocks for glucose/cysteine/sulfide",
      "mass_g": 5,
      "late_stock_strength_and_volume": null,
      "final_g_per_l": null
    },
    "rationale": "Retain the batch contribution and explicit preparation order; the separate-stock volumes are not quantified. Existing final g/L cannot be authenticated by the unavailable provider graph.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "D-Glucose 5.00 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q12",
    "component_or_context": "L-Cysteine HCl x H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main receiving batch; separate late stocks for glucose/cysteine/sulfide",
      "mass_g": 0.5,
      "late_stock_strength_and_volume": null,
      "final_g_per_l": null
    },
    "rationale": "Retain the batch contribution and explicit preparation order; the separate-stock volumes are not quantified. Existing final g/L cannot be authenticated by the unavailable provider graph.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "L-Cysteine HCl x H2O 0.50 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Na2S x 9 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.488759",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "main receiving batch; separate late stocks for glucose/cysteine/sulfide",
      "mass_g": 0.5,
      "late_stock_strength_and_volume": null,
      "final_g_per_l": null
    },
    "rationale": "Retain the batch contribution and explicit preparation order; the separate-stock volumes are not quantified. Existing final g/L cannot be authenticated by the unavailable provider graph.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main table",
        "exact_source_quote": "Na2S x 9 H2O 0.50 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q14",
    "component_or_context": "SL-10 HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 10,
      "unit": "ml",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. The source 25% has no stated mass/volume basis; stored 2.5 g/L is not justified by 10 mL of that reagent. No density or molarity is inferred.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "HCl (25%) 10.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q15",
    "component_or_context": "SL-10 FeCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 1.5,
      "unit": "g",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "FeCl2 x 4 H2O 1.50 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q16",
    "component_or_context": "SL-10 ZnCl2",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 70,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "ZnCl2 70.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q17",
    "component_or_context": "SL-10 MnCl2 x 4 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 100,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "MnCl2 x 4 H2O 100.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q18",
    "component_or_context": "SL-10 H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.006",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 6,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "H3BO3 6.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q19",
    "component_or_context": "SL-10 CoCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.19",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 190,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "CoCl2 x 6 H2O 190.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q20",
    "component_or_context": "SL-10 CuCl2 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.002",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 2,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "CuCl2 x 2 H2O 2.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q21",
    "component_or_context": "SL-10 NiCl2 x 6 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "0.024",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 24,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "NiCl2 x 6 H2O 24.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q22",
    "component_or_context": "SL-10 Na2MoO4 x 2 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.036",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10 stock",
      "amount": 36,
      "unit": "mg",
      "final_makeup_ml": 1000,
      "receiving_dose_ml": 1
    },
    "rationale": "These quantities belong to the stock and must not remain direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 SL-10 subsection",
        "exact_source_quote": "Na2MoO4 x 2 H2O 36.00 mg",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q23",
    "component_or_context": "Isobutyric acid in fatty stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "23",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "23",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "23",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "fatty-acid stock",
      "volume_ml": 23,
      "main_stock_dose_ml": 20,
      "mass_or_final_concentration": null
    },
    "rationale": "The source gives millilitres of liquid acid, not grams per liter. No density, mass conversion or measured finished stock volume is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty acid mixture",
        "exact_source_quote": "Isobutyric acid 23.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q24",
    "component_or_context": "Valeric acid in fatty stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "27",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "27",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "27",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "fatty-acid stock",
      "volume_ml": 27,
      "main_stock_dose_ml": 20,
      "mass_or_final_concentration": null
    },
    "rationale": "The source gives millilitres of liquid acid, not grams per liter. No density, mass conversion or measured finished stock volume is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty acid mixture",
        "exact_source_quote": "Valeric acid 27.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q25",
    "component_or_context": "Isovaleric acid in fatty stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "27",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "27",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "27",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "fatty-acid stock",
      "volume_ml": 27,
      "main_stock_dose_ml": 20,
      "mass_or_final_concentration": null
    },
    "rationale": "The source gives millilitres of liquid acid, not grams per liter. No density, mass conversion or measured finished stock volume is supplied.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty acid mixture",
        "exact_source_quote": "Isovaleric acid 27.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q26",
    "component_or_context": "Extraneous LB constituent: Tryptone",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "action": "remove the separately identified LB-expanded node from this recipe; preserve genuine same-labelled main yeast and salt",
      "replacement_source_component": "DL-2-Methylbutyric acid",
      "source_volume_ml": 27,
      "stage": "fatty-acid stock"
    },
    "rationale": "The exact recipe supports the fatty acid instead of this commercial-product expansion. This does not set the extraneous ingredient amount to zero, merge genuine duplicate-labelled inputs, or transfer a JCM-specific repair.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty-acid stock",
        "exact_source_quote": "DL-2-Methylbutyric acid 27.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q27",
    "component_or_context": "Extraneous LB constituent: Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "5.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "action": "remove the separately identified LB-expanded node from this recipe; preserve genuine same-labelled main yeast and salt",
      "replacement_source_component": "DL-2-Methylbutyric acid",
      "source_volume_ml": 27,
      "stage": "fatty-acid stock"
    },
    "rationale": "The exact recipe supports the fatty acid instead of this commercial-product expansion. This does not set the extraneous ingredient amount to zero, merge genuine duplicate-labelled inputs, or transfer a JCM-specific repair.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty-acid stock",
        "exact_source_quote": "DL-2-Methylbutyric acid 27.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q28",
    "component_or_context": "Extraneous LB constituent: Sodium chloride",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "10.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "action": "remove the separately identified LB-expanded node from this recipe; preserve genuine same-labelled main yeast and salt",
      "replacement_source_component": "DL-2-Methylbutyric acid",
      "source_volume_ml": 27,
      "stage": "fatty-acid stock"
    },
    "rationale": "The exact recipe supports the fatty acid instead of this commercial-product expansion. This does not set the extraneous ingredient amount to zero, merge genuine duplicate-labelled inputs, or transfer a JCM-specific repair.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty-acid stock",
        "exact_source_quote": "DL-2-Methylbutyric acid 27.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q29",
    "component_or_context": "Missing DL-2-methylbutyric acid",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "fatty-acid stock",
      "volume_ml": 27,
      "identifier": null
    },
    "rationale": "Restore the literal acid name and volume in the stock without inventing an ontology ID or a density conversion.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty-acid stock",
        "exact_source_quote": "DL-2-Methylbutyric acid 27.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q30",
    "component_or_context": "Ferrous sulfate stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "ferrous-sulfate stock",
      "mass_g": 1,
      "solvent": "0.1 N H2SO4",
      "solvent_volume_ml": 1000,
      "main_dose_ml": 2,
      "main_strength": "0.1% w/v"
    },
    "rationale": "The 1 g stock input and its explicitly named strength do not belong as 1 g/L direct main ingredient; retain the 2 mL receiving dose separately.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 ferrous-sulfate stock",
        "exact_source_quote": "FeSO4 x 7 H2O 1.00 g",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q31",
    "component_or_context": "Sulfuric-acid stock solvent",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "ferrous-sulfate stock solvent",
      "volume_ml": 1000,
      "normality": 0.1
    },
    "rationale": "1000 mL of 0.1 N solution is not 1000 g/L sulfuric acid; do not infer a mass or molarity conversion.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 ferrous-sulfate stock",
        "exact_source_quote": "H2SO4 (0.1 N) 1000.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q32",
    "component_or_context": "Main water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "main",
      "water_ml": 1000
    },
    "rationale": "Add a separate source-stage representation. Listed solvent volumes and liquid sums do not independently establish the main finished volume.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Exact named main/stock table row",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q33",
    "component_or_context": "SL-10 water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "water_ml": 990,
      "final_makeup_ml": 1000
    },
    "rationale": "Add a separate source-stage representation. Listed solvent volumes and liquid sums do not independently establish the main finished volume.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Exact named main/stock table row",
        "exact_source_quote": "Distilled water 990.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q34",
    "component_or_context": "Fatty stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "stage": "fatty-acid mixture",
      "water_ml": 896
    },
    "rationale": "Add a separate source-stage representation. Listed solvent volumes and liquid sums do not independently establish the main finished volume.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Exact named main/stock table row",
        "exact_source_quote": "Distilled water 896.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q35",
    "component_or_context": "SL-10 receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 1
    },
    "rationale": "Add a separate source-stage representation. Listed solvent volumes and liquid sums do not independently establish the main finished volume.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Exact named main/stock table row",
        "exact_source_quote": "Trace element solution SL-10 1.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q36",
    "component_or_context": "Fatty stock receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 20
    },
    "rationale": "Add a separate source-stage representation. Listed solvent volumes and liquid sums do not independently establish the main finished volume.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Exact named main/stock table row",
        "exact_source_quote": "Fatty acid mixture 20.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q37",
    "component_or_context": "Ferrous stock receiving dose",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "dose_ml": 2,
      "strength": "0.1% w/v"
    },
    "rationale": "Add a separate source-stage representation. Listed solvent volumes and liquid sums do not independently establish the main finished volume.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Exact named main/stock table row",
        "exact_source_quote": "FeSO4 x 7 H2O solution (0.1% w/v) 2.00 ml",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q38",
    "component_or_context": "Main gas mixture",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of complete medium and adjust to 6.8 - 7.0, if necessary.",
        "decision": "evidence_only"
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
    "rationale": "Preserve exact stage and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner context and move stock-only owner instructions into their stock containers. Gas basis is not expanded beyond the printed statement.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main/SL-10 or page 2 fatty-stock preparation",
        "exact_source_quote": "with 80% N2 and 20% CO2 gas mixture for 30 - 45 min",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q39",
    "component_or_context": "Late-stock gas",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of complete medium and adjust to 6.8 - 7.0, if necessary.",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "glucose/cysteine/sulfide stocks",
      "N2_percent": 100
    },
    "rationale": "Preserve exact stage and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner context and move stock-only owner instructions into their stock containers. Gas basis is not expanded beyond the printed statement.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main/SL-10 or page 2 fatty-stock preparation",
        "exact_source_quote": "stock solutions prepared under 100% N2 gas.",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q40",
    "component_or_context": "Final main pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve ingredients except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of complete medium and adjust to 6.8 - 7.0, if necessary.",
        "decision": "evidence_only"
      },
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 6.8,
          "max": 7.0
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "stage": "complete medium",
      "pH": [
        6.8,
        7
      ],
      "conditional": true
    },
    "rationale": "Preserve exact stage and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner context and move stock-only owner instructions into their stock containers. Gas basis is not expanded beyond the printed statement.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main/SL-10 or page 2 fatty-stock preparation",
        "exact_source_quote": "and adjust to 6.8 - 7.0, if necessary.",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q41",
    "component_or_context": "SL-10 make-up",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "SL-10",
      "final_makeup_ml": 1000
    },
    "rationale": "Preserve exact stage and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner context and move stock-only owner instructions into their stock containers. Gas basis is not expanded beyond the printed statement.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main/SL-10 or page 2 fatty-stock preparation",
        "exact_source_quote": "make up to 1000.00 ml.",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q42",
    "component_or_context": "Fatty stock pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Adjust pH to 7.5 with concentrated NaOH.",
        "decision": "correct"
      }
    ],
    "proposed_source_representation": {
      "stage": "fatty stock",
      "pH": 7.5,
      "NaOH_dose": null
    },
    "rationale": "Preserve exact stage and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner context and move stock-only owner instructions into their stock containers. Gas basis is not expanded beyond the printed statement.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main/SL-10 or page 2 fatty-stock preparation",
        "exact_source_quote": "Adjust pH to 7.5 with concentrated NaOH.",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q43",
    "component_or_context": "Unquantified stock titrant",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "solutions",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": {
      "reagent": "concentrated NaOH",
      "dose": null
    },
    "rationale": "Source titrant is explicit but has no fixed dose or numeric strength.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 2 fatty stock",
        "exact_source_quote": "Adjust pH to 7.5 with concentrated NaOH.",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  },
  {
    "quantity_id": "q44",
    "component_or_context": "Unspecified autoclave cycle",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Dissolve ingredients except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of complete medium and adjust to 6.8 - 7.0, if necessary."
          },
          {
            "step_number": 2,
            "action": "DISSOLVE",
            "description": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."
          },
          {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.5 with concentrated NaOH."
          },
          {
            "step_number": 4,
            "action": "MIX",
            "description": "The ferrous sulfate solution is not stable and should be freshly prepared."
          }
        ],
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": {
      "method": "autoclave",
      "temperature": null,
      "duration": null
    },
    "rationale": "The method and ordering are stated; a numeric cycle is not. Restore the source procedure without inventing time or temperature.",
    "source_snippets": [
      {
        "source_key": "dsmz719",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf",
        "source_locator": "Page 1 main preparation",
        "exact_source_quote": "tubes or serum vials and autoclave.",
        "snapshot_sha256": "dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77",
        "parsed_text_sha256": "43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470"
      }
    ]
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:006361.

28 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 29/30 primary and 25/30 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 30: primary 96.67%; secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006361.

23 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### DSMZ719, KOMODO719 and maintained ownership

identity: concern. Targets: CultureMech:006361.

The exact collection accession, catalog identity and two stable owner IDs agree, but the LB product notes and three expanded constituents conflict with the actual recipe. The stock DL-2-methylbutyric acid is missing. Same ingredient signatures reflect the same corruption, not independently supported recipe identity.

### All direct amounts and source-only stock quantities

evidence: concern. Targets: CultureMech:006361.

No ingredient evidence objects are attached in the target or either owner. Exact primary snippets support stage-specific batch amounts and corrections; current unavailable APIs cannot authenticate the historical normalized denominator. Historical local reports remain derivative leads, not retrieved provider bytes.

### Salt, hydrate, mixture and supplied-form limits

grounding: concern. Targets: CultureMech:006361.

Source sodium resazurin conflicts with neutral CHEBI:8806 C12H7NO4; source nickel chloride hexahydrate conflicts with CHEBI:34887 Cl2Ni. Sodium acetate is not hydrate-qualified in the source while CHEBI:32954 is anhydrous, so that specificity remains unverified. MICRO:0000182 and FOODON:03315426 correctly label tryptone and yeast extract but do not justify their LB-derived inclusion or supplier composition claims. Genuine main yeast extract remains distinct.

### Main and stock instructions across owner layers

completeness: concern. Targets: CultureMech:006361.

The target and KOMODO owner omit the main anaerobic preparation and final-pH range retained in the DSMZ owner. That owner also retains stock-only SL-10 make-up, fatty-stock titration and fresh ferrous-stock warning at main root. Restore stage containers and all exact qualifiers; no numeric sterilization cycle or late-stock volumes are supplied.

### Composition and biological claim limits

scope: concern. Targets: CultureMech:006361.

COMPLEX/UNDEFINED and LIQUID remain compatible with the genuine yeast-extract formula. Aerobic: Yes is imported catalog metadata and conflicts with the explicit anoxic preparation if treated as a recipe condition. Neither generic cultivation nor the title or supplier ingredient roles establishes a new organism-growth claim; no target organism CURIE or graph match is asserted.

### Current writers and maintained input follow-up

provenance: concern. Targets: CultureMech:006361.

Current MediaDive parsing separates first-solution ingredients and stock additions, while collecting preparation steps from solution sections. The current resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific repair is context only. Fix the two maintained719 owners with their own exact evidence before separately authorized regeneration.

## Findings

### f1: Unrelated LB constituents replace a fatty-acid component

blocker / open / confirmed; issue key: culturemech.006361.wrong-lb-replacement.

All three local layers contain LB-labelled tryptone 10, yeast extract 5 and sodium chloride 10 g/L, plus commercial-product metadata, while exact719 specifies DL-2-methylbutyric acid 27 mL in its fatty stock. Genuine main yeast extract and NaCl must be retained separately.

### f2: Stock compositions and liquid inputs are represented as main g/L

blocker / open / confirmed; issue key: culturemech.006361.stock-and-unit-collapse.

SL-10, fatty acids and the ferrous-sulfate solvent are flattened; acid mL and1000 mL 0.1 N sulfuric solution became g/L. Main rates depend on an unverified denominator. Stock doses/water and their distinct bases are absent.

### f3: Sodium resazurin and nickel hydrate have incompatible primary mappings

major / open / confirmed; issue key: culturemech.006361.form-grounding.

The sodium dye is mapped to neutral resazurin, and nickel hexahydrate to anhydrous nickel dichloride in primary and current secondary slots. Valid labels do not resolve supplied-form mismatch; sodium-acetate hydration is separately unverified.

### f4: Main preparation is lost and stock preparation is detached

major / open / confirmed; issue key: culturemech.006361.preparation-loss.

The DSMZ owner retains the complete main procedure and pH range, but target/KOMODO omit them. Stock-only make-up, titration and instability warning must move with the restored stocks; imported aerobic metadata must not replace the explicit anoxic preparation.

### f5: Import history contains malformed or timezone-naive timestamps

minor / open / confirmed; issue key: culturemech.006361.historical-timestamps.

The KOMODO-derived target and owner retain malformed .fZ import timestamps and naive enrichment timestamps. These are historical provenance limitations, not permission to rewrite events.

## Recommended Actions And Acceptance Checks

### a1

Remove only the unsupported LB expansion and supersede its active product claims in both maintained owners; restore the source fatty-acid input and evidence without inventing an identifier. Preserve history append-only and genuine same-labelled main components.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore main batch and three stock scopes, explicit receiving doses, solvent units and supported strengths in both owners. Preserve missing final-volume/density/percentage-basis limits and attach per-claim evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Verify source-compatible salt/hydrate identifiers and assess secondary links independently. Qualify acetate specificity rather than choosing an unprinted hydrate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Preserve main ordering and all source gas/pH qualifiers, restore missing layers, and relocate stock instructions. Do not invent a numerical autoclave cycle or infer growth from atmosphere.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Preserve old events and append a dated clarification with exact evidence when curation is authorized; fix future writers separately.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/anaerofilum_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch028/274/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch028/274/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml:1:id: CultureMech:006361<br>./data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml:1:id: CultureMech:006361<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/274/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 45 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-owner-context | /private/tmp/culturemech-review-work-batch028/source-preflight-bound/274/evidence-context-original.json; Complete target and maintained owner; source and identifier search contexts | context_only | Whole fresh target and owner read; all frozen local-record objects equal the fresh inspected YAML. Source interpretations are independently checked against actual bound raw/text bytes. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf; Pages 1–2, complete main formula and three explicitly named stock subsections | supports | The exact DSMZ 719 recipe supplies main batch masses, stock doses, three stock compositions and separate preparation. It contains DL-2-methylbutyric acid in the fatty-acid stock and no LB product. No main final-volume statement is printed. |
| parent-sl10 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; Trace element solution SL-10 subsection only | supports | The cross-referenced parent is scoped to SL-10. The child719 subsection remains the direct amount authority; no parent basal formula or unprinted acid percentage basis transfers. |
| parent-fatty-iron | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf; Fatty acid mixture and ferrous-sulfate solution subsections only | supports | Only the two stocks explicitly referenced by DSMZ719 are relevant; no parent receiving medium or cultivation assertion transfers. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch028/274/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi16135 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16135; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16135 resolves to isobutyric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17418 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17418; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17418 resolves to valeric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17634; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17634 resolves to D-glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi28484 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28484; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:28484 resolves to isovaleric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32954 resolves to sodium acetate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:53503 resolves to cobalt chloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:62965 resolves to sodium formate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | FOODON:03315426 resolves to yeast extract. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| micro0000182 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | MICRO:0000182 resolves to tryptone. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:16135": [{"label": "Isobutyric acid", "match_type": "preferred_term", "identifier": "CHEBI:16135", "preferred_term": "Isobutyric acid", "ontology_id": "CHEBI:16135", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17418": [{"label": "Valeric acid", "match_type": "preferred_term", "identifier": "CHEBI:17418", "preferred_term": "Valeric acid", "ontology_id": "CHEBI:17418", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term", "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28484": [{"label": "Isovaleric acid", "match_type": "preferred_term", "identifier": "CHEBI:28484", "preferred_term": "Isovaleric acid", "ontology_id": "CHEBI:28484", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term", "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:53503": [{"label": "Cobalt chloride hexahydrate", "match_type": "preferred_term", "identifier": "CHEBI:53503", "preferred_term": "Cobalt chloride hexahydrate", "ontology_id": "CHEBI:53503", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:62965": [{"label": "Na-formate", "match_type": "preferred_term", "identifier": "CHEBI:62965", "preferred_term": "Na-formate", "ontology_id": "CHEBI:62965", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml; data/normalized_yaml/bacterial/anaerofilum_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:02.341109"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml", "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value": "2026-02-03T11:19:02.341109"}]}, {"input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml", "events": 7, "timestamp_issues": []}] |
| current-code-0 | src/culturemech/import/mediadive_importer.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive parsing separates first-solution ingredients and stock additions, while collecting preparation steps from solution sections. The current resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific repair is context only. Fix the two maintained719 owners with their own exact evidence before separately authorized regeneration. |
| current-code-1 | src/culturemech/enrich/dsmz_resolver.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive parsing separates first-solution ingredients and stock additions, while collecting preparation steps from solution sections. The current resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific repair is context only. Fix the two maintained719 owners with their own exact evidence before separately authorized regeneration. |
| current-code-2 | src/culturemech/merge/formulation.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive parsing separates first-solution ingredients and stock additions, while collecting preparation steps from solution sections. The current resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific repair is context only. Fix the two maintained719 owners with their own exact evidence before separately authorized regeneration. |
| current-code-3 | scripts/repair_jcm_lb_acids.py; Current scoped functions read; supplemental current code hash; no historical-version inference | context_only | Current MediaDive parsing separates first-solution ingredients and stock additions, while collecting preparation steps from solution sections. The current resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific repair is context only. Fix the two maintained719 owners with their own exact evidence before separately authorized regeneration. |
| mediadive719api-attempt | https://mediadive.dsmz.de/rest/medium/719; Preserved exact public retrieval result | context_only | Preserved access limitation for mediadive719api: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| mediadive719apiRetry-attempt | https://mediadive.dsmz.de/rest/medium/719; Preserved exact public retrieval result | context_only | Preserved access limitation for mediadive719apiRetry: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| komodo719detail-attempt | https://komodo.modelseed.org/servlet/Komodo?MediaInfo=719; Preserved exact public retrieval result | context_only | Preserved access limitation for komodo719detail: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| komodo719actual-attempt | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=719; Preserved exact public retrieval result | context_only | Preserved access limitation for komodo719actual: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| solution209-attempt | https://mediadive.dsmz.de/rest/solution/209; Preserved exact public retrieval result | context_only | Preserved access limitation for solution209: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| solution5861-attempt | https://mediadive.dsmz.de/rest/solution/5861; Preserved exact public retrieval result | context_only | Preserved access limitation for solution5861: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| laboratoryNotes-attempt | https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/; Preserved exact public retrieval result | context_only | Preserved access limitation for laboratoryNotes: None. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| sigmaL3522-attempt | https://www.sigmaaldrich.com/US/en/product/sigma/l3522?context=product; Preserved exact public retrieval result | context_only | Preserved access limitation for sigmaL3522: None. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |
| bd244520-attempt | https://www.bd.com/en-us/products-and-solutions/products/product-page.244520; Preserved exact public retrieval result | context_only | Preserved access limitation for bd244520: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The complete current primary is available, but it supplies no main final-volume statement or late-stock volumes; both current719 API attempts failed 503. Required authentication of the historical 1.023 L normalization and exact assembled final rates remains unavailable. Source-stage masses and confirmed identity defects are supported; partial scope is not based solely on optional KOMODO access failures.
- Preserved access limitation for mediadive719api: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for mediadive719apiRetry: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for komodo719detail: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for komodo719actual: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for solution209: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for solution5861: 503. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for laboratoryNotes: None. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for sigmaL3522: None. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- Preserved access limitation for bd244520: 403. No unavailable product or provider response is treated as formulation evidence; DSMZ719 directly establishes the current recipe scope.
- No supplier composition was substituted for the exact collection recipe. Current primary disagreements are not assigned a chronology relative to historical provider data.
- Exact source quantities are preserved without assuming a main one-liter final volume, acid density, unqualified 25% basis, or current API content that could not be retrieved.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T155333Z-culturemech-006361-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: anaerofilum_medium (CultureMech:006361)'
started_at: '2026-10-21T15:43:30Z'
finished_at: '2026-10-21T15:53:33Z'
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
summary: DSMZ 719 and the two maintained owners identify ANAEROFILUM medium, but an
  unrelated LB expansion replaces the source fatty-acid component, and stock recipes
  are flattened as direct concentrations. Main normalization lacks a verified final-volume
  basis. Sodium-resazurin and nickel-hydrate groundings and lost preparation scope
  require curation; exact historical provider correspondence remains limited.
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
  - path: data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
    sha256: 8a8874a83f00e23b1dc61da29d953353c5ddb4bafb65092dc7b5c5dd32e8db78
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    sha256: e2e54bf5159a521e56c5c186cc58a62a930f0503597a07808623f09b7bd87241
    role: context
  - path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
    sha256: 038468d842f0847bb150ae789c30462b691642f4fb08e576fc8d54a0c40e12f2
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/anaerofilum_medium.yaml.md
    sha256: 553631982378687548bed528dbee3ce1704f707a40b23ccaa8fd2eddd6f3bd3c
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
  - path: scripts/repair_jcm_lb_acids.py
    sha256: d0369c380e17c91eca520659c5364b7ae5d2c5894036a98f7b23b176f188ff01
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
  selection: Task review 274; batch 028 item 4 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-seven task batches
    contain 270 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 273 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006361
targets:
- target_id: CultureMech:006361
  path: data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  label: anaerofilum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch028/274/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/274/strict.tsv"
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006361
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
  - CultureMech:006361
- check_id: source-assembly-basis
  name: Required source assembly/denominator clarification
  required: true
  status: unavailable
  summary: The complete current primary is available, but it supplies no main final-volume
    statement or late-stock volumes; both current719 API attempts failed 503. Required
    authentication of the historical 1.023 L normalization and exact assembled final
    rates remains unavailable. Source-stage masses and confirmed identity defects
    are supported; partial scope is not based solely on optional KOMODO access failures.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - primary
  - quantity-inventory
- check_id: mediadive719api-source-access
  name: 'Exact source content access: mediadive719api'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for mediadive719api: 503. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - mediadive719api-attempt
- check_id: mediadive719apiRetry-source-access
  name: 'Exact source content access: mediadive719apiRetry'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for mediadive719apiRetry: 503. No unavailable
    product or provider response is treated as formulation evidence; DSMZ719 directly
    establishes the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - mediadive719apiRetry-attempt
- check_id: komodo719detail-source-access
  name: 'Exact source content access: komodo719detail'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for komodo719detail: 403. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - komodo719detail-attempt
- check_id: komodo719actual-source-access
  name: 'Exact source content access: komodo719actual'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for komodo719actual: 403. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - komodo719actual-attempt
- check_id: solution209-source-access
  name: 'Exact source content access: solution209'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for solution209: 503. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - solution209-attempt
- check_id: solution5861-source-access
  name: 'Exact source content access: solution5861'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for solution5861: 503. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - solution5861-attempt
- check_id: laboratoryNotes-source-access
  name: 'Exact source content access: laboratoryNotes'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for laboratoryNotes: None. No unavailable
    product or provider response is treated as formulation evidence; DSMZ719 directly
    establishes the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - laboratoryNotes-attempt
- check_id: sigmaL3522-source-access
  name: 'Exact source content access: sigmaL3522'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for sigmaL3522: None. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - sigmaL3522-attempt
- check_id: bd244520-source-access
  name: 'Exact source content access: bd244520'
  required: false
  status: unavailable
  summary: 'Preserved access limitation for bd244520: 403. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - bd244520-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:56.293361Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch028/274/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:57.651422Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-028/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch028/274/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:43:59.393501Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T15:44:00.450155Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T15:53:28Z'
  support: supports
  summary: './data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml:1:id: CultureMech:006361

    ./data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml:1:id: CultureMech:006361

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/274/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T15:53:28Z'
  support: supports
  summary: 45 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 7e1f03eec40e8bd869e9eda091bbd755e33d41f065bcb0391373587bd6ecaac2
- evidence_id: bound-owner-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/source-preflight-bound/274/evidence-context-original.json
  locator: Complete target and maintained owner; source and identifier search contexts
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Whole fresh target and owner read; all frozen local-record objects equal
    the fresh inspected YAML. Source interpretations are independently checked against
    actual bound raw/text bytes.
  snapshot_sha256: b647e2bcf86054667b7b7220d80020c226ff9bd72e6714289e7282584d8591e1
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf
  locator: Pages 1–2, complete main formula and three explicitly named stock subsections
  accessed_at: '2026-10-21T15:16:37.870762Z'
  support: supports
  summary: The exact DSMZ 719 recipe supplies main batch masses, stock doses, three
    stock compositions and separate preparation. It contains DL-2-methylbutyric acid
    in the fatty-acid stock and no LB product. No main final-volume statement is printed.
  snapshot_sha256: dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77
- evidence_id: parent-sl10
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: Trace element solution SL-10 subsection only
  accessed_at: '2026-10-21T13:20:08.151265Z'
  support: supports
  summary: The cross-referenced parent is scoped to SL-10. The child719 subsection
    remains the direct amount authority; no parent basal formula or unprinted acid
    percentage basis transfers.
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: parent-fatty-iron
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf
  locator: Fatty acid mixture and ferrous-sulfate solution subsections only
  accessed_at: '2026-10-21T15:19:01.122498Z'
  support: supports
  summary: Only the two stocks explicitly referenced by DSMZ719 are relevant; no parent
    receiving medium or cultivation assertion transfers.
  snapshot_sha256: 65295918764de4ed5b73ce773ab4057a7183ecf8bfd7fff0d02393d901b41a2a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch028/274/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7e3f85ae0b428bec0b7ece4b2ffc459503e6200b3226a91450399caf5b4f89e9
- evidence_id: chebi16135
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16135
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.576156Z'
  support: supports
  summary: CHEBI:16135 resolves to isobutyric acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 9066add4e624c1d66e8ed2b31b6d8cd83aee6227fe29e0fe5a7bf1d36fedb4ab
- evidence_id: chebi17418
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17418
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.845270Z'
  support: supports
  summary: CHEBI:17418 resolves to valeric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 6546fe66aa87af53dc1299ff42f673250bf3224d190f83b9b21df72da4eb863b
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
- evidence_id: chebi26836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:29:13.222926Z'
  support: supports
  summary: CHEBI:26836 resolves to sulfuric acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi28484
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28484
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T11:29:08.988065Z'
  support: supports
  summary: CHEBI:28484 resolves to isovaleric acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 2b4dfb8baa01781ecd4134258216b42713d7a04212539eab80e08ba7f10e1a72
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
- evidence_id: chebi62965
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62965
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T09:49:55.570542Z'
  support: supports
  summary: CHEBI:62965 resolves to sodium formate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f36b7c1107922c948bf6387ce77e0468c3fcdf76ce80969b5411b600e051910d
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
- evidence_id: foodon03315426
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:49.388263Z'
  support: supports
  summary: FOODON:03315426 resolves to yeast extract. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: micro0000182
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:37:21.973857Z'
  support: supports
  summary: MICRO:0000182 resolves to tryptone. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T15:53:28Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:16135":
    [{"label": "Isobutyric acid", "match_type": "preferred_term", "identifier": "CHEBI:16135",
    "preferred_term": "Isobutyric acid", "ontology_id": "CHEBI:16135", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:17418": [{"label": "Valeric acid", "match_type":
    "preferred_term", "identifier": "CHEBI:17418", "preferred_term": "Valeric acid",
    "ontology_id": "CHEBI:17418", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17634": [{"label": "D-Glucose", "match_type": "preferred_term", "identifier":
    "CHEBI:17634", "preferred_term": "D-Glucose", "ontology_id": "CHEBI:17634", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type":
    "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id":
    "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:26836": [{"label": "H2SO4", "match_type": "preferred_term",
    "identifier": "CHEBI:26836", "preferred_term": "H2SO4", "ontology_id": "CHEBI:26836",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:28484": [{"label":
    "Isovaleric acid", "match_type": "preferred_term", "identifier": "CHEBI:28484",
    "preferred_term": "Isovaleric acid", "ontology_id": "CHEBI:28484", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32954": [{"label": "Na-acetate", "match_type": "preferred_term",
    "identifier": "CHEBI:32954", "preferred_term": "Na-acetate", "ontology_id": "CHEBI:32954",
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
    "unique"}], "CHEBI:62965": [{"label": "Na-formate", "match_type": "preferred_term",
    "identifier": "CHEBI:62965", "preferred_term": "Na-formate", "ontology_id": "CHEBI:62965",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836":
    [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O",
    "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label":
    "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249",
    "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term":
    "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id":
    "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248":
    [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier":
    "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml;
    data/normalized_yaml/bacterial/anaerofilum_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: '[{"input": "target", "events": 9, "timestamp_issues": [{"index": 0, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue":
    "timezone absent", "value": "2026-02-03T11:19:02.341109"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml",
    "events": 7, "timestamp_issues": [{"index": 0, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 1, "issue": "timezone absent", "value":
    "2026-02-03T11:19:02.341109"}]}, {"input": "data/normalized_yaml/bacterial/anaerofilum_medium.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: current-code-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Current MediaDive parsing separates first-solution ingredients and stock
    additions, while collecting preparation steps from solution sections. The current
    resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly
    guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific
    repair is context only. Fix the two maintained719 owners with their own exact
    evidence before separately authorized regeneration.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: current-code-1
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Current MediaDive parsing separates first-solution ingredients and stock
    additions, while collecting preparation steps from solution sections. The current
    resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly
    guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific
    repair is context only. Fix the two maintained719 owners with their own exact
    evidence before separately authorized regeneration.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: current-code-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Current MediaDive parsing separates first-solution ingredients and stock
    additions, while collecting preparation steps from solution sections. The current
    resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly
    guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific
    repair is context only. Fix the two maintained719 owners with their own exact
    evidence before separately authorized regeneration.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: current-code-3
  kind: record_content
  reference: scripts/repair_jcm_lb_acids.py
  locator: Current scoped functions read; supplemental current code hash; no historical-version
    inference
  accessed_at: '2026-10-21T15:53:28Z'
  support: context_only
  summary: Current MediaDive parsing separates first-solution ingredients and stock
    additions, while collecting preparation steps from solution sections. The current
    resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly
    guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific
    repair is context only. Fix the two maintained719 owners with their own exact
    evidence before separately authorized regeneration.
  snapshot_sha256: d0369c380e17c91eca520659c5364b7ae5d2c5894036a98f7b23b176f188ff01
- evidence_id: mediadive719api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/719
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.967197Z'
  support: context_only
  summary: 'Preserved access limitation for mediadive719api: 503. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive719apiRetry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/719
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.692932Z'
  support: context_only
  summary: 'Preserved access limitation for mediadive719apiRetry: 503. No unavailable
    product or provider response is treated as formulation evidence; DSMZ719 directly
    establishes the current recipe scope.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo719detail-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?MediaInfo=719
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:16:36.485950Z'
  support: context_only
  summary: 'Preserved access limitation for komodo719detail: 403. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  snapshot_sha256: e4e8499f2bf43bfe5a2a1c4acd6f6dedfbc49fcb350dd0de28125b488d354552
- evidence_id: komodo719actual-attempt
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=719
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:00.267098Z'
  support: context_only
  summary: 'Preserved access limitation for komodo719actual: 403. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  snapshot_sha256: 4ba72e6f91daa46748e4690311bfca88f9c7214d6522a332c2f2aa982f686e42
- evidence_id: solution209-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/209
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:20:32.863095Z'
  support: context_only
  summary: 'Preserved access limitation for solution209: 503. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution5861-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5861
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:20:32.863391Z'
  support: context_only
  summary: 'Preserved access limitation for solution5861: 503. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: laboratoryNotes-attempt
  kind: database
  reference: https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:01.238249Z'
  support: context_only
  summary: 'Preserved access limitation for laboratoryNotes: None. No unavailable
    product or provider response is treated as formulation evidence; DSMZ719 directly
    establishes the current recipe scope.'
- evidence_id: sigmaL3522-attempt
  kind: database
  reference: https://www.sigmaaldrich.com/US/en/product/sigma/l3522?context=product
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:01.562357Z'
  support: context_only
  summary: 'Preserved access limitation for sigmaL3522: None. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
- evidence_id: bd244520-attempt
  kind: database
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.244520
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T15:19:01.058548Z'
  support: context_only
  summary: 'Preserved access limitation for bd244520: 403. No unavailable product
    or provider response is treated as formulation evidence; DSMZ719 directly establishes
    the current recipe scope.'
  snapshot_sha256: 38dfcf180ec30997dff235af9872d8523f59a5b01afc0fa4239bf2cf886e4dc7
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 44 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    KH2PO4\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.488759\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.488759\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.488759\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 0.5,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"KH2PO4 0.50 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"MgSO4 x 7 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.391007\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.391007\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.391007\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 0.4,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"MgSO4 x 7 H2O 0.40 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.391007\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.391007\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.391007\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 0.4,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaCl 0.40 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"NH4Cl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.391007\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.391007\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.391007\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 0.4,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NH4Cl 0.40 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"CaCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.0488759\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.0488759\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.0488759\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 0.05,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"CaCl2 x 2 H2O 0.05 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Yeast extract\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.977517\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.977517\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[5].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.977517\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 1,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Yeast extract 1.00 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Na-acetate\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.977517\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.977517\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[6].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.977517\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main batch\",\n      \"source_mass_g\": 1,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na-acetate 1.00 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Na-formate\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.95503\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1.95503\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.95503\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main batch\",\n      \"source_mass_g\": 2,\n      \"main_final_volume\"\
    : null\n    },\n    \"rationale\": \"Restore the explicit source batch amount\
    \ and distinguish the existing g/L normalization. Stored values approximate division\
    \ by 1.023 L; listed liquid inputs sum to 1023.5 mL before unquantified late-stock\
    \ volumes, and neither sum is an explicit finished volume. Do not substitute a\
    \ guessed denominator.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na-formate 2.00 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Sodium resazurin stock contribution\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000488759\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.000488759\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\"\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n       \
    \ \"field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n \
    \         \"value\": \"0.000488759\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_dose_ml\": 0.5,\n      \"stock_strength\": \"0.1% w/v\",\n\
    \      \"receiving_mass_g\": 0.0005,\n      \"final_g_per_l\": null\n    },\n\
    \    \"rationale\": \"0.1 g per 100 mL times 0.5 mL gives 0.0005 g per receiving\
    \ batch, not a verified final g/L. Preserve sodium-salt identity and source stock\
    \ dose.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Sodium resazurin (0.1% w/v) 0.50 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"NaHCO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.91007\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[9].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3.91007\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.91007\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main receiving batch; separate late stocks for glucose/cysteine/sulfide\"\
    ,\n      \"mass_g\": 4,\n      \"late_stock_strength_and_volume\": null,\n   \
    \   \"final_g_per_l\": null\n    },\n    \"rationale\": \"Retain the batch contribution\
    \ and explicit preparation order; the separate-stock volumes are not quantified.\
    \ Existing final g/L cannot be authenticated by the unavailable provider graph.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"NaHCO3 4.00 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"component_or_context\"\
    : \"D-Glucose\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.88759\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[10].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"4.88759\",\n          \"unit\": \"G_PER_L\"\n    \
    \    },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"4.88759\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main receiving batch; separate late stocks for glucose/cysteine/sulfide\"\
    ,\n      \"mass_g\": 5,\n      \"late_stock_strength_and_volume\": null,\n   \
    \   \"final_g_per_l\": null\n    },\n    \"rationale\": \"Retain the batch contribution\
    \ and explicit preparation order; the separate-stock volumes are not quantified.\
    \ Existing final g/L cannot be authenticated by the unavailable provider graph.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"D-Glucose 5.00 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q12\",\n    \"component_or_context\"\
    : \"L-Cysteine HCl x H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.488759\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[11].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.488759\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[11].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.488759\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main receiving batch; separate late stocks for glucose/cysteine/sulfide\"\
    ,\n      \"mass_g\": 0.5,\n      \"late_stock_strength_and_volume\": null,\n \
    \     \"final_g_per_l\": null\n    },\n    \"rationale\": \"Retain the batch contribution\
    \ and explicit preparation order; the separate-stock volumes are not quantified.\
    \ Existing final g/L cannot be authenticated by the unavailable provider graph.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"L-Cysteine HCl x H2O 0.50 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"component_or_context\"\
    : \"Na2S x 9 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.488759\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[12].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.488759\",\n          \"unit\": \"G_PER_L\"\n   \
    \     },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[12].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.488759\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"main receiving batch; separate late stocks for glucose/cysteine/sulfide\"\
    ,\n      \"mass_g\": 0.5,\n      \"late_stock_strength_and_volume\": null,\n \
    \     \"final_g_per_l\": null\n    },\n    \"rationale\": \"Retain the batch contribution\
    \ and explicit preparation order; the separate-stock volumes are not quantified.\
    \ Existing final g/L cannot be authenticated by the unavailable provider graph.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main table\",\n        \"exact_source_quote\"\
    : \"Na2S x 9 H2O 0.50 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"SL-10 HCl\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"amount\": 10,\n      \"unit\"\
    : \"ml\",\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n\
    \    },\n    \"rationale\": \"These quantities belong to the stock and must not\
    \ remain direct main concentrations. The source 25% has no stated mass/volume\
    \ basis; stored 2.5 g/L is not justified by 10 mL of that reagent. No density\
    \ or molarity is inferred.\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"HCl (25%) 10.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"component_or_context\"\
    : \"SL-10 FeCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"amount\": 1.5,\n      \"unit\"\
    : \"g\",\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n \
    \   },\n    \"rationale\": \"These quantities belong to the stock and must not\
    \ remain direct main concentrations. For mg rows, stock g/L is amount/1000 at\
    \ the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch\
    \ input.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"FeCl2 x 4 H2O 1.50 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"component_or_context\"\
    : \"SL-10 ZnCl2\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[15].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[15].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.07\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"SL-10 stock\",\n      \"amount\": 70,\n      \"unit\": \"mg\"\
    ,\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n    },\n\
    \    \"rationale\": \"These quantities belong to the stock and must not remain\
    \ direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit\
    \ 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"ZnCl2 70.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q17\",\n    \"component_or_context\"\
    : \"SL-10 MnCl2 x 4 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10 stock\",\n      \"amount\": 100,\n      \"unit\"\
    : \"mg\",\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n\
    \    },\n    \"rationale\": \"These quantities belong to the stock and must not\
    \ remain direct main concentrations. For mg rows, stock g/L is amount/1000 at\
    \ the explicit 1 L make-up; the 1 mL stock dose is a separate receiving-batch\
    \ input.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"MnCl2 x 4 H2O 100.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\"\
    : \"SL-10 H3BO3\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[17].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.006\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[17].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.006\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"SL-10 stock\",\n      \"amount\": 6,\n      \"unit\": \"mg\"\
    ,\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n    },\n\
    \    \"rationale\": \"These quantities belong to the stock and must not remain\
    \ direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit\
    \ 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"H3BO3 6.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q19\",\n    \"component_or_context\"\
    : \"SL-10 CoCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[18].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.19\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[18].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.19\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"SL-10 stock\",\n      \"amount\": 190,\n      \"unit\": \"mg\"\
    ,\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n    },\n\
    \    \"rationale\": \"These quantities belong to the stock and must not remain\
    \ direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit\
    \ 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"CoCl2 x 6 H2O 190.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"component_or_context\"\
    : \"SL-10 CuCl2 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[19].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.002\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[19].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.002\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"SL-10 stock\",\n      \"amount\": 2,\n      \"unit\": \"mg\"\
    ,\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n    },\n\
    \    \"rationale\": \"These quantities belong to the stock and must not remain\
    \ direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit\
    \ 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"CuCl2 x 2 H2O 2.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"SL-10 NiCl2 x 6 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[20].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.024\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[20].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.024\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"SL-10 stock\",\n      \"amount\": 24,\n      \"unit\": \"mg\"\
    ,\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n    },\n\
    \    \"rationale\": \"These quantities belong to the stock and must not remain\
    \ direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit\
    \ 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"NiCl2 x 6 H2O 24.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q22\",\n    \"component_or_context\"\
    : \"SL-10 Na2MoO4 x 2 H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[21].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.036\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[21].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.036\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"SL-10 stock\",\n      \"amount\": 36,\n      \"unit\": \"mg\"\
    ,\n      \"final_makeup_ml\": 1000,\n      \"receiving_dose_ml\": 1\n    },\n\
    \    \"rationale\": \"These quantities belong to the stock and must not remain\
    \ direct main concentrations. For mg rows, stock g/L is amount/1000 at the explicit\
    \ 1 L make-up; the 1 mL stock dose is a separate receiving-batch input.\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 SL-10 subsection\",\n        \"exact_source_quote\"\
    : \"Na2MoO4 x 2 H2O 36.00 mg\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"component_or_context\"\
    : \"Isobutyric acid in fatty stock\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"23\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"23\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"23\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"fatty-acid stock\",\n      \"volume_ml\": 23,\n      \"\
    main_stock_dose_ml\": 20,\n      \"mass_or_final_concentration\": null\n    },\n\
    \    \"rationale\": \"The source gives millilitres of liquid acid, not grams per\
    \ liter. No density, mass conversion or measured finished stock volume is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty acid mixture\",\n        \"exact_source_quote\"\
    : \"Isobutyric acid 23.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"component_or_context\"\
    : \"Valeric acid in fatty stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"fatty-acid stock\",\n      \"volume_ml\": 27,\n      \"\
    main_stock_dose_ml\": 20,\n      \"mass_or_final_concentration\": null\n    },\n\
    \    \"rationale\": \"The source gives millilitres of liquid acid, not grams per\
    \ liter. No density, mass conversion or measured finished stock volume is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty acid mixture\",\n        \"exact_source_quote\"\
    : \"Valeric acid 27.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"component_or_context\"\
    : \"Isovaleric acid in fatty stock\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"27\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"fatty-acid stock\",\n      \"volume_ml\": 27,\n      \"\
    main_stock_dose_ml\": 20,\n      \"mass_or_final_concentration\": null\n    },\n\
    \    \"rationale\": \"The source gives millilitres of liquid acid, not grams per\
    \ liter. No density, mass conversion or measured finished stock volume is supplied.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty acid mixture\",\n        \"exact_source_quote\"\
    : \"Isovaleric acid 27.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"component_or_context\"\
    : \"Extraneous LB constituent: Tryptone\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[23].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[23].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"action\": \"remove the separately identified LB-expanded node from this\
    \ recipe; preserve genuine same-labelled main yeast and salt\",\n      \"replacement_source_component\"\
    : \"DL-2-Methylbutyric acid\",\n      \"source_volume_ml\": 27,\n      \"stage\"\
    : \"fatty-acid stock\"\n    },\n    \"rationale\": \"The exact recipe supports\
    \ the fatty acid instead of this commercial-product expansion. This does not set\
    \ the extraneous ingredient amount to zero, merge genuine duplicate-labelled inputs,\
    \ or transfer a JCM-specific repair.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty-acid stock\",\n        \"exact_source_quote\"\
    : \"DL-2-Methylbutyric acid 27.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"component_or_context\"\
    : \"Extraneous LB constituent: Yeast extract\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"action\": \"remove the separately identified LB-expanded node from\
    \ this recipe; preserve genuine same-labelled main yeast and salt\",\n      \"\
    replacement_source_component\": \"DL-2-Methylbutyric acid\",\n      \"source_volume_ml\"\
    : 27,\n      \"stage\": \"fatty-acid stock\"\n    },\n    \"rationale\": \"The\
    \ exact recipe supports the fatty acid instead of this commercial-product expansion.\
    \ This does not set the extraneous ingredient amount to zero, merge genuine duplicate-labelled\
    \ inputs, or transfer a JCM-specific repair.\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty-acid stock\",\n        \"exact_source_quote\"\
    : \"DL-2-Methylbutyric acid 27.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"component_or_context\"\
    : \"Extraneous LB constituent: Sodium chloride\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[25].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"10.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[25].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10.0\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"action\": \"remove the separately identified LB-expanded node from this\
    \ recipe; preserve genuine same-labelled main yeast and salt\",\n      \"replacement_source_component\"\
    : \"DL-2-Methylbutyric acid\",\n      \"source_volume_ml\": 27,\n      \"stage\"\
    : \"fatty-acid stock\"\n    },\n    \"rationale\": \"The exact recipe supports\
    \ the fatty acid instead of this commercial-product expansion. This does not set\
    \ the extraneous ingredient amount to zero, merge genuine duplicate-labelled inputs,\
    \ or transfer a JCM-specific repair.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty-acid stock\",\n        \"exact_source_quote\"\
    : \"DL-2-Methylbutyric acid 27.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"component_or_context\"\
    : \"Missing DL-2-methylbutyric acid\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"fatty-acid stock\",\n      \"volume_ml\": 27,\n      \"\
    identifier\": null\n    },\n    \"rationale\": \"Restore the literal acid name\
    \ and volume in the stock without inventing an ontology ID or a density conversion.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty-acid stock\",\n        \"exact_source_quote\"\
    : \"DL-2-Methylbutyric acid 27.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q30\",\n    \"component_or_context\"\
    : \"Ferrous sulfate stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"ferrous-sulfate stock\",\n      \"mass_g\": 1,\n     \
    \ \"solvent\": \"0.1 N H2SO4\",\n      \"solvent_volume_ml\": 1000,\n      \"\
    main_dose_ml\": 2,\n      \"main_strength\": \"0.1% w/v\"\n    },\n    \"rationale\"\
    : \"The 1 g stock input and its explicitly named strength do not belong as 1 g/L\
    \ direct main ingredient; retain the 2 mL receiving dose separately.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n        \"\
    source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 ferrous-sulfate stock\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O 1.00 g\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q31\",\n    \"component_or_context\"\
    : \"Sulfuric-acid stock solvent\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[29].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[29].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1000\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\"\
    : \"correct\"\n      }\n    ],\n    \"proposed_source_representation\": {\n  \
    \    \"stage\": \"ferrous-sulfate stock solvent\",\n      \"volume_ml\": 1000,\n\
    \      \"normality\": 0.1\n    },\n    \"rationale\": \"1000 mL of 0.1 N solution\
    \ is not 1000 g/L sulfuric acid; do not infer a mass or molarity conversion.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 ferrous-sulfate stock\",\n        \"exact_source_quote\"\
    : \"H2SO4 (0.1 N) 1000.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q32\",\n    \"component_or_context\"\
    : \"Main water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"main\",\n      \"water_ml\": 1000\n    },\n    \"rationale\"\
    : \"Add a separate source-stage representation. Listed solvent volumes and liquid\
    \ sums do not independently establish the main finished volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz719\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\",\n        \"\
    source_locator\": \"Exact named main/stock table row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q33\",\n    \"component_or_context\"\
    : \"SL-10 water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"SL-10\",\n      \"water_ml\": 990,\n      \"final_makeup_ml\"\
    : 1000\n    },\n    \"rationale\": \"Add a separate source-stage representation.\
    \ Listed solvent volumes and liquid sums do not independently establish the main\
    \ finished volume.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Exact named main/stock table row\",\n       \
    \ \"exact_source_quote\": \"Distilled water 990.00 ml\",\n        \"snapshot_sha256\"\
    : \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\",\n    \
    \    \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q34\",\n    \"component_or_context\"\
    : \"Fatty stock water\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"fatty-acid mixture\",\n      \"water_ml\": 896\n    },\n\
    \    \"rationale\": \"Add a separate source-stage representation. Listed solvent\
    \ volumes and liquid sums do not independently establish the main finished volume.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n\
    \        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Exact named main/stock table row\",\n       \
    \ \"exact_source_quote\": \"Distilled water 896.00 ml\",\n        \"snapshot_sha256\"\
    : \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\",\n    \
    \    \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"component_or_context\"\
    : \"SL-10 receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 1\n    },\n    \"rationale\": \"Add a separate source-stage\
    \ representation. Listed solvent volumes and liquid sums do not independently\
    \ establish the main finished volume.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Exact named main/stock table row\",\n       \
    \ \"exact_source_quote\": \"Trace element solution SL-10 1.00 ml\",\n        \"\
    snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"component_or_context\"\
    : \"Fatty stock receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 20\n    },\n    \"rationale\": \"Add a separate source-stage\
    \ representation. Listed solvent volumes and liquid sums do not independently\
    \ establish the main finished volume.\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Exact named main/stock table row\",\n       \
    \ \"exact_source_quote\": \"Fatty acid mixture 20.00 ml\",\n        \"snapshot_sha256\"\
    : \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\",\n    \
    \    \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"component_or_context\"\
    : \"Ferrous stock receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"dose_ml\": 2,\n      \"strength\": \"0.1% w/v\"\n    },\n    \"rationale\"\
    : \"Add a separate source-stage representation. Listed solvent volumes and liquid\
    \ sums do not independently establish the main finished volume.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz719\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\",\n        \"\
    source_locator\": \"Exact named main/stock table row\",\n        \"exact_source_quote\"\
    : \"FeSO4 x 7 H2O solution (0.1% w/v) 2.00 ml\",\n        \"snapshot_sha256\"\
    : \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\",\n    \
    \    \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"component_or_context\"\
    : \"Main gas mixture\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2\
    \ and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve\
    \ bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of\
    \ complete medium and adjust to 6.8 - 7.0, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"N2_percent\": 80,\n      \"CO2_percent\": 20,\n      \"minutes\"\
    : [\n        30,\n        45\n      ]\n    },\n    \"rationale\": \"Preserve exact\
    \ stage and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner\
    \ context and move stock-only owner instructions into their stock containers.\
    \ Gas basis is not expanded beyond the printed statement.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz719\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\",\n        \"\
    source_locator\": \"Page 1 main/SL-10 or page 2 fatty-stock preparation\",\n \
    \       \"exact_source_quote\": \"with 80% N2 and 20% CO2 gas mixture for 30 -\
    \ 45 min\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"component_or_context\"\
    : \"Late-stock gas\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2\
    \ and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve\
    \ bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of\
    \ complete medium and adjust to 6.8 - 7.0, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"stage\": \"glucose/cysteine/sulfide stocks\",\n      \"N2_percent\"\
    : 100\n    },\n    \"rationale\": \"Preserve exact stage and qualifier. Restore\
    \ missing target/KOMODO context; retain main DSMZ-owner context and move stock-only\
    \ owner instructions into their stock containers. Gas basis is not expanded beyond\
    \ the printed statement.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main/SL-10 or page 2 fatty-stock preparation\"\
    ,\n        \"exact_source_quote\": \"stock solutions prepared under 100% N2 gas.\"\
    ,\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"component_or_context\"\
    : \"Final main pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Dissolve ingredients\
    \ except bicarbonate, glucose, cysteine and sulfide. Sparge medium with 80% N2\
    \ and 20% CO2 gas mixture for 30 - 45 min to make it anoxic. Add and dissolve\
    \ bicarbonate, then dispense medium under same gas atmosphere into anoxic Hungate-type\
    \ tubes or serum vials and autoclave. Add glucose, cysteine and sulfide from sterile\
    \ anoxic stock solutions prepared under 100% N2 gas. Prior to use check pH of\
    \ complete medium and adjust to 6.8 - 7.0, if necessary.\",\n        \"decision\"\
    : \"evidence_only\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 6.8,\n          \"max\": 7.0\n        },\n        \"decision\": \"evidence_only\"\
    \n      }\n    ],\n    \"proposed_source_representation\": {\n      \"stage\"\
    : \"complete medium\",\n      \"pH\": [\n        6.8,\n        7\n      ],\n \
    \     \"conditional\": true\n    },\n    \"rationale\": \"Preserve exact stage\
    \ and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner\
    \ context and move stock-only owner instructions into their stock containers.\
    \ Gas basis is not expanded beyond the printed statement.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz719\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\",\n        \"\
    source_locator\": \"Page 1 main/SL-10 or page 2 fatty-stock preparation\",\n \
    \       \"exact_source_quote\": \"and adjust to 6.8 - 7.0, if necessary.\",\n\
    \        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"component_or_context\"\
    : \"SL-10 make-up\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[1].description\",\n        \"stored\": \"First dissolve\
    \ FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\
    \ make up to 1000.00 ml.\",\n        \"decision\": \"correct\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stage\": \"SL-10\",\n    \
    \  \"final_makeup_ml\": 1000\n    },\n    \"rationale\": \"Preserve exact stage\
    \ and qualifier. Restore missing target/KOMODO context; retain main DSMZ-owner\
    \ context and move stock-only owner instructions into their stock containers.\
    \ Gas basis is not expanded beyond the printed statement.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz719\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\",\n        \"\
    source_locator\": \"Page 1 main/SL-10 or page 2 fatty-stock preparation\",\n \
    \       \"exact_source_quote\": \"make up to 1000.00 ml.\",\n        \"snapshot_sha256\"\
    : \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\",\n    \
    \    \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"component_or_context\"\
    : \"Fatty stock pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\",\n   \
    \     \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\"\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\",\n        \"field_path\"\
    : \"preparation_steps[2].description\",\n        \"stored\": \"Adjust pH to 7.5\
    \ with concentrated NaOH.\",\n        \"decision\": \"correct\"\n      }\n   \
    \ ],\n    \"proposed_source_representation\": {\n      \"stage\": \"fatty stock\"\
    ,\n      \"pH\": 7.5,\n      \"NaOH_dose\": null\n    },\n    \"rationale\": \"\
    Preserve exact stage and qualifier. Restore missing target/KOMODO context; retain\
    \ main DSMZ-owner context and move stock-only owner instructions into their stock\
    \ containers. Gas basis is not expanded beyond the printed statement.\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz719\",\n    \
    \    \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main/SL-10 or page 2 fatty-stock preparation\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 7.5 with concentrated NaOH.\"\
    ,\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"component_or_context\"\
    : \"Unquantified stock titrant\",\n    \"decision\": \"not_quantified\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null,\n       \
    \ \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"reagent\": \"concentrated NaOH\",\n      \"dose\": null\n    },\n\
    \    \"rationale\": \"Source titrant is explicit but has no fixed dose or numeric\
    \ strength.\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 2 fatty stock\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.5 with concentrated NaOH.\",\n        \"snapshot_sha256\":\
    \ \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\",\n    \
    \    \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"component_or_context\"\
    : \"Unspecified autoclave cycle\",\n    \"decision\": \"not_quantified\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/anaerofilum_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"AUTOCLAVE\"\
    ,\n            \"description\": \"Dissolve ingredients except bicarbonate, glucose,\
    \ cysteine and sulfide. Sparge medium with 80% N2 and 20% CO2 gas mixture for\
    \ 30 - 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium\
    \ under same gas atmosphere into anoxic Hungate-type tubes or serum vials and\
    \ autoclave. Add glucose, cysteine and sulfide from sterile anoxic stock solutions\
    \ prepared under 100% N2 gas. Prior to use check pH of complete medium and adjust\
    \ to 6.8 - 7.0, if necessary.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"DISSOLVE\",\n            \"description\": \"First\
    \ dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other\
    \ salts. Finally make up to 1000.00 ml.\"\n          },\n          {\n       \
    \     \"step_number\": 3,\n            \"action\": \"ADJUST_PH\",\n          \
    \  \"description\": \"Adjust pH to 7.5 with concentrated NaOH.\"\n          },\n\
    \          {\n            \"step_number\": 4,\n            \"action\": \"MIX\"\
    ,\n            \"description\": \"The ferrous sulfate solution is not stable and\
    \ should be freshly prepared.\"\n          }\n        ],\n        \"decision\"\
    : \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\":\
    \ {\n      \"method\": \"autoclave\",\n      \"temperature\": null,\n      \"\
    duration\": null\n    },\n    \"rationale\": \"The method and ordering are stated;\
    \ a numeric cycle is not. Restore the source procedure without inventing time\
    \ or temperature.\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz719\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium719.pdf\"\
    ,\n        \"source_locator\": \"Page 1 main preparation\",\n        \"exact_source_quote\"\
    : \"tubes or serum vials and autoclave.\",\n        \"snapshot_sha256\": \"dfd5a77f5e71253bc4b561062237473b33129b433cf5bce0450b9e050543de77\"\
    ,\n        \"parsed_text_sha256\": \"43c736924d8917e82441ae4ca15618612c3a6dc7be3a07fafef610d1a13f2470\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '28 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 29/30
    primary and 25/30 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi16135
  - chebi17418
  - chebi17634
  - chebi17883
  - chebi26710
  - chebi26836
  - chebi28484
  - chebi31206
  - chebi31795
  - chebi32139
  - chebi32954
  - chebi33118
  - chebi34887
  - chebi49976
  - chebi53503
  - chebi62965
  - chebi63036
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86368
  - chebi8806
  - chebi91248
  - foodon03315426
  - micro0000182
  details: 'Instance coverage on a 0–100 percent scale, denominator 30: primary 96.67%;
    secondary 83.33%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 23 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: identity
  area: identity
  topic: DSMZ719, KOMODO719 and maintained ownership
  outcome: concern
  summary: The exact collection accession, catalog identity and two stable owner IDs
    agree, but the LB product notes and three expanded constituents conflict with
    the actual recipe. The stock DL-2-methylbutyric acid is missing. Same ingredient
    signatures reflect the same corruption, not independently supported recipe identity.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - id-search
- assessment_id: evidence
  area: evidence
  topic: All direct amounts and source-only stock quantities
  outcome: concern
  summary: No ingredient evidence objects are attached in the target or either owner.
    Exact primary snippets support stage-specific batch amounts and corrections; current
    unavailable APIs cannot authenticate the historical normalized denominator. Historical
    local reports remain derivative leads, not retrieved provider bytes.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - primary
  - quantity-inventory
  - bound-owner-context
- assessment_id: forms
  area: grounding
  topic: Salt, hydrate, mixture and supplied-form limits
  outcome: concern
  summary: Source sodium resazurin conflicts with neutral CHEBI:8806 C12H7NO4; source
    nickel chloride hexahydrate conflicts with CHEBI:34887 Cl2Ni. Sodium acetate is
    not hydrate-qualified in the source while CHEBI:32954 is anhydrous, so that specificity
    remains unverified. MICRO:0000182 and FOODON:03315426 correctly label tryptone
    and yeast extract but do not justify their LB-derived inclusion or supplier composition
    claims. Genuine main yeast extract remains distinct.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - primary
  - chebi8806
  - chebi34887
  - chebi32954
  - micro0000182
  - foodon03315426
- assessment_id: preparation
  area: completeness
  topic: Main and stock instructions across owner layers
  outcome: concern
  summary: The target and KOMODO owner omit the main anaerobic preparation and final-pH
    range retained in the DSMZ owner. That owner also retains stock-only SL-10 make-up,
    fatty-stock titration and fresh ferrous-stock warning at main root. Restore stage
    containers and all exact qualifiers; no numeric sterilization cycle or late-stock
    volumes are supplied.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Composition and biological claim limits
  outcome: concern
  summary: 'COMPLEX/UNDEFINED and LIQUID remain compatible with the genuine yeast-extract
    formula. Aerobic: Yes is imported catalog metadata and conflicts with the explicit
    anoxic preparation if treated as a recipe condition. Neither generic cultivation
    nor the title or supplier ingredient roles establishes a new organism-growth claim;
    no target organism CURIE or graph match is asserted.'
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - primary
- assessment_id: current-writers
  area: provenance
  topic: Current writers and maintained input follow-up
  outcome: concern
  summary: Current MediaDive parsing separates first-solution ingredients and stock
    additions, while collecting preparation steps from solution sections. The current
    resolver and merger are not a historical replay. repair_jcm_lb_acids.py is explicitly
    guarded to J266/J675/J1203 and cannot be applied to DSMZ719 by analogy; its source-specific
    repair is context only. Fix the two maintained719 owners with their own exact
    evidence before separately authorized regeneration.
  target_ids:
  - CultureMech:006361
  evidence_ids:
  - record
  - current-code-0
  - current-code-1
  - current-code-2
  - current-code-3
findings:
- finding_id: f1
  issue_key: culturemech.006361.wrong-lb-replacement
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Unrelated LB constituents replace a fatty-acid component
  description: All three local layers contain LB-labelled tryptone 10, yeast extract
    5 and sodium chloride 10 g/L, plus commercial-product metadata, while exact719
    specifies DL-2-methylbutyric acid 27 mL in its fatty stock. Genuine main yeast
    extract and NaCl must be retained separately.
  target_ids:
  - CultureMech:006361
  field_paths:
  - ingredients[23]
  - ingredients[24]
  - ingredients[25]
  - notes
  - solutions
  evidence_ids:
  - primary
  - record
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  issue_key: culturemech.006361.stock-and-unit-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock compositions and liquid inputs are represented as main g/L
  description: SL-10, fatty acids and the ferrous-sulfate solvent are flattened; acid
    mL and1000 mL 0.1 N sulfuric solution became g/L. Main rates depend on an unverified
    denominator. Stock doses/water and their distinct bases are absent.
  target_ids:
  - CultureMech:006361
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  issue_key: culturemech.006361.form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin and nickel hydrate have incompatible primary mappings
  description: The sodium dye is mapped to neutral resazurin, and nickel hexahydrate
    to anhydrous nickel dichloride in primary and current secondary slots. Valid labels
    do not resolve supplied-form mismatch; sodium-acetate hydration is separately
    unverified.
  target_ids:
  - CultureMech:006361
  field_paths:
  - ingredients[8].term
  - ingredients[20].term
  - ingredients[20].mediaingredientmech_chebi_term
  - ingredients[6].term
  evidence_ids:
  - primary
  - chebi8806
  - chebi34887
  - chebi32954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  issue_key: culturemech.006361.preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Main preparation is lost and stock preparation is detached
  description: The DSMZ owner retains the complete main procedure and pH range, but
    target/KOMODO omit them. Stock-only make-up, titration and instability warning
    must move with the restored stocks; imported aerobic metadata must not replace
    the explicit anoxic preparation.
  target_ids:
  - CultureMech:006361
  field_paths:
  - preparation_steps
  - ph_range
  - notes
  - solutions
  evidence_ids:
  - primary
  - owner-1
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  issue_key: culturemech.006361.historical-timestamps
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Import history contains malformed or timezone-naive timestamps
  description: The KOMODO-derived target and owner retain malformed .fZ import timestamps
    and naive enrichment timestamps. These are historical provenance limitations,
    not permission to rewrite events.
  target_ids:
  - CultureMech:006361
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  description: Remove only the unsupported LB expansion and supersede its active product
    claims in both maintained owners; restore the source fatty-acid input and evidence
    without inventing an identifier. Preserve history append-only and genuine same-labelled
    main components.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006361
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  description: Restore main batch and three stock scopes, explicit receiving doses,
    solvent units and supported strengths in both owners. Preserve missing final-volume/density/percentage-basis
    limits and attach per-claim evidence.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006361
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  description: Verify source-compatible salt/hydrate identifiers and assess secondary
    links independently. Qualify acetate specificity rather than choosing an unprinted
    hydrate.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006361
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  description: Preserve main ordering and all source gas/pH qualifiers, restore missing
    layers, and relocate stock instructions. Do not invent a numerical autoclave cycle
    or infer growth from atmosphere.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006361
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
  description: Preserve old events and append a dated clarification with exact evidence
    when curation is authorized; fix future writers separately.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006361
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/anaerofilum_medium.yaml
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
- The complete current primary is available, but it supplies no main final-volume
  statement or late-stock volumes; both current719 API attempts failed 503. Required
  authentication of the historical 1.023 L normalization and exact assembled final
  rates remains unavailable. Source-stage masses and confirmed identity defects are
  supported; partial scope is not based solely on optional KOMODO access failures.
- 'Preserved access limitation for mediadive719api: 503. No unavailable product or
  provider response is treated as formulation evidence; DSMZ719 directly establishes
  the current recipe scope.'
- 'Preserved access limitation for mediadive719apiRetry: 503. No unavailable product
  or provider response is treated as formulation evidence; DSMZ719 directly establishes
  the current recipe scope.'
- 'Preserved access limitation for komodo719detail: 403. No unavailable product or
  provider response is treated as formulation evidence; DSMZ719 directly establishes
  the current recipe scope.'
- 'Preserved access limitation for komodo719actual: 403. No unavailable product or
  provider response is treated as formulation evidence; DSMZ719 directly establishes
  the current recipe scope.'
- 'Preserved access limitation for solution209: 503. No unavailable product or provider
  response is treated as formulation evidence; DSMZ719 directly establishes the current
  recipe scope.'
- 'Preserved access limitation for solution5861: 503. No unavailable product or provider
  response is treated as formulation evidence; DSMZ719 directly establishes the current
  recipe scope.'
- 'Preserved access limitation for laboratoryNotes: None. No unavailable product or
  provider response is treated as formulation evidence; DSMZ719 directly establishes
  the current recipe scope.'
- 'Preserved access limitation for sigmaL3522: None. No unavailable product or provider
  response is treated as formulation evidence; DSMZ719 directly establishes the current
  recipe scope.'
- 'Preserved access limitation for bd244520: 403. No unavailable product or provider
  response is treated as formulation evidence; DSMZ719 directly establishes the current
  recipe scope.'
- No supplier composition was substituted for the exact collection recipe. Current
  primary disagreements are not assigned a chronology relative to historical provider
  data.
- Exact source quantities are preserved without assuming a main one-liter final volume,
  acid density, unqualified 25% basis, or current API content that could not be retrieved.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-028
- generated-medium
```
