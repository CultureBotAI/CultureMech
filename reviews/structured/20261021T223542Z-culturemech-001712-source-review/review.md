# Source and formulation review: bcye_alpha_agar (CultureMech:001712)

- Review: 20261021T223542Z-culturemech-001712-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T22:32:19Z
- Finished UTC: 2026-10-21T22:35:42Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact 585a official-page projection distinguishes a commercial alternative and four separately prepared solutions. Both local layers flatten their amounts into one ingredient list, including a volume-to-mass error for the commercial base, and omit the four water inputs and explicit solution doses. Fourteen preparation steps are retained, but their stock ownership is not structured. Source formula/prose conflict, a missing current MIM key and unresolved legacy correspondence require bounded follow-up.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 396; batch 040 item 6 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-nine task batches contain 390 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 393 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a639c4b597e95b6061f2d1c7baa04de84ba2f00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001712 | data/merge_yaml/merged/BCYE_alpha_agar.yaml | generated | bcye_alpha_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001712 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001712 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/396/strict.tsv |
| validate-terms | passed | True | CultureMech:001712 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001712 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001712 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: dsmz585a | unavailable | False | CultureMech:001712 | Exact dsmz585a attempt retained HTTP 404. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| Exact source content access: mediadive585aapi | unavailable | False | CultureMech:001712 | Exact mediadive585aapi attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| Exact source content access: mediadive585aapi_retry | unavailable | False | CultureMech:001712 | Exact mediadive585aapi_retry attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| Exact source content access: dsmz585aOfficialPDF | unavailable | False | CultureMech:001712 | Exact dsmz585aOfficialPDF attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| Exact source content access: dsmz585aOfficialPage | unavailable | True | CultureMech:001712 | Exact dsmz585aOfficialPage attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| Historical legacy MediaIngredientMech:000555 identity | unavailable | True | CultureMech:001712 | Current pinned index/catalog/tree were searched exactly and have no legacy object. No original historical object was recovered; primary ACES support does not authenticate that secondary identity. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001712.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:001712.

41 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "name": "Commercial OXOID base",
    "stage": "Commercial alternative",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 1000,
      "source_unit": "ml",
      "stock_water_input_ml": null,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 111; not raw HTTP",
        "exact_source_quote": "L111: (with Legionella BCYE supplement)  &#124; 1000  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The source says 1000 ml of prepared commercial alternative, not 1000 g/L; do not combine this alternative with the full separate formulation."
  },
  {
    "decision_id": "q2",
    "name": "Commercial OXOID base",
    "stage": "Commercial alternative",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 1000,
      "source_unit": "ml",
      "stock_water_input_ml": null,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 111; not raw HTTP",
        "exact_source_quote": "L111: (with Legionella BCYE supplement)  &#124; 1000  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The source says 1000 ml of prepared commercial alternative, not 1000 g/L; do not combine this alternative with the full separate formulation."
  },
  {
    "decision_id": "q3",
    "name": "ACES",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20.4082",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 10,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 122; not raw HTTP",
        "exact_source_quote": "L122: (N-2-acetamido-2-aminoethane-sulfonic acid)  &#124; 10  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q4",
    "name": "ACES",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20.4082",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 10,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 122; not raw HTTP",
        "exact_source_quote": "L122: (N-2-acetamido-2-aminoethane-sulfonic acid)  &#124; 10  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q5",
    "name": "Yeast extract",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "20.4082",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 10,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 124; not raw HTTP",
        "exact_source_quote": "L124: (Difco 0127)  &#124; 10  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q6",
    "name": "Yeast extract",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "20.4082",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 10,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 124; not raw HTTP",
        "exact_source_quote": "L124: (Difco 0127)  &#124; 10  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q7",
    "name": "Activated charcoal",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.08163",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 2,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 126; not raw HTTP",
        "exact_source_quote": "L126: (Sigma C 5510)  &#124; 2  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q8",
    "name": "Activated charcoal",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.08163",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 2,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 126; not raw HTTP",
        "exact_source_quote": "L126: (Sigma C 5510)  &#124; 2  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q9",
    "name": "Disodium alpha-ketoglutarate",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.04082",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 1,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 127; not raw HTTP",
        "exact_source_quote": "L127: [Input]  &#124; Na_{2} alpha-ketoglutarate  &#124; 1  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q10",
    "name": "Disodium alpha-ketoglutarate",
    "stage": "Solution A",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "2.04082",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 1,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 127; not raw HTTP",
        "exact_source_quote": "L127: [Input]  &#124; Na_{2} alpha-ketoglutarate  &#124; 1  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q11",
    "name": "Agar",
    "stage": "Solution B",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "30.6122",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 15,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 136; not raw HTTP",
        "exact_source_quote": "L136: [Input]  &#124; Agar  &#124; 15  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 137; not raw HTTP",
        "exact_source_quote": "L137: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q12",
    "name": "Agar",
    "stage": "Solution B",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "30.6122",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 15,
      "source_unit": "g",
      "stock_water_input_ml": 490,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 136; not raw HTTP",
        "exact_source_quote": "L136: [Input]  &#124; Agar  &#124; 15  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 137; not raw HTTP",
        "exact_source_quote": "L137: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q13",
    "name": "L-cysteine hydrochloride monohydrate",
    "stage": "Solution C",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 0.4,
      "source_unit": "g",
      "stock_water_input_ml": 10,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 146; not raw HTTP",
        "exact_source_quote": "L146: [Input]  &#124; L-Cysteine HCl x H_{2}O  &#124; 0.4  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 147; not raw HTTP",
        "exact_source_quote": "L147: [Input]  &#124; Distilled water  &#124; 10.0  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q14",
    "name": "L-cysteine hydrochloride monohydrate",
    "stage": "Solution C",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "40",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 0.4,
      "source_unit": "g",
      "stock_water_input_ml": 10,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 146; not raw HTTP",
        "exact_source_quote": "L146: [Input]  &#124; L-Cysteine HCl x H_{2}O  &#124; 0.4  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 147; not raw HTTP",
        "exact_source_quote": "L147: [Input]  &#124; Distilled water  &#124; 10.0  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate."
  },
  {
    "decision_id": "q15",
    "name": "Literal Fe4(PO4)2",
    "stage": "Solution D",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 0.25,
      "source_unit": "g",
      "stock_water_input_ml": 10,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 155; not raw HTTP",
        "exact_source_quote": "L155: [Input]  &#124; Fe_{4}(PO_{4})_{2}  &#124; 0.25  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 156; not raw HTTP",
        "exact_source_quote": "L156: [Input]  &#124; Distilled water  &#124; 10.00  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 158; not raw HTTP",
        "exact_source_quote": "L158: 2 Please note: Soluble ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical looses its green colour and becomes brown or yellow.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate. The printed formula conflicts with the source prose ferric pyrophosphate; preserve both pending reconciliation."
  },
  {
    "decision_id": "q16",
    "name": "Literal Fe4(PO4)2",
    "stage": "Solution D",
    "decision": "conflict",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        }
      }
    ],
    "desired": {
      "source_batch_amount": 0.25,
      "source_unit": "g",
      "stock_water_input_ml": 10,
      "final_medium_concentration": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 155; not raw HTTP",
        "exact_source_quote": "L155: [Input]  &#124; Fe_{4}(PO_{4})_{2}  &#124; 0.25  &#124; g",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 156; not raw HTTP",
        "exact_source_quote": "L156: [Input]  &#124; Distilled water  &#124; 10.00  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 158; not raw HTTP",
        "exact_source_quote": "L158: 2 Please note: Soluble ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical looses its green colour and becomes brown or yellow.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The stored rate is flattened outside its named stock. Restore the printed batch amount and stage; no density or measured final volume is available. The numerical rate can describe the stock water basis, not an independently established final-medium rate. The printed formula conflicts with the source prose ferric pyrophosphate; preserve both pending reconciliation."
  },
  {
    "decision_id": "q17",
    "name": "Distilled water",
    "stage": "Solution A preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 490,
      "source_unit": "ml",
      "stage": "A"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 128; not raw HTTP",
        "exact_source_quote": "L128: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "No local solvent entry exists. Keep each water input attached to its own preparation; their sum is not a measured final volume."
  },
  {
    "decision_id": "q18",
    "name": "Distilled water",
    "stage": "Solution B preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 490,
      "source_unit": "ml",
      "stage": "B"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 137; not raw HTTP",
        "exact_source_quote": "L137: [Input]  &#124; Distilled water  &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "No local solvent entry exists. Keep each water input attached to its own preparation; their sum is not a measured final volume."
  },
  {
    "decision_id": "q19",
    "name": "Distilled water",
    "stage": "Solution C preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "ml",
      "stage": "C"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 147; not raw HTTP",
        "exact_source_quote": "L147: [Input]  &#124; Distilled water  &#124; 10.0  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "No local solvent entry exists. Keep each water input attached to its own preparation; their sum is not a measured final volume."
  },
  {
    "decision_id": "q20",
    "name": "Distilled water",
    "stage": "Solution D preparation",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ingredients",
        "stored": [
          {
            "preferred_term": "OXOID Legionella CYE-Agar base",
            "concentration": {
              "value": "1000",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "ACES",
            "term": {
              "id": "CHEBI:39061",
              "label": "ACES"
            },
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_term": {
              "id": "MediaIngredientMech:000555",
              "label": "ACES"
            }
          },
          {
            "preferred_term": "Yeast extract",
            "concentration": {
              "value": "20.4082",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Activated charcoal",
            "concentration": {
              "value": "4.08163",
              "unit": "G_PER_L"
            }
          },
          {
            "preferred_term": "Na2 alpha-ketoglutarate",
            "term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            },
            "concentration": {
              "value": "2.04082",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:16810",
              "label": "2-oxoglutarate(2-)"
            }
          },
          {
            "preferred_term": "Agar",
            "term": {
              "id": "CHEBI:2509",
              "label": "agar"
            },
            "concentration": {
              "value": "30.6122",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:2509",
              "label": "agar"
            }
          },
          {
            "preferred_term": "L-Cysteine HCl x H2O",
            "term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            },
            "concentration": {
              "value": "40",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:91248",
              "label": "L-cysteine hydrochloride hydrate"
            }
          },
          {
            "preferred_term": "Fe4(PO4)2",
            "term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            },
            "concentration": {
              "value": "25",
              "unit": "G_PER_L"
            },
            "mediaingredientmech_chebi_term": {
              "id": "CHEBI:132767",
              "label": "ferric pyrophosphate"
            }
          }
        ]
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "ml",
      "stage": "D"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 156; not raw HTTP",
        "exact_source_quote": "L156: [Input]  &#124; Distilled water  &#124; 10.00  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "No local solvent entry exists. Keep each water input attached to its own preparation; their sum is not a measured final volume."
  },
  {
    "decision_id": "q21",
    "name": "Solution A dose",
    "stage": "Main assembly",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 490,
      "source_unit": "ml",
      "stage": "A"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 94; not raw HTTP",
        "exact_source_quote": "L94: [Input]  &#124; cite26†Solution A &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 103; not raw HTTP",
        "exact_source_quote": "L103: 6 Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The source explicitly lists the receiving doses; retain their sequence and commercial alternative. These are stock-addition volumes, not masses or stock solute concentrations."
  },
  {
    "decision_id": "q22",
    "name": "Solution B dose",
    "stage": "Main assembly",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 490,
      "source_unit": "ml",
      "stage": "B"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 95; not raw HTTP",
        "exact_source_quote": "L95: [Input]  &#124; cite27†Solution B &#124; 490  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 103; not raw HTTP",
        "exact_source_quote": "L103: 6 Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The source explicitly lists the receiving doses; retain their sequence and commercial alternative. These are stock-addition volumes, not masses or stock solute concentrations."
  },
  {
    "decision_id": "q23",
    "name": "Solution C dose",
    "stage": "Main assembly",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "ml",
      "stage": "C"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 96; not raw HTTP",
        "exact_source_quote": "L96: [Input]  &#124; cite28†Solution C &#124; 10  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 103; not raw HTTP",
        "exact_source_quote": "L103: 6 Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The source explicitly lists the receiving doses; retain their sequence and commercial alternative. These are stock-addition volumes, not masses or stock solute concentrations."
  },
  {
    "decision_id": "q24",
    "name": "Solution D dose",
    "stage": "Main assembly",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "desired": {
      "source_amount": 10,
      "source_unit": "ml",
      "stage": "D"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 97; not raw HTTP",
        "exact_source_quote": "L97: [Input]  &#124; cite29†Solution D &#124; 10  &#124; ml",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 103; not raw HTTP",
        "exact_source_quote": "L103: 6 Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The source explicitly lists the receiving doses; retain their sequence and commercial alternative. These are stock-addition volumes, not masses or stock solute concentrations."
  },
  {
    "decision_id": "q25",
    "name": "Preparation step 1",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Prepare OXOID Legionella CYE-Agar base or solution A."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Prepare OXOID Legionella CYE-Agar base or solution A."
      }
    ],
    "desired": {
      "source_instruction": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 98; not raw HTTP",
        "exact_source_quote": "L98: 1 Prepare OXOID Legionella CYE-Agar base or solution A.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q26",
    "name": "Preparation step 2",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Cool down to 50 °C."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Cool down to 50 °C."
      }
    ],
    "desired": {
      "source_instruction": "L99: 2 Cool down to 50 °C.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 99; not raw HTTP",
        "exact_source_quote": "L99: 2 Cool down to 50 °C.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q27",
    "name": "Preparation step 3",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Add solution C (Cysteine-HCl) and solution D (ferric pyrophosphate)."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "Add solution C (Cysteine-HCl) and solution D (ferric pyrophosphate)."
      }
    ],
    "desired": {
      "source_instruction": "L100: 3 Add solution C (Cysteine-HCl) and solution D (ferric pyrophosphate).",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 100; not raw HTTP",
        "exact_source_quote": "L100: 3 Add solution C (Cysteine-HCl) and solution D (ferric pyrophosphate).",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q28",
    "name": "Preparation step 4",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Adjust pH to 6.9 with sterile 1.0 N KOH or HCl."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Adjust pH to 6.9 with sterile 1.0 N KOH or HCl."
      }
    ],
    "desired": {
      "source_instruction": "L101: 4 Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 101; not raw HTTP",
        "exact_source_quote": "L101: 4 Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q29",
    "name": "Preparation step 5",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "The pH of the medium is critical."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[4].description",
        "stored": "The pH of the medium is critical."
      }
    ],
    "desired": {
      "source_instruction": "L102: 5 The pH of the medium is critical.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 102; not raw HTTP",
        "exact_source_quote": "L102: 5 The pH of the medium is critical.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q30",
    "name": "Preparation step 6",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[5].description",
        "stored": "Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[5].description",
        "stored": "Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended."
      }
    ],
    "desired": {
      "source_instruction": "L103: 6 Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 103; not raw HTTP",
        "exact_source_quote": "L103: 6 Finally, add solution B. Swirl medium in flask during dispensing to petri dishes or tubes in order to keep charcoal suspended.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q31",
    "name": "Preparation step 7",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[6].description",
        "stored": "Dehydrated media preparations are available from media distributors."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[6].description",
        "stored": "Dehydrated media preparations are available from media distributors."
      }
    ],
    "desired": {
      "source_instruction": "L112: 1 Dehydrated media preparations are available from media distributors.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 112; not raw HTTP",
        "exact_source_quote": "L112: 1 Dehydrated media preparations are available from media distributors.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q32",
    "name": "Preparation step 8",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[7].description",
        "stored": "We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[7].description",
        "stored": "We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement."
      }
    ],
    "desired": {
      "source_instruction": "L113: 2 We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 113; not raw HTTP",
        "exact_source_quote": "L113: 2 We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q33",
    "name": "Preparation step 9",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[8].description",
        "stored": "Note: Alternatively use CYE-ACES AGAR"
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[8].description",
        "stored": "Note: Alternatively use CYE-ACES AGAR"
      }
    ],
    "desired": {
      "source_instruction": "L114: 3 Note: Alternatively use CYE-ACES AGAR",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 114; not raw HTTP",
        "exact_source_quote": "L114: 3 Note: Alternatively use CYE-ACES AGAR",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q34",
    "name": "Preparation step 10",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[9].description",
        "stored": "Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[9].description",
        "stored": "Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C."
      }
    ],
    "desired": {
      "source_instruction": "L129: 1 Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 129; not raw HTTP",
        "exact_source_quote": "L129: 1 Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q35",
    "name": "Preparation step 11",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[10].description",
        "stored": "Autoclave at 121°C and cool to 50 - 55°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[10].description",
        "stored": "Autoclave at 121°C and cool to 50 - 55°C."
      }
    ],
    "desired": {
      "source_instruction": "L138: 1 Autoclave at 121°C and cool to 50 - 55°C.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 138; not raw HTTP",
        "exact_source_quote": "L138: 1 Autoclave at 121°C and cool to 50 - 55°C.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q36",
    "name": "Preparation step 12",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[11].description",
        "stored": "Prepare a fresh solution and filter-sterilize it."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[11].description",
        "stored": "Prepare a fresh solution and filter-sterilize it."
      }
    ],
    "desired": {
      "source_instruction": "L148: 1 Prepare a fresh solution and filter-sterilize it.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 148; not raw HTTP",
        "exact_source_quote": "L148: 1 Prepare a fresh solution and filter-sterilize it.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q37",
    "name": "Preparation step 13",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[12].description",
        "stored": "Prepare a fresh solution by heating to 50 - 55°C in a water-bath. Filter-sterilize solution separately."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[12].description",
        "stored": "Prepare a fresh solution by heating to 50 - 55°C in a water-bath. Filter-sterilize solution separately."
      }
    ],
    "desired": {
      "source_instruction": "L157: 1 Prepare a fresh solution by heating to 50 - 55°C in a water-bath. Filter-sterilize solution separately.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 157; not raw HTTP",
        "exact_source_quote": "L157: 1 Prepare a fresh solution by heating to 50 - 55°C in a water-bath. Filter-sterilize solution separately.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q38",
    "name": "Preparation step 14",
    "stage": "Main/commercial/A/B/C/D stages as stated",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[13].description",
        "stored": "Please note: Soluble ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical looses its green colour and becomes brown or yellow."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[13].description",
        "stored": "Please note: Soluble ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical looses its green colour and becomes brown or yellow."
      }
    ],
    "desired": {
      "source_instruction": "L158: 2 Please note: Soluble ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical looses its green colour and becomes brown or yellow.",
      "scope": "Preserve exact stage, including all stated numbers"
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 158; not raw HTTP",
        "exact_source_quote": "L158: 2 Please note: Soluble ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical looses its green colour and becomes brown or yellow.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Both layers already retain this instruction. Attach stage-specific support and retain all numerical qualifiers; do not generalize the A sterilization time to B or the filter steps to A/B."
  },
  {
    "decision_id": "q39",
    "name": "Main pH",
    "stage": "Final medium",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "ph_value",
        "stored": 6.9
      }
    ],
    "desired": {
      "value": 6.9
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 78; not raw HTTP",
        "exact_source_quote": "L78: Final pH: 6.9",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 101; not raw HTTP",
        "exact_source_quote": "L101: 4 Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The main pH agrees. The same numerical A-adjustment pH is a separate preparation stage, not independent evidence of the measured final volume."
  },
  {
    "decision_id": "q40",
    "name": "Titrant strength and unspecified dose",
    "stage": "Main and A pH adjustment",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Adjust pH to 6.9 with sterile 1.0 N KOH or HCl."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[3].description",
        "stored": "Adjust pH to 6.9 with sterile 1.0 N KOH or HCl."
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "preparation_steps[9].description",
        "stored": "Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C."
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "preparation_steps[9].description",
        "stored": "Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C."
      }
    ],
    "desired": {
      "main_titrants": "sterile 1.0 N KOH or HCl",
      "A_titrant": "1 N KOH",
      "dose": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 101; not raw HTTP",
        "exact_source_quote": "L101: 4 Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 129; not raw HTTP",
        "exact_source_quote": "L129: 1 Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "Retain normality as stated. No fixed volume, molarity conversion or mass follows without further information."
  },
  {
    "decision_id": "q41",
    "name": "Unknown incubation and final-volume measurement",
    "stage": "Whole medium",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "temperature_value",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "temperature_range",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/BCYE_alpha_agar.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "desired": {
      "incubation_temperature": null,
      "measured_final_volume": null,
      "B_cycle_minutes": null
    },
    "source_snippets": [
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 54; not raw HTTP",
        "exact_source_quote": "L54: [Input: 1000]",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 78; not raw HTTP",
        "exact_source_quote": "L78: Final pH: 6.9",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      },
      {
        "source_key": "bacmedia585aWebProjection",
        "source_url": "https://bacmedia.dsmz.de/medium/585a?mobile=1",
        "source_locator": "Preserved official web-tool projection line 138; not raw HTTP",
        "exact_source_quote": "L138: 1 Autoclave at 121°C and cool to 50 - 55°C.",
        "snapshot_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919",
        "parsed_text_sha256": "99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919"
      }
    ],
    "interpretation": "The displayed 1000 ml main volume and additive dosing are source presentation, not a measured volume. Heating/cooling temperatures are preparation only. B has no stated duration."
  }
]

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:001712.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact 585a identity and commercial alternative

identity: supported. Targets: CultureMech:001712.

The one maintained contributor, accession 585a and official projected page identify this medium. The commercial base is an alternative preparation; a fingerprint or shared name does not authorize summing it with all four independently prepared solutions.

### Chemical forms, salts and source-internal conflict

grounding: concern. Targets: CultureMech:001712.

ACES and agar names match their asserted primary terms. CHEBI:91248 includes the monohydrate formula and exact L-cysteine hydrochloride monohydrate synonyms, supporting the source form. CHEBI:16810 is the bare dianion (charge −2, no sodium), not the complete supplied disodium salt. CHEBI:132767 describes four Fe(III) ions with three diphosphates; it agrees with the prose ferric pyrophosphate but not literal Fe4(PO4)2. Do not silently repair this source conflict or infer a replacement identity. Yeast extract, charcoal and commercial base are not grounded as pure chemicals.

### Instance linkage and exact current membership

grounding: concern. Targets: CultureMech:001712.

On the target denominator of eight ingredient instances, five primary links give 62.5% linkage and four CHEBI-keyed secondary links give 50%; one separate legacy slot gives 12.5%. These are linkage metrics, not correctness. Current CHEBI:16810 secondary membership is absent; legacy 000555 historical correspondence remains unavailable despite successful current negative searches.

### Retained instructions and missing stock structure

completeness: concern. Targets: CultureMech:001712.

Both layers retain fourteen steps, pH 6.9, cooling and filtration. Their missing explicit A/B/C/D composition and dose boundaries obscure those instructions. A alone specifies 121 °C for 15 minutes; B specifies 121 °C without duration, C/D are separately filtered and D is warmed. Unknown acid/base doses remain unquantified.

### Classification and growth scope

scope: supported. Targets: CultureMech:001712.

Agar and complex commercial/yeast material support a complex undefined solid medium. Preparation temperatures do not establish growth temperature or oxygen conditions. No species-specific growth or taxonomic assertions are inferred from the commercial Legionella name.

## Findings

### f1: Alternative and stock amounts are flattened

major / open / confirmed; issue key: culturemech.001712.flat-alternative-and-stock-amounts.

Both layers store commercial 1000 ml as 1000 G_PER_L and stock-normalized solute rates as direct ingredients. The commercial alternative and four stock formulations cannot be treated as one cumulative formula.

### f2: Four solvent inputs and explicit stock doses are absent

major / open / confirmed; issue key: culturemech.001712.missing-solvent-and-stage-ownership.

Both layers retain preparation prose but omit the A/B/C/D water entries and structured stock-dose ownership, leaving critical quantities outside the represented formulation.

### f3: Counterion and iron formula require reconciliation

major / open / confirmed; issue key: culturemech.001712.supplied-form-conflicts.

The disodium source is grounded to a bare dianion, and the iron formula differs from both source prose and the asserted ferric pyrophosphate structure.

### f4: Secondary correspondence is unresolved

major / open / confirmed; issue key: culturemech.001712.secondary-current-and-historical-gaps.

CHEBI:16810 has no mapped preferred row in the exact current MIM index. Legacy 000555 is absent from current snapshots, while its original historical identity is unavailable. Primary OLS existence does not authenticate either secondary assertion.

## Recommended Actions And Acceptance Checks

### a1

Represent the exact commercial alternative and A/B/C/D batch compositions and receiving doses separately, with source evidence; do not calculate final concentrations from an assumed measured volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore the four solvent inputs and exact source-stage associations while preserving existing preparation and unknown quantities; regenerate only after owner review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the exact supplied disodium and iron forms from authoritative source clarification; preserve source conflict and mass amounts without inventing replacements.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve or qualify the current secondary membership independently from the historical legacy lookup; retain the unresolved history instead of fabricating a mapping.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/BCYE_alpha_agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/bcye_alpha_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/BCYE_alpha_agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/BCYE_alpha_agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch040/396/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch040/396/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/BCYE_alpha_agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/BCYE_alpha_agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/bcye_alpha_agar.yaml:1:id: CultureMech:001712<br>./data/merge_yaml/merged/BCYE_alpha_agar.yaml:1:id: CultureMech:001712<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch040/source-preflight-bound/396/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 13 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary-projection | https://bacmedia.dsmz.de/medium/585a?mobile=1; Official 585a page projected lines 70–158; preserved tool output, HTTP status null | supports | This is a full preserved official-page text projection, not recovered HTTP HTML or API raw. The recorded time is projection preservation time. Source recipe statements are usable with this limitation; direct HTTP retrieval remains unavailable. |
| dsmz585a-attempt | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium585a.pdf; Preserved exact public retrieval result | context_only | Exact dsmz585a attempt retained HTTP 404. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| mediadive585aapi-attempt | https://mediadive.dsmz.de/rest/medium/585a; Preserved exact public retrieval result | context_only | Exact mediadive585aapi attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| mediadive585aapi_retry-attempt | https://mediadive.dsmz.de/rest/medium/585a; Preserved exact public retrieval result | context_only | Exact mediadive585aapi_retry attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| dsmz585aOfficialPDF-attempt | https://bacmedia.dsmz.de/pdf/585a; Preserved exact public retrieval result | context_only | Exact dsmz585aOfficialPDF attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| dsmz585aOfficialPage-attempt | https://bacmedia.dsmz.de/medium/585a?mobile=1; Preserved exact public retrieval result | context_only | Exact dsmz585aOfficialPage attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch040/396/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi39061 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39061; Exact OLS term including label, definition, formula, charge, synonyms and obsolete status | supports | CHEBI:39061 has matching canonical label ACES. Source form assessment is separate. |
| chebi16810 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16810; Exact OLS term including label, definition, formula, charge, synonyms and obsolete status | supports | CHEBI:16810 has matching canonical label 2-oxoglutarate(2-). Source form assessment is separate. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS term including label, definition, formula, charge, synonyms and obsolete status | supports | CHEBI:2509 has matching canonical label agar. Source form assessment is separate. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS term including label, definition, formula, charge, synonyms and obsolete status | supports | CHEBI:91248 has matching canonical label L-cysteine hydrochloride hydrate. Source form assessment is separate. |
| chebi132767 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132767; Exact OLS term including label, definition, formula, charge, synonyms and obsolete status | supports | CHEBI:132767 has matching canonical label ferric pyrophosphate. Source form assessment is separate. |
| grounding-inventory | /private/tmp/culturemech-review-work-batch040/396/grounding-inventory.json; All primary/secondary instances; exact current index and legacy lookup scope | context_only | Five unique primary chemical IDs have canonical nonobsolete labels. Four current CHEBI-keyed secondary slots include one absent current preferred mapping, CHEBI:16810. Legacy 000555 is absent in the pinned current index/catalog/tree; its historical identity is unresolved. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete exact-key preferred-term lookup; adjacent pinned metadata | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows": {"CHEBI:132767": [{"label": "Fe4(PO4)2", "match_type": "preferred_term", "identifier": "CHEBI:132767", "preferred_term": "Fe4(PO4)2", "ontology_id": "CHEBI:132767", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16810": [], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type": "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| mim-current | https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json; Pinned current catalog; exact legacy ID search | supports | Complete current snapshot has no object or literal ID MediaIngredientMech:000555. This is a completed bounded negative lookup, not proof the historical identifier never existed. |
| history-metadata | data/merge_yaml/merged/BCYE_alpha_agar.yaml; data/normalized_yaml/bacterial/bcye_alpha_agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml", "events": 6, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer/guarded merger is implementation context only. The observed flattening and missing stage ownership do not prove execution of these exact current code bytes in the old import or merge. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer/guarded merger is implementation context only. The observed flattening and missing stage ownership do not prove execution of these exact current code bytes in the old import or merge. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer/guarded merger is implementation context only. The observed flattening and missing stage ownership do not prove execution of these exact current code bytes in the old import or merge. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Exact dsmz585a attempt retained HTTP 404. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response.
- Exact mediadive585aapi attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response.
- Exact mediadive585aapi_retry attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response.
- Exact dsmz585aOfficialPDF attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response.
- Exact dsmz585aOfficialPage attempt retained HTTP 503. No raw formulation was recovered from this attempt. The separate official-page web-tool projection has null HTTP status and is not a successful raw response.
- Partial completion reflects unavailable original legacy correspondence and missing raw official HTTP formulation, with the exact official web-tool projection separately retained. Its timestamp records preservation, not a measured retrieval interval or HTTP 200.
- No manufacturer formulation, source iron correction, titrant dose, independently measured final volume or organism growth is established.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T223542Z-culturemech-001712-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: bcye_alpha_agar (CultureMech:001712)'
started_at: '2026-10-21T22:32:19Z'
finished_at: '2026-10-21T22:35:42Z'
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
summary: The exact 585a official-page projection distinguishes a commercial alternative
  and four separately prepared solutions. Both local layers flatten their amounts
  into one ingredient list, including a volume-to-mass error for the commercial base,
  and omit the four water inputs and explicit solution doses. Fourteen preparation
  steps are retained, but their stock ownership is not structured. Source formula/prose
  conflict, a missing current MIM key and unresolved legacy correspondence require
  bounded follow-up.
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
  - path: data/merge_yaml/merged/BCYE_alpha_agar.yaml
    sha256: 306da84c945b6dd5b9656e7947a58b470797300365d16377d0f843933acc85dd
    role: target
  - path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
    sha256: 57f0a42492b0f935e9be13f5c3c8f235b19bd5c0e71967142c869f11e72b04f7
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/bcye_alpha_agar.yaml.md
    sha256: 9e03c3c71cd8d1f61a405ed778f0f7ee660a232033fe93c0d8e533d1199170f9
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
  selection: Task review 396; batch 040 item 6 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-nine task batches
    contain 390 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 6a639c4b597e95b6061f2d1c7baa04de84ba2f00
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 393 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001712
targets:
- target_id: CultureMech:001712
  path: data/merge_yaml/merged/BCYE_alpha_agar.yaml
  label: bcye_alpha_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/BCYE_alpha_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/BCYE_alpha_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch040/396/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/396/strict.tsv"
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/BCYE_alpha_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/BCYE_alpha_agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001712
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
  - CultureMech:001712
- check_id: dsmz585a-source-access
  name: 'Exact source content access: dsmz585a'
  required: false
  status: unavailable
  summary: Exact dsmz585a attempt retained HTTP 404. No raw formulation was recovered
    from this attempt. The separate official-page web-tool projection has null HTTP
    status and is not a successful raw response.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - dsmz585a-attempt
- check_id: mediadive585aapi-source-access
  name: 'Exact source content access: mediadive585aapi'
  required: false
  status: unavailable
  summary: Exact mediadive585aapi attempt retained HTTP 503. No raw formulation was
    recovered from this attempt. The separate official-page web-tool projection has
    null HTTP status and is not a successful raw response.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - mediadive585aapi-attempt
- check_id: mediadive585aapi_retry-source-access
  name: 'Exact source content access: mediadive585aapi_retry'
  required: false
  status: unavailable
  summary: Exact mediadive585aapi_retry attempt retained HTTP 503. No raw formulation
    was recovered from this attempt. The separate official-page web-tool projection
    has null HTTP status and is not a successful raw response.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - mediadive585aapi_retry-attempt
- check_id: dsmz585aOfficialPDF-source-access
  name: 'Exact source content access: dsmz585aOfficialPDF'
  required: false
  status: unavailable
  summary: Exact dsmz585aOfficialPDF attempt retained HTTP 503. No raw formulation
    was recovered from this attempt. The separate official-page web-tool projection
    has null HTTP status and is not a successful raw response.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - dsmz585aOfficialPDF-attempt
- check_id: dsmz585aOfficialPage-source-access
  name: 'Exact source content access: dsmz585aOfficialPage'
  required: true
  status: unavailable
  summary: Exact dsmz585aOfficialPage attempt retained HTTP 503. No raw formulation
    was recovered from this attempt. The separate official-page web-tool projection
    has null HTTP status and is not a successful raw response.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - dsmz585aOfficialPage-attempt
- check_id: legacy-original-correspondence
  name: Historical legacy MediaIngredientMech:000555 identity
  required: true
  status: unavailable
  summary: Current pinned index/catalog/tree were searched exactly and have no legacy
    object. No original historical object was recovered; primary ACES support does
    not authenticate that secondary identity.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - grounding-inventory
  - mim-current
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/BCYE_alpha_agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/BCYE_alpha_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:41.434865Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/BCYE_alpha_agar.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch040/396/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:42.470882Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-040/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch040/396/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/BCYE_alpha_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:43.723019Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/BCYE_alpha_agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T22:32:44.543495Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T22:35:41Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/bcye_alpha_agar.yaml:1:id: CultureMech:001712

    ./data/merge_yaml/merged/BCYE_alpha_agar.yaml:1:id: CultureMech:001712

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/source-preflight-bound/396/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T22:35:41Z'
  support: supports
  summary: 13 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 5e11d20b7558f75e9bbfd9c859b624d5e73624605cad46b312ed24a9b903a914
- evidence_id: primary-projection
  kind: database
  reference: https://bacmedia.dsmz.de/medium/585a?mobile=1
  locator: Official 585a page projected lines 70–158; preserved tool output, HTTP
    status null
  accessed_at: '2026-10-21T22:04:28.417267Z'
  support: supports
  summary: This is a full preserved official-page text projection, not recovered HTTP
    HTML or API raw. The recorded time is projection preservation time. Source recipe
    statements are usable with this limitation; direct HTTP retrieval remains unavailable.
  quote: 'L78: Final pH: 6.9'
  snapshot_sha256: 99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919
- evidence_id: dsmz585a-attempt
  kind: database
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium585a.pdf
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:02:49.344037Z'
  support: context_only
  summary: Exact dsmz585a attempt retained HTTP 404. No raw formulation was recovered
    from this attempt. The separate official-page web-tool projection has null HTTP
    status and is not a successful raw response.
  snapshot_sha256: 204a5955c3f6b572a77e0d49c48b5fcd340d60781b28b4b8dd2ee1c476f5d6a1
- evidence_id: mediadive585aapi-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/585a
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:02:48.349878Z'
  support: context_only
  summary: Exact mediadive585aapi attempt retained HTTP 503. No raw formulation was
    recovered from this attempt. The separate official-page web-tool projection has
    null HTTP status and is not a successful raw response.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadive585aapi_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/585a
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:03:45.468135Z'
  support: context_only
  summary: Exact mediadive585aapi_retry attempt retained HTTP 503. No raw formulation
    was recovered from this attempt. The separate official-page web-tool projection
    has null HTTP status and is not a successful raw response.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: dsmz585aOfficialPDF-attempt
  kind: database
  reference: https://bacmedia.dsmz.de/pdf/585a
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:03:46.085737Z'
  support: context_only
  summary: Exact dsmz585aOfficialPDF attempt retained HTTP 503. No raw formulation
    was recovered from this attempt. The separate official-page web-tool projection
    has null HTTP status and is not a successful raw response.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: dsmz585aOfficialPage-attempt
  kind: database
  reference: https://bacmedia.dsmz.de/medium/585a?mobile=1
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T22:03:46.098846Z'
  support: context_only
  summary: Exact dsmz585aOfficialPage attempt retained HTTP 503. No raw formulation
    was recovered from this attempt. The separate official-page web-tool projection
    has null HTTP status and is not a successful raw response.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/396/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7895b6ee2fd2f6631ada9d9721dd5819d4f92e494ce4579113ffec6d35b764de
- evidence_id: chebi39061
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39061
  locator: Exact OLS term including label, definition, formula, charge, synonyms and
    obsolete status
  accessed_at: '2026-10-21T22:02:49.943823Z'
  support: supports
  summary: CHEBI:39061 has matching canonical label ACES. Source form assessment is
    separate.
  snapshot_sha256: fff904e3ad8982128a1fcce42a2c7eb3d2271339fa18af47a4559be898e61719
- evidence_id: chebi16810
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16810
  locator: Exact OLS term including label, definition, formula, charge, synonyms and
    obsolete status
  accessed_at: '2026-10-21T22:02:49.747929Z'
  support: supports
  summary: CHEBI:16810 has matching canonical label 2-oxoglutarate(2-). Source form
    assessment is separate.
  snapshot_sha256: ed9d4b6102140f49ba3e57df7536a3825e73219eae009b89747d7cc01a6f7cd2
- evidence_id: chebi2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: Exact OLS term including label, definition, formula, charge, synonyms and
    obsolete status
  accessed_at: '2026-10-21T08:17:27.847373Z'
  support: supports
  summary: CHEBI:2509 has matching canonical label agar. Source form assessment is
    separate.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi91248
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: Exact OLS term including label, definition, formula, charge, synonyms and
    obsolete status
  accessed_at: '2026-10-21T08:42:32.136441Z'
  support: supports
  summary: CHEBI:91248 has matching canonical label L-cysteine hydrochloride hydrate.
    Source form assessment is separate.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: chebi132767
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132767
  locator: Exact OLS term including label, definition, formula, charge, synonyms and
    obsolete status
  accessed_at: '2026-10-21T09:27:39.168264Z'
  support: supports
  summary: CHEBI:132767 has matching canonical label ferric pyrophosphate. Source
    form assessment is separate.
  snapshot_sha256: 4264ab17d5b8af4f0619ab7fafb1e12fb178393bbba6d9f8150257dec67f9722
- evidence_id: grounding-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch040/396/grounding-inventory.json
  locator: All primary/secondary instances; exact current index and legacy lookup
    scope
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Five unique primary chemical IDs have canonical nonobsolete labels. Four
    current CHEBI-keyed secondary slots include one absent current preferred mapping,
    CHEBI:16810. Legacy 000555 is absent in the pinned current index/catalog/tree;
    its historical identity is unresolved.
  snapshot_sha256: fade31f8e420e24a1f5029d872327c4f6cda9fc81158df79c3adef7dbab6158f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete exact-key preferred-term lookup; adjacent pinned metadata
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "rows":
    {"CHEBI:132767": [{"label": "Fe4(PO4)2", "match_type": "preferred_term", "identifier":
    "CHEBI:132767", "preferred_term": "Fe4(PO4)2", "ontology_id": "CHEBI:132767",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16810": [], "CHEBI:2509":
    [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509",
    "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:91248": [{"label": "L-Cysteine HCl x H2O", "match_type":
    "preferred_term", "identifier": "CHEBI:91248", "preferred_term": "L-Cysteine HCl
    x H2O", "ontology_id": "CHEBI:91248", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-current
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/6643131b0f12ab40b66f98135245fca04027e0e9/docs/data/all_ingredients.json
  locator: Pinned current catalog; exact legacy ID search
  accessed_at: '2026-10-21T09:52:30.606764Z'
  support: supports
  summary: Complete current snapshot has no object or literal ID MediaIngredientMech:000555.
    This is a completed bounded negative lookup, not proof the historical identifier
    never existed.
  snapshot_sha256: 474ff60bd51606ef6e272b8b22d421bbe51d9f78567a114f94e59d04fe51acc7
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/BCYE_alpha_agar.yaml; data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/bcye_alpha_agar.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Current importer/guarded merger is implementation context only. The observed
    flattening and missing stage ownership do not prove execution of these exact current
    code bytes in the old import or merge.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Current importer/guarded merger is implementation context only. The observed
    flattening and missing stage ownership do not prove execution of these exact current
    code bytes in the old import or merge.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T22:35:41Z'
  support: context_only
  summary: Current importer/guarded merger is implementation context only. The observed
    flattening and missing stage ownership do not prove execution of these exact current
    code bytes in the old import or merge.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 41 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"name\": \"Commercial OXOID\
    \ base\",\n    \"stage\": \"Commercial alternative\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 1000,\n\
    \      \"source_unit\": \"ml\",\n      \"stock_water_input_ml\": null,\n     \
    \ \"final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 111; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L111: (with Legionella BCYE supplement)  | 1000  |\
    \ ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The source says 1000 ml of prepared commercial alternative,\
    \ not 1000 g/L; do not combine this alternative with the full separate formulation.\"\
    \n  },\n  {\n    \"decision_id\": \"q2\",\n    \"name\": \"Commercial OXOID base\"\
    ,\n    \"stage\": \"Commercial alternative\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 1000,\n\
    \      \"source_unit\": \"ml\",\n      \"stock_water_input_ml\": null,\n     \
    \ \"final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 111; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L111: (with Legionella BCYE supplement)  | 1000  |\
    \ ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The source says 1000 ml of prepared commercial alternative,\
    \ not 1000 g/L; do not combine this alternative with the full separate formulation.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"name\": \"ACES\",\n    \"stage\"\
    : \"Solution A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20.4082\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 10,\n\
    \      \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"\
    final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 122; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L122: (N-2-acetamido-2-aminoethane-sulfonic acid)\
    \  | 10  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q4\",\n    \"name\": \"ACES\",\n    \"stage\": \"Solution A\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20.4082\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 10,\n\
    \      \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"\
    final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 122; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L122: (N-2-acetamido-2-aminoethane-sulfonic acid)\
    \  | 10  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q5\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"Solution A\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"20.4082\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"source_batch_amount\": 10,\n      \"source_unit\"\
    : \"g\",\n      \"stock_water_input_ml\": 490,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 124;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L124: (Difco 0127)  | 10\
    \  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q6\",\n    \"name\": \"Yeast extract\",\n    \"stage\": \"Solution A\",\n\
    \    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"\
    field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"20.4082\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 10,\n     \
    \ \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 124;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L124: (Difco 0127)  | 10\
    \  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q7\",\n    \"name\": \"Activated charcoal\",\n    \"stage\": \"Solution A\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"4.08163\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n\
    \    \"desired\": {\n      \"source_batch_amount\": 2,\n      \"source_unit\"\
    : \"g\",\n      \"stock_water_input_ml\": 490,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 126;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L126: (Sigma C 5510)  | 2\
    \  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q8\",\n    \"name\": \"Activated charcoal\",\n    \"stage\": \"Solution A\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"\
    field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n     \
    \     \"value\": \"4.08163\",\n          \"unit\": \"G_PER_L\"\n        }\n  \
    \    }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 2,\n      \"\
    source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 126;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L126: (Sigma C 5510)  | 2\
    \  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"name\": \"Disodium alpha-ketoglutarate\",\n    \"stage\": \"\
    Solution A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n   \
    \     \"field_path\": \"ingredients[4].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.04082\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 1,\n    \
    \  \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 127;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L127: [Input]  | Na_{2} alpha-ketoglutarate\
    \  | 1  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q10\",\n    \"name\": \"Disodium alpha-ketoglutarate\",\n    \"stage\": \"\
    Solution A\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.04082\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 1,\n\
    \      \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"\
    final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 127; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L127: [Input]  | Na_{2} alpha-ketoglutarate  | 1 \
    \ | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 128;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L128: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"name\": \"Agar\",\n    \"stage\": \"Solution B\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30.6122\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 15,\n\
    \      \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"\
    final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 136; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L136: [Input]  | Agar  | 15  | g\",\n        \"snapshot_sha256\"\
    : \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\",\n    \
    \    \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 137;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L137: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"name\": \"Agar\",\n    \"stage\": \"Solution B\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30.6122\",\n          \"unit\": \"G_PER_L\"\n    \
    \    }\n      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 15,\n\
    \      \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 490,\n      \"\
    final_medium_concentration\": null\n    },\n    \"source_snippets\": [\n     \
    \ {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 136; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L136: [Input]  | Agar  | 15  | g\",\n        \"snapshot_sha256\"\
    : \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\",\n    \
    \    \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 137;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L137: [Input]  | Distilled\
    \ water  | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"name\": \"L-cysteine hydrochloride monohydrate\",\n    \"stage\"\
    : \"Solution C\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 0.4,\n  \
    \    \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 10,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 146;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L146: [Input]  | L-Cysteine\
    \ HCl x H_{2}O  | 0.4  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 147;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L147: [Input]  | Distilled\
    \ water  | 10.0  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"name\": \"L-cysteine hydrochloride monohydrate\",\n    \"stage\"\
    : \"Solution C\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"40\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 0.4,\n  \
    \    \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 10,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 146;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L146: [Input]  | L-Cysteine\
    \ HCl x H_{2}O  | 0.4  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 147;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L147: [Input]  | Distilled\
    \ water  | 10.0  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"name\": \"Literal Fe4(PO4)2\",\n    \"stage\": \"Solution D\"\
    ,\n    \"decision\": \"conflict\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\"\
    : \"ingredients[7].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"25\",\n          \"unit\": \"G_PER_L\"\n        }\n      }\n    ],\n    \"\
    desired\": {\n      \"source_batch_amount\": 0.25,\n      \"source_unit\": \"\
    g\",\n      \"stock_water_input_ml\": 10,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 155;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L155: [Input]  | Fe_{4}(PO_{4})_{2}\
    \  | 0.25  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 156;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L156: [Input]  | Distilled\
    \ water  | 10.00  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 158;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L158: 2 Please note: Soluble\
    \ ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical\
    \ looses its green colour and becomes brown or yellow.\",\n        \"snapshot_sha256\"\
    : \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\",\n    \
    \    \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate. The printed formula conflicts\
    \ with the source prose ferric pyrophosphate; preserve both pending reconciliation.\"\
    \n  },\n  {\n    \"decision_id\": \"q16\",\n    \"name\": \"Literal Fe4(PO4)2\"\
    ,\n    \"stage\": \"Solution D\",\n    \"decision\": \"conflict\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_batch_amount\": 0.25,\n \
    \     \"source_unit\": \"g\",\n      \"stock_water_input_ml\": 10,\n      \"final_medium_concentration\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 155;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L155: [Input]  | Fe_{4}(PO_{4})_{2}\
    \  | 0.25  | g\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 156;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L156: [Input]  | Distilled\
    \ water  | 10.00  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 158;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L158: 2 Please note: Soluble\
    \ ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical\
    \ looses its green colour and becomes brown or yellow.\",\n        \"snapshot_sha256\"\
    : \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\",\n    \
    \    \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The stored rate is flattened outside\
    \ its named stock. Restore the printed batch amount and stage; no density or measured\
    \ final volume is available. The numerical rate can describe the stock water basis,\
    \ not an independently established final-medium rate. The printed formula conflicts\
    \ with the source prose ferric pyrophosphate; preserve both pending reconciliation.\"\
    \n  },\n  {\n    \"decision_id\": \"q17\",\n    \"name\": \"Distilled water\"\
    ,\n    \"stage\": \"Solution A preparation\",\n    \"decision\": \"add\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 490,\n      \"source_unit\": \"ml\"\
    ,\n      \"stage\": \"A\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"\
    https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\":\
    \ \"Preserved official web-tool projection line 128; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L128: [Input]  | Distilled water  | 490  | ml\",\n\
    \        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"No local solvent entry exists. Keep\
    \ each water input attached to its own preparation; their sum is not a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q18\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"Solution B preparation\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 490,\n      \"source_unit\": \"ml\"\
    ,\n      \"stage\": \"B\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"\
    https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\":\
    \ \"Preserved official web-tool projection line 137; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L137: [Input]  | Distilled water  | 490  | ml\",\n\
    \        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"No local solvent entry exists. Keep\
    \ each water input attached to its own preparation; their sum is not a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"Solution C preparation\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 10,\n      \"source_unit\": \"ml\"\
    ,\n      \"stage\": \"C\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"\
    https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\":\
    \ \"Preserved official web-tool projection line 147; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L147: [Input]  | Distilled water  | 10.0  | ml\",\n\
    \        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"No local solvent entry exists. Keep\
    \ each water input attached to its own preparation; their sum is not a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"name\": \"\
    Distilled water\",\n    \"stage\": \"Solution D preparation\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ingredients\",\n        \"stored\": [\n          {\n\
    \            \"preferred_term\": \"OXOID Legionella CYE-Agar base\",\n       \
    \     \"concentration\": {\n              \"value\": \"1000\",\n             \
    \ \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n          \
    \  \"preferred_term\": \"ACES\",\n            \"term\": {\n              \"id\"\
    : \"CHEBI:39061\",\n              \"label\": \"ACES\"\n            },\n      \
    \      \"concentration\": {\n              \"value\": \"20.4082\",\n         \
    \     \"unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_term\"\
    : {\n              \"id\": \"MediaIngredientMech:000555\",\n              \"label\"\
    : \"ACES\"\n            }\n          },\n          {\n            \"preferred_term\"\
    : \"Yeast extract\",\n            \"concentration\": {\n              \"value\"\
    : \"20.4082\",\n              \"unit\": \"G_PER_L\"\n            }\n         \
    \ },\n          {\n            \"preferred_term\": \"Activated charcoal\",\n \
    \           \"concentration\": {\n              \"value\": \"4.08163\",\n    \
    \          \"unit\": \"G_PER_L\"\n            }\n          },\n          {\n \
    \           \"preferred_term\": \"Na2 alpha-ketoglutarate\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:16810\",\n              \"label\": \"2-oxoglutarate(2-)\"\
    \n            },\n            \"concentration\": {\n              \"value\": \"\
    2.04082\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:16810\",\n\
    \              \"label\": \"2-oxoglutarate(2-)\"\n            }\n          },\n\
    \          {\n            \"preferred_term\": \"Agar\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:2509\",\n              \"label\": \"agar\"\n\
    \            },\n            \"concentration\": {\n              \"value\": \"\
    30.6122\",\n              \"unit\": \"G_PER_L\"\n            },\n            \"\
    mediaingredientmech_chebi_term\": {\n              \"id\": \"CHEBI:2509\",\n \
    \             \"label\": \"agar\"\n            }\n          },\n          {\n\
    \            \"preferred_term\": \"L-Cysteine HCl x H2O\",\n            \"term\"\
    : {\n              \"id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine\
    \ hydrochloride hydrate\"\n            },\n            \"concentration\": {\n\
    \              \"value\": \"40\",\n              \"unit\": \"G_PER_L\"\n     \
    \       },\n            \"mediaingredientmech_chebi_term\": {\n              \"\
    id\": \"CHEBI:91248\",\n              \"label\": \"L-cysteine hydrochloride hydrate\"\
    \n            }\n          },\n          {\n            \"preferred_term\": \"\
    Fe4(PO4)2\",\n            \"term\": {\n              \"id\": \"CHEBI:132767\"\
    ,\n              \"label\": \"ferric pyrophosphate\"\n            },\n       \
    \     \"concentration\": {\n              \"value\": \"25\",\n              \"\
    unit\": \"G_PER_L\"\n            },\n            \"mediaingredientmech_chebi_term\"\
    : {\n              \"id\": \"CHEBI:132767\",\n              \"label\": \"ferric\
    \ pyrophosphate\"\n            }\n          }\n        ]\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_amount\": 10,\n      \"source_unit\": \"ml\"\
    ,\n      \"stage\": \"D\"\n    },\n    \"source_snippets\": [\n      {\n     \
    \   \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"\
    https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\":\
    \ \"Preserved official web-tool projection line 156; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L156: [Input]  | Distilled water  | 10.00  | ml\"\
    ,\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"No local solvent entry exists. Keep\
    \ each water input attached to its own preparation; their sum is not a measured\
    \ final volume.\"\n  },\n  {\n    \"decision_id\": \"q21\",\n    \"name\": \"\
    Solution A dose\",\n    \"stage\": \"Main assembly\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"desired\": {\n      \"source_amount\": 490,\n      \"source_unit\"\
    : \"ml\",\n      \"stage\": \"A\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 94; not raw HTTP\",\n        \"\
    exact_source_quote\": \"L94: [Input]  | cite26†Solution A | 490  | ml\",\n\
    \        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 103;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L103: 6 Finally, add solution\
    \ B. Swirl medium in flask during dispensing to petri dishes or tubes in order\
    \ to keep charcoal suspended.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The source explicitly lists the receiving\
    \ doses; retain their sequence and commercial alternative. These are stock-addition\
    \ volumes, not masses or stock solute concentrations.\"\n  },\n  {\n    \"decision_id\"\
    : \"q22\",\n    \"name\": \"Solution B dose\",\n    \"stage\": \"Main assembly\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\": \"\
    solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      }\n    ],\n    \"desired\":\
    \ {\n      \"source_amount\": 490,\n      \"source_unit\": \"ml\",\n      \"stage\"\
    : \"B\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 95;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L95: [Input]  | cite27†Solution\
    \ B | 490  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 103;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L103: 6 Finally, add solution\
    \ B. Swirl medium in flask during dispensing to petri dishes or tubes in order\
    \ to keep charcoal suspended.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The source explicitly lists the receiving\
    \ doses; retain their sequence and commercial alternative. These are stock-addition\
    \ volumes, not masses or stock solute concentrations.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"name\": \"Solution C dose\",\n    \"stage\": \"Main assembly\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\": \"\
    solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      }\n    ],\n    \"desired\":\
    \ {\n      \"source_amount\": 10,\n      \"source_unit\": \"ml\",\n      \"stage\"\
    : \"C\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 96;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L96: [Input]  | cite28†Solution\
    \ C | 10  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 103;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L103: 6 Finally, add solution\
    \ B. Swirl medium in flask during dispensing to petri dishes or tubes in order\
    \ to keep charcoal suspended.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The source explicitly lists the receiving\
    \ doses; retain their sequence and commercial alternative. These are stock-addition\
    \ volumes, not masses or stock solute concentrations.\"\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"name\": \"Solution D dose\",\n    \"stage\": \"Main assembly\"\
    ,\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\": \"\
    solutions\",\n        \"stored\": null\n      },\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"field_path\"\
    : \"solutions\",\n        \"stored\": null\n      }\n    ],\n    \"desired\":\
    \ {\n      \"source_amount\": 10,\n      \"source_unit\": \"ml\",\n      \"stage\"\
    : \"D\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 97;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L97: [Input]  | cite29†Solution\
    \ D | 10  | ml\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 103;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L103: 6 Finally, add solution\
    \ B. Swirl medium in flask during dispensing to petri dishes or tubes in order\
    \ to keep charcoal suspended.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The source explicitly lists the receiving\
    \ doses; retain their sequence and commercial alternative. These are stock-addition\
    \ volumes, not masses or stock solute concentrations.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"name\": \"Preparation step 1\",\n    \"stage\": \"Main/commercial/A/B/C/D\
    \ stages as stated\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Prepare OXOID Legionella CYE-Agar base or solution A.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Prepare OXOID Legionella CYE-Agar base or solution A.\"\n      }\n    ],\n\
    \    \"desired\": {\n      \"source_instruction\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n      \"scope\": \"Preserve exact stage, including\
    \ all stated numbers\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 98;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L98: 1 Prepare OXOID Legionella\
    \ CYE-Agar base or solution A.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q26\",\n    \"name\": \"Preparation step 2\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Cool down to 50 °C.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Cool down to 50 °C.\"\n      }\n    ],\n    \"desired\": {\n      \"source_instruction\"\
    : \"L99: 2 Cool down to 50 °C.\",\n      \"scope\": \"Preserve exact stage, including\
    \ all stated numbers\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 99;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L99: 2 Cool down to 50 °C.\"\
    ,\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q27\",\n    \"name\": \"Preparation step 3\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"Add solution C (Cysteine-HCl) and solution D (ferric pyrophosphate).\"\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"Add solution C (Cysteine-HCl) and solution D (ferric pyrophosphate).\"\n \
    \     }\n    ],\n    \"desired\": {\n      \"source_instruction\": \"L100: 3 Add\
    \ solution C (Cysteine-HCl) and solution D (ferric pyrophosphate).\",\n      \"\
    scope\": \"Preserve exact stage, including all stated numbers\"\n    },\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\"\
    ,\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 100;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L100: 3 Add solution C (Cysteine-HCl)\
    \ and solution D (ferric pyrophosphate).\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q28\",\n    \"name\": \"Preparation step 4\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : \"Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : \"Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.\"\n      }\n    ],\n    \"\
    desired\": {\n      \"source_instruction\": \"L101: 4 Adjust pH to 6.9 with sterile\
    \ 1.0 N KOH or HCl.\",\n      \"scope\": \"Preserve exact stage, including all\
    \ stated numbers\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 101;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L101: 4 Adjust pH to 6.9\
    \ with sterile 1.0 N KOH or HCl.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q29\",\n    \"name\": \"Preparation step 5\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[4].description\",\n        \"stored\"\
    : \"The pH of the medium is critical.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"field_path\"\
    : \"preparation_steps[4].description\",\n        \"stored\": \"The pH of the medium\
    \ is critical.\"\n      }\n    ],\n    \"desired\": {\n      \"source_instruction\"\
    : \"L102: 5 The pH of the medium is critical.\",\n      \"scope\": \"Preserve\
    \ exact stage, including all stated numbers\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n       \
    \ \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n       \
    \ \"source_locator\": \"Preserved official web-tool projection line 102; not raw\
    \ HTTP\",\n        \"exact_source_quote\": \"L102: 5 The pH of the medium is critical.\"\
    ,\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q30\",\n    \"name\": \"Preparation step 6\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[5].description\",\n        \"stored\"\
    : \"Finally, add solution B. Swirl medium in flask during dispensing to petri\
    \ dishes or tubes in order to keep charcoal suspended.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"preparation_steps[5].description\",\n        \"stored\"\
    : \"Finally, add solution B. Swirl medium in flask during dispensing to petri\
    \ dishes or tubes in order to keep charcoal suspended.\"\n      }\n    ],\n  \
    \  \"desired\": {\n      \"source_instruction\": \"L103: 6 Finally, add solution\
    \ B. Swirl medium in flask during dispensing to petri dishes or tubes in order\
    \ to keep charcoal suspended.\",\n      \"scope\": \"Preserve exact stage, including\
    \ all stated numbers\"\n    },\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 103;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L103: 6 Finally, add solution\
    \ B. Swirl medium in flask during dispensing to petri dishes or tubes in order\
    \ to keep charcoal suspended.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q31\",\n    \"name\": \"Preparation step 7\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[6].description\",\n        \"stored\"\
    : \"Dehydrated media preparations are available from media distributors.\"\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[6].description\",\n        \"stored\"\
    : \"Dehydrated media preparations are available from media distributors.\"\n \
    \     }\n    ],\n    \"desired\": {\n      \"source_instruction\": \"L112: 1 Dehydrated\
    \ media preparations are available from media distributors.\",\n      \"scope\"\
    : \"Preserve exact stage, including all stated numbers\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n       \
    \ \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n       \
    \ \"source_locator\": \"Preserved official web-tool projection line 112; not raw\
    \ HTTP\",\n        \"exact_source_quote\": \"L112: 1 Dehydrated media preparations\
    \ are available from media distributors.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q32\",\n    \"name\": \"Preparation step 8\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[7].description\",\n        \"stored\"\
    : \"We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[7].description\",\n        \"stored\"\
    : \"We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement.\"\n\
    \      }\n    ],\n    \"desired\": {\n      \"source_instruction\": \"L113: 2\
    \ We use OXOID Legionella CYE-Agar base with Legionella BCYE supplement.\",\n\
    \      \"scope\": \"Preserve exact stage, including all stated numbers\"\n   \
    \ },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\"\
    ,\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 113;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L113: 2 We use OXOID Legionella\
    \ CYE-Agar base with Legionella BCYE supplement.\",\n        \"snapshot_sha256\"\
    : \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\",\n    \
    \    \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q33\",\n    \"name\": \"Preparation step 9\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[8].description\",\n        \"stored\"\
    : \"Note: Alternatively use CYE-ACES AGAR\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"field_path\"\
    : \"preparation_steps[8].description\",\n        \"stored\": \"Note: Alternatively\
    \ use CYE-ACES AGAR\"\n      }\n    ],\n    \"desired\": {\n      \"source_instruction\"\
    : \"L114: 3 Note: Alternatively use CYE-ACES AGAR\",\n      \"scope\": \"Preserve\
    \ exact stage, including all stated numbers\"\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n       \
    \ \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n       \
    \ \"source_locator\": \"Preserved official web-tool projection line 114; not raw\
    \ HTTP\",\n        \"exact_source_quote\": \"L114: 3 Note: Alternatively use CYE-ACES\
    \ AGAR\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q34\",\n    \"name\": \"Preparation step 10\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[9].description\",\n        \"stored\"\
    : \"Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other\
    \ components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool\
    \ to 50 - 55°C.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[9].description\",\n        \"stored\"\
    : \"Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other\
    \ components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool\
    \ to 50 - 55°C.\"\n      }\n    ],\n    \"desired\": {\n      \"source_instruction\"\
    : \"L129: 1 Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the\
    \ other components and dissolve by boiling. Autoclave at 121°C for 15 minutes.\
    \ Cool to 50 - 55°C.\",\n      \"scope\": \"Preserve exact stage, including all\
    \ stated numbers\"\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 129;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L129: 1 Dissolve ACES and\
    \ bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve\
    \ by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C.\",\n     \
    \   \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q35\",\n    \"name\": \"Preparation step 11\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[10].description\",\n        \"\
    stored\": \"Autoclave at 121°C and cool to 50 - 55°C.\"\n      },\n      {\n \
    \       \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n\
    \        \"field_path\": \"preparation_steps[10].description\",\n        \"stored\"\
    : \"Autoclave at 121°C and cool to 50 - 55°C.\"\n      }\n    ],\n    \"desired\"\
    : {\n      \"source_instruction\": \"L138: 1 Autoclave at 121°C and cool to 50\
    \ - 55°C.\",\n      \"scope\": \"Preserve exact stage, including all stated numbers\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\"\
    ,\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 138;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L138: 1 Autoclave at 121°C\
    \ and cool to 50 - 55°C.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q36\",\n    \"name\": \"Preparation step 12\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[11].description\",\n        \"\
    stored\": \"Prepare a fresh solution and filter-sterilize it.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[11].description\",\n        \"\
    stored\": \"Prepare a fresh solution and filter-sterilize it.\"\n      }\n   \
    \ ],\n    \"desired\": {\n      \"source_instruction\": \"L148: 1 Prepare a fresh\
    \ solution and filter-sterilize it.\",\n      \"scope\": \"Preserve exact stage,\
    \ including all stated numbers\"\n    },\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 148; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L148: 1 Prepare a fresh solution and filter-sterilize\
    \ it.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q37\",\n    \"name\": \"Preparation step 13\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[12].description\",\n        \"\
    stored\": \"Prepare a fresh solution by heating to 50 - 55°C in a water-bath.\
    \ Filter-sterilize solution separately.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n        \"field_path\"\
    : \"preparation_steps[12].description\",\n        \"stored\": \"Prepare a fresh\
    \ solution by heating to 50 - 55°C in a water-bath. Filter-sterilize solution\
    \ separately.\"\n      }\n    ],\n    \"desired\": {\n      \"source_instruction\"\
    : \"L157: 1 Prepare a fresh solution by heating to 50 - 55°C in a water-bath.\
    \ Filter-sterilize solution separately.\",\n      \"scope\": \"Preserve exact\
    \ stage, including all stated numbers\"\n    },\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n        \"source_url\"\
    : \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n        \"source_locator\"\
    : \"Preserved official web-tool projection line 157; not raw HTTP\",\n       \
    \ \"exact_source_quote\": \"L157: 1 Prepare a fresh solution by heating to 50\
    \ - 55°C in a water-bath. Filter-sterilize solution separately.\",\n        \"\
    snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q38\",\n    \"name\": \"Preparation step 14\",\n    \"stage\"\
    : \"Main/commercial/A/B/C/D stages as stated\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[13].description\",\n        \"\
    stored\": \"Please note: Soluble ferric pyrophosphate must be kept dry and in\
    \ the dark. Do not use if chemical looses its green colour and becomes brown or\
    \ yellow.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[13].description\",\n        \"\
    stored\": \"Please note: Soluble ferric pyrophosphate must be kept dry and in\
    \ the dark. Do not use if chemical looses its green colour and becomes brown or\
    \ yellow.\"\n      }\n    ],\n    \"desired\": {\n      \"source_instruction\"\
    : \"L158: 2 Please note: Soluble ferric pyrophosphate must be kept dry and in\
    \ the dark. Do not use if chemical looses its green colour and becomes brown or\
    \ yellow.\",\n      \"scope\": \"Preserve exact stage, including all stated numbers\"\
    \n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\"\
    ,\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 158;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L158: 2 Please note: Soluble\
    \ ferric pyrophosphate must be kept dry and in the dark. Do not use if chemical\
    \ looses its green colour and becomes brown or yellow.\",\n        \"snapshot_sha256\"\
    : \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\",\n    \
    \    \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers already retain this instruction.\
    \ Attach stage-specific support and retain all numerical qualifiers; do not generalize\
    \ the A sterilization time to B or the filter steps to A/B.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q39\",\n    \"name\": \"Main pH\",\n    \"stage\": \"Final\
    \ medium\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": 6.9\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 6.9\n      }\n \
    \   ],\n    \"desired\": {\n      \"value\": 6.9\n    },\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n       \
    \ \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n       \
    \ \"source_locator\": \"Preserved official web-tool projection line 78; not raw\
    \ HTTP\",\n        \"exact_source_quote\": \"L78: Final pH: 6.9\",\n        \"\
    snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 101;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L101: 4 Adjust pH to 6.9\
    \ with sterile 1.0 N KOH or HCl.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The main pH agrees. The same numerical\
    \ A-adjustment pH is a separate preparation stage, not independent evidence of\
    \ the measured final volume.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n   \
    \ \"name\": \"Titrant strength and unspecified dose\",\n    \"stage\": \"Main\
    \ and A pH adjustment\",\n    \"decision\": \"not_quantified\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : \"Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.\"\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\",\n  \
    \      \"field_path\": \"preparation_steps[3].description\",\n        \"stored\"\
    : \"Adjust pH to 6.9 with sterile 1.0 N KOH or HCl.\"\n      },\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"\
    field_path\": \"preparation_steps[9].description\",\n        \"stored\": \"Dissolve\
    \ ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other components\
    \ and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[9].description\",\n        \"stored\"\
    : \"Dissolve ACES and bring to pH 6.9 by slowly adding 1 N KOH. Add the other\
    \ components and dissolve by boiling. Autoclave at 121°C for 15 minutes. Cool\
    \ to 50 - 55°C.\"\n      }\n    ],\n    \"desired\": {\n      \"main_titrants\"\
    : \"sterile 1.0 N KOH or HCl\",\n      \"A_titrant\": \"1 N KOH\",\n      \"dose\"\
    : null\n    },\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    bacmedia585aWebProjection\",\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\"\
    ,\n        \"source_locator\": \"Preserved official web-tool projection line 101;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L101: 4 Adjust pH to 6.9\
    \ with sterile 1.0 N KOH or HCl.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 129;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L129: 1 Dissolve ACES and\
    \ bring to pH 6.9 by slowly adding 1 N KOH. Add the other components and dissolve\
    \ by boiling. Autoclave at 121°C for 15 minutes. Cool to 50 - 55°C.\",\n     \
    \   \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain normality as stated. No fixed\
    \ volume, molarity conversion or mass follows without further information.\"\n\
    \  },\n  {\n    \"decision_id\": \"q41\",\n    \"name\": \"Unknown incubation\
    \ and final-volume measurement\",\n    \"stage\": \"Whole medium\",\n    \"decision\"\
    : \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/BCYE_alpha_agar.yaml\",\n        \"field_path\": \"temperature_value\"\
    ,\n        \"stored\": null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"temperature_value\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"temperature_range\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/merge_yaml/merged/BCYE_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/bcye_alpha_agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"desired\": {\n      \"incubation_temperature\": null,\n  \
    \    \"measured_final_volume\": null,\n      \"B_cycle_minutes\": null\n    },\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"bacmedia585aWebProjection\"\
    ,\n        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 54;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L54: [Input: 1000]\",\n \
    \       \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 78;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L78: Final pH: 6.9\",\n \
    \       \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      },\n      {\n        \"source_key\": \"bacmedia585aWebProjection\",\n\
    \        \"source_url\": \"https://bacmedia.dsmz.de/medium/585a?mobile=1\",\n\
    \        \"source_locator\": \"Preserved official web-tool projection line 138;\
    \ not raw HTTP\",\n        \"exact_source_quote\": \"L138: 1 Autoclave at 121°C\
    \ and cool to 50 - 55°C.\",\n        \"snapshot_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    ,\n        \"parsed_text_sha256\": \"99d369ed20e8d77549c773e87219a067f70530a5b87f0eb78773e0c9f5ea0919\"\
    \n      }\n    ],\n    \"interpretation\": \"The displayed 1000 ml main volume\
    \ and additive dosing are source presentation, not a measured volume. Heating/cooling\
    \ temperatures are preparation only. B has no stated duration.\"\n  }\n]"
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact 585a identity and commercial alternative
  outcome: supported
  summary: The one maintained contributor, accession 585a and official projected page
    identify this medium. The commercial base is an alternative preparation; a fingerprint
    or shared name does not authorize summing it with all four independently prepared
    solutions.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - record
  - owner-0
  - primary-projection
- assessment_id: forms
  area: grounding
  topic: Chemical forms, salts and source-internal conflict
  outcome: concern
  summary: ACES and agar names match their asserted primary terms. CHEBI:91248 includes
    the monohydrate formula and exact L-cysteine hydrochloride monohydrate synonyms,
    supporting the source form. CHEBI:16810 is the bare dianion (charge −2, no sodium),
    not the complete supplied disodium salt. CHEBI:132767 describes four Fe(III) ions
    with three diphosphates; it agrees with the prose ferric pyrophosphate but not
    literal Fe4(PO4)2. Do not silently repair this source conflict or infer a replacement
    identity. Yeast extract, charcoal and commercial base are not grounded as pure
    chemicals.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - primary-projection
  - grounding-inventory
  - chebi39061
  - chebi16810
  - chebi2509
  - chebi91248
  - chebi132767
- assessment_id: linkage
  area: grounding
  topic: Instance linkage and exact current membership
  outcome: concern
  summary: On the target denominator of eight ingredient instances, five primary links
    give 62.5% linkage and four CHEBI-keyed secondary links give 50%; one separate
    legacy slot gives 12.5%. These are linkage metrics, not correctness. Current CHEBI:16810
    secondary membership is absent; legacy 000555 historical correspondence remains
    unavailable despite successful current negative searches.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - mim
  - mim-current
  - grounding-inventory
- assessment_id: preparation
  area: completeness
  topic: Retained instructions and missing stock structure
  outcome: concern
  summary: Both layers retain fourteen steps, pH 6.9, cooling and filtration. Their
    missing explicit A/B/C/D composition and dose boundaries obscure those instructions.
    A alone specifies 121 °C for 15 minutes; B specifies 121 °C without duration,
    C/D are separately filtered and D is warmed. Unknown acid/base doses remain unquantified.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - record
  - owner-0
  - primary-projection
  - quantity-inventory
- assessment_id: biology
  area: scope
  topic: Classification and growth scope
  outcome: supported
  summary: Agar and complex commercial/yeast material support a complex undefined
    solid medium. Preparation temperatures do not establish growth temperature or
    oxygen conditions. No species-specific growth or taxonomic assertions are inferred
    from the commercial Legionella name.
  target_ids:
  - CultureMech:001712
  evidence_ids:
  - record
  - primary-projection
findings:
- finding_id: f1
  issue_key: culturemech.001712.flat-alternative-and-stock-amounts
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Alternative and stock amounts are flattened
  description: Both layers store commercial 1000 ml as 1000 G_PER_L and stock-normalized
    solute rates as direct ingredients. The commercial alternative and four stock
    formulations cannot be treated as one cumulative formula.
  target_ids:
  - CultureMech:001712
  field_paths:
  - ingredients[*].concentration
  - solutions
  evidence_ids:
  - primary-projection
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
  issue_key: culturemech.001712.missing-solvent-and-stage-ownership
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Four solvent inputs and explicit stock doses are absent
  description: Both layers retain preparation prose but omit the A/B/C/D water entries
    and structured stock-dose ownership, leaving critical quantities outside the represented
    formulation.
  target_ids:
  - CultureMech:001712
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - primary-projection
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
  issue_key: culturemech.001712.supplied-form-conflicts
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Counterion and iron formula require reconciliation
  description: The disodium source is grounded to a bare dianion, and the iron formula
    differs from both source prose and the asserted ferric pyrophosphate structure.
  target_ids:
  - CultureMech:001712
  field_paths:
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  - ingredients[7].preferred_term
  - ingredients[7].term
  - ingredients[7].mediaingredientmech_chebi_term
  evidence_ids:
  - primary-projection
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
  issue_key: culturemech.001712.secondary-current-and-historical-gaps
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Secondary correspondence is unresolved
  description: CHEBI:16810 has no mapped preferred row in the exact current MIM index.
    Legacy 000555 is absent from current snapshots, while its original historical
    identity is unavailable. Primary OLS existence does not authenticate either secondary
    assertion.
  target_ids:
  - CultureMech:001712
  field_paths:
  - ingredients[1].mediaingredientmech_term
  - ingredients[4].mediaingredientmech_chebi_term
  evidence_ids:
  - mim
  - mim-current
  - grounding-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.1
  native_severity: P2.1
  normalization_reason: P2.1 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Represent the exact commercial alternative and A/B/C/D batch compositions
    and receiving doses separately, with source evidence; do not calculate final concentrations
    from an assumed measured volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001712
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
  description: Restore the four solvent inputs and exact source-stage associations
    while preserving existing preparation and unknown quantities; regenerate only
    after owner review.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001712
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
  description: Resolve the exact supplied disodium and iron forms from authoritative
    source clarification; preserve source conflict and mass amounts without inventing
    replacements.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001712
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
  description: Resolve or qualify the current secondary membership independently from
    the historical legacy lookup; retain the unresolved history instead of fabricating
    a mapping.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001712
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/bcye_alpha_agar.yaml
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
- Exact dsmz585a attempt retained HTTP 404. No raw formulation was recovered from
  this attempt. The separate official-page web-tool projection has null HTTP status
  and is not a successful raw response.
- Exact mediadive585aapi attempt retained HTTP 503. No raw formulation was recovered
  from this attempt. The separate official-page web-tool projection has null HTTP
  status and is not a successful raw response.
- Exact mediadive585aapi_retry attempt retained HTTP 503. No raw formulation was recovered
  from this attempt. The separate official-page web-tool projection has null HTTP
  status and is not a successful raw response.
- Exact dsmz585aOfficialPDF attempt retained HTTP 503. No raw formulation was recovered
  from this attempt. The separate official-page web-tool projection has null HTTP
  status and is not a successful raw response.
- Exact dsmz585aOfficialPage attempt retained HTTP 503. No raw formulation was recovered
  from this attempt. The separate official-page web-tool projection has null HTTP
  status and is not a successful raw response.
- Partial completion reflects unavailable original legacy correspondence and missing
  raw official HTTP formulation, with the exact official web-tool projection separately
  retained. Its timestamp records preservation, not a measured retrieval interval
  or HTTP 200.
- No manufacturer formulation, source iron correction, titrant dose, independently
  measured final volume or organism growth is established.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-040
- generated-medium
```
