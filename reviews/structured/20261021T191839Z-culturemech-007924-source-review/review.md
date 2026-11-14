# Source and formulation review: alkaline_malt_extract_agar (CultureMech:007924)

- Review: 20261021T191839Z-culturemech-007924-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:13:57Z
- Finished UTC: 2026-10-21T19:18:39Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M138 identifies the bacterial JCM 147 record, but the exact primary returns Nothing found. The two layers have incorrect stock identities, water/solution units and lost preparation stages; the review remains partial for primary-source verification.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 350; batch 035 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-four task batches contain 340 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 343 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007924 | data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml | generated | alkaline_malt_extract_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007924 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007924 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/350/strict.tsv |
| validate-terms | passed | True | CultureMech:007924 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007924 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007924 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm147 | unavailable | True | CultureMech:007924 | The exact JCM 147 request returned HTTP 200 Nothing found, with no usable recipe or default sterilization instruction. Required original-source verification remains unavailable; this review is partial. |
| Exact source content access: mediadiveJ147 | unavailable | False | CultureMech:007924 | Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content. |
| Exact source content access: mediadiveJ147Retry1 | unavailable | False | CultureMech:007924 | Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content. |
| Exact source content access: togoM138 | unavailable | False | CultureMech:007924 | Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007924.

The four documented recipes completed; interpret the scope of each separately.

### Medium identity and excluded namesake

identity: concern. Targets: CultureMech:007924.

TOGO M138 and the retained JCM 147 source identity match the bacterial CultureMech:007924 target and sole owner. The exact JCM page returns Nothing found. Fungal CultureMech:010507 has the same basename but a different stable ID and import provenance and is excluded; no ingredients or evidence are transferred from it.

### Single bacterial contributor and unchanged scientific fields

ownership: supported. Targets: CultureMech:007924.

The full merge provenance resolves only the bacterial owner. Both local layers retain the same scientific amounts, malformed solution identities and missing preparation; the generated merge metadata supplies no independent scientific evidence.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007924.

18 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Restore this distinct 900 ml water input; both layers instead combine 900 and 100 as 1000 G_PER_L. These are different preparation stages, not duplicate claims or an additional final-medium water dose."
  },
  {
    "decision_id": "q2",
    "ingredient": "Agar",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 20,\n          \"unit\": \"g\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Retain the printed batch grams within the named preparation. The local G_PER_L field loses stage/batch scope; neither source nor placeholder stocks establishes a measured final denominator."
  },
  {
    "decision_id": "q3",
    "ingredient": "Malt extract",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"Malt extract\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Retain the printed batch grams within the named preparation. The local G_PER_L field loses stage/batch scope; neither source nor placeholder stocks establishes a measured final denominator."
  },
  {
    "decision_id": "q4",
    "ingredient": "Peptone",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Peptone\",\n          \"volume\": 2.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Retain the printed batch grams within the named preparation. The local G_PER_L field loses stage/batch scope; neither source nor placeholder stocks establishes a measured final denominator."
  },
  {
    "decision_id": "q5",
    "ingredient": "NaOH dose",
    "decision": "not_quantified",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[0].comment (paragraph 3)",
        "exact_source_quote": "Adjust pH to 7.0 with 1 N NaOH.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "VARIABLE does not supply a dose. Retain the unquantified adjustment reagent; source stock strength is separately 1 N, not a final-medium normality."
  },
  {
    "decision_id": "q6",
    "ingredient": "NaOH stock strength",
    "decision": "add",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[4]",
        "stored": {
          "preferred_term": "NaOH",
          "notes": "Properties: Defined component, Inorganic compound, Solution",
          "term": {
            "id": "CHEBI:32145",
            "label": "sodium hydroxide"
          },
          "concentration": {
            "value": "variable",
            "unit": "VARIABLE"
          },
          "mediaingredientmech_chebi_term": {
            "id": "CHEBI:32145",
            "label": "sodium hydroxide"
          }
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[4]",
        "stored": {
          "preferred_term": "NaOH",
          "notes": "Properties: Defined component, Inorganic compound, Solution",
          "term": {
            "id": "CHEBI:32145",
            "label": "sodium hydroxide"
          },
          "concentration": {
            "value": "variable",
            "unit": "VARIABLE"
          },
          "mediaingredientmech_chebi_term": {
            "id": "CHEBI:32145",
            "label": "sodium hydroxide"
          }
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"N\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[0].comment (paragraph 3)",
        "exact_source_quote": "Adjust pH to 7.0 with 1 N NaOH.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Record the explicit 1 N stock strength at the A pH-adjustment stage without inventing an addition volume."
  },
  {
    "decision_id": "q7",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Restore this distinct 100 ml water input; both layers instead combine 900 and 100 as 1000 G_PER_L. These are different preparation stages, not duplicate claims or an additional final-medium water dose."
  },
  {
    "decision_id": "q8",
    "ingredient": "Na2CO3",
    "decision": "correct",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 6,\n          \"unit\": \"g\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Retain the printed batch grams within the named preparation. The local G_PER_L field loses stage/batch scope; neither source nor placeholder stocks establishes a measured final denominator."
  },
  {
    "decision_id": "q9",
    "ingredient": "Bicarbonate stock dose",
    "decision": "not_quantified",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"NaHCO3 solution\",\n          \"conc_value\": 6,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[1].comment (paragraph 5)",
        "exact_source_quote": "Adjust pH to 9.4 with 6% NaHCO3 solution.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "The existing VARIABLE stub has no numerical dose; do not calculate a final bicarbonate concentration."
  },
  {
    "decision_id": "q10",
    "ingredient": "Bicarbonate stock strength",
    "decision": "add",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"NaHCO3 solution\",\n          \"conc_value\": 6,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[1].comment (paragraph 5)",
        "exact_source_quote": "Adjust pH to 9.4 with 6% NaHCO3 solution.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Retain the printed 6% stock strength. The percentage basis is unspecified; do not convert it to w/v or infer a stock dose."
  },
  {
    "decision_id": "q11",
    "ingredient": "Solution A addition",
    "decision": "correct",
    "stage": "Assembly",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Restore the source liquid addition 900 ml rather than G_PER_L; represent the exact local stock, excluding unrelated MediaDive 5342/5343."
  },
  {
    "decision_id": "q12",
    "ingredient": "Solution B addition",
    "decision": "correct",
    "stage": "Assembly",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Restore the source liquid addition 100 ml rather than G_PER_L; represent the exact local stock, excluding unrelated MediaDive 5342/5343."
  },
  {
    "decision_id": "q13",
    "ingredient": "A target pH",
    "decision": "add",
    "stage": "Solution A before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[0].comment (paragraph 3)",
        "exact_source_quote": "Adjust pH to 7.0 with 1 N NaOH.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Add pH 7.0 for A and its 1 N NaOH adjustment. Do not assign this to the final mixed medium."
  },
  {
    "decision_id": "q14",
    "ingredient": "B target pH",
    "decision": "add",
    "stage": "Solution B before combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[1].comment (paragraph 5)",
        "exact_source_quote": "Adjust pH to 9.4 with 6% NaHCO3 solution.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Add pH 9.4 for B and its 6% bicarbonate adjustment. This is not an asserted final pH."
  },
  {
    "decision_id": "q15",
    "ingredient": "Separate autoclaving and aseptic mixing",
    "decision": "add",
    "stage": "A/B preparation and assembly",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[2].comment (paragraph 6)",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Retain the exact preparation order. No numerical cycle is supplied by the available provider."
  },
  {
    "decision_id": "q16",
    "ingredient": "Autoclave cycle",
    "decision": "not_quantified",
    "stage": "Separate A/B sterilization",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[2].comment (paragraph 6)",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "No temperature, time or pressure is stated. The empty JCM page does not authenticate a generic default."
  },
  {
    "decision_id": "q17",
    "ingredient": "Final pH",
    "decision": "not_quantified",
    "stage": "After A/B mixture",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[0].comment (paragraph 3)",
        "exact_source_quote": "Adjust pH to 7.0 with 1 N NaOH.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[1].comment (paragraph 5)",
        "exact_source_quote": "Adjust pH to 9.4 with 6% NaHCO3 solution.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.comments[2].comment (paragraph 6)",
        "exact_source_quote": "Autoclave Solutions A and B separately, and mix aseptically.",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "Neither pH 7.0 nor pH 9.4 describes the final mixture; do not infer a final value."
  },
  {
    "decision_id": "q18",
    "ingredient": "Measured final volume",
    "decision": "not_quantified",
    "stage": "After A/B mixture",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      },
      {
        "source_key": "togoM138original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77"
      }
    ],
    "interpretation": "The 900 and 100 ml solution additions imply a nominal assembly total, not a measured final volume after adjustment; do not silently normalize all source masses."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:007924.

4 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary and 4/6 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Chemical identifiers and mixture scope

grounding: supported. Targets: CultureMech:007924.

All four asserted primary/current secondary ingredient keys resolve with matching labels. Sodium hydroxide and carbonate agree with available provider identities; malt extract and peptone remain complex mixtures without invented molecular identifiers. Stock strength and preparation claims are independently limited by source availability.

### Missing stage-specific preparation

completeness: concern. Targets: CultureMech:007924.

Neither layer retains A pH 7.0, B pH 9.4, the 1 N hydroxide / 6% bicarbonate strengths or separate autoclaving and aseptic mixing. Percent basis, reagent doses, cycle and final pH remain unknown.

### Composition, physical state and growth

scope: supported. Targets: CultureMech:007924.

COMPLEX/UNDEFINED and SOLID_AGAR agree with malt extract, peptone and required agar in the provider. The bacterial source identity does not justify transferring a fungal namesake or asserting an organism-specific growth observation.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007924.

25 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Secondary evidence versus inaccessible primary

evidence: concern. Targets: CultureMech:007924.

No local quantity or preparation claim has attached evidence. TOGO supports a bounded secondary-source assessment; JCM 147 primary authentication remains unavailable and is not replaced by the fungal namesake or generic defaults.

## Findings

### f1: Unrelated high-salt stocks replace the source A/B identities

blocker / open / confirmed; issue key: wrong-stock-identities.

MediaDive 5342 and 5343 have incompatible formulas. Both layers attach these IDs solely alongside generic solution names; the actual provider defines local A/B preparations.

### f2: Liquid additions and water are represented as mass concentrations

major / open / confirmed; issue key: liquid-and-batch-scope.

Water 900/100 ml is flattened to 1000 G_PER_L and solution additions 900/100 ml become G_PER_L. The constituent batch masses lose their A/B stage scope.

### f3: Source adjustment strengths and separate pH stages are missing

major / open / confirmed; issue key: missing-adjustment-and-preparation.

The available provider specifies A pH 7.0 with 1 N NaOH and B pH 9.4 with 6% bicarbonate, plus separate autoclaving and aseptic mixing. Both layers omit these distinctions.

### f4: Exact primary is unavailable and claims have no attached evidence

major / open / confirmed; issue key: primary-and-claim-evidence.

JCM 147 returns HTTP 200 with Nothing found. Three current provider statements and component objects remain secondary support; no ingredient or preparation evidence is attached locally.

## Recommended Actions And Acceptance Checks

### a1

Resolve source-local stock identity and composition before curating links; remove unsupported correspondence without transferring unrelated ingredients or preparation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore exact liquid units, distinct preparation membership and batch amounts in the owner after primary resolution; retain unknown final volume.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve exact stage-specific preparation with evidence, leaving percentage basis, doses, cycle and final pH unspecified.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Recover the exact primary version if available and attach literal claim-level evidence. Preserve unavailable-check status until resolved; do not use HTTP status alone as content availability.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch035/350/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/350/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml:1:id: CultureMech:007924<br>./data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml:1:id: CultureMech:007924<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/350/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 18 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138; $.meta and complete $.components / $.comments | supports | Exact current secondary source identifies JCM 147 and preserves the distinct A/B preparation recipes. It does not substitute for unavailable primary authentication. |
| preparation-0 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138; $.comments[0].comment | supports | Exact source-scoped preparation text. |
| preparation-1 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138; $.comments[1].comment | supports | Exact source-scoped preparation text. |
| preparation-2 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138; $.comments[2].comment | supports | Exact source-scoped preparation text. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch035/350/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| solution5342 | https://mediadive.dsmz.de/rest/solution/5342; $.data.id, recipe and steps | refutes | The asserted accession is a different high-salt stock: 5342 includes 100 g NaCl and incompatible nutrients; 5343 includes 80 g carbonate and 100 g NaCl. These are comparison evidence only. |
| solution5342-local | data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml; Complete pinned stock record | context_only | The local cross-reference resolves to the same incompatible stock family, not the TOGO M138 A/B preparation. |
| solution5343 | https://mediadive.dsmz.de/rest/solution/5343; $.data.id, recipe and steps | refutes | The asserted accession is a different high-salt stock: 5342 includes 100 g NaCl and incompatible nutrients; 5343 includes 80 g carbonate and 100 g NaCl. These are comparison evidence only. |
| solution5343-local | data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml; Complete pinned stock record | context_only | The local cross-reference resolves to the same incompatible stock family, not the TOGO M138 A/B preparation. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32145 resolves to sodium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145": [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145", "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml; data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml", "events": 12, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes solution references and adjustment strengths, the legacy solution migrator resolves generic names, and cleanup combines duplicate ingredients. These current functions and recorded history do not prove a historical execution path or source equivalence. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes solution references and adjustment strengths, the legacy solution migrator resolves generic names, and cleanup combines duplicate ingredients. These current functions and recorded history do not prove a historical execution path or source equivalence. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes solution references and adjustment strengths, the legacy solution migrator resolves generic names, and cleanup combines duplicate ingredients. These current functions and recorded history do not prove a historical execution path or source equivalence. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer distinguishes solution references and adjustment strengths, the legacy solution migrator resolves generic names, and cleanup combines duplicate ingredients. These current functions and recorded history do not prove a historical execution path or source equivalence. |
| jcm147-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=147; Preserved exact public retrieval result | context_only | The exact JCM 147 request returned HTTP 200 Nothing found, with no usable recipe or default sterilization instruction. Required original-source verification remains unavailable; this review is partial. |
| mediadiveJ147-attempt | https://mediadive.dsmz.de/rest/medium/J147; Preserved exact public retrieval result | context_only | Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content. |
| mediadiveJ147Retry1-attempt | https://mediadive.dsmz.de/rest/medium/J147; Preserved exact public retrieval result | context_only | Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content. |
| togoM138-attempt | https://mediumapi.dbcls.jp/medium/M138; Preserved exact public retrieval result | context_only | Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact JCM 147 request returned HTTP 200 Nothing found, with no usable recipe or default sterilization instruction. Required original-source verification remains unavailable; this review is partial.
- Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content.
- Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content.
- Preserved optional alternate-source request failure. The separately captured original TOGO endpoint is usable, but does not authenticate missing JCM primary content.
- The fungal namesake and unrelated 5342/5343 stocks are excluded from formulation transfer. No experimental growth, percentage basis, final pH, final measured volume or sterilization cycle is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191839Z-culturemech-007924-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaline_malt_extract_agar (CultureMech:007924)'
started_at: '2026-10-21T19:13:57Z'
finished_at: '2026-10-21T19:18:39Z'
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
summary: TOGO M138 identifies the bacterial JCM 147 record, but the exact primary
  returns Nothing found. The two layers have incorrect stock identities, water/solution
  units and lost preparation stages; the review remains partial for primary-source
  verification.
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
  - path: data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
    sha256: c21b3c9aaf44a7a2243665ff7f039d32ae8a13af2a8eda43bcd5d9223222d8c2
    role: target
  - path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
    sha256: c64dc567f8fe4303849277526de90dda46c23b5f073574ec0e1865d948a27811
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
    role: context
  - path: data/normalized_yaml/fungal/alkaline_malt_extract_agar.yaml
    sha256: b86d2e41065e75a0723f137749ffaa75a8f21533033292d13bb6e3ba82aae4cf
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
  selection: Task review 350; batch 035 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-four task batches
    contain 340 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 343 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007924
targets:
- target_id: CultureMech:007924
  path: data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  label: alkaline_malt_extract_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/350/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/350/strict.tsv"
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007924
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
  - CultureMech:007924
- check_id: jcm147-source-access
  name: 'Exact source content access: jcm147'
  required: true
  status: unavailable
  summary: The exact JCM 147 request returned HTTP 200 Nothing found, with no usable
    recipe or default sterilization instruction. Required original-source verification
    remains unavailable; this review is partial.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - jcm147-attempt
- check_id: mediadiveJ147-source-access
  name: 'Exact source content access: mediadiveJ147'
  required: false
  status: unavailable
  summary: Preserved optional alternate-source request failure. The separately captured
    original TOGO endpoint is usable, but does not authenticate missing JCM primary
    content.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - mediadiveJ147-attempt
- check_id: mediadiveJ147Retry1-source-access
  name: 'Exact source content access: mediadiveJ147Retry1'
  required: false
  status: unavailable
  summary: Preserved optional alternate-source request failure. The separately captured
    original TOGO endpoint is usable, but does not authenticate missing JCM primary
    content.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - mediadiveJ147Retry1-attempt
- check_id: togoM138-source-access
  name: 'Exact source content access: togoM138'
  required: false
  status: unavailable
  summary: Preserved optional alternate-source request failure. The separately captured
    original TOGO endpoint is usable, but does not authenticate missing JCM primary
    content.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - togoM138-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:50.541195Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch035/350/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:51.757965Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/350/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:53.113391Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:53.963653Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:18:38Z'
  support: supports
  summary: './data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml:1:id: CultureMech:007924

    ./data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml:1:id: CultureMech:007924

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/350/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:18:38Z'
  support: supports
  summary: 18 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 5ca451b8e4b006aa4ca99e9eb9e2808abb706601bd6fe5ba449415ab7172d265
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138
  locator: $.meta and complete $.components / $.comments
  accessed_at: '2026-10-21T19:02:23.875311Z'
  support: supports
  summary: Exact current secondary source identifies JCM 147 and preserves the distinct
    A/B preparation recipes. It does not substitute for unavailable primary authentication.
  quote: '"original_media_id": "JCM_M147"'
  snapshot_sha256: 200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77
- evidence_id: preparation-0
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138
  locator: $.comments[0].comment
  accessed_at: '2026-10-21T19:02:23.875311Z'
  support: supports
  summary: Exact source-scoped preparation text.
  quote: Adjust pH to 7.0 with 1 N NaOH.
  snapshot_sha256: 200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77
- evidence_id: preparation-1
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138
  locator: $.comments[1].comment
  accessed_at: '2026-10-21T19:02:23.875311Z'
  support: supports
  summary: Exact source-scoped preparation text.
  quote: Adjust pH to 9.4 with 6% NaHCO3 solution.
  snapshot_sha256: 200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77
- evidence_id: preparation-2
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138
  locator: $.comments[2].comment
  accessed_at: '2026-10-21T19:02:23.875311Z'
  support: supports
  summary: Exact source-scoped preparation text.
  quote: Autoclave Solutions A and B separately, and mix aseptically.
  snapshot_sha256: 200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/350/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 6c6174a7dc0df8e1fb9738d377797875d3b7bc36ed141dab7ebbf7ec6c9130e6
- evidence_id: solution5342
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: $.data.id, recipe and steps
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: refutes
  summary: 'The asserted accession is a different high-salt stock: 5342 includes 100
    g NaCl and incompatible nutrients; 5343 includes 80 g carbonate and 100 g NaCl.
    These are comparison evidence only.'
  quote: "{\n    \"status\": 200,\n    \"count\": 1,\n    \"data\": {\n        \"\
    id\": 5342,\n        \"name\": \"Solution A\",\n        \"volume\": null,\n  \
    \      \"recipe\": [\n            {\n                \"recipe_order\": 1,\n  \
    \              \"compound\": \"Yeast extract\",\n                \"compound_id\"\
    : 16,\n                \"solution\": null,\n                \"solution_id\": null,\n\
    \                \"condition\": null,\n                \"attribute\": \"BD-Difco\"\
    ,\n                \"amount\": 2,\n                \"unit\": \"g\",\n        \
    \        \"g_l\": null,\n                \"mmol_l\": null,\n                \"\
    optional\": 0\n            },\n            {\n                \"recipe_order\"\
    : 2,\n                \"compound\": \"Casamino acids\",\n                \"compound_id\"\
    : 101,\n                \"solution\": null,\n                \"solution_id\":\
    \ null,\n                \"condition\": null,\n                \"attribute\":\
    \ \"BD-Difco\",\n                \"amount\": 2,\n                \"unit\": \"\
    g\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n    \
    \            \"optional\": 0\n            },\n            {\n                \"\
    recipe_order\": 3,\n                \"compound\": \"Na glutamate\",\n        \
    \        \"compound_id\": 839,\n                \"solution\": null,\n        \
    \        \"solution_id\": null,\n                \"condition\": null,\n      \
    \          \"attribute\": null,\n                \"amount\": 1,\n            \
    \    \"unit\": \"g\",\n                \"g_l\": null,\n                \"mmol_l\"\
    : null,\n                \"optional\": 0\n            },\n            {\n    \
    \            \"recipe_order\": 4,\n                \"compound\": \"Trisodium citrate\
    \ x 2 H2O\",\n                \"compound_id\": 1249,\n                \"solution\"\
    : null,\n                \"solution_id\": null,\n                \"condition\"\
    : null,\n                \"attribute\": null,\n                \"amount\": 3,\n\
    \                \"unit\": \"g\",\n                \"g_l\": null,\n          \
    \      \"mmol_l\": null,\n                \"optional\": 0\n            },\n  \
    \          {\n                \"recipe_order\": 5,\n                \"compound\"\
    : \"MgSO4 x 7 H2O\",\n                \"compound_id\": 8,\n                \"\
    solution\": null,\n                \"solution_id\": null,\n                \"\
    condition\": null,\n                \"attribute\": null,\n                \"amount\"\
    : 0.1,\n                \"unit\": \"g\",\n                \"g_l\": null,\n   \
    \             \"mmol_l\": null,\n                \"optional\": 0\n           \
    \ },\n            {\n                \"recipe_order\": 6,\n                \"\
    compound\": \"CaSO4 x 2 H2O\",\n                \"compound_id\": 190,\n      \
    \          \"solution\": null,\n                \"solution_id\": null,\n     \
    \           \"condition\": null,\n                \"attribute\": null,\n     \
    \           \"amount\": 0.1,\n                \"unit\": \"g\",\n             \
    \   \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\"\
    : 0\n            },\n            {\n                \"recipe_order\": 7,\n   \
    \             \"compound\": \"KCl\",\n                \"compound_id\": 61,\n \
    \               \"solution\": null,\n                \"solution_id\": null,\n\
    \                \"condition\": null,\n                \"attribute\": null,\n\
    \                \"amount\": 1,\n                \"unit\": \"g\",\n          \
    \      \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\"\
    : 0\n            },\n            {\n                \"recipe_order\": 8,\n   \
    \             \"compound\": \"NaCl\",\n                \"compound_id\": 43,\n\
    \                \"solution\": null,\n                \"solution_id\": null,\n\
    \                \"condition\": null,\n                \"attribute\": null,\n\
    \                \"amount\": 100,\n                \"unit\": \"g\",\n        \
    \        \"g_l\": null,\n                \"mmol_l\": null,\n                \"\
    optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n\
    \                \"recipe_order\": null,\n                \"step\": \"Add components\
    \ to distilled water and bring volume to 500 ml.\"\n            }\n        ],\n\
    \        \"equipment\": []\n    }\n}"
  snapshot_sha256: 4bf262e02d0a83f9d1a24a52d2a14383aa8c6f27384e446d7da6274a05319240
- evidence_id: solution5342-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
  locator: Complete pinned stock record
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: The local cross-reference resolves to the same incompatible stock family,
    not the TOGO M138 A/B preparation.
  snapshot_sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
- evidence_id: solution5343
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: $.data.id, recipe and steps
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: refutes
  summary: 'The asserted accession is a different high-salt stock: 5342 includes 100
    g NaCl and incompatible nutrients; 5343 includes 80 g carbonate and 100 g NaCl.
    These are comparison evidence only.'
  quote: "{\n    \"status\": 200,\n    \"count\": 1,\n    \"data\": {\n        \"\
    id\": 5343,\n        \"name\": \"Solution B\",\n        \"volume\": null,\n  \
    \      \"recipe\": [\n            {\n                \"recipe_order\": 1,\n  \
    \              \"compound\": \"Na2CO3\",\n                \"compound_id\": 32,\n\
    \                \"solution\": null,\n                \"solution_id\": null,\n\
    \                \"condition\": null,\n                \"attribute\": null,\n\
    \                \"amount\": 80,\n                \"unit\": \"g\",\n         \
    \       \"g_l\": null,\n                \"mmol_l\": null,\n                \"\
    optional\": 0\n            },\n            {\n                \"recipe_order\"\
    : 2,\n                \"compound\": \"NaCl\",\n                \"compound_id\"\
    : 43,\n                \"solution\": null,\n                \"solution_id\": null,\n\
    \                \"condition\": null,\n                \"attribute\": null,\n\
    \                \"amount\": 100,\n                \"unit\": \"g\",\n        \
    \        \"g_l\": null,\n                \"mmol_l\": null,\n                \"\
    optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n\
    \                \"recipe_order\": null,\n                \"step\": \"Add components\
    \ to distilled water and bring volume to 500 ml.\"\n            },\n         \
    \   {\n                \"recipe_order\": null,\n                \"step\": \"Autoclave\
    \ solutions A and B separately and combine them after cooling. For preparation\
    \ of solid medium, add 18.0 g agar to Solution A (500 ml), combine them after\
    \ cooling to 60-70C, mix well and quickly distribute into sterile petri dishes\
    \ or test tubes.\"\n            }\n        ],\n        \"equipment\": {\n    \
    \        \"309\": \"Autoclave\"\n        }\n    }\n}"
  snapshot_sha256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- evidence_id: solution5343-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
  locator: Complete pinned stock record
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: The local cross-reference resolves to the same incompatible stock family,
    not the TOGO M138 A/B preparation.
  snapshot_sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T19:18:38Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377":
    [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32145":
    [{"label": "NaOH", "match_type": "preferred_term", "identifier": "CHEBI:32145",
    "preferred_term": "NaOH", "ontology_id": "CHEBI:32145", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml; data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml", "events": 12,
    "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Current importer distinguishes solution references and adjustment strengths,
    the legacy solution migrator resolves generic names, and cleanup combines duplicate
    ingredients. These current functions and recorded history do not prove a historical
    execution path or source equivalence.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Current importer distinguishes solution references and adjustment strengths,
    the legacy solution migrator resolves generic names, and cleanup combines duplicate
    ingredients. These current functions and recorded history do not prove a historical
    execution path or source equivalence.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Current importer distinguishes solution references and adjustment strengths,
    the legacy solution migrator resolves generic names, and cleanup combines duplicate
    ingredients. These current functions and recorded history do not prove a historical
    execution path or source equivalence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:18:38Z'
  support: context_only
  summary: Current importer distinguishes solution references and adjustment strengths,
    the legacy solution migrator resolves generic names, and cleanup combines duplicate
    ingredients. These current functions and recorded history do not prove a historical
    execution path or source equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: jcm147-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=147
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:25.141868Z'
  support: context_only
  summary: The exact JCM 147 request returned HTTP 200 Nothing found, with no usable
    recipe or default sterilization instruction. Required original-source verification
    remains unavailable; this review is partial.
  snapshot_sha256: 1fd396127179a4a8c537b5db1ed59966aec0e3c0ccbe64fb37d556a6149da03e
- evidence_id: mediadiveJ147-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J147
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:22.563460Z'
  support: context_only
  summary: Preserved optional alternate-source request failure. The separately captured
    original TOGO endpoint is usable, but does not authenticate missing JCM primary
    content.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ147Retry1-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J147
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:03:33.023572Z'
  support: context_only
  summary: Preserved optional alternate-source request failure. The separately captured
    original TOGO endpoint is usable, but does not authenticate missing JCM primary
    content.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: togoM138-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M138
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:23.205842Z'
  support: context_only
  summary: Preserved optional alternate-source request failure. The separately captured
    original TOGO endpoint is usable, but does not authenticate missing JCM primary
    content.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Medium identity and excluded namesake
  outcome: concern
  summary: TOGO M138 and the retained JCM 147 source identity match the bacterial
    CultureMech:007924 target and sole owner. The exact JCM page returns Nothing found.
    Fungal CultureMech:010507 has the same basename but a different stable ID and
    import provenance and is excluded; no ingredients or evidence are transferred
    from it.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - owner-0
  - provider
  - id-search
- assessment_id: ownership
  area: ownership
  topic: Single bacterial contributor and unchanged scientific fields
  outcome: supported
  summary: The full merge provenance resolves only the bacterial owner. Both local
    layers retain the same scientific amounts, malformed solution identities and missing
    preparation; the generated merge metadata supplies no independent scientific evidence.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - owner-0
  - id-search
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 18 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"Distilled\
    \ water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\n      }\n\
    \    ],\n    \"interpretation\": \"Restore this distinct 900 ml water input; both\
    \ layers instead combine 900 and 100 as 1000 G_PER_L. These are different preparation\
    \ stages, not duplicate claims or an additional final-medium water dose.\"\n \
    \ },\n  {\n    \"decision_id\": \"q2\",\n    \"ingredient\": \"Agar\",\n    \"\
    decision\": \"correct\",\n    \"stage\": \"Solution A preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 20,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch grams within\
    \ the named preparation. The local G_PER_L field loses stage/batch scope; neither\
    \ source nor placeholder stocks establishes a measured final denominator.\"\n\
    \  },\n  {\n    \"decision_id\": \"q3\",\n    \"ingredient\": \"Malt extract\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Malt extract\\\",\\n          \\\"volume\\\":\
    \ 10,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\n      }\n\
    \    ],\n    \"interpretation\": \"Retain the printed batch grams within the named\
    \ preparation. The local G_PER_L field loses stage/batch scope; neither source\
    \ nor placeholder stocks establishes a measured final denominator.\"\n  },\n \
    \ {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"Peptone\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Solution A preparation\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Peptone\\\",\\n          \\\"volume\\\": 2.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch grams within\
    \ the named preparation. The local G_PER_L field loses stage/batch scope; neither\
    \ source nor placeholder stocks establishes a measured final denominator.\"\n\
    \  },\n  {\n    \"decision_id\": \"q5\",\n    \"ingredient\": \"NaOH dose\",\n\
    \    \"decision\": \"not_quantified\",\n    \"stage\": \"Solution A preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      },\n      {\n        \"source_key\": \"togoM138original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[0].comment (paragraph 3)\",\n    \
    \    \"exact_source_quote\": \"Adjust pH to 7.0 with 1 N NaOH.\",\n        \"\
    snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"VARIABLE does not supply a dose.\
    \ Retain the unquantified adjustment reagent; source stock strength is separately\
    \ 1 N, not a final-medium normality.\"\n  },\n  {\n    \"decision_id\": \"q6\"\
    ,\n    \"ingredient\": \"NaOH stock strength\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"Solution A preparation\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4]\",\n        \"stored\": {\n      \
    \    \"preferred_term\": \"NaOH\",\n          \"notes\": \"Properties: Defined\
    \ component, Inorganic compound, Solution\",\n          \"term\": {\n        \
    \    \"id\": \"CHEBI:32145\",\n            \"label\": \"sodium hydroxide\"\n \
    \         },\n          \"concentration\": {\n            \"value\": \"variable\"\
    ,\n            \"unit\": \"VARIABLE\"\n          },\n          \"mediaingredientmech_chebi_term\"\
    : {\n            \"id\": \"CHEBI:32145\",\n            \"label\": \"sodium hydroxide\"\
    \n          }\n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4]\",\n        \"stored\": {\n      \
    \    \"preferred_term\": \"NaOH\",\n          \"notes\": \"Properties: Defined\
    \ component, Inorganic compound, Solution\",\n          \"term\": {\n        \
    \    \"id\": \"CHEBI:32145\",\n            \"label\": \"sodium hydroxide\"\n \
    \         },\n          \"concentration\": {\n            \"value\": \"variable\"\
    ,\n            \"unit\": \"VARIABLE\"\n          },\n          \"mediaingredientmech_chebi_term\"\
    : {\n            \"id\": \"CHEBI:32145\",\n            \"label\": \"sodium hydroxide\"\
    \n          }\n        }\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"N\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      },\n      {\n        \"source_key\": \"togoM138original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[0].comment (paragraph 3)\",\n    \
    \    \"exact_source_quote\": \"Adjust pH to 7.0 with 1 N NaOH.\",\n        \"\
    snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Record the explicit 1 N stock strength\
    \ at the A pH-adjustment stage without inventing an addition volume.\"\n  },\n\
    \  {\n    \"decision_id\": \"q7\",\n    \"ingredient\": \"Distilled water\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Solution B preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\n      }\n\
    \    ],\n    \"interpretation\": \"Restore this distinct 100 ml water input; both\
    \ layers instead combine 900 and 100 as 1000 G_PER_L. These are different preparation\
    \ stages, not duplicate claims or an additional final-medium water dose.\"\n \
    \ },\n  {\n    \"decision_id\": \"q8\",\n    \"ingredient\": \"Na2CO3\",\n   \
    \ \"decision\": \"correct\",\n    \"stage\": \"Solution B preparation\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 6,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed batch grams within\
    \ the named preparation. The local G_PER_L field loses stage/batch scope; neither\
    \ source nor placeholder stocks establishes a measured final denominator.\"\n\
    \  },\n  {\n    \"decision_id\": \"q9\",\n    \"ingredient\": \"Bicarbonate stock\
    \ dose\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"Solution B\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3 solution\\\",\\n          \\\"conc_value\\\
    \": 6,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM138original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\",\n \
    \       \"source_locator\": \"$.comments[1].comment (paragraph 5)\",\n       \
    \ \"exact_source_quote\": \"Adjust pH to 9.4 with 6% NaHCO3 solution.\",\n   \
    \     \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"The existing VARIABLE stub has no\
    \ numerical dose; do not calculate a final bicarbonate concentration.\"\n  },\n\
    \  {\n    \"decision_id\": \"q10\",\n    \"ingredient\": \"Bicarbonate stock strength\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Solution B preparation\",\n  \
    \  \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3 solution\\\",\\n          \\\"conc_value\\\
    \": 6,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM138original\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\",\n \
    \       \"source_locator\": \"$.comments[1].comment (paragraph 5)\",\n       \
    \ \"exact_source_quote\": \"Adjust pH to 9.4 with 6% NaHCO3 solution.\",\n   \
    \     \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the printed 6% stock strength.\
    \ The percentage basis is unspecified; do not convert it to w/v or infer a stock\
    \ dose.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"ingredient\": \"Solution\
    \ A addition\",\n    \"decision\": \"correct\",\n    \"stage\": \"Assembly\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 900,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the source liquid addition\
    \ 900 ml rather than G_PER_L; represent the exact local stock, excluding unrelated\
    \ MediaDive 5342/5343.\"\n  },\n  {\n    \"decision_id\": \"q12\",\n    \"ingredient\"\
    : \"Solution B addition\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Assembly\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Restore the source liquid addition\
    \ 100 ml rather than G_PER_L; represent the exact local stock, excluding unrelated\
    \ MediaDive 5342/5343.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"ingredient\"\
    : \"A target pH\",\n    \"decision\": \"add\",\n    \"stage\": \"Solution A before\
    \ combination\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[0].comment (paragraph 3)\",\n    \
    \    \"exact_source_quote\": \"Adjust pH to 7.0 with 1 N NaOH.\",\n        \"\
    snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Add pH 7.0 for A and its 1 N NaOH\
    \ adjustment. Do not assign this to the final mixed medium.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q14\",\n    \"ingredient\": \"B target pH\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"Solution B before combination\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[1].comment (paragraph 5)\",\n    \
    \    \"exact_source_quote\": \"Adjust pH to 9.4 with 6% NaHCO3 solution.\",\n\
    \        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Add pH 9.4 for B and its 6% bicarbonate\
    \ adjustment. This is not an asserted final pH.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"ingredient\": \"Separate autoclaving and aseptic mixing\",\n\
    \    \"decision\": \"add\",\n    \"stage\": \"A/B preparation and assembly\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[2].comment (paragraph 6)\",\n    \
    \    \"exact_source_quote\": \"Autoclave Solutions A and B separately, and mix\
    \ aseptically.\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Retain the exact preparation order.\
    \ No numerical cycle is supplied by the available provider.\"\n  },\n  {\n   \
    \ \"decision_id\": \"q16\",\n    \"ingredient\": \"Autoclave cycle\",\n    \"\
    decision\": \"not_quantified\",\n    \"stage\": \"Separate A/B sterilization\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[2].comment (paragraph 6)\",\n    \
    \    \"exact_source_quote\": \"Autoclave Solutions A and B separately, and mix\
    \ aseptically.\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"No temperature, time or pressure\
    \ is stated. The empty JCM page does not authenticate a generic default.\"\n \
    \ },\n  {\n    \"decision_id\": \"q17\",\n    \"ingredient\": \"Final pH\",\n\
    \    \"decision\": \"not_quantified\",\n    \"stage\": \"After A/B mixture\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM138original\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[0].comment (paragraph 3)\",\n    \
    \    \"exact_source_quote\": \"Adjust pH to 7.0 with 1 N NaOH.\",\n        \"\
    snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      },\n      {\n        \"source_key\": \"togoM138original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[1].comment (paragraph 5)\",\n    \
    \    \"exact_source_quote\": \"Adjust pH to 9.4 with 6% NaHCO3 solution.\",\n\
    \        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      },\n      {\n        \"source_key\": \"togoM138original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.comments[2].comment (paragraph 6)\",\n    \
    \    \"exact_source_quote\": \"Autoclave Solutions A and B separately, and mix\
    \ aseptically.\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"Neither pH 7.0 nor pH 9.4 describes\
    \ the final mixture; do not infer a final value.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"ingredient\": \"Measured final volume\",\n    \"decision\":\
    \ \"not_quantified\",\n    \"stage\": \"After A/B mixture\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkaline_Malt_Extract_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM138original\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A\\\",\\n          \\\"volume\\\": 900,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      },\n      {\n        \"source_key\": \"togoM138original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M138\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"200d19c48b85fa3533e0f743f54bd50d8a0593a59401a0b14765803087199f77\"\
    \n      }\n    ],\n    \"interpretation\": \"The 900 and 100 ml solution additions\
    \ imply a nominal assembly total, not a measured final volume after adjustment;\
    \ do not silently normalize all source masses.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '4 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary
    and 4/6 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi2509
  - chebi29377
  - chebi32145
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Chemical identifiers and mixture scope
  outcome: supported
  summary: All four asserted primary/current secondary ingredient keys resolve with
    matching labels. Sodium hydroxide and carbonate agree with available provider
    identities; malt extract and peptone remain complex mixtures without invented
    molecular identifiers. Stock strength and preparation claims are independently
    limited by source availability.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - provider
  - chebi32145
  - chebi29377
  - mim
- assessment_id: preparation
  area: completeness
  topic: Missing stage-specific preparation
  outcome: concern
  summary: Neither layer retains A pH 7.0, B pH 9.4, the 1 N hydroxide / 6% bicarbonate
    strengths or separate autoclaving and aseptic mixing. Percent basis, reagent doses,
    cycle and final pH remain unknown.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - preparation-0
  - preparation-1
  - preparation-2
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Composition, physical state and growth
  outcome: supported
  summary: COMPLEX/UNDEFINED and SOLID_AGAR agree with malt extract, peptone and required
    agar in the provider. The bacterial source identity does not justify transferring
    a fungal namesake or asserting an organism-specific growth observation.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - provider
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 25 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: provenance
  area: evidence
  topic: Secondary evidence versus inaccessible primary
  outcome: concern
  summary: No local quantity or preparation claim has attached evidence. TOGO supports
    a bounded secondary-source assessment; JCM 147 primary authentication remains
    unavailable and is not replaced by the fungal namesake or generic defaults.
  target_ids:
  - CultureMech:007924
  evidence_ids:
  - record
  - owner-0
  - provider
findings:
- finding_id: f1
  issue_key: wrong-stock-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Unrelated high-salt stocks replace the source A/B identities
  description: MediaDive 5342 and 5343 have incompatible formulas. Both layers attach
    these IDs solely alongside generic solution names; the actual provider defines
    local A/B preparations.
  target_ids:
  - CultureMech:007924
  field_paths:
  - solutions[0].term
  - solutions[1].term
  evidence_ids:
  - provider
  - solution5342
  - solution5343
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  issue_key: liquid-and-batch-scope
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid additions and water are represented as mass concentrations
  description: Water 900/100 ml is flattened to 1000 G_PER_L and solution additions
    900/100 ml become G_PER_L. The constituent batch masses lose their A/B stage scope.
  target_ids:
  - CultureMech:007924
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  issue_key: missing-adjustment-and-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source adjustment strengths and separate pH stages are missing
  description: The available provider specifies A pH 7.0 with 1 N NaOH and B pH 9.4
    with 6% bicarbonate, plus separate autoclaving and aseptic mixing. Both layers
    omit these distinctions.
  target_ids:
  - CultureMech:007924
  field_paths:
  - preparation_steps
  - solutions[2]
  - ingredients[4]
  evidence_ids:
  - preparation-0
  - preparation-1
  - preparation-2
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  issue_key: primary-and-claim-evidence
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Exact primary is unavailable and claims have no attached evidence
  description: JCM 147 returns HTTP 200 with Nothing found. Three current provider
    statements and component objects remain secondary support; no ingredient or preparation
    evidence is attached locally.
  target_ids:
  - CultureMech:007924
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  - notes
  evidence_ids:
  - record
  - owner-0
  - provider
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  description: Resolve source-local stock identity and composition before curating
    links; remove unsupported correspondence without transferring unrelated ingredients
    or preparation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007924
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  description: Restore exact liquid units, distinct preparation membership and batch
    amounts in the owner after primary resolution; retain unknown final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007924
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  description: Preserve exact stage-specific preparation with evidence, leaving percentage
    basis, doses, cycle and final pH unspecified.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007924
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
  description: Recover the exact primary version if available and attach literal claim-level
    evidence. Preserve unavailable-check status until resolved; do not use HTTP status
    alone as content availability.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007924
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkaline_malt_extract_agar.yaml
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
- The exact JCM 147 request returned HTTP 200 Nothing found, with no usable recipe
  or default sterilization instruction. Required original-source verification remains
  unavailable; this review is partial.
- Preserved optional alternate-source request failure. The separately captured original
  TOGO endpoint is usable, but does not authenticate missing JCM primary content.
- Preserved optional alternate-source request failure. The separately captured original
  TOGO endpoint is usable, but does not authenticate missing JCM primary content.
- Preserved optional alternate-source request failure. The separately captured original
  TOGO endpoint is usable, but does not authenticate missing JCM primary content.
- The fungal namesake and unrelated 5342/5343 stocks are excluded from formulation
  transfer. No experimental growth, percentage basis, final pH, final measured volume
  or sterilization cycle is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-035
- generated-medium
```
