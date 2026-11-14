# Source and formulation review: alkaline_lb_agar (CultureMech:009956)

- Review: 20261021T130704Z-culturemech-009956-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:04:52Z
- Finished UTC: 2026-10-21T13:07:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact JCM 557 / TOGO M561 identity and five mass amounts are supported, but water is recorded in a mass unit, material carbonate filtration and basal sterilization instructions are absent, and the source pH and narrow quantity evidence need representation. The generated target and its one maintained owner share these gaps.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 211; batch 022 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-one task batches contain 210 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 213 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009956 | data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml | generated | alkaline_lb_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009956 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009956 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/211/strict.tsv |
| validate-terms | passed | True | CultureMech:009956 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009956 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009956 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009956.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009956.

10 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "Distilled water main-recipe amount",
    "decision": "correct",
    "stage": "JCM 557 main recipe; carbonate prepared separately",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Distilled water 1.0 L",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Medium557 exact ingredient Distilled water",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      },
      {
        "source_key": "togoM561",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63"
      },
      {
        "source_key": "mediadiveJ557api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J557",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67"
      }
    ],
    "explanation": "Source water is 1.0 L = 1000 mL batch input, whereas both layers assert 1 G_PER_L; retain a volume representation and original batch scope, not a density-based mass conversion."
  },
  {
    "decision_id": "q2",
    "claim": "NaCl main-recipe amount",
    "decision": "evidence_only",
    "stage": "JCM 557 main recipe; carbonate prepared separately",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NaCl 15.0 g",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Medium557 exact ingredient NaCl",
        "exact_source_quote": "NaCl 15.0 g",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      },
      {
        "source_key": "togoM561",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63"
      },
      {
        "source_key": "mediadiveJ557api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J557",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 256.674,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67"
      }
    ],
    "explanation": "Both layers contain the matching provider-declared g/L amount but no attached claim evidence. Primary prints batch mass; use the provider explicit 1000 mL basis and g_l field, not an assumed measured final volume. Preserve exact product/form and the separately filtered carbonate preparation."
  },
  {
    "decision_id": "q3",
    "claim": "Na2CO3 main-recipe amount",
    "decision": "evidence_only",
    "stage": "JCM 557 main recipe; carbonate prepared separately",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 CO 3 5.0 g",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Medium557 exact ingredient Na2CO3",
        "exact_source_quote": "Na 2 CO 3 5.0 g",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      },
      {
        "source_key": "togoM561",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63"
      },
      {
        "source_key": "mediadiveJ557api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J557",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 47.1752,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67"
      }
    ],
    "explanation": "Both layers contain the matching provider-declared g/L amount but no attached claim evidence. Primary prints batch mass; use the provider explicit 1000 mL basis and g_l field, not an assumed measured final volume. Preserve exact product/form and the separately filtered carbonate preparation."
  },
  {
    "decision_id": "q4",
    "claim": "Agar main-recipe amount",
    "decision": "evidence_only",
    "stage": "JCM 557 main recipe; carbonate prepared separately",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Agar 15.0 g",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Medium557 exact ingredient Agar",
        "exact_source_quote": "Agar 15.0 g",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      },
      {
        "source_key": "togoM561",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63"
      },
      {
        "source_key": "mediadiveJ557api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J557",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67"
      }
    ],
    "explanation": "Both layers contain the matching provider-declared g/L amount but no attached claim evidence. Primary prints batch mass; use the provider explicit 1000 mL basis and g_l field, not an assumed measured final volume. Preserve exact product/form and the separately filtered carbonate preparation."
  },
  {
    "decision_id": "q5",
    "claim": "Yeast extract (BD-Difco) main-recipe amount",
    "decision": "evidence_only",
    "stage": "JCM 557 main recipe; carbonate prepared separately",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Yeast extract (BD-Difco) 5.0 g",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Medium557 exact ingredient Yeast extract (BD-Difco)",
        "exact_source_quote": "Yeast extract (BD-Difco) 5.0 g",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      },
      {
        "source_key": "togoM561",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63"
      },
      {
        "source_key": "mediadiveJ557api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J557",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67"
      }
    ],
    "explanation": "Both layers contain the matching provider-declared g/L amount but no attached claim evidence. Primary prints batch mass; use the provider explicit 1000 mL basis and g_l field, not an assumed measured final volume. Preserve exact product/form and the separately filtered carbonate preparation."
  },
  {
    "decision_id": "q6",
    "claim": "Tryptone (BD-Difco) main-recipe amount",
    "decision": "evidence_only",
    "stage": "JCM 557 main recipe; carbonate prepared separately",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Tryptone (BD-Difco) 10.0 g",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Medium557 exact ingredient Tryptone (BD-Difco)",
        "exact_source_quote": "Tryptone (BD-Difco) 10.0 g",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      },
      {
        "source_key": "togoM561",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Tryptone (BD-Difco)\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63"
      },
      {
        "source_key": "mediadiveJ557api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J557",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"mmol_l\": 140.687,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67"
      }
    ],
    "explanation": "Both layers contain the matching provider-declared g/L amount but no attached claim evidence. Primary prints batch mass; use the provider explicit 1000 mL basis and g_l field, not an assumed measured final volume. Preserve exact product/form and the separately filtered carbonate preparation."
  },
  {
    "decision_id": "q7",
    "claim": "Final pH",
    "decision": "add",
    "stage": "Final medium after carbonate addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_amount": "about 8.5",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Final preparation sentence",
        "exact_source_quote": "Check final pH to be about 8.5.",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      }
    ],
    "explanation": "Preserve approximate source wording; target and owner have no pH field."
  },
  {
    "decision_id": "q8",
    "claim": "Basal autoclave temperature",
    "decision": "add",
    "stage": "Displayed page default applies except separately filtered carbonate",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_amount": "121°C",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Page557 displayed default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      }
    ],
    "explanation": "Source default is available on this exact page; it is not an incubation condition or permission to autoclave carbonate."
  },
  {
    "decision_id": "q9",
    "claim": "Basal autoclave duration",
    "decision": "add",
    "stage": "Displayed page default applies except separately filtered carbonate",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_amount": "15 min",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Page557 displayed default",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      }
    ],
    "explanation": "Source default is available on this exact page; it is not an incubation condition or permission to autoclave carbonate."
  },
  {
    "decision_id": "q10",
    "claim": "Carbonate filtration solution volume",
    "decision": "not_quantified",
    "stage": "Separately filtered carbonate then aseptic addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "No stock solvent volume, stock strength or filter specification supplied",
    "source_snippets": [
      {
        "source_key": "jcm557",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557",
        "source_locator": "Carbonate preparation sentence",
        "exact_source_quote": "Separately sterilize Na 2 CO 3 by filtration and aseptically add to the medium.",
        "snapshot_sha256": "aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018",
        "parsed_text_sha256": "c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7"
      }
    ],
    "explanation": "The 5 g ingredient amount is known; no separate stock dose/volume or filtration device specification is inferred."
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: supported. Targets: CultureMech:009956.

4 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 4/6 primary and 4/6 secondary instances; all asserted secondary keys have exact pinned MIM rows. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%; secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009956.

15 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact medium and maintained owner

identity: supported. Targets: CultureMech:009956.

CultureMech:009956 maps to TOGO M561 / JCM 557, not generic LB. One exact source contributor resolves; no variant or organism-specific growth assertion is made.

### Classifications, products and stated applications

scope: supported. Targets: CultureMech:009956.

Complex/undefined is consistent with tryptone and yeast extract; 15 g agar supports the solid-agar branch. Bacterial filing and generic cultivation application do not establish strain growth. No invented pure-molecule IDs are assigned to BD-Difco products. Water/salt/carbonate/agar source forms are consistent with the asserted generic terms; source roles are retained as annotations, not experimental claims.

### Maintained input and generated output

ownership: supported. Targets: CultureMech:009956.

Both exact layers currently share all six ingredient quantities and source/history claims. Correct the normalized source and any demonstrated writer issue before authorized regeneration; never patch the derived merge. Current code is not evidence of how the historical bytes were produced.

## Findings

### f1: Water volume is recorded as mass concentration

major / open / confirmed; issue key: cm009956-water-unit.

Both layers assert 1 G_PER_L water; the exact primary and TOGO state 1 L and the provider states 1000 mL. No source supports the mass unit.

### f2: Carbonate filtration and basal sterilization are omitted

major / open / confirmed; issue key: cm009956-preparation-boundary.

Neither layer retains preparation or sterilization. The primary separately filters carbonate and adds it aseptically; its displayed 121°C / 15 min default applies only where not otherwise stated. Omitting this exception changes the preparation scope.

### f3: The final pH check is absent

minor / open / confirmed; issue key: cm009956-ph.

Primary final pH is about 8.5; neither layer retains it. This is a preparation target, not a reported growth optimum.

### f4: Supported mass amounts lack claim-level evidence

minor / open / confirmed; issue key: cm009956-claim-evidence.

All five provider-declared mass concentrations match the source but lack attached source snippets in both layers. Source URLs in notes and ontology mappings do not authenticate individual amounts or bases.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained water representation from exact volume evidence, preserving batch versus provider basis; regenerate after validation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add source-scoped basal sterilization and separate carbonate filtration/addition; do not invent a stock volume or filter specification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Represent the approximate source pH check and attach its exact preparation evidence.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Attach narrow exact primary/provider evidence for unchanged quantities and source metadata; keep undefined-mixture molarity out of the curated claims.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch022/211/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch022/211/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml:1:id: CultureMech:009956<br>./data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml:1:id: CultureMech:009956<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/211/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch022/source-preflight-bound/211/evidence-context-original.json; Complete frozen source context compared with fresh native input hashes | context_only | Every contextual input hash matches the fresh inspection at the same base. Preflight remains provisional provenance; this review supplies its own single-target judgment. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557; Entire exact medium 557 page, all six ingredients, preparation sentence and displayed default | supports | Primary specifies six original amounts, separately filtered carbonate, final pH about 8.5 and basal autoclaving default. Product names remain BD-Difco. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561; meta, components[0].items[0:6], comments[0] | supports | TOGO M561 maps explicitly to JCM 557 and retains original mass/water units and carbonate preparation. |
| provider | https://mediadive.dsmz.de/rest/medium/J557; data.medium and complete solutions[0], id4373 | supports | MediaDive J557 explicitly declares 1000 mL main volume and five g_l amounts. These provider declarations do not independently measure final volume or authenticate molarity for undefined tryptone or agar. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch022/211/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml", "events": 7, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO amount/unit conversion and current single-source merge/equality logic are inspected context. They are not replayed and do not establish historical causation for the frozen bad water unit or omitted preparation. |
| writer-1 | src/culturemech/merge/merger.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO amount/unit conversion and current single-source merge/equality logic are inspected context. They are not replayed and do not establish historical causation for the frozen bad water unit or omitted preparation. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO amount/unit conversion and current single-source merge/equality logic are inspected context. They are not replayed and do not establish historical causation for the frozen bad water unit or omitted preparation. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T130704Z-culturemech-009956-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaline_lb_agar (CultureMech:009956)'
started_at: '2026-10-21T13:04:52Z'
finished_at: '2026-10-21T13:07:04Z'
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
summary: The exact JCM 557 / TOGO M561 identity and five mass amounts are supported,
  but water is recorded in a mass unit, material carbonate filtration and basal sterilization
  instructions are absent, and the source pH and narrow quantity evidence need representation.
  The generated target and its one maintained owner share these gaps.
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
  - path: data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
    sha256: 3138b6e961f1c7f5a5525f9a654caca95c21872f486bcdc42e4d717e2f8ed45c
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
    sha256: c8cbea14b8316d6c4a639356c2a356688e6000725a81aab116ed1d8847223e62
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
  selection: Task review 211; batch 022 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-one task batches
    contain 210 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 213 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009956
targets:
- target_id: CultureMech:009956
  path: data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  label: alkaline_lb_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch022/211/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/211/strict.tsv"
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009956
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
  - CultureMech:009956
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:04.118954Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch022/211/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:05.782111Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-022/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch022/211/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:09.426545Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:05:12.895323Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:07:02Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml:1:id: CultureMech:009956

    ./data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml:1:id: CultureMech:009956

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/211/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:07:02Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: a82620c4d6c901c9342cd87c7c0f6d1681f9338f9f22286c570ac4886c0feda3
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/source-preflight-bound/211/evidence-context-original.json
  locator: Complete frozen source context compared with fresh native input hashes
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Every contextual input hash matches the fresh inspection at the same base.
    Preflight remains provisional provenance; this review supplies its own single-target
    judgment.
  snapshot_sha256: 1cf1fb8d10413b6a814de8d30a16c5b5e1d35559230935b38f898c892e671665
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557
  locator: Entire exact medium 557 page, all six ingredients, preparation sentence
    and displayed default
  accessed_at: '2026-10-21T12:52:19.019265Z'
  support: supports
  summary: Primary specifies six original amounts, separately filtered carbonate,
    final pH about 8.5 and basal autoclaving default. Product names remain BD-Difco.
  snapshot_sha256: aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561
  locator: meta, components[0].items[0:6], comments[0]
  accessed_at: '2026-10-21T12:52:18.179444Z'
  support: supports
  summary: TOGO M561 maps explicitly to JCM 557 and retains original mass/water units
    and carbonate preparation.
  snapshot_sha256: 5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J557
  locator: data.medium and complete solutions[0], id4373
  accessed_at: '2026-10-21T12:52:17.452705Z'
  support: supports
  summary: MediaDive J557 explicitly declares 1000 mL main volume and five g_l amounts.
    These provider declarations do not independently measure final volume or authenticate
    molarity for undefined tryptone or agar.
  snapshot_sha256: 0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch022/211/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 1e83d79515480e90a36db34f328cd0dd27874288863beb06707032c4ab872154
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:07:02Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type":
    "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id":
    "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term",
    "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate
    solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term":
    "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED",
    "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: '[{"input": "target", "events": 8, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml",
    "events": 7, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Current TOGO amount/unit conversion and current single-source merge/equality
    logic are inspected context. They are not replayed and do not establish historical
    causation for the frozen bad water unit or omitted preparation.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Current TOGO amount/unit conversion and current single-source merge/equality
    logic are inspected context. They are not replayed and do not establish historical
    causation for the frozen bad water unit or omitted preparation.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:07:02Z'
  support: context_only
  summary: Current TOGO amount/unit conversion and current single-source merge/equality
    logic are inspected context. They are not replayed and do not establish historical
    causation for the frozen bad water unit or omitted preparation.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 10 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"Distilled water\
    \ main-recipe amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM\
    \ 557 main recipe; carbonate prepared separately\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Distilled water 1.0 L\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\",\n        \"source_locator\"\
    : \"Medium557 exact ingredient Distilled water\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      },\n      {\n        \"source_key\": \"togoM561\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ557api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J557\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67\"\
    \n      }\n    ],\n    \"explanation\": \"Source water is 1.0 L = 1000 mL batch\
    \ input, whereas both layers assert 1 G_PER_L; retain a volume representation\
    \ and original batch scope, not a density-based mass conversion.\"\n  },\n  {\n\
    \    \"decision_id\": \"q2\",\n    \"claim\": \"NaCl main-recipe amount\",\n \
    \   \"decision\": \"evidence_only\",\n    \"stage\": \"JCM 557 main recipe; carbonate\
    \ prepared separately\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\",\n        \"field_path\": \"\
    ingredients[1].concentration\",\n        \"stored\": {\n          \"value\": \"\
    15\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"NaCl 15.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\",\n        \"source_locator\"\
    : \"Medium557 exact ingredient NaCl\",\n        \"exact_source_quote\": \"NaCl\
    \ 15.0 g\",\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      },\n      {\n        \"source_key\": \"togoM561\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561\",\n \
    \       \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 15,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ557api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J557\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 256.674,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67\"\
    \n      }\n    ],\n    \"explanation\": \"Both layers contain the matching provider-declared\
    \ g/L amount but no attached claim evidence. Primary prints batch mass; use the\
    \ provider explicit 1000 mL basis and g_l field, not an assumed measured final\
    \ volume. Preserve exact product/form and the separately filtered carbonate preparation.\"\
    \n  },\n  {\n    \"decision_id\": \"q3\",\n    \"claim\": \"Na2CO3 main-recipe\
    \ amount\",\n    \"decision\": \"evidence_only\",\n    \"stage\": \"JCM 557 main\
    \ recipe; carbonate prepared separately\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\",\n      \
    \  \"field_path\": \"ingredients[2].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Na 2 CO 3 5.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\",\n        \"source_locator\"\
    : \"Medium557 exact ingredient Na2CO3\",\n        \"exact_source_quote\": \"Na\
    \ 2 CO 3 5.0 g\",\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      },\n      {\n        \"source_key\": \"togoM561\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 5,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ557api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J557\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"amount\\\": 5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n                  \
    \      \\\"mmol_l\\\": 47.1752,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67\"\
    \n      }\n    ],\n    \"explanation\": \"Both layers contain the matching provider-declared\
    \ g/L amount but no attached claim evidence. Primary prints batch mass; use the\
    \ provider explicit 1000 mL basis and g_l field, not an assumed measured final\
    \ volume. Preserve exact product/form and the separately filtered carbonate preparation.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"claim\": \"Agar main-recipe amount\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"stage\": \"JCM 557 main recipe;\
    \ carbonate prepared separately\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\",\n        \"field_path\"\
    : \"ingredients[3].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Agar 15.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\",\n        \"source_locator\"\
    : \"Medium557 exact ingredient Agar\",\n        \"exact_source_quote\": \"Agar\
    \ 15.0 g\",\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      },\n      {\n        \"source_key\": \"togoM561\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561\",\n \
    \       \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 15,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ557api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J557\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67\"\
    \n      }\n    ],\n    \"explanation\": \"Both layers contain the matching provider-declared\
    \ g/L amount but no attached claim evidence. Primary prints batch mass; use the\
    \ provider explicit 1000 mL basis and g_l field, not an assumed measured final\
    \ volume. Preserve exact product/form and the separately filtered carbonate preparation.\"\
    \n  },\n  {\n    \"decision_id\": \"q5\",\n    \"claim\": \"Yeast extract (BD-Difco)\
    \ main-recipe amount\",\n    \"decision\": \"evidence_only\",\n    \"stage\":\
    \ \"JCM 557 main recipe; carbonate prepared separately\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Yeast extract (BD-Difco) 5.0 g\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm557\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\"\
    ,\n        \"source_locator\": \"Medium557 exact ingredient Yeast extract (BD-Difco)\"\
    ,\n        \"exact_source_quote\": \"Yeast extract (BD-Difco) 5.0 g\",\n     \
    \   \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      },\n      {\n        \"source_key\": \"togoM561\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561\",\n \
    \       \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ557api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J557\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"BD-Difco\\\",\\n    \
    \                    \\\"amount\\\": 5,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n                    \
    \    \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67\"\n     \
    \ }\n    ],\n    \"explanation\": \"Both layers contain the matching provider-declared\
    \ g/L amount but no attached claim evidence. Primary prints batch mass; use the\
    \ provider explicit 1000 mL basis and g_l field, not an assumed measured final\
    \ volume. Preserve exact product/form and the separately filtered carbonate preparation.\"\
    \n  },\n  {\n    \"decision_id\": \"q6\",\n    \"claim\": \"Tryptone (BD-Difco)\
    \ main-recipe amount\",\n    \"decision\": \"evidence_only\",\n    \"stage\":\
    \ \"JCM 557 main recipe; carbonate prepared separately\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Tryptone (BD-Difco) 10.0 g\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm557\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\"\
    ,\n        \"source_locator\": \"Medium557 exact ingredient Tryptone (BD-Difco)\"\
    ,\n        \"exact_source_quote\": \"Tryptone (BD-Difco) 10.0 g\",\n        \"\
    snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      },\n      {\n        \"source_key\": \"togoM561\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M561\",\n \
    \       \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tryptone (BD-Difco)\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    5135a6567012543c9d39702b6bb73a2484c40ee5976e957a2341beac89e49a63\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ557api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J557\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Tryptone\\\",\\n                        \\\"compound_id\\\"\
    : 71,\\n                        \\\"attribute\\\": \\\"BD-Difco\\\",\\n      \
    \                  \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                   \
    \     \\\"mmol_l\\\": 140.687,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"0c607e4d924ae6cb885ef70256c150a3c7dd84ee3811df43c39abe138ef3ca67\"\
    \n      }\n    ],\n    \"explanation\": \"Both layers contain the matching provider-declared\
    \ g/L amount but no attached claim evidence. Primary prints batch mass; use the\
    \ provider explicit 1000 mL basis and g_l field, not an assumed measured final\
    \ volume. Preserve exact product/form and the separately filtered carbonate preparation.\"\
    \n  },\n  {\n    \"decision_id\": \"q7\",\n    \"claim\": \"Final pH\",\n    \"\
    decision\": \"add\",\n    \"stage\": \"Final medium after carbonate addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"about 8.5\",\n    \"source_snippets\": [\n \
    \     {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\"\
    ,\n        \"source_locator\": \"Final preparation sentence\",\n        \"exact_source_quote\"\
    : \"Check final pH to be about 8.5.\",\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve approximate source wording;\
    \ target and owner have no pH field.\"\n  },\n  {\n    \"decision_id\": \"q8\"\
    ,\n    \"claim\": \"Basal autoclave temperature\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"Displayed page default applies except separately filtered\
    \ carbonate\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_amount\": \"121°C\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\"\
    ,\n        \"source_locator\": \"Page557 displayed default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      }\n    ],\n    \"explanation\": \"Source default is available on this\
    \ exact page; it is not an incubation condition or permission to autoclave carbonate.\"\
    \n  },\n  {\n    \"decision_id\": \"q9\",\n    \"claim\": \"Basal autoclave duration\"\
    ,\n    \"decision\": \"add\",\n    \"stage\": \"Displayed page default applies\
    \ except separately filtered carbonate\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\",\n      \
    \  \"field_path\": \"sterilization\",\n        \"stored\": null\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_amount\": \"15 min\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm557\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\"\
    ,\n        \"source_locator\": \"Page557 displayed default\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      }\n    ],\n    \"explanation\": \"Source default is available on this\
    \ exact page; it is not an incubation condition or permission to autoclave carbonate.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"claim\": \"Carbonate filtration\
    \ solution volume\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"\
    Separately filtered carbonate then aseptic addition\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LB_AGAR.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"No stock solvent volume, stock strength\
    \ or filter specification supplied\",\n    \"source_snippets\": [\n      {\n \
    \       \"source_key\": \"jcm557\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=557\"\
    ,\n        \"source_locator\": \"Carbonate preparation sentence\",\n        \"\
    exact_source_quote\": \"Separately sterilize Na 2 CO 3 by filtration and aseptically\
    \ add to the medium.\",\n        \"snapshot_sha256\": \"aac8075900e30a34e35f2d30f1c1e125f311872fd3d14da52e65846bf865b018\"\
    ,\n        \"parsed_text_sha256\": \"c1c0a879cbadb50c5b787804bc243bc0e7e82681929ea07052fb95f0d02f7ec7\"\
    \n      }\n    ],\n    \"explanation\": \"The 5 g ingredient amount is known;\
    \ no separate stock dose/volume or filtration device specification is inferred.\"\
    \n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: supported
  summary: '4 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 4/6 primary and 4/6 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Source forms
    are assessed separately.'
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi2509
  - chebi26710
  - chebi29377
  details: 'Instance coverage on a 0–100 percent scale, denominator 6: primary 66.67%;
    secondary 66.67%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 15 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact medium and maintained owner
  outcome: supported
  summary: CultureMech:009956 maps to TOGO M561 / JCM 557, not generic LB. One exact
    source contributor resolves; no variant or organism-specific growth assertion
    is made.
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - togo
  - provider
- assessment_id: classification
  area: scope
  topic: Classifications, products and stated applications
  outcome: supported
  summary: Complex/undefined is consistent with tryptone and yeast extract; 15 g agar
    supports the solid-agar branch. Bacterial filing and generic cultivation application
    do not establish strain growth. No invented pure-molecule IDs are assigned to
    BD-Difco products. Water/salt/carbonate/agar source forms are consistent with
    the asserted generic terms; source roles are retained as annotations, not experimental
    claims.
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - record
  - primary
  - togo
  - provider
  - chebi15377
  - chebi26710
  - chebi29377
  - chebi2509
- assessment_id: ownership
  area: ownership
  topic: Maintained input and generated output
  outcome: supported
  summary: Both exact layers currently share all six ingredient quantities and source/history
    claims. Correct the normalized source and any demonstrated writer issue before
    authorized regeneration; never patch the derived merge. Current code is not evidence
    of how the historical bytes were produced.
  target_ids:
  - CultureMech:009956
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: cm009956-water-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water volume is recorded as mass concentration
  description: Both layers assert 1 G_PER_L water; the exact primary and TOGO state
    1 L and the provider states 1000 mL. No source supports the mass unit.
  target_ids:
  - CultureMech:009956
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
  issue_key: cm009956-preparation-boundary
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Carbonate filtration and basal sterilization are omitted
  description: Neither layer retains preparation or sterilization. The primary separately
    filters carbonate and adds it aseptically; its displayed 121°C / 15 min default
    applies only where not otherwise stated. Omitting this exception changes the preparation
    scope.
  target_ids:
  - CultureMech:009956
  field_paths:
  - preparation_steps
  - sterilization
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
  issue_key: cm009956-ph
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The final pH check is absent
  description: Primary final pH is about 8.5; neither layer retains it. This is a
    preparation target, not a reported growth optimum.
  target_ids:
  - CultureMech:009956
  field_paths:
  - ph_value
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: cm009956-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Supported mass amounts lack claim-level evidence
  description: All five provider-declared mass concentrations match the source but
    lack attached source snippets in both layers. Source URLs in notes and ontology
    mappings do not authenticate individual amounts or bases.
  target_ids:
  - CultureMech:009956
  field_paths:
  - ingredients
  - references
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
  description: Correct the maintained water representation from exact volume evidence,
    preserving batch versus provider basis; regenerate after validation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
  description: Add source-scoped basal sterilization and separate carbonate filtration/addition;
    do not invent a stock volume or filter specification.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
  description: Represent the approximate source pH check and attach its exact preparation
    evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
  description: Attach narrow exact primary/provider evidence for unchanged quantities
    and source metadata; keep undefined-mixture molarity out of the curated claims.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009956
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M561_Alkaline_LB_Agar.yaml
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
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-022
- generated-medium
```
