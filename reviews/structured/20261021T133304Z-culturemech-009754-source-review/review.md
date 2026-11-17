# Source and formulation review: alkaliphilus_crotonatoxidans_medium (CultureMech:009754)

- Review: 20261021T133304Z-culturemech-009754-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T13:27:09Z
- Finished UTC: 2026-10-21T13:33:04Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact TOGO M373 / JCM 378 medium is identifiable, but both local layers collapse preparation stages into unsupported mass concentrations, misstate resazurin and water units, retain five unnamed empty stock stubs, and omit material preparation. Current provider main volume 20 mL and pH 6 are incompatible with the primary main preparation. Explicit cobalt/nickel hexahydrates also have anhydrous groundings; manganese hydration remains unspecified.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 221; batch 023 item 1 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-two task batches contain 220 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 223 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009754 | data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml | generated | alkaliphilus_crotonatoxidans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009754 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009754 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/221/strict.tsv |
| validate-terms | passed | True | CultureMech:009754 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009754 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009754 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009754.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:009754.

73 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "claim": "Sol.1 addition",
    "decision": "correct",
    "stage": "TOGO assembly of main solution 1",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "900",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "900 mL Sol.1",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Sol.1\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      }
    ],
    "explanation": "The stored 900 G_PER_L is a solution volume, not an ingredient mass or final concentration."
  },
  {
    "decision_id": "q2",
    "claim": "Flattened water",
    "decision": "correct",
    "stage": "Distinct main/crotonate/metal/reductant batches",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "900 mL +100 mL +1 L +10 mL +10 mL in separate stages",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[5].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      }
    ],
    "explanation": "The stored 1021 G_PER_L improperly adds numerical amounts with heterogeneous units and separate stock-batch scope. Do not sum them as a medium volume."
  },
  {
    "decision_id": "q3",
    "claim": "NaCl main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NaCl 0.4 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "NaCl 0.4 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 342.231,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q4",
    "claim": "CaCl2・2H2O main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.05",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "CaCl 2 ·2H 2 O 0.05 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.05 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.05,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 17.0051,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q5",
    "claim": "KH2PO4 main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "KH 2 PO 4 0.5 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "KH 2 PO 4 0.5 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\": 183.707,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q6",
    "claim": "NH4Cl main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NH 4 Cl 0.4 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "NH 4 Cl 0.4 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 20,\n                        \"mmol_l\": 373.902,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q7",
    "claim": "Resazurin main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Resazurin 1.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Resazurin 1.0 mg",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[13]",
        "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.21816,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q8",
    "claim": "MgCl2・6H2O main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.33",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "MgCl 2 ·6H 2 O 0.33 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "MgCl 2 ·6H 2 O 0.33 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 16.5,\n                        \"mmol_l\": 81.1596,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q9",
    "claim": "NaHCO3 main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "3.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NaHCO 3 3.5 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "NaHCO 3 3.5 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"NaHCO3\",\n          \"volume\": 3.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 3.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 175,\n                        \"mmol_l\": 2083.16,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q10",
    "claim": "Yeast extract (BD-Difco) main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Yeast extract (BD-Difco) 2.0 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Yeast extract (BD-Difco) 2.0 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 100,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q11",
    "claim": "Tryptone (BD-Difco) main batch amount",
    "decision": "correct",
    "stage": "JCM378 main recipe with staged preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Tryptone (BD-Difco) 2.0 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Tryptone (BD-Difco) 2.0 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Tryptone (BD-Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 100,\n                        \"mmol_l\": 1406.87,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Preserve the original batch mass and preparation stage. Local G_PER_L is not established by an independently supported final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot repair the basis. BD-Difco product qualifications remain explicit."
  },
  {
    "decision_id": "q12",
    "claim": "Carbon dioxide gas absolute dose",
    "decision": "not_quantified",
    "stage": "Main cooling and dispensing gas atmosphere",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": "No absolute gas dose; mixture 80:20 v/v",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "N 2 -CO 2 (80:20, v/v)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Variable absolute gas amount is appropriate; it does not replace the source mixture ratio recorded separately below."
  },
  {
    "decision_id": "q13",
    "claim": "N2 absolute dose",
    "decision": "not_quantified",
    "stage": "Main cooling and dispensing gas atmosphere",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": "No absolute gas dose; mixture 80:20 v/v",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "N 2 -CO 2 (80:20, v/v)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Variable absolute gas amount is appropriate; it does not replace the source mixture ratio recorded separately below."
  },
  {
    "decision_id": "q14",
    "claim": "Crotonic acid main and stock mass",
    "decision": "correct",
    "stage": "Main table; separately prepared crotonate stock",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.86",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "0.86",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "0.86 g main table and0.86 g/100 mL stock",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Crotonic acid 0.86 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "crotonic acid solution (0.86 g/100 ml, pH 7.0)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Crotonic acid\",\n          \"volume\": 0.86,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      }
    ],
    "explanation": "The source mass and stock concentration are distinct claims. The local 0.86 G/L is not authenticated by the primary staged-volume instructions or current 20 mL provider basis; do not double-count the same contribution."
  },
  {
    "decision_id": "q15",
    "claim": "Na2MoO4・2H2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 MoO 4 ·2H 2 O 0.02 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 0.02 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0826617,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q16",
    "claim": "CoCl2・6H2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "CoCl 2 ·6H 2 O 0.2 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "CoCl 2 ·6H 2 O 0.2 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q17",
    "claim": "NiCl2・6H2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[16].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "NiCl 2 ·6H 2 O 0.02 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "NiCl 2 ·6H 2 O 0.02 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q18",
    "claim": "ZnSO4・7H2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[17].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "ZnSO 4 ·7H 2 O 0.2 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "ZnSO 4 ·7H 2 O 0.2 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[4]",
        "exact_source_quote": "\"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.695505,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q19",
    "claim": "CuCl2・2H2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[18].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "CuCl 2 ·2H 2 O 0.02 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "CuCl 2 ·2H 2 O 0.02 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[5]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.117314,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q20",
    "claim": "Nitrilotriacetic acid trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[19].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Nitrilotriacetic acid 2.0 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "Nitrilotriacetic acid 2.0 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[6]",
        "exact_source_quote": "\"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 10.4635,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q21",
    "claim": "MnSO4・xH2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[20].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "MnSO 4 · x H 2 O 1.0 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "MnSO 4 · x H 2 O 1.0 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[7]",
        "exact_source_quote": "\"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q22",
    "claim": "Fe(NH4)2(SO4)2・6H2O trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[21].concentration",
        "stored": {
          "value": "0.8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Fe(NH 4 ) 2 (SO 4 ) 2 ·6H 2 O 0.8 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "Fe(NH 4 ) 2 (SO 4 ) 2 ·6H 2 O 0.8 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[8]",
        "exact_source_quote": "\"component_name\": \"Fe(NH4)2(SO4)2・6H2O\",\n          \"volume\": 0.8,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Fe(NH4)2(SO4)2 x 6 H2O\",\n                        \"compound_id\": 247,\n                        \"amount\": 0.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.8,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q23",
    "claim": "Na2WO4 trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[22].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 WO 4 0.02 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "Na 2 WO 4 0.02 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[9]",
        "exact_source_quote": "\"component_name\": \"Na2WO4\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2WO4\",\n                        \"compound_id\": 550,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0680689,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q24",
    "claim": "Na2SeO4 trace batch amount",
    "decision": "correct",
    "stage": "Trace-metal stock,10 mL receiving addition",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[23].concentration",
        "stored": {
          "value": "0.02",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 SeO 4 0.02 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 Trace metal solution, exact ingredient",
        "exact_source_quote": "Na 2 SeO 4 0.02 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[10]",
        "exact_source_quote": "\"component_name\": \"Na2SeO4\",\n          \"volume\": 0.02,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[1].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Na2SeO4\",\n                        \"compound_id\": 375,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.105848,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "The source stock batch amount/provider stock rate is exposed as a direct receiving-medium concentration. Reconstruct the stock and its dose without inferring final medium volume. Preserve explicit hydrate form and unspecified manganese hydrate count."
  },
  {
    "decision_id": "q25",
    "claim": "KOH titrant",
    "decision": "correct",
    "stage": "Trace-metal stock only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[24].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_amount": "Unquantified KOH to stock pH 6.0",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Adjust pH to 6.0 with KOH.",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "No fixed dose or strength is supplied. Keep unknown quantity, but move the direct-medium assertion into the trace-stock context."
  },
  {
    "decision_id": "q26",
    "claim": "L--Cysteine・HCL・H2O contribution",
    "decision": "correct",
    "stage": "Separately prepared reductant added to main",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[25].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "L-Cysteine·HCL·H 2 O 0.5 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "L-Cysteine·HCL·H 2 O 0.5 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[4].items[1]",
        "exact_source_quote": "\"component_name\": \"L--Cysteine・HCL・H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[11]",
        "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 25,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Primary gives 0.5 g batch contribution and a separate 5% stock instruction; TOGO gives 0.5 g in 10 mL water. None independently establishes the local final-medium g/L denominator."
  },
  {
    "decision_id": "q27",
    "claim": "Na2S・9H2O contribution",
    "decision": "correct",
    "stage": "Separately prepared reductant added to main",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[26].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Na 2 S·9H 2 O 0.5 g",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Na 2 S·9H 2 O 0.5 g",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      },
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[5].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[0].recipe[12]",
        "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\": 104.088,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Primary gives 0.5 g batch contribution and a separate 5% stock instruction; TOGO gives 0.5 g in 10 mL water. None independently establishes the local final-medium g/L denominator."
  },
  {
    "decision_id": "q28",
    "claim": "Existing stock addition crotonic acid solution",
    "decision": "correct",
    "stage": "Named stock addition in its source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "100",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "100 mL",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"crotonic acid solution\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "crotonic acid solution (0.86 g/100 ml, pH 7.0)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "The existing stock stub has a mass-concentration unit and no composition. Preserve TOGO addition volume with primary fraction/stock context; do not equate mL to grams or assert per-final-liter basis."
  },
  {
    "decision_id": "q29",
    "claim": "Existing stock addition cysteine・HCl solution",
    "decision": "correct",
    "stage": "Named stock addition in its source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "10 mL",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"cysteine・HCl solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Autoclave cysteine·HCl and Na 2 S·9H 2 O as 5% solutions",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "The existing stock stub has a mass-concentration unit and no composition. Preserve TOGO addition volume with primary fraction/stock context; do not equate mL to grams or assert per-final-liter basis."
  },
  {
    "decision_id": "q30",
    "claim": "Existing stock addition Na2S・9H2O solution",
    "decision": "correct",
    "stage": "Named stock addition in its source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "10 mL",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"Na2S・9H2O solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Autoclave cysteine·HCl and Na 2 S·9H 2 O as 5% solutions",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "The existing stock stub has a mass-concentration unit and no composition. Preserve TOGO addition volume with primary fraction/stock context; do not equate mL to grams or assert per-final-liter basis."
  },
  {
    "decision_id": "q31",
    "claim": "Existing stock addition Trace metal solution (see below)",
    "decision": "correct",
    "stage": "Named stock addition in its source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "10 mL",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Trace metal solution (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Trace metal solution (see below) 10.0 ml",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "The existing stock stub has a mass-concentration unit and no composition. Preserve TOGO addition volume with primary fraction/stock context; do not equate mL to grams or assert per-final-liter basis."
  },
  {
    "decision_id": "q32",
    "claim": "Existing stock addition Trace vitamins (see Medium [M190])",
    "decision": "correct",
    "stage": "Named stock addition in its source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "10 mL",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[11]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Trace vitamins (see Medium No. 197 ) 10.0 ml",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "The existing stock stub has a mass-concentration unit and no composition. Preserve TOGO addition volume with primary fraction/stock context; do not equate mL to grams or assert per-final-liter basis."
  },
  {
    "decision_id": "q33",
    "claim": "basal water batch input",
    "decision": "correct",
    "stage": "basal stock/main preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Source-specific water volume",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 900,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "in 900 ml of distilled water",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Each water input has its own preparation stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry are retained separately; no measured final-volume inference."
  },
  {
    "decision_id": "q34",
    "claim": "crotonate water batch input",
    "decision": "correct",
    "stage": "crotonate stock/main preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Source-specific water volume",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "crotonic acid solution (0.86 g/100 ml, pH 7.0)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Each water input has its own preparation stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry are retained separately; no measured final-volume inference."
  },
  {
    "decision_id": "q35",
    "claim": "trace metal water batch input",
    "decision": "correct",
    "stage": "trace metal stock/main preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Source-specific water volume",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      },
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Each water input has its own preparation stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry are retained separately; no measured final-volume inference."
  },
  {
    "decision_id": "q36",
    "claim": "cysteine water batch input",
    "decision": "correct",
    "stage": "cysteine stock/main preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Source-specific water volume",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[4].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      }
    ],
    "explanation": "Each water input has its own preparation stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry are retained separately; no measured final-volume inference."
  },
  {
    "decision_id": "q37",
    "claim": "sulfide water batch input",
    "decision": "correct",
    "stage": "sulfide stock/main preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1021.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_amount": "Source-specific water volume",
    "source_snippets": [
      {
        "source_key": "togoM373",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373",
        "source_locator": "$.components[5].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad"
      }
    ],
    "explanation": "Each water input has its own preparation stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry are retained separately; no measured final-volume inference."
  },
  {
    "decision_id": "q38",
    "claim": "Transferred vitamin stock Distilled water",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Distilled water 1.0 L",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q39",
    "claim": "Existing dependency vitamin batch claim 0",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        }
      }
    ],
    "source_amount": "Distilled water 1.0 L",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[10]",
        "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q40",
    "claim": "Transferred vitamin stock Biotin",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Biotin 2.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Biotin 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q41",
    "claim": "Existing dependency vitamin batch claim 1",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Biotin 2.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Biotin 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q42",
    "claim": "Transferred vitamin stock p--Aminobenzoic acid",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "p -Aminobenzoic acid 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "p -Aminobenzoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q43",
    "claim": "Existing dependency vitamin batch claim 2",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "p -Aminobenzoic acid 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "p -Aminobenzoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[8]",
        "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q44",
    "claim": "Transferred vitamin stock Thiamine・HCl",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Thiamine·HCl 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Thiamine·HCl 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q45",
    "claim": "Existing dependency vitamin batch claim 3",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Thiamine·HCl 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Thiamine·HCl 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q46",
    "claim": "Transferred vitamin stock Calcium pantothenate",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Calcium pantothenate 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Calcium pantothenate 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q47",
    "claim": "Existing dependency vitamin batch claim 4",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Calcium pantothenate 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Calcium pantothenate 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q48",
    "claim": "Transferred vitamin stock Pyridoxine・HCl",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Pyridoxine·HCl 10.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Pyridoxine·HCl 10.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q49",
    "claim": "Existing dependency vitamin batch claim 5",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Pyridoxine·HCl 10.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Pyridoxine·HCl 10.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q50",
    "claim": "Transferred vitamin stock Folic acid",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Folic acid 2.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Folic acid 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q51",
    "claim": "Existing dependency vitamin batch claim 6",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Folic acid 2.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Folic acid 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q52",
    "claim": "Transferred vitamin stock Vitamin B12",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Vitamin B 1 2 0.1 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Vitamin B 1 2 0.1 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q53",
    "claim": "Existing dependency vitamin batch claim 7",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Vitamin B 1 2 0.1 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Vitamin B 1 2 0.1 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[7]",
        "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q54",
    "claim": "Transferred vitamin stock Riboflavin",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Riboflavin 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Riboflavin 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q55",
    "claim": "Existing dependency vitamin batch claim 8",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[8].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Riboflavin 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Riboflavin 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q56",
    "claim": "Transferred vitamin stock Nicotinic acid",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Nicotinic acid 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Nicotinic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q57",
    "claim": "Existing dependency vitamin batch claim 9",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[9].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Nicotinic acid 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Nicotinic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q58",
    "claim": "Transferred vitamin stock Lipoic acid",
    "decision": "add",
    "stage": "JCM197 trace-vitamin stock only, receiving addition 10 mL",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_amount": "Lipoic acid 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Lipoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Source-only batch composition is absent from target/owner stock stub. No parent basal/mineral/reductant content or specific stereochemical grounding is inherited."
  },
  {
    "decision_id": "q59",
    "claim": "Existing dependency vitamin batch claim 10",
    "decision": "verified",
    "stage": "Context dependency only; not inherited as target evidence",
    "local_fields": [
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[10].notes",
        "stored": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."
      }
    ],
    "source_amount": "Lipoic acid 5.0 mg",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "JCM197 Trace vitamins subsection, exact ingredient",
        "exact_source_quote": "Lipoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      },
      {
        "source_key": "mediadiveJ378api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J378",
        "source_locator": "$.data.solutions[2].recipe[9]",
        "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f"
      }
    ],
    "explanation": "Exact same-layer attached source snippet and claimed response hash match current capture; original date retained. For solutes only the source batch-mass notes are verified, not an absent concentration or the chemical grounding."
  },
  {
    "decision_id": "q60",
    "claim": "Initial main pH",
    "decision": "add",
    "stage": "Initial main pH source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "ph_range",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "ph_range",
        "stored": null
      }
    ],
    "source_amount": "7.0–7.5",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "adjust pH to 7.0-7.5.",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q61",
    "claim": "Brief boil duration",
    "decision": "add",
    "stage": "Brief boil duration source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "5–10 sec",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Bring to a boil for 5-10 sec",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q62",
    "claim": "Main cooling/dispensing gas ratio",
    "decision": "add",
    "stage": "Main cooling/dispensing gas ratio source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "80:20 v/v",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "N 2 -CO 2 (80:20, v/v)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q63",
    "claim": "Basal dispensing fraction",
    "decision": "add",
    "stage": "Basal dispensing fraction source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "0.9 volume",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Dispense 0.9 volume of the medium",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q64",
    "claim": "Crotonate addition fraction",
    "decision": "add",
    "stage": "Crotonate addition fraction source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "0.1 volume",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Add 0.1 volume of a filter-sterilized crotonic acid solution",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q65",
    "claim": "Crotonate stock strength",
    "decision": "add",
    "stage": "Crotonate stock strength source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_amount": "0.86 g/100 mL",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "crotonic acid solution (0.86 g/100 ml, pH 7.0)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q66",
    "claim": "Crotonate stock pH",
    "decision": "add",
    "stage": "Crotonate stock pH source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[0].preparation_notes",
        "stored": null
      }
    ],
    "source_amount": "7.0",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "crotonic acid solution (0.86 g/100 ml, pH 7.0)",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q67",
    "claim": "Cysteine stock percentage",
    "decision": "add",
    "stage": "Cysteine stock percentage source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[1].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[1].preparation_notes",
        "stored": null
      }
    ],
    "source_amount": "5%, basis unstated",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Autoclave cysteine·HCl and Na 2 S·9H 2 O as 5% solutions",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q68",
    "claim": "Sulfide stock percentage",
    "decision": "add",
    "stage": "Sulfide stock percentage source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[2].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[2].preparation_notes",
        "stored": null
      }
    ],
    "source_amount": "5%, basis unstated",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Autoclave cysteine·HCl and Na 2 S·9H 2 O as 5% solutions",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q69",
    "claim": "Trace stock pH",
    "decision": "add",
    "stage": "Trace stock pH source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[3].preparation_notes",
        "stored": null
      }
    ],
    "source_amount": "6.0",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Adjust pH to 6.0 with KOH.",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q70",
    "claim": "Autoclave temperature",
    "decision": "add",
    "stage": "Autoclave temperature source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_amount": "121°C",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q71",
    "claim": "Autoclave duration",
    "decision": "add",
    "stage": "Autoclave duration source stage",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_amount": "15 min",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Retain the exact qualified source instruction. No incubation setting, measured final volume, unstated percentage basis or parent-medium condition is inferred."
  },
  {
    "decision_id": "q72",
    "claim": "Reductant-stock N2 atmosphere",
    "decision": "add",
    "stage": "Separately autoclaved reductant stocks",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_amount": "N2 atmosphere; purity not numerically specified",
    "source_snippets": [
      {
        "source_key": "jcm378",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378",
        "source_locator": "JCM378 exact ingredient or preparation sentence",
        "exact_source_quote": "as 5% solutions, respectively, under a N 2 atmosphere.",
        "snapshot_sha256": "ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029",
        "parsed_text_sha256": "9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e"
      }
    ],
    "explanation": "Do not rewrite source N2 as a numerical 100% purity claim."
  },
  {
    "decision_id": "q73",
    "claim": "Trace-vitamin stock filtration atmosphere",
    "decision": "add",
    "stage": "JCM197 vitamin-specific filtration only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml",
        "field_path": "solutions[4].preparation_notes",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
        "field_path": "solutions[4].preparation_notes",
        "stored": null
      }
    ],
    "source_amount": "Filter sterilization while gassing with N2",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Vitamin-specific preparation clause",
        "exact_source_quote": "Trace vitamins while gassing       with N 2 .",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      }
    ],
    "explanation": "Transfer only the instruction explicitly about the referenced vitamin stock; no parent medium gas mixture or final pH is transferred."
  }
]

### Asserted ontology and pinned secondary identifier metadata

grounding: concern. Targets: CultureMech:009754.

24 distinct asserted primary/secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 24/27 primary and 11/27 secondary instances; all asserted CHEBI-keyed secondary IDs have exact pinned MIM rows; no legacy MIM identifier is asserted in the target or maintained owner. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 27: primary 88.89%; secondary 40.74%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:009754.

27 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact accession, stocks and maintained owner

identity: supported. Targets: CultureMech:009754.

CM009754 resolves to one exact maintained M373 contributor and current JCM378. M190 explicitly maps to JCM197; only its trace-vitamin recipe transfers. Stock endpoints 4104/3861 agree with their named provider subsections. No formula fingerprint establishes whole-parent equivalence.

### Mixtures, products, preparation and growth scope

scope: supported. Targets: CultureMech:009754.

Complex/undefined follows BD-Difco yeast extract and tryptone; liquid is consistent with the absence of gelling ingredient. Source role/property annotations are not independent organism-growth claims. No strain assertion or specific growth optimum is inferred. Source salt/hydrate forms are assessed independently of label validity.

### Authoritative fixes and generated correspondence

ownership: supported. Targets: CultureMech:009754.

Both target and maintained M373 owner share the identified quantity, empty-stock and preparation gaps. The separately repaired M190 dependency is context and must not be treated as a second reviewed target. Correct maintained inputs only after source-scoped curation; preserve append-only history and regenerate separately.

## Findings

### f1: Preparation stages collapse into an incoherent direct formulation

blocker / open / confirmed; issue key: cm009754-stock-flattening.

Both layers expose stock strengths and solution additions as direct G_PER_L amounts, combine water from unrelated stages with mixed units, and retain five unnamed empty stock stubs. The result does not faithfully denote the complete staged JCM378 recipe. Source trace-vitamin composition is entirely absent.

### f2: Resazurin has the wrong mass unit and basis

major / open / confirmed; issue key: cm009754-resazurin-unit.

Both layers store 1 G_PER_L while both primary and TOGO state 1 mg for the receiving batch. Current provider 0.05 g/L derives from an inconsistent 20 mL basis and is not a supported replacement.

### f3: Explicit cobalt and nickel hexahydrates use anhydrous IDs

major / open / confirmed; issue key: cm009754-supplied-forms.

Source CoCl2·6H2O and NiCl2·6H2O are grounded to anhydrous CHEBI35696/34887. Manganese is source xH2O with unspecified count, while its generic anhydrous term loses that qualification; do not select a presumed hydrate. Amounts remain source masses.

### f4: Material staged preparation is absent

major / open / confirmed; issue key: cm009754-preparation.

Neither layer retains primary pH stages, gas composition, brief boil, 0.9/0.1 dispensing, overnight stand, crotonate filtration, separately autoclaved reductant stocks or displayed sterilization default. Main pH must not be replaced by provider trace pH 6.

### f5: Source accession notes do not authenticate individual quantities

minor / open / confirmed; issue key: cm009754-quantity-evidence.

Target and maintained owner have no attached claim-level quantity evidence. Current provider metadata contain a 20 mL normalization artifact and tracepH contamination, so blind source-wide evidence would perpetuate errors. M190 evidence stays attached only to its own stock claims.

## Recommended Actions And Acceptance Checks

### a1

Restore exact source stages, stock identities, original masses/volumes and scoped compositions; remove unsupported final-medium rates rather than inventing a final denominator.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Retain exact 1 mg batch input with source stage; establish a legitimate denominator before any final concentration claim.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve exact supplied-form identifiers where supported; preserve unspecified manganese hydration and leave unresolved specificity explicit. Recheck linked annotations independently.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add narrow primary preparation and explicit stock exceptions, including vitamin-specific filtration. Keep default autoclaving separate from filtration and never infer unspecified dose, purity or percentage basis.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach exact primary/provider snippets to each corrected or retained claim, explicitly preserving source conflicts and original access/version metadata.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch023/221/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch023/221/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml:1:id: CultureMech:009754<br>./data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml:1:id: CultureMech:009754<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/221/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 48 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| bound-context | /private/tmp/culturemech-review-work-batch023/source-preflight-bound/221/evidence-context-original.json; Complete frozen source context compared with fresh native input hashes | context_only | Every contextual input hash matches the fresh inspection at the same base. Preflight remains provisional provenance; this review supplies its own single-target judgment. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378; Entire exact medium 378 page and trace-metal subsection | supports | Primary original masses, two trace additions, staged 900 mL preparation,0.9/0.1 volumes, separate 5% reductant stocks, primary pH 7.0–7.5 and trace pH 6.0 are distinct. Displayed 121°C 15 min default applies except stated filtration. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373; meta; all six component groups and all comments | supports | M373 explicitly names JCM378. TOGO retains Sol.1 and separate crotonate/reductant stock batches, unlike the local flattened record. |
| provider | https://mediadive.dsmz.de/rest/medium/J378; data.medium; solutions 4103/4104/3861, all recipe and step rows | supports | The main declared volume 20 mL produces unsupported rates such as 2 g YE -&gt;100 g/L, while its procedure specifies 900 mL water and0.9/0.1 staging. Root pH 6 is trace-stock pH. These provider artifacts are preserved as conflicts, not adopted. |
| vitamin-primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only; vitamin-specific filtration statement | supports | Only the ten-solute trace-vitamin batch and 1 L water transfer from the cross-reference. Other JCM197 medium/mineral/reductant formulations and final pH 6.8 do not transfer. |
| vitamin-togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; meta and components[1] only for transferred vitamin stock | supports | TOGO M190 resolves the local dependency to JCM197. Existing vitamin-row evidence is separately checked against exact bytes, original timestamps retained. |
| vitamin-provider | https://mediadive.dsmz.de/rest/medium/J197; Only trace-vitamin solution3861 | supports | Provider composition corroborates the transferred vitamin subsection; other parent solutions are excluded. |
| trace-api | https://mediadive.dsmz.de/rest/solution/4104; Exact stock 4104 endpoint | supports | Ten solutes plus 1000 mL water and trace-only pH 6 with unquantified KOH. |
| vitamin-api | https://mediadive.dsmz.de/rest/solution/3861; Exact stock 3861 endpoint | supports | Ten vitamin solutes plus 1000 mL water; provider-declared stock basis does not measure final volume. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch023/221/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32035 resolves to potassium hydroxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32139 resolves to sodium hydrogencarbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:34887 resolves to nickel dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:35696 resolves to cobalt dichloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi41131 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_41131; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:41131 resolves to crotonic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63940; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63940 resolves to sodium tungstate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:75213 resolves to sodium molybdate dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76181 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76181; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76181 resolves to ferrous ammonium sulfate hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:77775 resolves to sodium selenate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86318 resolves to copper(II) chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:91248 resolves to L-cysteine hydrochloride hydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32035": [{"label": "KOH", "match_type": "preferred_term", "identifier": "CHEBI:32035", "preferred_term": "KOH", "ontology_id": "CHEBI:32035", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:41131": [{"label": "Crotonic acid", "match_type": "preferred_term", "identifier": "CHEBI:41131", "preferred_term": "Crotonic acid", "ontology_id": "CHEBI:41131", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63940": [{"label": "Na2WO4", "match_type": "preferred_term", "identifier": "CHEBI:63940", "preferred_term": "Na2WO4", "ontology_id": "CHEBI:63940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:77775": [{"label": "Na2SeO4", "match_type": "preferred_term", "identifier": "CHEBI:77775", "preferred_term": "Na2SeO4", "ontology_id": "CHEBI:77775", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 14, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| dependency | data/normalized_yaml/bacterial/togo_medium_m190.yaml; Full current dependency read; only solutions[1] transferred; eleven exact evidence objects checked | context_only | The dependency has been maintained into separate batches and carries literal TOGO evidence. Its water 1 L and ten mass notes are independently verified in the inventory. This does not certify parent recipe identity, other stocks, or import their evidence into the target. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source conversion, stock preservation and merge boundaries are inspected context; none was executed or replayed. Historical duplicate-collapse notes describe old water/stock loss but do not prove current code would reproduce it. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source conversion, stock preservation and merge boundaries are inspected context; none was executed or replayed. Historical duplicate-collapse notes describe old water/stock loss but do not prove current code would reproduce it. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source conversion, stock preservation and merge boundaries are inspected context; none was executed or replayed. Historical duplicate-collapse notes describe old water/stock loss but do not prove current code would reproduce it. |
| writer-3 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source conversion, stock preservation and merge boundaries are inspected context; none was executed or replayed. Historical duplicate-collapse notes describe old water/stock loss but do not prove current code would reproduce it. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The intended measured final volume, unspecified 5% stock bases and manganese hydrate count are not established. Completed review means those bounded uncertainties were identified; it does not validate any guessed replacement concentration. JCM197 non-vitamin content is outside transfer scope.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133304Z-culturemech-009754-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkaliphilus_crotonatoxidans_medium (CultureMech:009754)'
started_at: '2026-10-21T13:27:09Z'
finished_at: '2026-10-21T13:33:04Z'
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
summary: The exact TOGO M373 / JCM 378 medium is identifiable, but both local layers
  collapse preparation stages into unsupported mass concentrations, misstate resazurin
  and water units, retain five unnamed empty stock stubs, and omit material preparation.
  Current provider main volume 20 mL and pH 6 are incompatible with the primary main
  preparation. Explicit cobalt/nickel hexahydrates also have anhydrous groundings;
  manganese hydration remains unspecified.
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
  - path: data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
    sha256: 8917690bfcc3ee2f136052305d448ad187ecdb262f8465731b179018abde93c3
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
    sha256: a844be64aeb44490151b4b75d31e75ce863da625eb0d71a116fc0a82bb7ee698
    role: context
  - path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
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
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
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
  selection: Task review 221; batch 023 item 1 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-two task batches
    contain 220 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 223 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009754
targets:
- target_id: CultureMech:009754
  path: data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  label: alkaliphilus_crotonatoxidans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/221/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/221/strict.tsv"
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009754
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
  - CultureMech:009754
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:25.021187Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch023/221/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:26.542398Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-023/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch023/221/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:28.713672Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T13:27:29.883401Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T13:33:02Z'
  support: supports
  summary: './data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml:1:id:
    CultureMech:009754

    ./data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml:1:id:
    CultureMech:009754

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/221/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T13:33:02Z'
  support: supports
  summary: 48 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: cf23b16c76bbf30a493c2edd6e2b6ea342dec239ea6f8eb66cabf24a17a3e3a5
- evidence_id: bound-context
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/source-preflight-bound/221/evidence-context-original.json
  locator: Complete frozen source context compared with fresh native input hashes
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Every contextual input hash matches the fresh inspection at the same base.
    Preflight remains provisional provenance; this review supplies its own single-target
    judgment.
  snapshot_sha256: 9056c4ccde812046b4cb9cabc6fae6be807ed110dec69a937db451fad71ff23a
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378
  locator: Entire exact medium 378 page and trace-metal subsection
  accessed_at: '2026-10-21T13:13:22.528336Z'
  support: supports
  summary: Primary original masses, two trace additions, staged 900 mL preparation,0.9/0.1
    volumes, separate 5% reductant stocks, primary pH 7.0–7.5 and trace pH 6.0 are
    distinct. Displayed 121°C 15 min default applies except stated filtration.
  snapshot_sha256: ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373
  locator: meta; all six component groups and all comments
  accessed_at: '2026-10-21T13:13:19.773874Z'
  support: supports
  summary: M373 explicitly names JCM378. TOGO retains Sol.1 and separate crotonate/reductant
    stock batches, unlike the local flattened record.
  snapshot_sha256: 7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad
- evidence_id: provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J378
  locator: data.medium; solutions 4103/4104/3861, all recipe and step rows
  accessed_at: '2026-10-21T13:13:19.050376Z'
  support: supports
  summary: The main declared volume 20 mL produces unsupported rates such as 2 g YE
    ->100 g/L, while its procedure specifies 900 mL water and0.9/0.1 staging. Root
    pH 6 is trace-stock pH. These provider artifacts are preserved as conflicts, not
    adopted.
  snapshot_sha256: 916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f
- evidence_id: vitamin-primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only; vitamin-specific filtration statement
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Only the ten-solute trace-vitamin batch and 1 L water transfer from the
    cross-reference. Other JCM197 medium/mineral/reductant formulations and final
    pH 6.8 do not transfer.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: vitamin-togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: meta and components[1] only for transferred vitamin stock
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: TOGO M190 resolves the local dependency to JCM197. Existing vitamin-row
    evidence is separately checked against exact bytes, original timestamps retained.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: vitamin-provider
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J197
  locator: Only trace-vitamin solution3861
  accessed_at: '2026-10-21T09:49:11.793511Z'
  support: supports
  summary: Provider composition corroborates the transferred vitamin subsection; other
    parent solutions are excluded.
  snapshot_sha256: 779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb
- evidence_id: trace-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4104
  locator: Exact stock 4104 endpoint
  accessed_at: '2026-10-21T13:16:27.278221Z'
  support: supports
  summary: Ten solutes plus 1000 mL water and trace-only pH 6 with unquantified KOH.
  snapshot_sha256: c3f59d13c37652bbd6d6efe2e5c4d2ca1cdf4f6e5f79195f80ba009d9d4ac08d
- evidence_id: vitamin-api
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3861
  locator: Exact stock 3861 endpoint
  accessed_at: '2026-10-20T06:58:06.579458Z'
  support: supports
  summary: Ten vitamin solutes plus 1000 mL water; provider-declared stock basis does
    not measure final volume.
  snapshot_sha256: c6829f83ad6e234909db1d65f45a27c24993e0280ff68c4d7355a8f6344335b9
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch023/221/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 8b17b48c02880335c1f2dc67dab5a126d8e3cc94f3f7c8598e83473f81641330
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
- evidence_id: chebi16526
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.337128Z'
  support: supports
  summary: CHEBI:16526 resolves to carbon dioxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:27.385647Z'
  support: supports
  summary: CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
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
- evidence_id: chebi32035
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32035
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T06:57:47.017507Z'
  support: supports
  summary: CHEBI:32035 resolves to potassium hydroxide. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 6ed3df00965b4707265cfced80411c4b1937b727f8c2093addbc467f88ce2ec8
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
- evidence_id: chebi41131
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_41131
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T13:13:21.899924Z'
  support: supports
  summary: CHEBI:41131 resolves to crotonic acid. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: f08c868d7d90142bc455feb86662dc662640c84681a90b7e8486691b0147cb4a
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: CHEBI:44557 resolves to nitrilotriacetic acid. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
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
- evidence_id: chebi63940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63940
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T10:07:18.442988Z'
  support: supports
  summary: CHEBI:63940 resolves to sodium tungstate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: c40f4b9c14d073989f58af77af0f1ffe969948e21d2bbe05a08c919f776aaf5c
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
- evidence_id: chebi77775
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:09.354177Z'
  support: supports
  summary: CHEBI:77775 resolves to sodium selenate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: a1a4ab87bbf08908fef7df53a788a85d9f6eee32350f082895e0563d6344c908
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
- evidence_id: chebi86360
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:05.958063Z'
  support: supports
  summary: CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T13:33:02Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206":
    [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206",
    "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32035": [{"label": "KOH", "match_type": "preferred_term",
    "identifier": "CHEBI:32035", "preferred_term": "KOH", "ontology_id": "CHEBI:32035",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label":
    "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term":
    "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:41131": [{"label": "Crotonic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:41131", "preferred_term": "Crotonic acid", "ontology_id":
    "CHEBI:41131", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557":
    [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label":
    "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term":
    "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:63940": [{"label": "Na2WO4", "match_type": "preferred_term",
    "identifier": "CHEBI:63940", "preferred_term": "Na2WO4", "ontology_id": "CHEBI:63940",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:77775": [{"label":
    "Na2SeO4", "match_type": "preferred_term", "identifier": "CHEBI:77775", "preferred_term":
    "Na2SeO4", "ontology_id": "CHEBI:77775", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: '[{"input": "target", "events": 14, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml",
    "events": 13, "timestamp_issues": []}]'
- evidence_id: dependency
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: Full current dependency read; only solutions[1] transferred; eleven exact
    evidence objects checked
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: The dependency has been maintained into separate batches and carries literal
    TOGO evidence. Its water 1 L and ten mass notes are independently verified in
    the inventory. This does not certify parent recipe identity, other stocks, or
    import their evidence into the target.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Current source conversion, stock preservation and merge boundaries are
    inspected context; none was executed or replayed. Historical duplicate-collapse
    notes describe old water/stock loss but do not prove current code would reproduce
    it.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Current source conversion, stock preservation and merge boundaries are
    inspected context; none was executed or replayed. Historical duplicate-collapse
    notes describe old water/stock loss but do not prove current code would reproduce
    it.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Current source conversion, stock preservation and merge boundaries are
    inspected context; none was executed or replayed. Historical duplicate-collapse
    notes describe old water/stock loss but do not prove current code would reproduce
    it.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T13:33:02Z'
  support: context_only
  summary: Current source conversion, stock preservation and merge boundaries are
    inspected context; none was executed or replayed. Historical duplicate-collapse
    notes describe old water/stock loss but do not prove current code would reproduce
    it.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 73 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"claim\": \"Sol.1 addition\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"TOGO assembly of main solution\
    \ 1\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"900\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"900 mL Sol.1\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n     \
    \   \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sol.1\\\",\\n          \\\"volume\\\": 900,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      }\n    ],\n    \"explanation\": \"The stored 900 G_PER_L is a solution\
    \ volume, not an ingredient mass or final concentration.\"\n  },\n  {\n    \"\
    decision_id\": \"q2\",\n    \"claim\": \"Flattened water\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Distinct main/crotonate/metal/reductant batches\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"900 mL +100 mL +1 L +10 mL +10\
    \ mL in separate stages\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"togoM373\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[5].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      }\n\
    \    ],\n    \"explanation\": \"The stored 1021 G_PER_L improperly adds numerical\
    \ amounts with heterogeneous units and separate stock-batch scope. Do not sum\
    \ them as a medium volume.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"\
    claim\": \"NaCl main batch amount\",\n    \"decision\": \"correct\",\n    \"stage\"\
    : \"JCM378 main recipe with staged preparation\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"NaCl 0.4 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"NaCl 0.4 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 0.4,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 0.4,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n                 \
    \       \\\"mmol_l\\\": 342.231,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q4\",\n    \"claim\": \"CaCl2・2H2O main batch\
    \ amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main recipe\
    \ with staged preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[3].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.05\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"CaCl 2 ·2H 2 O 0.05 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"CaCl 2 ·2H 2 O 0.05 g\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.05,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"CaCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 7,\\n                        \\\"amount\\\": 0.05,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 2.5,\\n \
    \                       \\\"mmol_l\\\": 17.0051,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q5\",\n    \"claim\": \"KH2PO4 main batch amount\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main recipe with staged\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"KH 2 PO 4 0.5 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"KH 2 PO 4 0.5 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"KH2PO4\\\",\\n                        \\\"compound_id\\\": 11,\\\
    n                        \\\"amount\\\": 0.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 25,\\n                 \
    \       \\\"mmol_l\\\": 183.707,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q6\",\n    \"claim\": \"NH4Cl main batch amount\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main recipe with staged\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"NH 4 Cl 0.4 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"NH 4 Cl 0.4 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"NH4Cl\\\",\\n                        \\\"compound_id\\\": 42,\\\
    n                        \\\"amount\\\": 0.4,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 20,\\n                 \
    \       \\\"mmol_l\\\": 373.902,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q7\",\n    \"claim\": \"Resazurin main batch\
    \ amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main recipe\
    \ with staged preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[6].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n   \
    \   },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Resazurin 1.0 mg\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Resazurin 1.0 mg\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[13]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 14,\\n                        \\\
    \"compound\\\": \\\"Resazurin\\\",\\n                        \\\"compound_id\\\
    \": 25,\\n                        \\\"amount\\\": 1,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.05,\\n \
    \                       \\\"mmol_l\\\": 0.21816,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q8\",\n    \"claim\": \"MgCl2・6H2O main batch\
    \ amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main recipe\
    \ with staged preparation\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"ingredients[7].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.33\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"MgCl 2 ·6H 2 O 0.33 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"MgCl 2 ·6H 2 O 0.33 g\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.33,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"MgCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 79,\\n                        \\\"amount\\\": 0.33,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 16.5,\\\
    n                        \\\"mmol_l\\\": 81.1596,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"Preserve the original batch mass and preparation\
    \ stage. Local G_PER_L is not established by an independently supported final\
    \ volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot\
    \ repair the basis. BD-Difco product qualifications remain explicit.\"\n  },\n\
    \  {\n    \"decision_id\": \"q9\",\n    \"claim\": \"NaHCO3 main batch amount\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main recipe with staged\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"3.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"NaHCO 3 3.5 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"NaHCO 3 3.5 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaHCO3\\\",\\n          \\\"volume\\\": 3.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"NaHCO3\\\",\\n                        \\\"compound_id\\\"\
    : 55,\\n                        \\\"amount\\\": 3.5,\\n                      \
    \  \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 175,\\n   \
    \                     \\\"mmol_l\\\": 2083.16,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q10\",\n    \"claim\": \"Yeast extract (BD-Difco)\
    \ main batch amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378\
    \ main recipe with staged preparation\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Yeast extract (BD-Difco) 2.0 g\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Yeast extract (BD-Difco) 2.0 g\",\n     \
    \   \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract (BD-Difco)\\\",\\n          \\\"\
    volume\\\": 2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\"\
    : \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Yeast extract\\\",\\n                        \\\"compound_id\\\
    \": 16,\\n                        \\\"attribute\\\": \\\"BD-Difco\\\",\\n    \
    \                    \\\"amount\\\": 2,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 100,\\n                  \
    \      \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Preserve the original batch mass and preparation\
    \ stage. Local G_PER_L is not established by an independently supported final\
    \ volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization cannot\
    \ repair the basis. BD-Difco product qualifications remain explicit.\"\n  },\n\
    \  {\n    \"decision_id\": \"q11\",\n    \"claim\": \"Tryptone (BD-Difco) main\
    \ batch amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"JCM378 main\
    \ recipe with staged preparation\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Tryptone (BD-Difco) 2.0 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Tryptone (BD-Difco) 2.0 g\",\n        \"\
    snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Tryptone (BD-Difco)\\\",\\n          \\\"volume\\\
    \": 2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Tryptone\\\",\\n                        \\\"compound_id\\\"\
    : 71,\\n                        \\\"attribute\\\": \\\"BD-Difco\\\",\\n      \
    \                  \\\"amount\\\": 2,\\n                        \\\"unit\\\":\
    \ \\\"g\\\",\\n                        \\\"g_l\\\": 100,\\n                  \
    \      \\\"mmol_l\\\": 1406.87,\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Preserve the original batch mass and\
    \ preparation stage. Local G_PER_L is not established by an independently supported\
    \ final volume. Resazurin is 1 mg, not 1 g; current provider20 mL normalization\
    \ cannot repair the basis. BD-Difco product qualifications remain explicit.\"\n\
    \  },\n  {\n    \"decision_id\": \"q12\",\n    \"claim\": \"Carbon dioxide gas\
    \ absolute dose\",\n    \"decision\": \"not_quantified\",\n    \"stage\": \"Main\
    \ cooling and dispensing gas atmosphere\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"No absolute gas dose; mixture\
    \ 80:20 v/v\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"N 2 -CO 2 (80:20, v/v)\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Variable absolute gas amount is appropriate;\
    \ it does not replace the source mixture ratio recorded separately below.\"\n\
    \  },\n  {\n    \"decision_id\": \"q13\",\n    \"claim\": \"N2 absolute dose\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"stage\": \"Main cooling and dispensing\
    \ gas atmosphere\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"No absolute gas dose; mixture\
    \ 80:20 v/v\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"N 2 -CO 2 (80:20, v/v)\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Variable absolute gas amount is appropriate;\
    \ it does not replace the source mixture ratio recorded separately below.\"\n\
    \  },\n  {\n    \"decision_id\": \"q14\",\n    \"claim\": \"Crotonic acid main\
    \ and stock mass\",\n    \"decision\": \"correct\",\n    \"stage\": \"Main table;\
    \ separately prepared crotonate stock\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.86\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.86\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"0.86 g main table and0.86 g/100\
    \ mL stock\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Crotonic acid 0.86 g\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"crotonic acid solution (0.86 g/100 ml, pH 7.0)\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Crotonic acid\\\",\\n          \\\"volume\\\"\
    : 0.86,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      }\n\
    \    ],\n    \"explanation\": \"The source mass and stock concentration are distinct\
    \ claims. The local 0.86 G/L is not authenticated by the primary staged-volume\
    \ instructions or current 20 mL provider basis; do not double-count the same contribution.\"\
    \n  },\n  {\n    \"decision_id\": \"q15\",\n    \"claim\": \"Na2MoO4・2H2O trace\
    \ batch amount\",\n    \"decision\": \"correct\",\n    \"stage\": \"Trace-metal\
    \ stock,10 mL receiving addition\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"Na 2 MoO 4 ·2H 2 O 0.02 g\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 Trace metal solution, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 0.02 g\",\n        \"\
    snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 0.02,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Na2MoO4 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 9,\\n                        \\\"amount\\\": 0.02,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.0826617,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The source stock batch amount/provider stock\
    \ rate is exposed as a direct receiving-medium concentration. Reconstruct the\
    \ stock and its dose without inferring final medium volume. Preserve explicit\
    \ hydrate form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q16\",\n    \"claim\": \"CoCl2・6H2O trace batch amount\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"CoCl 2 ·6H 2 O 0.2 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 Trace metal solution, exact ingredient\",\n        \"exact_source_quote\"\
    : \"CoCl 2 ·6H 2 O 0.2 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"CoCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 38,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 1.54037,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock batch amount/provider\
    \ stock rate is exposed as a direct receiving-medium concentration. Reconstruct\
    \ the stock and its dose without inferring final medium volume. Preserve explicit\
    \ hydrate form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q17\",\n    \"claim\": \"NiCl2・6H2O trace batch amount\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[16].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"NiCl 2 ·6H 2 O 0.02 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 Trace metal solution, exact ingredient\",\n\
    \        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"NiCl2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 40,\\n                        \\\"amount\\\": 0.02,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.154322,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock batch amount/provider stock rate\
    \ is exposed as a direct receiving-medium concentration. Reconstruct the stock\
    \ and its dose without inferring final medium volume. Preserve explicit hydrate\
    \ form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q18\",\n    \"claim\": \"ZnSO4・7H2O trace batch amount\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[17].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"ZnSO 4 ·7H 2 O 0.2 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 Trace metal solution, exact ingredient\",\n        \"exact_source_quote\"\
    : \"ZnSO 4 ·7H 2 O 0.2 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4・7H2O\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"ZnSO4 x 7 H2O\\\",\\n                        \\\"compound_id\\\
    \": 35,\\n                        \\\"amount\\\": 0.2,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.2,\\n \
    \                       \\\"mmol_l\\\": 0.695505,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock batch amount/provider stock rate\
    \ is exposed as a direct receiving-medium concentration. Reconstruct the stock\
    \ and its dose without inferring final medium volume. Preserve explicit hydrate\
    \ form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"claim\": \"CuCl2・2H2O trace batch amount\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[18].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"CuCl 2 ·2H 2 O 0.02 g\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 Trace metal solution, exact ingredient\",\n\
    \        \"exact_source_quote\": \"CuCl 2 ·2H 2 O 0.02 g\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"CuCl2 x 2 H2O\\\",\\n                        \\\"compound_id\\\
    \": 39,\\n                        \\\"amount\\\": 0.02,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\\
    n                        \\\"mmol_l\\\": 0.117314,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock batch amount/provider stock rate\
    \ is exposed as a direct receiving-medium concentration. Reconstruct the stock\
    \ and its dose without inferring final medium volume. Preserve explicit hydrate\
    \ form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"claim\": \"Nitrilotriacetic acid trace batch amount\",\n   \
    \ \"decision\": \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving\
    \ addition\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[19].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Nitrilotriacetic acid 2.0 g\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 Trace metal solution, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Nitrilotriacetic acid 2.0 g\",\n        \"\
    snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nitrilotriacetic acid\\\",\\n          \\\"volume\\\
    \": 2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Nitrilotriacetic acid\\\",\\n                        \\\"\
    compound_id\\\": 189,\\n                        \\\"amount\\\": 2,\\n        \
    \                \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\"\
    : 2,\\n                        \\\"mmol_l\\\": 10.4635,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"The source stock batch amount/provider stock\
    \ rate is exposed as a direct receiving-medium concentration. Reconstruct the\
    \ stock and its dose without inferring final medium volume. Preserve explicit\
    \ hydrate form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"claim\": \"MnSO4・xH2O trace batch amount\",\n    \"decision\"\
    : \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[20].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"MnSO 4 · x H 2 O 1.0 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 Trace metal solution, exact ingredient\",\n        \"exact_source_quote\"\
    : \"MnSO 4 · x H 2 O 1.0 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4・xH2O\\\",\\n          \\\"volume\\\": 1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"MnSO4 x n H2O\\\",\\n                        \\\"compound_id\\\
    \": 1000,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n   \
    \                     \\\"optional\\\": 0\\n                    }\",\n       \
    \ \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock batch amount/provider\
    \ stock rate is exposed as a direct receiving-medium concentration. Reconstruct\
    \ the stock and its dose without inferring final medium volume. Preserve explicit\
    \ hydrate form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q22\",\n    \"claim\": \"Fe(NH4)2(SO4)2・6H2O trace batch amount\",\n    \"\
    decision\": \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[21].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Fe(NH 4 ) 2 (SO 4 ) 2 ·6H 2 O 0.8 g\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 Trace metal solution, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Fe(NH 4 ) 2 (SO 4 ) 2 ·6H 2 O 0.8 g\",\n\
    \        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Fe(NH4)2(SO4)2・6H2O\\\",\\n          \\\"volume\\\
    \": 0.8,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Fe(NH4)2(SO4)2 x 6 H2O\\\",\\n                        \\\"compound_id\\\
    \": 247,\\n                        \\\"amount\\\": 0.8,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.8,\\n\
    \                        \\\"optional\\\": 0\\n                    }\",\n    \
    \    \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock batch amount/provider\
    \ stock rate is exposed as a direct receiving-medium concentration. Reconstruct\
    \ the stock and its dose without inferring final medium volume. Preserve explicit\
    \ hydrate form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q23\",\n    \"claim\": \"Na2WO4 trace batch amount\",\n    \"decision\": \"\
    correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[22].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"Na 2 WO 4 0.02 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 Trace metal solution, exact ingredient\",\n        \"exact_source_quote\"\
    : \"Na 2 WO 4 0.02 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"Na2WO4\\\",\\n                        \\\"compound_id\\\": 550,\\\
    n                        \\\"amount\\\": 0.02,\\n                        \\\"\
    unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\n         \
    \               \\\"mmol_l\\\": 0.0680689,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"The source stock batch amount/provider\
    \ stock rate is exposed as a direct receiving-medium concentration. Reconstruct\
    \ the stock and its dose without inferring final medium volume. Preserve explicit\
    \ hydrate form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"claim\": \"Na2SeO4 trace batch amount\",\n    \"decision\":\
    \ \"correct\",\n    \"stage\": \"Trace-metal stock,10 mL receiving addition\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[23].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.02\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_amount\": \"Na 2 SeO 4 0.02 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 Trace metal solution, exact ingredient\",\n        \"exact_source_quote\"\
    : \"Na 2 SeO 4 0.02 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[3].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO4\\\",\\n          \\\"volume\\\": 0.02,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[1].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Na2SeO4\\\",\\n                        \\\"compound_id\\\":\
    \ 375,\\n                        \\\"amount\\\": 0.02,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 0.02,\\n\
    \                        \\\"mmol_l\\\": 0.105848,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"The source stock batch amount/provider stock rate\
    \ is exposed as a direct receiving-medium concentration. Reconstruct the stock\
    \ and its dose without inferring final medium volume. Preserve explicit hydrate\
    \ form and unspecified manganese hydrate count.\"\n  },\n  {\n    \"decision_id\"\
    : \"q25\",\n    \"claim\": \"KOH titrant\",\n    \"decision\": \"correct\",\n\
    \    \"stage\": \"Trace-metal stock only\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[24].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_amount\": \"Unquantified KOH to stock\
    \ pH 6.0\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm378\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Adjust pH to 6.0 with KOH.\",\n        \"\
    snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"No fixed dose or strength is supplied.\
    \ Keep unknown quantity, but move the direct-medium assertion into the trace-stock\
    \ context.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"claim\": \"L--Cysteine・HCL・H2O\
    \ contribution\",\n    \"decision\": \"correct\",\n    \"stage\": \"Separately\
    \ prepared reductant added to main\",\n    \"local_fields\": [\n      {\n    \
    \    \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[25].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"L-Cysteine·HCL·H 2 O 0.5 g\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"L-Cysteine·HCL·H 2 O 0.5 g\",\n        \"\
    snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[4].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L--Cysteine・HCL・H2O\\\",\\n          \\\"volume\\\
    \": 0.5,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\":\
    \ \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n     \
    \ },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[11]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 12,\\n                        \\\
    \"compound\\\": \\\"L-Cysteine HCl x H2O\\\",\\n                        \\\"compound_id\\\
    \": 770,\\n                        \\\"amount\\\": 0.5,\\n                   \
    \     \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 25,\\n \
    \                       \\\"optional\\\": 0\\n                    }\",\n     \
    \   \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Primary gives 0.5 g batch contribution\
    \ and a separate 5% stock instruction; TOGO gives 0.5 g in 10 mL water. None independently\
    \ establishes the local final-medium g/L denominator.\"\n  },\n  {\n    \"decision_id\"\
    : \"q27\",\n    \"claim\": \"Na2S・9H2O contribution\",\n    \"decision\": \"correct\"\
    ,\n    \"stage\": \"Separately prepared reductant added to main\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[26].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"Na 2 S·9H 2 O 0.5 g\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Na 2 S·9H 2 O 0.5 g\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      },\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n \
    \       \"source_locator\": \"$.components[5].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S・9H2O\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[12]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 13,\\n                        \\\
    \"compound\\\": \\\"Na2S x 9 H2O\\\",\\n                        \\\"compound_id\\\
    \": 54,\\n                        \\\"amount\\\": 0.5,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 25,\\n  \
    \                      \\\"mmol_l\\\": 104.088,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Primary gives 0.5 g batch contribution\
    \ and a separate 5% stock instruction; TOGO gives 0.5 g in 10 mL water. None independently\
    \ establishes the local final-medium g/L denominator.\"\n  },\n  {\n    \"decision_id\"\
    : \"q28\",\n    \"claim\": \"Existing stock addition crotonic acid solution\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"Named stock addition in its\
    \ source stage\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"100\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"100 mL\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n     \
    \   \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"crotonic acid solution\\\",\\n          \\\"volume\\\
    \": 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\"\
    : \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"crotonic acid solution (0.86 g/100 ml, pH 7.0)\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"The existing stock stub has a mass-concentration\
    \ unit and no composition. Preserve TOGO addition volume with primary fraction/stock\
    \ context; do not equate mL to grams or assert per-final-liter basis.\"\n  },\n\
    \  {\n    \"decision_id\": \"q29\",\n    \"claim\": \"Existing stock addition\
    \ cysteine・HCl solution\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Named stock addition in its source stage\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"10 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n     \
    \   \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"cysteine・HCl solution\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Autoclave cysteine·HCl and Na 2 S·9H 2 O as 5% solutions\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"The existing stock stub has a mass-concentration\
    \ unit and no composition. Preserve TOGO addition volume with primary fraction/stock\
    \ context; do not equate mL to grams or assert per-final-liter basis.\"\n  },\n\
    \  {\n    \"decision_id\": \"q30\",\n    \"claim\": \"Existing stock addition\
    \ Na2S・9H2O solution\",\n    \"decision\": \"correct\",\n    \"stage\": \"Named\
    \ stock addition in its source stage\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"10 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n     \
    \   \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2S・9H2O solution\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\":\
    \ \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n     \
    \ },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Autoclave cysteine·HCl and Na 2 S·9H 2 O as 5% solutions\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"The existing stock stub has a mass-concentration\
    \ unit and no composition. Preserve TOGO addition volume with primary fraction/stock\
    \ context; do not equate mL to grams or assert per-final-liter basis.\"\n  },\n\
    \  {\n    \"decision_id\": \"q31\",\n    \"claim\": \"Existing stock addition\
    \ Trace metal solution (see below)\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Named stock addition in its source stage\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"10 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n     \
    \   \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace metal solution (see below)\\\",\\n     \
    \     \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Trace metal solution (see below) 10.0 ml\",\n        \"snapshot_sha256\":\
    \ \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"The existing stock stub has a mass-concentration\
    \ unit and no composition. Preserve TOGO addition volume with primary fraction/stock\
    \ context; do not equate mL to grams or assert per-final-liter basis.\"\n  },\n\
    \  {\n    \"decision_id\": \"q32\",\n    \"claim\": \"Existing stock addition\
    \ Trace vitamins (see Medium [M190])\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Named stock addition in its source stage\",\n    \"local_fields\":\
    \ [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_amount\": \"10 mL\",\n    \"source_snippets\":\
    \ [\n      {\n        \"source_key\": \"togoM373\",\n        \"source_url\": \"\
    https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\",\n     \
    \   \"source_locator\": \"$.components[1].items[11]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Trace vitamins (see Medium No. 197 ) 10.0 ml\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"The existing stock stub has a mass-concentration\
    \ unit and no composition. Preserve TOGO addition volume with primary fraction/stock\
    \ context; do not equate mL to grams or assert per-final-liter basis.\"\n  },\n\
    \  {\n    \"decision_id\": \"q33\",\n    \"claim\": \"basal water batch input\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"basal stock/main preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"Source-specific water volume\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM373\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 900,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"in 900 ml of distilled water\",\n       \
    \ \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Each water input has its own preparation\
    \ stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry\
    \ are retained separately; no measured final-volume inference.\"\n  },\n  {\n\
    \    \"decision_id\": \"q34\",\n    \"claim\": \"crotonate water batch input\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"crotonate stock/main preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"Source-specific water volume\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM373\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 100,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      },\n\
    \      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"crotonic acid solution (0.86 g/100 ml, pH\
    \ 7.0)\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Each water input has its own preparation\
    \ stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry\
    \ are retained separately; no measured final-volume inference.\"\n  },\n  {\n\
    \    \"decision_id\": \"q35\",\n    \"claim\": \"trace metal water batch input\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"trace metal stock/main preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"Source-specific water volume\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM373\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\
    \n      },\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Each water input has its own preparation\
    \ stage. The crotonic 100 mL concentration denominator and TOGO100 mL water entry\
    \ are retained separately; no measured final-volume inference.\"\n  },\n  {\n\
    \    \"decision_id\": \"q36\",\n    \"claim\": \"cysteine water batch input\"\
    ,\n    \"decision\": \"correct\",\n    \"stage\": \"cysteine stock/main preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"Source-specific water volume\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM373\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[4].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      }\n\
    \    ],\n    \"explanation\": \"Each water input has its own preparation stage.\
    \ The crotonic 100 mL concentration denominator and TOGO100 mL water entry are\
    \ retained separately; no measured final-volume inference.\"\n  },\n  {\n    \"\
    decision_id\": \"q37\",\n    \"claim\": \"sulfide water batch input\",\n    \"\
    decision\": \"correct\",\n    \"stage\": \"sulfide stock/main preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1021.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      }\n    ],\n    \"source_amount\": \"Source-specific water volume\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"togoM373\",\n\
    \        \"source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M373\"\
    ,\n        \"source_locator\": \"$.components[5].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    7648bdd8903a2b1b1f1f22024cb100f1f6bbce21fc4851f54eeaef7abd23a9ad\"\n      }\n\
    \    ],\n    \"explanation\": \"Each water input has its own preparation stage.\
    \ The crotonic 100 mL concentration denominator and TOGO100 mL water entry are\
    \ retained separately; no measured final-volume inference.\"\n  },\n  {\n    \"\
    decision_id\": \"q38\",\n    \"claim\": \"Transferred vitamin stock Distilled\
    \ water\",\n    \"decision\": \"add\",\n    \"stage\": \"JCM197 trace-vitamin\
    \ stock only, receiving addition 10 mL\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Distilled water 1.0 L\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Source-only batch composition is absent\
    \ from target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q39\",\n    \"claim\": \"Existing dependency vitamin batch claim 0\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[0].concentration\",\n        \"stored\": {\n    \
    \      \"value\": \"1\",\n          \"unit\": \"L\"\n        }\n      }\n    ],\n\
    \    \"source_amount\": \"Distilled water 1.0 L\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[10]\",\n        \"exact_source_quote\": \"{\\n\
    \                        \\\"recipe_order\\\": 11,\\n                        \\\
    \"compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet\
    \ and claimed response hash match current capture; original date retained. For\
    \ solutes only the source batch-mass notes are verified, not an absent concentration\
    \ or the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q40\",\n   \
    \ \"claim\": \"Transferred vitamin stock Biotin\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Biotin 2.0 mg\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins subsection, exact ingredient\",\n        \"exact_source_quote\"\
    : \"Biotin 2.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n             \
    \           \\\"mmol_l\\\": 0.00818632,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Source-only batch composition is absent\
    \ from target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q41\",\n    \"claim\": \"Existing dependency vitamin batch claim 1\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[1].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 2 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Biotin 2.0 mg\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Biotin 2.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Biotin\\\",\\n                        \\\"compound_id\\\": 46,\\\
    n                        \\\"amount\\\": 2,\\n                        \\\"unit\\\
    \": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n             \
    \           \\\"mmol_l\\\": 0.00818632,\\n                        \\\"optional\\\
    \": 0\\n                    }\",\n        \"snapshot_sha256\": \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\
    \n      }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet\
    \ and claimed response hash match current capture; original date retained. For\
    \ solutes only the source batch-mass notes are verified, not an absent concentration\
    \ or the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q42\",\n   \
    \ \"claim\": \"Transferred vitamin stock p--Aminobenzoic acid\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition\
    \ 10 mL\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"p -Aminobenzoic acid 5.0 mg\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"p -Aminobenzoic acid 5.0 mg\",\n        \"\
    snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                        \\\"compound_id\\\
    \": 47,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n\
    \                        \\\"mmol_l\\\": 0.0364591,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q43\",\n    \"claim\": \"Existing dependency vitamin batch claim 2\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[2].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"p -Aminobenzoic\
    \ acid 5.0 mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"p -Aminobenzoic acid 5.0 mg\",\n        \"\
    snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[8]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 9,\\n                        \\\"\
    compound\\\": \\\"p-Aminobenzoic acid\\\",\\n                        \\\"compound_id\\\
    \": 47,\\n                        \\\"amount\\\": 5,\\n                      \
    \  \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n\
    \                        \\\"mmol_l\\\": 0.0364591,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q44\",\n    \"\
    claim\": \"Transferred vitamin stock Thiamine・HCl\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Thiamine·HCl 5.0 mg\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n  \
    \      \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Thiamine·HCl 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Thiamine HCl\\\",\\n                        \\\"compound_id\\\
    \": 1207,\\n                        \\\"amount\\\": 5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0148236,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q45\",\n    \"claim\": \"Existing dependency vitamin batch claim 3\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[3].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Thiamine·HCl 5.0\
    \ mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Thiamine·HCl 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Thiamine HCl\\\",\\n                        \\\"compound_id\\\
    \": 1207,\\n                        \\\"amount\\\": 5,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0148236,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q46\",\n    \"\
    claim\": \"Transferred vitamin stock Calcium pantothenate\",\n    \"decision\"\
    : \"add\",\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition\
    \ 10 mL\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Calcium pantothenate 5.0 mg\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Calcium pantothenate 5.0 mg\",\n        \"\
    snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Calcium pantothenate\\\",\\n                        \\\"compound_id\\\
    \": 518,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0104925,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q47\",\n    \"claim\": \"Existing dependency vitamin batch claim 4\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[4].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Calcium pantothenate\
    \ 5.0 mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Calcium pantothenate 5.0 mg\",\n        \"\
    snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Calcium pantothenate\\\",\\n                        \\\"compound_id\\\
    \": 518,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0104925,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q48\",\n    \"\
    claim\": \"Transferred vitamin stock Pyridoxine・HCl\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Pyridoxine·HCl 10.0 mg\",\n  \
    \  \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n    \
    \    \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Pyridoxine·HCl 10.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                        \\\"\
    compound_id\\\": 519,\\n                        \\\"amount\\\": 10,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.01,\\n                        \\\"mmol_l\\\": 0.0486287,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q49\",\n    \"claim\": \"Existing dependency vitamin batch claim 5\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[5].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 10 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Pyridoxine·HCl 10.0\
    \ mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Pyridoxine·HCl 10.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"Pyridoxine hydrochloride\\\",\\n                        \\\"\
    compound_id\\\": 519,\\n                        \\\"amount\\\": 10,\\n       \
    \                 \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\
    \": 0.01,\\n                        \\\"mmol_l\\\": 0.0486287,\\n            \
    \            \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q50\",\n    \"\
    claim\": \"Transferred vitamin stock Folic acid\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Folic acid 2.0 mg\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins subsection, exact ingredient\",\n        \"exact_source_quote\"\
    : \"Folic acid 2.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Folic acid\\\",\\n                        \\\"compound_id\\\"\
    : 138,\\n                        \\\"amount\\\": 2,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n \
    \                       \\\"mmol_l\\\": 0.00453104,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q51\",\n    \"claim\": \"Existing dependency vitamin batch claim 6\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[6].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 2 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Folic acid 2.0 mg\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Folic acid 2.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"Folic acid\\\",\\n                        \\\"compound_id\\\"\
    : 138,\\n                        \\\"amount\\\": 2,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.002,\\n \
    \                       \\\"mmol_l\\\": 0.00453104,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q52\",\n    \"\
    claim\": \"Transferred vitamin stock Vitamin B12\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Vitamin B 1 2 0.1 mg\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n  \
    \      \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Vitamin B 1 2 0.1 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0001,\\\
    n                        \\\"mmol_l\\\": 7.3779e-5,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q53\",\n    \"claim\": \"Existing dependency vitamin batch claim 7\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[7].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 0.1 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Vitamin B 1 2 0.1\
    \ mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Vitamin B 1 2 0.1 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[7]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 8,\\n                        \\\"\
    compound\\\": \\\"Vitamin B12\\\",\\n                        \\\"compound_id\\\
    \": 18,\\n                        \\\"amount\\\": 0.1,\\n                    \
    \    \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.0001,\\\
    n                        \\\"mmol_l\\\": 7.3779e-5,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q54\",\n    \"\
    claim\": \"Transferred vitamin stock Riboflavin\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Riboflavin 5.0 mg\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm197\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n        \"source_locator\"\
    : \"JCM197 Trace vitamins subsection, exact ingredient\",\n        \"exact_source_quote\"\
    : \"Riboflavin 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Riboflavin\\\",\\n                        \\\"compound_id\\\"\
    : 136,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n \
    \                       \\\"mmol_l\\\": 0.0132837,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"Source-only batch composition is absent from target/owner\
    \ stock stub. No parent basal/mineral/reductant content or specific stereochemical\
    \ grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"q55\",\n    \"\
    claim\": \"Existing dependency vitamin batch claim 8\",\n    \"decision\": \"\
    verified\",\n    \"stage\": \"Context dependency only; not inherited as target\
    \ evidence\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[8].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\"\n      }\n    ],\n    \"source_amount\":\
    \ \"Riboflavin 5.0 mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Riboflavin 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Riboflavin\\\",\\n                        \\\"compound_id\\\"\
    : 136,\\n                        \\\"amount\\\": 5,\\n                       \
    \ \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\n \
    \                       \\\"mmol_l\\\": 0.0132837,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"Exact same-layer attached source snippet and claimed\
    \ response hash match current capture; original date retained. For solutes only\
    \ the source batch-mass notes are verified, not an absent concentration or the\
    \ chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q56\",\n    \"claim\"\
    : \"Transferred vitamin stock Nicotinic acid\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Nicotinic acid 5.0 mg\",\n   \
    \ \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n     \
    \   \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Nicotinic acid 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"compound_id\\\
    \": 139,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0406141,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Source-only batch composition is absent from\
    \ target/owner stock stub. No parent basal/mineral/reductant content or specific\
    \ stereochemical grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"\
    q57\",\n    \"claim\": \"Existing dependency vitamin batch claim 9\",\n    \"\
    decision\": \"verified\",\n    \"stage\": \"Context dependency only; not inherited\
    \ as target evidence\",\n    \"local_fields\": [\n      {\n        \"input\":\
    \ \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\",\n        \"field_path\"\
    : \"solutions[1].composition[9].notes\",\n        \"stored\": \"Role: Vitamin;\
    \ Properties: Organic compound, Defined component, Simple component\\n\\nSource\
    \ batch input: 5 mg. Final preparation volume is not independently established;\
    \ the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter\
    \ concentration.\"\n      }\n    ],\n    \"source_amount\": \"Nicotinic acid 5.0\
    \ mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Nicotinic acid 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      },\n\
    \      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"source_url\"\
    : \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Nicotinic acid\\\",\\n                        \\\"compound_id\\\
    \": 139,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.0406141,\\n                       \
    \ \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n     \
    \ }\n    ],\n    \"explanation\": \"Exact same-layer attached source snippet and\
    \ claimed response hash match current capture; original date retained. For solutes\
    \ only the source batch-mass notes are verified, not an absent concentration or\
    \ the chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q58\",\n    \"\
    claim\": \"Transferred vitamin stock Lipoic acid\",\n    \"decision\": \"add\"\
    ,\n    \"stage\": \"JCM197 trace-vitamin stock only, receiving addition 10 mL\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"Lipoic acid 5.0 mg\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm197\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\",\n  \
    \      \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Lipoic acid 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Lipoic acid\\\",\\n                        \\\"compound_id\\\
    \": 368,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.024233,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"Source-only batch composition is absent from target/owner\
    \ stock stub. No parent basal/mineral/reductant content or specific stereochemical\
    \ grounding is inherited.\"\n  },\n  {\n    \"decision_id\": \"q59\",\n    \"\
    claim\": \"Existing dependency vitamin batch claim 10\",\n    \"decision\": \"\
    verified\",\n    \"stage\": \"Context dependency only; not inherited as target\
    \ evidence\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].notes\",\n        \"\
    stored\": \"Role: Growth factor; Properties: Organic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 5 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\"\n      }\n    ],\n    \"source_amount\"\
    : \"Lipoic acid 5.0 mg\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"JCM197 Trace vitamins subsection, exact ingredient\"\
    ,\n        \"exact_source_quote\": \"Lipoic acid 5.0 mg\",\n        \"snapshot_sha256\"\
    : \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\",\n    \
    \    \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\",\n \
    \       \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ378api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J378\",\n        \"source_locator\"\
    : \"$.data.solutions[2].recipe[9]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 10,\\n                        \\\
    \"compound\\\": \\\"Lipoic acid\\\",\\n                        \\\"compound_id\\\
    \": 368,\\n                        \\\"amount\\\": 5,\\n                     \
    \   \\\"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.005,\\\
    n                        \\\"mmol_l\\\": 0.024233,\\n                        \\\
    \"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"\
    916cd66fd911954430486630290180051d6c031dc447245f78b0cd8c8f5c9d0f\"\n      }\n\
    \    ],\n    \"explanation\": \"Exact same-layer attached source snippet and claimed\
    \ response hash match current capture; original date retained. For solutes only\
    \ the source batch-mass notes are verified, not an absent concentration or the\
    \ chemical grounding.\"\n  },\n  {\n    \"decision_id\": \"q60\",\n    \"claim\"\
    : \"Initial main pH\",\n    \"decision\": \"add\",\n    \"stage\": \"Initial main\
    \ pH source stage\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n        \"\
    field_path\": \"ph_range\",\n        \"stored\": null\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_amount\": \"7.0–7.5\",\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"adjust pH to 7.0-7.5.\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q61\",\n    \"claim\"\
    : \"Brief boil duration\",\n    \"decision\": \"add\",\n    \"stage\": \"Brief\
    \ boil duration source stage\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n  \
    \    },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"5–10 sec\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Bring to a boil for 5-10 sec\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q62\",\n    \"claim\"\
    : \"Main cooling/dispensing gas ratio\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Main cooling/dispensing gas ratio source stage\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"80:20 v/v\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (80:20, v/v)\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q63\",\n    \"claim\"\
    : \"Basal dispensing fraction\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Basal dispensing fraction source stage\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"0.9 volume\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Dispense 0.9 volume of the medium\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q64\",\n    \"claim\"\
    : \"Crotonate addition fraction\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Crotonate addition fraction source stage\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"0.1 volume\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Add 0.1 volume of a filter-sterilized crotonic acid solution\",\n        \"\
    snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q65\",\n    \"claim\"\
    : \"Crotonate stock strength\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Crotonate stock strength source stage\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_amount\": \"0.86 g/100 mL\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"crotonic acid solution (0.86 g/100 ml, pH 7.0)\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q66\",\n    \"claim\"\
    : \"Crotonate stock pH\",\n    \"decision\": \"add\",\n    \"stage\": \"Crotonate\
    \ stock pH source stage\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_amount\": \"7.0\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"crotonic acid solution (0.86 g/100 ml, pH 7.0)\",\n        \"snapshot_sha256\"\
    : \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\",\n    \
    \    \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q67\",\n    \"claim\"\
    : \"Cysteine stock percentage\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Cysteine stock percentage source stage\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].preparation_notes\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_amount\": \"5%, basis unstated\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Autoclave cysteine·HCl and Na 2 S·9H 2 O\
    \ as 5% solutions\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q68\",\n    \"claim\"\
    : \"Sulfide stock percentage\",\n    \"decision\": \"add\",\n    \"stage\": \"\
    Sulfide stock percentage source stage\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].preparation_notes\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_amount\": \"5%, basis unstated\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm378\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n  \
    \      \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Autoclave cysteine·HCl and Na 2 S·9H 2 O\
    \ as 5% solutions\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q69\",\n    \"claim\"\
    : \"Trace stock pH\",\n    \"decision\": \"add\",\n    \"stage\": \"Trace stock\
    \ pH source stage\",\n    \"local_fields\": [\n      {\n        \"input\": \"\
    data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n        \"\
    field_path\": \"solutions[3].preparation_notes\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_amount\": \"6.0\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\",\n        \"source_locator\"\
    : \"JCM378 exact ingredient or preparation sentence\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 6.0 with KOH.\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q70\",\n    \"claim\"\
    : \"Autoclave temperature\",\n    \"decision\": \"add\",\n    \"stage\": \"Autoclave\
    \ temperature source stage\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"sterilization\",\n        \"stored\": null\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_amount\": \"121°C\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q71\",\n    \"claim\"\
    : \"Autoclave duration\",\n    \"decision\": \"add\",\n    \"stage\": \"Autoclave\
    \ duration source stage\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\",\n     \
    \   \"field_path\": \"sterilization\",\n        \"stored\": null\n      },\n \
    \     {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"sterilization\",\n        \"stored\": null\n    \
    \  }\n    ],\n    \"source_amount\": \"15 min\",\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Unless otherwise stated, sterilize media\
    \ by autoclaving at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Retain the exact qualified source instruction.\
    \ No incubation setting, measured final volume, unstated percentage basis or parent-medium\
    \ condition is inferred.\"\n  },\n  {\n    \"decision_id\": \"q72\",\n    \"claim\"\
    : \"Reductant-stock N2 atmosphere\",\n    \"decision\": \"add\",\n    \"stage\"\
    : \"Separately autoclaved reductant stocks\",\n    \"local_fields\": [\n     \
    \ {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_amount\": \"N2 atmosphere; purity not numerically\
    \ specified\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm378\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=378\"\
    ,\n        \"source_locator\": \"JCM378 exact ingredient or preparation sentence\"\
    ,\n        \"exact_source_quote\": \"as 5% solutions, respectively, under a N\
    \ 2 atmosphere.\",\n        \"snapshot_sha256\": \"ea5b13a5a03be4d5478f086d1433d260146f2a9862da77d121f272cdc7bf0029\"\
    ,\n        \"parsed_text_sha256\": \"9917f91dea510541599721447ebd5cd5fd64be228068d56db9026647a3fdd54e\"\
    \n      }\n    ],\n    \"explanation\": \"Do not rewrite source N2 as a numerical\
    \ 100% purity claim.\"\n  },\n  {\n    \"decision_id\": \"q73\",\n    \"claim\"\
    : \"Trace-vitamin stock filtration atmosphere\",\n    \"decision\": \"add\",\n\
    \    \"stage\": \"JCM197 vitamin-specific filtration only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/ALKALIPHILUS_CROTONATOXIDANS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].preparation_notes\",\n        \"stored\"\
    : null\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].preparation_notes\",\n        \"stored\"\
    : null\n      }\n    ],\n    \"source_amount\": \"Filter sterilization while gassing\
    \ with N2\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"\
    jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Vitamin-specific preparation clause\",\n    \
    \    \"exact_source_quote\": \"Trace vitamins while gassing       with N 2 .\"\
    ,\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      }\n    ],\n    \"explanation\": \"Transfer only the instruction explicitly\
    \ about the referenced vitamin stock; no parent medium gas mixture or final pH\
    \ is transferred.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and pinned secondary identifier metadata
  outcome: concern
  summary: '24 distinct asserted primary/secondary IDs resolve to matching nonobsolete
    labels in all inspected layers. Target linkage: 24/27 primary and 11/27 secondary
    instances; all asserted CHEBI-keyed secondary IDs have exact pinned MIM rows;
    no legacy MIM identifier is asserted in the target or maintained owner. Exact
    supplied-form mismatch is addressed separately; valid IDs and labels do not establish
    correct source grounding.'
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi26710
  - chebi31206
  - chebi32035
  - chebi32139
  - chebi32312
  - chebi34887
  - chebi35696
  - chebi41131
  - chebi44557
  - chebi63036
  - chebi63940
  - chebi75213
  - chebi76181
  - chebi76209
  - chebi77775
  - chebi86158
  - chebi86318
  - chebi86345
  - chebi86360
  - chebi8806
  - chebi91248
  details: 'Instance coverage on a 0–100 percent scale, denominator 27: primary 88.89%;
    secondary 40.74%. These are linkage metrics, not correctness scores. Missing optional
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
  - CultureMech:009754
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact accession, stocks and maintained owner
  outcome: supported
  summary: CM009754 resolves to one exact maintained M373 contributor and current
    JCM378. M190 explicitly maps to JCM197; only its trace-vitamin recipe transfers.
    Stock endpoints 4104/3861 agree with their named provider subsections. No formula
    fingerprint establishes whole-parent equivalence.
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - record
  - owner-0
  - id-search
  - primary
  - togo
  - provider
  - dependency
  - vitamin-primary
  - vitamin-togo
  - vitamin-provider
  - trace-api
  - vitamin-api
- assessment_id: classification
  area: scope
  topic: Mixtures, products, preparation and growth scope
  outcome: supported
  summary: Complex/undefined follows BD-Difco yeast extract and tryptone; liquid is
    consistent with the absence of gelling ingredient. Source role/property annotations
    are not independent organism-growth claims. No strain assertion or specific growth
    optimum is inferred. Source salt/hydrate forms are assessed independently of label
    validity.
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - quantity-inventory
- assessment_id: ownership
  area: ownership
  topic: Authoritative fixes and generated correspondence
  outcome: supported
  summary: Both target and maintained M373 owner share the identified quantity, empty-stock
    and preparation gaps. The separately repaired M190 dependency is context and must
    not be treated as a second reviewed target. Correct maintained inputs only after
    source-scoped curation; preserve append-only history and regenerate separately.
  target_ids:
  - CultureMech:009754
  evidence_ids:
  - record
  - owner-0
  - dependency
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: cm009754-stock-flattening
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Preparation stages collapse into an incoherent direct formulation
  description: Both layers expose stock strengths and solution additions as direct
    G_PER_L amounts, combine water from unrelated stages with mixed units, and retain
    five unnamed empty stock stubs. The result does not faithfully denote the complete
    staged JCM378 recipe. Source trace-vitamin composition is entirely absent.
  target_ids:
  - CultureMech:009754
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  issue_key: cm009754-resazurin-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Resazurin has the wrong mass unit and basis
  description: Both layers store 1 G_PER_L while both primary and TOGO state 1 mg
    for the receiving batch. Current provider 0.05 g/L derives from an inconsistent
    20 mL basis and is not a supported replacement.
  target_ids:
  - CultureMech:009754
  field_paths:
  - ingredients[6].concentration
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - provider
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  issue_key: cm009754-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Explicit cobalt and nickel hexahydrates use anhydrous IDs
  description: Source CoCl2·6H2O and NiCl2·6H2O are grounded to anhydrous CHEBI35696/34887.
    Manganese is source xH2O with unspecified count, while its generic anhydrous term
    loses that qualification; do not select a presumed hydrate. Amounts remain source
    masses.
  target_ids:
  - CultureMech:009754
  field_paths:
  - ingredients[15].term
  - ingredients[16].term
  - ingredients[20].term
  evidence_ids:
  - record
  - owner-0
  - primary
  - chebi35696
  - chebi34887
  - chebi86360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  issue_key: cm009754-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Material staged preparation is absent
  description: Neither layer retains primary pH stages, gas composition, brief boil,
    0.9/0.1 dispensing, overnight stand, crotonate filtration, separately autoclaved
    reductant stocks or displayed sterilization default. Main pH must not be replaced
    by provider trace pH 6.
  target_ids:
  - CultureMech:009754
  field_paths:
  - preparation_steps
  - sterilization
  - ph_range
  - solutions
  evidence_ids:
  - record
  - owner-0
  - primary
  - vitamin-primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: cm009754-quantity-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source accession notes do not authenticate individual quantities
  description: Target and maintained owner have no attached claim-level quantity evidence.
    Current provider metadata contain a 20 mL normalization artifact and tracepH contamination,
    so blind source-wide evidence would perpetuate errors. M190 evidence stays attached
    only to its own stock claims.
  target_ids:
  - CultureMech:009754
  field_paths:
  - ingredients
  - solutions
  - references
  evidence_ids:
  - record
  - owner-0
  - primary
  - togo
  - provider
  - dependency
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  description: Restore exact source stages, stock identities, original masses/volumes
    and scoped compositions; remove unsupported final-medium rates rather than inventing
    a final denominator.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  description: Retain exact 1 mg batch input with source stage; establish a legitimate
    denominator before any final concentration claim.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  description: Resolve exact supplied-form identifiers where supported; preserve unspecified
    manganese hydration and leave unresolved specificity explicit. Recheck linked
    annotations independently.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  description: Add narrow primary preparation and explicit stock exceptions, including
    vitamin-specific filtration. Keep default autoclaving separate from filtration
    and never infer unspecified dose, purity or percentage basis.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
  description: Attach exact primary/provider snippets to each corrected or retained
    claim, explicitly preserving source conflicts and original access/version metadata.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009754
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M373_Alkaliphilus_Crotonatoxidans_Medium.yaml
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
- The intended measured final volume, unspecified 5% stock bases and manganese hydrate
  count are not established. Completed review means those bounded uncertainties were
  identified; it does not validate any guessed replacement concentration. JCM197 non-vitamin
  content is outside transfer scope.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-023
- generated-medium
```
