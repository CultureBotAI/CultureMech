# Source and formulation review: alkali_b_medium (CultureMech:008367)

- Review: 20261021T191750Z-culturemech-008367-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T19:13:56Z
- Finished UTC: 2026-10-21T19:17:50Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact NBRC recipe resolves, but both layers flatten separately prepared A/B solutions, misstate liquid units and point to unrelated MediaDive stocks. The later water-collapse repair does not restore the two source stages.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 348; batch 035 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding thirty-four task batches contain 340 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 343 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008367 | data/merge_yaml/merged/Alkali_B_medium.yaml | generated | alkali_b_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008367 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008367 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/348/strict.tsv |
| validate-terms | passed | True | CultureMech:008367 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008367 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008367 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact source content access: togoM1799 | unavailable | False | CultureMech:008367 | The optional alternate mediumapi request failed DNS. Exact original TOGO and NBRC primary content are available, so this failure does not prevent assessment of the current recipe. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008367.

The four documented recipes completed; interpret the scope of each separately.

### Exact medium and maintained owner

identity: supported. Targets: CultureMech:008367.

The exact NBRC accession and TOGO identifier agree. One maintained bacterial owner resolves by stable ID and complete merge provenance; no strain-specific growth, supplier identity or citation is invented.

### Generated versus maintained water history

ownership: concern. Targets: CultureMech:008367.

The target retains 1000 G_PER_L water from summing two 500 entries; the owner later collapses them to 500 G_PER_L. The source has one 500 ml water entry in each distinct solution. Neither numerical operation establishes correct scientific stage or units. Other source amounts and the two wrong stock links remain in both layers.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:008367.

20 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "decision_id": "q1",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "500.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; Distilled water",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 500,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "This is a separate 500 ml water input in the named solution. The target 1000 G_PER_L and owner 500 G_PER_L are both wrong representations: restore both stage-specific liquid quantities rather than treating equal numbers as duplicate claims."
  },
  {
    "decision_id": "q2",
    "ingredient": "MgSO4·7H2O",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; MgSO4·7H2O",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[1]",
        "exact_source_quote": "\"component_name\": \"MgSO4·7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q3",
    "ingredient": "Yeast extract",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "0.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; Yeast extract",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[2]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 0.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q4",
    "ingredient": "K2HPO4",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; K2HPO4",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[3]",
        "exact_source_quote": "\"component_name\": \"K2HPO4\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q5",
    "ingredient": "CuSO4·5H2O",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; CuSO4·5H2O",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[4]",
        "exact_source_quote": "\"component_name\": \"CuSO4·5H2O\",\n          \"volume\": 0.001,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q6",
    "ingredient": "Glucose",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; Glucose",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[5]",
        "exact_source_quote": "\"component_name\": \"Glucose\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q7",
    "ingredient": "L-Asparagine",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.3",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; L-Asparagine",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[6]",
        "exact_source_quote": "\"component_name\": \"L-Asparagine\",\n          \"volume\": 0.3,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q8",
    "ingredient": "Agar",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; Agar",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[7]",
        "exact_source_quote": "\"component_name\": \"Agar\",\n          \"volume\": 15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q9",
    "ingredient": "Fe2(SO4)3·6H2O",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.01",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; Fe2(SO4)3·6H2O",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[8]",
        "exact_source_quote": "\"component_name\": \"Fe2(SO4)3·6H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q10",
    "ingredient": "Peptone",
    "decision": "correct",
    "stage": "Solution A preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution A preparation; Peptone",
        "exact_source_quote": "*Solution A; Glucose 10 g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[1].items[9]",
        "exact_source_quote": "\"component_name\": \"Peptone\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q11",
    "ingredient": "Distilled water",
    "decision": "correct",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1000.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "500.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution B preparation; Distilled water",
        "exact_source_quote": "**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[2].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 500,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "This is a separate 500 ml water input in the named solution. The target 1000 G_PER_L and owner 500 G_PER_L are both wrong representations: restore both stage-specific liquid quantities rather than treating equal numbers as duplicate claims."
  },
  {
    "decision_id": "q12",
    "ingredient": "ZnSO4·7H2O",
    "decision": "correct",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution B preparation; ZnSO4·7H2O",
        "exact_source_quote": "**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[2].items[1]",
        "exact_source_quote": "\"component_name\": \"ZnSO4·7H2O\",\n          \"volume\": 0.001,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q13",
    "ingredient": "Na2CO3",
    "decision": "correct",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "10",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution B preparation; Na2CO3",
        "exact_source_quote": "**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[2].items[2]",
        "exact_source_quote": "\"component_name\": \"Na2CO3\",\n          \"volume\": 10,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q14",
    "ingredient": "MnSO4·7H2O",
    "decision": "correct",
    "stage": "Solution B preparation",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "0.001",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Solution B preparation; MnSO4·7H2O",
        "exact_source_quote": "**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[2].items[3]",
        "exact_source_quote": "\"component_name\": \"MnSO4·7H2O\",\n          \"volume\": 0.001,\n          \"unit\": \"g\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "Both layers flatten this source amount into final-medium ingredients. Preserve the printed batch grams in the named 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000 ml assembly is not a measured final volume. No attached amount evidence is present."
  },
  {
    "decision_id": "q15",
    "ingredient": "Solution A addition",
    "decision": "correct",
    "stage": "Assembly",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Assembly; Solution A addition",
        "exact_source_quote": "Solution A* 500 ml",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Solution A*\",\n          \"volume\": 500,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "The source adds 500 ml of the corresponding locally defined solution; the existing 500 G_PER_L unit is wrong. Preserve the addition and its correct local composition without adopting the unrelated MediaDive accession."
  },
  {
    "decision_id": "q16",
    "ingredient": "Solution B addition",
    "decision": "correct",
    "stage": "Assembly",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "500",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Assembly; Solution B addition",
        "exact_source_quote": "Solution B** 500 ml",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      },
      {
        "source_key": "togoM1799original",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Solution B**\",\n          \"volume\": 500,\n          \"unit\": \"ml\"",
        "snapshot_sha256": "71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8"
      }
    ],
    "interpretation": "The source adds 500 ml of the corresponding locally defined solution; the existing 500 G_PER_L unit is wrong. Preserve the addition and its correct local composition without adopting the unrelated MediaDive accession."
  },
  {
    "decision_id": "q17",
    "ingredient": "Final target pH",
    "decision": "add",
    "stage": "After A/B combination",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "ph_value",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; After A/B combination; Final target pH",
        "exact_source_quote": "Solutions A and B are autoclaved separately and combined before solidified. Final pH 10.3.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      }
    ],
    "interpretation": "Both layers omit the explicit final target pH 10.3; this is a source target, not an experimental measurement."
  },
  {
    "decision_id": "q18",
    "ingredient": "Separate autoclaving and combination",
    "decision": "add",
    "stage": "Preparation order",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Preparation order; Separate autoclaving and combination",
        "exact_source_quote": "Solutions A and B are autoclaved separately and combined before solidified. Final pH 10.3.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      }
    ],
    "interpretation": "Both layers omit separate autoclaving and combination before solidification. No temperature, duration or pressure is stated."
  },
  {
    "decision_id": "q19",
    "ingredient": "Sterilization cycle",
    "decision": "not_quantified",
    "stage": "Separate A/B autoclaving",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "sterilization",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; Separate A/B autoclaving; Sterilization cycle",
        "exact_source_quote": "Solutions A and B are autoclaved separately and combined before solidified. Final pH 10.3.",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      }
    ],
    "interpretation": "Do not transfer a cycle from another medium or the incorrectly referenced stocks."
  },
  {
    "decision_id": "q20",
    "ingredient": "Final measured volume",
    "decision": "not_quantified",
    "stage": "After A/B mixing",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/Alkali_B_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "nbrc1025",
        "source_url": "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025",
        "source_locator": "NBRC 1025; After A/B mixing; Final measured volume",
        "exact_source_quote": "Solution A* 500 ml Solution B** 500 ml",
        "snapshot_sha256": "017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e",
        "parsed_text_sha256": "6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811"
      }
    ],
    "interpretation": "The two solution additions total a nominal 1000 ml. Neither a measured final volume nor a make-up instruction is supplied; retain batch amounts and stage boundaries."
  }
]

### Incorrect stock cross-references

identity: concern. Targets: CultureMech:008367.

MediaDive 5342 contains 100 g NaCl and unrelated nutrients, while 5343 contains 80 g carbonate plus 100 g NaCl. The exact NBRC stocks instead contain the explicitly listed A constituents and B carbonate recipe. Both API volume fields are null; the APIs say bring their own stocks to 500 ml. None of those unrelated quantities are transferred.

### Asserted ontology and current CHEBI-based secondary metadata

grounding: concern. Targets: CultureMech:008367.

10 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 10/13 primary and 9/13 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Exact supplied-form mismatch is addressed separately; valid IDs and labels do not establish correct source grounding.

Instance coverage on a 0–100 percent scale, denominator 13: primary 76.92%; secondary 69.23%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Source chemical form support

grounding: concern. Targets: CultureMech:008367.

The source explicitly prints MnSO4·7H2O, but CHEBI:86360 represents anhydrous manganese(II) sulfate. Magnesium, copper and zinc hydrate forms and L-asparagine match their source specificity. Ferric sulfate hexahydrate remains ungrounded; do not infer a replacement identifier.

### Complete preparation and missing source evidence

completeness: concern. Targets: CultureMech:008367.

The source supplies two complete preparations, separate autoclaving, combination before solidification and final pH 10.3. Both layers lack this preparation and pH. Exact cycle, incubation conditions and a final measured volume are not supplied.

### Composition, physical state and growth scope

scope: supported. Targets: CultureMech:008367.

COMPLEX/UNDEFINED are supported by yeast extract and peptone; SOLID_AGAR agrees with required agar. Generic microbial-cultivation application and bacterial categorization do not establish a species or strain growth observation.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:008367.

26 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Claim-level evidence and transformation scope

evidence: concern. Targets: CultureMech:008367.

Accession notes and histories exist, but target and owner have no attached quantity or preparation evidence. Current source support is available; no assertion of original historical byte equivalence is made.

## Findings

### f1: Generic stock names link unrelated formulations

blocker / open / confirmed; issue key: unrelated-stock-identities.

Both layers assert MediaDive 5342/5343 for the exact NBRC A/B recipes. The captured referenced recipes are high-salt formulations with incompatible constituents. Empty local solution stubs and matching names do not justify those identities.

### f2: Water and solution volumes are stored as mass concentrations

major / open / confirmed; issue key: liquid-units-and-stage-collapse.

The source uses two distinct 500 ml water preparations and 500 ml additions of each solution. The target sums water to 1000 G_PER_L; the owner collapses it to 500 G_PER_L. Both solution doses are 500 G_PER_L, and batch ingredient masses are flattened without their solution scope.

### f3: Manganese sulfate hydrate is grounded to anhydrous salt

major / open / confirmed; issue key: manganese-hydrate.

The source and preferred term specify MnSO4·7H2O, whereas CHEBI:86360 has Mn.O4S without hydrate water. Valid ID-label correspondence does not establish the supplied form.

### f4: Separate sterilization and final pH are missing

major / open / confirmed; issue key: preparation-and-ph.

Both layers omit separate A/B autoclaving, combination before solidification and final target pH 10.3.

### f5: Formulation claims lack attached evidence

minor / open / confirmed; issue key: attached-evidence.

Source links and history do not attach the actual amount, stage, form or preparation evidence to retained claims.

## Recommended Actions And Acceptance Checks

### a1

Remove or replace the unsupported identities only after exact local source stock representation is established; retain stage composition and verify any proposed identifier independently.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Restore volume units, distinct A/B preparation membership and original batch mass basis in the owner; then regenerate the target after independent source checks. Do not sum stock water again as extra final-medium water.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve and independently verify the supplied hydrate identity before replacing its grounding; retain source mass and avoid molar conversion using the wrong form.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Add only the exact source preparation and final target pH with evidence; preserve the unspecified sterilization cycle.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach exact source snippets with persistent URL, original access time and snapshot hash to all curated claims; preserve history and distinguish current source support from historical import bytes.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/Alkali_B_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/alkali_b_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/Alkali_B_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Alkali_B_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch035/348/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch035/348/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Alkali_B_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Alkali_B_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/Alkali_B_medium.yaml:1:id: CultureMech:008367<br>./data/normalized_yaml/bacterial/alkali_b_medium.yaml:1:id: CultureMech:008367<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch035/source-preflight-bound/348/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 21 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| primary | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025; NBRC 1025 complete composition and preparation | supports | Exact A/B recipes, their liquid additions, separate sterilization and final pH are available. |
| provider | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799; $.meta; all three components and comments | supports | TOGO explicitly links this NBRC accession and preserves stage-specific amounts. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch035/348/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| solution5342 | https://mediadive.dsmz.de/rest/solution/5342; $.data.id, $.data.recipe and $.data.steps | refutes | Exact accession resolves to an unrelated high-salt recipe. Its quantities and preparation are identity-comparison context only, not transferred to this medium. |
| solution5342-local | data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml; Complete pinned referenced stock | context_only | The local referenced record corroborates the incompatible recipe identity; generic Solution A/B names cannot authenticate a correspondence. |
| solution5343 | https://mediadive.dsmz.de/rest/solution/5343; $.data.id, $.data.recipe and $.data.steps | refutes | Exact accession resolves to an unrelated high-salt recipe. Its quantities and preparation are identity-comparison context only, not transferred to this medium. |
| solution5343-local | data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml; Complete pinned referenced stock | context_only | The local referenced record corroborates the incompatible recipe identity; generic Solution A/B names cannot authenticate a correspondence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:131527 resolves to dipotassium hydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17196 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17196; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17196 resolves to L-asparagine. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17234 resolves to glucose. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:2509 resolves to agar. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:29377 resolves to sodium carbonate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86360 resolves to manganese(II) sulfate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527": [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527", "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17196": [{"label": "L-Asparagine", "match_type": "preferred_term", "identifier": "CHEBI:17196", "preferred_term": "L-Asparagine", "ontology_id": "CHEBI:17196", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier": "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| history-metadata | data/merge_yaml/merged/Alkali_B_medium.yaml; data/normalized_yaml/bacterial/alkali_b_medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/alkali_b_medium.yaml", "events": 13, "timestamp_issues": []}] |
| writer-0 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer can retain local stage compositions; the legacy-name resolver can select Solution A/B by generic name, and the duplicate repair uses equality of numbers without source-stage verification. Current code and recorded history explain review boundaries, not proven historical execution causation. |
| writer-1 | scripts/migrate_solutions_from_ingredients.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer can retain local stage compositions; the legacy-name resolver can select Solution A/B by generic name, and the duplicate repair uses equality of numbers without source-stage verification. Current code and recorded history explain review boundaries, not proven historical execution causation. |
| writer-2 | scripts/repair_merged_duplicates.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer can retain local stage compositions; the legacy-name resolver can select Solution A/B by generic name, and the duplicate repair uses equality of numbers without source-stage verification. Current code and recorded history explain review boundaries, not proven historical execution causation. |
| writer-3 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current importer can retain local stage compositions; the legacy-name resolver can select Solution A/B by generic name, and the duplicate repair uses equality of numbers without source-stage verification. Current code and recorded history explain review boundaries, not proven historical execution causation. |
| togoM1799-attempt | https://mediumapi.dbcls.jp/medium/M1799; Preserved exact public retrieval result | context_only | The optional alternate mediumapi request failed DNS. Exact original TOGO and NBRC primary content are available, so this failure does not prevent assessment of the current recipe. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- The optional alternate mediumapi request failed DNS. Exact original TOGO and NBRC primary content are available, so this failure does not prevent assessment of the current recipe.
- The unrelated 5342/5343 records are identity-comparison context only. Their stock strengths, salt content and preparation conditions are excluded from the reviewed NBRC medium. No final measured volume or source-absent cycle is inferred.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191750Z-culturemech-008367-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: alkali_b_medium (CultureMech:008367)'
started_at: '2026-10-21T19:13:56Z'
finished_at: '2026-10-21T19:17:50Z'
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
summary: The exact NBRC recipe resolves, but both layers flatten separately prepared
  A/B solutions, misstate liquid units and point to unrelated MediaDive stocks. The
  later water-collapse repair does not restore the two source stages.
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
  - path: data/merge_yaml/merged/Alkali_B_medium.yaml
    sha256: 146451a34cba1e8dd1b30a4bbcdae05b867090700ec1a5de749a29f8339748ec
    role: target
  - path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
    sha256: 2ab5b67c7c07581575acf47faa7c669465a80c6d583478576e8dbfc84c5f9c6a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  selection: Task review 348; batch 035 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding thirty-four task batches
    contain 340 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 343 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008367
targets:
- target_id: CultureMech:008367
  path: data/merge_yaml/merged/Alkali_B_medium.yaml
  label: alkali_b_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Alkali_B_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Alkali_B_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch035/348/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/348/strict.tsv"
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Alkali_B_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Alkali_B_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008367
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
  - CultureMech:008367
- check_id: togoM1799-source-access
  name: 'Exact source content access: togoM1799'
  required: false
  status: unavailable
  summary: The optional alternate mediumapi request failed DNS. Exact original TOGO
    and NBRC primary content are available, so this failure does not prevent assessment
    of the current recipe.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - togoM1799-attempt
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/Alkali_B_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/alkali_b_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Alkali_B_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:41.698094Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Alkali_B_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch035/348/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:43.079697Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-035/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch035/348/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Alkali_B_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:44.672034Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Alkali_B_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T19:14:45.550610Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T19:17:48Z'
  support: supports
  summary: './data/merge_yaml/merged/Alkali_B_medium.yaml:1:id: CultureMech:008367

    ./data/normalized_yaml/bacterial/alkali_b_medium.yaml:1:id: CultureMech:008367

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/source-preflight-bound/348/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T19:17:48Z'
  support: supports
  summary: 21 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 73bf1ca0390c528575e9b7b5c1b11c9395951a563485eae1ec86bd5810d60df3
- evidence_id: primary
  kind: database
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025
  locator: NBRC 1025 complete composition and preparation
  accessed_at: '2026-10-21T19:02:25.500920Z'
  support: supports
  summary: Exact A/B recipes, their liquid additions, separate sterilization and final
    pH are available.
  quote: Composition Solution A* 500 ml Solution B** 500 ml *Solution A; Glucose 10
    g, L-Asparagine 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO
    4 ·7H 2 O 0.1 g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15
    g, Distilled water 500 ml. **Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO 4 ·7H 2
    O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml. Solutions A and B are autoclaved
    separately and combined before solidified. Final pH 10.3.
  snapshot_sha256: 017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e
- evidence_id: provider
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799
  locator: $.meta; all three components and comments
  accessed_at: '2026-10-21T19:02:24.323718Z'
  support: supports
  summary: TOGO explicitly links this NBRC accession and preserves stage-specific
    amounts.
  quote: '"original_media_id": "NBRC_M1025"'
  snapshot_sha256: 71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch035/348/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 1ec1dc54a2758dd983ac11a92a5c2abab1a0b79133c4036f3acefdead1fd76b0
- evidence_id: solution5342
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  locator: $.data.id, $.data.recipe and $.data.steps
  accessed_at: '2026-10-21T07:31:13.269119Z'
  support: refutes
  summary: Exact accession resolves to an unrelated high-salt recipe. Its quantities
    and preparation are identity-comparison context only, not transferred to this
    medium.
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
  locator: Complete pinned referenced stock
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: The local referenced record corroborates the incompatible recipe identity;
    generic Solution A/B names cannot authenticate a correspondence.
  snapshot_sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
- evidence_id: solution5343
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  locator: $.data.id, $.data.recipe and $.data.steps
  accessed_at: '2026-10-21T07:31:13.547266Z'
  support: refutes
  summary: Exact accession resolves to an unrelated high-salt recipe. Its quantities
    and preparation are identity-comparison context only, not transferred to this
    medium.
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
  locator: Complete pinned referenced stock
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: The local referenced record corroborates the incompatible recipe identity;
    generic Solution A/B names cannot authenticate a correspondence.
  snapshot_sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
- evidence_id: chebi17196
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17196
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T19:02:24.508520Z'
  support: supports
  summary: CHEBI:17196 resolves to L-asparagine. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: 5e546def4d69297d487ef85c54167891ab8505aa4b59957410bcc05722f4b8a2
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.738243Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
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
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash
  accessed_at: '2026-10-21T19:17:48Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:131527":
    [{"label": "K2HPO4", "match_type": "preferred_term", "identifier": "CHEBI:131527",
    "preferred_term": "K2HPO4", "ontology_id": "CHEBI:131527", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:15377": [{"label": "Distilled water", "match_type":
    "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water",
    "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:17196": [{"label": "L-Asparagine", "match_type": "preferred_term", "identifier":
    "CHEBI:17196", "preferred_term": "L-Asparagine", "ontology_id": "CHEBI:17196",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label":
    "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term":
    "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:2509": [{"label": "Agar", "match_type": "preferred_term", "identifier":
    "CHEBI:2509", "preferred_term": "Agar", "ontology_id": "CHEBI:2509", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:29377": [{"label": "Na2CO3", "match_type":
    "preferred_term", "identifier": "CHEBI:29377", "preferred_term": "Na2CO3", "ontology_id":
    "CHEBI:29377", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "Sodium
    carbonate solution", "match_type": "preferred_term", "identifier": "CHEBI:29377",
    "preferred_term": "Sodium carbonate solution", "ontology_id": "CHEBI:29377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term":
    "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id":
    "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term":
    "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/Alkali_B_medium.yaml; data/normalized_yaml/bacterial/alkali_b_medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/alkali_b_medium.yaml", "events": 13, "timestamp_issues":
    []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Current importer can retain local stage compositions; the legacy-name resolver
    can select Solution A/B by generic name, and the duplicate repair uses equality
    of numbers without source-stage verification. Current code and recorded history
    explain review boundaries, not proven historical execution causation.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-1
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Current importer can retain local stage compositions; the legacy-name resolver
    can select Solution A/B by generic name, and the duplicate repair uses equality
    of numbers without source-stage verification. Current code and recorded history
    explain review boundaries, not proven historical execution causation.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-2
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Current importer can retain local stage compositions; the legacy-name resolver
    can select Solution A/B by generic name, and the duplicate repair uses equality
    of numbers without source-stage verification. Current code and recorded history
    explain review boundaries, not proven historical execution causation.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T19:17:48Z'
  support: context_only
  summary: Current importer can retain local stage compositions; the legacy-name resolver
    can select Solution A/B by generic name, and the duplicate repair uses equality
    of numbers without source-stage verification. Current code and recorded history
    explain review boundaries, not proven historical execution causation.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: togoM1799-attempt
  kind: database
  reference: https://mediumapi.dbcls.jp/medium/M1799
  locator: Preserved exact public retrieval result
  accessed_at: '2026-10-21T19:02:23.207482Z'
  support: context_only
  summary: The optional alternate mediumapi request failed DNS. Exact original TOGO
    and NBRC primary content are available, so this failure does not prevent assessment
    of the current recipe.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact medium and maintained owner
  outcome: supported
  summary: The exact NBRC accession and TOGO identifier agree. One maintained bacterial
    owner resolves by stable ID and complete merge provenance; no strain-specific
    growth, supplier identity or citation is invented.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
- assessment_id: ownership
  area: ownership
  topic: Generated versus maintained water history
  outcome: concern
  summary: The target retains 1000 G_PER_L water from summing two 500 entries; the
    owner later collapses them to 500 G_PER_L. The source has one 500 ml water entry
    in each distinct solution. Neither numerical operation establishes correct scientific
    stage or units. Other source amounts and the two wrong stock links remain in both
    layers.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - record
  - owner-0
  - primary
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 20 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"decision_id\": \"q1\",\n    \"ingredient\": \"Distilled\
    \ water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; Distilled\
    \ water\",\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine\
    \ 0.3 g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1\
    \ g, Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 500,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a separate 500 ml water input in the\
    \ named solution. The target 1000 G_PER_L and owner 500 G_PER_L are both wrong\
    \ representations: restore both stage-specific liquid quantities rather than treating\
    \ equal numbers as duplicate claims.\"\n  },\n  {\n    \"decision_id\": \"q2\"\
    ,\n    \"ingredient\": \"MgSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Solution A preparation\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[1].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\",\n \
    \       \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; MgSO4·7H2O\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgSO4·7H2O\\\",\\n          \\\"volume\\\": 0.1,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q3\",\n    \"ingredient\":\
    \ \"Yeast extract\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution\
    \ A preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; Yeast extract\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 0.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\n      }\n\
    \    ],\n    \"interpretation\": \"Both layers flatten this source amount into\
    \ final-medium ingredients. Preserve the printed batch grams in the named 500\
    \ ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000\
    \ ml assembly is not a measured final volume. No attached amount evidence is present.\"\
    \n  },\n  {\n    \"decision_id\": \"q4\",\n    \"ingredient\": \"K2HPO4\",\n \
    \   \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; K2HPO4\",\n\
    \        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"K2HPO4\\\",\\n          \\\"volume\\\": 1,\\n\
    \          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q5\",\n    \"ingredient\":\
    \ \"CuSO4·5H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution A\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; CuSO4·5H2O\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CuSO4·5H2O\\\",\\n          \\\"volume\\\": 0.001,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q6\",\n    \"ingredient\":\
    \ \"Glucose\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; Glucose\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Glucose\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q7\",\n    \"ingredient\":\
    \ \"L-Asparagine\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution\
    \ A preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.3\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; L-Asparagine\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"L-Asparagine\\\",\\n          \\\"volume\\\":\
    \ 0.3,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\n      }\n\
    \    ],\n    \"interpretation\": \"Both layers flatten this source amount into\
    \ final-medium ingredients. Preserve the printed batch grams in the named 500\
    \ ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000\
    \ ml assembly is not a measured final volume. No attached amount evidence is present.\"\
    \n  },\n  {\n    \"decision_id\": \"q8\",\n    \"ingredient\": \"Agar\",\n   \
    \ \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\",\n   \
    \ \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"15\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; Agar\",\n\
    \        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Agar\\\",\\n          \\\"volume\\\": 15,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q9\",\n    \"ingredient\":\
    \ \"Fe2(SO4)3·6H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution\
    \ A preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.01\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; Fe2(SO4)3·6H2O\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Fe2(SO4)3·6H2O\\\",\\n          \\\"volume\\\"\
    : 0.01,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\n      }\n\
    \    ],\n    \"interpretation\": \"Both layers flatten this source amount into\
    \ final-medium ingredients. Preserve the printed batch grams in the named 500\
    \ ml preparation and distinguish its subsequent 500 ml addition; a nominal 1000\
    \ ml assembly is not a measured final volume. No attached amount evidence is present.\"\
    \n  },\n  {\n    \"decision_id\": \"q10\",\n    \"ingredient\": \"Peptone\",\n\
    \    \"decision\": \"correct\",\n    \"stage\": \"Solution A preparation\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution A preparation; Peptone\"\
    ,\n        \"exact_source_quote\": \"*Solution A; Glucose 10 g, L-Asparagine 0.3\
    \ g, Peptone 0.2 g, Yeast extract 0.1 g, K 2 HPO 4 1 g, MgSO 4 ·7H 2 O 0.1 g,\
    \ Fe 2 (SO 4 ) 3 ·6H 2 O 0.01 g, CuSO 4 ·5H 2 O 0.001 g, Agar 15 g, Distilled\
    \ water 500 ml.\",\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[1].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Peptone\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q11\",\n    \"ingredient\"\
    : \"Distilled water\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution\
    \ B preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1000.0\",\n          \"unit\": \"G_PER_L\"\n     \
    \   }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500.0\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution B preparation; Distilled\
    \ water\",\n        \"exact_source_quote\": \"**Solution B; ZnSO 4 ·7H 2 O 0.001\
    \ g, MnSO 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.\",\n    \
    \    \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[2].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 500,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\n      }\n\
    \    ],\n    \"interpretation\": \"This is a separate 500 ml water input in the\
    \ named solution. The target 1000 G_PER_L and owner 500 G_PER_L are both wrong\
    \ representations: restore both stage-specific liquid quantities rather than treating\
    \ equal numbers as duplicate claims.\"\n  },\n  {\n    \"decision_id\": \"q12\"\
    ,\n    \"ingredient\": \"ZnSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"\
    stage\": \"Solution B preparation\",\n    \"local_fields\": [\n      {\n     \
    \   \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\",\n        \"field_path\"\
    : \"ingredients[10].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"0.001\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n\
    \        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\",\n\
    \        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution B preparation; ZnSO4·7H2O\"\
    ,\n        \"exact_source_quote\": \"**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO\
    \ 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[2].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"ZnSO4·7H2O\\\",\\n          \\\"volume\\\": 0.001,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q13\",\n    \"ingredient\"\
    : \"Na2CO3\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution B preparation\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"10\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution B preparation; Na2CO3\",\n\
    \        \"exact_source_quote\": \"**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO\
    \ 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[2].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Na2CO3\\\",\\n          \\\"volume\\\": 10,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q14\",\n    \"ingredient\"\
    : \"MnSO4·7H2O\",\n    \"decision\": \"correct\",\n    \"stage\": \"Solution B\
    \ preparation\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.001\",\n          \"unit\": \"G_PER_L\"\n      \
    \  }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Solution B preparation; MnSO4·7H2O\"\
    ,\n        \"exact_source_quote\": \"**Solution B; ZnSO 4 ·7H 2 O 0.001 g, MnSO\
    \ 4 ·7H 2 O 0.001 g, Na 2 CO 3 10 g, Distilled water 500 ml.\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[2].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MnSO4·7H2O\\\",\\n          \\\"volume\\\": 0.001,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers flatten this source amount\
    \ into final-medium ingredients. Preserve the printed batch grams in the named\
    \ 500 ml preparation and distinguish its subsequent 500 ml addition; a nominal\
    \ 1000 ml assembly is not a measured final volume. No attached amount evidence\
    \ is present.\"\n  },\n  {\n    \"decision_id\": \"q15\",\n    \"ingredient\"\
    : \"Solution A addition\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Assembly\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Assembly; Solution A addition\",\n\
    \        \"exact_source_quote\": \"Solution A* 500 ml\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution A*\\\",\\n          \\\"volume\\\": 500,\\\
    n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\
    \n      }\n    ],\n    \"interpretation\": \"The source adds 500 ml of the corresponding\
    \ locally defined solution; the existing 500 G_PER_L unit is wrong. Preserve the\
    \ addition and its correct local composition without adopting the unrelated MediaDive\
    \ accession.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"ingredient\":\
    \ \"Solution B addition\",\n    \"decision\": \"correct\",\n    \"stage\": \"\
    Assembly\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"500\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Assembly; Solution B addition\",\n\
    \        \"exact_source_quote\": \"Solution B** 500 ml\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      },\n      {\n        \"source_key\": \"togoM1799original\",\n        \"\
    source_url\": \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1799\"\
    ,\n        \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Solution B**\\\",\\n          \\\"volume\\\":\
    \ 500,\\n          \\\"unit\\\": \\\"ml\\\"\",\n        \"snapshot_sha256\": \"\
    71423884382f9683c9573b9f45102bdc43f9177f6090f13e4b21e0fd2f18fed8\"\n      }\n\
    \    ],\n    \"interpretation\": \"The source adds 500 ml of the corresponding\
    \ locally defined solution; the existing 500 G_PER_L unit is wrong. Preserve the\
    \ addition and its correct local composition without adopting the unrelated MediaDive\
    \ accession.\"\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"ingredient\":\
    \ \"Final target pH\",\n    \"decision\": \"add\",\n    \"stage\": \"After A/B\
    \ combination\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"ph_value\",\n        \"stored\": null\n      }\n\
    \    ],\n    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1025\"\
    ,\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; After A/B combination; Final target\
    \ pH\",\n        \"exact_source_quote\": \"Solutions A and B are autoclaved separately\
    \ and combined before solidified. Final pH 10.3.\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers omit the explicit final\
    \ target pH 10.3; this is a source target, not an experimental measurement.\"\n\
    \  },\n  {\n    \"decision_id\": \"q18\",\n    \"ingredient\": \"Separate autoclaving\
    \ and combination\",\n    \"decision\": \"add\",\n    \"stage\": \"Preparation\
    \ order\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Preparation order; Separate autoclaving\
    \ and combination\",\n        \"exact_source_quote\": \"Solutions A and B are\
    \ autoclaved separately and combined before solidified. Final pH 10.3.\",\n  \
    \      \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      }\n    ],\n    \"interpretation\": \"Both layers omit separate autoclaving\
    \ and combination before solidification. No temperature, duration or pressure\
    \ is stated.\"\n  },\n  {\n    \"decision_id\": \"q19\",\n    \"ingredient\":\
    \ \"Sterilization cycle\",\n    \"decision\": \"not_quantified\",\n    \"stage\"\
    : \"Separate A/B autoclaving\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\",\n        \"field_path\"\
    : \"sterilization\",\n        \"stored\": null\n      },\n      {\n        \"\
    input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\",\n        \"\
    field_path\": \"sterilization\",\n        \"stored\": null\n      }\n    ],\n\
    \    \"source_snippets\": [\n      {\n        \"source_key\": \"nbrc1025\",\n\
    \        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; Separate A/B autoclaving; Sterilization\
    \ cycle\",\n        \"exact_source_quote\": \"Solutions A and B are autoclaved\
    \ separately and combined before solidified. Final pH 10.3.\",\n        \"snapshot_sha256\"\
    : \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\",\n    \
    \    \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      }\n    ],\n    \"interpretation\": \"Do not transfer a cycle from another\
    \ medium or the incorrectly referenced stocks.\"\n  },\n  {\n    \"decision_id\"\
    : \"q20\",\n    \"ingredient\": \"Final measured volume\",\n    \"decision\":\
    \ \"not_quantified\",\n    \"stage\": \"After A/B mixing\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/Alkali_B_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/alkali_b_medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"nbrc1025\",\n        \"source_url\": \"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1025\"\
    ,\n        \"source_locator\": \"NBRC 1025; After A/B mixing; Final measured volume\"\
    ,\n        \"exact_source_quote\": \"Solution A* 500 ml Solution B** 500 ml\"\
    ,\n        \"snapshot_sha256\": \"017ad73b6bcd0a6980053ab0bc740827794d6c5ec84e4b61315222931bcf035e\"\
    ,\n        \"parsed_text_sha256\": \"6fe66f0f8af28c0949083aef8dcdea14023425eba2491f47ed55a179b98ec811\"\
    \n      }\n    ],\n    \"interpretation\": \"The two solution additions total\
    \ a nominal 1000 ml. Neither a measured final volume nor a make-up instruction\
    \ is supplied; retain batch amounts and stage boundaries.\"\n  }\n]"
- assessment_id: stocks
  area: identity
  topic: Incorrect stock cross-references
  outcome: concern
  summary: MediaDive 5342 contains 100 g NaCl and unrelated nutrients, while 5343
    contains 80 g carbonate plus 100 g NaCl. The exact NBRC stocks instead contain
    the explicitly listed A constituents and B carbonate recipe. Both API volume fields
    are null; the APIs say bring their own stocks to 500 ml. None of those unrelated
    quantities are transferred.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - primary
  - provider
  - solution5342
  - solution5343
  - solution5342-local
  - solution5343-local
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: concern
  summary: '10 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 10/13
    primary and 9/13 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Exact supplied-form mismatch is addressed separately; valid IDs and labels do
    not establish correct source grounding.'
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi131527
  - chebi15377
  - chebi17196
  - chebi17234
  - chebi2509
  - chebi29377
  - chebi31440
  - chebi31795
  - chebi32312
  - chebi86360
  details: 'Instance coverage on a 0–100 percent scale, denominator 13: primary 76.92%;
    secondary 69.23%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: forms
  area: grounding
  topic: Source chemical form support
  outcome: concern
  summary: The source explicitly prints MnSO4·7H2O, but CHEBI:86360 represents anhydrous
    manganese(II) sulfate. Magnesium, copper and zinc hydrate forms and L-asparagine
    match their source specificity. Ferric sulfate hexahydrate remains ungrounded;
    do not infer a replacement identifier.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - primary
  - chebi86360
- assessment_id: preparation
  area: completeness
  topic: Complete preparation and missing source evidence
  outcome: concern
  summary: The source supplies two complete preparations, separate autoclaving, combination
    before solidification and final pH 10.3. Both layers lack this preparation and
    pH. Exact cycle, incubation conditions and a final measured volume are not supplied.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
- assessment_id: classification
  area: scope
  topic: Composition, physical state and growth scope
  outcome: supported
  summary: COMPLEX/UNDEFINED are supported by yeast extract and peptone; SOLID_AGAR
    agrees with required agar. Generic microbial-cultivation application and bacterial
    categorization do not establish a species or strain growth observation.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - primary
  - record
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 26 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: provenance
  area: evidence
  topic: Claim-level evidence and transformation scope
  outcome: concern
  summary: Accession notes and histories exist, but target and owner have no attached
    quantity or preparation evidence. Current source support is available; no assertion
    of original historical byte equivalence is made.
  target_ids:
  - CultureMech:008367
  evidence_ids:
  - record
  - owner-0
  - primary
  - provider
  - writer-0
  - writer-1
  - writer-2
findings:
- finding_id: f1
  issue_key: unrelated-stock-identities
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generic stock names link unrelated formulations
  description: Both layers assert MediaDive 5342/5343 for the exact NBRC A/B recipes.
    The captured referenced recipes are high-salt formulations with incompatible constituents.
    Empty local solution stubs and matching names do not justify those identities.
  target_ids:
  - CultureMech:008367
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions
  evidence_ids:
  - primary
  - provider
  - solution5342
  - solution5343
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  issue_key: liquid-units-and-stage-collapse
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water and solution volumes are stored as mass concentrations
  description: The source uses two distinct 500 ml water preparations and 500 ml additions
    of each solution. The target sums water to 1000 G_PER_L; the owner collapses it
    to 500 G_PER_L. Both solution doses are 500 G_PER_L, and batch ingredient masses
    are flattened without their solution scope.
  target_ids:
  - CultureMech:008367
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - primary
  - quantity-inventory
  - record
  - owner-0
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  issue_key: manganese-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Manganese sulfate hydrate is grounded to anhydrous salt
  description: The source and preferred term specify MnSO4·7H2O, whereas CHEBI:86360
    has Mn.O4S without hydrate water. Valid ID-label correspondence does not establish
    the supplied form.
  target_ids:
  - CultureMech:008367
  field_paths:
  - ingredients[12].term
  evidence_ids:
  - primary
  - chebi86360
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  issue_key: preparation-and-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Separate sterilization and final pH are missing
  description: Both layers omit separate A/B autoclaving, combination before solidification
    and final target pH 10.3.
  target_ids:
  - CultureMech:008367
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - primary
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  issue_key: attached-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Formulation claims lack attached evidence
  description: Source links and history do not attach the actual amount, stage, form
    or preparation evidence to retained claims.
  target_ids:
  - CultureMech:008367
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  description: Remove or replace the unsupported identities only after exact local
    source stock representation is established; retain stage composition and verify
    any proposed identifier independently.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  description: Restore volume units, distinct A/B preparation membership and original
    batch mass basis in the owner; then regenerate the target after independent source
    checks. Do not sum stock water again as extra final-medium water.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  description: Resolve and independently verify the supplied hydrate identity before
    replacing its grounding; retain source mass and avoid molar conversion using the
    wrong form.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  description: Add only the exact source preparation and final target pH with evidence;
    preserve the unspecified sterilization cycle.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
  description: Attach exact source snippets with persistent URL, original access time
    and snapshot hash to all curated claims; preserve history and distinguish current
    source support from historical import bytes.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008367
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/alkali_b_medium.yaml
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
- The optional alternate mediumapi request failed DNS. Exact original TOGO and NBRC
  primary content are available, so this failure does not prevent assessment of the
  current recipe.
- The unrelated 5342/5343 records are identity-comparison context only. Their stock
  strengths, salt content and preparation conditions are excluded from the reviewed
  NBRC medium. No final measured volume or source-absent cycle is inferred.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-035
- generated-medium
```
