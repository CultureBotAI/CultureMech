# Source and formulation review: an1_medium (CultureMech:002624)

- Review: 20261021T145820Z-culturemech-002624-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:47:49Z
- Finished UTC: 2026-10-21T14:58:20Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact JCM 267/MediaDive J267 identity and all six main amount representations resolve. Water, primary default sterilization and narrow evidence are missing; the sulfur secondary key has a completed current MIM mapping gap. The separate KG ingredient-set assertion cannot be verified without graph data, so the review is partial for that check.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 257; batch 026 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-five task batches contain 250 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 253 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002624 | data/merge_yaml/merged/AN1_MEDIUM.yaml | generated | an1_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002624 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002624 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/257/strict.tsv |
| validate-terms | passed | True | CultureMech:002624 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002624 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:002624 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact KG ingredient-set assertion verification | unavailable | True | CultureMech:002624 | No transformed MediaDive edges.tsv/nodes.tsv were found in the fresh owned checkout after an ignored-inclusive search. The asserted J267 graph correspondence remains unverified; matcher was not invoked. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:002624.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:002624.

14 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "quantity": "Trypticase peptone",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Trypticase peptone (BD-BBL) 10.0 g",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[0]",
        "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD-BBL\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Existing G_PER_L value agrees with the provider declared 1000 mL representation, but neither layer attaches source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate addition; do not claim measured final volume. Sulfur powder and BD-BBL product context belong to the exact source ingredient. Resazurin 1 mg corresponds to the stored provider 0.001 g/L."
  },
  {
    "quantity_id": "q2",
    "quantity": "K2HPO4",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "K 2 HPO 4 1.5 g",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[1]",
        "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 8.61198,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Existing G_PER_L value agrees with the provider declared 1000 mL representation, but neither layer attaches source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate addition; do not claim measured final volume. Sulfur powder and BD-BBL product context belong to the exact source ingredient. Resazurin 1 mg corresponds to the stored provider 0.001 g/L."
  },
  {
    "quantity_id": "q3",
    "quantity": "NaCl",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "2.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "NaCl 2.5 g",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[2]",
        "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 42.7789,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Existing G_PER_L value agrees with the provider declared 1000 mL representation, but neither layer attaches source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate addition; do not claim measured final volume. Sulfur powder and BD-BBL product context belong to the exact source ingredient. Resazurin 1 mg corresponds to the stored provider 0.001 g/L."
  },
  {
    "quantity_id": "q4",
    "quantity": "Sodium thioglycolate",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Sodium thioglycolate 1.0 g",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[3]",
        "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Sodium thioglycolate\",\n                        \"compound_id\": 1644,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 8.76424,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Existing G_PER_L value agrees with the provider declared 1000 mL representation, but neither layer attaches source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate addition; do not claim measured final volume. Sulfur powder and BD-BBL product context belong to the exact source ingredient. Resazurin 1 mg corresponds to the stored provider 0.001 g/L."
  },
  {
    "quantity_id": "q5",
    "quantity": "Sulfur",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Sulfur (powder) 8.0 g",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[4]",
        "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"attribute\": \"powder\",\n                        \"amount\": 8,\n                        \"unit\": \"g\",\n                        \"g_l\": 8,\n                        \"mmol_l\": 249.454,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Existing G_PER_L value agrees with the provider declared 1000 mL representation, but neither layer attaches source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate addition; do not claim measured final volume. Sulfur powder and BD-BBL product context belong to the exact source ingredient. Resazurin 1 mg corresponds to the stored provider 0.001 g/L."
  },
  {
    "quantity_id": "q6",
    "quantity": "Resazurin",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main table, exact named row",
        "exact_source_quote": "Resazurin 1.0 mg",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[5]",
        "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00436319,\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Existing G_PER_L value agrees with the provider declared 1000 mL representation, but neither layer attaches source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate addition; do not claim measured final volume. Sulfur powder and BD-BBL product context belong to the exact source ingredient. Resazurin 1 mg corresponds to the stored provider 0.001 g/L."
  },
  {
    "quantity_id": "q7",
    "quantity": "Source water input",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main water row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "mediadiveJ267api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J267",
        "source_locator": "$.data.solutions[0].recipe[6]",
        "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }",
        "snapshot_sha256": "4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1"
      }
    ],
    "source_stage_and_basis": "Primary 1 L water is absent from the local representation. Provider declares 1000 mL, but water input alone does not measure final volume after later additions; retain the source basis explicitly."
  },
  {
    "quantity_id": "q8",
    "quantity": "Main target pH",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.3
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "ph_value",
        "stored": 7.3
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main preparation sentence",
        "exact_source_quote": "adjust pH to 7.3.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "Existing target pH 7.3 is source-supported as a target, not a measured growth optimum; both layers need attached evidence."
  },
  {
    "quantity_id": "q9",
    "quantity": "Preparation pH instruction",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Initial preparation sentence",
        "exact_source_quote": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "Existing preparation retains pH 7.3 and the two excluded components. No titrant identity or dose is stated."
  },
  {
    "quantity_id": "q10",
    "quantity": "Separate thioglycolate stock strength",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Separate thioglycolate preparation sentence",
        "exact_source_quote": "Separately autoclave sodium thioglycolate as 10% solution under a N 2 atmosphere.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "The 10% stock strength and N2 treatment are preserved in text; percentage basis is unspecified. Do not label it w/v or infer a numerical receiving dose from an assumed density or convention."
  },
  {
    "quantity_id": "q11",
    "quantity": "Sulfur alternative treatment",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Sulfur treatment sentence",
        "exact_source_quote": "Steam sulfur for 3 hr on each of 3 successive days.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "Existing 3 hours on each of 3 successive days is a sulfur-specific alternative, not the main autoclave cycle or a growth incubation period. Attach scoped evidence."
  },
  {
    "quantity_id": "q12",
    "quantity": "Displayed default sterilization cycle",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "sterilization_method",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "sterilization_method",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "JCM267 displayed page default header",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "The source default 121 C/15 min applies to autoclaving unless explicitly excepted. Sulfur has its own steaming treatment; do not apply the default to that exception. Neither layer preserves the numerical default."
  },
  {
    "quantity_id": "q13",
    "quantity": "Unspecified thioglycolate stock dose",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "solutions",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Last preparation sentence",
        "exact_source_quote": "Prior to inoculation, add the thioglycolate solution to the medium anaerobically.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "Source specifies stock strength and main ingredient amount but does not print a liquid stock dose or percentage basis. No numerical addition is inferred."
  },
  {
    "quantity_id": "q14",
    "quantity": "Unspecified gas amount and pH titrant",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      },
      {
        "input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
        "field_path": "preparation_steps[0].description",
        "stored": "Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution to the medium anaerobically."
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Main autoclave sentence",
        "exact_source_quote": "Autoclave the medium under a N 2 atmosphere.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      },
      {
        "source_key": "jcm267",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267",
        "source_locator": "Initial pH instruction",
        "exact_source_quote": "adjust pH to 7.3.",
        "snapshot_sha256": "22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9",
        "parsed_text_sha256": "7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d"
      }
    ],
    "source_stage_and_basis": "N2 atmosphere and pH target are explicit; absolute gas flow, pressure, titrant identity and titrant dose are not quantified. Keep existing anaerobic staging without inventing these values."
  }
]

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:002624.

13 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Canonical terms and completed current MIM lookup

grounding: concern. Targets: CultureMech:002624.

All five distinct asserted primary IDs and secondary CHEBI keys resolve to matching nonobsolete labels. Target primary and secondary linkage are each 5/6 ingredient instances (83.33% on a 0–100 scale); this measures linkage, not correctness. Four secondary keys have current index rows, while CHEBI:26833 has zero rows after a complete exact-key scan. This is a completed mapping gap, not unavailable catalog evidence. Sulfur atom is broad elemental grounding; source powder detail is missing, but no wrong allotrope or replacement ID is inferred.

### Separate kg_microbe_match assertion

graph: concern. Targets: CultureMech:002624.

Both layers assert mediadive.medium:J267. The public accession and recipe resolve, but the graph contract requires ingredient-set equality using actual graph data, which are unavailable in the bounded checkout. This does not establish a wrong match; retain the uncertainty and partial scope.

### Main source and single maintained owner

identity: supported. Targets: CultureMech:002624.

Generated and maintained records resolve to exact JCM267/MediaDive J267, with the displayed JCM source and all six source amounts inspected. No sibling variant, parent recipe or unrelated default is substituted.

### Source-specific preparation and physical form

completeness: concern. Targets: CultureMech:002624.

The single local preparation step retains pH, separate thioglycolate, sulfur steaming, anaerobic mixing and pre-inoculation addition. Missing source water, displayed numerical default and exact BD-BBL/sulfur-powder details require scoped completion; undefined 10% basis and stock dose remain unresolved. Both layers lack claim-level evidence.

### Complex liquid classification and no invented growth

scope: supported. Targets: CultureMech:002624.

Trypticase supports complex/undefined classification and the source supports a liquid medium. The broad cultivation application and medium name do not establish strain-specific growth. No taxon, DOI or PMID is asserted. pH and preparation conditions are not growth-optimum claims.

## Findings

### f1: Exact preparation context and narrow evidence are incomplete

major / open / confirmed; issue key: cm002624-source-evidence-preparation.

Both layers omit source water and the displayed 121 C/15 min default, and drop BD-BBL/sulfur-powder details. Existing quantities and preparation lack attached source evidence; the thioglycolate 10% basis and dose must remain unresolved rather than converted by assumption.

### f2: The asserted KG correspondence lacks inspected graph evidence

major / open / confirmed; issue key: cm002624-kg-match-unverified.

Source J267 identity resolves, but no actual graph comparison supports the separate kg_microbe_match assertion in either layer. Required graph files are unavailable in the bounded fresh checkout; this is an unverified assertion, not a demonstrated mismatch.

### f3: Sulfur secondary key is absent from the current pinned MIM index

minor / open / confirmed; issue key: cm002624-sulfur-secondary-gap.

CHEBI:26833 is a valid live sulfur-atom ID, but complete current pinned-index lookup finds no row for the claimed mediaingredientmech_chebi_term key. Valid primary ontology identity is distinct from current secondary membership.

## Recommended Actions And Acceptance Checks

### a1

Add narrow source evidence and missing preparation/product context in the maintained owner, respecting the sulfur exception and unquantified stock/gas/titrant details; regenerate only after review.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Every ingredient amount and preparation condition has source-specific scope; no guessed stock dose or percentage basis is introduced.

### a2

Recover the appropriately versioned MediaDive graph and verify the asserted normalized ingredient set with the actual matcher contract, recording version/input hashes; do not infer validity from shared accession alone.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Exact graph ingredient-set evidence supports or explicitly revises the assertion without treating amount equality as the contract.

### a3

Reconcile the stale or unresolved secondary membership against the maintained mapping source, preserving valid primary identity and source powder context. Do not invent a mapping or allotrope replacement.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Any secondary link has verified current mapping membership; current absence is not promoted to a claim about all historical versions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AN1_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AN1_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AN1_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch026/257/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch026/257/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AN1_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AN1_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AN1_MEDIUM.yaml:1:id: CultureMech:002624<br>./data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml:1:id: CultureMech:002624<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch026/source-preflight-bound/257/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 7 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267; Entire exact JCM recipe and displayed default header | supports | JCM 267 gives six constituents, 1 L water, pH 7.3, separate thioglycolate solution, sulfur treatment and anaerobic preparation. The displayed default autoclave header is separate from the sulfur exception. |
| api | https://mediadive.dsmz.de/rest/medium/J267; Whole medium identity, solution3955 and all preparation | supports | Provider J267 names the exact primary and declares 1000 mL. This supports its quantity representation but does not authenticate a KG graph ingredient-set match. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch026/257/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| history-metadata | data/merge_yaml/merged/AN1_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml", "events": 6, "timestamp_issues": []}] |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS identifier, canonical label, definition, synonyms and structure | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate; valid metadata is distinct from the exact source physical form and current MIM membership. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS identifier, canonical label, definition, synonyms and structure | supports | CHEBI:26710 resolves to sodium chloride; valid metadata is distinct from the exact source physical form and current MIM membership. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; Exact OLS identifier, canonical label, definition, synonyms and structure | supports | CHEBI:26833 resolves to sulfur atom; valid metadata is distinct from the exact source physical form and current MIM membership. |
| chebi86481 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481; Exact OLS identifier, canonical label, definition, synonyms and structure | supports | CHEBI:86481 resolves to sodium thioglycolate; valid metadata is distinct from the exact source physical form and current MIM membership. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS identifier, canonical label, definition, synonyms and structure | supports | CHEBI:8806 resolves to Resazurin; valid metadata is distinct from the exact source physical form and current MIM membership. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete pinned index exact identifier scan; adjacent hash/source commit | context_only | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "exact_rows": {"CHEBI:131527": [{"label": "Dibasic potassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium hydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium hydrogenorthophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium monohydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium orthophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Hydrogen dipotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K 2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO4(Sigma P 3786)", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "KH2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Phosphoric acid, dipotassium salt", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dibasic phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium monohydrogen phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium monophosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate (dibasic)", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate dibasic", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833": [], "CHEBI:86481": [{"label": "Mercaptoacetic acid, sodium salt", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Na-thioglycolate", "match_type": "preferred_term", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium 2-mercatoethanoate", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium 2-sulfanylacetate", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium mercaptoacetate", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "sodium sulfanylacetate", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium thioglycolate", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium thioglycollate", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioglycolate sodium", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Thioglycollic acid, sodium salt", "match_type": "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0,1%)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0.02%)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0.025%)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0.1% w/v in water)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0.1%)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (1 mg/L)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "resazurin sodium salt", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium resazurin", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium resazurin (0.1% w/v)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| kg-availability | /private/tmp/culturemech-review-work-batch026/257/kg-graph-availability.json; Ignored-inclusive file inventory of fresh owned checkout; exact MediaDive edges/nodes paths | context_only | {"recorded_at": "2026-10-21T14:57:07.158916+00:00", "root": "/private/tmp/culturemech-record-review-20261019-batch-026", "argv": ["rg", "--files", "--no-ignore", "--hidden", "."], "exit_code": 0, "file_count": 64849, "listing_sha256": "6d150f125714f79b5c05c8e95ca686d1d83bb3f55371f6aad80467e92d2f6c34", "matching_graph_paths": [], "scope": "Owned fresh batch026 checkout, including ignored/hidden files. No assertion about external checkouts. Search only; matcher not invoked."} |
| kg-contract | src/culturemech/match/kg_media_matcher.py; _load_kg_microbe_data, extract_recipe_ingredients, find_matches and find_exact_match | supports | Actual matcher traverses graph edges, compares extracted CHEBI/FOODON sets and ignores concentrations. It requires transformed MediaDive edges.tsv and nodes.tsv. Public source accession identity or matching current values cannot substitute for the graph comparison. |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source importer, cleanup and merge context inspected without asserting historical execution or running the graph matcher. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source importer, cleanup and merge context inspected without asserting historical execution or running the graph matcher. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source importer, cleanup and merge context inspected without asserting historical execution or running the graph matcher. |
| writer-3 | src/culturemech/match/kg_media_matcher.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current source importer, cleanup and merge context inspected without asserting historical execution or running the graph matcher. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Partial completion concerns only unavailable graph verification of the asserted kg_microbe_match. The exact JCM recipe and live ontology labels are available; CHEBI:26833 MIM absence is a completed current mapping gap, not a failed source-access check.
- Graph search included ignored and hidden files in the owned fresh batch026 checkout only. No external repository state or historical KG version is asserted.
- Main source water and provider volume are preserved without measuring final volume; unqualified thioglycolate 10%, stock dose, titrant and gas quantities are not guessed. No sulfur allotrope is inferred from the word powder.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T145820Z-culturemech-002624-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: an1_medium (CultureMech:002624)'
started_at: '2026-10-21T14:47:49Z'
finished_at: '2026-10-21T14:58:20Z'
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
summary: Exact JCM 267/MediaDive J267 identity and all six main amount representations
  resolve. Water, primary default sterilization and narrow evidence are missing; the
  sulfur secondary key has a completed current MIM mapping gap. The separate KG ingredient-set
  assertion cannot be verified without graph data, so the review is partial for that
  check.
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
  - path: .claude/skills/match-kg-microbe/SKILL.md
    sha256: add85aafc1e18164de2a9717cc9d63e5e20f34a1d597568a0c6d8b039c574a99
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
  - path: data/merge_yaml/merged/AN1_MEDIUM.yaml
    sha256: d480d73e2194ee252e40375de18d066b4abedc9a856c4fa6887cb195df4d8ecc
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
    sha256: db86279de5a6a3c9c678547333298c274dca1a9204811f2d173c632aaa736609
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/kg_microbe_matching.md
    sha256: 1b01e76b7b7b2067490b1fcd290e906b18bbebecc82ac4c607b6864708ae46c1
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
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
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
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  selection: Task review 257; batch 026 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-five task batches
    contain 250 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 253 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002624
targets:
- target_id: CultureMech:002624
  path: data/merge_yaml/merged/AN1_MEDIUM.yaml
  label: an1_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AN1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AN1_MEDIUM.yaml --workers 1
    --out /private/tmp/culturemech-review-work-batch026/257/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/257/strict.tsv"
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AN1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AN1_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:002624
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
  - CultureMech:002624
- check_id: kg-exact-match-source
  name: Exact KG ingredient-set assertion verification
  required: true
  status: unavailable
  summary: No transformed MediaDive edges.tsv/nodes.tsv were found in the fresh owned
    checkout after an ignored-inclusive search. The asserted J267 graph correspondence
    remains unverified; matcher was not invoked.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - kg-availability
  - kg-contract
  - api
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AN1_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AN1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:03.405094Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AN1_MEDIUM.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch026/257/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:05.588125Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-026/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch026/257/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AN1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:08.720809Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AN1_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:50:09.990794Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:58:17Z'
  support: supports
  summary: './data/merge_yaml/merged/AN1_MEDIUM.yaml:1:id: CultureMech:002624

    ./data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml:1:id: CultureMech:002624

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/source-preflight-bound/257/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:58:17Z'
  support: supports
  summary: 7 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: be4e415a6e512a34325f0ddfa29491a9f1439531ec65d6755cbc6844b497a43a
- evidence_id: primary
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267
  locator: Entire exact JCM recipe and displayed default header
  accessed_at: '2026-10-21T14:35:48.118918Z'
  support: supports
  summary: JCM 267 gives six constituents, 1 L water, pH 7.3, separate thioglycolate
    solution, sulfur treatment and anaerobic preparation. The displayed default autoclave
    header is separate from the sulfur exception.
  quote: Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.
  snapshot_sha256: 22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J267
  locator: Whole medium identity, solution3955 and all preparation
  accessed_at: '2026-10-21T14:35:46.581535Z'
  support: supports
  summary: Provider J267 names the exact primary and declares 1000 mL. This supports
    its quantity representation but does not authenticate a KG graph ingredient-set
    match.
  snapshot_sha256: 4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch026/257/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 7a717d5635bb94cd59ddfe3cf0264f2ef6b5aa5a9e739fd1c86efc24f48c7ff8
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AN1_MEDIUM.yaml; data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: '[{"input": "target", "events": 7, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml",
    "events": 6, "timestamp_issues": []}]'
- evidence_id: chebi131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: Exact OLS identifier, canonical label, definition, synonyms and structure
  accessed_at: '2026-10-20T07:22:08.349487Z'
  support: supports
  summary: CHEBI:131527 resolves to dipotassium hydrogen phosphate; valid metadata
    is distinct from the exact source physical form and current MIM membership.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS identifier, canonical label, definition, synonyms and structure
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride; valid metadata is distinct from
    the exact source physical form and current MIM membership.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi26833
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  locator: Exact OLS identifier, canonical label, definition, synonyms and structure
  accessed_at: '2026-10-20T06:55:04.114839Z'
  support: supports
  summary: CHEBI:26833 resolves to sulfur atom; valid metadata is distinct from the
    exact source physical form and current MIM membership.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi86481
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86481
  locator: Exact OLS identifier, canonical label, definition, synonyms and structure
  accessed_at: '2026-10-21T09:27:41.310467Z'
  support: supports
  summary: CHEBI:86481 resolves to sodium thioglycolate; valid metadata is distinct
    from the exact source physical form and current MIM membership.
  snapshot_sha256: 444afd61f333b50a1be0a902c67c78c7b97483187e4fb554b6f7deeb009cd966
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS identifier, canonical label, definition, synonyms and structure
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: CHEBI:8806 resolves to Resazurin; valid metadata is distinct from the exact
    source physical form and current MIM membership.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete pinned index exact identifier scan; adjacent hash/source commit
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "exact_rows":
    {"CHEBI:131527": [{"label": "Dibasic potassium phosphate", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium hydrogen
    phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Dipotassium hydrogenorthophosphate", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium monohydrogen
    phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Dipotassium monophosphate", "match_type": "synonym", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Dipotassium orthophosphate", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "Dipotassium phosphate", "match_type": "synonym", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Hydrogen dipotassium phosphate", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "K 2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "K2HPO", "match_type": "synonym", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "K2HPO4", "match_type": "preferred_term", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "K2HPO4(Sigma P 3786)", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label":
    "KH2HPO4", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Phosphoric acid, dipotassium salt", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium dibasic
    phosphate", "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term":
    "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Potassium monohydrogen phosphate", "match_type": "synonym",
    "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Potassium monophosphate",
    "match_type": "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4",
    "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Potassium phosphate (dibasic)", "match_type": "synonym", "identifier":
    "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Potassium phosphate dibasic", "match_type":
    "synonym", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id":
    "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "1% Sodium Chloride", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "chlorure de sodium", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "cloruro sodico",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "common salt", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Kochsalz", "match_type": "synonym", "identifier":
    "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "NaCl (Fisher S271-500)",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "NaCl(Fisher S271-500)", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "natrii chloridum", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Natriumchlorid",
    "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl",
    "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "rock salt", "match_type": "synonym", "identifier": "CHEBI:26710", "preferred_term":
    "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "salt", "match_type": "synonym", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "Sodium Chloride", "match_type": "synonym",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "table salt", "match_type":
    "synonym", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26833":
    [], "CHEBI:86481": [{"label": "Mercaptoacetic acid, sodium salt", "match_type":
    "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate",
    "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Na-thioglycolate", "match_type": "preferred_term", "identifier": "CHEBI:86481",
    "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium 2-mercatoethanoate", "match_type":
    "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate",
    "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Sodium 2-sulfanylacetate", "match_type": "synonym", "identifier": "CHEBI:86481",
    "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium mercaptoacetate", "match_type":
    "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate",
    "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "sodium sulfanylacetate", "match_type": "synonym", "identifier": "CHEBI:86481",
    "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Sodium thioglycolate", "match_type":
    "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate",
    "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Sodium thioglycollate", "match_type": "synonym", "identifier": "CHEBI:86481",
    "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Thioglycolate sodium", "match_type":
    "synonym", "identifier": "CHEBI:86481", "preferred_term": "Na-thioglycolate",
    "ontology_id": "CHEBI:86481", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Thioglycollic acid, sodium salt", "match_type": "synonym", "identifier":
    "CHEBI:86481", "preferred_term": "Na-thioglycolate", "ontology_id": "CHEBI:86481",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label":
    "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Resazurin (0,1%)", "match_type": "synonym", "identifier":
    "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0.02%)", "match_type":
    "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id":
    "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin
    (0.025%)", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Resazurin (0.1% w/v in water)", "match_type": "synonym",
    "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806",
    "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Resazurin (0.1%)",
    "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin",
    "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"},
    {"label": "Resazurin (1 mg/L)", "match_type": "synonym", "identifier": "CHEBI:8806",
    "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "resazurin sodium salt", "match_type":
    "synonym", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id":
    "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    resazurin", "match_type": "synonym", "identifier": "CHEBI:8806", "preferred_term":
    "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity":
    "unique"}, {"label": "Sodium resazurin (0.1% w/v)", "match_type": "synonym", "identifier":
    "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: kg-availability
  kind: search
  reference: /private/tmp/culturemech-review-work-batch026/257/kg-graph-availability.json
  locator: Ignored-inclusive file inventory of fresh owned checkout; exact MediaDive
    edges/nodes paths
  accessed_at: '2026-10-21T14:57:07.158916Z'
  support: context_only
  summary: '{"recorded_at": "2026-10-21T14:57:07.158916+00:00", "root": "/private/tmp/culturemech-record-review-20261019-batch-026",
    "argv": ["rg", "--files", "--no-ignore", "--hidden", "."], "exit_code": 0, "file_count":
    64849, "listing_sha256": "6d150f125714f79b5c05c8e95ca686d1d83bb3f55371f6aad80467e92d2f6c34",
    "matching_graph_paths": [], "scope": "Owned fresh batch026 checkout, including
    ignored/hidden files. No assertion about external checkouts. Search only; matcher
    not invoked."}'
  snapshot_sha256: 9b56608eecbcae98dc9681e7f7c41000d89a7a93c3038a704e215bf2c7fe24cf
  search_scope: All files under the owned batch026 checkout, including ignored and
    hidden files. Matching edges.tsv/nodes.tsv paths under MediaDive were not found;
    no claim is made about external repositories.
- evidence_id: kg-contract
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: _load_kg_microbe_data, extract_recipe_ingredients, find_matches and find_exact_match
  accessed_at: '2026-10-21T14:58:17Z'
  support: supports
  summary: Actual matcher traverses graph edges, compares extracted CHEBI/FOODON sets
    and ignores concentrations. It requires transformed MediaDive edges.tsv and nodes.tsv.
    Public source accession identity or matching current values cannot substitute
    for the graph comparison.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Current source importer, cleanup and merge context inspected without asserting
    historical execution or running the graph matcher.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Current source importer, cleanup and merge context inspected without asserting
    historical execution or running the graph matcher.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Current source importer, cleanup and merge context inspected without asserting
    historical execution or running the graph matcher.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/match/kg_media_matcher.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:58:17Z'
  support: context_only
  summary: Current source importer, cleanup and merge context inspected without asserting
    historical execution or running the graph matcher.
  snapshot_sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:002624
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
  - CultureMech:002624
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"quantity\": \"Trypticase peptone\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Trypticase peptone (BD-BBL) 10.0 g\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[0]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 1,\\n                        \\\"\
    compound\\\": \\\"Trypticase peptone\\\",\\n                        \\\"compound_id\\\
    \": 124,\\n                        \\\"attribute\\\": \\\"BD-BBL\\\",\\n     \
    \                   \\\"amount\\\": 10,\\n                        \\\"unit\\\"\
    : \\\"g\\\",\\n                        \\\"g_l\\\": 10,\\n                   \
    \     \\\"optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\"\
    : \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\n     \
    \ }\n    ],\n    \"source_stage_and_basis\": \"Existing G_PER_L value agrees with\
    \ the provider declared 1000 mL representation, but neither layer attaches source\
    \ evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate\
    \ addition; do not claim measured final volume. Sulfur powder and BD-BBL product\
    \ context belong to the exact source ingredient. Resazurin 1 mg corresponds to\
    \ the stored provider 0.001 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n\
    \    \"quantity\": \"K2HPO4\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"K 2 HPO 4 1.5 g\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[1]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 2,\\n                        \\\"\
    compound\\\": \\\"K2HPO4\\\",\\n                        \\\"compound_id\\\": 10,\\\
    n                        \\\"amount\\\": 1.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 1.5,\\n                \
    \        \\\"mmol_l\\\": 8.61198,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing G_PER_L value agrees\
    \ with the provider declared 1000 mL representation, but neither layer attaches\
    \ source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate\
    \ addition; do not claim measured final volume. Sulfur powder and BD-BBL product\
    \ context belong to the exact source ingredient. Resazurin 1 mg corresponds to\
    \ the stored provider 0.001 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q3\",\n\
    \    \"quantity\": \"NaCl\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"NaCl 2.5 g\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[2]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 3,\\n                        \\\"\
    compound\\\": \\\"NaCl\\\",\\n                        \\\"compound_id\\\": 43,\\\
    n                        \\\"amount\\\": 2.5,\\n                        \\\"unit\\\
    \": \\\"g\\\",\\n                        \\\"g_l\\\": 2.5,\\n                \
    \        \\\"mmol_l\\\": 42.7789,\\n                        \\\"optional\\\":\
    \ 0\\n                    }\",\n        \"snapshot_sha256\": \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing G_PER_L value agrees\
    \ with the provider declared 1000 mL representation, but neither layer attaches\
    \ source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate\
    \ addition; do not claim measured final volume. Sulfur powder and BD-BBL product\
    \ context belong to the exact source ingredient. Resazurin 1 mg corresponds to\
    \ the stored provider 0.001 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q4\",\n\
    \    \"quantity\": \"Sodium thioglycolate\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Sodium thioglycolate 1.0 g\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[3]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 4,\\n                        \\\"\
    compound\\\": \\\"Sodium thioglycolate\\\",\\n                        \\\"compound_id\\\
    \": 1644,\\n                        \\\"amount\\\": 1,\\n                    \
    \    \\\"unit\\\": \\\"g\\\",\\n                        \\\"g_l\\\": 1,\\n   \
    \                     \\\"mmol_l\\\": 8.76424,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing G_PER_L value agrees\
    \ with the provider declared 1000 mL representation, but neither layer attaches\
    \ source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate\
    \ addition; do not claim measured final volume. Sulfur powder and BD-BBL product\
    \ context belong to the exact source ingredient. Resazurin 1 mg corresponds to\
    \ the stored provider 0.001 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q5\",\n\
    \    \"quantity\": \"Sulfur\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Sulfur (powder) 8.0 g\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[4]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 5,\\n                        \\\"\
    compound\\\": \\\"Sulfur\\\",\\n                        \\\"compound_id\\\": 80,\\\
    n                        \\\"attribute\\\": \\\"powder\\\",\\n               \
    \         \\\"amount\\\": 8,\\n                        \\\"unit\\\": \\\"g\\\"\
    ,\\n                        \\\"g_l\\\": 8,\\n                        \\\"mmol_l\\\
    \": 249.454,\\n                        \\\"optional\\\": 0\\n                \
    \    }\",\n        \"snapshot_sha256\": \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing G_PER_L value agrees\
    \ with the provider declared 1000 mL representation, but neither layer attaches\
    \ source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate\
    \ addition; do not claim measured final volume. Sulfur powder and BD-BBL product\
    \ context belong to the exact source ingredient. Resazurin 1 mg corresponds to\
    \ the stored provider 0.001 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n\
    \    \"quantity\": \"Resazurin\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main table, exact named row\",\n        \"exact_source_quote\"\
    : \"Resazurin 1.0 mg\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[5]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 6,\\n                        \\\"\
    compound\\\": \\\"Resazurin\\\",\\n                        \\\"compound_id\\\"\
    : 25,\\n                        \\\"amount\\\": 1,\\n                        \\\
    \"unit\\\": \\\"mg\\\",\\n                        \\\"g_l\\\": 0.001,\\n     \
    \                   \\\"mmol_l\\\": 0.00436319,\\n                        \\\"\
    optional\\\": 0\\n                    }\",\n        \"snapshot_sha256\": \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing G_PER_L value agrees\
    \ with the provider declared 1000 mL representation, but neither layer attaches\
    \ source evidence. Preserve primary g/mg with 1 L water and separate later thioglycolate\
    \ addition; do not claim measured final volume. Sulfur powder and BD-BBL product\
    \ context belong to the exact source ingredient. Resazurin 1 mg corresponds to\
    \ the stored provider 0.001 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q7\",\n\
    \    \"quantity\": \"Source water input\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm267\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main water row\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"mediadiveJ267api\",\n        \"\
    source_url\": \"https://mediadive.dsmz.de/rest/medium/J267\",\n        \"source_locator\"\
    : \"$.data.solutions[0].recipe[6]\",\n        \"exact_source_quote\": \"{\\n \
    \                       \\\"recipe_order\\\": 7,\\n                        \\\"\
    compound\\\": \\\"Distilled water\\\",\\n                        \\\"compound_id\\\
    \": 4,\\n                        \\\"amount\\\": 1000,\\n                    \
    \    \\\"unit\\\": \\\"ml\\\",\\n                        \\\"optional\\\": 0\\\
    n                    }\",\n        \"snapshot_sha256\": \"4ea031a685a6910a5828d3bc51d2479036ef2ecdf1c32d499e12cf1c2200cbe1\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Primary 1 L water is absent\
    \ from the local representation. Provider declares 1000 mL, but water input alone\
    \ does not measure final volume after later additions; retain the source basis\
    \ explicitly.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"quantity\": \"\
    Main target pH\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"ph_value\",\n        \"stored\": 7.3\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": 7.3\n      }\n \
    \   ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm267\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Main preparation sentence\",\n        \"exact_source_quote\"\
    : \"adjust pH to 7.3.\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing target pH 7.3 is\
    \ source-supported as a target, not a measured growth optimum; both layers need\
    \ attached evidence.\"\n  },\n  {\n    \"quantity_id\": \"q9\",\n    \"quantity\"\
    : \"Preparation pH instruction\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to\
    \ 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium\
    \ thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on\
    \ each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture\
    \ vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate\
    \ solution to the medium anaerobically.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Mix ingredients,\
    \ except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the\
    \ medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10%\
    \ solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive\
    \ days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal\
    \ with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution\
    \ to the medium anaerobically.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Initial preparation sentence\",\n        \"exact_source_quote\"\
    : \"Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to\
    \ 7.3.\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing preparation retains\
    \ pH 7.3 and the two excluded components. No titrant identity or dose is stated.\"\
    \n  },\n  {\n    \"quantity_id\": \"q10\",\n    \"quantity\": \"Separate thioglycolate\
    \ stock strength\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to\
    \ 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium\
    \ thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on\
    \ each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture\
    \ vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate\
    \ solution to the medium anaerobically.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Mix ingredients,\
    \ except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the\
    \ medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10%\
    \ solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive\
    \ days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal\
    \ with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution\
    \ to the medium anaerobically.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Separate thioglycolate preparation sentence\"\
    ,\n        \"exact_source_quote\": \"Separately autoclave sodium thioglycolate\
    \ as 10% solution under a N 2 atmosphere.\",\n        \"snapshot_sha256\": \"\
    22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\",\n        \"\
    parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The 10% stock strength and\
    \ N2 treatment are preserved in text; percentage basis is unspecified. Do not\
    \ label it w/v or infer a numerical receiving dose from an assumed density or\
    \ convention.\"\n  },\n  {\n    \"quantity_id\": \"q11\",\n    \"quantity\": \"\
    Sulfur alternative treatment\",\n    \"decision\": \"evidence_only\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to\
    \ 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium\
    \ thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on\
    \ each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture\
    \ vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate\
    \ solution to the medium anaerobically.\"\n      },\n      {\n        \"input\"\
    : \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Mix ingredients,\
    \ except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the\
    \ medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10%\
    \ solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive\
    \ days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal\
    \ with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution\
    \ to the medium anaerobically.\"\n      }\n    ],\n    \"source_snippets\": [\n\
    \      {\n        \"source_key\": \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Sulfur treatment sentence\",\n        \"exact_source_quote\"\
    : \"Steam sulfur for 3 hr on each of 3 successive days.\",\n        \"snapshot_sha256\"\
    : \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\",\n    \
    \    \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Existing 3 hours on each\
    \ of 3 successive days is a sulfur-specific alternative, not the main autoclave\
    \ cycle or a growth incubation period. Attach scoped evidence.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q12\",\n    \"quantity\": \"Displayed default sterilization\
    \ cycle\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n   \
    \     \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"sterilization_method\",\n        \"stored\": null\n      },\n      {\n   \
    \     \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\",\n\
    \        \"field_path\": \"sterilization_method\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm267\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"JCM267 displayed page default header\",\n   \
    \     \"exact_source_quote\": \"Unless otherwise stated, sterilize media by autoclaving\
    \ at 121°C for 15 min.\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The source default 121 C/15\
    \ min applies to autoclaving unless explicitly excepted. Sulfur has its own steaming\
    \ treatment; do not apply the default to that exception. Neither layer preserves\
    \ the numerical default.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n    \"quantity\"\
    : \"Unspecified thioglycolate stock dose\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm267\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\"\
    ,\n        \"source_locator\": \"Last preparation sentence\",\n        \"exact_source_quote\"\
    : \"Prior to inoculation, add the thioglycolate solution to the medium anaerobically.\"\
    ,\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source specifies stock strength\
    \ and main ingredient amount but does not print a liquid stock dose or percentage\
    \ basis. No numerical addition is inferred.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q14\",\n    \"quantity\": \"Unspecified gas amount and pH titrant\",\n   \
    \ \"decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n      \
    \  \"input\": \"data/merge_yaml/merged/AN1_MEDIUM.yaml\",\n        \"field_path\"\
    : \"preparation_steps[0].description\",\n        \"stored\": \"Mix ingredients,\
    \ except sodium thioglycolate and sulfur, and adjust pH to 7.3. Autoclave the\
    \ medium under a N2 atmosphere. Separately autoclave sodium thioglycolate as 10%\
    \ solution under a N2 atmosphere. Steam sulfur for 3 hr on each of 3 successive\
    \ days. Under a N2 stream, mix the medium and sulfur in culture vessels and seal\
    \ with butyl rubber stoppers. Prior to inoculation, add the thioglycolate solution\
    \ to the medium anaerobically.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps[0].description\",\n        \"stored\"\
    : \"Mix ingredients, except sodium thioglycolate and sulfur, and adjust pH to\
    \ 7.3. Autoclave the medium under a N2 atmosphere. Separately autoclave sodium\
    \ thioglycolate as 10% solution under a N2 atmosphere. Steam sulfur for 3 hr on\
    \ each of 3 successive days. Under a N2 stream, mix the medium and sulfur in culture\
    \ vessels and seal with butyl rubber stoppers. Prior to inoculation, add the thioglycolate\
    \ solution to the medium anaerobically.\"\n      }\n    ],\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm267\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\",\n        \"source_locator\"\
    : \"Main autoclave sentence\",\n        \"exact_source_quote\": \"Autoclave the\
    \ medium under a N 2 atmosphere.\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      },\n      {\n        \"source_key\": \"jcm267\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=267\",\n        \"source_locator\"\
    : \"Initial pH instruction\",\n        \"exact_source_quote\": \"adjust pH to\
    \ 7.3.\",\n        \"snapshot_sha256\": \"22f70993d84abd3961b874e18bc056295b642e5001fdd8c5c55ef43b1f63aca9\"\
    ,\n        \"parsed_text_sha256\": \"7ae6d53ea033b834b4799b2feb958e350372dccb8c3b66ce73612f65a157489d\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"N2 atmosphere and pH target\
    \ are explicit; absolute gas flow, pressure, titrant identity and titrant dose\
    \ are not quantified. Keep existing anaerobic staging without inventing these\
    \ values.\"\n  }\n]"
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 13 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: grounding
  area: grounding
  topic: Canonical terms and completed current MIM lookup
  outcome: concern
  summary: All five distinct asserted primary IDs and secondary CHEBI keys resolve
    to matching nonobsolete labels. Target primary and secondary linkage are each
    5/6 ingredient instances (83.33% on a 0–100 scale); this measures linkage, not
    correctness. Four secondary keys have current index rows, while CHEBI:26833 has
    zero rows after a complete exact-key scan. This is a completed mapping gap, not
    unavailable catalog evidence. Sulfur atom is broad elemental grounding; source
    powder detail is missing, but no wrong allotrope or replacement ID is inferred.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - record
  - owner-0
  - primary
  - mim
  - chebi131527
  - chebi26710
  - chebi26833
  - chebi86481
  - chebi8806
- assessment_id: graph
  area: graph
  topic: Separate kg_microbe_match assertion
  outcome: concern
  summary: Both layers assert mediadive.medium:J267. The public accession and recipe
    resolve, but the graph contract requires ingredient-set equality using actual
    graph data, which are unavailable in the bounded checkout. This does not establish
    a wrong match; retain the uncertainty and partial scope.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - record
  - owner-0
  - api
  - kg-availability
  - kg-contract
- assessment_id: identity
  area: identity
  topic: Main source and single maintained owner
  outcome: supported
  summary: Generated and maintained records resolve to exact JCM267/MediaDive J267,
    with the displayed JCM source and all six source amounts inspected. No sibling
    variant, parent recipe or unrelated default is substituted.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
- assessment_id: preparation
  area: completeness
  topic: Source-specific preparation and physical form
  outcome: concern
  summary: The single local preparation step retains pH, separate thioglycolate, sulfur
    steaming, anaerobic mixing and pre-inoculation addition. Missing source water,
    displayed numerical default and exact BD-BBL/sulfur-powder details require scoped
    completion; undefined 10% basis and stock dose remain unresolved. Both layers
    lack claim-level evidence.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - quantity-inventory
- assessment_id: classification
  area: scope
  topic: Complex liquid classification and no invented growth
  outcome: supported
  summary: Trypticase supports complex/undefined classification and the source supports
    a liquid medium. The broad cultivation application and medium name do not establish
    strain-specific growth. No taxon, DOI or PMID is asserted. pH and preparation
    conditions are not growth-optimum claims.
  target_ids:
  - CultureMech:002624
  evidence_ids:
  - record
  - primary
  - api
findings:
- finding_id: f1
  issue_key: cm002624-source-evidence-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact preparation context and narrow evidence are incomplete
  description: Both layers omit source water and the displayed 121 C/15 min default,
    and drop BD-BBL/sulfur-powder details. Existing quantities and preparation lack
    attached source evidence; the thioglycolate 10% basis and dose must remain unresolved
    rather than converted by assumption.
  target_ids:
  - CultureMech:002624
  field_paths:
  - ingredients
  - solutions
  - sterilization_method
  - preparation_steps
  - references
  - evidence
  evidence_ids:
  - record
  - owner-0
  - primary
  - api
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
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
  issue_key: cm002624-kg-match-unverified
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: The asserted KG correspondence lacks inspected graph evidence
  description: Source J267 identity resolves, but no actual graph comparison supports
    the separate kg_microbe_match assertion in either layer. Required graph files
    are unavailable in the bounded fresh checkout; this is an unverified assertion,
    not a demonstrated mismatch.
  target_ids:
  - CultureMech:002624
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - record
  - owner-0
  - api
  - kg-availability
  - kg-contract
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
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
  issue_key: cm002624-sulfur-secondary-gap
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Sulfur secondary key is absent from the current pinned MIM index
  description: CHEBI:26833 is a valid live sulfur-atom ID, but complete current pinned-index
    lookup finds no row for the claimed mediaingredientmech_chebi_term key. Valid
    primary ontology identity is distinct from current secondary membership.
  target_ids:
  - CultureMech:002624
  field_paths:
  - ingredients[4].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - chebi26833
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
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
  description: Add narrow source evidence and missing preparation/product context
    in the maintained owner, respecting the sulfur exception and unquantified stock/gas/titrant
    details; regenerate only after review.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:002624
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
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
  - Every ingredient amount and preparation condition has source-specific scope; no
    guessed stock dose or percentage basis is introduced.
- action_id: a2
  description: Recover the appropriately versioned MediaDive graph and verify the
    asserted normalized ingredient set with the actual matcher contract, recording
    version/input hashes; do not infer validity from shared accession alone.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:002624
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
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
  - Exact graph ingredient-set evidence supports or explicitly revises the assertion
    without treating amount equality as the contract.
- action_id: a3
  description: Reconcile the stale or unresolved secondary membership against the
    maintained mapping source, preserving valid primary identity and source powder
    context. Do not invent a mapping or allotrope replacement.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:002624
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J267_AN1_MEDIUM.yaml
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
  - Any secondary link has verified current mapping membership; current absence is
    not promoted to a claim about all historical versions.
limitations:
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Partial completion concerns only unavailable graph verification of the asserted
  kg_microbe_match. The exact JCM recipe and live ontology labels are available; CHEBI:26833
  MIM absence is a completed current mapping gap, not a failed source-access check.
- Graph search included ignored and hidden files in the owned fresh batch026 checkout
  only. No external repository state or historical KG version is asserted.
- Main source water and provider volume are preserved without measuring final volume;
  unqualified thioglycolate 10%, stock dose, titrant and gas quantities are not guessed.
  No sulfur allotrope is inferred from the word powder.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-026
- generated-medium
```
