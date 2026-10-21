# Source and formulation review: alkaline_lactose_agar (CultureMech:010329)

- Review: 20261021T124632Z-culturemech-010329-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T12:39:27Z
- Finished UTC: 2026-10-21T12:46:32Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The local TOGO M90 record agrees with the available provider basal masses but changes water and carbonate-stock volumes into mass concentrations, omits provider preparation, and overstates lactose anomer specificity. Exact JCM98 retrieval returns no formulation, so primary confirmation remains unavailable and this scientific review is partial.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 210; batch 021 item 10 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty task batches contain 200 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 203 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010329 | data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml | generated | alkaline_lactose_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010329 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010329 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/210/strict.tsv |
| validate-terms | passed | True | CultureMech:010329 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010329 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010329 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: jcm98 | unavailable | True | CultureMech:010329 | The exact cited JCM98 page returned HTTP 200 with Nothing found. The required primary formulation/conditions check is unavailable despite successful transport. TOGO M90 and MediaDive J98 support a bounded secondary-source comparison; no alternate accession or uncaptured primary text is substituted. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010329.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010329.

10 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "component_or_context": "MgSO4・7H2O basal mass",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "0.2 g per provider recipe; the current g/L value matches the provider's declared nominal 1000 mL basis.",
    "rationale": "No attached quantity evidence exists in either layer. Preserve the literal source mass and provider nominal-volume basis rather than asserting measured final volume. The supplied name/grade remains as written; no alternate commercial product is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q2",
    "component_or_context": "Yeast extract basal mass",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "5 g per provider recipe; the current g/L value matches the provider's declared nominal 1000 mL basis.",
    "rationale": "No attached quantity evidence exists in either layer. Preserve the literal source mass and provider nominal-volume basis rather than asserting measured final volume. The supplied name/grade remains as written; no alternate commercial product is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q3",
    "component_or_context": "K2HPO4 basal mass",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "1 g per provider recipe; the current g/L value matches the provider's declared nominal 1000 mL basis.",
    "rationale": "No attached quantity evidence exists in either layer. Preserve the literal source mass and provider nominal-volume basis rather than asserting measured final volume. The supplied name/grade remains as written; no alternate commercial product is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q4",
    "component_or_context": "Lactose basal mass",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "5 g per provider recipe; the current g/L value matches the provider's declared nominal 1000 mL basis.",
    "rationale": "No attached quantity evidence exists in either layer. Preserve the literal source mass and provider nominal-volume basis rather than asserting measured final volume. The amount is supported, but the provider generic Lactose name does not establish beta-anomer identity.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"Lactose\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Lactose\",\n                        \"compound_id\": 394,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 14.6071,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q5",
    "component_or_context": "Agar basal mass",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "15 g per provider recipe; the current g/L value matches the provider's declared nominal 1000 mL basis.",
    "rationale": "No attached quantity evidence exists in either layer. Preserve the literal source mass and provider nominal-volume basis rather than asserting measured final volume. The supplied name/grade remains as written; no alternate commercial product is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q6",
    "component_or_context": "Polypepton (Nihon Pharm. Co.) basal mass",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "5 g per provider recipe; the current g/L value matches the provider's declared nominal 1000 mL basis.",
    "rationale": "No attached quantity evidence exists in either layer. Preserve the literal source mass and provider nominal-volume basis rather than asserting measured final volume. The supplied name/grade remains as written; no alternate commercial product is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"Polypepton (Nihon Pharm. Co.)\",\n          \"volume\": 5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Polypeptone\",\n                        \"compound_id\": 442,\n                        \"attribute\": \"Nihon Pharm. Co.\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q7",
    "component_or_context": "Basal water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "900 mL distilled water in the basal recipe.",
    "rationale": "The stored 900 G_PER_L is not the source mL amount. Preserve the water volume, separate from the carbonate-stock dose; no density conversion is supported.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 900,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q8",
    "component_or_context": "Carbonate solution receiving dose",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        },
        "decision": "correct"
      }
    ],
    "proposed_source_representation": "100 mL of the named 10% Na2CO3 solution in the provider recipe.",
    "rationale": "The stored 100 G_PER_L confuses a stock dose with a mass concentration. The provider declares a nominal litre from 900+100 mL inputs; solute displacement or measured final volume is not independently documented.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"10% Na2CO3 solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"attribute\": \"10%\",\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  },
  {
    "quantity_id": "q9",
    "component_or_context": "Carbonate stock strength and percent basis",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "10% Na2CO3 solution",
        "decision": "evidence_only"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "solutions[0].preferred_term",
        "stored": "10% Na2CO3 solution",
        "decision": "evidence_only"
      }
    ],
    "proposed_source_representation": "Retain 10% Na2CO3 as an unqualified stock-strength statement; percentage basis remains unspecified.",
    "rationale": "The 10% descriptor already exists in the preferred name, without attached evidence. Do not infer PERCENT_W_V, a stock mass recipe or a final carbonate g/L from this unqualified percentage. Resolve the Unknown solution placeholder using the existing name, not an unrelated stock ID.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"10% Na2CO3 solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      }
    ]
  },
  {
    "quantity_id": "q10",
    "component_or_context": "Approximate final pH",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "ph_value",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add"
      }
    ],
    "proposed_source_representation": "Approximately pH 10.0 after adding the separately filter-sterilized carbonate stock.",
    "rationale": "The current layers lack both the pH field and preparation text. This is an explicit provider claim, not independently verified primary evidence. Preserve the approximate qualifier and final-stage scope; no uncaptured basal sterilization cycle is inferred.",
    "source_snippets": [
      {
        "source_key": "togoM90",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90",
        "source_locator": "$.comments[0].comment",
        "exact_source_quote": "Separately sterilize Na2CO3 solution by filtration, and aseptically add to the medium. Check final pH to be about 10.0.",
        "snapshot_sha256": "523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75"
      },
      {
        "source_key": "mediadiveJ98api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J98",
        "source_locator": "$.data.solutions[0].steps[0].step",
        "exact_source_quote": "Separately sterilize Na2CO3 solution by filtration, and aseptically add to the medium. Check final pH to be about 10.0.",
        "snapshot_sha256": "14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988"
      }
    ]
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:010329.

5 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 5/7 primary and 4/7 secondary instances; all asserted secondary keys have exact pinned MIM rows. Unsupported source specificity is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 7: primary 71.43%; secondary 57.14%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Exact accession, stable identity and maintained ownership

identity: supported. Targets: CultureMech:010329.

CM010329 has one exact normalized TOGO M90 owner and a matching generated merge event. M90 and MediaDive J98 explicitly identify JCM98, but the exact JCM page is empty. Accession correspondence is supported by providers; primary formulation confirmation remains unavailable.

### Claim-level evidence and provider/primary scope

evidence: concern. Targets: CultureMech:010329.

Import URLs and history are provenance, not attached ingredient evidence. Every listed local concentration is covered in the inventory with literal source text, exact locators, original units and scope. Source availability and scientific correctness are assessed separately.

### Preparation stages and missing source conditions

completeness: concern. Targets: CultureMech:010329.

Both current layers omit the provider instruction to filter-sterilize the carbonate solution separately, add it aseptically and check the final pH at about 10.0. Recover those provider-supported claims with their provenance. Do not invent a basal sterilization cycle from another JCM page or assume a percent basis.

### Composition and physical-state classification

scope: supported. Targets: CultureMech:010329.

Provider yeast extract and Polypepton support COMPLEX/UNDEFINED, while 15 g agar supports SOLID_AGAR. Generic cultivation application is contextual only. The unavailable primary limits confirmation, not the existence of the provider formulation.

### Supplied forms and limits of chemical specificity

grounding: concern. Targets: CultureMech:010329.

MgSO4·7H2O matches CHEBI:31795 heptahydrate. Generic Lactose is mapped in both layers to CHEBI:36218, explicitly the beta-anomer; its valid label and synonym LACTOSE do not establish source anomer specificity. Retain the written Nihon Pharm. Co. supplier wording without equating another supplier/catalog. No unsupported replacement identifier or hydrate-dependent conversion is proposed.

### Growth, taxonomy and graph claim scope

scope: not_applicable. Targets: CultureMech:010329.

No experimental growth assertion or target-organism evidence is present. The medium title, generic application and provider context do not establish a strain phenotype, current taxonomy identifier or graph membership. No unrelated organism evidence is transferred.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010329.

23 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Current writers and authoritative correction path

provenance: concern. Targets: CultureMech:010329.

Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path.

## Findings

### f1: Water and carbonate-stock volumes use mass-concentration units

major / open / confirmed; issue key: water-stock-volume.

Both layers encode 900 mL water and 100 mL of 10% sodium carbonate solution as 900 and 100 G_PER_L. The stock composition is empty and its name placeholder obscures a source-named solution. Neither source states the percentage basis needed for a mass conversion.

### f2: Separate stock filtration and approximate final pH are omitted

major / open / confirmed; issue key: missing-provider-preparation.

TOGO and MediaDive retain a carbonate-specific filtration/addition instruction and approximate final pH 10.0, but neither local layer has preparation_steps or ph_value. The unavailable JCM primary must not be reported as verified support for these claims.

### f3: The lactose mapping claims an unsupported beta-anomer

minor / open / confirmed; issue key: lactose-anomer-specificity.

Both providers name Lactose without specifying the reducing-end anomer. CHEBI:36218 resolves correctly to beta-lactose, with a beta-specific definition and stereochemical representation. Identifier validity and a generic synonym do not establish that this source uses the beta-anomer.

## Recommended Actions And Acceptance Checks

### a1

Correct the maintained owner to preserve 900 mL basal water and 100 mL of the named 10% carbonate solution, attach exact provider evidence and explicitly retain the unknown percent basis. Avoid inventing a carbonate stock mass recipe or density; regenerate after authorized owner correction.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Add the exact provider-supported preparation and approximate final-pH qualifier with transparent secondary provenance; keep the required primary confirmation open. Do not supply an unobserved basal sterilization temperature or duration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Preserve the generic source name and record the unresolved anomer specification. Obtain exact primary/product evidence before affirming a specific anomer or choosing an alternative identifier; any eventual primary/secondary grounding change must be consistent and evidenced.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch021/210/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch021/210/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml:1:id: CultureMech:010329<br>./data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml:1:id: CultureMech:010329<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch021/source-preflight-bound/210/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 8 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90; meta; components[0]; comments[0] | supports | TOGO M90 explicitly identifies JCM_M98, six basal masses, 900 mL water and 100 mL of 10% carbonate solution; it retains filtration and approximate final pH 10.0. Percent basis is unspecified. |
| mediadive | https://mediadive.dsmz.de/rest/medium/J98; data.medium; main solution 3728, recipe and steps | supports | MediaDive J98 declares 1000 mL and corroborates the provider amounts and preparation text. Corroborating secondary records do not recover the missing primary formulation. |
| jcm98-attempt | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=98; Preserved exact public retrieval result | context_only | The exact cited JCM98 page returned HTTP 200 with Nothing found. The required primary formulation/conditions check is unavailable despite successful transport. TOGO M90 and MediaDive J98 support a bounded secondary-source comparison; no alternate accession or uncaptured primary text is substituted. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch021/210/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi36218 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36218; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:36218 resolves to beta-lactose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:36218": [{"label": "Beta-Lactose", "match_type": "preferred_term", "identifier": "CHEBI:36218", "preferred_term": "Beta-Lactose", "ontology_id": "CHEBI:36218", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 12, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml", "events": 11, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |
| writer-3 | src/culturemech/validation/schema_defaulter.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current TOGO code separates primary and local solution sections, retains comments, maps ml to ML_PER_L and can normalize local batches from liquid/water anchors; those anchors are not measured final volumes. Its bare percent mapping does not independently establish a w/v source basis. Current cleanup no longer sums disagreeing duplicates. The solution migrator resolves generic solution names from a global name index; name equality alone is insufficient source identity. Defaults supply variable values and Unknown solution names without scientific evidence. These current functions do not prove which historical execution produced the stored values. Correct the maintained owner with exact evidence, preserve old events and append clarification, then regenerate through the normal path. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The exact cited JCM98 page returned HTTP 200 with Nothing found. The required primary formulation/conditions check is unavailable despite successful transport. TOGO M90 and MediaDive J98 support a bounded secondary-source comparison; no alternate accession or uncaptured primary text is substituted.
- The fresh inspection inputs and exact per-record bound catalog are authoritative. Captures retain original retrieval timestamps and hashes; preflight observations do not replace the current source comparisons. No recipe or saved review has been edited.
- Partial completion rests on the required exact JCM98 formulation check being unavailable. Current OLS and pinned CHEBI-based MIM lookups completed successfully; their valid metadata do not recover the primary source or prove lactose anomer specificity.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124632Z-culturemech-010329-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaline_lactose_agar (CultureMech:010329)'
started_at: '2026-10-21T12:39:27Z'
finished_at: '2026-10-21T12:46:32Z'
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
summary: The local TOGO M90 record agrees with the available provider basal masses
  but changes water and carbonate-stock volumes into mass concentrations, omits provider
  preparation, and overstates lactose anomer specificity. Exact JCM98 retrieval returns
  no formulation, so primary confirmation remains unavailable and this scientific
  review is partial.
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
  - path: data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
    sha256: b388eec288ccecde5dddc6d9239e71e9f7bd8bf021c1983ffc97486176375dfb
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
    sha256: a07065d051fea673906ddd5093147a83a333319eb0c7e5e265d3eab24d73d05e
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
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 210; batch 021 item 10 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty task batches contain
    200 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 203 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010329
targets:
- target_id: CultureMech:010329
  path: data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  label: alkaline_lactose_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/210/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/210/strict.tsv"
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010329
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
  - CultureMech:010329
- check_id: jcm98-source-access
  name: 'Exact source content access: jcm98'
  required: true
  status: unavailable
  summary: The exact cited JCM98 page returned HTTP 200 with Nothing found. The required
    primary formulation/conditions check is unavailable despite successful transport.
    TOGO M90 and MediaDive J98 support a bounded secondary-source comparison; no alternate
    accession or uncaptured primary text is substituted.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - jcm98-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:54.915848Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch021/210/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:56.729310Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-021/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch021/210/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:58.713861Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T12:40:59.879004Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T12:46:29Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml:1:id:
    CultureMech:010329

    ./data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml:1:id: CultureMech:010329

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/source-preflight-bound/210/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T12:46:29Z'
  support: supports
  summary: 8 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 19fffe7428791cc736428d1fd941b658ef0d36f1110fa8cc1df7a8f01ddcdcad
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90
  locator: meta; components[0]; comments[0]
  accessed_at: '2026-10-21T12:23:42.733911Z'
  support: supports
  summary: TOGO M90 explicitly identifies JCM_M98, six basal masses, 900 mL water
    and 100 mL of 10% carbonate solution; it retains filtration and approximate final
    pH 10.0. Percent basis is unspecified.
  snapshot_sha256: 523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75
- evidence_id: mediadive
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J98
  locator: data.medium; main solution 3728, recipe and steps
  accessed_at: '2026-10-21T12:23:42.204720Z'
  support: supports
  summary: MediaDive J98 declares 1000 mL and corroborates the provider amounts and
    preparation text. Corroborating secondary records do not recover the missing primary
    formulation.
  snapshot_sha256: 14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988
- evidence_id: jcm98-attempt
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=98
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T12:23:44.853970Z'
  support: context_only
  summary: The exact cited JCM98 page returned HTTP 200 with Nothing found. The required
    primary formulation/conditions check is unavailable despite successful transport.
    TOGO M90 and MediaDive J98 support a bounded secondary-source comparison; no alternate
    accession or uncaptured primary text is substituted.
  snapshot_sha256: c02cc440b99b89e2e1661b4dbf45cb8e36b797aadc789da0d559dc9ab3bac38a
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch021/210/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: d5dc55f99e88afbcc3913232d98056c8673736420481e150321dada95e675701
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
- evidence_id: chebi36218
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36218
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T12:23:43.383673Z'
  support: supports
  summary: CHEBI:36218 resolves to beta-lactose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 035843f597328dd74de030d9544c56ace7ec50d56d1b990b17b561c7f200e4b3
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T12:46:29Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:36218": [{"label": "Beta-Lactose", "match_type":
    "preferred_term", "identifier": "CHEBI:36218", "preferred_term": "Beta-Lactose",
    "ontology_id": "CHEBI:36218", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml; data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: '[{"input": "target", "events": 12, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml", "events":
    11, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T12:46:29Z'
  support: context_only
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010329
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
  - CultureMech:010329
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"component_or_context\": \"\
    MgSO4・7H2O basal mass\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\",\n  \
    \      \"field_path\": \"ingredients[1].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"0.2 g per provider recipe; the current g/L value matches the provider's declared\
    \ nominal 1000 mL basis.\",\n    \"rationale\": \"No attached quantity evidence\
    \ exists in either layer. Preserve the literal source mass and provider nominal-volume\
    \ basis rather than asserting measured final volume. The supplied name/grade remains\
    \ as written; no alternate commercial product is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MgSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 8,\\n                        \\\"amount\\\": 0.2,\\n                     \
    \   \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n  \
    \                      \\\"mmol_l\\\": 0.811438,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"component_or_context\"\
    : \"Yeast extract basal mass\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\",\n  \
    \      \"field_path\": \"ingredients[2].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g per provider recipe; the current g/L value matches the provider's declared\
    \ nominal 1000 mL basis.\",\n    \"rationale\": \"No attached quantity evidence\
    \ exists in either layer. Preserve the literal source mass and provider nominal-volume\
    \ basis rather than asserting measured final volume. The supplied name/grade remains\
    \ as written; no alternate commercial product is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n     \
    \                   \\\"optional\\\": 0\\n                    }\",\n        \"\
    snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q3\",\n    \"component_or_context\"\
    : \"K2HPO4 basal mass\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\",\n  \
    \      \"field_path\": \"ingredients[3].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"1 g per provider recipe; the current g/L value matches the provider's declared\
    \ nominal 1000 mL basis.\",\n    \"rationale\": \"No attached quantity evidence\
    \ exists in either layer. Preserve the literal source mass and provider nominal-volume\
    \ basis rather than asserting measured final volume. The supplied name/grade remains\
    \ as written; no alternate commercial product is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 1,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 1,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n                  \
    \      \\\"mmol_l\\\": 5.74132,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q4\",\n    \"component_or_context\"\
    : \"Lactose basal mass\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\",\n  \
    \      \"field_path\": \"ingredients[4].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g per provider recipe; the current g/L value matches the provider's declared\
    \ nominal 1000 mL basis.\",\n    \"rationale\": \"No attached quantity evidence\
    \ exists in either layer. Preserve the literal source mass and provider nominal-volume\
    \ basis rather than asserting measured final volume. The amount is supported,\
    \ but the provider generic Lactose name does not establish beta-anomer identity.\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM90\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lactose\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Lactose\\\",\\n                        \\\"compound_id\\\":\
    \ 394,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n      \
    \                  \\\"mmol_l\\\": 14.6071,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q5\",\n    \"component_or_context\"\
    : \"Agar basal mass\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\",\n  \
    \      \"field_path\": \"ingredients[5].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"15 g per provider recipe; the current g/L value matches the provider's declared\
    \ nominal 1000 mL basis.\",\n    \"rationale\": \"No attached quantity evidence\
    \ exists in either layer. Preserve the literal source mass and provider nominal-volume\
    \ basis rather than asserting measured final volume. The supplied name/grade remains\
    \ as written; no alternate commercial product is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 15,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Agar\\\",\\n                        \\\"compound_id\\\": 3,\\\
    n                        \\\"amount\\\": 15,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 15,\\n                 \
    \       \\\"mmol_l\\\": 44.5991,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"component_or_context\"\
    : \"Polypepton (Nihon Pharm. Co.) basal mass\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\",\n  \
    \      \"field_path\": \"ingredients[6].concentration\",\n        \"stored\":\
    \ {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"evidence_only\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"5 g per provider recipe; the current g/L value matches the provider's declared\
    \ nominal 1000 mL basis.\",\n    \"rationale\": \"No attached quantity evidence\
    \ exists in either layer. Preserve the literal source mass and provider nominal-volume\
    \ basis rather than asserting measured final volume. The supplied name/grade remains\
    \ as written; no alternate commercial product is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Polypepton (Nihon Pharm. Co.)\\\",\\n        \
    \  \\\"volume\\\": 5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Polypeptone\\\",\\n                        \\\"compound_id\\\
    \": 442,\\n                        \\\"attribute\\\": \\\"Nihon Pharm. Co.\\\"\
    ,\\n                        \\\"amount\\\": 5,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 5,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q7\",\n    \"component_or_context\"\
    : \"Basal water\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"900 mL distilled water in the basal recipe.\",\n    \"rationale\": \"The stored\
    \ 900 G_PER_L is not the source mL amount. Preserve the water volume, separate\
    \ from the carbonate-stock dose; no density conversion is supported.\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"togoM90\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 900,\\n                     \
    \   \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"component_or_context\"\
    : \"Carbonate solution receiving dose\",\n    \"decision\": \"correct\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"100 mL of the named 10% Na2CO3 solution in the provider recipe.\",\n    \"\
    rationale\": \"The stored 100 G_PER_L confuses a stock dose with a mass concentration.\
    \ The provider declares a nominal litre from 900+100 mL inputs; solute displacement\
    \ or measured final volume is not independently documented.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% Na2CO3 solution\\\",\\n          \\\"volume\\\
    \": 100,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\"\
    : 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2CO3\\\",\\n                        \\\"compound_id\\\": 32,\\\
    n                        \\\"attribute\\\": \\\"10%\\\",\\n                  \
    \      \\\"amount\\\": 100,\\n                        \\\"unit\\\": \\\"ml\\\"\
    ,\\n                        \\\"optional\\\": 0\\n                    }\",\n \
    \       \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"component_or_context\"\
    : \"Carbonate stock strength and percent basis\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preferred_term\",\n        \"stored\"\
    : \"10% Na2CO3 solution\",\n        \"decision\": \"evidence_only\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preferred_term\",\n        \"stored\"\
    : \"10% Na2CO3 solution\",\n        \"decision\": \"evidence_only\"\n      }\n\
    \    ],\n    \"proposed_source_representation\": \"Retain 10% Na2CO3 as an unqualified\
    \ stock-strength statement; percentage basis remains unspecified.\",\n    \"rationale\"\
    : \"The 10% descriptor already exists in the preferred name, without attached\
    \ evidence. Do not infer PERCENT_W_V, a stock mass recipe or a final carbonate\
    \ g/L from this unqualified percentage. Resolve the Unknown solution placeholder\
    \ using the existing name, not an unrelated stock ID.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"10% Na2CO3 solution\\\",\\n          \\\"volume\\\
    \": 100,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\"\
    : 10,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\n     \
    \ }\n    ]\n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"component_or_context\"\
    : \"Approximate final pH\",\n    \"decision\": \"add\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null,\n        \"\
    decision\": \"add\"\n      },\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALINE_LACTOSE_AGAR.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\"\n      }\n    ],\n    \"proposed_source_representation\"\
    : \"Approximately pH 10.0 after adding the separately filter-sterilized carbonate\
    \ stock.\",\n    \"rationale\": \"The current layers lack both the pH field and\
    \ preparation text. This is an explicit provider claim, not independently verified\
    \ primary evidence. Preserve the approximate qualifier and final-stage scope;\
    \ no uncaptured basal sterilization cycle is inferred.\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM90\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M90\",\n      \
    \  \"source_locator\": \"$.comments[0].comment\",\n        \"exact_source_quote\"\
    : \"Separately sterilize Na2CO3 solution by filtration, and aseptically add to\
    \ the medium. Check final pH to be about 10.0.\",\n        \"snapshot_sha256\"\
    : \"523df9531c21bde7d3269da60bb0e63957b93a6e679436db1db1ae613b99bf75\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ98api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J98\",\n        \"source_locator\":\
    \ \"$.data.solutions[0].steps[0].step\",\n        \"exact_source_quote\": \"Separately\
    \ sterilize Na2CO3 solution by filtration, and aseptically add to the medium.\
    \ Check final pH to be about 10.0.\",\n        \"snapshot_sha256\": \"14fb9c22ecb0468ac62e2777b2c08e777d75a409fff3659b4906e096fb201988\"\
    \n      }\n    ]\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '5 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 5/7 primary and 4/7 secondary
    instances; all asserted secondary keys have exact pinned MIM rows. Unsupported
    source specificity is addressed separately; valid IDs and labels do not establish
    correct source grounding.'
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi2509
  - chebi31795
  - chebi36218
  details: 'Instance coverage on a 0–100 percent scale, denominator 7: primary 71.43%;
    secondary 57.14%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: identity
  area: identity
  topic: Exact accession, stable identity and maintained ownership
  outcome: supported
  summary: CM010329 has one exact normalized TOGO M90 owner and a matching generated
    merge event. M90 and MediaDive J98 explicitly identify JCM98, but the exact JCM
    page is empty. Accession correspondence is supported by providers; primary formulation
    confirmation remains unavailable.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - id-search
  - owner-0
  - provider
  - mediadive
- assessment_id: source-evidence
  area: evidence
  topic: Claim-level evidence and provider/primary scope
  outcome: concern
  summary: Import URLs and history are provenance, not attached ingredient evidence.
    Every listed local concentration is covered in the inventory with literal source
    text, exact locators, original units and scope. Source availability and scientific
    correctness are assessed separately.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - quantity-inventory
  - provider
  - mediadive
- assessment_id: preparation
  area: completeness
  topic: Preparation stages and missing source conditions
  outcome: concern
  summary: Both current layers omit the provider instruction to filter-sterilize the
    carbonate solution separately, add it aseptically and check the final pH at about
    10.0. Recover those provider-supported claims with their provenance. Do not invent
    a basal sterilization cycle from another JCM page or assume a percent basis.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - quantity-inventory
  - provider
  - mediadive
- assessment_id: classification
  area: scope
  topic: Composition and physical-state classification
  outcome: supported
  summary: Provider yeast extract and Polypepton support COMPLEX/UNDEFINED, while
    15 g agar supports SOLID_AGAR. Generic cultivation application is contextual only.
    The unavailable primary limits confirmation, not the existence of the provider
    formulation.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - provider
  - mediadive
- assessment_id: forms
  area: grounding
  topic: Supplied forms and limits of chemical specificity
  outcome: concern
  summary: MgSO4·7H2O matches CHEBI:31795 heptahydrate. Generic Lactose is mapped
    in both layers to CHEBI:36218, explicitly the beta-anomer; its valid label and
    synonym LACTOSE do not establish source anomer specificity. Retain the written
    Nihon Pharm. Co. supplier wording without equating another supplier/catalog. No
    unsupported replacement identifier or hydrate-dependent conversion is proposed.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - provider
  - mediadive
- assessment_id: growth
  area: scope
  topic: Growth, taxonomy and graph claim scope
  outcome: not_applicable
  summary: No experimental growth assertion or target-organism evidence is present.
    The medium title, generic application and provider context do not establish a
    strain phenotype, current taxonomy identifier or graph membership. No unrelated
    organism evidence is transferred.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - provider
  - mediadive
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 23 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: writer
  area: provenance
  topic: Current writers and authoritative correction path
  outcome: concern
  summary: Current TOGO code separates primary and local solution sections, retains
    comments, maps ml to ML_PER_L and can normalize local batches from liquid/water
    anchors; those anchors are not measured final volumes. Its bare percent mapping
    does not independently establish a w/v source basis. Current cleanup no longer
    sums disagreeing duplicates. The solution migrator resolves generic solution names
    from a global name index; name equality alone is insufficient source identity.
    Defaults supply variable values and Unknown solution names without scientific
    evidence. These current functions do not prove which historical execution produced
    the stored values. Correct the maintained owner with exact evidence, preserve
    old events and append clarification, then regenerate through the normal path.
  target_ids:
  - CultureMech:010329
  evidence_ids:
  - record
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: water-stock-volume
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and carbonate-stock volumes use mass-concentration units
  description: Both layers encode 900 mL water and 100 mL of 10% sodium carbonate
    solution as 900 and 100 G_PER_L. The stock composition is empty and its name placeholder
    obscures a source-named solution. Neither source states the percentage basis needed
    for a mass conversion.
  target_ids:
  - CultureMech:010329
  field_paths:
  - ingredients[0].concentration
  - solutions[0]
  evidence_ids:
  - record
  - provider
  - mediadive
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
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
  issue_key: missing-provider-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Separate stock filtration and approximate final pH are omitted
  description: TOGO and MediaDive retain a carbonate-specific filtration/addition
    instruction and approximate final pH 10.0, but neither local layer has preparation_steps
    or ph_value. The unavailable JCM primary must not be reported as verified support
    for these claims.
  target_ids:
  - CultureMech:010329
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - record
  - provider
  - mediadive
  - jcm98-attempt
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: P3.5 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: lactose-anomer-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The lactose mapping claims an unsupported beta-anomer
  description: Both providers name Lactose without specifying the reducing-end anomer.
    CHEBI:36218 resolves correctly to beta-lactose, with a beta-specific definition
    and stereochemical representation. Identifier validity and a generic synonym do
    not establish that this source uses the beta-anomer.
  target_ids:
  - CultureMech:010329
  field_paths:
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - provider
  - mediadive
  - chebi36218
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
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
  description: Correct the maintained owner to preserve 900 mL basal water and 100
    mL of the named 10% carbonate solution, attach exact provider evidence and explicitly
    retain the unknown percent basis. Avoid inventing a carbonate stock mass recipe
    or density; regenerate after authorized owner correction.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
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
  description: Add the exact provider-supported preparation and approximate final-pH
    qualifier with transparent secondary provenance; keep the required primary confirmation
    open. Do not supply an unobserved basal sterilization temperature or duration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
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
  description: Preserve the generic source name and record the unresolved anomer specification.
    Obtain exact primary/product evidence before affirming a specific anomer or choosing
    an alternative identifier; any eventual primary/secondary grounding change must
    be consistent and evidenced.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010329
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M90_Alkaline_Lactose_Agar.yaml
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
- The exact cited JCM98 page returned HTTP 200 with Nothing found. The required primary
  formulation/conditions check is unavailable despite successful transport. TOGO M90
  and MediaDive J98 support a bounded secondary-source comparison; no alternate accession
  or uncaptured primary text is substituted.
- The fresh inspection inputs and exact per-record bound catalog are authoritative.
  Captures retain original retrieval timestamps and hashes; preflight observations
  do not replace the current source comparisons. No recipe or saved review has been
  edited.
- Partial completion rests on the required exact JCM98 formulation check being unavailable.
  Current OLS and pinned CHEBI-based MIM lookups completed successfully; their valid
  metadata do not recover the primary source or prove lactose anomer specificity.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-021
- generated-medium
```
