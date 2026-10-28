# Source and formulation review: cens_medium (CultureMech:006399)

- Review: 20261025T201513Z-culturemech-006399-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-25T20:08:38Z
- Finished UTC: 2026-10-25T20:15:13Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM748 supports the CENS identity and its separate main, True Blue and chelated iron stages. All three local documents flatten the stock components; EDTA is a sum across incompatible stages, and the preparation retained by one owner is misplaced at medium level. Nickel and cobalt hydrate mappings require correction. Current primary evidence takes precedence over an erroneous historical cobalt reading and unsupported historical final-volume assumptions.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 527; batch 053 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fifty-two task batches contain 520 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 523 of 6325 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 231e0ba71b41d45362168d539efebe7991823464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006399 | data/merge_yaml/merged/CENS_MEDIUM.yaml | generated | cens_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006399 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:006399 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/527/strict.tsv |
| validate-terms | passed | True | CultureMech:006399 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:006399 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:006399 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: api748 | unavailable | True | CultureMech:006399 | The exact current api748 capture returned HTTP 503; its maintenance/challenge body supplies no formulation. DSM748 remains usable, while independent current KOMODO formulation confirmation is unavailable. The failed attempt and original timestamp remain preserved. |
| Exact source content access: komodo748 | unavailable | True | CultureMech:006399 | The exact current komodo748 capture returned HTTP 403; its maintenance/challenge body supplies no formulation. DSM748 remains usable, while independent current KOMODO formulation confirmation is unavailable. The failed attempt and original timestamp remain preserved. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:006399.

The four documented recipes completed; interpret the scope of each separately.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:006399.

21 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels across the selected target and its exact maintained owners. Target linkage: 21/22 primary and 21/22 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Complete recursive inspection of these selected documents found zero legacy mediaingredientmech_term slots and zero numeric legacy MediaIngredientMech identifiers. Generic placeholder text in history is not an asserted identifier. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 22: primary 95.45%; secondary 95.45%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: concern. Targets: CultureMech:006399.

29 timestamp instances inspected; 4 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:006399.

28 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "subject": "K2HPO4 main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "0.9",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 4: K2HPO4",
        "exact_source_quote": "K2HPO4                                                            0.9       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 0.9,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q2",
    "subject": "KH2PO4 main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 5: KH2PO4",
        "exact_source_quote": "KH2PO4                                                            0.6       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 0.6,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q3",
    "subject": "NH4Cl main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 6: NH4Cl",
        "exact_source_quote": "NH4Cl                                                             1.0       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 1,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q4",
    "subject": "EDTA separated across three preparation stages",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "12.22722",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "12.22722",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "12.22722",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 7: EDTA",
        "exact_source_quote": "EDTA                                                              5.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 20: EDTA",
        "exact_source_quote": " EDTA                                                             2.5       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 37: EDTA",
        "exact_source_quote": " EDTA                                                             2.0        g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 39: Distilled water",
        "exact_source_quote": " Distilled water                                                900.0       ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "12.22722 G_PER_L is the local sum of 0.005,10 and 2.22222 values from different stages. Source supports 5 mg basal EDTA,2.5 g in the final 250 ml True Blue stock and 2 g in the iron stock with 900 ml listed water. Only True Blue supports 10 g/L stock arithmetic; iron 2/0.9 g/L is conditional on an unproven final stock volume. No summed final-medium rate is established.",
    "proposed_source_representation": {
      "main_batch": {
        "amount": 5,
        "unit": "mg"
      },
      "True_Blue_stock": {
        "amount": 2.5,
        "unit": "g",
        "explicit_final_volume_ml": 250,
        "stock_rate_g_per_l": 10
      },
      "Chelated_Iron_stock": {
        "amount": 2,
        "unit": "g",
        "water_input_ml": 900,
        "final_volume": "unspecified"
      }
    }
  },
  {
    "decision_id": "q5",
    "subject": "MgSO4 main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 8: MgSO4",
        "exact_source_quote": "MgSO4 x 7 H2O                                                     0.2       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 0.2,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q6",
    "subject": "CaCl2 main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.075",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.075",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.075",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 9: CaCl2",
        "exact_source_quote": "CaCl2 x 2 H2O                                                    75.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 75,
      "unit": "mg",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q7",
    "subject": "Vitamin B12 main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "2e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 12: Vitamin B12",
        "exact_source_quote": "Vitamin B12                                                      20.0      μg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 20,
      "unit": "microgram",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q8",
    "subject": "Biotin main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5e-05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5e-05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "1.5e-05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 13: Biotin",
        "exact_source_quote": "Biotin                                                           15.0      μg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 15,
      "unit": "microgram",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q9",
    "subject": "Na2S2O3 main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 14: Na2S2O3",
        "exact_source_quote": "Na2S2O3 x 5 H2O                                                   0.5       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 0.5,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q10",
    "subject": "Soytone main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 15: Soytone",
        "exact_source_quote": "Soytone (Difco 0436)                                              4.0       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. ",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 4,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q11",
    "subject": "Na-pyruvate main batch input",
    "decision": "unsupported",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 16: Na-pyruvate",
        "exact_source_quote": "Na-pyruvate (filter-sterilized)                                   2.2       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The printed batch amount is supported; its stored G_PER_L representation assumes a final medium denominator not declared by the primary. Listed 1000 ml water plus stock additions must not silently become a final 1 L or1.003L volume. No numeric error in the printed mass is inferred. Filter sterilization is explicitly required for this sodium-pyruvate addition.",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 2.2,
      "unit": "g",
      "final_medium_volume": "unspecified"
    }
  },
  {
    "decision_id": "q12",
    "subject": "MnCl2 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 21: MnCl2",
        "exact_source_quote": " MnCl2 x 4 H2O                                                    0.2       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. ",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 0.2,
      "batch_unit": "g",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.8,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q13",
    "subject": "H3BO3 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 22: H3BO3",
        "exact_source_quote": " H3BO3                                                            0.1       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. ",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 0.1,
      "batch_unit": "g",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.4,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q14",
    "subject": "Na2MoO4 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 23: Na2MoO4",
        "exact_source_quote": " Na2MoO4 x 2 H2O                                                  0.1       g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. ",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 0.1,
      "batch_unit": "g",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.4,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q15",
    "subject": "ZnCl2 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 24: ZnCl2",
        "exact_source_quote": " ZnCl2                                                           50.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. ",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 50,
      "batch_unit": "mg",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.2,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q16",
    "subject": "NiCl2 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 25: NiCl2",
        "exact_source_quote": " NiCl2 x 6 H2O                                                   50.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. Source hydrate identity requires separate reconciliation of both asserted term slots.",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 50,
      "batch_unit": "mg",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.2,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q17",
    "subject": "CoCl2 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.08",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 26: CoCl2",
        "exact_source_quote": " CoCl2 x 2 H2O                                                   20.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. Source hydrate identity requires separate reconciliation of both asserted term slots.",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 20,
      "batch_unit": "mg",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.08,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q18",
    "subject": "CuCl2 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.04",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 27: CuCl2",
        "exact_source_quote": " CuCl2 x 2 H2O                                                   10.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. ",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 10,
      "batch_unit": "mg",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.04,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q19",
    "subject": "Na2SeO3 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 28: Na2SeO3",
        "exact_source_quote": " Na2SeO3                                                          5.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. ",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 5,
      "batch_unit": "mg",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.02,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q20",
    "subject": "NaVO3 in True Blue stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 29: NaVO3",
        "exact_source_quote": " NaVO3 x n H2O (meta)                                             5.0      mg",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The stored number matches the concentration of this ingredient in the explicitly final 250 ml stock, but it is currently asserted as a direct medium concentration. Restore the named stock recipe and its 1 ml batch addition. This does not establish a final-medium G_PER_L rate. Source hydrate number remains unspecified for NaVO3 x n H2O.",
    "proposed_source_representation": {
      "stage": "True Blue Trace Elements stock",
      "batch_amount": 5,
      "batch_unit": "mg",
      "explicit_final_volume_ml": 250,
      "stock_rate_g_per_l": 0.02,
      "receiving_batch_dose_ml": 1
    }
  },
  {
    "decision_id": "q21",
    "subject": "FeCl2 tetrahydrate in chelated iron stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "1.11111",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "1.11111",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "1.11111",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 36: FeCl2",
        "exact_source_quote": " FeCl2 x 4 H2O                                                    1.0        g",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 39: Distilled water",
        "exact_source_quote": " Distilled water                                                900.0       ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 11: Chelated Iron",
        "exact_source_quote": "Chelated Iron solution (see below)                                2.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The source places 1 g in a stock made with 900 ml listed water, dosed 2 ml into the main batch. Stored 1.11111 G_PER_L is a stock-water normalization flattened into the medium; neither an exact stock final volume nor a final-medium rate is established.",
    "proposed_source_representation": {
      "stage": "Chelated Iron solution",
      "amount": 1,
      "unit": "g",
      "water_input_ml": 900,
      "receiving_batch_dose_ml": 2,
      "final_stock_volume": "unspecified"
    }
  },
  {
    "decision_id": "q22",
    "subject": "Concentrated HCl volume in chelated iron stock",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/CENS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 38: HCl",
        "exact_source_quote": " HCl (conc.)                                                      3.0       ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 39: Distilled water",
        "exact_source_quote": " Distilled water                                                900.0       ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "Source 3 ml concentrated HCl is a volume input to the iron stock, not 3 g/L in the medium. Acid strength, density, final stock volume and final-medium rate are not specified; no mass conversion is proposed.",
    "proposed_source_representation": {
      "stage": "Chelated Iron solution",
      "amount": 3,
      "unit": "ml",
      "strength": "concentrated; numeric strength unspecified"
    }
  },
  {
    "decision_id": "q23",
    "subject": "True Blue receiving dose",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 10: True Blue",
        "exact_source_quote": "True Blue Trace elements (see below)                              1.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "Missing source-explicit volume or stock-addition representation. Treat this as the printed batch input; no unspecified final-volume normalization.",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 1,
      "unit": "ml",
      "basis": "batch input"
    }
  },
  {
    "decision_id": "q24",
    "subject": "Chelated iron receiving dose",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 11: Chelated Iron",
        "exact_source_quote": "Chelated Iron solution (see below)                                2.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "Missing source-explicit volume or stock-addition representation. Treat this as the printed batch input; no unspecified final-volume normalization.",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 2,
      "unit": "ml",
      "basis": "batch input"
    }
  },
  {
    "decision_id": "q25",
    "subject": "Main distilled-water input",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 17: Distilled water",
        "exact_source_quote": "Distilled water                                                1000.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "Missing source-explicit volume or stock-addition representation. Treat this as the printed batch input; no unspecified final-volume normalization.",
    "proposed_source_representation": {
      "stage": "main batch",
      "amount": 1000,
      "unit": "ml",
      "basis": "batch input"
    }
  },
  {
    "decision_id": "q26",
    "subject": "True Blue stock water/final makeup",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 30: Distilled water",
        "exact_source_quote": " Distilled water                                                250.0      ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      },
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "Missing source-explicit volume or stock-addition representation. The following preparation explicitly makes this stock to final 250 ml.",
    "proposed_source_representation": {
      "stage": "True Blue stock",
      "amount": 250,
      "unit": "ml",
      "basis": "explicit final stock volume"
    }
  },
  {
    "decision_id": "q27",
    "subject": "Chelated iron water input",
    "decision": "add",
    "local_fields": [],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text line 39: Distilled water",
        "exact_source_quote": " Distilled water                                                900.0       ml",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "Missing source-explicit volume or stock-addition representation. Treat this as the printed batch input; no unspecified final-volume normalization.",
    "proposed_source_representation": {
      "stage": "Chelated Iron stock",
      "amount": 900,
      "unit": "ml",
      "basis": "batch input"
    }
  },
  {
    "decision_id": "q28",
    "subject": "True Blue preparation scope",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "preparation_steps[0].step_number",
        "stored": 1
      },
      {
        "input": "data/normalized_yaml/bacterial/cens_medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final volume to 250.0 ml with additional water."
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz748",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf",
        "source_locator": "PDF page 1; extracted text lines 32–33",
        "exact_source_quote": "Dissolve chemicals one at a time in approximately 200.0 ml distilled water. Bring final\nvolume to 250.0 ml with additional water.",
        "snapshot_sha256": "4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe",
        "parsed_text_sha256": "0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab",
        "accessed_at": "2026-10-22T09:27:20.100374+00:00"
      }
    ],
    "rationale": "The retained text is accurate but belongs to the True Blue stock, not the whole CENS medium. Preserve its sequence number as local ordering metadata and attach the approximately 200 ml dissolution/final 250 ml makeup to that stock; target and KOMODO owner currently lack it.",
    "proposed_source_representation": {
      "stage": "True Blue stock preparation",
      "initial_water_ml_approx": 200,
      "explicit_final_volume_ml": 250
    }
  }
]

### DSM748 and copied KOMODO source identity

identity: supported. Targets: CultureMech:006399.

CENS corresponds to the current DSM748 primary. KOMODO owner provenance explicitly copies DSM composition, which explains shared data without independently proving current KOMODO formulation equivalence. Current web/API access is unavailable.

### Stock boundaries, preparation and evidence placement

completeness: concern. Targets: CultureMech:006399.

The primary supplies both stock recipes and doses. The DSM owner retains True Blue makeup text but at medium level; the target and KOMODO owner omit it. Sodium pyruvate filter sterilization is absent locally. No pH, autoclave program or growth condition is invented.

### Historical report interpretation versus exact source

evidence: concern. Targets: CultureMech:006399.

All six reports were read. API748 remains unrecovered within the pinned bounded parent search; the October tables are derivative. The September cobalt-hexahydrate claim and iron final-volume arithmetic are not adopted. The current primary page is the basis for the present findings.

### Record type, category and growth claims

scope: unknown. Targets: CultureMech:006399.

The selected documents are bacterial liquid MediaRecipe records. The bounded collection formulation establishes a recipe identity, not strain-specific experimental growth. No organism growth assertion, incubation optimum or literature-wide evidence claim is added.

## Findings

### f1: Separate the flattened stocks and EDTA sum

major / open / confirmed; issue key: CENS_STOCK_STAGES.

All three documents flatten True Blue and chelated iron ingredients into direct medium G_PER_L values and retain an EDTA sum across three preparation stages. The explicit True Blue final 250 ml supports stock rates only; main and iron listed-water amounts do not establish final volumes. HCl is 3 ml within iron stock, not 3 g/L medium.

### f2: Reconcile nickel and cobalt hydrate mappings

major / open / confirmed; issue key: CENS_SUPPLIED_HYDRATES.

NiCl2 x 6 H2O and CoCl2 x 2 H2O are explicitly printed, while both primary and secondary slots assert anhydrous CHEBI:34887 and CHEBI:35696. The local preferred cobalt dihydrate text is correct; the historical claim that the primary specifies a hexahydrate is not. Source vanadate nH2O additionally leaves monohydrate specificity unresolved.

### f3: Keep stock makeup and pyruvate sterilization at their own stages

major / open / confirmed; issue key: CENS_PREPARATION_SCOPE.

The DSM owner contains True Blue approximately 200 ml/final 250 ml makeup as top-level preparation, while the other layers omit it. The primary separately marks sodium pyruvate filter-sterilized. These are stage-specific details, not instructions to prepare the entire medium at 250 ml.

### f4: Preserve and qualify malformed import timestamps

minor / open / confirmed; issue key: CENS_HISTORY_TIMESTAMP.

The target and KOMODO owner retain a timestamp with a literal .fZ suffix. It is not a valid UTC instant. Preserve original history and add a bounded clarification rather than replacing it with a guessed access or execution time.

## Recommended Actions And Acceptance Checks

### a1

Restore both named stock recipes and source batch doses in the maintained owners, separate each EDTA occurrence, and preserve unsupported final-volume bases as unresolved. Rebuild the target only after exact formulation comparison.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Reconcile the two supplied hydrate mappings against explicit source forms and current ontology evidence. Resolve vanadate specificity without inventing n; retain ingredient names and sources. Do not substitute a new identifier without verifying its exact definition.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Retain the existing stock instruction but move or scope it to True Blue; represent source pyruvate filter sterilization without inventing its timing, a basal autoclave program or final medium volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Append a provenance clarification for the malformed timestamp and verify the current timestamp writer separately; keep all original source access times and historical bytes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/CENS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/cens_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/CENS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/CENS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch053/527/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch053/527/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/CENS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/CENS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/CENS_MEDIUM.yaml:1:id: CultureMech:006399<br>./data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml:1:id: CultureMech:006399<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/527/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 27 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| source-reading | /private/tmp/culturemech-review-work-batch053/records527-528-source-reading-20261025T201126Z/source-reading.json; Complete selected documents, primary pages, fourteen historical reports and named current writer functions | context_only | The pinned reading receipt distinguishes complete source reads from derivative historical interpretation and from current writer behavior. |
| context | /private/tmp/culturemech-review-work-batch053/source-preflight-bound/527/evidence-context-original.json; Full per-record source context and scoped inventories | context_only | Frozen local inventories, source captures, source-access outcomes and exact owner/parent scope; context is an index, not additional independent scientific evidence. |
| dsm748-main | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf; Complete page 1 main recipe, rows 4–17 | supports | Primary main recipe specifies original batch masses, two stock doses and listed water. It does not declare a measured final medium volume. |
| dsm748-blue | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf; Page1 True Blue Trace Elements table and preparation, lines 19–33 | supports | This stock is explicitly made to final 250 ml. The approximately 200 ml dissolution instruction belongs to this stock alone; source cobalt is the dihydrate. |
| dsm748-iron | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf; Page1 Chelated Iron solution, lines 35–39 | supports | Iron stock lists 1 g FeCl2 tetrahydrate, 2 g EDTA, 3 ml concentrated HCl and 900 ml water; neither final stock volume nor HCl strength or density is specified. |
| api748-attempt | https://mediadive.dsmz.de/rest/medium/748; Preserved exact public retrieval result | context_only | The exact current api748 capture returned HTTP 503; its maintenance/challenge body supplies no formulation. DSM748 remains usable, while independent current KOMODO formulation confirmation is unavailable. The failed attempt and original timestamp remain preserved. |
| komodo748-attempt | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=748; Preserved exact public retrieval result | context_only | The exact current komodo748 capture returned HTTP 403; its maintenance/challenge body supplies no formulation. DSM748 remains usable, while independent current KOMODO formulation confirmation is unavailable. The failed attempt and original timestamp remain preserved. |
| report-0 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_748_CENS_medium.yaml.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct 7 KOMODO report retained all 22 local quantities unresolved because main and stock stages were flattened. Its cited API748 raw digest is not recovered in the bounded parent search; decoded tables remain derivative. |
| report-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cens_medium.yaml.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct 7 DSM report likewise retained the unchanged 22-row owner and unresolved stock quantities. Agreement with the KOMODO report is not an independent raw capture. |
| report-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENS_MEDIUM.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct 5 generated-target inventory has0/22 source-checked concentrations; candidate same-slug records are not additional maintained owners. |
| report-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_748_CENS_medium.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct 5 KOMODO-owner inventory has0/22 source-checked concentrations; no independent source confirmation. |
| report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cens_medium.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Oct 5 DSM-owner inventory has0/22 source-checked concentrations; no independent source confirmation. |
| report-5 | reports/yaml_record_review/20260922T064616Z-CENS_MEDIUM.md; Entire exact historical report; identity header, quantity table, decisions and limits | context_only | Entire September review read. Its claimed source CoCl2 hexahydrate contradicts the current pinned PDF, which prints dihydrate. Its iron900ml final-volume and final-medium-rate assumptions are not source-established. Its stock-flattening discussion is historical context only. |
| writer-0 | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit, _parse_preparation_steps | context_only | Current import separates main composition from referenced stock additions and maps provider units. Unit mapping alone cannot establish final volume. Preparation parsing still iterates solution steps, so their receiving-medium versus stock scope must be preserved. These functions do not prove which historical version produced the assessed record. |
| writer-1 | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current web import builds source identity and a composition placeholder; it does not independently verify a later copied DSM formulation. Its time.strftime format includes %f, consistent with the malformed literal history timestamp, but current source code alone does not establish historical execution. |
| writer-2 | src/culturemech/enrich/dsmz_resolver.py; merge_composition | context_only | Current resolver copies non-placeholder DSM ingredients and solutions plus missing pH. Copied DSM data are shared provenance, not independent confirmation of KOMODO or strain-specific equivalence; the function does not transfer complete preparation. |
| writer-3 | scripts/cleanup_media_quality.py; merge_duplicate_ingredients; _merge_ingredient_group | context_only | Current duplicate cleanup explicitly does not sum concentration values: equal quantities may collapse and disagreements retain a representative with a warning. The old merged EDTA sum is not evidence that this current implementation still adds concentrations across preparation stages. |
| writer-4 | src/culturemech/merge/formulation.py; Entire file: scientific projection, formulation_signature, merge_formulation_evidence | context_only | Current scientific comparison retains exact quantities, notes, preparation, solution structure and list order, and rejects incompatible formulations before provenance union. It is not an ingredient-only equivalence test. |
| writer-5 | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group invokes the exact scientific-formulation guard before combining evidence. Old generated content and old ingredient-signature merge history do not establish that the current guard would merge the now-divergent maintained owners. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi132095 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132095; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:132095 resolves to sodium metavanadate hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17883 resolves to hydrogen chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32150; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32150 resolves to sodium thiosulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_4735; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:4735 resolves to ethylenediaminetetraacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi48843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:48843 resolves to disodium selenite. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49976 resolves to zinc dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86249 resolves to iron dichloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86368 resolves to manganese(II) chloride tetrahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:132095": [{"label": "NaVO3 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:132095", "preferred_term": "NaVO3 x H2O", "ontology_id": "CHEBI:132095", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier": "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label": "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150", "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:35696": [{"label": "CoCl2", "match_type": "preferred_term", "identifier": "CHEBI:35696", "preferred_term": "CoCl2", "ontology_id": "CHEBI:35696", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:4735": [{"label": "EDTA", "match_type": "preferred_term", "identifier": "CHEBI:4735", "preferred_term": "EDTA", "ontology_id": "CHEBI:4735", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:48843": [{"label": "Na2SeO3", "match_type": "preferred_term", "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label": "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term": "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term": "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id": "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368": [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368", "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/CENS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml; data/normalized_yaml/bacterial/cens_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": [{"index": 1, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:19:15.275332"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml", "events": 9, "timestamp_issues": [{"index": 1, "issue": "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 2, "issue": "timezone absent", "value": "2026-02-03T11:19:15.275332"}]}, {"input": "data/normalized_yaml/bacterial/cens_medium.yaml", "events": 9, "timestamp_issues": []}] |
| quantity-inventory | /private/tmp/culturemech-review-work-batch053/527/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact current api748 capture returned HTTP 503; its maintenance/challenge body supplies no formulation. DSM748 remains usable, while independent current KOMODO formulation confirmation is unavailable. The failed attempt and original timestamp remain preserved.
- The exact current komodo748 capture returned HTTP 403; its maintenance/challenge body supplies no formulation. DSM748 remains usable, while independent current KOMODO formulation confirmation is unavailable. The failed attempt and original timestamp remain preserved.
- No exact historical API748 response was recovered on the twelve explicitly searched JSON parent surfaces; this is a bounded result, not universal absence.
- No direct growth publication or strain-specific performance evidence was assessed. The preserved references and classification do not establish growth.
- True Blue final stock volume is explicit; main and iron stock final volumes are not. No exact diluted final-medium rates are asserted.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201513Z-culturemech-006399-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: cens_medium (CultureMech:006399)'
started_at: '2026-10-25T20:08:38Z'
finished_at: '2026-10-25T20:15:13Z'
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
summary: DSM748 supports the CENS identity and its separate main, True Blue and chelated
  iron stages. All three local documents flatten the stock components; EDTA is a sum
  across incompatible stages, and the preparation retained by one owner is misplaced
  at medium level. Nickel and cobalt hydrate mappings require correction. Current
  primary evidence takes precedence over an erroneous historical cobalt reading and
  unsupported historical final-volume assumptions.
source:
  git_revision: 231e0ba71b41d45362168d539efebe7991823464
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: data/merge_yaml/merged/CENS_MEDIUM.yaml
    sha256: 87f350e525ac4c61bc84523ad9c6542853fa6be950d2b64ab5c4156cc9522cd3
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    sha256: bf4ff8d3467bfe23153066ac328d91e765961c93fcbcbc9d6a3b1a0f91a1c968
    role: context
  - path: data/normalized_yaml/bacterial/cens_medium.yaml
    sha256: f85fc9c48370753c8139e39ba9df64631706c9e2d5e59b552a03f1632e3fb598
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_650_CENTENUM_medium.yaml.md
    sha256: cea95c8bef224d7988c89e55916e6bfc1c85e40e1e04644c416ba76677bfaf5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_748_CENS_medium.yaml.md
    sha256: 013cdd23597b0f17ae16040cfcff4fa5612704583733ff2b59f4575da6a5ef4e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/medium_650_modified_for_dsm_8319.yaml.md
    sha256: bf8b812d7257fd833fe40a0c3d65ecca0d062d667e5d7ef32e8da45fdc400b8d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cellulosilyticum_medium.yaml.md
    sha256: 6fc71489fc62d3a8490420a79c8e85ef97b1bf00048f2b4a5f9cbde290926d95
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cens_medium.yaml.md
    sha256: 21cd5c7838ddcd4136764be9d06f0b560c3df459ffd3510ca5a9df7e1f34e292
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/centenum_medium.yaml.md
    sha256: 11adfae044a191efafa6569efa6dae001a26c2b4186bb1c4165f15ec06fb5aa7
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1500-2000/records/bacterial/cgm.yaml.md
    sha256: 00bc6814a1dfc5789c97728aa09b3959c842ce63a226744cc526ee36a88f826e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.yaml.md
    sha256: 3338d620d73f8bd698294bbb4b0a267bb79d279ff8c96056cc4586cd8535f187
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5312_Solution_C.yaml.md
    sha256: e167b06340bce70ab77d6408c8f5e9cb6b1dbeef2c36e29ff20952990e3bfbd2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5342_Solution_A.yaml.md
    sha256: f68b7d85766061aa31ffef0f0172844d47d0aae036221dc66d608c86e8dce7a6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5343_Solution_B.yaml.md
    sha256: aca054ad3ae72ab8aee9908cb67ceac62a96adf84ff60a5141dda9b4f13ff6d8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
    sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-m258-m260-stocks/records/M258.md
    sha256: fda8033086b0627144eb23d2558e66134a597bfa67939fec2f18992de7845747
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CEJFB1T_MEDIUM.md
    sha256: 49ac2c7b79c5da4e7d56b164324afa763d1f8301cb1794aacecb55c381582cb6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.md
    sha256: a9112230e5f2b35a345d29058d2d06b1aec1b6c6e36d77e294ecbad9801f92ba
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: d71859ea710d11f601c3f0c34e1740f6d2afbae9b6516f296dccbe34c913d948
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSE_AGAR.md
    sha256: f90ca9219519b238b5b06d86a8ca2e84f6832a4ab67b0feabd05bdc3a9839381
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSILYTICUM_MEDIUM.md
    sha256: 3a3e74ac86eca9c6db45ec35f7ef0e6a76527941fffd6422ec02b9931c0c4212
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.md
    sha256: 63217cedf21217428eca34c2c1418b1982e2e1b435abc3a6130e2689216f9fb0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENS_MEDIUM.md
    sha256: 597cb6a7938f9cd459897adf69983dff16ed4d88f1a910366ad8abe4b3928222
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENTENUM_MEDIUM.md
    sha256: 64359ed6e4f323a585a64a19e0259164f4e54dd0e8d5c90443fca6183b6c91e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CGM.md
    sha256: a07bbba50f039aeb8d2aa1f811f38913a6651995e329748e80f180b9a3d57a3b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CGY_Medium.md
    sha256: 2d2435a40efa8bac48c6238994b420ea1f7022e9d1a615b67aa2734a79397302
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/algae/cgm.md
    sha256: 306c1cacb9be80fb75cde15b3ccffd282c046df9f6cf08ef2ff32055f4886ee4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M1148_Halanaeroarchaeum_Medium.md
    sha256: edfdd0b0fb57e8f9d9c328c8326da947773576733a6c38f9ecda66e70fb8e1a9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.md
    sha256: 10dbfce058ee6e85485dcfdc15b611cc9e0b95cea52a03f631a3b54fe008fa04
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J295_CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: 9a63092a34db92eb9ca60f2db910800f0034f5e7f0e6d1eb074e146061fa60d4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.md
    sha256: 9305c9cfd434cbb5f857fd99357fe9a811cb31a48a3d05d779959557c84250b2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_748_CENS_medium.md
    sha256: a9c41ec015e0f2f45bb92ed0065eb0ddc3f3852207c12751d1ce686377ba8326
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1040_CEJFB1T_Medium.md
    sha256: d3295a1ae91e3c543bac519713a5559b6da46ed2a5384def64ef0c9354ed6e4f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1264_Cellulolytic_Natronoarchaea_Medium.md
    sha256: 59c8979a006d9b770dd6d2b0ecdbdfd4a81fa2339fff1d33afd41e65932df4fc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M439_Desulfovibrio_Aerotolerans_DVO5_Medium.md
    sha256: e43ae29a243274817a13192084b67ac0741248fff46309a4e2862aef08e1ef58
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M57_Cellulose_Agar.md
    sha256: 7a3396b4e01bffebe1a22b591ead29f62ecbfeaeeeb315bbcac5a84050435f83
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.md
    sha256: a1adca9a9911e57b4bd66fce0a5f4db9d2feea7b745195bf0c6e53238beeb2d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cellulosilyticum_medium.md
    sha256: da0b08c05cca15abca3721b4461c97a7cb8390a6cbb460045efe9dd04a956ec2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cens_medium.md
    sha256: 874c7e795a7cd6cb420776fb624326f85520f9879d26165de81a0638506b1de2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/centenum_medium.md
    sha256: fabcbe826c085e4f317e0f4dffb71c125ef8c93ca6d7c378eb5aa003bcbc9f94
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgm.md
    sha256: aed676ac8b2825a51883505bc77e41d3fd59a20a6facce044c7c62a638aa64d1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cgy_medium.md
    sha256: 328084240301f3a0bd2140a55d72e331bb4d75dd7e40be3971155dff910193bc
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5312_Solution_C.md
    sha256: 64ab17db61f41d71c9fab76cb8c0838b8cdcd81c4e35f7f240c71642196f0ff3
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5342_Solution_A.md
    sha256: 31d821180b177a4395ac64cfe2eb443091729cb74309085beeb1b765ed2dd2f2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5343_Solution_B.md
    sha256: a1f8fb64c671e4aae298c328e3a93b1ad420e2d60c7400dbae6775f8081a0e33
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_650_modified_for_dsm_8319.md
    sha256: f8616b950028d94561a0c4a986c40d5fdcdfa14324af5f8fa130447d9f7d7bdb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
    role: context
  - path: reports/yaml_record_review/20260922T063517Z-CEJFB1T_MEDIUM.md
    sha256: 1c833062655743da5d43f5f05638efd1b7bad9147a054541027cb892ea737379
    role: context
  - path: reports/yaml_record_review/20260922T063654Z-CELLULOLYTIC_NATRONOARCHAEA_MEDIUM.md
    sha256: 812641f1e5b20ca4a328fc409a8fd1f8cf18a1b8c740c904170097e764dd491a
    role: context
  - path: reports/yaml_record_review/20260922T063822Z-CELLULOMONAS_FERMENTANS_MEDIUM.md
    sha256: cde23788b5a2bdfea2e67768ac9f27f0ad5200aeccb4c3e6fd8af84b3ac70c14
    role: context
  - path: reports/yaml_record_review/20260922T063942Z-CELLULOSE_AGAR.md
    sha256: 7d7df31cd5aa0b65511048a3ad7ea51ed128f3d111280455da6b27b77deeff3a
    role: context
  - path: reports/yaml_record_review/20260922T064115Z-CELLULOSILYTICUM_MEDIUM.md
    sha256: b3996678c78481e187be45d3a239865ef844eff74fcc663396ac72e9b986aaef
    role: context
  - path: reports/yaml_record_review/20260922T064238Z-CELLULOSILYTICUM_RUMINICOLA_MEDIUM.md
    sha256: 0b2275d6cbeebebbd700d25e120994c47e980a94f276e53b82544cbf4ab4ddff
    role: context
  - path: reports/yaml_record_review/20260922T064616Z-CENS_MEDIUM.md
    sha256: 6358d704259dc7ba50caf8263a8e95c81f311c9618f805c8f60587de73d37d16
    role: context
  - path: reports/yaml_record_review/20260922T064817Z-CENTENUM_MEDIUM.md
    sha256: 5a517b2db46fa7608fa93b1fd6f7ca36633e65d9e9187b38ed2f820fc9ff5c4c
    role: context
  - path: reports/yaml_record_review/20260922T064954Z-CGM.md
    sha256: b50dfb754feed998bcc620cfe9162a90071733ad665f78825ce24a6a870fe143
    role: context
  - path: reports/yaml_record_review/20260922T065133Z-CGY_Medium.md
    sha256: f24f1ad05b4a65ae735f976877698aed5a3ffa1df9130d14103914260882ae5a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/audit_mim_sssom_divergence.py
    sha256: ad3478a5aeb757f2ce503be1b4720c86f0c1d90f5549918e1341dc7ac2c0f445
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_dsmz650_752_762_preparations.py
    sha256: 0b955dd562a885fec75dd73bed1eaa00af707b3e2f9d35f7f16b066feb743e1a
    role: context
  - path: scripts/repair_komodo650_752_762_preparations.py
    sha256: 477e2e14b5ff6284e4e291986b333552215f44dca2473fc64cf1d60e0028c0bd
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_public_stock_concentrations.py
    sha256: 220dafdb1b826063f533a4b7e41dc3f2576adc433be92c65243605255fb97bb1
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
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
  selection: Task review 527; batch 053 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fifty-two task batches
    contain 520 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 231e0ba71b41d45362168d539efebe7991823464
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 523 of 6325 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006399
targets:
- target_id: CultureMech:006399
  path: data/merge_yaml/merged/CENS_MEDIUM.yaml
  label: cens_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CENS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CENS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/527/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/527/strict.tsv"
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CENS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CENS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:006399
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
  - CultureMech:006399
- check_id: api748-source-access
  name: 'Exact source content access: api748'
  required: true
  status: unavailable
  summary: The exact current api748 capture returned HTTP 503; its maintenance/challenge
    body supplies no formulation. DSM748 remains usable, while independent current
    KOMODO formulation confirmation is unavailable. The failed attempt and original
    timestamp remain preserved.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - api748-attempt
- check_id: komodo748-source-access
  name: 'Exact source content access: komodo748'
  required: true
  status: unavailable
  summary: The exact current komodo748 capture returned HTTP 403; its maintenance/challenge
    body supplies no formulation. DSM748 remains usable, while independent current
    KOMODO formulation confirmation is unavailable. The failed attempt and original
    timestamp remain preserved.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - komodo748-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/CENS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/cens_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/CENS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:31.949025Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/CENS_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch053/527/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:36.019175Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-053/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch053/527/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/CENS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:40.401451Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/CENS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-25T20:10:43.299608Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-25T20:15:13Z'
  support: supports
  summary: './data/merge_yaml/merged/CENS_MEDIUM.yaml:1:id: CultureMech:006399

    ./data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml:1:id: CultureMech:006399

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/527/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-25T20:15:13Z'
  support: supports
  summary: 27 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: e66d7d21e9f1cc9501bdc4d8755343cb098c6188edd9ac37295ba7b3b65d3c5b
- evidence_id: source-reading
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/records527-528-source-reading-20261025T201126Z/source-reading.json
  locator: Complete selected documents, primary pages, fourteen historical reports
    and named current writer functions
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: The pinned reading receipt distinguishes complete source reads from derivative
    historical interpretation and from current writer behavior.
  snapshot_sha256: 3abfdc0608b7fe1ec45fe129effbc097de9262f7552d2edccbcaedf257015727
- evidence_id: context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/source-preflight-bound/527/evidence-context-original.json
  locator: Full per-record source context and scoped inventories
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Frozen local inventories, source captures, source-access outcomes and exact
    owner/parent scope; context is an index, not additional independent scientific
    evidence.
  snapshot_sha256: 3a7926f31e2654f8e93c94be59da388463f6afc8f28eec1bf96fcaaba876ce43
- evidence_id: dsm748-main
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf
  locator: Complete page 1 main recipe, rows 4–17
  accessed_at: '2026-10-22T09:27:20.100374Z'
  support: supports
  summary: Primary main recipe specifies original batch masses, two stock doses and
    listed water. It does not declare a measured final medium volume.
  quote: 748. CENS MEDIUM
  snapshot_sha256: 4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe
- evidence_id: dsm748-blue
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf
  locator: Page1 True Blue Trace Elements table and preparation, lines 19–33
  accessed_at: '2026-10-22T09:27:20.100374Z'
  support: supports
  summary: This stock is explicitly made to final 250 ml. The approximately 200 ml
    dissolution instruction belongs to this stock alone; source cobalt is the dihydrate.
  quote: 'Dissolve chemicals one at a time in approximately 200.0 ml distilled water.
    Bring final

    volume to 250.0 ml with additional water.'
  snapshot_sha256: 4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe
- evidence_id: dsm748-iron
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf
  locator: Page1 Chelated Iron solution, lines 35–39
  accessed_at: '2026-10-22T09:27:20.100374Z'
  support: supports
  summary: Iron stock lists 1 g FeCl2 tetrahydrate, 2 g EDTA, 3 ml concentrated HCl
    and 900 ml water; neither final stock volume nor HCl strength or density is specified.
  quote: ' HCl (conc.)                                                      3.0       ml'
  snapshot_sha256: 4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe
- evidence_id: api748-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/748
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:20.975631Z'
  support: context_only
  summary: The exact current api748 capture returned HTTP 503; its maintenance/challenge
    body supplies no formulation. DSM748 remains usable, while independent current
    KOMODO formulation confirmation is unavailable. The failed attempt and original
    timestamp remain preserved.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: komodo748-attempt
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=748
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-22T09:27:22.908679Z'
  support: context_only
  summary: The exact current komodo748 capture returned HTTP 403; its maintenance/challenge
    body supplies no formulation. DSM748 remains usable, while independent current
    KOMODO formulation confirmation is unavailable. The failed attempt and original
    timestamp remain preserved.
  snapshot_sha256: 2496453588dbad05bca956de242bc103fb0ab5aace6e3f3e5e36dfc7071e5657
- evidence_id: report-0
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_748_CENS_medium.yaml.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Oct 7 KOMODO report retained all 22 local quantities unresolved because
    main and stock stages were flattened. Its cited API748 raw digest is not recovered
    in the bounded parent search; decoded tables remain derivative.
  snapshot_sha256: 013cdd23597b0f17ae16040cfcff4fa5612704583733ff2b59f4575da6a5ef4e
- evidence_id: report-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/cens_medium.yaml.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Oct 7 DSM report likewise retained the unchanged 22-row owner and unresolved
    stock quantities. Agreement with the KOMODO report is not an independent raw capture.
  snapshot_sha256: 21cd5c7838ddcd4136764be9d06f0b560c3df459ffd3510ca5a9df7e1f34e292
- evidence_id: report-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CENS_MEDIUM.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Oct 5 generated-target inventory has0/22 source-checked concentrations;
    candidate same-slug records are not additional maintained owners.
  snapshot_sha256: 597cb6a7938f9cd459897adf69983dff16ed4d88f1a910366ad8abe4b3928222
- evidence_id: report-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_748_CENS_medium.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Oct 5 KOMODO-owner inventory has0/22 source-checked concentrations; no
    independent source confirmation.
  snapshot_sha256: a9c41ec015e0f2f45bb92ed0065eb0ddc3f3852207c12751d1ce686377ba8326
- evidence_id: report-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cens_medium.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Oct 5 DSM-owner inventory has0/22 source-checked concentrations; no independent
    source confirmation.
  snapshot_sha256: 874c7e795a7cd6cb420776fb624326f85520f9879d26165de81a0638506b1de2
- evidence_id: report-5
  kind: record_content
  reference: reports/yaml_record_review/20260922T064616Z-CENS_MEDIUM.md
  locator: Entire exact historical report; identity header, quantity table, decisions
    and limits
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Entire September review read. Its claimed source CoCl2 hexahydrate contradicts
    the current pinned PDF, which prints dihydrate. Its iron900ml final-volume and
    final-medium-rate assumptions are not source-established. Its stock-flattening
    discussion is historical context only.
  snapshot_sha256: 6358d704259dc7ba50caf8263a8e95c81f311c9618f805c8f60587de73d37d16
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit,
    _parse_preparation_steps
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Current import separates main composition from referenced stock additions
    and maps provider units. Unit mapping alone cannot establish final volume. Preparation
    parsing still iterates solution steps, so their receiving-medium versus stock
    scope must be preserved. These functions do not prove which historical version
    produced the assessed record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Current web import builds source identity and a composition placeholder;
    it does not independently verify a later copied DSM formulation. Its time.strftime
    format includes %f, consistent with the malformed literal history timestamp, but
    current source code alone does not establish historical execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Current resolver copies non-placeholder DSM ingredients and solutions plus
    missing pH. Copied DSM data are shared provenance, not independent confirmation
    of KOMODO or strain-specific equivalence; the function does not transfer complete
    preparation.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-3
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: merge_duplicate_ingredients; _merge_ingredient_group
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: 'Current duplicate cleanup explicitly does not sum concentration values:
    equal quantities may collapse and disagreements retain a representative with a
    warning. The old merged EDTA sum is not evidence that this current implementation
    still adds concentrations across preparation stages.'
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-4
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: 'Entire file: scientific projection, formulation_signature, merge_formulation_evidence'
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Current scientific comparison retains exact quantities, notes, preparation,
    solution structure and list order, and rejects incompatible formulations before
    provenance union. It is not an ingredient-only equivalence test.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-5
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Current merge_group invokes the exact scientific-formulation guard before
    combining evidence. Old generated content and old ingredient-signature merge history
    do not establish that the current guard would merge the now-divergent maintained
    owners.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:00:46.687620Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi132095
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132095
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-22T09:27:28.422781Z'
  support: supports
  summary: CHEBI:132095 resolves to sodium metavanadate hydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: 77717bffaef18e81d1e64ea049300d654783f6bec28ec5c58aef12d13c31b34d
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
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi4735
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_4735
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:28.659368Z'
  support: supports
  summary: CHEBI:4735 resolves to ethylenediaminetetraacetic acid. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: ef8713e257a5e52aa813d8a43a26ed321ff04a475591ff238c00a47758f96717
- evidence_id: chebi48843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:07:16.976958Z'
  support: supports
  summary: CHEBI:48843 resolves to disodium selenite. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: f8b54c90292c3ea1c215cbb96e7b9302304ba97f07c586c66f09b6689b9f2d91
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
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:08.324907Z'
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
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:43:09.378884Z'
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-25T20:15:13Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:132095": [{"label": "NaVO3 x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:132095", "preferred_term": "NaVO3 x H2O",
    "ontology_id": "CHEBI:132095", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier":
    "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type":
    "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12",
    "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}],
    "CHEBI:17883": [{"label": "HCl", "match_type": "preferred_term", "identifier":
    "CHEBI:17883", "preferred_term": "HCl", "ontology_id": "CHEBI:17883", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795":
    [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32150": [{"label":
    "Na2S2O3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32150",
    "preferred_term": "Na2S2O3 x 5 H2O", "ontology_id": "CHEBI:32150", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type":
    "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id":
    "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887":
    [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887",
    "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:35696": [{"label": "CoCl2", "match_type": "preferred_term",
    "identifier": "CHEBI:35696", "preferred_term": "CoCl2", "ontology_id": "CHEBI:35696",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:4735": [{"label":
    "EDTA", "match_type": "preferred_term", "identifier": "CHEBI:4735", "preferred_term":
    "EDTA", "ontology_id": "CHEBI:4735", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:48843": [{"label": "Na2SeO3", "match_type": "preferred_term",
    "identifier": "CHEBI:48843", "preferred_term": "Na2SeO3", "ontology_id": "CHEBI:48843",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49976": [{"label":
    "ZnCl2", "match_type": "preferred_term", "identifier": "CHEBI:49976", "preferred_term":
    "ZnCl2", "ontology_id": "CHEBI:49976", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term",
    "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id":
    "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86249": [{"label": "FeCl2 x 4 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86249", "preferred_term":
    "FeCl2 x 4 H2O", "ontology_id": "CHEBI:86249", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:86318": [{"label": "CuCl2 x 2 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86318", "preferred_term": "CuCl2 x 2 H2O", "ontology_id":
    "CHEBI:86318", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86368":
    [{"label": "MnCl2 x 4 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86368",
    "preferred_term": "MnCl2 x 4 H2O", "ontology_id": "CHEBI:86368", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/CENS_MEDIUM.yaml; data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml;
    data/normalized_yaml/bacterial/cens_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": [{"index": 1, "issue":
    "malformed timestamp", "value": "2026-01-27T01:15:03.fZ"}, {"index": 2, "issue":
    "timezone absent", "value": "2026-02-03T11:19:15.275332"}]}, {"input": "data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml",
    "events": 9, "timestamp_issues": [{"index": 1, "issue": "malformed timestamp",
    "value": "2026-01-27T01:15:03.fZ"}, {"index": 2, "issue": "timezone absent", "value":
    "2026-02-03T11:19:15.275332"}]}, {"input": "data/normalized_yaml/bacterial/cens_medium.yaml",
    "events": 9, "timestamp_issues": []}]'
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch053/527/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-25T20:15:13Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7ea441533aa08673690fcd58b5ddf85f701d71d02fe7444e16f165ecf2368534
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '21 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels across the selected target and its exact maintained
    owners. Target linkage: 21/22 primary and 21/22 secondary instances; all asserted
    current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Complete
    recursive inspection of these selected documents found zero legacy mediaingredientmech_term
    slots and zero numeric legacy MediaIngredientMech identifiers. Generic placeholder
    text in history is not an asserted identifier. Exact supplied-form mismatch is
    addressed separately; valid IDs and labels do not establish correct source grounding.'
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - record
  - mim
  - owner-0
  - owner-1
  - chebi131527
  - chebi132095
  - chebi15956
  - chebi176843
  - chebi17883
  - chebi31206
  - chebi31795
  - chebi32150
  - chebi33118
  - chebi34887
  - chebi35696
  - chebi4735
  - chebi48843
  - chebi49976
  - chebi50144
  - chebi63036
  - chebi75213
  - chebi86158
  - chebi86249
  - chebi86318
  - chebi86368
  details: 'Instance coverage on a 0–100 percent scale, denominator 22: primary 95.45%;
    secondary 95.45%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: concern
  summary: 29 timestamp instances inspected; 4 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - record
  - history-metadata
  - owner-0
  - owner-1
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 28 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"subject\": \"K2HPO4 main batch\
    \ input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n      \
    \  \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.9\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.9\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.9\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 4: K2HPO4\",\n\
    \        \"exact_source_quote\": \"K2HPO4                                    \
    \                        0.9       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 0.9,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q2\",\n    \"subject\"\
    : \"KH2PO4 main batch input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 5: KH2PO4\",\n\
    \        \"exact_source_quote\": \"KH2PO4                                    \
    \                        0.6       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 0.6,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"subject\"\
    : \"NH4Cl main batch input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 6: NH4Cl\",\n\
    \        \"exact_source_quote\": \"NH4Cl                                     \
    \                        1.0       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 1,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q4\",\n    \"subject\"\
    : \"EDTA separated across three preparation stages\",\n    \"decision\": \"conflict\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.22722\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.22722\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"12.22722\",\n          \"unit\": \"G_PER_L\"\n   \
    \     }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 7: EDTA\",\n\
    \        \"exact_source_quote\": \"EDTA                                      \
    \                        5.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 20: EDTA\",\n\
    \        \"exact_source_quote\": \" EDTA                                     \
    \                        2.5       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 37: EDTA\",\n\
    \        \"exact_source_quote\": \" EDTA                                     \
    \                        2.0        g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 39: Distilled\
    \ water\",\n        \"exact_source_quote\": \" Distilled water               \
    \                                 900.0       ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"12.22722 G_PER_L is the local sum of 0.005,10 and\
    \ 2.22222 values from different stages. Source supports 5 mg basal EDTA,2.5 g\
    \ in the final 250 ml True Blue stock and 2 g in the iron stock with 900 ml listed\
    \ water. Only True Blue supports 10 g/L stock arithmetic; iron 2/0.9 g/L is conditional\
    \ on an unproven final stock volume. No summed final-medium rate is established.\"\
    ,\n    \"proposed_source_representation\": {\n      \"main_batch\": {\n      \
    \  \"amount\": 5,\n        \"unit\": \"mg\"\n      },\n      \"True_Blue_stock\"\
    : {\n        \"amount\": 2.5,\n        \"unit\": \"g\",\n        \"explicit_final_volume_ml\"\
    : 250,\n        \"stock_rate_g_per_l\": 10\n      },\n      \"Chelated_Iron_stock\"\
    : {\n        \"amount\": 2,\n        \"unit\": \"g\",\n        \"water_input_ml\"\
    : 900,\n        \"final_volume\": \"unspecified\"\n      }\n    }\n  },\n  {\n\
    \    \"decision_id\": \"q5\",\n    \"subject\": \"MgSO4 main batch input\",\n\
    \    \"decision\": \"unsupported\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[4].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 8: MgSO4\",\n\
    \        \"exact_source_quote\": \"MgSO4 x 7 H2O                             \
    \                        0.2       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 0.2,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"subject\"\
    : \"CaCl2 main batch input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.075\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.075\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.075\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 9: CaCl2\",\n\
    \        \"exact_source_quote\": \"CaCl2 x 2 H2O                             \
    \                       75.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 75,\n      \"unit\": \"mg\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"subject\"\
    : \"Vitamin B12 main batch input\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2e-05\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 12: Vitamin B12\"\
    ,\n        \"exact_source_quote\": \"Vitamin B12                             \
    \                         20.0      μg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 20,\n      \"unit\": \"microgram\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q8\",\n    \"subject\"\
    : \"Biotin main batch input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5e-05\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5e-05\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5e-05\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 13: Biotin\"\
    ,\n        \"exact_source_quote\": \"Biotin                                  \
    \                         15.0      μg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 15,\n      \"unit\": \"microgram\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"subject\"\
    : \"Na2S2O3 main batch input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 14: Na2S2O3\"\
    ,\n        \"exact_source_quote\": \"Na2S2O3 x 5 H2O                         \
    \                          0.5       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 0.5,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"subject\"\
    : \"Soytone main batch input\",\n    \"decision\": \"unsupported\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 15: Soytone\"\
    ,\n        \"exact_source_quote\": \"Soytone (Difco 0436)                    \
    \                          4.0       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ \",\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 4,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"subject\"\
    : \"Na-pyruvate main batch input\",\n    \"decision\": \"unsupported\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 16: Na-pyruvate\"\
    ,\n        \"exact_source_quote\": \"Na-pyruvate (filter-sterilized)         \
    \                          2.2       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 17: Distilled\
    \ water\",\n        \"exact_source_quote\": \"Distilled water                \
    \                                1000.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The printed batch amount is supported; its stored\
    \ G_PER_L representation assumes a final medium denominator not declared by the\
    \ primary. Listed 1000 ml water plus stock additions must not silently become\
    \ a final 1 L or1.003L volume. No numeric error in the printed mass is inferred.\
    \ Filter sterilization is explicitly required for this sodium-pyruvate addition.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 2.2,\n      \"unit\": \"g\",\n      \"final_medium_volume\"\
    : \"unspecified\"\n    }\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"subject\"\
    : \"MnCl2 in True Blue stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 21: MnCl2\",\n\
    \        \"exact_source_quote\": \" MnCl2 x 4 H2O                            \
    \                        0.2       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. \",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 0.2,\n      \"batch_unit\": \"g\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.8,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q13\",\n    \"subject\": \"H3BO3 in True Blue stock\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 22: H3BO3\",\n\
    \        \"exact_source_quote\": \" H3BO3                                    \
    \                        0.1       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. \",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 0.1,\n      \"batch_unit\": \"g\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.4,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q14\",\n    \"subject\": \"Na2MoO4 in True Blue stock\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 23: Na2MoO4\"\
    ,\n        \"exact_source_quote\": \" Na2MoO4 x 2 H2O                        \
    \                          0.1       g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. \",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 0.1,\n      \"batch_unit\": \"g\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.4,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q15\",\n    \"subject\": \"ZnCl2 in True Blue stock\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 24: ZnCl2\",\n\
    \        \"exact_source_quote\": \" ZnCl2                                    \
    \                       50.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. \",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 50,\n      \"batch_unit\": \"mg\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.2,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q16\",\n    \"subject\": \"NiCl2 in True Blue stock\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 25: NiCl2\",\n\
    \        \"exact_source_quote\": \" NiCl2 x 6 H2O                            \
    \                       50.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. Source\
    \ hydrate identity requires separate reconciliation of both asserted term slots.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 50,\n      \"batch_unit\": \"mg\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.2,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q17\",\n    \"subject\": \"CoCl2 in True Blue stock\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.08\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 26: CoCl2\",\n\
    \        \"exact_source_quote\": \" CoCl2 x 2 H2O                            \
    \                       20.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. Source\
    \ hydrate identity requires separate reconciliation of both asserted term slots.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 20,\n      \"batch_unit\": \"mg\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.08,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q18\",\n    \"subject\": \"CuCl2 in True Blue stock\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.04\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 27: CuCl2\",\n\
    \        \"exact_source_quote\": \" CuCl2 x 2 H2O                            \
    \                       10.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. \",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 10,\n      \"batch_unit\": \"mg\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.04,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q19\",\n    \"subject\": \"Na2SeO3 in True Blue stock\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 28: Na2SeO3\"\
    ,\n        \"exact_source_quote\": \" Na2SeO3                                \
    \                          5.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. \",\n \
    \   \"proposed_source_representation\": {\n      \"stage\": \"True Blue Trace\
    \ Elements stock\",\n      \"batch_amount\": 5,\n      \"batch_unit\": \"mg\"\
    ,\n      \"explicit_final_volume_ml\": 250,\n      \"stock_rate_g_per_l\": 0.02,\n\
    \      \"receiving_batch_dose_ml\": 1\n    }\n  },\n  {\n    \"decision_id\":\
    \ \"q20\",\n    \"subject\": \"NaVO3 in True Blue stock\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 29: NaVO3\",\n\
    \        \"exact_source_quote\": \" NaVO3 x n H2O (meta)                     \
    \                        5.0      mg\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The stored number matches the concentration of this\
    \ ingredient in the explicitly final 250 ml stock, but it is currently asserted\
    \ as a direct medium concentration. Restore the named stock recipe and its 1 ml\
    \ batch addition. This does not establish a final-medium G_PER_L rate. Source\
    \ hydrate number remains unspecified for NaVO3 x n H2O.\",\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"True Blue Trace Elements stock\",\n      \"batch_amount\"\
    : 5,\n      \"batch_unit\": \"mg\",\n      \"explicit_final_volume_ml\": 250,\n\
    \      \"stock_rate_g_per_l\": 0.02,\n      \"receiving_batch_dose_ml\": 1\n \
    \   }\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"subject\": \"FeCl2 tetrahydrate\
    \ in chelated iron stock\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.11111\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.11111\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.11111\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 36: FeCl2\",\n\
    \        \"exact_source_quote\": \" FeCl2 x 4 H2O                            \
    \                        1.0        g\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 39: Distilled\
    \ water\",\n        \"exact_source_quote\": \" Distilled water               \
    \                                 900.0       ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 11: Chelated\
    \ Iron\",\n        \"exact_source_quote\": \"Chelated Iron solution (see below)\
    \                                2.0      ml\",\n        \"snapshot_sha256\":\
    \ \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The source places 1 g in a stock made with 900 ml\
    \ listed water, dosed 2 ml into the main batch. Stored 1.11111 G_PER_L is a stock-water\
    \ normalization flattened into the medium; neither an exact stock final volume\
    \ nor a final-medium rate is established.\",\n    \"proposed_source_representation\"\
    : {\n      \"stage\": \"Chelated Iron solution\",\n      \"amount\": 1,\n    \
    \  \"unit\": \"g\",\n      \"water_input_ml\": 900,\n      \"receiving_batch_dose_ml\"\
    : 2,\n      \"final_stock_volume\": \"unspecified\"\n    }\n  },\n  {\n    \"\
    decision_id\": \"q22\",\n    \"subject\": \"Concentrated HCl volume in chelated\
    \ iron stock\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/CENS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[21].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 38: HCl\",\n\
    \        \"exact_source_quote\": \" HCl (conc.)                              \
    \                        3.0       ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 39: Distilled\
    \ water\",\n        \"exact_source_quote\": \" Distilled water               \
    \                                 900.0       ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Source 3 ml concentrated HCl is a volume input to\
    \ the iron stock, not 3 g/L in the medium. Acid strength, density, final stock\
    \ volume and final-medium rate are not specified; no mass conversion is proposed.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"Chelated Iron\
    \ solution\",\n      \"amount\": 3,\n      \"unit\": \"ml\",\n      \"strength\"\
    : \"concentrated; numeric strength unspecified\"\n    }\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"subject\": \"True Blue receiving dose\",\n    \"decision\":\
    \ \"add\",\n    \"local_fields\": [],\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 10: True Blue\"\
    ,\n        \"exact_source_quote\": \"True Blue Trace elements (see below)    \
    \                          1.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Missing source-explicit volume or stock-addition representation.\
    \ Treat this as the printed batch input; no unspecified final-volume normalization.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 1,\n      \"unit\": \"ml\",\n      \"basis\": \"batch input\"\
    \n    }\n  },\n  {\n    \"decision_id\": \"q24\",\n    \"subject\": \"Chelated\
    \ iron receiving dose\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz748\",\n \
    \       \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 11: Chelated\
    \ Iron\",\n        \"exact_source_quote\": \"Chelated Iron solution (see below)\
    \                                2.0      ml\",\n        \"snapshot_sha256\":\
    \ \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Missing source-explicit volume or stock-addition representation.\
    \ Treat this as the printed batch input; no unspecified final-volume normalization.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 2,\n      \"unit\": \"ml\",\n      \"basis\": \"batch input\"\
    \n    }\n  },\n  {\n    \"decision_id\": \"q25\",\n    \"subject\": \"Main distilled-water\
    \ input\",\n    \"decision\": \"add\",\n    \"local_fields\": [],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\",\n        \"\
    source_locator\": \"PDF page 1; extracted text line 17: Distilled water\",\n \
    \       \"exact_source_quote\": \"Distilled water                            \
    \                    1000.0      ml\",\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Missing source-explicit volume or stock-addition representation.\
    \ Treat this as the printed batch input; no unspecified final-volume normalization.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"main batch\"\
    ,\n      \"amount\": 1000,\n      \"unit\": \"ml\",\n      \"basis\": \"batch\
    \ input\"\n    }\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"subject\": \"\
    True Blue stock water/final makeup\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz748\"\
    ,\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 30: Distilled\
    \ water\",\n        \"exact_source_quote\": \" Distilled water               \
    \                                 250.0      ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      },\n \
    \     {\n        \"source_key\": \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Missing source-explicit volume or stock-addition representation.\
    \ The following preparation explicitly makes this stock to final 250 ml.\",\n\
    \    \"proposed_source_representation\": {\n      \"stage\": \"True Blue stock\"\
    ,\n      \"amount\": 250,\n      \"unit\": \"ml\",\n      \"basis\": \"explicit\
    \ final stock volume\"\n    }\n  },\n  {\n    \"decision_id\": \"q27\",\n    \"\
    subject\": \"Chelated iron water input\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"dsmz748\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text line 39: Distilled\
    \ water\",\n        \"exact_source_quote\": \" Distilled water               \
    \                                 900.0       ml\",\n        \"snapshot_sha256\"\
    : \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\",\n    \
    \    \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"Missing source-explicit volume or stock-addition representation.\
    \ Treat this as the printed batch input; no unspecified final-volume normalization.\"\
    ,\n    \"proposed_source_representation\": {\n      \"stage\": \"Chelated Iron\
    \ stock\",\n      \"amount\": 900,\n      \"unit\": \"ml\",\n      \"basis\":\
    \ \"batch input\"\n    }\n  },\n  {\n    \"decision_id\": \"q28\",\n    \"subject\"\
    : \"True Blue preparation scope\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].step_number\",\n        \"stored\"\
    : 1\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/cens_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve chemicals one at a time in approximately 200.0 ml distilled water.\
    \ Bring final volume to 250.0 ml with additional water.\"\n      }\n    ],\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"dsmz748\",\n  \
    \      \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium748.pdf\"\
    ,\n        \"source_locator\": \"PDF page 1; extracted text lines 32–33\",\n \
    \       \"exact_source_quote\": \"Dissolve chemicals one at a time in approximately\
    \ 200.0 ml distilled water. Bring final\\nvolume to 250.0 ml with additional water.\"\
    ,\n        \"snapshot_sha256\": \"4c7e8f7b7365af01d829f8923c020372e730a23d31308ccaa55f1516a7450cfe\"\
    ,\n        \"parsed_text_sha256\": \"0ea6a76aa10f10562b6b50d35a6c81ddc3202e10b182f6b40d8d37d8dfce9eab\"\
    ,\n        \"accessed_at\": \"2026-10-22T09:27:20.100374+00:00\"\n      }\n  \
    \  ],\n    \"rationale\": \"The retained text is accurate but belongs to the True\
    \ Blue stock, not the whole CENS medium. Preserve its sequence number as local\
    \ ordering metadata and attach the approximately 200 ml dissolution/final 250\
    \ ml makeup to that stock; target and KOMODO owner currently lack it.\",\n   \
    \ \"proposed_source_representation\": {\n      \"stage\": \"True Blue stock preparation\"\
    ,\n      \"initial_water_ml_approx\": 200,\n      \"explicit_final_volume_ml\"\
    : 250\n    }\n  }\n]"
- assessment_id: identity
  area: identity
  topic: DSM748 and copied KOMODO source identity
  outcome: supported
  summary: CENS corresponds to the current DSM748 primary. KOMODO owner provenance
    explicitly copies DSM composition, which explains shared data without independently
    proving current KOMODO formulation equivalence. Current web/API access is unavailable.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsm748-main
  - api748-attempt
  - komodo748-attempt
- assessment_id: source-preparation
  area: completeness
  topic: Stock boundaries, preparation and evidence placement
  outcome: concern
  summary: The primary supplies both stock recipes and doses. The DSM owner retains
    True Blue makeup text but at medium level; the target and KOMODO owner omit it.
    Sodium pyruvate filter sterilization is absent locally. No pH, autoclave program
    or growth condition is invented.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - dsm748-main
  - dsm748-blue
  - dsm748-iron
  - owner-1
  - quantity-inventory
- assessment_id: historical-support
  area: evidence
  topic: Historical report interpretation versus exact source
  outcome: concern
  summary: All six reports were read. API748 remains unrecovered within the pinned
    bounded parent search; the October tables are derivative. The September cobalt-hexahydrate
    claim and iron final-volume arithmetic are not adopted. The current primary page
    is the basis for the present findings.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - report-0
  - report-1
  - report-2
  - report-3
  - report-4
  - report-5
  - dsm748-blue
  - dsm748-iron
  - context
- assessment_id: classification
  area: scope
  topic: Record type, category and growth claims
  outcome: unknown
  summary: The selected documents are bacterial liquid MediaRecipe records. The bounded
    collection formulation establishes a recipe identity, not strain-specific experimental
    growth. No organism growth assertion, incubation optimum or literature-wide evidence
    claim is added.
  target_ids:
  - CultureMech:006399
  evidence_ids:
  - record
  - dsm748-main
findings:
- finding_id: f1
  issue_key: CENS_STOCK_STAGES
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate the flattened stocks and EDTA sum
  description: All three documents flatten True Blue and chelated iron ingredients
    into direct medium G_PER_L values and retain an EDTA sum across three preparation
    stages. The explicit True Blue final 250 ml supports stock rates only; main and
    iron listed-water amounts do not establish final volumes. HCl is 3 ml within iron
    stock, not 3 g/L medium.
  target_ids:
  - CultureMech:006399
  field_paths:
  - ingredients[3].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[21].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsm748-main
  - dsm748-blue
  - dsm748-iron
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: SOURCE_STAGE_AND_DIMENSION
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CENS_SUPPLIED_HYDRATES
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile nickel and cobalt hydrate mappings
  description: NiCl2 x 6 H2O and CoCl2 x 2 H2O are explicitly printed, while both
    primary and secondary slots assert anhydrous CHEBI:34887 and CHEBI:35696. The
    local preferred cobalt dihydrate text is correct; the historical claim that the
    primary specifies a hexahydrate is not. Source vanadate nH2O additionally leaves
    monohydrate specificity unresolved.
  target_ids:
  - CultureMech:006399
  field_paths:
  - ingredients[15].term
  - ingredients[15].mediaingredientmech_chebi_term
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm748-blue
  - chebi34887
  - chebi35696
  - chebi132095
  - mim
  - report-5
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: SOURCE_FORM_CORRESPONDENCE
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CENS_PREPARATION_SCOPE
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Keep stock makeup and pyruvate sterilization at their own stages
  description: The DSM owner contains True Blue approximately 200 ml/final 250 ml
    makeup as top-level preparation, while the other layers omit it. The primary separately
    marks sodium pyruvate filter-sterilized. These are stage-specific details, not
    instructions to prepare the entire medium at 250 ml.
  target_ids:
  - CultureMech:006399
  field_paths:
  - preparation_steps
  - ingredients[10]
  - solutions
  evidence_ids:
  - owner-1
  - dsm748-main
  - dsm748-blue
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: PREPARATION_STAGE_PLACEMENT
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CENS_HISTORY_TIMESTAMP
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve and qualify malformed import timestamps
  description: The target and KOMODO owner retain a timestamp with a literal .fZ suffix.
    It is not a valid UTC instant. Preserve original history and add a bounded clarification
    rather than replacing it with a guessed access or execution time.
  target_ids:
  - CultureMech:006399
  field_paths:
  - curation_history
  evidence_ids:
  - history-metadata
  - writer-1
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: PROVENANCE_TIMESTAMP_SHAPE
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore both named stock recipes and source batch doses in the maintained
    owners, separate each EDTA occurrence, and preserve unsupported final-volume bases
    as unresolved. Rebuild the target only after exact formulation comparison.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006399
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
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
  description: Reconcile the two supplied hydrate mappings against explicit source
    forms and current ontology evidence. Resolve vanadate specificity without inventing
    n; retain ingredient names and sources. Do not substitute a new identifier without
    verifying its exact definition.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006399
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
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
  description: Retain the existing stock instruction but move or scope it to True
    Blue; represent source pyruvate filter sterilization without inventing its timing,
    a basal autoclave program or final medium volume.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006399
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
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
  description: Append a provenance clarification for the malformed timestamp and verify
    the current timestamp writer separately; keep all original source access times
    and historical bytes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006399
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cens_medium.yaml
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
- The exact current api748 capture returned HTTP 503; its maintenance/challenge body
  supplies no formulation. DSM748 remains usable, while independent current KOMODO
  formulation confirmation is unavailable. The failed attempt and original timestamp
  remain preserved.
- The exact current komodo748 capture returned HTTP 403; its maintenance/challenge
  body supplies no formulation. DSM748 remains usable, while independent current KOMODO
  formulation confirmation is unavailable. The failed attempt and original timestamp
  remain preserved.
- No exact historical API748 response was recovered on the twelve explicitly searched
  JSON parent surfaces; this is a bounded result, not universal absence.
- No direct growth publication or strain-specific performance evidence was assessed.
  The preserved references and classification do not establish growth.
- True Blue final stock volume is explicit; main and iron stock final volumes are
  not. No exact diluted final-medium rates are asserted.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-053
- generated-medium
```
