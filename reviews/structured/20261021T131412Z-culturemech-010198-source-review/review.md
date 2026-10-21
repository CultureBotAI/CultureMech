# Source and formulation review: alkaline_tryptone_soya_broth_medium (CultureMech:010198)

- Review: 20261021T131412Z-culturemech-010198-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:04:54Z
- Finished UTC: 2026-10-21T13:14:12Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated target retains a water mass-unit error and an empty carbonate stock, while its maintained owner already restores water volume, pH range and preparation. The secondary sources support these improvements but only an unqualified 20% stock; the owner adds an unsupported w/v basis. Exact JCM 763 formulation content is unavailable, so the review remains partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 213; batch 022 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-one task batches contain 210 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 213 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010198 | data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml | generated | alkaline_tryptone_soya_broth_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010198 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010198 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/213/strict.tsv |
| validate-terms | passed | True | CultureMech:010198 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010198 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010198 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm763 | unavailable | True | CultureMech:010198 | The exact collection request for JCM 763 returned HTTP 200 with Nothing found, not recipe content. Primary formulation, percent basis and any collection-specific defaults therefore remain unavailable. Secondary transcriptions remain usable with their source scope; no JCM default cycle is imported. |
| Exact source content access: togoM789page | unavailable | False | CultureMech:010198 | The TOGO M789 HTML page capture contains only its application shell. The exact M789 API payload is available and independently inspected, so this optional page-rendering limit does not remove the secondary formulation evidence. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010198.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010198.

14 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "Generated water quantity",
    "decision": "correct",
    "stage": "Liquid main recipe, provider-declared 1000 mL basis",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "1 L source water; provider 1000 mL",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The target stores 1 G_PER_L, a mass-unit conversion error. Retain the source volume and main-recipe basis; no density conversion or measured post-adjustment final volume is inferred."
  },
  {
    "decision_id": "q2",
    "claim": "Maintained water quantity and repeated preparation claim",
    "decision": "evidence_only",
    "stage": "Liquid main recipe before variable stock adjustment",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "ML_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "ingredients[0].notes",
        "stored": "TOGO M789 / JCM Medium 763 contributes 1000.0 ml/L distilled water."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L water."
      }
    ],
    "source_amount": "1000 mL on the declared 1000 mL main basis",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The maintained owner already corrects the target unit to ML_PER_L and states the same volume in preparation. It has source prose but no attached amount evidence. The later variable carbonate addition does not establish a measured final volume."
  },
  {
    "decision_id": "q3",
    "claim": "Commercial broth amount in both layers",
    "decision": "evidence_only",
    "stage": "Liquid main medium; intact commercial mixture",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "30.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "ingredients[1].notes",
        "stored": "TOGO M789 / JCM Medium 763 lists 30.0 g/L Oxoid Tryptone soya broth."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Dissolve 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L water."
      }
    ],
    "source_amount": "30 g source batch; provider explicitly 30 g/L",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Tryptone soya broth (Oxoid)\",\n          \"volume\": 30,\n          \"unit\": \"g\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Trypticase soy broth\",\n                        \"compound_id\": 99,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "Both layers retain the correct amount; none has attached claim-level evidence. Provider g_l supplies the declared basis. Preserve the Oxoid mixture identity without decomposing it into guessed constituents or substituting a generic product."
  },
  {
    "decision_id": "q4",
    "claim": "Variable carbonate addition",
    "decision": "not_quantified",
    "stage": "After basal sterilization and cooling, adjust to source pH range",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": "No fixed stock volume or final carbonate amount supplied",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"sodium carbonate solution\",\n          \"conc_value\": 20,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "Both layers correctly retain VARIABLE for the pH-adjusting dose. The 20% is a stock-strength statement, not the dose or final-medium concentration. Do not infer a volume, dilution or final carbonate mass."
  },
  {
    "decision_id": "q5",
    "claim": "Missing target stock-strength context",
    "decision": "add",
    "stage": "Separate pH-adjusting stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "solutions[0].name",
        "stored": "Unknown solution"
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "solutions[0].notes",
        "stored": "Role: Buffer; Properties: Defined component, Inorganic compound, Solution"
      }
    ],
    "source_amount": "20%; percent basis unspecified",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"sodium carbonate solution\",\n          \"conc_value\": 20,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The target retains an empty composition and Unknown solution name. Restore the source-named 20% sodium carbonate stock and preserve the undefined percent basis; do not copy the maintained owner w/v interpretation as authenticated evidence."
  },
  {
    "decision_id": "q6",
    "claim": "Maintained stock composition basis",
    "decision": "correct",
    "stage": "Separate sodium carbonate stock, not main medium",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "20.0",
          "unit": "PERCENT_W_V"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "solutions[0].composition[0].notes",
        "stored": "TOGO M789 / JCM Medium 763 specifies the pH-adjusting sodium carbonate solution as 20.0% w/v."
      }
    ],
    "source_amount": "20%; source does not specify w/v, w/w or another denominator",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"sodium carbonate solution\",\n          \"conc_value\": 20,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The numeric 20 is supported, but PERCENT_W_V and the assertion that the source specifies w/v exceed the captured sources. Preserve the verbatim percent statement and mark its basis unresolved rather than converting to grams per litre or selecting another percent unit."
  },
  {
    "decision_id": "q7",
    "claim": "Maintained unqualified stock-strength statements",
    "decision": "evidence_only",
    "stage": "Stock identity and qualitative preparation context",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "20% sodium carbonate solution"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "solutions[0].notes",
        "stored": "TOGO M789 / JCM Medium 763 uses sterile 20% sodium carbonate to adjust pH."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "sterilization.notes",
        "stored": "Autoclave the basal medium and the 20% sodium carbonate solution before final pH adjustment."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "notes",
        "stored": "MediaDive J763 and TOGO M789 describe JCM Medium 763 Alkaline Tryptone Soya Broth Medium as 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L distilled water, adjusted after autoclaving to pH 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution."
      }
    ],
    "source_amount": "20% unqualified stock",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"sodium carbonate solution\",\n          \"conc_value\": 20,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "These existing statements retain the source percentage without an explicit mass/volume denominator and need attached evidence. Their support does not authenticate the separate PERCENT_W_V concentration field."
  },
  {
    "decision_id": "q8",
    "claim": "Missing generated pH range",
    "decision": "add",
    "stage": "After cooling and variable carbonate addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "8.5–9.0",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "Restore the source interval with its adjustment stage. No single measured pH is supplied, and the provider summary 8.8 must not replace the explicit procedural range."
  },
  {
    "decision_id": "q9",
    "claim": "Maintained pH range",
    "decision": "evidence_only",
    "stage": "After cooling and carbonate adjustment",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 8.5,
          "max": 9.0
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution."
      }
    ],
    "source_amount": "8.5–9.0",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The maintained owner already retains the correct range and stage; attach narrow evidence without changing its values."
  },
  {
    "decision_id": "q10",
    "claim": "Provider pH summary versus procedural interval",
    "decision": "conflict",
    "stage": "Secondary metadata compared with the same source preparation text",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "ph_range",
        "stored": {
          "min": 8.5,
          "max": 9.0
        }
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null
      }
    ],
    "source_amount": "Provider min_pH=max_pH=8.8; preparation 8.5–9.0",
    "source_snippets": [
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.medium.min_pH/max_pH",
        "exact_source_quote": "\"min_pH\": 8.8,\n            \"max_pH\": 8.8",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      },
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The scalar metadata is narrower than the explicit preparation interval; no evidence identifies it as a measured final pH. Preserve the range and report this source-level difference without overwriting correct owner values or asserting how the scalar was derived."
  },
  {
    "decision_id": "q11",
    "claim": "Generated basal and stock preparation",
    "decision": "add",
    "stage": "Basal autoclaving, cooling, then sterile autoclaved stock adjustment",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null
      }
    ],
    "source_amount": "No numeric cycle or cooling temperature specified",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "Restore the available secondary-source sequence and distinguish basal medium from the separately autoclaved stock. The unavailable JCM page supplies no transferable default."
  },
  {
    "decision_id": "q12",
    "claim": "Maintained preparation and stock sterilization",
    "decision": "evidence_only",
    "stage": "Existing preparation and separate stock treatment",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps[1].description",
        "stored": "Autoclave."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps[2].description",
        "stored": "After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "notes": "Autoclave the basal medium and the 20% sodium carbonate solution before final pH adjustment."
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": "Autoclave before adjusting the medium pH."
      }
    ],
    "source_amount": "Autoclave; cool before pH adjustment; sterile stock also autoclaved",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "The maintained owner already retains this secondary-source sequence and does not invent a numeric cycle. It needs exact evidence, not a finding that its preparation is absent."
  },
  {
    "decision_id": "q13",
    "claim": "Unspecified sterilization parameters",
    "decision": "not_quantified",
    "stage": "Basal and stock autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "sterilization",
        "stored": {
          "method": "AUTOCLAVE",
          "notes": "Autoclave the basal medium and the 20% sodium carbonate solution before final pH adjustment."
        }
      }
    ],
    "source_amount": "Temperature, duration and pressure not stated",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 -- 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with sterile 20% sodium carbonate solution (autoclaved).",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "No numeric sterilization parameters can be extracted from either secondary source or the empty primary response. Do not supply generic JCM defaults, a guessed cooling temperature or a borrowed cycle."
  },
  {
    "decision_id": "q14",
    "claim": "Conditional solid-medium branch",
    "decision": "add",
    "stage": "Separate physical-state variant of the liquid recipe",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "variant_children",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "variant_children",
        "stored": null
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": [
          {
            "step_number": 1,
            "action": "MIX",
            "description": "Dissolve 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L water."
          },
          {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave."
          },
          {
            "step_number": 3,
            "action": "ADJUST_PH",
            "description": "After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution."
          }
        ]
      }
    ],
    "source_amount": "20.0 g/L agar",
    "source_snippets": [
      {
        "source_key": "togoM789",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789",
        "source_locator": "$.comments[1].comment",
        "exact_source_quote": "For preparation of solid medium, add 20.0 g/L agar.",
        "snapshot_sha256": "ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9"
      },
      {
        "source_key": "mediadiveJ763api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J763",
        "source_locator": "$.data.solutions[0].steps[1].step",
        "exact_source_quote": "For preparation of solid medium, add 20.0 g/L agar.",
        "snapshot_sha256": "07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41"
      }
    ],
    "explanation": "Retain the source-only solidification option as a scoped branch or variant context. Do not add agar to the unconditional liquid recipe. The context parent mentions a sibling, but this review does not independently authenticate that separate sibling record."
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:010198.

2 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 1/2 primary and 1/2 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 2: primary 50.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010198.

22 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source identity and direct relation scope

identity: supported. Targets: CultureMech:010198.

TOGO M789 explicitly identifies JCM_M763, and MediaDive J763 has the matching source link and formulation identity. The direct maintained parent resolves to the exact accession and CultureMech ID. This establishes source correspondence from usable secondary records while collection-level confirmation remains a required access limitation; it does not establish strain growth.

### Water, sodium carbonate and commercial mixture specificity

grounding: concern. Targets: CultureMech:010198.

Water grounding is compatible. The owner sodium carbonate term resolves to the unsolvated CO3.2Na structure; the secondary source names sodium carbonate without a hydrate or supplied-form specification. This is a specificity limit, not proof of an incorrect chemical identifier. No hydrate-specific mass, molarity or replacement ID is inferred. Oxoid broth remains a commercial undefined mixture; its absent pure-chemical mapping does not justify invented composition.

### Liquid complex-medium scope and source-only solid branch

scope: supported. Targets: CultureMech:010198.

The liquid base is complex and undefined because it uses commercial broth. Generic bacterial filing and microbial cultivation are broad metadata, not organism-specific growth evidence. The 20 g/L agar statement is explicitly conditional and does not contradict the liquid base classification. Current provider page has no demonstrated strain-growth evidence.

### Generated target versus maintained source and context parent

ownership: concern. Targets: CultureMech:010198.

The sole maintained owner already fixes water units, names the stock and preserves pH/preparation; the generated target predates that repair and remains stale. The maintained owner still overstates percentage basis and lacks attached narrow evidence. Its context parent shares those interpretations, so shared values do not make the w/v claim independently verified. Correct the maintained source first, then use a separately authorized generator; do not directly patch generated data.

## Findings

### f1: Generated recipe omits maintained volume, stock and preparation corrections

major / open / confirmed; issue key: cm010198-stale-generated-layer.

The target still stores water as 1 G_PER_L, an empty Unknown solution and no pH or preparation, while its September-maintained owner has volumetric water, a named stock and the source-range sequence. The exact secondary sources support these improvements with a remaining percent-basis limitation.

### f2: Maintained stock claims an unsupported w/v basis

major / open / confirmed; issue key: cm010198-percent-basis.

The owner represents sodium carbonate as 20.0 PERCENT_W_V and says the source specifies w/v. TOGO and MediaDive instead provide only 20%, with a variable pH-adjusting dose. The unavailable primary does not resolve the denominator, and source agreement is not evidence for a specific percent basis.

### f3: Correct maintained quantities and preparation lack attached evidence

minor / open / confirmed; issue key: cm010198-claim-evidence.

Source/notes and bare references are present in the maintained owner, but none of its amount or preparation claims has attached literal evidence. The target has no such evidence either. Successful reference validation checked zero excerpts and cannot authenticate those claims.

## Recommended Actions And Acceptance Checks

### a1

Preserve the already-correct maintained volume and source sequence, resolve stock-basis overstatement there, then regenerate the target through the owning pipeline with stage-specific evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain the supported 20% statement while explicitly documenting unresolved percent basis; do not invent stock mass, final dilution or a replacement unit. Seek exact primary support before asserting a denominator.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach the exact secondary snippets to supported layer-specific values and stages, labeling primary access limits; keep unsupported percentage basis separate from correct evidence-only claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch022/213/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/213/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml:1:id: CultureMech:010198<br>./data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml:1:id: CultureMech:010198<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/213/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/213/evidence-context-original.json; Complete frozen source context compared with fresh native input hashes | context_only | Every contextual input hash matches the fresh inspection at the same base. Preflight remains provisional provenance; this review supplies its own single-target judgment. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789; Complete meta, components[0].items[0:3] and both comments | supports | TOGO M789 explicitly maps to JCM_M763 and the exact JCM URL. It gives 1 L water, 30 g Oxoid broth, an unqualified 20% sodium carbonate stock, pH 8.5–9.0 after cooling and a distinct solid branch. This is a secondary transcription, not currently accessible collection confirmation. |
| secondary | https://mediadive.dsmz.de/rest/medium/J763; Complete data.medium, solutions[0] recipe, steps and equipment | supports | Exact J763 identity and declared 1000 mL main basis agree with TOGO. The preparation step preserves pH 8.5–9.0 despite scalar metadata 8.8. No structured stock formulation, percent basis, fixed stock dose or numeric autoclave cycle is supplied. |
| provider-page | https://mediadive.dsmz.de/medium/J763; Whole recipe, preparation steps and metadata; external-source notice | supports | The public page corroborates API content and explicitly labels the record unofficial and supplied by external sources. It does not replace missing primary confirmation or demonstrate growth by any strain. |
| jcm763-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=763; Preserved exact public retrieval result | context_only | The exact collection request for JCM 763 returned HTTP 200 with Nothing found, not recipe content. Primary formulation, percent basis and any collection-specific defaults therefore remain unavailable. Secondary transcriptions remain usable with their source scope; no JCM default cycle is imported. |
| togoM789page-attempt | https://togomedium.org/medium/M789; Preserved exact public retrieval result | context_only | The TOGO M789 HTML page capture contains only its application shell. The exact M789 API payload is available and independently inspected, so this optional page-rendering limit does not remove the secondary formulation evidence. |
| relation | data/normalized_yaml/bacterial/alkaline_tryptone_soya_broth_medium.yaml; Complete context parent and maintained owner parent_media; exact Git path, ID, name and source accession | supports | The direct parent path resolves exactly to CultureMech:003106 and MediaDive J763. Its current source-stage values agree with the maintained owner, including the same unsupported w/v specificity. Current mutual agreement and SOURCE_DUPLICATE metadata support accession correspondence, not independent primary authentication. Parent-only sibling claims are context and are not transferred into this target review. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch022/213/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 11, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml", "events": 11, "timestamp_issues": []}] |
| writer-0 | scripts/repair_togo_m789_alkaline_tsb_score15.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current M789 repair writer explicitly restores volume, pH, stock and preparation but assigns PERCENT_W_V without an explicit basis in captured secondary sources. Its September repair postdates the August generated merge event. Current importer/merge code is context only and has not been replayed; these inspected bytes support a stale-layer comparison, not proof of historical execution. |
| writer-1 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current M789 repair writer explicitly restores volume, pH, stock and preparation but assigns PERCENT_W_V without an explicit basis in captured secondary sources. Its September repair postdates the August generated merge event. Current importer/merge code is context only and has not been replayed; these inspected bytes support a stale-layer comparison, not proof of historical execution. |
| writer-2 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | The current M789 repair writer explicitly restores volume, pH, stock and preparation but assigns PERCENT_W_V without an explicit basis in captured secondary sources. Its September repair postdates the August generated merge event. Current importer/merge code is context only and has not been replayed; these inspected bytes support a stale-layer comparison, not proof of historical execution. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact collection request for JCM 763 returned HTTP 200 with Nothing found, not recipe content. Primary formulation, percent basis and any collection-specific defaults therefore remain unavailable. Secondary transcriptions remain usable with their source scope; no JCM default cycle is imported.
- The TOGO M789 HTML page capture contains only its application shell. The exact M789 API payload is available and independently inspected, so this optional page-rendering limit does not remove the secondary formulation evidence.
- The context parent is read only to verify the maintained direct source relationship and compare inherited interpretation. Its separate sibling medium is not reviewed or asserted equivalent. No catalogue product specification, hydrate-specific carbonate form, percent denominator or strain-growth outcome is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131412Z-culturemech-010198-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaline_tryptone_soya_broth_medium (CultureMech:010198)'
started_at: '2026-10-21T13:04:54Z'
finished_at: '2026-10-21T13:14:12Z'
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
summary: The generated target retains a water mass-unit error and an empty carbonate
  stock, while its maintained owner already restores water volume, pH range and preparation.
  The secondary sources support these improvements but only an unqualified 20% stock;
  the owner adds an unsupported w/v basis. Exact JCM 763 formulation content is unavailable,
  so the review remains partial.
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
  - path: data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
    sha256: aa5580509094b3f4b3bb8f4cd3908cabf0c13a7ac1ebf2e1ff32e5888a297933
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
    sha256: d5cff6fe4a5177c98726bc1a5d31ff490e340eae0ef710e752ca536819d55fa4
    role: context
  - path: data/normalized_yaml/bacterial/alkaline_tryptone_soya_broth_medium.yaml
    sha256: 8cd2fe93e52bc05320418e4dafd493b53a4339ec64e6f7ea3211c8d12a6ffc10
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
  - path: scripts/fetch_medium_concentration_sources.py
    sha256: 746c2828863e6ee409d88409a540ea0a8d01ffad3e38be4a4a47f47bec5bbeb5
    role: context
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
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
  - path: scripts/repair_mediadive_stock_concentration_evidence.py
    sha256: 54d862deea48e76f83f424b79cbef57567ba41b539bbea29229d15c2fabd1158
    role: context
  - path: scripts/repair_togo_m789_alkaline_tsb_score15.py
    sha256: 4a13f016ca1aab8e1a1a99cb579e337af9c966e89ca6832b06723cb6269cf18c
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
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 213; batch 022 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-one task batches
    contain 210 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 213 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010198
targets:
- target_id: CultureMech:010198
  path: data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  label: alkaline_tryptone_soya_broth_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/213/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/213/strict.tsv"
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010198
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
  - CultureMech:010198
- check_id: jcm763-source-access
  name: 'Exact source content access: jcm763'
  required: true
  status: unavailable
  summary: The exact collection request for JCM 763 returned HTTP 200 with Nothing
    found, not recipe content. Primary formulation, percent basis and any collection-specific
    defaults therefore remain unavailable. Secondary transcriptions remain usable
    with their source scope; no JCM default cycle is imported.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - jcm763-attempt
- check_id: togoM789page-source-access
  name: 'Exact source content access: togoM789page'
  required: false
  status: unavailable
  summary: The TOGO M789 HTML page capture contains only its application shell. The
    exact M789 API payload is available and independently inspected, so this optional
    page-rendering limit does not remove the secondary formulation evidence.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - togoM789page-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:24.285548Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch022/213/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:25.844060Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/213/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:27.898051Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:29.378320Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:14:11Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml:1:id:
    CultureMech:010198

    ./data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml:1:id:
    CultureMech:010198

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/213/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:14:11Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 196658d3b7437f1e48e8d6330c9f16223714506fc7d7792ebd679d7959697c09
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/213/evidence-context-original.json
  locator: Complete frozen source context compared with fresh native input hashes
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: Every contextual input hash matches the fresh inspection at the same base.
    Preflight remains provisional provenance; this review supplies its own single-target
    judgment.
  snapshot_sha256: 3b31f2b647f02ac6006acebb0e7c4345a1ea9fce4f0461ba5ce87c4604320a73
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789
  locator: Complete meta, components[0].items[0:3] and both comments
  accessed_at: '2026-10-21T12:52:18.373954Z'
  support: supports
  summary: TOGO M789 explicitly maps to JCM_M763 and the exact JCM URL. It gives 1
    L water, 30 g Oxoid broth, an unqualified 20% sodium carbonate stock, pH 8.5–9.0
    after cooling and a distinct solid branch. This is a secondary transcription,
    not currently accessible collection confirmation.
  snapshot_sha256: ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9
- evidence_id: secondary
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J763
  locator: Complete data.medium, solutions[0] recipe, steps and equipment
  accessed_at: '2026-10-21T12:52:17.841109Z'
  support: supports
  summary: Exact J763 identity and declared 1000 mL main basis agree with TOGO. The
    preparation step preserves pH 8.5–9.0 despite scalar metadata 8.8. No structured
    stock formulation, percent basis, fixed stock dose or numeric autoclave cycle
    is supplied.
  snapshot_sha256: 07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41
- evidence_id: provider-page
  kind: database
  reference: https://mediadive.dsmz.de/medium/J763
  locator: Whole recipe, preparation steps and metadata; external-source notice
  accessed_at: '2026-10-21T12:52:17.261270Z'
  support: supports
  summary: The public page corroborates API content and explicitly labels the record
    unofficial and supplied by external sources. It does not replace missing primary
    confirmation or demonstrate growth by any strain.
  snapshot_sha256: 5c13004a2363a41a6f789261c5f4228f5d282d2b10c3dcaf8b29abe32c512201
- evidence_id: jcm763-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=763
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:52:19.054106Z'
  support: context_only
  summary: The exact collection request for JCM 763 returned HTTP 200 with Nothing
    found, not recipe content. Primary formulation, percent basis and any collection-specific
    defaults therefore remain unavailable. Secondary transcriptions remain usable
    with their source scope; no JCM default cycle is imported.
  snapshot_sha256: 784cc346c2cab175d2a052d634cd95dd7c50649c144bc029c8205c70e748eb56
- evidence_id: togoM789page-attempt
  kind: database
  reference: https://togomedium.org/medium/M789
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:52:18.025462Z'
  support: context_only
  summary: The TOGO M789 HTML page capture contains only its application shell. The
    exact M789 API payload is available and independently inspected, so this optional
    page-rendering limit does not remove the secondary formulation evidence.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: relation
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkaline_tryptone_soya_broth_medium.yaml
  locator: Complete context parent and maintained owner parent_media; exact Git path,
    ID, name and source accession
  accessed_at: '2026-10-21T13:14:11Z'
  support: supports
  summary: The direct parent path resolves exactly to CultureMech:003106 and MediaDive
    J763. Its current source-stage values agree with the maintained owner, including
    the same unsupported w/v specificity. Current mutual agreement and SOURCE_DUPLICATE
    metadata support accession correspondence, not independent primary authentication.
    Parent-only sibling claims are context and are not transferred into this target
    review.
  snapshot_sha256: 8cd2fe93e52bc05320418e4dafd493b53a4339ec64e6f7ea3211c8d12a6ffc10
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/213/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 5e0eeca0ab2aa8585e82d97fa7aef1d3bff27ec47a4aacff8a0eb43dc15086c5
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:14:11Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type":
    "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: '[{"input": "target", "events": 11, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml",
    "events": 11, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: scripts/repair_togo_m789_alkaline_tsb_score15.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: The current M789 repair writer explicitly restores volume, pH, stock and
    preparation but assigns PERCENT_W_V without an explicit basis in captured secondary
    sources. Its September repair postdates the August generated merge event. Current
    importer/merge code is context only and has not been replayed; these inspected
    bytes support a stale-layer comparison, not proof of historical execution.
  snapshot_sha256: 4a13f016ca1aab8e1a1a99cb579e337af9c966e89ca6832b06723cb6269cf18c
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: The current M789 repair writer explicitly restores volume, pH, stock and
    preparation but assigns PERCENT_W_V without an explicit basis in captured secondary
    sources. Its September repair postdates the August generated merge event. Current
    importer/merge code is context only and has not been replayed; these inspected
    bytes support a stale-layer comparison, not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:14:11Z'
  support: context_only
  summary: The current M789 repair writer explicitly restores volume, pH, stock and
    preparation but assigns PERCENT_W_V without an explicit basis in captured secondary
    sources. Its September repair postdates the August generated merge event. Current
    importer/merge code is context only and has not been replayed; these inspected
    bytes support a stale-layer comparison, not proof of historical execution.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 14 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"Generated water\
    \ quantity\",\n    \"decision\": \"correct\",\n    \"stage\": \"Liquid main recipe,\
    \ provider-declared 1000 mL basis\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"1 L source water; provider 1000 mL\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM789\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\
    \n      }\n    ],\n    \"explanation\": \"The target stores 1 G_PER_L, a mass-unit\
    \ conversion error. Retain the source volume and main-recipe basis; no density\
    \ conversion or measured post-adjustment final volume is inferred.\"\n  },\n \
    \ {\n    \"decision_id\": \"q2\",\n    \"claim\": \"Maintained water quantity\
    \ and repeated preparation claim\",\n    \"decision\": \"evidence_only\",\n  \
    \  \"stage\": \"Liquid main recipe before variable stock adjustment\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"ML_PER_L\"\n    \
    \    }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].notes\",\n        \"stored\": \"TOGO\
    \ M789 / JCM Medium 763 contributes 1000.0 ml/L distilled water.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L water.\"\n    \
    \  }\n    ],\n    \"source_amount\": \"1000 mL on the declared 1000 mL main basis\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM789\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\
    \n      }\n    ],\n    \"explanation\": \"The maintained owner already corrects\
    \ the target unit to ML_PER_L and states the same volume in preparation. It has\
    \ source prose but no attached amount evidence. The later variable carbonate addition\
    \ does not establish a measured final volume.\"\n  },\n  {\n    \"decision_id\"\
    : \"q3\",\n    \"claim\": \"Commercial broth amount in both layers\",\n    \"\
    decision\": \"evidence_only\",\n    \"stage\": \"Liquid main medium; intact commercial\
    \ mixture\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30.0\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].notes\",\n        \"stored\": \"TOGO\
    \ M789 / JCM Medium 763 lists 30.0 g/L Oxoid Tryptone soya broth.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Dissolve 30.0 g/L Oxoid Tryptone soya broth in 1000.0 ml/L water.\"\n    \
    \  }\n    ],\n    \"source_amount\": \"30 g source batch; provider explicitly\
    \ 30 g/L\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM789\"\
    ,\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tryptone soya broth (Oxoid)\\\",\\n          \\\
    \"volume\\\": 30,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Trypticase soy broth\\\",\\n                        \\\"compound_id\\\
    \": 99,\\n                        \\\"attribute\\\": \\\"Oxoid\\\",\\n       \
    \                 \\\"amount\\\": 30,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 30,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"Both layers retain the correct amount; none\
    \ has attached claim-level evidence. Provider g_l supplies the declared basis.\
    \ Preserve the Oxoid mixture identity without decomposing it into guessed constituents\
    \ or substituting a generic product.\"\n  },\n  {\n    \"decision_id\": \"q4\"\
    ,\n    \"claim\": \"Variable carbonate addition\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"stage\": \"After basal sterilization and cooling, adjust to source pH\
    \ range\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"No fixed stock volume or final\
    \ carbonate amount supplied\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"togoM789\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"sodium carbonate solution\\\",\\n          \\\"\
    conc_value\\\": 20,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n \
    \       \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"Both layers correctly retain VARIABLE for\
    \ the pH-adjusting dose. The 20% is a stock-strength statement, not the dose or\
    \ final-medium concentration. Do not infer a volume, dilution or final carbonate\
    \ mass.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"claim\": \"Missing target\
    \ stock-strength context\",\n    \"decision\": \"add\",\n    \"stage\": \"Separate\
    \ pH-adjusting stock\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[0].composition\",\n        \"stored\": []\n  \
    \    },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].name\",\n        \"stored\": \"Unknown\
    \ solution\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].notes\",\n        \"stored\": \"Role:\
    \ Buffer; Properties: Defined component, Inorganic compound, Solution\"\n    \
    \  }\n    ],\n    \"source_amount\": \"20%; percent basis unspecified\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"togoM789\",\n   \
    \     \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"sodium carbonate solution\\\",\\n          \\\"\
    conc_value\\\": 20,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n \
    \       \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"The target retains an empty composition and\
    \ Unknown solution name. Restore the source-named 20% sodium carbonate stock and\
    \ preserve the undefined percent basis; do not copy the maintained owner w/v interpretation\
    \ as authenticated evidence.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"\
    claim\": \"Maintained stock composition basis\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Separate sodium carbonate stock, not main medium\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"20.0\",\n          \"unit\": \"PERCENT_W_V\"\
    \n        }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].notes\",\n        \"\
    stored\": \"TOGO M789 / JCM Medium 763 specifies the pH-adjusting sodium carbonate\
    \ solution as 20.0% w/v.\"\n      }\n    ],\n    \"source_amount\": \"20%; source\
    \ does not specify w/v, w/w or another denominator\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n     \
    \   \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"sodium carbonate solution\\\",\\n          \\\"\
    conc_value\\\": 20,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n \
    \       \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"The numeric 20 is supported, but PERCENT_W_V\
    \ and the assertion that the source specifies w/v exceed the captured sources.\
    \ Preserve the verbatim percent statement and mark its basis unresolved rather\
    \ than converting to grams per litre or selecting another percent unit.\"\n  },\n\
    \  {\n    \"decision_id\": \"q7\",\n    \"claim\": \"Maintained unqualified stock-strength\
    \ statements\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Stock\
    \ identity and qualitative preparation context\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preferred_term\",\n        \"stored\"\
    : \"20% sodium carbonate solution\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].notes\",\n        \"stored\": \"TOGO\
    \ M789 / JCM Medium 763 uses sterile 20% sodium carbonate to adjust pH.\"\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate\
    \ solution.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization.notes\",\n        \"stored\": \"Autoclave\
    \ the basal medium and the 20% sodium carbonate solution before final pH adjustment.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"notes\",\n        \"stored\": \"MediaDive J763 and\
    \ TOGO M789 describe JCM Medium 763 Alkaline Tryptone Soya Broth Medium as 30.0\
    \ g/L Oxoid Tryptone soya broth in 1000.0 ml/L distilled water, adjusted after\
    \ autoclaving to pH 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution.\"\
    \n      }\n    ],\n    \"source_amount\": \"20% unqualified stock\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n     \
    \   \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"sodium carbonate solution\\\",\\n          \\\"\
    conc_value\\\": 20,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n \
    \       \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"These existing statements retain the source\
    \ percentage without an explicit mass/volume denominator and need attached evidence.\
    \ Their support does not authenticate the separate PERCENT_W_V concentration field.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"claim\": \"Missing generated\
    \ pH range\",\n    \"decision\": \"add\",\n    \"stage\": \"After cooling and\
    \ variable carbonate addition\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ph_range\",\n        \"stored\": null\n      },\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"8.5–9.0\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n     \
    \   \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"Restore the source interval with its adjustment\
    \ stage. No single measured pH is supplied, and the provider summary 8.8 must\
    \ not replace the explicit procedural range.\"\n  },\n  {\n    \"decision_id\"\
    : \"q9\",\n    \"claim\": \"Maintained pH range\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"stage\": \"After cooling and carbonate adjustment\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 8.5,\n          \"max\": 9.0\n        }\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate\
    \ solution.\"\n      }\n    ],\n    \"source_amount\": \"8.5–9.0\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n     \
    \   \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"The maintained owner already retains the correct\
    \ range and stage; attach narrow evidence without changing its values.\"\n  },\n\
    \  {\n    \"decision_id\": \"q10\",\n    \"claim\": \"Provider pH summary versus\
    \ procedural interval\",\n    \"decision\": \"conflict\",\n    \"stage\": \"Secondary\
    \ metadata compared with the same source preparation text\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": {\n          \"\
    min\": 8.5,\n          \"max\": 9.0\n        }\n      },\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ph_range\",\n        \"stored\": null\n      }\n  \
    \  ],\n    \"source_amount\": \"Provider min_pH=max_pH=8.8; preparation 8.5–9.0\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"mediadiveJ763api\"\
    ,\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n \
    \       \"source_locator\": \"$.data.medium.min_pH/max_pH\",\n        \"exact_source_quote\"\
    : \"\\\"min_pH\\\": 8.8,\\n            \\\"max_pH\\\": 8.8\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ },\n      {\n        \"source_key\": \"togoM789\",\n        \"source_url\":\
    \ \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\",\n \
    \       \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"The scalar metadata is narrower than the explicit\
    \ preparation interval; no evidence identifies it as a measured final pH. Preserve\
    \ the range and report this source-level difference without overwriting correct\
    \ owner values or asserting how the scalar was derived.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"claim\": \"Generated basal and stock preparation\",\n    \"\
    decision\": \"add\",\n    \"stage\": \"Basal autoclaving, cooling, then sterile\
    \ autoclaved stock adjustment\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n  \
    \    },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_amount\": \"No numeric cycle or cooling\
    \ temperature specified\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM789\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"Restore the available secondary-source sequence\
    \ and distinguish basal medium from the separately autoclaved stock. The unavailable\
    \ JCM page supplies no transferable default.\"\n  },\n  {\n    \"decision_id\"\
    : \"q12\",\n    \"claim\": \"Maintained preparation and stock sterilization\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"Existing preparation\
    \ and separate stock treatment\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[1].description\",\n        \"stored\"\
    : \"Autoclave.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[2].description\",\n        \"stored\"\
    : \"After cooling, adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate\
    \ solution.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"notes\": \"Autoclave the basal medium\
    \ and the 20% sodium carbonate solution before final pH adjustment.\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : \"Autoclave before adjusting the medium pH.\"\n      }\n    ],\n    \"source_amount\"\
    : \"Autoclave; cool before pH adjustment; sterile stock also autoclaved\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"togoM789\",\n \
    \       \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"The maintained owner already retains this\
    \ secondary-source sequence and does not invent a numeric cycle. It needs exact\
    \ evidence, not a finding that its preparation is absent.\"\n  },\n  {\n    \"\
    decision_id\": \"q13\",\n    \"claim\": \"Unspecified sterilization parameters\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"stage\": \"Basal and stock autoclaving\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": {\n       \
    \   \"method\": \"AUTOCLAVE\",\n          \"notes\": \"Autoclave the basal medium\
    \ and the 20% sodium carbonate solution before final pH adjustment.\"\n      \
    \  }\n      }\n    ],\n    \"source_amount\": \"Temperature, duration and pressure\
    \ not stated\",\n    \"source_snippets\": [\n      {\n        \"source_key\":\
    \ \"togoM789\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Mix components thoroughly and autoclave. After cooling, adjust pH to 8.5 --\
    \ 9.0 with sterile 20% sodium carbonate solution (autoclaved).\",\n        \"\
    snapshot_sha256\": \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Mix\
    \ components thoroughly and autoclave. After cooling, adjust pH to 8.5 - 9.0 with\
    \ sterile 20% sodium carbonate solution (autoclaved).\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"No numeric sterilization parameters can be\
    \ extracted from either secondary source or the empty primary response. Do not\
    \ supply generic JCM defaults, a guessed cooling temperature or a borrowed cycle.\"\
    \n  },\n  {\n    \"decision_id\": \"q14\",\n    \"claim\": \"Conditional solid-medium\
    \ branch\",\n    \"decision\": \"add\",\n    \"stage\": \"Separate physical-state\
    \ variant of the liquid recipe\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\",\n\
    \        \"field_path\": \"variant_children\",\n        \"stored\": null\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"variant_children\",\n        \"stored\": null\n \
    \     },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": [\n   \
    \       {\n            \"step_number\": 1,\n            \"action\": \"MIX\",\n\
    \            \"description\": \"Dissolve 30.0 g/L Oxoid Tryptone soya broth in\
    \ 1000.0 ml/L water.\"\n          },\n          {\n            \"step_number\"\
    : 2,\n            \"action\": \"AUTOCLAVE\",\n            \"description\": \"\
    Autoclave.\"\n          },\n          {\n            \"step_number\": 3,\n   \
    \         \"action\": \"ADJUST_PH\",\n            \"description\": \"After cooling,\
    \ adjust pH to 8.5-9.0 with sterile autoclaved 20% sodium carbonate solution.\"\
    \n          }\n        ]\n      }\n    ],\n    \"source_amount\": \"20.0 g/L agar\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM789\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M789\"\
    ,\n        \"source_locator\": \"$.comments[1].comment\",\n        \"exact_source_quote\"\
    : \"For preparation of solid medium, add 20.0 g/L agar.\",\n        \"snapshot_sha256\"\
    : \"ba6254c6cff5062b7aca832f397f724e846de27d96402e0e785bd18607f616c9\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ763api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J763\",\n        \"source_locator\"\
    : \"$.data.solutions[0].steps[1].step\",\n        \"exact_source_quote\": \"For\
    \ preparation of solid medium, add 20.0 g/L agar.\",\n        \"snapshot_sha256\"\
    : \"07d8d8e6894db3c89c80e00ee53ea40f9ec8c9008e4220d17dabb1516f969b41\"\n     \
    \ }\n    ],\n    \"explanation\": \"Retain the source-only solidification option\
    \ as a scoped branch or variant context. Do not add agar to the unconditional\
    \ liquid recipe. The context parent mentions a sibling, but this review does not\
    \ independently authenticate that separate sibling record.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '2 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 1/2 primary and 1/2 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi29377
  details: 'Instance coverage on a 0–100 percent scale, denominator 2: primary 50.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 22 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact source identity and direct relation scope
  outcome: supported
  summary: TOGO M789 explicitly identifies JCM_M763, and MediaDive J763 has the matching
    source link and formulation identity. The direct maintained parent resolves to
    the exact accession and CultureMech ID. This establishes source correspondence
    from usable secondary records while collection-level confirmation remains a required
    access limitation; it does not establish strain growth.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - owner-0
  - provider
  - secondary
  - relation
  - provider-page
- assessment_id: forms
  area: grounding
  topic: Water, sodium carbonate and commercial mixture specificity
  outcome: concern
  summary: Water grounding is compatible. The owner sodium carbonate term resolves
    to the unsolvated CO3.2Na structure; the secondary source names sodium carbonate
    without a hydrate or supplied-form specification. This is a specificity limit,
    not proof of an incorrect chemical identifier. No hydrate-specific mass, molarity
    or replacement ID is inferred. Oxoid broth remains a commercial undefined mixture;
    its absent pure-chemical mapping does not justify invented composition.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - owner-0
  - provider
  - secondary
  - chebi15377
  - chebi29377
- assessment_id: classification
  area: scope
  topic: Liquid complex-medium scope and source-only solid branch
  outcome: supported
  summary: The liquid base is complex and undefined because it uses commercial broth.
    Generic bacterial filing and microbial cultivation are broad metadata, not organism-specific
    growth evidence. The 20 g/L agar statement is explicitly conditional and does
    not contradict the liquid base classification. Current provider page has no demonstrated
    strain-growth evidence.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - provider
  - secondary
  - provider-page
  - quantity-inventory
- assessment_id: ownership
  area: ownership
  topic: Generated target versus maintained source and context parent
  outcome: concern
  summary: The sole maintained owner already fixes water units, names the stock and
    preserves pH/preparation; the generated target predates that repair and remains
    stale. The maintained owner still overstates percentage basis and lacks attached
    narrow evidence. Its context parent shares those interpretations, so shared values
    do not make the w/v claim independently verified. Correct the maintained source
    first, then use a separately authorized generator; do not directly patch generated
    data.
  target_ids:
  - CultureMech:010198
  evidence_ids:
  - record
  - owner-0
  - relation
  - writer-0
  - writer-1
  - writer-2
  - quantity-inventory
findings:
- finding_id: f1
  issue_key: cm010198-stale-generated-layer
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Generated recipe omits maintained volume, stock and preparation corrections
  description: The target still stores water as 1 G_PER_L, an empty Unknown solution
    and no pH or preparation, while its September-maintained owner has volumetric
    water, a named stock and the source-range sequence. The exact secondary sources
    support these improvements with a remaining percent-basis limitation.
  target_ids:
  - CultureMech:010198
  field_paths:
  - ingredients[0].concentration
  - solutions[0]
  - ph_range
  - preparation_steps
  - sterilization
  evidence_ids:
  - record
  - owner-0
  - provider
  - secondary
  - writer-0
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
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
  issue_key: cm010198-percent-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Maintained stock claims an unsupported w/v basis
  description: The owner represents sodium carbonate as 20.0 PERCENT_W_V and says
    the source specifies w/v. TOGO and MediaDive instead provide only 20%, with a
    variable pH-adjusting dose. The unavailable primary does not resolve the denominator,
    and source agreement is not evidence for a specific percent basis.
  target_ids:
  - CultureMech:010198
  field_paths:
  - solutions[0].composition[0].concentration
  - solutions[0].composition[0].notes
  evidence_ids:
  - owner-0
  - provider
  - secondary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
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
  issue_key: cm010198-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct maintained quantities and preparation lack attached evidence
  description: Source/notes and bare references are present in the maintained owner,
    but none of its amount or preparation claims has attached literal evidence. The
    target has no such evidence either. Successful reference validation checked zero
    excerpts and cannot authenticate those claims.
  target_ids:
  - CultureMech:010198
  field_paths:
  - ingredients
  - solutions
  - ph_range
  - preparation_steps
  - references
  evidence_ids:
  - record
  - owner-0
  - provider
  - secondary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
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
  description: Preserve the already-correct maintained volume and source sequence,
    resolve stock-basis overstatement there, then regenerate the target through the
    owning pipeline with stage-specific evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
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
  description: Retain the supported 20% statement while explicitly documenting unresolved
    percent basis; do not invent stock mass, final dilution or a replacement unit.
    Seek exact primary support before asserting a denominator.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
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
  description: Attach the exact secondary snippets to supported layer-specific values
    and stages, labeling primary access limits; keep unsupported percentage basis
    separate from correct evidence-only claims.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010198
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml
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
- The exact collection request for JCM 763 returned HTTP 200 with Nothing found, not
  recipe content. Primary formulation, percent basis and any collection-specific defaults
  therefore remain unavailable. Secondary transcriptions remain usable with their
  source scope; no JCM default cycle is imported.
- The TOGO M789 HTML page capture contains only its application shell. The exact M789
  API payload is available and independently inspected, so this optional page-rendering
  limit does not remove the secondary formulation evidence.
- The context parent is read only to verify the maintained direct source relationship
  and compare inherited interpretation. Its separate sibling medium is not reviewed
  or asserted equivalent. No catalogue product specification, hydrate-specific carbonate
  form, percent denominator or strain-growth outcome is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-022
- generated-medium
```
