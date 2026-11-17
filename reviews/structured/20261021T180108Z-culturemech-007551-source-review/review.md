# Source and formulation review: artificial_seawater_medium_with_pullulan (CultureMech:007551)

- Review: 20261021T180108Z-culturemech-007551-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T17:54:24Z
- Finished UTC: 2026-10-21T18:01:08Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM 983 and exact TOGO M1036 resolve the medium, but its water, resazurin and stock doses use the wrong quantity representation. Seven empty stock slots and absent preparation obscure the source formulation. Scoped parent evidence supports stock reconstruction while exposing cobalt/nickel hydrate mismatches; no final volume or unspecified percentage basis is inferred.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 313; batch 032 item 3 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-one task batches contain 310 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 313 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007551 | data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml | generated | artificial_seawater_medium_with_pullulan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007551 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007551 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch032/313/strict.tsv |
| validate-terms | passed | True | CultureMech:007551 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007551 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007551 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: mediadiveJ983api | unavailable | False | CultureMech:007551 | Optional alternate source attempt mediadiveJ983api did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| Exact source content access: mediadiveJ983api_retry | unavailable | False | CultureMech:007551 | Optional alternate source attempt mediadiveJ983api_retry did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| Exact source content access: togoM1036 | unavailable | False | CultureMech:007551 | Optional alternate source attempt togoM1036 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| Exact source content access: togoM1036page | unavailable | False | CultureMech:007551 | Optional alternate source attempt togoM1036page did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| Exact source content access: togoM180 | unavailable | False | CultureMech:007551 | Optional alternate source attempt togoM180 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| Exact source content access: togoM431 | unavailable | False | CultureMech:007551 | Optional alternate source attempt togoM431 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| Exact source content access: togoM190 | unavailable | False | CultureMech:007551 | Optional alternate source attempt togoM190 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007551.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:007551.

55 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "ingredient_or_context": "Distilled water",
    "field_path": "ingredients[0].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "L",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Source water is 1 L of batch input, not 1 g/L or a measured final litre."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Source water is 1 L of batch input, not 1 g/L or a measured final litre."
      }
    ],
    "arithmetic_and_scope": "Source water is 1 L of batch input, not 1 g/L or a measured final litre."
  },
  {
    "quantity_id": "q2",
    "ingredient_or_context": "MgSO4・7H2O",
    "field_path": "ingredients[1].concentration",
    "local": {
      "value": "25",
      "unit": "G_PER_L"
    },
    "source_amount": 25,
    "source_unit": "g",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "MgSO 4 ·7H 2 O 25.0 g",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "25",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      }
    ],
    "arithmetic_and_scope": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
  },
  {
    "quantity_id": "q3",
    "ingredient_or_context": "NaCl",
    "field_path": "ingredients[2].concentration",
    "local": {
      "value": "80",
      "unit": "G_PER_L"
    },
    "source_amount": 80,
    "source_unit": "g",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "NaCl 80.0 g",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 80,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "80",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "80",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      }
    ],
    "arithmetic_and_scope": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
  },
  {
    "quantity_id": "q4",
    "ingredient_or_context": "CaCl2・2H2O",
    "field_path": "ingredients[3].concentration",
    "local": {
      "value": "4.5",
      "unit": "G_PER_L"
    },
    "source_amount": 4.5,
    "source_unit": "g",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "CaCl 2 ·2H 2 O 4.5 g",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 4.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "4.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      }
    ],
    "arithmetic_and_scope": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
  },
  {
    "quantity_id": "q5",
    "ingredient_or_context": "Resazurin",
    "field_path": "ingredients[4].concentration",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_amount": 0.5,
    "source_unit": "mg",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "Resazurin 0.5 mg",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Source 0.5 mg equals 0.0005 g per batch. The local 0.5 G_PER_L loses the milligram scale and assumes a final-litre basis; on the same nominal litre basis the numeric mass is 1000-fold larger."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Source 0.5 mg equals 0.0005 g per batch. The local 0.5 G_PER_L loses the milligram scale and assumes a final-litre basis; on the same nominal litre basis the numeric mass is 1000-fold larger."
      }
    ],
    "arithmetic_and_scope": "Source 0.5 mg equals 0.0005 g per batch. The local 0.5 G_PER_L loses the milligram scale and assumes a final-litre basis; on the same nominal litre basis the numeric mass is 1000-fold larger."
  },
  {
    "quantity_id": "q6",
    "ingredient_or_context": "KCl",
    "field_path": "ingredients[5].concentration",
    "local": {
      "value": "1.5",
      "unit": "G_PER_L"
    },
    "source_amount": 1.5,
    "source_unit": "g",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "KCl 1.5 g",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "1.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      }
    ],
    "arithmetic_and_scope": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
  },
  {
    "quantity_id": "q7",
    "ingredient_or_context": "Pullulan",
    "field_path": "ingredients[6].concentration",
    "local": {
      "value": "0.5",
      "unit": "G_PER_L"
    },
    "source_amount": 0.5,
    "source_unit": "g",
    "source_stage": "Initial main batch",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "Pullulan 0.5 g",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Pullulan\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
      }
    ],
    "arithmetic_and_scope": "The number matches the source batch mass, but G_PER_L asserts an unestablished final-volume denominator. Preserve the literal batch amount and source stage; do not divide by the listed liquid-input sum as if measured final volume."
  },
  {
    "quantity_id": "q8",
    "ingredient_or_context": "Carbon dioxide amount",
    "field_path": "ingredients[7].concentration",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_amount": null,
    "source_unit": "unquantified gas amount",
    "source_stage": "Initial main atmosphere",
    "primary_source_evidence_id": "jcm983",
    "decision": "not_quantified",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "First preparation sentence",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "No fixed amount of this gas is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent the ratio in preparation rather than inventing dissolved concentration or flow."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "No fixed amount of this gas is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent the ratio in preparation rather than inventing dissolved concentration or flow."
      }
    ],
    "arithmetic_and_scope": "No fixed amount of this gas is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent the ratio in preparation rather than inventing dissolved concentration or flow."
  },
  {
    "quantity_id": "q9",
    "ingredient_or_context": "Nitrogen amount",
    "field_path": "ingredients[8].concentration",
    "local": {
      "value": "variable",
      "unit": "VARIABLE"
    },
    "source_amount": null,
    "source_unit": "unquantified gas amount",
    "source_stage": "Initial main atmosphere",
    "primary_source_evidence_id": "jcm983",
    "decision": "not_quantified",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "First preparation sentence",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "No fixed amount of this gas is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent the ratio in preparation rather than inventing dissolved concentration or flow."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        },
        "decision": "not_quantified",
        "rationale": "No fixed amount of this gas is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent the ratio in preparation rather than inventing dissolved concentration or flow."
      }
    ],
    "arithmetic_and_scope": "No fixed amount of this gas is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent the ratio in preparation rather than inventing dissolved concentration or flow."
  },
  {
    "quantity_id": "q10",
    "ingredient_or_context": "FeCl2 solution (see Medium [M180])",
    "field_path": "solutions[0].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "ml",
    "source_stage": "Initial main addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "FeCl 2 solution (see Medium No. 187 ) 1.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q11",
    "ingredient_or_context": "Trace element solution (see Medium [M180])",
    "field_path": "solutions[1].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "ml",
    "source_stage": "Initial main addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "Trace element solution (see Medium No. 187 ) 1.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q12",
    "ingredient_or_context": "Selenite--tungstate solution (see Medium [M431])",
    "field_path": "solutions[2].concentration",
    "local": {
      "value": "1",
      "unit": "G_PER_L"
    },
    "source_amount": 1,
    "source_unit": "ml",
    "source_stage": "Initial main addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "Selenite-tungstate solution (see Medium No. 431 ) 1.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q13",
    "ingredient_or_context": "5% Na2CO3 solution",
    "field_path": "solutions[3].concentration",
    "local": {
      "value": "20",
      "unit": "G_PER_L"
    },
    "source_amount": 20,
    "source_unit": "ml",
    "source_stage": "Post-autoclave addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "5% Na 2 CO 3 solution 20.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"5% Na2CO3 solution\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 20 mL = 0.02 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 20 mL = 0.02 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 20 mL = 0.02 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q14",
    "ingredient_or_context": "1% NH4Cl solution",
    "field_path": "solutions[4].concentration",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_amount": 10,
    "source_unit": "ml",
    "source_stage": "Post-autoclave addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "1% NH 4 Cl solution 10.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"1% NH4Cl solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q15",
    "ingredient_or_context": "1% KH2PO4 solution",
    "field_path": "solutions[5].concentration",
    "local": {
      "value": "5",
      "unit": "G_PER_L"
    },
    "source_amount": 5,
    "source_unit": "ml",
    "source_stage": "Post-autoclave addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "1% KH 2 PO 4 solution 5.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"1% KH2PO4 solution\",\n          \"volume\": 5,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 5 mL = 0.005 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "5",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 5 mL = 0.005 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 5 mL = 0.005 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q16",
    "ingredient_or_context": "Trace vitamins (see Medium [M190])",
    "field_path": "solutions[6].concentration",
    "local": {
      "value": "10",
      "unit": "G_PER_L"
    },
    "source_amount": 10,
    "source_unit": "ml",
    "source_stage": "Post-autoclave addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "Trace vitamins* (see Medium No. 197 ) 10.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "The source dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
      }
    ],
    "arithmetic_and_scope": "The source dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final litre. Keep stock composition and receiving addition separate."
  },
  {
    "quantity_id": "q17",
    "ingredient_or_context": "5% sodium sulfide nonahydrate solution dose",
    "field_path": "ingredients[9].concentration",
    "local": {
      "value": "6",
      "unit": "G_PER_L"
    },
    "source_amount": 6,
    "source_unit": "ml",
    "source_stage": "Post-autoclave addition",
    "primary_source_evidence_id": "jcm983",
    "decision": "correct",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "5% Na 2 S·9H 2 O 6.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "togoM1036original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"5% Na2S・9H2O\",\n          \"volume\": 6,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Source 6 mL = 0.006 L is an addition of the separately prepared 5% sulfide solution. It is not 6 g/L sulfide; the percentage basis is unspecified."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "Source 6 mL = 0.006 L is an addition of the separately prepared 5% sulfide solution. It is not 6 g/L sulfide; the percentage basis is unspecified."
      }
    ],
    "arithmetic_and_scope": "Source 6 mL = 0.006 L is an addition of the separately prepared 5% sulfide solution. It is not 6 g/L sulfide; the percentage basis is unspecified."
  },
  {
    "quantity_id": "q18",
    "ingredient_or_context": "FeCl2 stock: 25% HCl (7.7 M)",
    "field_path": "solutions[0].composition",
    "local": [],
    "source_amount": 10,
    "source_unit": "ml",
    "source_stage": "FeCl2 stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock table",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].solutions[0].concentration",
        "stored": {
          "value": "0.01",
          "unit": "L"
        },
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q19",
    "ingredient_or_context": "FeCl2 stock: Distilled water",
    "field_path": "solutions[0].composition",
    "local": [],
    "source_amount": 990,
    "source_unit": "ml",
    "source_stage": "FeCl2 stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock table",
        "exact_source_quote": "Distilled water 990.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].composition[0].concentration",
        "stored": {
          "value": "0.99",
          "unit": "L"
        },
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q20",
    "ingredient_or_context": "FeCl2 stock: FeCl2・4H2O",
    "field_path": "solutions[0].composition",
    "local": [],
    "source_amount": 1.5,
    "source_unit": "g",
    "source_stage": "FeCl2 stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock table",
        "exact_source_quote": "FeCl 2 ·4H 2 O 1.5 g",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].composition[1].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q21",
    "ingredient_or_context": "Trace element stock: Distilled water",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 1,
    "source_unit": "L",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q22",
    "ingredient_or_context": "Trace element stock: Na2MoO4・2H2O",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 36,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q23",
    "ingredient_or_context": "Trace element stock: H3BO3",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 6,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "H 3 BO 3 6.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q24",
    "ingredient_or_context": "Trace element stock: MnCl2・4H2O",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 100,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "MnCl 2 ·4H 2 O 100.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q25",
    "ingredient_or_context": "Trace element stock: CoCl2・6H2O",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 190,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "CoCl 2 ·6H 2 O 190.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[4]",
        "exact_source_quote": "\"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q26",
    "ingredient_or_context": "Trace element stock: NiCl2・6H2O",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 24,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "NiCl 2 ·6H 2 O 24.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[5]",
        "exact_source_quote": "\"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q27",
    "ingredient_or_context": "Trace element stock: CuCl2・2H2O",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 2,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "CuCl 2 ·2H 2 O 2.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[6]",
        "exact_source_quote": "\"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q28",
    "ingredient_or_context": "Trace element stock: ZnCl2",
    "field_path": "solutions[1].composition",
    "local": [],
    "source_amount": 70,
    "source_unit": "mg",
    "source_stage": "Trace element stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element stock table",
        "exact_source_quote": "ZnCl 2 70.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      },
      {
        "source_key": "togoM180original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180",
        "source_locator": "$.components[2].items[7]",
        "exact_source_quote": "\"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[1].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q29",
    "ingredient_or_context": "Selenite-tungstate stock: Distilled water",
    "field_path": "solutions[2].composition",
    "local": [],
    "source_amount": 1,
    "source_unit": "L",
    "source_stage": "Selenite-tungstate stock",
    "primary_source_evidence_id": "jcm431",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate stock table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "989.0",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "This dependency still flattens the named stock into its main ingredients; restore the stock stage and original unit. Its combined water value also contains other source stages and cannot be copied."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q30",
    "ingredient_or_context": "Selenite-tungstate stock: Na2SeO3・5H2O",
    "field_path": "solutions[2].composition",
    "local": [],
    "source_amount": 6,
    "source_unit": "mg",
    "source_stage": "Selenite-tungstate stock",
    "primary_source_evidence_id": "jcm431",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate stock table",
        "exact_source_quote": "Na 2 SeO 3 ·5H 2 O 6.0 mg",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[1]",
        "exact_source_quote": "\"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[27].concentration",
        "stored": {
          "value": "6",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "This dependency still flattens the named stock into its main ingredients; restore the stock stage and original unit. Its combined water value also contains other source stages and cannot be copied."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q31",
    "ingredient_or_context": "Selenite-tungstate stock: Na2WO4・2H2O",
    "field_path": "solutions[2].composition",
    "local": [],
    "source_amount": 8,
    "source_unit": "mg",
    "source_stage": "Selenite-tungstate stock",
    "primary_source_evidence_id": "jcm431",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate stock table",
        "exact_source_quote": "Na 2 WO 4 ·2H 2 O 8.0 mg",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[28].concentration",
        "stored": {
          "value": "8",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "This dependency still flattens the named stock into its main ingredients; restore the stock stage and original unit. Its combined water value also contains other source stages and cannot be copied."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q32",
    "ingredient_or_context": "Selenite-tungstate stock: NaOH",
    "field_path": "solutions[2].composition",
    "local": [],
    "source_amount": 0.4,
    "source_unit": "g",
    "source_stage": "Selenite-tungstate stock",
    "primary_source_evidence_id": "jcm431",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate stock table",
        "exact_source_quote": "NaOH 0.4 g",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      },
      {
        "source_key": "togoM431original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431",
        "source_locator": "$.components[3].items[3]",
        "exact_source_quote": "\"component_name\": \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[2].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml",
        "field_path": "ingredients[29].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        },
        "decision": "correct",
        "rationale": "This dependency still flattens the named stock into its main ingredients; restore the stock stage and original unit. Its combined water value also contains other source stages and cannot be copied."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q33",
    "ingredient_or_context": "Trace-vitamin stock: Distilled water",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 1,
    "source_unit": "L",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[0].concentration",
        "stored": {
          "value": "1",
          "unit": "L"
        },
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q34",
    "ingredient_or_context": "Trace-vitamin stock: Biotin",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 2,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Biotin 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[1].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q35",
    "ingredient_or_context": "Trace-vitamin stock: p--Aminobenzoic acid",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 5,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "p -Aminobenzoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[2].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q36",
    "ingredient_or_context": "Trace-vitamin stock: Thiamine・HCl",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 5,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Thiamine·HCl 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[3].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q37",
    "ingredient_or_context": "Trace-vitamin stock: Calcium pantothenate",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 5,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Calcium pantothenate 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[4].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q38",
    "ingredient_or_context": "Trace-vitamin stock: Pyridoxine・HCl",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 10,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Pyridoxine·HCl 10.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[5].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q39",
    "ingredient_or_context": "Trace-vitamin stock: Folic acid",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 2,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Folic acid 2.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[6].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q40",
    "ingredient_or_context": "Trace-vitamin stock: Vitamin B12",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 0.1,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Vitamin B 1 2 0.1 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[7].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q41",
    "ingredient_or_context": "Trace-vitamin stock: Riboflavin",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 5,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Riboflavin 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[8].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q42",
    "ingredient_or_context": "Trace-vitamin stock: Nicotinic acid",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 5,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Nicotinic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[9].notes",
        "stored": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q43",
    "ingredient_or_context": "Trace-vitamin stock: Lipoic acid",
    "field_path": "solutions[6].composition",
    "local": [],
    "source_amount": 5,
    "source_unit": "mg",
    "source_stage": "Trace-vitamin stock",
    "primary_source_evidence_id": "jcm197",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm197",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197",
        "source_locator": "Trace-vitamin stock table",
        "exact_source_quote": "Lipoic acid 5.0 mg",
        "snapshot_sha256": "39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532",
        "parsed_text_sha256": "818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f"
      },
      {
        "source_key": "togoM190original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
        "source_locator": "$.components[1].items[10]",
        "exact_source_quote": "\"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[6].composition",
        "stored": [],
        "decision": "add",
        "rationale": "The stock composition is empty here; add only this named source-stock ingredient with its stage and evidence."
      },
      {
        "input": "data/normalized_yaml/bacterial/togo_medium_m190.yaml",
        "field_path": "solutions[1].composition[10].notes",
        "stored": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
        "decision": "verified",
        "rationale": "This exact scoped quantity is already preserved in the dependency field with matching attached source evidence; verification does not establish chemical-form correctness or a target receiving concentration."
      }
    ],
    "arithmetic_and_scope": "Retain this literal stock-batch input and supplied form separately from its receiving dose. Input water is not an independently measured final stock volume; no final-medium concentration is calculated."
  },
  {
    "quantity_id": "q44",
    "ingredient_or_context": "Fe-stock HCl reagent molarity",
    "field_path": "solutions[0].composition",
    "local": [],
    "source_amount": 7.7,
    "source_unit": "M",
    "source_stage": "HCl reagent before its 10 mL stock addition",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock table",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "Retain explicit reagent strength inside the Fe stock, not as a main-medium concentration."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "Retain explicit reagent strength inside the Fe stock, not as a main-medium concentration."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].solutions[0].composition[0].concentration",
        "stored": {
          "value": "7.7",
          "unit": "MOLAR"
        },
        "decision": "verified",
        "rationale": "Existing 7.7 MOLAR reagent field has both exact provider and primary attached support."
      }
    ],
    "arithmetic_and_scope": "7.7 M is stated directly. It is not inferred by converting the unqualified 25% label; no acid density is assumed."
  },
  {
    "quantity_id": "q45",
    "ingredient_or_context": "Carbonate nominal stock-strength label",
    "field_path": "solutions[3].preferred_term",
    "local": "5% Na2CO3 solution",
    "source_amount": 5,
    "source_unit": "% (basis unspecified)",
    "source_stage": "Separate reagent stock",
    "primary_source_evidence_id": "jcm983",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "5% Na 2 CO 3 solution 20.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[3].preferred_term",
        "stored": "5% Na2CO3 solution",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[3].preferred_term",
        "stored": "5% Na2CO3 solution",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      }
    ],
    "arithmetic_and_scope": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
  },
  {
    "quantity_id": "q46",
    "ingredient_or_context": "Ammonium chloride nominal stock-strength label",
    "field_path": "solutions[4].preferred_term",
    "local": "1% NH4Cl solution",
    "source_amount": 1,
    "source_unit": "% (basis unspecified)",
    "source_stage": "Separate reagent stock",
    "primary_source_evidence_id": "jcm983",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "1% NH 4 Cl solution 10.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[4].preferred_term",
        "stored": "1% NH4Cl solution",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[4].preferred_term",
        "stored": "1% NH4Cl solution",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      }
    ],
    "arithmetic_and_scope": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
  },
  {
    "quantity_id": "q47",
    "ingredient_or_context": "Potassium phosphate nominal stock-strength label",
    "field_path": "solutions[5].preferred_term",
    "local": "1% KH2PO4 solution",
    "source_amount": 1,
    "source_unit": "% (basis unspecified)",
    "source_stage": "Separate reagent stock",
    "primary_source_evidence_id": "jcm983",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "1% KH 2 PO 4 solution 5.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[5].preferred_term",
        "stored": "1% KH2PO4 solution",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[5].preferred_term",
        "stored": "1% KH2PO4 solution",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      }
    ],
    "arithmetic_and_scope": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
  },
  {
    "quantity_id": "q48",
    "ingredient_or_context": "Sulfide nominal stock-strength label",
    "field_path": "ingredients[9].preferred_term",
    "local": "5% Na2S・9H2O",
    "source_amount": 5,
    "source_unit": "% (basis unspecified)",
    "source_stage": "Separate reagent stock",
    "primary_source_evidence_id": "jcm983",
    "decision": "evidence_only",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "5% Na 2 S·9H 2 O 6.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ingredients[9].preferred_term",
        "stored": "5% Na2S・9H2O",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ingredients[9].preferred_term",
        "stored": "5% Na2S・9H2O",
        "decision": "evidence_only",
        "rationale": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
      }
    ],
    "arithmetic_and_scope": "The percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do not convert to grams or molarity."
  },
  {
    "quantity_id": "q49",
    "ingredient_or_context": "HCl nominal percentage label",
    "field_path": "solutions[0].composition",
    "local": [],
    "source_amount": 25,
    "source_unit": "% (basis unspecified)",
    "source_stage": "HCl reagent for Fe stock",
    "primary_source_evidence_id": "jcm187",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock table",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "Retain the source label without converting an unknown percent basis."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "solutions[0].composition",
        "stored": [],
        "decision": "add",
        "rationale": "Retain the source label without converting an unknown percent basis."
      },
      {
        "input": "data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml",
        "field_path": "solutions[0].solutions[0].composition[0].preferred_term",
        "stored": "25% HCl (7.7 M)",
        "decision": "verified",
        "rationale": "The literal label is retained with attached exact support; the explicit molarity is separate."
      }
    ],
    "arithmetic_and_scope": "The fixed 10 mL dose and independently explicit 7.7 M strength do not resolve the source percent basis."
  },
  {
    "quantity_id": "q50",
    "ingredient_or_context": "Basal gas ratio",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": "4:1",
    "source_unit": "v/v N2:CO2",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "jcm983",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Preparation/default text",
        "exact_source_quote": "N 2 -CO 2 (4:1, v/v) gas mixture",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Main mixture autoclaved under the stated volumetric ratio; 80:20 is equivalent arithmetic, not a measured gas dose."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Main mixture autoclaved under the stated volumetric ratio; 80:20 is equivalent arithmetic, not a measured gas dose."
      }
    ],
    "arithmetic_and_scope": "Main mixture autoclaved under the stated volumetric ratio; 80:20 is equivalent arithmetic, not a measured gas dose."
  },
  {
    "quantity_id": "q51",
    "ingredient_or_context": "Collection default autoclave temperature",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 121,
    "source_unit": "°C",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "jcm983",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Preparation/default text",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Collection default applies to specified autoclaving; it does not replace the vitamin filtration exception."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Collection default applies to specified autoclaving; it does not replace the vitamin filtration exception."
      }
    ],
    "arithmetic_and_scope": "Collection default applies to specified autoclaving; it does not replace the vitamin filtration exception."
  },
  {
    "quantity_id": "q52",
    "ingredient_or_context": "Collection default autoclave duration",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 15,
    "source_unit": "min",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "jcm983",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Preparation/default text",
        "exact_source_quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Retain this source-specific default with the appropriate autoclave stage."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Retain this source-specific default with the appropriate autoclave stage."
      }
    ],
    "arithmetic_and_scope": "Retain this source-specific default with the appropriate autoclave stage."
  },
  {
    "quantity_id": "q53",
    "ingredient_or_context": "Main pH range",
    "field_path": "ph_range",
    "local": null,
    "source_amount": "7.2–7.5",
    "source_unit": "pH",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "jcm983",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Preparation/default text",
        "exact_source_quote": "Adjust pH to 7.2 - 7.5 with a 5% Na 2 CO 3 solution, if necessary.",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve the range, without a midpoint or an invented incubation optimum."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "ph_range",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve the range, without a midpoint or an invented incubation optimum."
      }
    ],
    "arithmetic_and_scope": "Preserve the range, without a midpoint or an invented incubation optimum."
  },
  {
    "quantity_id": "q54",
    "ingredient_or_context": "Optional carbonate adjustment",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": null,
    "source_unit": "unquantified additional dose",
    "source_stage": "Main preparation",
    "primary_source_evidence_id": "jcm983",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Preparation/default text",
        "exact_source_quote": "Adjust pH to 7.2 - 7.5 with a 5% Na 2 CO 3 solution, if necessary.",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "The initial 20 mL carbonate addition is separate from any additional adjustment. No fixed adjustment dose or percent basis is supplied."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "The initial 20 mL carbonate addition is separate from any additional adjustment. No fixed adjustment dose or percent basis is supplied."
      }
    ],
    "arithmetic_and_scope": "The initial 20 mL carbonate addition is separate from any additional adjustment. No fixed adjustment dose or percent basis is supplied."
  },
  {
    "quantity_id": "q55",
    "ingredient_or_context": "Listed liquid inputs; unresolved final volume",
    "field_path": "preparation_steps",
    "local": null,
    "source_amount": 1054,
    "source_unit": "mL listed input sum",
    "source_stage": "Across initial and later additions",
    "primary_source_evidence_id": "jcm983",
    "decision": "add",
    "source_snippets": [
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Main table",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Later-addition table",
        "exact_source_quote": "1% NH 4 Cl solution 10.0 ml 1% KH 2 PO 4 solution 5.0 ml Trace vitamins* (see Medium No. 197 ) 10.0 ml 5% Na 2 CO 3 solution 20.0 ml 5% Na 2 S·9H 2 O 6.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      },
      {
        "source_key": "jcm983",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983",
        "source_locator": "Initial stock rows; all three are 1 mL",
        "exact_source_quote": "Selenite-tungstate solution (see Medium No. 431 ) 1.0 ml",
        "snapshot_sha256": "0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9",
        "parsed_text_sha256": "f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c"
      }
    ],
    "layer_decisions": [
      {
        "input": "target",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve the ordered additions without asserting a final denominator."
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
        "field_path": "preparation_steps",
        "stored": null,
        "decision": "add",
        "rationale": "Preserve the ordered additions without asserting a final denominator."
      }
    ],
    "arithmetic_and_scope": "1000 + 1 + 1 + 1 + 10 + 5 + 10 + 20 + 6 = 1054 mL of listed liquid inputs, before optional carbonate adjustment. This sum is not a measured final volume and cannot justify g/L normalization."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:007551.

9 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 9/10 primary and 5/10 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 10: primary 90.00%; secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:007551.

23 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact main accession and maintained owner

identity: supported. Targets: CultureMech:007551.

CultureMech:007551 resolves to TOGO M1036 and JCM983. The sole maintained contributor shares its stable ID, name and retained import event; the generated record adds merge metadata. Parent M180/M431/M190 records are stock dependencies, not interchangeable media or additional owners.

### All amounts and source stages

consistency: concern. Targets: CultureMech:007551.

Every target and owner concentration is covered by the quantity inventory. The five unchanged numeric gram amounts retain unsupported final-litre denominators; water, resazurin and eight liquid additions also lose their original units. No amount is declared verified on the target or owner because neither attaches supporting formulation evidence. The source liquid-input sum is not a final-volume measurement.

### Seven empty stock slots and four bounded parent formulations

completeness: concern. Targets: CultureMech:007551.

Four referenced stock batches can be recovered from exact J187/J431/J197 sections; three percentage-labelled main stock slots and the separate sulfide reagent retain uncertain percent bases. M180 and M190 have corrected stock quantities and attached evidence in scope, whereas M431 still flattens the selenite-tungstate ingredients. Transfer only these named sections, preserving their own doses and stages.

### Sterilization, anaerobic addition order and pH

completeness: concern. Targets: CultureMech:007551.

Neither local layer contains preparation_steps or ph_range. J983 explicitly autoclaves the initial mixture under N2:CO2 4:1 v/v, then adds separately autoclaved or marked filter-sterilized solutions anaerobically after N2 storage. Vitamins carry the filtration marker. The collection default is 121°C for 15 min where autoclaving applies; gas purity, pressure, filtration pore size, incubation temperature and duration are not supplied.

### Chemical forms on transferred stock dependencies

grounding: concern. Targets: CultureMech:007551.

The target empty stocks do not assert these dependent term IDs. Before populating them, resolve M180 source CoCl2·6H2O and NiCl2·6H2O being assigned to the anhydrous terms CHEBI:35696 and CHEBI:34887. M190 calcium pantothenate at 5 mg has a stereospecific D structural term CHEBI:31345 while the source names no isomer; this is unresolved specificity, not proof that D is wrong. Other target hydrated salts match their source forms; no new IDs are proposed.

### Existing evidence and precise transfer limits

evidence: concern. Targets: CultureMech:007551.

The target and owner retain source URLs in notes but no ingredient or stock-dose evidence. Twenty-three existing parent-stock evidence objects are authenticated only in their original scopes. Root references and exact narrow evidence should accompany later authorized repairs; one parent source citation cannot support its whole medium or a different stock. Current access failures are retained separately from successful exact primaries and original TOGO responses.

### Record category, composition and growth boundaries

scope: concern. Targets: CultureMech:007551.

LIQUID is compatible with the source formulation. The current TOGO category inference defaults to bacterial; this is filing metadata, not a demonstrated organism range. COMPLEX/UNDEFINED lacks an explicit source classification rationale; pullulan is a polymer, so a defined/complex replacement is not prescribed without a documented local definition and product context. No target organism, strain, DOI/PMID, growth result, variant, high_metal or kg_microbe_match is asserted by this target. Parent growth conditions and legacy sulfur links do not transfer.

### Current import, migration, merge and export responsibilities

provenance: supported. Targets: CultureMech:007551.

Repair the maintained M1036 owner and only the identified dependency assertions before authorized regeneration. The existing migration event and current copy logic explain why empty topology alone is insufficient; current importer code and evidence-aware merge behavior do not authenticate an unknown old response. Numeric/string field preservation by an exporter is not scientific validation.

## Findings

### f1: Wrong units and stock doses make the stored formulation unusable

blocker / open / confirmed; issue key: cm007551-main-units-and-basis.

Both local layers encode 1 L water as 1 G_PER_L, 0.5 mg resazurin as 0.5 G_PER_L, and all eight receiving liquid additions as G_PER_L. The five correctly transcribed numeric gram amounts also lack an established final-litre denominator. These are dimensional and preparation-scale changes, not a harmless naming issue; a faithful source recipe cannot be reconstructed by reading these quantities literally.

### f2: Named source stocks remain empty and cannot inherit unrelated parent recipes

major / open / confirmed; issue key: cm007551-stock-completeness.

Seven Unknown solution slots have empty compositions despite four explicitly recoverable stock formulations. The M431 dependency still carries selenite-tungstate solutes in its flattened main ingredient list, including mg-to-G_PER_L and combined-water artifacts. M180 and M190 provide useful scoped existing evidence, but their parent main recipes, receiving doses, sulfur links and unrelated minerals are not this medium.

### f3: Missing preparation loses sterilization exceptions, gas ratio and pH

major / open / confirmed; issue key: cm007551-source-preparation-omission.

Both layers omit the entire source preparation: initial autoclaving under N2:CO2 4:1 v/v, source default 121°C/15 min, later anaerobic additions and N2 storage, specifically filtered vitamins, and pH 7.2–7.5 with optional further 5% carbonate. Omission materially changes how the recipe would be prepared; no generic stock or parent cycle can safely substitute.

### f4: Referenced trace-stock hydrate identities conflict with captured ontology structures

major / open / confirmed; issue key: cm007551-dependent-hydrate-grounding.

M180 solutions[1].composition[4] and [5] name cobalt chloride hexahydrate and nickel chloride hexahydrate, corroborated by J187 and the exact provider. Their CHEBI:35696 and CHEBI:34887 terms instead encode anhydrous chlorides. These are dependency assertions that must not be copied into the currently empty target stock. Separately, generic source calcium pantothenate does not establish the D stereochemistry encoded by M190 CHEBI:31345; that narrower point remains an unresolved support limit.

## Recommended Actions And Acceptance Checks

### a1

Restore literal batch quantities and receiving stock volumes in the maintained owner with claim-level evidence. Preserve mg versus g, batch input versus concentration and the unknown final volume. Reconcile the owner before regenerating the merged record.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Populate or reference only the named Fe, trace-element, selenite-tungstate and trace-vitamin stock sections; preserve the separate percentage-labelled reagents without an invented basis. Reconcile the scoped M431 stock representation and recheck dependency terms before reuse.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Restore the exact source sequence, main pH range and stock-specific sterilization/storage qualifiers. Keep the unspecified additional carbonate dose, unqualified percent bases and unknown gas amount explicit.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Check and correct the two exact M180 hydrate term assignments using source-specific ontology evidence before stock reuse; preserve masses. Resolve the calcium-pantothenate stereochemical specificity without guessing a replacement. Regenerate only after maintained-input curation.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch032/313/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch032/313/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml:1:id: CultureMech:007551<br>./data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml:1:id: CultureMech:007551<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch032/source-preflight-bound/313/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 62 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| dependency-TOGO_M180_Desulfurococcus_Amylolyticus_Medium | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; Named stock sections only; full captured input hash, current stock fields, evidence and historical context | context_only | This is a scoped dependency, not an additional target or formulation-equivalent owner. Parent basal components, receiving doses, conditions, organisms and unrelated legacy links are excluded. |
| dependency-TOGO_M431_BN3_Medium | data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; Named stock sections only; full captured input hash, current stock fields, evidence and historical context | context_only | This is a scoped dependency, not an additional target or formulation-equivalent owner. Parent basal components, receiving doses, conditions, organisms and unrelated legacy links are excluded. |
| dependency-togo_medium_m190 | data/normalized_yaml/bacterial/togo_medium_m190.yaml; Named stock sections only; full captured input hash, current stock fields, evidence and historical context | context_only | This is a scoped dependency, not an additional target or formulation-equivalent owner. Parent basal components, receiving doses, conditions, organisms and unrelated legacy links are excluded. |
| jcm983 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983; Exact JCM 983 main table, later additions, preparation and collection default | supports | The primary distinguishes input masses, water, initial stock doses and post-autoclave additions; it does not declare measured final volume. |
| togo-main | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036; $.meta, $.components[0:2], $.comments | supports | Exact successful original API identifies M1036 and JCM983. Component values preserve g, mg, L and mL source units; the browser shell and failed alternative endpoint are not recipe evidence. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; FeCl2 solution and Trace element solution subsections only | supports | Transfer the named stock batches only, including explicit 7.7 M HCl strength. The parent basal formula and receiving preparation do not transfer. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; Selenite-tungstate solution subsection only | supports | Transfer four source rows from this stock; exclude BN3 basal medium, other trace stock, receiving doses and organisms. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins subsection only | supports | Transfer the ten vitamin masses and 1 L input water. Do not transfer the separate trace-mineral formulation or its KOH instruction. |
| togoM180original | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; Only components[1] FeCl2 solution and components[2] Trace element solution transfer; main recipe and its vitamins/other preparation excluded. | supports | Exact original provider payload corroborates only the stated transferred stock sections. Existing claim snippets and raw hashes are assessed separately. |
| togoM431original | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; Only components[3] Selenite--tungstate solution transfers; all other sections excluded. | supports | Exact original provider payload corroborates only the stated transferred stock sections. Existing claim snippets and raw hashes are assessed separately. |
| togoM190original | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; Only components[1] Trace vitamins transfers; components[0] main and components[2] Trace mineral solution excluded. | supports | Exact original provider payload corroborates only the stated transferred stock sections. Existing claim snippets and raw hashes are assessed separately. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch032/313/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi27941 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27941; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:27941 resolves to pullulan. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27941": [{"label": "Pullulan", "match_type": "preferred_term", "identifier": "CHEBI:27941", "preferred_term": "Pullulan", "ontology_id": "CHEBI:27941", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml; data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 12, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml", "events": 11, "timestamp_issues": []}] |
| scoped-existing-evidence | /private/tmp/culturemech-review-work-batch032/313/scoped-existing-evidence-audit.json; 23 exact existing stock evidence objects, current field paths, literal source checks and cited raw hashes | context_only | Twelve M180 Fe/trace objects and eleven M190 vitamin objects retain matching source hashes and snippets. One HCl primary snippet matches extracted text; the other 22 match raw responses. This does not provide attached evidence on the reviewed target or its owner, nor prove source chemical-form correctness. Fifty-two other parent objects are excluded. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS canonical term, formula and stereochemical annotation | supports | Source-specific dependency form assessment: nickel/cobalt terms omit the source hexahydrate; calcium pantothenate encodes stereochemistry not stated by the generic source. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS canonical term, formula and stereochemical annotation | supports | Source-specific dependency form assessment: nickel/cobalt terms omit the source hexahydrate; calcium pantothenate encodes stereochemistry not stated by the generic source. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS canonical term, formula and stereochemical annotation | supports | Source-specific dependency form assessment: nickel/cobalt terms omit the source hexahydrate; calcium pantothenate encodes stereochemistry not stated by the generic source. |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions were read without execution. TOGO maps g to G_PER_L and bare % to PERCENT_W_V, which does not independently prove a final-volume or percent basis. Its current solution parser separates stock references. The migration copies an existing concentration into empty composition stubs; moving topology does not curate quantities. Current exact-formulation merge retains scoped evidence only for compatible assertions. Export walks asserted stock composition and quantities and cannot repair missing source facts. Current code is not a replay of historical generation. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions were read without execution. TOGO maps g to G_PER_L and bare % to PERCENT_W_V, which does not independently prove a final-volume or percent basis. Its current solution parser separates stock references. The migration copies an existing concentration into empty composition stubs; moving topology does not curate quantities. Current exact-formulation merge retains scoped evidence only for compatible assertions. Export walks asserted stock composition and quantities and cannot repair missing source facts. Current code is not a replay of historical generation. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions were read without execution. TOGO maps g to G_PER_L and bare % to PERCENT_W_V, which does not independently prove a final-volume or percent basis. Its current solution parser separates stock references. The migration copies an existing concentration into empty composition stubs; moving topology does not curate quantities. Current exact-formulation merge retains scoped evidence only for compatible assertions. Export walks asserted stock composition and quantities and cannot repair missing source facts. Current code is not a replay of historical generation. |
| writer-3 | src/culturemech/export/kgx_export.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current functions were read without execution. TOGO maps g to G_PER_L and bare % to PERCENT_W_V, which does not independently prove a final-volume or percent basis. Its current solution parser separates stock references. The migration copies an existing concentration into empty composition stubs; moving topology does not curate quantities. Current exact-formulation merge retains scoped evidence only for compatible assertions. Export walks asserted stock composition and quantities and cannot repair missing source facts. Current code is not a replay of historical generation. |
| mediadiveJ983api-attempt | https://mediadive.dsmz.de/rest/medium/J983; Preserved exact public retrieval result | context_only | Optional alternate source attempt mediadiveJ983api did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| mediadiveJ983api_retry-attempt | https://mediadive.dsmz.de/rest/medium/J983; Preserved exact public retrieval result | context_only | Optional alternate source attempt mediadiveJ983api_retry did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| togoM1036-attempt | https://mediumapi.dbcls.jp/medium/M1036; Preserved exact public retrieval result | context_only | Optional alternate source attempt togoM1036 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| togoM1036page-attempt | https://togomedium.org/medium/M1036; Preserved exact public retrieval result | context_only | Optional alternate source attempt togoM1036page did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| togoM180-attempt | https://mediumapi.dbcls.jp/medium/M180; Preserved exact public retrieval result | context_only | Optional alternate source attempt togoM180 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| togoM431-attempt | https://mediumapi.dbcls.jp/medium/M431; Preserved exact public retrieval result | context_only | Optional alternate source attempt togoM431 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |
| togoM190-attempt | https://mediumapi.dbcls.jp/medium/M190; Preserved exact public retrieval result | context_only | Optional alternate source attempt togoM190 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Optional alternate source attempt mediadiveJ983api did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt mediadiveJ983api_retry did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM1036 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM1036page did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM180 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM431 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM190 did not supply usable formulation content; exact JCM main/stock primaries and successful original TOGO endpoints are available. The actual attempt and timestamp are preserved.
- No required source check is unavailable in this bounded review. The failed alternate/API routes do not require a partial conclusion because exact main and named-stock primary sources and the original TOGO payloads were inspected.
- Only the current target and maintained owner are record-level review targets. Parent documents were inspected for their explicitly transferred stock sections and related evidence; this review does not endorse their complete formulations, histories, growth assertions or legacy links.
- The 1054 mL arithmetic is a sum of listed liquid inputs, not a measured final volume. Source 1%, 5% and 25% labels do not establish a percentage basis. No density, gas purity, final salinity or incubation optimum was inferred.
- This scientific assessment preceded formal review validation and saving; their results are recorded separately by the root workflow.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180108Z-culturemech-007551-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: artificial_seawater_medium_with_pullulan (CultureMech:007551)'
started_at: '2026-10-21T17:54:24Z'
finished_at: '2026-10-21T18:01:08Z'
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
summary: JCM 983 and exact TOGO M1036 resolve the medium, but its water, resazurin
  and stock doses use the wrong quantity representation. Seven empty stock slots and
  absent preparation obscure the source formulation. Scoped parent evidence supports
  stock reconstruction while exposing cobalt/nickel hydrate mismatches; no final volume
  or unspecified percentage basis is inferred.
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
  - path: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
    sha256: c841731d35a0ee457bfa14bf75627a221ae6bc6e04db3a22a85cdff742d677d8
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
    sha256: e9319bfc1ddc370016c4bbcc704c60d1e211c7bfad68c2fe825a25482065411e
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
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
  selection: Task review 313; batch 032 item 3 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-one task batches
    contain 310 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 313 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007551
targets:
- target_id: CultureMech:007551
  path: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  label: artificial_seawater_medium_with_pullulan
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch032/313/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch032/313/strict.tsv"
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007551
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
  - CultureMech:007551
- check_id: mediadiveJ983api-source-access
  name: 'Exact source content access: mediadiveJ983api'
  required: false
  status: unavailable
  summary: Optional alternate source attempt mediadiveJ983api did not supply usable
    formulation content; exact JCM main/stock primaries and successful original TOGO
    endpoints are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - mediadiveJ983api-attempt
- check_id: mediadiveJ983api_retry-source-access
  name: 'Exact source content access: mediadiveJ983api_retry'
  required: false
  status: unavailable
  summary: Optional alternate source attempt mediadiveJ983api_retry did not supply
    usable formulation content; exact JCM main/stock primaries and successful original
    TOGO endpoints are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - mediadiveJ983api_retry-attempt
- check_id: togoM1036-source-access
  name: 'Exact source content access: togoM1036'
  required: false
  status: unavailable
  summary: Optional alternate source attempt togoM1036 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - togoM1036-attempt
- check_id: togoM1036page-source-access
  name: 'Exact source content access: togoM1036page'
  required: false
  status: unavailable
  summary: Optional alternate source attempt togoM1036page did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - togoM1036page-attempt
- check_id: togoM180-source-access
  name: 'Exact source content access: togoM180'
  required: false
  status: unavailable
  summary: Optional alternate source attempt togoM180 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - togoM180-attempt
- check_id: togoM431-source-access
  name: 'Exact source content access: togoM431'
  required: false
  status: unavailable
  summary: Optional alternate source attempt togoM431 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - togoM431-attempt
- check_id: togoM190-source-access
  name: 'Exact source content access: togoM190'
  required: false
  status: unavailable
  summary: Optional alternate source attempt togoM190 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - togoM190-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:02.478911Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch032/313/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:03.688384Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-032/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch032/313/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:05.292085Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T17:55:06.087376Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T18:01:07Z'
  support: supports
  summary: './data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml:1:id:
    CultureMech:007551

    ./data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml:1:id:
    CultureMech:007551

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/source-preflight-bound/313/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T18:01:07Z'
  support: supports
  summary: 62 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: b22db2880a8146719fe2b63ce9a319bdff1be681e07911a3a408558206d9abde
- evidence_id: dependency-TOGO_M180_Desulfurococcus_Amylolyticus_Medium
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: Named stock sections only; full captured input hash, current stock fields,
    evidence and historical context
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: This is a scoped dependency, not an additional target or formulation-equivalent
    owner. Parent basal components, receiving doses, conditions, organisms and unrelated
    legacy links are excluded.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dependency-TOGO_M431_BN3_Medium
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: Named stock sections only; full captured input hash, current stock fields,
    evidence and historical context
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: This is a scoped dependency, not an additional target or formulation-equivalent
    owner. Parent basal components, receiving doses, conditions, organisms and unrelated
    legacy links are excluded.
  snapshot_sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
- evidence_id: dependency-togo_medium_m190
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: Named stock sections only; full captured input hash, current stock fields,
    evidence and historical context
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: This is a scoped dependency, not an additional target or formulation-equivalent
    owner. Parent basal components, receiving doses, conditions, organisms and unrelated
    legacy links are excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: jcm983
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983
  locator: Exact JCM 983 main table, later additions, preparation and collection default
  accessed_at: '2026-10-21T17:37:00.535218Z'
  support: supports
  summary: The primary distinguishes input masses, water, initial stock doses and
    post-autoclave additions; it does not declare measured final volume.
  quote: Resazurin 0.5 mg
  snapshot_sha256: 0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9
- evidence_id: togo-main
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036
  locator: $.meta, $.components[0:2], $.comments
  accessed_at: '2026-10-21T17:38:20.800164Z'
  support: supports
  summary: Exact successful original API identifies M1036 and JCM983. Component values
    preserve g, mg, L and mL source units; the browser shell and failed alternative
    endpoint are not recipe evidence.
  snapshot_sha256: f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: FeCl2 solution and Trace element solution subsections only
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: Transfer the named stock batches only, including explicit 7.7 M HCl strength.
    The parent basal formula and receiving preparation do not transfer.
  quote: 25% HCl (7.7 M) 10.0 ml
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: Selenite-tungstate solution subsection only
  accessed_at: '2026-10-21T12:23:19.260180Z'
  support: supports
  summary: Transfer four source rows from this stock; exclude BN3 basal medium, other
    trace stock, receiving doses and organisms.
  quote: NaOH 0.4 g
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Trace vitamins subsection only
  accessed_at: '2026-10-20T06:58:05.867253Z'
  support: supports
  summary: Transfer the ten vitamin masses and 1 L input water. Do not transfer the
    separate trace-mineral formulation or its KOH instruction.
  quote: Vitamin B 1 2 0.1 mg
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: togoM180original
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  locator: Only components[1] FeCl2 solution and components[2] Trace element solution
    transfer; main recipe and its vitamins/other preparation excluded.
  accessed_at: '2026-10-21T10:35:28.558157Z'
  support: supports
  summary: Exact original provider payload corroborates only the stated transferred
    stock sections. Existing claim snippets and raw hashes are assessed separately.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: togoM431original
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  locator: Only components[3] Selenite--tungstate solution transfers; all other sections
    excluded.
  accessed_at: '2026-10-21T12:23:17.822513Z'
  support: supports
  summary: Exact original provider payload corroborates only the stated transferred
    stock sections. Existing claim snippets and raw hashes are assessed separately.
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: togoM190original
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: Only components[1] Trace vitamins transfers; components[0] main and components[2]
    Trace mineral solution excluded.
  accessed_at: '2026-10-21T09:28:25.418127Z'
  support: supports
  summary: Exact original provider payload corroborates only the stated transferred
    stock sections. Existing claim snippets and raw hashes are assessed separately.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/313/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: fdb45e26fbfbcee955ff11726bb14e0c9414718b2891882a1a829f6b253619e6
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
- evidence_id: chebi27941
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27941
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T17:36:59.759037Z'
  support: supports
  summary: CHEBI:27941 resolves to pullulan. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 281d91b75af9088d1f3fca616cc7b1c4f11f31e83c20c0cb7e68daa33e3e2d50
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
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: CHEBI:32588 resolves to potassium chloride. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T18:01:07Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27941":
    [{"label": "Pullulan", "match_type": "preferred_term", "identifier": "CHEBI:27941",
    "preferred_term": "Pullulan", "ontology_id": "CHEBI:27941", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type":
    "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id":
    "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806":
    [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806",
    "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status":
    "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml;
    data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: '[{"input": "target", "events": 12, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml",
    "events": 11, "timestamp_issues": []}]'
- evidence_id: scoped-existing-evidence
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch032/313/scoped-existing-evidence-audit.json
  locator: 23 exact existing stock evidence objects, current field paths, literal
    source checks and cited raw hashes
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Twelve M180 Fe/trace objects and eleven M190 vitamin objects retain matching
    source hashes and snippets. One HCl primary snippet matches extracted text; the
    other 22 match raw responses. This does not provide attached evidence on the reviewed
    target or its owner, nor prove source chemical-form correctness. Fifty-two other
    parent objects are excluded.
  snapshot_sha256: c87437d66e0f27c4e9c584dcbf8f9b135c8ea4d5be79eff0c2d092a9f1e3d47f
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS canonical term, formula and stereochemical annotation
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: 'Source-specific dependency form assessment: nickel/cobalt terms omit the
    source hexahydrate; calcium pantothenate encodes stereochemistry not stated by
    the generic source.'
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS canonical term, formula and stereochemical annotation
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: 'Source-specific dependency form assessment: nickel/cobalt terms omit the
    source hexahydrate; calcium pantothenate encodes stereochemistry not stated by
    the generic source.'
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS canonical term, formula and stereochemical annotation
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: 'Source-specific dependency form assessment: nickel/cobalt terms omit the
    source hexahydrate; calcium pantothenate encodes stereochemistry not stated by
    the generic source.'
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Current functions were read without execution. TOGO maps g to G_PER_L and
    bare % to PERCENT_W_V, which does not independently prove a final-volume or percent
    basis. Its current solution parser separates stock references. The migration copies
    an existing concentration into empty composition stubs; moving topology does not
    curate quantities. Current exact-formulation merge retains scoped evidence only
    for compatible assertions. Export walks asserted stock composition and quantities
    and cannot repair missing source facts. Current code is not a replay of historical
    generation.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Current functions were read without execution. TOGO maps g to G_PER_L and
    bare % to PERCENT_W_V, which does not independently prove a final-volume or percent
    basis. Its current solution parser separates stock references. The migration copies
    an existing concentration into empty composition stubs; moving topology does not
    curate quantities. Current exact-formulation merge retains scoped evidence only
    for compatible assertions. Export walks asserted stock composition and quantities
    and cannot repair missing source facts. Current code is not a replay of historical
    generation.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Current functions were read without execution. TOGO maps g to G_PER_L and
    bare % to PERCENT_W_V, which does not independently prove a final-volume or percent
    basis. Its current solution parser separates stock references. The migration copies
    an existing concentration into empty composition stubs; moving topology does not
    curate quantities. Current exact-formulation merge retains scoped evidence only
    for compatible assertions. Export walks asserted stock composition and quantities
    and cannot repair missing source facts. Current code is not a replay of historical
    generation.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T18:01:07Z'
  support: context_only
  summary: Current functions were read without execution. TOGO maps g to G_PER_L and
    bare % to PERCENT_W_V, which does not independently prove a final-volume or percent
    basis. Its current solution parser separates stock references. The migration copies
    an existing concentration into empty composition stubs; moving topology does not
    curate quantities. Current exact-formulation merge retains scoped evidence only
    for compatible assertions. Export walks asserted stock composition and quantities
    and cannot repair missing source facts. Current code is not a replay of historical
    generation.
  snapshot_sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
- evidence_id: mediadiveJ983api-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J983
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:59.178730Z'
  support: context_only
  summary: Optional alternate source attempt mediadiveJ983api did not supply usable
    formulation content; exact JCM main/stock primaries and successful original TOGO
    endpoints are available. The actual attempt and timestamp are preserved.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: mediadiveJ983api_retry-attempt
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J983
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:38:20.164046Z'
  support: context_only
  summary: Optional alternate source attempt mediadiveJ983api_retry did not supply
    usable formulation content; exact JCM main/stock primaries and successful original
    TOGO endpoints are available. The actual attempt and timestamp are preserved.
  snapshot_sha256: 7ca12d7be5347706cce83581186621c0382542be93c82f5911ae9b541150f286
- evidence_id: togoM1036-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M1036
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:59.186409Z'
  support: context_only
  summary: Optional alternate source attempt togoM1036 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
- evidence_id: togoM1036page-attempt
  kind: database
  reference: https://togomedium.org/medium/M1036
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:59.272037Z'
  support: context_only
  summary: Optional alternate source attempt togoM1036page did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: togoM180-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M180
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:59.216713Z'
  support: context_only
  summary: Optional alternate source attempt togoM180 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
- evidence_id: togoM431-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M431
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:59.245833Z'
  support: context_only
  summary: Optional alternate source attempt togoM431 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
- evidence_id: togoM190-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M190
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T17:36:59.218725Z'
  support: context_only
  summary: Optional alternate source attempt togoM190 did not supply usable formulation
    content; exact JCM main/stock primaries and successful original TOGO endpoints
    are available. The actual attempt and timestamp are preserved.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 55 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"ingredient_or_context\": \"\
    Distilled water\",\n    \"field_path\": \"ingredients[0].concentration\",\n  \
    \  \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_amount\": 1,\n    \"source_unit\": \"L\",\n    \"source_stage\"\
    : \"Initial main batch\",\n    \"primary_source_evidence_id\": \"jcm983\",\n \
    \   \"decision\": \"correct\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[0].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Source\
    \ water is 1 L of batch input, not 1 g/L or a measured final litre.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Source water is\
    \ 1 L of batch input, not 1 g/L or a measured final litre.\"\n      }\n    ],\n\
    \    \"arithmetic_and_scope\": \"Source water is 1 L of batch input, not 1 g/L\
    \ or a measured final litre.\"\n  },\n  {\n    \"quantity_id\": \"q2\",\n    \"\
    ingredient_or_context\": \"MgSO4・7H2O\",\n    \"field_path\": \"ingredients[1].concentration\"\
    ,\n    \"local\": {\n      \"value\": \"25\",\n      \"unit\": \"G_PER_L\"\n \
    \   },\n    \"source_amount\": 25,\n    \"source_unit\": \"g\",\n    \"source_stage\"\
    : \"Initial main batch\",\n    \"primary_source_evidence_id\": \"jcm983\",\n \
    \   \"decision\": \"correct\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"MgSO 4 ·7H 2 O 25.0 g\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4・7H2O\\\",\\n          \\\"volume\\\": 25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[1].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ number matches the source batch mass, but G_PER_L asserts an unestablished final-volume\
    \ denominator. Preserve the literal batch amount and source stage; do not divide\
    \ by the listed liquid-input sum as if measured final volume.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"25\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The number matches\
    \ the source batch mass, but G_PER_L asserts an unestablished final-volume denominator.\
    \ Preserve the literal batch amount and source stage; do not divide by the listed\
    \ liquid-input sum as if measured final volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The number matches the source batch mass, but G_PER_L asserts an unestablished\
    \ final-volume denominator. Preserve the literal batch amount and source stage;\
    \ do not divide by the listed liquid-input sum as if measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q3\",\n    \"ingredient_or_context\": \"NaCl\"\
    ,\n    \"field_path\": \"ingredients[2].concentration\",\n    \"local\": {\n \
    \     \"value\": \"80\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 80,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"Initial main batch\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"NaCl 80.0 g\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 80,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[2].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"80\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ number matches the source batch mass, but G_PER_L asserts an unestablished final-volume\
    \ denominator. Preserve the literal batch amount and source stage; do not divide\
    \ by the listed liquid-input sum as if measured final volume.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"80\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The number matches\
    \ the source batch mass, but G_PER_L asserts an unestablished final-volume denominator.\
    \ Preserve the literal batch amount and source stage; do not divide by the listed\
    \ liquid-input sum as if measured final volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The number matches the source batch mass, but G_PER_L asserts an unestablished\
    \ final-volume denominator. Preserve the literal batch amount and source stage;\
    \ do not divide by the listed liquid-input sum as if measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q4\",\n    \"ingredient_or_context\": \"CaCl2・2H2O\"\
    ,\n    \"field_path\": \"ingredients[3].concentration\",\n    \"local\": {\n \
    \     \"value\": \"4.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 4.5,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"Initial main batch\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"CaCl 2 ·2H 2 O 4.5 g\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 4.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[3].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ number matches the source batch mass, but G_PER_L asserts an unestablished final-volume\
    \ denominator. Preserve the literal batch amount and source stage; do not divide\
    \ by the listed liquid-input sum as if measured final volume.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"4.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The number matches\
    \ the source batch mass, but G_PER_L asserts an unestablished final-volume denominator.\
    \ Preserve the literal batch amount and source stage; do not divide by the listed\
    \ liquid-input sum as if measured final volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The number matches the source batch mass, but G_PER_L asserts an unestablished\
    \ final-volume denominator. Preserve the literal batch amount and source stage;\
    \ do not divide by the listed liquid-input sum as if measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q5\",\n    \"ingredient_or_context\": \"Resazurin\"\
    ,\n    \"field_path\": \"ingredients[4].concentration\",\n    \"local\": {\n \
    \     \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 0.5,\n    \"source_unit\": \"mg\",\n    \"source_stage\": \"Initial main batch\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Resazurin 0.5 mg\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[4].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Source\
    \ 0.5 mg equals 0.0005 g per batch. The local 0.5 G_PER_L loses the milligram\
    \ scale and assumes a final-litre basis; on the same nominal litre basis the numeric\
    \ mass is 1000-fold larger.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Source 0.5 mg equals\
    \ 0.0005 g per batch. The local 0.5 G_PER_L loses the milligram scale and assumes\
    \ a final-litre basis; on the same nominal litre basis the numeric mass is 1000-fold\
    \ larger.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"Source 0.5 mg equals\
    \ 0.0005 g per batch. The local 0.5 G_PER_L loses the milligram scale and assumes\
    \ a final-litre basis; on the same nominal litre basis the numeric mass is 1000-fold\
    \ larger.\"\n  },\n  {\n    \"quantity_id\": \"q6\",\n    \"ingredient_or_context\"\
    : \"KCl\",\n    \"field_path\": \"ingredients[5].concentration\",\n    \"local\"\
    : {\n      \"value\": \"1.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 1.5,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"Initial main batch\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"KCl 1.5 g\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 1.5,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[5].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ number matches the source batch mass, but G_PER_L asserts an unestablished final-volume\
    \ denominator. Preserve the literal batch amount and source stage; do not divide\
    \ by the listed liquid-input sum as if measured final volume.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The number matches\
    \ the source batch mass, but G_PER_L asserts an unestablished final-volume denominator.\
    \ Preserve the literal batch amount and source stage; do not divide by the listed\
    \ liquid-input sum as if measured final volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The number matches the source batch mass, but G_PER_L asserts an unestablished\
    \ final-volume denominator. Preserve the literal batch amount and source stage;\
    \ do not divide by the listed liquid-input sum as if measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q7\",\n    \"ingredient_or_context\": \"Pullulan\"\
    ,\n    \"field_path\": \"ingredients[6].concentration\",\n    \"local\": {\n \
    \     \"value\": \"0.5\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 0.5,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"Initial main batch\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Pullulan 0.5 g\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pullulan\\\",\\n          \\\"volume\\\": 0.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[6].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\
    \n        },\n        \"decision\": \"correct\",\n        \"rationale\": \"The\
    \ number matches the source batch mass, but G_PER_L asserts an unestablished final-volume\
    \ denominator. Preserve the literal batch amount and source stage; do not divide\
    \ by the listed liquid-input sum as if measured final volume.\"\n      },\n  \
    \    {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The number matches\
    \ the source batch mass, but G_PER_L asserts an unestablished final-volume denominator.\
    \ Preserve the literal batch amount and source stage; do not divide by the listed\
    \ liquid-input sum as if measured final volume.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The number matches the source batch mass, but G_PER_L asserts an unestablished\
    \ final-volume denominator. Preserve the literal batch amount and source stage;\
    \ do not divide by the listed liquid-input sum as if measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q8\",\n    \"ingredient_or_context\": \"Carbon\
    \ dioxide amount\",\n    \"field_path\": \"ingredients[7].concentration\",\n \
    \   \"local\": {\n      \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\
    \n    },\n    \"source_amount\": null,\n    \"source_unit\": \"unquantified gas\
    \ amount\",\n    \"source_stage\": \"Initial main atmosphere\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"not_quantified\",\n    \"source_snippets\"\
    : [\n      {\n        \"source_key\": \"jcm983\",\n        \"source_url\": \"\
    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\",\n        \"source_locator\"\
    : \"First preparation sentence\",\n        \"exact_source_quote\": \"N 2 -CO 2\
    \ (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[7].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\
    \n        },\n        \"decision\": \"not_quantified\",\n        \"rationale\"\
    : \"No fixed amount of this gas is supplied. VARIABLE does not encode the specified\
    \ 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent\
    \ the ratio in preparation rather than inventing dissolved concentration or flow.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    No fixed amount of this gas is supplied. VARIABLE does not encode the specified\
    \ 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent\
    \ the ratio in preparation rather than inventing dissolved concentration or flow.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"No fixed amount of this gas\
    \ is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere\
    \ ratio; preserve the unquantified dose and represent the ratio in preparation\
    \ rather than inventing dissolved concentration or flow.\"\n  },\n  {\n    \"\
    quantity_id\": \"q9\",\n    \"ingredient_or_context\": \"Nitrogen amount\",\n\
    \    \"field_path\": \"ingredients[8].concentration\",\n    \"local\": {\n   \
    \   \"value\": \"variable\",\n      \"unit\": \"VARIABLE\"\n    },\n    \"source_amount\"\
    : null,\n    \"source_unit\": \"unquantified gas amount\",\n    \"source_stage\"\
    : \"Initial main atmosphere\",\n    \"primary_source_evidence_id\": \"jcm983\"\
    ,\n    \"decision\": \"not_quantified\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"First preparation sentence\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[8].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\
    \n        },\n        \"decision\": \"not_quantified\",\n        \"rationale\"\
    : \"No fixed amount of this gas is supplied. VARIABLE does not encode the specified\
    \ 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent\
    \ the ratio in preparation rather than inventing dissolved concentration or flow.\"\
    \n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      },\n        \"decision\": \"not_quantified\",\n        \"rationale\": \"\
    No fixed amount of this gas is supplied. VARIABLE does not encode the specified\
    \ 4:1 volumetric atmosphere ratio; preserve the unquantified dose and represent\
    \ the ratio in preparation rather than inventing dissolved concentration or flow.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"No fixed amount of this gas\
    \ is supplied. VARIABLE does not encode the specified 4:1 volumetric atmosphere\
    \ ratio; preserve the unquantified dose and represent the ratio in preparation\
    \ rather than inventing dissolved concentration or flow.\"\n  },\n  {\n    \"\
    quantity_id\": \"q10\",\n    \"ingredient_or_context\": \"FeCl2 solution (see\
    \ Medium [M180])\",\n    \"field_path\": \"solutions[0].concentration\",\n   \
    \ \"local\": {\n      \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n\
    \    \"source_amount\": 1,\n    \"source_unit\": \"ml\",\n    \"source_stage\"\
    : \"Initial main addition\",\n    \"primary_source_evidence_id\": \"jcm983\",\n\
    \    \"decision\": \"correct\",\n    \"source_snippets\": [\n      {\n       \
    \ \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"FeCl 2 solution (see Medium No. 187 ) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\",\n    \
    \    \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2 solution (see Medium [M180])\\\",\\n   \
    \       \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].concentration\",\n        \"\
    stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\",\n        \"rationale\": \"The source\
    \ dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 1 mL = 0.001 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q11\"\
    ,\n    \"ingredient_or_context\": \"Trace element solution (see Medium [M180])\"\
    ,\n    \"field_path\": \"solutions[1].concentration\",\n    \"local\": {\n   \
    \   \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 1,\n    \"source_unit\": \"ml\",\n    \"source_stage\": \"Initial main addition\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Trace element solution (see Medium No. 187 ) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\",\n    \
    \    \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace element solution (see Medium [M180])\\\"\
    ,\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n   \
    \     \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].concentration\",\n        \"\
    stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\",\n        \"rationale\": \"The source\
    \ dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 1 mL = 0.001 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q12\"\
    ,\n    \"ingredient_or_context\": \"Selenite--tungstate solution (see Medium [M431])\"\
    ,\n    \"field_path\": \"solutions[2].concentration\",\n    \"local\": {\n   \
    \   \"value\": \"1\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 1,\n    \"source_unit\": \"ml\",\n    \"source_stage\": \"Initial main addition\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Selenite-tungstate solution (see Medium No. 431 ) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\",\n    \
    \    \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Selenite--tungstate solution (see Medium [M431])\\\
    \",\\n          \\\"volume\\\": 1,\\n          \\\"unit\\\": \\\"ml\\\"\",\n \
    \       \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[2].concentration\",\n        \"\
    stored\": {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\",\n        \"rationale\": \"The source\
    \ dose is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 1 mL = 0.001 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 1 mL = 0.001 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q13\"\
    ,\n    \"ingredient_or_context\": \"5% Na2CO3 solution\",\n    \"field_path\"\
    : \"solutions[3].concentration\",\n    \"local\": {\n      \"value\": \"20\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 20,\n    \"source_unit\"\
    : \"ml\",\n    \"source_stage\": \"Post-autoclave addition\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"5% Na 2 CO 3 solution 20.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2CO3 solution\\\",\\n          \\\"volume\\\
    \": 20,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 5,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 20 mL = 0.02 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 20 mL = 0.02 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 20 mL = 0.02 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q14\"\
    ,\n    \"ingredient_or_context\": \"1% NH4Cl solution\",\n    \"field_path\":\
    \ \"solutions[4].concentration\",\n    \"local\": {\n      \"value\": \"10\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 10,\n    \"source_unit\"\
    : \"ml\",\n    \"source_stage\": \"Post-autoclave addition\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"1% NH 4 Cl solution 10.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1% NH4Cl solution\\\",\\n          \\\"volume\\\
    \": 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\":\
    \ 1,\\n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\"\
    : \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\n     \
    \ }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 10 mL = 0.01 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q15\"\
    ,\n    \"ingredient_or_context\": \"1% KH2PO4 solution\",\n    \"field_path\"\
    : \"solutions[5].concentration\",\n    \"local\": {\n      \"value\": \"5\",\n\
    \      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\": 5,\n    \"source_unit\"\
    : \"ml\",\n    \"source_stage\": \"Post-autoclave addition\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"correct\",\n    \"source_snippets\": [\n  \
    \    {\n        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"1% KH 2 PO 4 solution 5.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"1% KH2PO4 solution\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 1,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[5].concentration\",\n        \"\
    stored\": {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n  \
    \      },\n        \"decision\": \"correct\",\n        \"rationale\": \"The source\
    \ dose is 5 mL = 0.005 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"5\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 5 mL = 0.005 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 5 mL = 0.005 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q16\"\
    ,\n    \"ingredient_or_context\": \"Trace vitamins (see Medium [M190])\",\n  \
    \  \"field_path\": \"solutions[6].concentration\",\n    \"local\": {\n      \"\
    value\": \"10\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\":\
    \ 10,\n    \"source_unit\": \"ml\",\n    \"source_stage\": \"Post-autoclave addition\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"Trace vitamins* (see Medium No. 197 ) 10.0 ml\",\n        \"snapshot_sha256\"\
    : \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\",\n    \
    \    \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Trace vitamins (see Medium [M190])\\\",\\n   \
    \       \\\"volume\\\": 10,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"\
    snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].concentration\",\n        \"\
    stored\": {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n \
    \       },\n        \"decision\": \"correct\",\n        \"rationale\": \"The source\
    \ dose is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"The source dose\
    \ is 10 mL = 0.01 L per receiving batch, not grams or dose per measured final\
    \ litre. Keep stock composition and receiving addition separate.\"\n      }\n\
    \    ],\n    \"arithmetic_and_scope\": \"The source dose is 10 mL = 0.01 L per\
    \ receiving batch, not grams or dose per measured final litre. Keep stock composition\
    \ and receiving addition separate.\"\n  },\n  {\n    \"quantity_id\": \"q17\"\
    ,\n    \"ingredient_or_context\": \"5% sodium sulfide nonahydrate solution dose\"\
    ,\n    \"field_path\": \"ingredients[9].concentration\",\n    \"local\": {\n \
    \     \"value\": \"6\",\n      \"unit\": \"G_PER_L\"\n    },\n    \"source_amount\"\
    : 6,\n    \"source_unit\": \"ml\",\n    \"source_stage\": \"Post-autoclave addition\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"correct\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"5% Na 2 S·9H 2 O 6.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"togoM1036original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1036\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"5% Na2S・9H2O\\\",\\n          \\\"volume\\\":\
    \ 6,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 5,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"f7bc70e941f46e1aa195c969860f576b88ba9744b79e45dc87734e5096da7030\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[9].concentration\",\n       \
    \ \"stored\": {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n\
    \        },\n        \"decision\": \"correct\",\n        \"rationale\": \"Source\
    \ 6 mL = 0.006 L is an addition of the separately prepared 5% sulfide solution.\
    \ It is not 6 g/L sulfide; the percentage basis is unspecified.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"Source 6 mL = 0.006\
    \ L is an addition of the separately prepared 5% sulfide solution. It is not 6\
    \ g/L sulfide; the percentage basis is unspecified.\"\n      }\n    ],\n    \"\
    arithmetic_and_scope\": \"Source 6 mL = 0.006 L is an addition of the separately\
    \ prepared 5% sulfide solution. It is not 6 g/L sulfide; the percentage basis\
    \ is unspecified.\"\n  },\n  {\n    \"quantity_id\": \"q18\",\n    \"ingredient_or_context\"\
    : \"FeCl2 stock: 25% HCl (7.7 M)\",\n    \"field_path\": \"solutions[0].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 10,\n    \"source_unit\": \"ml\"\
    ,\n    \"source_stage\": \"FeCl2 stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock table\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M) 10.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"25% HCl (7.7 M)\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"ml\\\",\\n          \\\"conc_value\\\": 25,\\\
    n          \\\"conc_unit\\\": \\\"%\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].solutions[0].concentration\",\n    \
    \    \"stored\": {\n          \"value\": \"0.01\",\n          \"unit\": \"L\"\n\
    \        },\n        \"decision\": \"verified\",\n        \"rationale\": \"This\
    \ exact scoped quantity is already preserved in the dependency field with matching\
    \ attached source evidence; verification does not establish chemical-form correctness\
    \ or a target receiving concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q19\",\n    \"ingredient_or_context\": \"FeCl2 stock: Distilled water\",\n\
    \    \"field_path\": \"solutions[0].composition\",\n    \"local\": [],\n    \"\
    source_amount\": 990,\n    \"source_unit\": \"ml\",\n    \"source_stage\": \"\
    FeCl2 stock\",\n    \"primary_source_evidence_id\": \"jcm187\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock table\",\n        \"exact_source_quote\"\
    : \"Distilled water 990.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 990,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[0].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"0.99\",\n          \"unit\": \"L\"\
    \n        },\n        \"decision\": \"verified\",\n        \"rationale\": \"This\
    \ exact scoped quantity is already preserved in the dependency field with matching\
    \ attached source evidence; verification does not establish chemical-form correctness\
    \ or a target receiving concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q20\",\n    \"ingredient_or_context\": \"FeCl2 stock: FeCl2・4H2O\",\n    \"\
    field_path\": \"solutions[0].composition\",\n    \"local\": [],\n    \"source_amount\"\
    : 1.5,\n    \"source_unit\": \"g\",\n    \"source_stage\": \"FeCl2 stock\",\n\
    \    \"primary_source_evidence_id\": \"jcm187\",\n    \"decision\": \"add\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock table\",\n        \"exact_source_quote\"\
    : \"FeCl 2 ·4H 2 O 1.5 g\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"FeCl2・4H2O\\\",\\n          \\\"volume\\\": 1.5,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition[1].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 1.5 g. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q21\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: Distilled water\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 1,\n    \"source_unit\": \"L\",\n\
    \    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        },\n        \"decision\": \"verified\",\n        \"rationale\": \"This\
    \ exact scoped quantity is already preserved in the dependency field with matching\
    \ attached source evidence; verification does not establish chemical-form correctness\
    \ or a target receiving concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q22\",\n    \"ingredient_or_context\": \"Trace element stock: Na2MoO4・2H2O\"\
    ,\n    \"field_path\": \"solutions[1].composition\",\n    \"local\": [],\n   \
    \ \"source_amount\": 36,\n    \"source_unit\": \"mg\",\n    \"source_stage\":\
    \ \"Trace element stock\",\n    \"primary_source_evidence_id\": \"jcm187\",\n\
    \    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"Na 2 MoO 4 ·2H 2 O 36.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2MoO4・2H2O\\\",\\n          \\\"volume\\\":\
    \ 36,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[1].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 36 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q23\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: H3BO3\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 6,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"H 3 BO 3 6.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"H3BO3\\\",\\n          \\\"volume\\\": 6,\\n \
    \         \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 6 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q24\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: MnCl2・4H2O\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 100,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"MnCl 2 ·4H 2 O 100.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnCl2・4H2O\\\",\\n          \\\"volume\\\": 100,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 100 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q25\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: CoCl2・6H2O\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 190,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"CoCl 2 ·6H 2 O 190.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CoCl2・6H2O\\\",\\n          \\\"volume\\\": 190,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 190 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q26\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: NiCl2・6H2O\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 24,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"NiCl 2 ·6H 2 O 24.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NiCl2・6H2O\\\",\\n          \\\"volume\\\": 24,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 24 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q27\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: CuCl2・2H2O\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 2,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"CuCl 2 ·2H 2 O 2.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuCl2・2H2O\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 2 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q28\",\n    \"ingredient_or_context\"\
    : \"Trace element stock: ZnCl2\",\n    \"field_path\": \"solutions[1].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 70,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace element stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm187\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element stock table\",\n        \"exact_source_quote\"\
    : \"ZnCl 2 70.0 mg\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      },\n      {\n        \"source_key\": \"togoM180original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180\"\
    ,\n        \"source_locator\": \"$.components[2].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnCl2\\\",\\n          \\\"volume\\\": 70,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].notes\",\n        \"\
    stored\": \"Role: Mineral source; Properties: Inorganic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 70 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q29\",\n    \"ingredient_or_context\"\
    : \"Selenite-tungstate stock: Distilled water\",\n    \"field_path\": \"solutions[2].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 1,\n    \"source_unit\": \"L\",\n\
    \    \"source_stage\": \"Selenite-tungstate stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm431\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table\",\n        \"\
    exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"togoM431original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"989.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  },\n        \"decision\": \"correct\",\n        \"rationale\": \"This dependency\
    \ still flattens the named stock into its main ingredients; restore the stock\
    \ stage and original unit. Its combined water value also contains other source\
    \ stages and cannot be copied.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q30\",\n    \"ingredient_or_context\": \"Selenite-tungstate stock: Na2SeO3・5H2O\"\
    ,\n    \"field_path\": \"solutions[2].composition\",\n    \"local\": [],\n   \
    \ \"source_amount\": 6,\n    \"source_unit\": \"mg\",\n    \"source_stage\": \"\
    Selenite-tungstate stock\",\n    \"primary_source_evidence_id\": \"jcm431\",\n\
    \    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table\",\n        \"\
    exact_source_quote\": \"Na 2 SeO 3 ·5H 2 O 6.0 mg\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"togoM431original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2SeO3・5H2O\\\",\\n          \\\"volume\\\":\
    \ 6,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[2].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[27].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"6\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"This dependency\
    \ still flattens the named stock into its main ingredients; restore the stock\
    \ stage and original unit. Its combined water value also contains other source\
    \ stages and cannot be copied.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q31\",\n    \"ingredient_or_context\": \"Selenite-tungstate stock: Na2WO4・2H2O\"\
    ,\n    \"field_path\": \"solutions[2].composition\",\n    \"local\": [],\n   \
    \ \"source_amount\": 8,\n    \"source_unit\": \"mg\",\n    \"source_stage\": \"\
    Selenite-tungstate stock\",\n    \"primary_source_evidence_id\": \"jcm431\",\n\
    \    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table\",\n        \"\
    exact_source_quote\": \"Na 2 WO 4 ·2H 2 O 8.0 mg\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"togoM431original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2WO4・2H2O\\\",\\n          \\\"volume\\\": 8,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[28].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"8\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"This dependency\
    \ still flattens the named stock into its main ingredients; restore the stock\
    \ stage and original unit. Its combined water value also contains other source\
    \ stages and cannot be copied.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q32\",\n    \"ingredient_or_context\": \"Selenite-tungstate stock: NaOH\"\
    ,\n    \"field_path\": \"solutions[2].composition\",\n    \"local\": [],\n   \
    \ \"source_amount\": 0.4,\n    \"source_unit\": \"g\",\n    \"source_stage\":\
    \ \"Selenite-tungstate stock\",\n    \"primary_source_evidence_id\": \"jcm431\"\
    ,\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"\
    source_key\": \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate stock table\",\n        \"\
    exact_source_quote\": \"NaOH 0.4 g\",\n        \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      },\n      {\n        \"source_key\": \"togoM431original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431\"\
    ,\n        \"source_locator\": \"$.components[3].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaOH\\\",\\n          \\\"volume\\\": 0.4,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[29].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        },\n\
    \        \"decision\": \"correct\",\n        \"rationale\": \"This dependency\
    \ still flattens the named stock into its main ingredients; restore the stock\
    \ stage and original unit. Its combined water value also contains other source\
    \ stages and cannot be copied.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q33\",\n    \"ingredient_or_context\": \"Trace-vitamin stock: Distilled water\"\
    ,\n    \"field_path\": \"solutions[6].composition\",\n    \"local\": [],\n   \
    \ \"source_amount\": 1,\n    \"source_unit\": \"L\",\n    \"source_stage\": \"\
    Trace-vitamin stock\",\n    \"primary_source_evidence_id\": \"jcm197\",\n    \"\
    decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[0].concentration\",\n  \
    \      \"stored\": {\n          \"value\": \"1\",\n          \"unit\": \"L\"\n\
    \        },\n        \"decision\": \"verified\",\n        \"rationale\": \"This\
    \ exact scoped quantity is already preserved in the dependency field with matching\
    \ attached source evidence; verification does not establish chemical-form correctness\
    \ or a target receiving concentration.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this literal stock-batch input and supplied form separately from its\
    \ receiving dose. Input water is not an independently measured final stock volume;\
    \ no final-medium concentration is calculated.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q34\",\n    \"ingredient_or_context\": \"Trace-vitamin stock: Biotin\",\n\
    \    \"field_path\": \"solutions[6].composition\",\n    \"local\": [],\n    \"\
    source_amount\": 2,\n    \"source_unit\": \"mg\",\n    \"source_stage\": \"Trace-vitamin\
    \ stock\",\n    \"primary_source_evidence_id\": \"jcm197\",\n    \"decision\"\
    : \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm197\"\
    ,\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Biotin 2.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Biotin\\\",\\n          \\\"volume\\\": 2,\\n\
    \          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[1].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 2 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q35\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: p--Aminobenzoic acid\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 5,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"p -Aminobenzoic acid 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"p--Aminobenzoic acid\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[6].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[2].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q36\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Thiamine・HCl\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 5,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Thiamine·HCl 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Thiamine・HCl\\\",\\n          \\\"volume\\\":\
    \ 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[6].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[3].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q37\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Calcium pantothenate\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 5,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Calcium pantothenate 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Calcium pantothenate\\\",\\n          \\\"volume\\\
    \": 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[6].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[4].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q38\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Pyridoxine・HCl\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 10,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Pyridoxine·HCl 10.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Pyridoxine・HCl\\\",\\n          \\\"volume\\\"\
    : 10,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[6].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[5].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 10 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q39\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Folic acid\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 2,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Folic acid 2.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Folic acid\\\",\\n          \\\"volume\\\": 2,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[6].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 2 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q40\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Vitamin B12\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 0.1,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Vitamin B 1 2 0.1 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Vitamin B12\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[7].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 0.1 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q41\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Riboflavin\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 5,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Riboflavin 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Riboflavin\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[8].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q42\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Nicotinic acid\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 5,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Nicotinic acid 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Nicotinic acid\\\",\\n          \\\"volume\\\"\
    : 5,\\n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"\
    61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\n      }\n\
    \    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"target\",\n\
    \        \"field_path\": \"solutions[6].composition\",\n        \"stored\": [],\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[9].notes\",\n        \"\
    stored\": \"Role: Vitamin; Properties: Organic compound, Defined component, Simple\
    \ component\\n\\nSource batch input: 5 mg. Final preparation volume is not independently\
    \ established; the unsupported g/L assertion is withdrawn, not replaced by an\
    \ assumed one-liter concentration.\",\n        \"decision\": \"verified\",\n \
    \       \"rationale\": \"This exact scoped quantity is already preserved in the\
    \ dependency field with matching attached source evidence; verification does not\
    \ establish chemical-form correctness or a target receiving concentration.\"\n\
    \      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q43\",\n    \"ingredient_or_context\"\
    : \"Trace-vitamin stock: Lipoic acid\",\n    \"field_path\": \"solutions[6].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 5,\n    \"source_unit\": \"mg\"\
    ,\n    \"source_stage\": \"Trace-vitamin stock\",\n    \"primary_source_evidence_id\"\
    : \"jcm197\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm197\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197\"\
    ,\n        \"source_locator\": \"Trace-vitamin stock table\",\n        \"exact_source_quote\"\
    : \"Lipoic acid 5.0 mg\",\n        \"snapshot_sha256\": \"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532\"\
    ,\n        \"parsed_text_sha256\": \"818dbda42619dd184a66e2ca66e5772f7db327384df79441e793f75c32ed531f\"\
    \n      },\n      {\n        \"source_key\": \"togoM190original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190\"\
    ,\n        \"source_locator\": \"$.components[1].items[10]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Lipoic acid\\\",\\n          \\\"volume\\\": 5,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[6].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"The stock composition\
    \ is empty here; add only this named source-stock ingredient with its stage and\
    \ evidence.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/togo_medium_m190.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition[10].notes\",\n        \"\
    stored\": \"Role: Growth factor; Properties: Organic compound, Defined component,\
    \ Simple component\\n\\nSource batch input: 5 mg. Final preparation volume is\
    \ not independently established; the unsupported g/L assertion is withdrawn, not\
    \ replaced by an assumed one-liter concentration.\",\n        \"decision\": \"\
    verified\",\n        \"rationale\": \"This exact scoped quantity is already preserved\
    \ in the dependency field with matching attached source evidence; verification\
    \ does not establish chemical-form correctness or a target receiving concentration.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Retain this literal stock-batch\
    \ input and supplied form separately from its receiving dose. Input water is not\
    \ an independently measured final stock volume; no final-medium concentration\
    \ is calculated.\"\n  },\n  {\n    \"quantity_id\": \"q44\",\n    \"ingredient_or_context\"\
    : \"Fe-stock HCl reagent molarity\",\n    \"field_path\": \"solutions[0].composition\"\
    ,\n    \"local\": [],\n    \"source_amount\": 7.7,\n    \"source_unit\": \"M\"\
    ,\n    \"source_stage\": \"HCl reagent before its 10 mL stock addition\",\n  \
    \  \"primary_source_evidence_id\": \"jcm187\",\n    \"decision\": \"add\",\n \
    \   \"source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n   \
    \     \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock table\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M) 10.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"Retain explicit\
    \ reagent strength inside the Fe stock, not as a main-medium concentration.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"Retain explicit\
    \ reagent strength inside the Fe stock, not as a main-medium concentration.\"\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].solutions[0].composition[0].concentration\"\
    ,\n        \"stored\": {\n          \"value\": \"7.7\",\n          \"unit\": \"\
    MOLAR\"\n        },\n        \"decision\": \"verified\",\n        \"rationale\"\
    : \"Existing 7.7 MOLAR reagent field has both exact provider and primary attached\
    \ support.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"7.7 M is stated\
    \ directly. It is not inferred by converting the unqualified 25% label; no acid\
    \ density is assumed.\"\n  },\n  {\n    \"quantity_id\": \"q45\",\n    \"ingredient_or_context\"\
    : \"Carbonate nominal stock-strength label\",\n    \"field_path\": \"solutions[3].preferred_term\"\
    ,\n    \"local\": \"5% Na2CO3 solution\",\n    \"source_amount\": 5,\n    \"source_unit\"\
    : \"% (basis unspecified)\",\n    \"source_stage\": \"Separate reagent stock\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"5% Na 2 CO 3 solution 20.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[3].preferred_term\",\n        \"\
    stored\": \"5% Na2CO3 solution\",\n        \"decision\": \"evidence_only\",\n\
    \        \"rationale\": \"The percentage label is literal, but its w/v, w/w or\
    \ v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do\
    \ not convert to grams or molarity.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preferred_term\",\n        \"stored\"\
    : \"5% Na2CO3 solution\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The percentage label is literal, but its w/v, w/w or v/v basis\
    \ is unstated. Add scoped evidence and preserve that uncertainty; do not convert\
    \ to grams or molarity.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The\
    \ percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add\
    \ scoped evidence and preserve that uncertainty; do not convert to grams or molarity.\"\
    \n  },\n  {\n    \"quantity_id\": \"q46\",\n    \"ingredient_or_context\": \"\
    Ammonium chloride nominal stock-strength label\",\n    \"field_path\": \"solutions[4].preferred_term\"\
    ,\n    \"local\": \"1% NH4Cl solution\",\n    \"source_amount\": 1,\n    \"source_unit\"\
    : \"% (basis unspecified)\",\n    \"source_stage\": \"Separate reagent stock\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"1% NH 4 Cl solution 10.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[4].preferred_term\",\n        \"\
    stored\": \"1% NH4Cl solution\",\n        \"decision\": \"evidence_only\",\n \
    \       \"rationale\": \"The percentage label is literal, but its w/v, w/w or\
    \ v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do\
    \ not convert to grams or molarity.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[4].preferred_term\",\n        \"stored\"\
    : \"1% NH4Cl solution\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The percentage label is literal, but its w/v, w/w or v/v basis\
    \ is unstated. Add scoped evidence and preserve that uncertainty; do not convert\
    \ to grams or molarity.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The\
    \ percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add\
    \ scoped evidence and preserve that uncertainty; do not convert to grams or molarity.\"\
    \n  },\n  {\n    \"quantity_id\": \"q47\",\n    \"ingredient_or_context\": \"\
    Potassium phosphate nominal stock-strength label\",\n    \"field_path\": \"solutions[5].preferred_term\"\
    ,\n    \"local\": \"1% KH2PO4 solution\",\n    \"source_amount\": 1,\n    \"source_unit\"\
    : \"% (basis unspecified)\",\n    \"source_stage\": \"Separate reagent stock\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"1% KH 2 PO 4 solution 5.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[5].preferred_term\",\n        \"\
    stored\": \"1% KH2PO4 solution\",\n        \"decision\": \"evidence_only\",\n\
    \        \"rationale\": \"The percentage label is literal, but its w/v, w/w or\
    \ v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do\
    \ not convert to grams or molarity.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[5].preferred_term\",\n        \"stored\"\
    : \"1% KH2PO4 solution\",\n        \"decision\": \"evidence_only\",\n        \"\
    rationale\": \"The percentage label is literal, but its w/v, w/w or v/v basis\
    \ is unstated. Add scoped evidence and preserve that uncertainty; do not convert\
    \ to grams or molarity.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The\
    \ percentage label is literal, but its w/v, w/w or v/v basis is unstated. Add\
    \ scoped evidence and preserve that uncertainty; do not convert to grams or molarity.\"\
    \n  },\n  {\n    \"quantity_id\": \"q48\",\n    \"ingredient_or_context\": \"\
    Sulfide nominal stock-strength label\",\n    \"field_path\": \"ingredients[9].preferred_term\"\
    ,\n    \"local\": \"5% Na2S・9H2O\",\n    \"source_amount\": 5,\n    \"source_unit\"\
    : \"% (basis unspecified)\",\n    \"source_stage\": \"Separate reagent stock\"\
    ,\n    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n\
    \        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Later-addition table\",\n        \"exact_source_quote\"\
    : \"5% Na 2 S·9H 2 O 6.0 ml\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ingredients[9].preferred_term\",\n      \
    \  \"stored\": \"5% Na2S・9H2O\",\n        \"decision\": \"evidence_only\",\n \
    \       \"rationale\": \"The percentage label is literal, but its w/v, w/w or\
    \ v/v basis is unstated. Add scoped evidence and preserve that uncertainty; do\
    \ not convert to grams or molarity.\"\n      },\n      {\n        \"input\": \"\
    data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].preferred_term\",\n        \"stored\"\
    : \"5% Na2S・9H2O\",\n        \"decision\": \"evidence_only\",\n        \"rationale\"\
    : \"The percentage label is literal, but its w/v, w/w or v/v basis is unstated.\
    \ Add scoped evidence and preserve that uncertainty; do not convert to grams or\
    \ molarity.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"The percentage\
    \ label is literal, but its w/v, w/w or v/v basis is unstated. Add scoped evidence\
    \ and preserve that uncertainty; do not convert to grams or molarity.\"\n  },\n\
    \  {\n    \"quantity_id\": \"q49\",\n    \"ingredient_or_context\": \"HCl nominal\
    \ percentage label\",\n    \"field_path\": \"solutions[0].composition\",\n   \
    \ \"local\": [],\n    \"source_amount\": 25,\n    \"source_unit\": \"% (basis\
    \ unspecified)\",\n    \"source_stage\": \"HCl reagent for Fe stock\",\n    \"\
    primary_source_evidence_id\": \"jcm187\",\n    \"decision\": \"add\",\n    \"\
    source_snippets\": [\n      {\n        \"source_key\": \"jcm187\",\n        \"\
    source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\",\n  \
    \      \"source_locator\": \"FeCl2 stock table\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M) 10.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\"\
    : [],\n        \"decision\": \"add\",\n        \"rationale\": \"Retain the source\
    \ label without converting an unknown percent basis.\"\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ [],\n        \"decision\": \"add\",\n        \"rationale\": \"Retain the source\
    \ label without converting an unknown percent basis.\"\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].solutions[0].composition[0].preferred_term\"\
    ,\n        \"stored\": \"25% HCl (7.7 M)\",\n        \"decision\": \"verified\"\
    ,\n        \"rationale\": \"The literal label is retained with attached exact\
    \ support; the explicit molarity is separate.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The fixed 10 mL dose and independently explicit 7.7 M strength do not resolve\
    \ the source percent basis.\"\n  },\n  {\n    \"quantity_id\": \"q50\",\n    \"\
    ingredient_or_context\": \"Basal gas ratio\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"local\": null,\n    \"source_amount\": \"4:1\",\n    \"source_unit\"\
    : \"v/v N2:CO2\",\n    \"source_stage\": \"Main preparation\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Preparation/default text\",\n        \"exact_source_quote\"\
    : \"N 2 -CO 2 (4:1, v/v) gas mixture\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Main mixture\
    \ autoclaved under the stated volumetric ratio; 80:20 is equivalent arithmetic,\
    \ not a measured gas dose.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Main mixture autoclaved\
    \ under the stated volumetric ratio; 80:20 is equivalent arithmetic, not a measured\
    \ gas dose.\"\n      }\n    ],\n    \"arithmetic_and_scope\": \"Main mixture autoclaved\
    \ under the stated volumetric ratio; 80:20 is equivalent arithmetic, not a measured\
    \ gas dose.\"\n  },\n  {\n    \"quantity_id\": \"q51\",\n    \"ingredient_or_context\"\
    : \"Collection default autoclave temperature\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"local\": null,\n    \"source_amount\": 121,\n    \"source_unit\": \"\
    °C\",\n    \"source_stage\": \"Main preparation\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Preparation/default text\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Collection default\
    \ applies to specified autoclaving; it does not replace the vitamin filtration\
    \ exception.\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Collection default applies\
    \ to specified autoclaving; it does not replace the vitamin filtration exception.\"\
    \n      }\n    ],\n    \"arithmetic_and_scope\": \"Collection default applies\
    \ to specified autoclaving; it does not replace the vitamin filtration exception.\"\
    \n  },\n  {\n    \"quantity_id\": \"q52\",\n    \"ingredient_or_context\": \"\
    Collection default autoclave duration\",\n    \"field_path\": \"preparation_steps\"\
    ,\n    \"local\": null,\n    \"source_amount\": 15,\n    \"source_unit\": \"min\"\
    ,\n    \"source_stage\": \"Main preparation\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Preparation/default text\",\n        \"exact_source_quote\"\
    : \"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.\"\
    ,\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Retain this\
    \ source-specific default with the appropriate autoclave stage.\"\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Retain this source-specific\
    \ default with the appropriate autoclave stage.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Retain this source-specific default with the appropriate autoclave stage.\"\
    \n  },\n  {\n    \"quantity_id\": \"q53\",\n    \"ingredient_or_context\": \"\
    Main pH range\",\n    \"field_path\": \"ph_range\",\n    \"local\": null,\n  \
    \  \"source_amount\": \"7.2–7.5\",\n    \"source_unit\": \"pH\",\n    \"source_stage\"\
    : \"Main preparation\",\n    \"primary_source_evidence_id\": \"jcm983\",\n   \
    \ \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Preparation/default text\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.2 - 7.5 with a 5% Na 2 CO 3 solution, if necessary.\",\n  \
    \      \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Preserve the range,\
    \ without a midpoint or an invented incubation optimum.\"\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"ph_range\",\n        \"stored\": null,\n        \"\
    decision\": \"add\",\n        \"rationale\": \"Preserve the range, without a midpoint\
    \ or an invented incubation optimum.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"Preserve the range, without a midpoint or an invented incubation optimum.\"\
    \n  },\n  {\n    \"quantity_id\": \"q54\",\n    \"ingredient_or_context\": \"\
    Optional carbonate adjustment\",\n    \"field_path\": \"preparation_steps\",\n\
    \    \"local\": null,\n    \"source_amount\": null,\n    \"source_unit\": \"unquantified\
    \ additional dose\",\n    \"source_stage\": \"Main preparation\",\n    \"primary_source_evidence_id\"\
    : \"jcm983\",\n    \"decision\": \"add\",\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm983\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Preparation/default text\",\n        \"exact_source_quote\"\
    : \"Adjust pH to 7.2 - 7.5 with a 5% Na 2 CO 3 solution, if necessary.\",\n  \
    \      \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"The initial\
    \ 20 mL carbonate addition is separate from any additional adjustment. No fixed\
    \ adjustment dose or percent basis is supplied.\"\n      },\n      {\n       \
    \ \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"The initial 20 mL carbonate\
    \ addition is separate from any additional adjustment. No fixed adjustment dose\
    \ or percent basis is supplied.\"\n      }\n    ],\n    \"arithmetic_and_scope\"\
    : \"The initial 20 mL carbonate addition is separate from any additional adjustment.\
    \ No fixed adjustment dose or percent basis is supplied.\"\n  },\n  {\n    \"\
    quantity_id\": \"q55\",\n    \"ingredient_or_context\": \"Listed liquid inputs;\
    \ unresolved final volume\",\n    \"field_path\": \"preparation_steps\",\n   \
    \ \"local\": null,\n    \"source_amount\": 1054,\n    \"source_unit\": \"mL listed\
    \ input sum\",\n    \"source_stage\": \"Across initial and later additions\",\n\
    \    \"primary_source_evidence_id\": \"jcm983\",\n    \"decision\": \"add\",\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"jcm983\",\n  \
    \      \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\"\
    ,\n        \"source_locator\": \"Main table\",\n        \"exact_source_quote\"\
    : \"Distilled water 1.0 L\",\n        \"snapshot_sha256\": \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\"\
    ,\n        \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"jcm983\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\",\n        \"source_locator\"\
    : \"Later-addition table\",\n        \"exact_source_quote\": \"1% NH 4 Cl solution\
    \ 10.0 ml 1% KH 2 PO 4 solution 5.0 ml Trace vitamins* (see Medium No. 197 ) 10.0\
    \ ml 5% Na 2 CO 3 solution 20.0 ml 5% Na 2 S·9H 2 O 6.0 ml\",\n        \"snapshot_sha256\"\
    : \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\",\n    \
    \    \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      },\n      {\n        \"source_key\": \"jcm983\",\n        \"source_url\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=983\",\n        \"source_locator\"\
    : \"Initial stock rows; all three are 1 mL\",\n        \"exact_source_quote\"\
    : \"Selenite-tungstate solution (see Medium No. 431 ) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"0b8579ac84649c06912fc80920c20540da55edd3de19e4016cc0b26fa04b7ab9\",\n    \
    \    \"parsed_text_sha256\": \"f9e951334da82467ffea8467431675a096d2dd48f7084cdc832d200447f3762c\"\
    \n      }\n    ],\n    \"layer_decisions\": [\n      {\n        \"input\": \"\
    target\",\n        \"field_path\": \"preparation_steps\",\n        \"stored\"\
    : null,\n        \"decision\": \"add\",\n        \"rationale\": \"Preserve the\
    \ ordered additions without asserting a final denominator.\"\n      },\n     \
    \ {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null,\n\
    \        \"decision\": \"add\",\n        \"rationale\": \"Preserve the ordered\
    \ additions without asserting a final denominator.\"\n      }\n    ],\n    \"\
    arithmetic_and_scope\": \"1000 + 1 + 1 + 1 + 10 + 5 + 10 + 20 + 6 = 1054 mL of\
    \ listed liquid inputs, before optional carbonate adjustment. This sum is not\
    \ a measured final volume and cannot justify g/L normalization.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '9 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 9/10 primary
    and 5/10 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi16526
  - chebi17997
  - chebi26710
  - chebi27941
  - chebi31795
  - chebi32588
  - chebi86158
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 10: primary 90.00%;
    secondary 50.00%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 23 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact main accession and maintained owner
  outcome: supported
  summary: CultureMech:007551 resolves to TOGO M1036 and JCM983. The sole maintained
    contributor shares its stable ID, name and retained import event; the generated
    record adds merge metadata. Parent M180/M431/M190 records are stock dependencies,
    not interchangeable media or additional owners.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - owner-0
  - id-search
  - jcm983
  - togo-main
- assessment_id: formulation
  area: consistency
  topic: All amounts and source stages
  outcome: concern
  summary: Every target and owner concentration is covered by the quantity inventory.
    The five unchanged numeric gram amounts retain unsupported final-litre denominators;
    water, resazurin and eight liquid additions also lose their original units. No
    amount is declared verified on the target or owner because neither attaches supporting
    formulation evidence. The source liquid-input sum is not a final-volume measurement.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - owner-0
  - jcm983
  - quantity-inventory
- assessment_id: stocks
  area: completeness
  topic: Seven empty stock slots and four bounded parent formulations
  outcome: concern
  summary: Four referenced stock batches can be recovered from exact J187/J431/J197
    sections; three percentage-labelled main stock slots and the separate sulfide
    reagent retain uncertain percent bases. M180 and M190 have corrected stock quantities
    and attached evidence in scope, whereas M431 still flattens the selenite-tungstate
    ingredients. Transfer only these named sections, preserving their own doses and
    stages.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - jcm187
  - jcm431
  - jcm197
  - scoped-existing-evidence
  - quantity-inventory
- assessment_id: preparation
  area: completeness
  topic: Sterilization, anaerobic addition order and pH
  outcome: concern
  summary: Neither local layer contains preparation_steps or ph_range. J983 explicitly
    autoclaves the initial mixture under N2:CO2 4:1 v/v, then adds separately autoclaved
    or marked filter-sterilized solutions anaerobically after N2 storage. Vitamins
    carry the filtration marker. The collection default is 121°C for 15 min where
    autoclaving applies; gas purity, pressure, filtration pore size, incubation temperature
    and duration are not supplied.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - jcm983
  - record
  - owner-0
  - quantity-inventory
- assessment_id: dependent-forms
  area: grounding
  topic: Chemical forms on transferred stock dependencies
  outcome: concern
  summary: The target empty stocks do not assert these dependent term IDs. Before
    populating them, resolve M180 source CoCl2·6H2O and NiCl2·6H2O being assigned
    to the anhydrous terms CHEBI:35696 and CHEBI:34887. M190 calcium pantothenate
    at 5 mg has a stereospecific D structural term CHEBI:31345 while the source names
    no isomer; this is unresolved specificity, not proof that D is wrong. Other target
    hydrated salts match their source forms; no new IDs are proposed.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - jcm187
  - jcm197
  - chebi34887
  - chebi35696
  - chebi31345
  - scoped-existing-evidence
- assessment_id: evidence-placement
  area: evidence
  topic: Existing evidence and precise transfer limits
  outcome: concern
  summary: The target and owner retain source URLs in notes but no ingredient or stock-dose
    evidence. Twenty-three existing parent-stock evidence objects are authenticated
    only in their original scopes. Root references and exact narrow evidence should
    accompany later authorized repairs; one parent source citation cannot support
    its whole medium or a different stock. Current access failures are retained separately
    from successful exact primaries and original TOGO responses.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - owner-0
  - scoped-existing-evidence
  - bound-source-integrity
- assessment_id: classification
  area: scope
  topic: Record category, composition and growth boundaries
  outcome: concern
  summary: LIQUID is compatible with the source formulation. The current TOGO category
    inference defaults to bacterial; this is filing metadata, not a demonstrated organism
    range. COMPLEX/UNDEFINED lacks an explicit source classification rationale; pullulan
    is a polymer, so a defined/complex replacement is not prescribed without a documented
    local definition and product context. No target organism, strain, DOI/PMID, growth
    result, variant, high_metal or kg_microbe_match is asserted by this target. Parent
    growth conditions and legacy sulfur links do not transfer.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - owner-0
  - jcm983
  - writer-0
- assessment_id: writer-scope
  area: provenance
  topic: Current import, migration, merge and export responsibilities
  outcome: supported
  summary: Repair the maintained M1036 owner and only the identified dependency assertions
    before authorized regeneration. The existing migration event and current copy
    logic explain why empty topology alone is insufficient; current importer code
    and evidence-aware merge behavior do not authenticate an unknown old response.
    Numeric/string field preservation by an exporter is not scientific validation.
  target_ids:
  - CultureMech:007551
  evidence_ids:
  - record
  - owner-0
  - writer-0
  - writer-1
  - writer-2
  - writer-3
findings:
- finding_id: f1
  issue_key: cm007551-main-units-and-basis
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Wrong units and stock doses make the stored formulation unusable
  description: Both local layers encode 1 L water as 1 G_PER_L, 0.5 mg resazurin as
    0.5 G_PER_L, and all eight receiving liquid additions as G_PER_L. The five correctly
    transcribed numeric gram amounts also lack an established final-litre denominator.
    These are dimensional and preparation-scale changes, not a harmless naming issue;
    a faithful source recipe cannot be reconstructed by reading these quantities literally.
  target_ids:
  - CultureMech:007551
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[9].concentration
  - solutions
  evidence_ids:
  - record
  - owner-0
  - jcm983
  - togo-main
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
  issue_key: cm007551-stock-completeness
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Named source stocks remain empty and cannot inherit unrelated parent recipes
  description: Seven Unknown solution slots have empty compositions despite four explicitly
    recoverable stock formulations. The M431 dependency still carries selenite-tungstate
    solutes in its flattened main ingredient list, including mg-to-G_PER_L and combined-water
    artifacts. M180 and M190 provide useful scoped existing evidence, but their parent
    main recipes, receiving doses, sulfur links and unrelated minerals are not this
    medium.
  target_ids:
  - CultureMech:007551
  field_paths:
  - solutions[0].composition
  - solutions[1].composition
  - solutions[2].composition
  - solutions[3].composition
  - solutions[4].composition
  - solutions[5].composition
  - solutions[6].composition
  - ingredients[9]
  evidence_ids:
  - jcm983
  - jcm187
  - jcm431
  - jcm197
  - scoped-existing-evidence
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
  issue_key: cm007551-source-preparation-omission
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing preparation loses sterilization exceptions, gas ratio and pH
  description: 'Both layers omit the entire source preparation: initial autoclaving
    under N2:CO2 4:1 v/v, source default 121°C/15 min, later anaerobic additions and
    N2 storage, specifically filtered vitamins, and pH 7.2–7.5 with optional further
    5% carbonate. Omission materially changes how the recipe would be prepared; no
    generic stock or parent cycle can safely substitute.'
  target_ids:
  - CultureMech:007551
  field_paths:
  - preparation_steps
  - ph_range
  - ingredients[7]
  - ingredients[8]
  evidence_ids:
  - record
  - owner-0
  - jcm983
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3.5
  native_severity: P3.5
  normalization_reason: Native P3.5 is raised to major because omission of the source-specific
    main sterilization and vitamin filtration exception changes reproducibility; P3.4
    preparation absence is a secondary aspect of the same finding.
- finding_id: f4
  issue_key: cm007551-dependent-hydrate-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Referenced trace-stock hydrate identities conflict with captured ontology
    structures
  description: M180 solutions[1].composition[4] and [5] name cobalt chloride hexahydrate
    and nickel chloride hexahydrate, corroborated by J187 and the exact provider.
    Their CHEBI:35696 and CHEBI:34887 terms instead encode anhydrous chlorides. These
    are dependency assertions that must not be copied into the currently empty target
    stock. Separately, generic source calcium pantothenate does not establish the
    D stereochemistry encoded by M190 CHEBI:31345; that narrower point remains an
    unresolved support limit.
  target_ids:
  - CultureMech:007551
  field_paths:
  - solutions[1].composition
  - solutions[6].composition
  evidence_ids:
  - jcm187
  - jcm197
  - chebi35696
  - chebi34887
  - chebi31345
  - scoped-existing-evidence
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
  description: Restore literal batch quantities and receiving stock volumes in the
    maintained owner with claim-level evidence. Preserve mg versus g, batch input
    versus concentration and the unknown final volume. Reconcile the owner before
    regenerating the merged record.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007551
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
  description: Populate or reference only the named Fe, trace-element, selenite-tungstate
    and trace-vitamin stock sections; preserve the separate percentage-labelled reagents
    without an invented basis. Reconcile the scoped M431 stock representation and
    recheck dependency terms before reuse.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007551
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
  description: Restore the exact source sequence, main pH range and stock-specific
    sterilization/storage qualifiers. Keep the unspecified additional carbonate dose,
    unqualified percent bases and unknown gas amount explicit.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007551
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
  description: Check and correct the two exact M180 hydrate term assignments using
    source-specific ontology evidence before stock reuse; preserve masses. Resolve
    the calcium-pantothenate stereochemical specificity without guessing a replacement.
    Regenerate only after maintained-input curation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007551
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml
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
- Optional alternate source attempt mediadiveJ983api did not supply usable formulation
  content; exact JCM main/stock primaries and successful original TOGO endpoints are
  available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt mediadiveJ983api_retry did not supply usable formulation
  content; exact JCM main/stock primaries and successful original TOGO endpoints are
  available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM1036 did not supply usable formulation content;
  exact JCM main/stock primaries and successful original TOGO endpoints are available.
  The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM1036page did not supply usable formulation
  content; exact JCM main/stock primaries and successful original TOGO endpoints are
  available. The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM180 did not supply usable formulation content;
  exact JCM main/stock primaries and successful original TOGO endpoints are available.
  The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM431 did not supply usable formulation content;
  exact JCM main/stock primaries and successful original TOGO endpoints are available.
  The actual attempt and timestamp are preserved.
- Optional alternate source attempt togoM190 did not supply usable formulation content;
  exact JCM main/stock primaries and successful original TOGO endpoints are available.
  The actual attempt and timestamp are preserved.
- No required source check is unavailable in this bounded review. The failed alternate/API
  routes do not require a partial conclusion because exact main and named-stock primary
  sources and the original TOGO payloads were inspected.
- Only the current target and maintained owner are record-level review targets. Parent
  documents were inspected for their explicitly transferred stock sections and related
  evidence; this review does not endorse their complete formulations, histories, growth
  assertions or legacy links.
- The 1054 mL arithmetic is a sum of listed liquid inputs, not a measured final volume.
  Source 1%, 5% and 25% labels do not establish a percentage basis. No density, gas
  purity, final salinity or incubation optimum was inferred.
- This scientific assessment preceded formal review validation and saving; their results
  are recorded separately by the root workflow.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-032
- generated-medium
```
