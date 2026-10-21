# Source and formulation review: autotrophic_nitrobacter_medium (CultureMech:008936)

- Review: 20261021T201900Z-culturemech-008936-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T20:11:22Z
- Finished UTC: 2026-10-21T20:19:00Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 756c explicitly defines the autotrophic branch, but both local layers flatten its two stocks, mislabel water and stock doses as gram rates, and point to unrelated solution records. The primary recipe resolves the receiving formulation and preparation; unavailable historical 6127 bytes remain a bounded limitation on the unrelated dependency.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 369; batch 037 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-six task batches contain 360 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 363 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008936 | data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml | generated | autotrophic_nitrobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008936 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008936 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/369/strict.tsv |
| validate-terms | passed | True | CultureMech:008936 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008936 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008936 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadive756capi | unavailable | False | CultureMech:008936 | Preserved optional mediadive756capi attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| Exact source content access: mediadive756capi_retry | unavailable | False | CultureMech:008936 | Preserved optional mediadive756capi_retry attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| Exact source content access: solution6127 | unavailable | False | CultureMech:008936 | Preserved optional solution6127 attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| Exact source content access: solution6127_retry | unavailable | False | CultureMech:008936 | Preserved optional solution6127_retry attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008936.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008936.

21 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "Receiving recipe: Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2899.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2899.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, main formulation",
        "exact_source_quote": "Distilled water 899.00 ml",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 899,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "water_input_ml": 899,
      "measured_final_volume_L": null
    },
    "rationale": "Restore the literal volume and receiving stage; 899 + 100 + 1 = 1000 mL is a sum of listed liquids, not measured final volume. Stock preparation water must not be added to receiving water. The present G_PER_L encoding is not the source volume."
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Receiving recipe: NaNO2",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf",
        "source_locator": "Page 1, variant nitrite rate",
        "exact_source_quote": "2 g/l NaNO2",
        "snapshot_sha256": "95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda",
        "parsed_text_sha256": "c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686",
        "accessed_at": "2026-10-21T19:52:51.219574Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaNO2\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "sodium_nitrite_g_per_L": 2,
      "measured_final_volume_L": null
    },
    "rationale": "The primary explicitly supports the unchanged 2 g/L nitrite but no matching local evidence is attached."
  },
  {
    "quantity_id": "q3",
    "component_or_context": "Receiving recipe: Trace element solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, main formulation",
        "exact_source_quote": "Trace element solution 1.00 ml",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "trace_stock_addition_ml": 1,
      "measured_final_volume_L": null
    },
    "rationale": "Restore the literal volume and receiving stage; 899 + 100 + 1 = 1000 mL is a sum of listed liquids, not measured final volume. Stock preparation water must not be added to receiving water. The present G_PER_L encoding is not the source volume."
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Receiving recipe: Stock solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, main formulation",
        "exact_source_quote": "Stock solution 100.00 ml",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Stock solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "basal_stock_addition_ml": 100,
      "measured_final_volume_L": null
    },
    "rationale": "Restore the literal volume and receiving stage; 899 + 100 + 1 = 1000 mL is a sum of listed liquids, not measured final volume. Stock preparation water must not be added to receiving water. The present G_PER_L encoding is not the source volume."
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Trace element stock: Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2899.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2899.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; water line",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 1000,
      "unit": "ml",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Trace element stock: H3BO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "49.4",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "49.4",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; H3BO3",
        "exact_source_quote": "H3BO3 49.40 mg",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 49.4,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 49.4,
      "unit": "mg",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Trace element stock: FeSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "97.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "97.3",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; FeSO4 x 7 H2O",
        "exact_source_quote": "FeSO4 x 7 H2O 97.30 mg",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"FeSO4 x 7 H2O\",\n          \"volume\": 97.3,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 97.3,
      "unit": "mg",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Trace element stock: ZnSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "43.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "43.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; ZnSO4 x 7 H2O",
        "exact_source_quote": "ZnSO4 x 7 H2O 43.10 mg",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"ZnSO4 x 7 H2O\",\n          \"volume\": 43.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 43.1,
      "unit": "mg",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Trace element stock: CuSO4 x 5 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; CuSO4 x 5 H2O",
        "exact_source_quote": "CuSO4 x 5 H2O 25.00 mg",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"CuSO4 x 5 H2O\",\n          \"volume\": 25,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 25,
      "unit": "mg",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Trace element stock: MnSO4 x H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "33.8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "33.8",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; MnSO4 x H2O",
        "exact_source_quote": "MnSO4 x H2O 33.80 mg",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"MnSO4 x H2O\",\n          \"volume\": 33.8,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 33.8,
      "unit": "mg",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q11",
    "component_or_context": "Trace element stock: (NH4)6Mo7O24",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "37.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "37.1",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Trace element solution subsection; (NH4)6Mo7O24",
        "exact_source_quote": "(NH4)6Mo7O24 37.10 mg",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"(NH4)6Mo7O24\",\n          \"volume\": 37.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 37.1,
      "unit": "mg",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 1,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q12",
    "component_or_context": "Basal stock: Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2899.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2899.0",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Stock solution subsection; water line",
        "exact_source_quote": "Distilled water 1000.00 ml",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 1000,
      "unit": "ml",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 100,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q13",
    "component_or_context": "Basal stock: MgSO4 x 7 H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Stock solution subsection; MgSO4 x 7 H2O",
        "exact_source_quote": "MgSO4 x 7 H2O 0.50 g",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4 x 7 H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 0.5,
      "unit": "g",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 100,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q14",
    "component_or_context": "Basal stock: NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Stock solution subsection; NaCl",
        "exact_source_quote": "NaCl 5.00 g",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 5,
      "unit": "g",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 100,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q15",
    "component_or_context": "Basal stock: KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Stock solution subsection; KH2PO4",
        "exact_source_quote": "KH2PO4 1.50 g",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 1.5,
      "unit": "g",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 100,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q16",
    "component_or_context": "Basal stock: CaCO3",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "0.07",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf",
        "source_locator": "Page 1, Stock solution subsection; CaCO3",
        "exact_source_quote": "CaCO3 0.07 g",
        "snapshot_sha256": "25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a",
        "parsed_text_sha256": "c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1",
        "accessed_at": "2026-10-21T19:53:28.862593Z"
      },
      {
        "source_key": "togoM2351original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CaCO3\",\n          \"volume\": 0.07,\n          \"unit\": \"g\"",
        "snapshot_sha256": "29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f",
        "accessed_at": "2026-10-21T19:52:50.266514Z"
      }
    ],
    "proposed_source_representation": {
      "stock_batch_amount": 0.07,
      "unit": "g",
      "stock_water_input_ml": 1000,
      "stock_final_volume_ml": null,
      "receiving_dose_ml": 100,
      "calculated_final_concentration": null
    },
    "rationale": "Restore this named stock batch and remove the receiving-scope duplicate. The six trace masses are mg, not g; basal stock masses are not direct receiving concentrations. The source lists water 1000 mL but no final-volume make-up, so neither stock nor receiving concentrations are calculated from that volume alone."
  },
  {
    "quantity_id": "q17",
    "component_or_context": "Explicitly omitted parent organic ingredients",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[12]",
        "stored": null,
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "ingredients[12]",
        "stored": null,
        "decision": "evidence_only"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf",
        "source_locator": "Page 1, 756c variant exclusions",
        "exact_source_quote": "omit yeast extract, peptone, and Na-pyruvate.",
        "snapshot_sha256": "95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda",
        "parsed_text_sha256": "c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686",
        "accessed_at": "2026-10-21T19:52:51.219574Z"
      }
    ],
    "proposed_source_representation": {
      "omitted_components": [
        "yeast extract",
        "peptone",
        "Na-pyruvate"
      ],
      "parent_amounts_not_transferred": true
    },
    "rationale": "The current receiving layers already omit the three parent organic additions. Preserve that branch; no zero concentration or parent organic dose is inserted."
  },
  {
    "quantity_id": "q18",
    "component_or_context": "Initial adjustment pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf",
        "source_locator": "Page 1, 756c preparation paragraph",
        "exact_source_quote": "Adjust pH to 8.6 with NaOH or KOH.",
        "snapshot_sha256": "95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda",
        "parsed_text_sha256": "c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686",
        "accessed_at": "2026-10-21T19:52:51.219574Z"
      }
    ],
    "proposed_source_representation": {
      "stage": "before autoclaving",
      "pH": 8.6
    },
    "rationale": "Both layers omit this explicitly documented staged condition. Keep the initial and later pH distinct; do not substitute the parent pH 7.4 as the whole variant protocol."
  },
  {
    "quantity_id": "q19",
    "component_or_context": "Standing duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf",
        "source_locator": "Page 1, 756c preparation paragraph",
        "exact_source_quote": "2 - 3",
        "snapshot_sha256": "95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda",
        "parsed_text_sha256": "c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686",
        "accessed_at": "2026-10-21T19:52:51.219574Z"
      }
    ],
    "proposed_source_representation": {
      "stage": "after autoclaving",
      "duration_days": [
        2,
        3
      ]
    },
    "rationale": "Both layers omit this explicitly documented staged condition. Keep the initial and later pH distinct; do not substitute the parent pH 7.4 as the whole variant protocol."
  },
  {
    "quantity_id": "q20",
    "component_or_context": "Resulting pH interval",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf",
        "source_locator": "Page 1, 756c preparation paragraph",
        "exact_source_quote": "pH 7.4 - 7.6.",
        "snapshot_sha256": "95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda",
        "parsed_text_sha256": "c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686",
        "accessed_at": "2026-10-21T19:52:51.219574Z"
      }
    ],
    "proposed_source_representation": {
      "stage": "after standing",
      "pH_range": [
        7.4,
        7.6
      ]
    },
    "rationale": "Both layers omit this explicitly documented staged condition. Keep the initial and later pH distinct; do not substitute the parent pH 7.4 as the whole variant protocol."
  },
  {
    "quantity_id": "q21",
    "component_or_context": "Adjustment reagent and autoclave cycle limits",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "source_snippets": [
      {
        "source_key": "dsmz756c",
        "source_url": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf",
        "source_locator": "Page 1, 756c preparation paragraph",
        "exact_source_quote": "NaOH or KOH. Autoclave",
        "snapshot_sha256": "95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda",
        "parsed_text_sha256": "c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686",
        "accessed_at": "2026-10-21T19:52:51.219574Z"
      }
    ],
    "proposed_source_representation": {
      "NaOH_or_KOH_dose": null,
      "temperature_C": null,
      "duration_min": null
    },
    "rationale": "Recover the stated alternative adjustment reagent and autoclaving, without invented reagent concentration, dose or cycle values."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:008936.

13 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 12/12 primary and 11/12 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 12: primary 100.00%; secondary 91.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008936.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact variant and two incorrectly linked stocks

identity: concern. Targets: CultureMech:008936.

CultureMech:008936 and its sole maintained owner identify TOGO M2351 / DSMZ 756c. The primary explicitly delegates the 756 stock definitions but omits its organics and changes preparation. MediaDive 6187 is an EDTA/chloride trace stock; local 6127 is a nitrate/phosphate stock. Their generic names do not establish equivalence to the source sulfate/borate trace and CaCO3/NaCl/MgSO4/KH2PO4 stock. All exact local paths and stable IDs resolve, but the scientific links are wrong.

### Heptamolybdate stoichiometry and magnesium hydration

grounding: concern. Targets: CultureMech:008936.

The printed (NH4)6Mo7O24 is ammonium heptamolybdate, whereas CHEBI:91249 encodes the 2:1 ammonium/orthomolybdate salt, formula 2H4N.MoO4. This is a stoichiometry mismatch despite a plausible canonical label. Magnesium’s primary CHEBI:31795 matches the heptahydrate, but its current secondary CHEBI:32599 omits that hydrate; align exact-form linkage after source verification. Iron, zinc, copper and manganese sulfate hydrates otherwise match the printed stock forms. Do not borrow hydrate or ion identities from unrelated linked stocks or invent a replacement heptamolybdate ID.

### Variant preparation and quantities

completeness: concern. Targets: CultureMech:008936.

Neither layer retains the primary initial pH 8.6 adjustment with NaOH or KOH, autoclaving, standing 2–3 days and later pH 7.4–7.6. No cycle temperature/time is printed. The parent pH 7.4 is overridden, and its yeast extract, peptone and pyruvate amounts do not transfer. No measured final stock or receiving volume is asserted from listed water or summed liquids.

### Defined inorganic branch and high-metal signal

scope: concern. Targets: CultureMech:008936.

The exact branch consists of specified inorganic salts after removing parent complex organics; COMPLEX/UNDEFINED is inconsistent with this defined formulation. LIQUID is compatible with no gelling agent. high_metal requires reassessment after fixing units/stages and links: six stock milligram amounts are currently represented as direct g/L, and other stock amounts are also flattened. A source-scoped, unit-aware recalculation must precede any Boolean decision; this review does not assert that the corrected medium must have a false flag. Neither the title nor annotations establish an organism phenotype or growth outcome.

### Historical evidence and source scope

provenance: concern. Targets: CultureMech:008936.

The receiving target and owner have no amount evidence; nine attached objects occur only in the two linked stock records. Six 6187 snippets match the available raw hash, while three 6127 objects remain derivative-only after bounded attempts/search. Source links must be corrected without transferring those objects to the delegated stocks. Preserve all import/migration/cleanup and stock-curation events append-only; the referenced stocks are contextual identities, not additional reviewed targets.

## Findings

### f1: Stock water and solutes are flattened into the receiving recipe

blocker / open / confirmed; issue key: culturemech.008936.stock-stage-unit-collapse.

Both layers merge 899 + 1000 + 1000 mL water into 2899 G_PER_L, promote six trace-stock mg inputs to direct g/L, retain four basal-stock masses as direct receiving rates and encode 1/100 mL stock doses as G_PER_L. This destroys source units and stages. The 2 g/L sodium nitrite is explicitly primary-supported but lacks attached evidence.

### f2: Two generic stock names point to different formulations

blocker / open / confirmed; issue key: culturemech.008936.wrong-stock-identities.

The trace link 6187 resolves to EDTA/chloride salts, while the delegated stock uses sulfate/borate/heptamolybdate. Local 6127 contains nitrate and hydrogen phosphates instead of the CaCO3/NaCl/MgSO4/KH2PO4 stock. All paths can exist while the intended formulations differ.

### f3: Heptamolybdate and magnesium linkage need exact-form grounding

major / open / confirmed; issue key: culturemech.008936.stock-molecular-forms.

The source ammonium heptamolybdate formula differs from CHEBI:91249 orthomolybdate. The primary magnesium hydrate is already correct while its secondary key remains anhydrous/generic.

### f4: The variant’s staged pH and sterilization instructions are absent

major / open / confirmed; issue key: culturemech.008936.variant-preparation.

The available primary specifies adjustment to pH 8.6, autoclaving, and standing 2–3 days until pH 7.4–7.6; neither layer retains this sequence.

### f5: The defined inorganic variant is classified as complex

major / open / confirmed; issue key: culturemech.008936.classification-after-stock-repair.

The source explicitly removes the parent organic mixtures and leaves specified inorganic components, contrary to COMPLEX/UNDEFINED. The high-metal flag is also confounded by flattened mg/g and stock scope.

## Recommended Actions And Acceptance Checks

### a1

Restore separate stock batches and volume additions, the 899 mL receiving water and exact mg/g inputs. Remove duplicated direct stock components. Attach literal scoped evidence; do not infer stock make-up or measured final volume from water inputs.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Detach unsupported stock identifiers and recover the exact source-scoped definitions through verified inline stocks or exact maintained identities. Preserve unrelated stock records and their evidence; do not reuse them solely because names match.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the printed heptamolybdate formula and resolve an exact supported term without guessing. Align the magnesium secondary key with the source hydrate and current primary term; keep amount correction separate.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add the exact staged preparation with narrow source evidence, retaining unknown autoclave temperature/time and adjustment reagent doses. Do not collapse initial and later pH into an unsupported single value.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Represent the exact defined branch and recompute any metal classification only after source units and stages are restored using an explicit justified method. Do not blindly retain or clear high_metal.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch037/369/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch037/369/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml:1:id: CultureMech:008936<br>./data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml:1:id: CultureMech:008936<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch037/source-preflight-bound/369/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 31 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch037/source-preflight-bound/369/evidence-context-original.json; Complete frozen source context and full local objects | context_only | Frozen target/owner objects match freshly inspected records. Source interpretations are assessed against actual bound capture bytes; historical limitations remain separate. |
| variant | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf; Page 1, complete 756c variant paragraph | supports | The primary adds 2 g/L sodium nitrite, omits yeast extract/peptone/pyruvate, and specifies initial pH 8.6, autoclaving and standing 2–3 days until pH 7.4–7.6. No temperature/time or reagent dose is supplied. |
| parent | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf; Page 1, main stock doses and Stock solution / Trace element solution subsections | supports | Only the delegated basal stock definitions and doses transfer to 756c. The parent organic additions are explicitly omitted and its pH instruction is overridden. Listed water is not explicit stock make-up or measured final volume. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351; $.meta, $.components[0:3], $.comments[0] | supports | The provider preserves main 899 mL water, 2 g nitrite, 1 mL trace and 100 mL stock, with both recipes separately. The primary independently states nitrite as 2 g/L. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch037/369/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi3311 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:3311 resolves to calcium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:33118 resolves to boric acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi78870 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_78870; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:78870 resolves to sodium nitrite. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91249; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91249 resolves to ammonium molybdate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term", "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id": "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311": [{"label": "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311", "preferred_term": "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:78870": [{"label": "NaNO2", "match_type": "preferred_term", "identifier": "CHEBI:78870", "preferred_term": "NaNO2", "ontology_id": "CHEBI:78870", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| dependency-6187 | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; Entire referenced SolutionRecipe; composition, preparation, evidence and history | context_only | Exact local linked stock read for identity comparison only. Its component evidence does not transfer to DSMZ 756c. |
| dependency-6127 | data/normalized_yaml/bacterial/mediadive_6127_Stock_solution.yaml; Entire referenced SolutionRecipe; composition, preparation, evidence and history | context_only | Exact local linked stock read for identity comparison only. Its component evidence does not transfer to DSMZ 756c. |
| linked6187 | https://mediadive.dsmz.de/rest/solution/6187; $.data.id, volume, recipe and steps | supports | 6187 explicitly contains EDTA and chloride salts, differing from the delegated 756 sulfate/borate/heptamolybdate trace recipe. Six current dependency snippets and their cited historical hash match these available raw bytes, supporting that stock only. |
| dependency-evidence | /private/tmp/culturemech-review-work-batch037/369/dependency-evidence-inventory.json; Six authenticated 6187 claims and three derivative-only 6127 claims | context_only | Six exact raw/cited-hash matches authenticate the EDTA/chloride stock only; the three nitrate/phosphate claims remain local derivatives. Neither is the source-delegated 756 stock. |
| mediadive756capi-attempt | https://mediadive.dsmz.de/rest/medium/756c; Preserved exact public retrieval result | context_only | Preserved optional mediadive756capi attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| mediadive756capi_retry-attempt | https://mediadive.dsmz.de/rest/medium/756c; Preserved exact public retrieval result | context_only | Preserved optional mediadive756capi_retry attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| solution6127-attempt | https://mediadive.dsmz.de/rest/solution/6127; Preserved exact public retrieval result | context_only | Preserved optional solution6127 attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| solution6127_retry-attempt | https://mediadive.dsmz.de/rest/solution/6127; Preserved exact public retrieval result | context_only | Preserved optional solution6127_retry attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions inspected without execution. TOGO now distinguishes primary sections and named stocks but its water-anchor normalization is not experimental final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based solution migration is insufficient identity evidence. Metal classification uses heuristic compound amounts and a corpus threshold, with a separate writer. Historical local transformations are preserved, not causally reconstructed from current code. |
| writer-1 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions inspected without execution. TOGO now distinguishes primary sections and named stocks but its water-anchor normalization is not experimental final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based solution migration is insufficient identity evidence. Metal classification uses heuristic compound amounts and a corpus threshold, with a separate writer. Historical local transformations are preserved, not causally reconstructed from current code. |
| writer-2 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions inspected without execution. TOGO now distinguishes primary sections and named stocks but its water-anchor normalization is not experimental final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based solution migration is insufficient identity evidence. Metal classification uses heuristic compound amounts and a corpus threshold, with a separate writer. Historical local transformations are preserved, not causally reconstructed from current code. |
| writer-3 | scripts/analyze_metal_concentrations.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions inspected without execution. TOGO now distinguishes primary sections and named stocks but its water-anchor normalization is not experimental final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based solution migration is insufficient identity evidence. Metal classification uses heuristic compound amounts and a corpus threshold, with a separate writer. Historical local transformations are preserved, not causally reconstructed from current code. |
| writer-4 | scripts/add_metal_ree_labels.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions inspected without execution. TOGO now distinguishes primary sections and named stocks but its water-anchor normalization is not experimental final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based solution migration is insufficient identity evidence. Metal classification uses heuristic compound amounts and a corpus threshold, with a separate writer. Historical local transformations are preserved, not causally reconstructed from current code. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Preserved optional mediadive756capi attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison.
- Preserved optional mediadive756capi_retry attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison.
- Preserved optional solution6127 attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison.
- Preserved optional solution6127_retry attempt returned HTTP 503. Exact DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated and are not imported. This access limit does not prevent the bounded receiving-medium comparison.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T201900Z-culturemech-008936-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: autotrophic_nitrobacter_medium (CultureMech:008936)'
started_at: '2026-10-21T20:11:22Z'
finished_at: '2026-10-21T20:19:00Z'
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
summary: DSMZ 756c explicitly defines the autotrophic branch, but both local layers
  flatten its two stocks, mislabel water and stock doses as gram rates, and point
  to unrelated solution records. The primary recipe resolves the receiving formulation
  and preparation; unavailable historical 6127 bytes remain a bounded limitation on
  the unrelated dependency.
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
  - path: data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
    sha256: 0e02a9eb52ad59cb34164e177d6b418b5aa62c03490e8c11526d91235e85970b
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
    sha256: f13c87932af0fc337a179c16ccfad5d4b59709482478fc026aa3b6aaa27fa27e
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6127_Stock_solution.yaml
    sha256: 3d050662a522836fb52a7e34bf4d09624e5768faece286eb687320244b11f447
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
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
  selection: Task review 369; batch 037 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-six task batches
    contain 360 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 363 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008936
targets:
- target_id: CultureMech:008936
  path: data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  label: autotrophic_nitrobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/369/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/369/strict.tsv"
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008936
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
  - CultureMech:008936
- check_id: mediadive756capi-source-access
  name: 'Exact source content access: mediadive756capi'
  required: false
  status: unavailable
  summary: Preserved optional mediadive756capi attempt returned HTTP 503. Exact DSMZ
    756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain
    unauthenticated and are not imported. This access limit does not prevent the bounded
    receiving-medium comparison.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - mediadive756capi-attempt
- check_id: mediadive756capi_retry-source-access
  name: 'Exact source content access: mediadive756capi_retry'
  required: false
  status: unavailable
  summary: Preserved optional mediadive756capi_retry attempt returned HTTP 503. Exact
    DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims
    remain unauthenticated and are not imported. This access limit does not prevent
    the bounded receiving-medium comparison.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - mediadive756capi_retry-attempt
- check_id: solution6127-source-access
  name: 'Exact source content access: solution6127'
  required: false
  status: unavailable
  summary: Preserved optional solution6127 attempt returned HTTP 503. Exact DSMZ 756c/756
    and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated
    and are not imported. This access limit does not prevent the bounded receiving-medium
    comparison.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - solution6127-attempt
- check_id: solution6127_retry-source-access
  name: 'Exact source content access: solution6127_retry'
  required: false
  status: unavailable
  summary: Preserved optional solution6127_retry attempt returned HTTP 503. Exact
    DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims
    remain unauthenticated and are not imported. This access limit does not prevent
    the bounded receiving-medium comparison.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - solution6127_retry-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:20.575122Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch037/369/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:21.807454Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-037/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch037/369/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:23.795305Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T20:12:25.147371Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T20:18:59Z'
  support: supports
  summary: './data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml:1:id: CultureMech:008936

    ./data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml:1:id:
    CultureMech:008936

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/source-preflight-bound/369/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T20:18:59Z'
  support: supports
  summary: 31 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 105d7c720ba20a7d53b15deb9dc232ccef54109cb70bc31560bbc9e98f2a99be
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/source-preflight-bound/369/evidence-context-original.json
  locator: Complete frozen source context and full local objects
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Frozen target/owner objects match freshly inspected records. Source interpretations
    are assessed against actual bound capture bytes; historical limitations remain
    separate.
  snapshot_sha256: 94e73e5b5f3d2020f85688182cf7d0e5129e49e865b2a6e102550a2318224e2b
- evidence_id: variant
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf
  locator: Page 1, complete 756c variant paragraph
  accessed_at: '2026-10-21T19:52:51.219574Z'
  support: supports
  summary: The primary adds 2 g/L sodium nitrite, omits yeast extract/peptone/pyruvate,
    and specifies initial pH 8.6, autoclaving and standing 2–3 days until pH 7.4–7.6.
    No temperature/time or reagent dose is supplied.
  snapshot_sha256: 95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda
- evidence_id: parent
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf
  locator: Page 1, main stock doses and Stock solution / Trace element solution subsections
  accessed_at: '2026-10-21T19:53:28.862593Z'
  support: supports
  summary: Only the delegated basal stock definitions and doses transfer to 756c.
    The parent organic additions are explicitly omitted and its pH instruction is
    overridden. Listed water is not explicit stock make-up or measured final volume.
  snapshot_sha256: 25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351
  locator: $.meta, $.components[0:3], $.comments[0]
  accessed_at: '2026-10-21T19:52:50.266514Z'
  support: supports
  summary: The provider preserves main 899 mL water, 2 g nitrite, 1 mL trace and 100
    mL stock, with both recipes separately. The primary independently states nitrite
    as 2 g/L.
  snapshot_sha256: 29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/369/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 6440ae719518cf813029eb3e7d20b1d3eec8642cf25894049d0295bb01012d41
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
- evidence_id: chebi32599
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.640268Z'
  support: supports
  summary: CHEBI:32599 resolves to magnesium sulfate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi3311
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3311
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:45.903210Z'
  support: supports
  summary: CHEBI:3311 resolves to calcium carbonate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 5413cec912ec253d62ba7a3f4ce7f0a9312ba8d1cb756713003f77a6e849d4b2
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
- evidence_id: chebi78870
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_78870
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T19:52:51.990231Z'
  support: supports
  summary: CHEBI:78870 resolves to sodium nitrite. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 9fd2f91f0da72f3e5e51c572efb1d48ddb832c449021c76f9d05d6b61df03ae6
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: CHEBI:86364 resolves to manganese(II) sulfate monohydrate. Identifier existence
    and label metadata do not establish source-specific hydrate, stereochemistry or
    product identity.
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi91249
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91249
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T15:28:32.029158Z'
  support: supports
  summary: CHEBI:91249 resolves to ammonium molybdate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 9a2c54385944d7bc3885d681295f3d476e3103d45179b57b846b0a1d5616edf2
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T20:18:59Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440":
    [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term":
    "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32599": [{"label": "Magnesium sulfate", "match_type": "preferred_term",
    "identifier": "CHEBI:32599", "preferred_term": "Magnesium sulfate", "ontology_id":
    "CHEBI:32599", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:3311":
    [{"label": "CaCO3", "match_type": "preferred_term", "identifier": "CHEBI:3311",
    "preferred_term": "CaCO3", "ontology_id": "CHEBI:3311", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id":
    "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:78870":
    [{"label": "NaNO2", "match_type": "preferred_term", "identifier": "CHEBI:78870",
    "preferred_term": "NaNO2", "ontology_id": "CHEBI:78870", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O",
    "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml; data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml",
    "events": 13, "timestamp_issues": []}]'
- evidence_id: dependency-6187
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: Entire referenced SolutionRecipe; composition, preparation, evidence and
    history
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Exact local linked stock read for identity comparison only. Its component
    evidence does not transfer to DSMZ 756c.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
- evidence_id: dependency-6127
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6127_Stock_solution.yaml
  locator: Entire referenced SolutionRecipe; composition, preparation, evidence and
    history
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Exact local linked stock read for identity comparison only. Its component
    evidence does not transfer to DSMZ 756c.
  snapshot_sha256: 3d050662a522836fb52a7e34bf4d09624e5768faece286eb687320244b11f447
- evidence_id: linked6187
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6187
  locator: $.data.id, volume, recipe and steps
  accessed_at: '2026-10-21T14:16:58.890288Z'
  support: supports
  summary: 6187 explicitly contains EDTA and chloride salts, differing from the delegated
    756 sulfate/borate/heptamolybdate trace recipe. Six current dependency snippets
    and their cited historical hash match these available raw bytes, supporting that
    stock only.
  snapshot_sha256: d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916
- evidence_id: dependency-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch037/369/dependency-evidence-inventory.json
  locator: Six authenticated 6187 claims and three derivative-only 6127 claims
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Six exact raw/cited-hash matches authenticate the EDTA/chloride stock only;
    the three nitrate/phosphate claims remain local derivatives. Neither is the source-delegated
    756 stock.
  snapshot_sha256: 350f9aef29a6254873434a01b9634b24f53b2501b21095675ef19ccb0225bac2
- evidence_id: mediadive756capi-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/756c
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:52:49.076119Z'
  support: context_only
  summary: Preserved optional mediadive756capi attempt returned HTTP 503. Exact DSMZ
    756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain
    unauthenticated and are not imported. This access limit does not prevent the bounded
    receiving-medium comparison.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive756capi_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/756c
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:53:28.239807Z'
  support: context_only
  summary: Preserved optional mediadive756capi_retry attempt returned HTTP 503. Exact
    DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims
    remain unauthenticated and are not imported. This access limit does not prevent
    the bounded receiving-medium comparison.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution6127-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6127
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:52:49.186226Z'
  support: context_only
  summary: Preserved optional solution6127 attempt returned HTTP 503. Exact DSMZ 756c/756
    and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated
    and are not imported. This access limit does not prevent the bounded receiving-medium
    comparison.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: solution6127_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6127
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:53:28.478172Z'
  support: context_only
  summary: Preserved optional solution6127_retry attempt returned HTTP 503. Exact
    DSMZ 756c/756 and TOGO resolve the receiving formulation; historical 6127 claims
    remain unauthenticated and are not imported. This access limit does not prevent
    the bounded receiving-medium comparison.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Current functions inspected without execution. TOGO now distinguishes primary
    sections and named stocks but its water-anchor normalization is not experimental
    final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based
    solution migration is insufficient identity evidence. Metal classification uses
    heuristic compound amounts and a corpus threshold, with a separate writer. Historical
    local transformations are preserved, not causally reconstructed from current code.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Current functions inspected without execution. TOGO now distinguishes primary
    sections and named stocks but its water-anchor normalization is not experimental
    final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based
    solution migration is insufficient identity evidence. Metal classification uses
    heuristic compound amounts and a corpus threshold, with a separate writer. Historical
    local transformations are preserved, not causally reconstructed from current code.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-2
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Current functions inspected without execution. TOGO now distinguishes primary
    sections and named stocks but its water-anchor normalization is not experimental
    final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based
    solution migration is insufficient identity evidence. Metal classification uses
    heuristic compound amounts and a corpus threshold, with a separate writer. Historical
    local transformations are preserved, not causally reconstructed from current code.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-3
  kind: record_content
  reference: scripts/analyze_metal_concentrations.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Current functions inspected without execution. TOGO now distinguishes primary
    sections and named stocks but its water-anchor normalization is not experimental
    final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based
    solution migration is insufficient identity evidence. Metal classification uses
    heuristic compound amounts and a corpus threshold, with a separate writer. Historical
    local transformations are preserved, not causally reconstructed from current code.
  snapshot_sha256: d9e414741123d14bf7350f57bd280eb2188bc9fc1a87917ce3d96a45c9d826cf
- evidence_id: writer-4
  kind: record_content
  reference: scripts/add_metal_ree_labels.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T20:18:59Z'
  support: context_only
  summary: Current functions inspected without execution. TOGO now distinguishes primary
    sections and named stocks but its water-anchor normalization is not experimental
    final-volume evidence; cleanup does not simply sum unequal duplicates. Name-based
    solution migration is insufficient identity evidence. Metal classification uses
    heuristic compound amounts and a corpus threshold, with a separate writer. Historical
    local transformations are preserved, not causally reconstructed from current code.
  snapshot_sha256: f4d45eaf1e633af60de15629b7b85371ea6d509052b6161fad63f7b607853b10
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008936
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
  - CultureMech:008936
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    Receiving recipe: Distilled water\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2899.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2899.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, main formulation\",\n        \"exact_source_quote\"\
    : \"Distilled water 899.00 ml\",\n        \"snapshot_sha256\": \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\"\
    ,\n        \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 899,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n        \"\
    accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"water_input_ml\": 899,\n      \"measured_final_volume_L\": null\n\
    \    },\n    \"rationale\": \"Restore the literal volume and receiving stage;\
    \ 899 + 100 + 1 = 1000 mL is a sum of listed liquids, not measured final volume.\
    \ Stock preparation water must not be added to receiving water. The present G_PER_L\
    \ encoding is not the source volume.\"\n  },\n  {\n    \"quantity_id\": \"q2\"\
    ,\n    \"component_or_context\": \"Receiving recipe: NaNO2\",\n    \"decision\"\
    : \"evidence_only\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n        \"decision\": \"\
    evidence_only\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756c\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf\",\n       \
    \ \"source_locator\": \"Page 1, variant nitrite rate\",\n        \"exact_source_quote\"\
    : \"2 g/l NaNO2\",\n        \"snapshot_sha256\": \"95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda\"\
    ,\n        \"parsed_text_sha256\": \"c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:51.219574Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaNO2\\\",\\n          \\\"volume\\\": 2,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"sodium_nitrite_g_per_L\":\
    \ 2,\n      \"measured_final_volume_L\": null\n    },\n    \"rationale\": \"The\
    \ primary explicitly supports the unchanged 2 g/L nitrite but no matching local\
    \ evidence is attached.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"Receiving recipe: Trace element solution\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, main formulation\",\n        \"exact_source_quote\"\
    : \"Trace element solution 1.00 ml\",\n        \"snapshot_sha256\": \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\"\
    ,\n        \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution\\\",\\n          \\\"volume\\\
    \": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n        \"\
    accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"trace_stock_addition_ml\": 1,\n      \"measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"Restore the literal volume and receiving\
    \ stage; 899 + 100 + 1 = 1000 mL is a sum of listed liquids, not measured final\
    \ volume. Stock preparation water must not be added to receiving water. The present\
    \ G_PER_L encoding is not the source volume.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q4\",\n    \"component_or_context\": \"Receiving recipe: Stock solution\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n   \
    \     \"field_path\": \"solutions[1].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, main formulation\",\n        \"exact_source_quote\"\
    : \"Stock solution 100.00 ml\",\n        \"snapshot_sha256\": \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\"\
    ,\n        \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Stock solution\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n        \"\
    accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"basal_stock_addition_ml\": 100,\n      \"measured_final_volume_L\"\
    : null\n    },\n    \"rationale\": \"Restore the literal volume and receiving\
    \ stage; 899 + 100 + 1 = 1000 mL is a sum of listed liquids, not measured final\
    \ volume. Stock preparation water must not be added to receiving water. The present\
    \ G_PER_L encoding is not the source volume.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q5\",\n    \"component_or_context\": \"Trace element stock: Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2899.0\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2899.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; water line\",\n\
    \        \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n    \
    \    \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"stock_batch_amount\": 1000,\n   \
    \   \"unit\": \"ml\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 1,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q6\",\n    \"component_or_context\": \"Trace element stock: H3BO3\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"49.4\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"49.4\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; H3BO3\",\n    \
    \    \"exact_source_quote\": \"H3BO3 49.40 mg\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 49.4,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 49.4,\n\
    \      \"unit\": \"mg\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 1,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q7\",\n    \"component_or_context\": \"Trace element stock: FeSO4 x 7 H2O\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"97.3\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"97.3\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; FeSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"FeSO4 x 7 H2O 97.30 mg\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 97.3,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\":\
    \ \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n    \
    \    \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"stock_batch_amount\": 97.3,\n   \
    \   \"unit\": \"mg\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 1,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q8\",\n    \"component_or_context\": \"Trace element stock: ZnSO4 x 7 H2O\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"43.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"43.1\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; ZnSO4 x 7 H2O\"\
    ,\n        \"exact_source_quote\": \"ZnSO4 x 7 H2O 43.10 mg\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 43.1,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\":\
    \ \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n    \
    \    \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"stock_batch_amount\": 43.1,\n   \
    \   \"unit\": \"mg\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 1,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q9\",\n    \"component_or_context\": \"Trace element stock: CuSO4 x 5 H2O\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[5].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n \
    \       \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; CuSO4 x 5 H2O\"\
    ,\n        \"exact_source_quote\": \"CuSO4 x 5 H2O 25.00 mg\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4 x 5 H2O\\\",\\n          \\\"volume\\\"\
    : 25,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n        \"\
    accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 25,\n      \"unit\": \"mg\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"stock_final_volume_ml\": null,\n      \"receiving_dose_ml\":\
    \ 1,\n      \"calculated_final_concentration\": null\n    },\n    \"rationale\"\
    : \"Restore this named stock batch and remove the receiving-scope duplicate. The\
    \ six trace masses are mg, not g; basal stock masses are not direct receiving\
    \ concentrations. The source lists water 1000 mL but no final-volume make-up,\
    \ so neither stock nor receiving concentrations are calculated from that volume\
    \ alone.\"\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Trace element stock: MnSO4 x H2O\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"33.8\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"33.8\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; MnSO4 x H2O\",\n\
    \        \"exact_source_quote\": \"MnSO4 x H2O 33.80 mg\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4 x H2O\\\",\\n          \\\"volume\\\": 33.8,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 33.8,\n\
    \      \"unit\": \"mg\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 1,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q11\",\n    \"component_or_context\": \"Trace element stock: (NH4)6Mo7O24\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n   \
    \     \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"37.1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"37.1\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Trace element solution subsection; (NH4)6Mo7O24\"\
    ,\n        \"exact_source_quote\": \"(NH4)6Mo7O24 37.10 mg\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"(NH4)6Mo7O24\\\",\\n          \\\"volume\\\":\
    \ 37.1,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\":\
    \ \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n    \
    \    \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"stock_batch_amount\": 37.1,\n   \
    \   \"unit\": \"mg\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 1,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q12\",\n    \"component_or_context\": \"Basal stock: Distilled water\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"2899.0\",\n          \"unit\": \"G_PER_L\"\n        },\n  \
    \      \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2899.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Stock solution subsection; water line\",\n       \
    \ \"exact_source_quote\": \"Distilled water 1000.00 ml\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1000,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n    \
    \    \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"\
    proposed_source_representation\": {\n      \"stock_batch_amount\": 1000,\n   \
    \   \"unit\": \"ml\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 100,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q13\",\n    \"component_or_context\": \"Basal stock: MgSO4 x 7 H2O\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n        \"\
    field_path\": \"ingredients[8].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n     \
    \   \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Stock solution subsection; MgSO4 x 7 H2O\",\n    \
    \    \"exact_source_quote\": \"MgSO4 x 7 H2O 0.50 g\",\n        \"snapshot_sha256\"\
    : \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\",\n    \
    \    \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4 x 7 H2O\\\",\\n          \\\"volume\\\"\
    : 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\",\n        \"\
    accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : {\n      \"stock_batch_amount\": 0.5,\n      \"unit\": \"g\",\n      \"stock_water_input_ml\"\
    : 1000,\n      \"stock_final_volume_ml\": null,\n      \"receiving_dose_ml\":\
    \ 100,\n      \"calculated_final_concentration\": null\n    },\n    \"rationale\"\
    : \"Restore this named stock batch and remove the receiving-scope duplicate. The\
    \ six trace masses are mg, not g; basal stock masses are not direct receiving\
    \ concentrations. The source lists water 1000 mL but no final-volume make-up,\
    \ so neither stock nor receiving concentrations are calculated from that volume\
    \ alone.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n    \"component_or_context\"\
    : \"Basal stock: NaCl\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Stock solution subsection; NaCl\",\n        \"exact_source_quote\"\
    : \"NaCl 5.00 g\",\n        \"snapshot_sha256\": \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\"\
    ,\n        \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 5,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 5,\n\
    \      \"unit\": \"g\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 100,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q15\",\n    \"component_or_context\": \"Basal stock: KH2PO4\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Stock solution subsection; KH2PO4\",\n        \"exact_source_quote\"\
    : \"KH2PO4 1.50 g\",\n        \"snapshot_sha256\": \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\"\
    ,\n        \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 1.5,\n\
    \      \"unit\": \"g\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 100,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q16\",\n    \"component_or_context\": \"Basal stock: CaCO3\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.07\",\n          \"unit\": \"G_PER_L\"\n       \
    \ },\n        \"decision\": \"correct\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756.pdf\",\n        \"\
    source_locator\": \"Page 1, Stock solution subsection; CaCO3\",\n        \"exact_source_quote\"\
    : \"CaCO3 0.07 g\",\n        \"snapshot_sha256\": \"25b51d5a442ba5acd085e47e6134dcecdb602b25b64b22386206367f8c12315a\"\
    ,\n        \"parsed_text_sha256\": \"c17e4df90beb72d9792b43090e283fc8db0937a70a7613c43636cf475b492cd1\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:53:28.862593Z\"\n      },\n      {\n\
    \        \"source_key\": \"togoM2351original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2351\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCO3\\\",\\n          \\\"volume\\\": 0.07,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"29badfb377a3ff3b16fbd2f5248cdbd705b799555fc8ab284159ca46695a7e8f\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:50.266514Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stock_batch_amount\": 0.07,\n\
    \      \"unit\": \"g\",\n      \"stock_water_input_ml\": 1000,\n      \"stock_final_volume_ml\"\
    : null,\n      \"receiving_dose_ml\": 100,\n      \"calculated_final_concentration\"\
    : null\n    },\n    \"rationale\": \"Restore this named stock batch and remove\
    \ the receiving-scope duplicate. The six trace masses are mg, not g; basal stock\
    \ masses are not direct receiving concentrations. The source lists water 1000\
    \ mL but no final-volume make-up, so neither stock nor receiving concentrations\
    \ are calculated from that volume alone.\"\n  },\n  {\n    \"quantity_id\": \"\
    q17\",\n    \"component_or_context\": \"Explicitly omitted parent organic ingredients\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12]\",\n        \"stored\": null,\n \
    \       \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12]\",\n        \"stored\": null,\n \
    \       \"decision\": \"evidence_only\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"dsmz756c\",\n        \"source_url\": \"\
    https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf\",\n       \
    \ \"source_locator\": \"Page 1, 756c variant exclusions\",\n        \"exact_source_quote\"\
    : \"omit yeast extract, peptone, and Na-pyruvate.\",\n        \"snapshot_sha256\"\
    : \"95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda\",\n    \
    \    \"parsed_text_sha256\": \"c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:51.219574Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"omitted_components\": [\n\
    \        \"yeast extract\",\n        \"peptone\",\n        \"Na-pyruvate\"\n \
    \     ],\n      \"parent_amounts_not_transferred\": true\n    },\n    \"rationale\"\
    : \"The current receiving layers already omit the three parent organic additions.\
    \ Preserve that branch; no zero concentration or parent organic dose is inserted.\"\
    \n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"component_or_context\": \"Initial\
    \ adjustment pH\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz756c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf\"\
    ,\n        \"source_locator\": \"Page 1, 756c preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"Adjust pH to 8.6 with NaOH or KOH.\",\n        \"\
    snapshot_sha256\": \"95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda\"\
    ,\n        \"parsed_text_sha256\": \"c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:51.219574Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stage\": \"before autoclaving\"\
    ,\n      \"pH\": 8.6\n    },\n    \"rationale\": \"Both layers omit this explicitly\
    \ documented staged condition. Keep the initial and later pH distinct; do not\
    \ substitute the parent pH 7.4 as the whole variant protocol.\"\n  },\n  {\n \
    \   \"quantity_id\": \"q19\",\n    \"component_or_context\": \"Standing duration\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\",\n        \"\
    field_path\": \"preparation_steps\",\n        \"stored\": null,\n        \"decision\"\
    : \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz756c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf\"\
    ,\n        \"source_locator\": \"Page 1, 756c preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"2 - 3\",\n        \"snapshot_sha256\": \"95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda\"\
    ,\n        \"parsed_text_sha256\": \"c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:51.219574Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stage\": \"after autoclaving\"\
    ,\n      \"duration_days\": [\n        2,\n        3\n      ]\n    },\n    \"\
    rationale\": \"Both layers omit this explicitly documented staged condition. Keep\
    \ the initial and later pH distinct; do not substitute the parent pH 7.4 as the\
    \ whole variant protocol.\"\n  },\n  {\n    \"quantity_id\": \"q20\",\n    \"\
    component_or_context\": \"Resulting pH interval\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz756c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf\"\
    ,\n        \"source_locator\": \"Page 1, 756c preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"pH 7.4 - 7.6.\",\n        \"snapshot_sha256\": \"\
    95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda\",\n        \"\
    parsed_text_sha256\": \"c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:51.219574Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"stage\": \"after standing\"\
    ,\n      \"pH_range\": [\n        7.4,\n        7.6\n      ]\n    },\n    \"rationale\"\
    : \"Both layers omit this explicitly documented staged condition. Keep the initial\
    \ and later pH distinct; do not substitute the parent pH 7.4 as the whole variant\
    \ protocol.\"\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"component_or_context\"\
    : \"Adjustment reagent and autoclave cycle limits\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"dsmz756c\",\n        \"source_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf\"\
    ,\n        \"source_locator\": \"Page 1, 756c preparation paragraph\",\n     \
    \   \"exact_source_quote\": \"NaOH or KOH. Autoclave\",\n        \"snapshot_sha256\"\
    : \"95371585e3415298bca435c96b3cc7fa9579d659ffd97cbfe490694194ea0eda\",\n    \
    \    \"parsed_text_sha256\": \"c9b55f8efdf3ffc2e2be4a28ff08fc5c10c17270753214940361b15ad2500686\"\
    ,\n        \"accessed_at\": \"2026-10-21T19:52:51.219574Z\"\n      }\n    ],\n\
    \    \"proposed_source_representation\": {\n      \"NaOH_or_KOH_dose\": null,\n\
    \      \"temperature_C\": null,\n      \"duration_min\": null\n    },\n    \"\
    rationale\": \"Recover the stated alternative adjustment reagent and autoclaving,\
    \ without invented reagent concentration, dose or cycle values.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '13 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 12/12
    primary and 11/12 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi26710
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi32599
  - chebi3311
  - chebi33118
  - chebi63036
  - chebi75836
  - chebi78870
  - chebi86364
  - chebi91249
  details: 'Instance coverage on a 0–100 percent scale, denominator 12: primary 100.00%;
    secondary 91.67%. These are linkage metrics, not correctness scores. Missing optional
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
  - CultureMech:008936
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact variant and two incorrectly linked stocks
  outcome: concern
  summary: CultureMech:008936 and its sole maintained owner identify TOGO M2351 /
    DSMZ 756c. The primary explicitly delegates the 756 stock definitions but omits
    its organics and changes preparation. MediaDive 6187 is an EDTA/chloride trace
    stock; local 6127 is a nitrate/phosphate stock. Their generic names do not establish
    equivalence to the source sulfate/borate trace and CaCO3/NaCl/MgSO4/KH2PO4 stock.
    All exact local paths and stable IDs resolve, but the scientific links are wrong.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - record
  - owner-0
  - id-search
  - variant
  - parent
  - provider
  - linked6187
  - dependency-6187
  - dependency-6127
- assessment_id: forms
  area: grounding
  topic: Heptamolybdate stoichiometry and magnesium hydration
  outcome: concern
  summary: The printed (NH4)6Mo7O24 is ammonium heptamolybdate, whereas CHEBI:91249
    encodes the 2:1 ammonium/orthomolybdate salt, formula 2H4N.MoO4. This is a stoichiometry
    mismatch despite a plausible canonical label. Magnesium’s primary CHEBI:31795
    matches the heptahydrate, but its current secondary CHEBI:32599 omits that hydrate;
    align exact-form linkage after source verification. Iron, zinc, copper and manganese
    sulfate hydrates otherwise match the printed stock forms. Do not borrow hydrate
    or ion identities from unrelated linked stocks or invent a replacement heptamolybdate
    ID.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - parent
  - provider
  - chebi91249
  - chebi31795
  - chebi32599
  - chebi75836
  - chebi32312
  - chebi31440
  - chebi86364
- assessment_id: preparation
  area: completeness
  topic: Variant preparation and quantities
  outcome: concern
  summary: Neither layer retains the primary initial pH 8.6 adjustment with NaOH or
    KOH, autoclaving, standing 2–3 days and later pH 7.4–7.6. No cycle temperature/time
    is printed. The parent pH 7.4 is overridden, and its yeast extract, peptone and
    pyruvate amounts do not transfer. No measured final stock or receiving volume
    is asserted from listed water or summed liquids.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - variant
  - parent
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Defined inorganic branch and high-metal signal
  outcome: concern
  summary: 'The exact branch consists of specified inorganic salts after removing
    parent complex organics; COMPLEX/UNDEFINED is inconsistent with this defined formulation.
    LIQUID is compatible with no gelling agent. high_metal requires reassessment after
    fixing units/stages and links: six stock milligram amounts are currently represented
    as direct g/L, and other stock amounts are also flattened. A source-scoped, unit-aware
    recalculation must precede any Boolean decision; this review does not assert that
    the corrected medium must have a false flag. Neither the title nor annotations
    establish an organism phenotype or growth outcome.'
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - variant
  - parent
  - provider
  - record
  - owner-0
  - writer-3
  - writer-4
- assessment_id: provenance
  area: provenance
  topic: Historical evidence and source scope
  outcome: concern
  summary: The receiving target and owner have no amount evidence; nine attached objects
    occur only in the two linked stock records. Six 6187 snippets match the available
    raw hash, while three 6127 objects remain derivative-only after bounded attempts/search.
    Source links must be corrected without transferring those objects to the delegated
    stocks. Preserve all import/migration/cleanup and stock-curation events append-only;
    the referenced stocks are contextual identities, not additional reviewed targets.
  target_ids:
  - CultureMech:008936
  evidence_ids:
  - record
  - owner-0
  - dependency-evidence
  - history-metadata
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: culturemech.008936.stock-stage-unit-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock water and solutes are flattened into the receiving recipe
  description: Both layers merge 899 + 1000 + 1000 mL water into 2899 G_PER_L, promote
    six trace-stock mg inputs to direct g/L, retain four basal-stock masses as direct
    receiving rates and encode 1/100 mL stock doses as G_PER_L. This destroys source
    units and stages. The 2 g/L sodium nitrite is explicitly primary-supported but
    lacks attached evidence.
  target_ids:
  - CultureMech:008936
  field_paths:
  - ingredients
  - solutions[0].concentration
  - solutions[1].concentration
  evidence_ids:
  - record
  - owner-0
  - variant
  - parent
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  issue_key: culturemech.008936.wrong-stock-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Two generic stock names point to different formulations
  description: The trace link 6187 resolves to EDTA/chloride salts, while the delegated
    stock uses sulfate/borate/heptamolybdate. Local 6127 contains nitrate and hydrogen
    phosphates instead of the CaCO3/NaCl/MgSO4/KH2PO4 stock. All paths can exist while
    the intended formulations differ.
  target_ids:
  - CultureMech:008936
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[0].name
  - solutions[1].name
  - solutions[0].notes
  - solutions[1].notes
  evidence_ids:
  - variant
  - parent
  - linked6187
  - dependency-6187
  - dependency-6127
  - dependency-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  issue_key: culturemech.008936.stock-molecular-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Heptamolybdate and magnesium linkage need exact-form grounding
  description: The source ammonium heptamolybdate formula differs from CHEBI:91249
    orthomolybdate. The primary magnesium hydrate is already correct while its secondary
    key remains anhydrous/generic.
  target_ids:
  - CultureMech:008936
  field_paths:
  - ingredients[7].term
  - ingredients[8].mediaingredientmech_chebi_term
  evidence_ids:
  - parent
  - provider
  - chebi91249
  - chebi31795
  - chebi32599
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  issue_key: culturemech.008936.variant-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The variant’s staged pH and sterilization instructions are absent
  description: The available primary specifies adjustment to pH 8.6, autoclaving,
    and standing 2–3 days until pH 7.4–7.6; neither layer retains this sequence.
  target_ids:
  - CultureMech:008936
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - variant
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3
  normalization_reason: P3.5 omission of sterilization/preparation is elevated to
    major because the exact variant’s initial and post-standing pH stages and autoclaving
    are entirely absent; it materially changes the operational identity, not merely
    prose style.
- finding_id: f5
  issue_key: culturemech.008936.classification-after-stock-repair
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The defined inorganic variant is classified as complex
  description: The source explicitly removes the parent organic mixtures and leaves
    specified inorganic components, contrary to COMPLEX/UNDEFINED. The high-metal
    flag is also confounded by flattened mg/g and stock scope.
  target_ids:
  - CultureMech:008936
  field_paths:
  - medium_type
  - composition_type
  - high_metal
  evidence_ids:
  - variant
  - parent
  - provider
  - writer-3
  - writer-4
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  description: Restore separate stock batches and volume additions, the 899 mL receiving
    water and exact mg/g inputs. Remove duplicated direct stock components. Attach
    literal scoped evidence; do not infer stock make-up or measured final volume from
    water inputs.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008936
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  description: Detach unsupported stock identifiers and recover the exact source-scoped
    definitions through verified inline stocks or exact maintained identities. Preserve
    unrelated stock records and their evidence; do not reuse them solely because names
    match.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008936
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  description: Preserve the printed heptamolybdate formula and resolve an exact supported
    term without guessing. Align the magnesium secondary key with the source hydrate
    and current primary term; keep amount correction separate.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008936
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  description: Add the exact staged preparation with narrow source evidence, retaining
    unknown autoclave temperature/time and adjustment reagent doses. Do not collapse
    initial and later pH into an unsupported single value.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008936
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
  description: Represent the exact defined branch and recompute any metal classification
    only after source units and stages are restored using an explicit justified method.
    Do not blindly retain or clear high_metal.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008936
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml
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
- Preserved optional mediadive756capi attempt returned HTTP 503. Exact DSMZ 756c/756
  and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated
  and are not imported. This access limit does not prevent the bounded receiving-medium
  comparison.
- Preserved optional mediadive756capi_retry attempt returned HTTP 503. Exact DSMZ
  756c/756 and TOGO resolve the receiving formulation; historical 6127 claims remain
  unauthenticated and are not imported. This access limit does not prevent the bounded
  receiving-medium comparison.
- Preserved optional solution6127 attempt returned HTTP 503. Exact DSMZ 756c/756 and
  TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated
  and are not imported. This access limit does not prevent the bounded receiving-medium
  comparison.
- Preserved optional solution6127_retry attempt returned HTTP 503. Exact DSMZ 756c/756
  and TOGO resolve the receiving formulation; historical 6127 claims remain unauthenticated
  and are not imported. This access limit does not prevent the bounded receiving-medium
  comparison.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-037
- generated-medium
```
