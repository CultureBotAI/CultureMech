# Source and formulation review: aminivibrio_asinoensis_medium (CultureMech:010414)

- Review: 20261021T142653Z-culturemech-010414-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T14:22:44Z
- Finished UTC: 2026-10-21T14:26:53Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

JCM940 identity resolves, but the generated record and its owner flatten vitamin-stock amounts, use mass units for water and liquid additions, omit preparation, and retain different duplicate-water histories. Required source sections are available; dependency evidence is restricted to the transferred Fe, trace and selenite stocks.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 248; batch 025 item 8 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding twenty-four task batches contain 240 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3 contains 41 validated baseline bundles covering 3 current merged paths. Unioning all prior lists with this baseline covers 243 of 6320 current merged paths, including 3 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 033ef56966c19f8948d84a579b3f280e3e94e9e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010414 | data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml | generated | aminivibrio_asinoensis_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010414 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010414 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/248/strict.tsv |
| validate-terms | passed | True | CultureMech:010414 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010414 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010414 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010414.

The four documented recipes completed; interpret the scope of each separately.

### Complete source-stage quantity decision inventory

quantity: concern. Targets: CultureMech:010414.

45 source-scoped decisions, including every local concentration and explicit source-only quantities. Verified applies only to the named local layer with attached matching evidence.

[
  {
    "quantity_id": "q1",
    "quantity": "Distilled water",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "2.0",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[0].concentration",
        "stored": {
          "value": "1.0",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[0]",
        "exact_source_quote": "\"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed. Generated 2.0 G_PER_L and owner 1.0 G_PER_L both misrepresent liquid water; the owner repair does not recover separate main/vitamin water stages."
  },
  {
    "quantity_id": "q2",
    "quantity": "Yeast extract",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[1].concentration",
        "stored": {
          "value": "2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "Yeast extract 2.0 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[1]",
        "exact_source_quote": "\"component_name\": \"Yeast extract\",\n          \"volume\": 2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q3",
    "quantity": "NaCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "NaCl 1.0 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[2]",
        "exact_source_quote": "\"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q4",
    "quantity": "CaCl2・2H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[3].concentration",
        "stored": {
          "value": "0.15",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "CaCl 2 ·2H 2 O 0.15 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[3]",
        "exact_source_quote": "\"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q5",
    "quantity": "KH2PO4",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[4].concentration",
        "stored": {
          "value": "0.2",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "KH 2 PO 4 0.2 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[4]",
        "exact_source_quote": "\"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q6",
    "quantity": "NH4Cl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[5].concentration",
        "stored": {
          "value": "0.25",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "NH 4 Cl 0.25 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[5]",
        "exact_source_quote": "\"component_name\": \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q7",
    "quantity": "Resazurin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[6].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "Resazurin 0.4 mg",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[6]",
        "exact_source_quote": "\"component_name\": \"Resazurin\",\n          \"volume\": 0.4,\n          \"unit\": \"mg\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed. Source 0.4 mg is not local 0.4 g/L."
  },
  {
    "quantity_id": "q8",
    "quantity": "MgCl2・6H2O",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[7].concentration",
        "stored": {
          "value": "0.4",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "MgCl 2 ·6H 2 O 0.4 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[7]",
        "exact_source_quote": "\"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q9",
    "quantity": "KCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[8].concentration",
        "stored": {
          "value": "0.5",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "KCl 0.5 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[8]",
        "exact_source_quote": "\"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q10",
    "quantity": "Sodium pyruvate",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[9].concentration",
        "stored": {
          "value": "1.1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table: exact named ingredient",
        "exact_source_quote": "Sodium pyruvate 1.1 g",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      },
      {
        "source_key": "togoM987",
        "source_url": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987",
        "source_locator": "$.components[0].items[9]",
        "exact_source_quote": "\"component_name\": \"Sodium pyruvate\",\n          \"volume\": 1.1,\n          \"unit\": \"g\"",
        "snapshot_sha256": "f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70"
      }
    ],
    "source_stage_and_basis": "Original main-table batch input, with 1 L water plus separate stock additions. Preserve the stated amount and unit; neither this water amount nor provider 1041 mL independently establishes final-medium volume. No concentration conversion is proposed."
  },
  {
    "quantity_id": "q11",
    "quantity": "FeCl2 solution (see Medium [M180])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[0].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table / post-cooling additions / final per-liter sulfide addition, as specified",
        "exact_source_quote": "FeCl 2 solution (see Medium No. 187 ) 1.0 ml",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Main-table receiving-batch addition before autoclaving. Retain liquid dose and exact source reference; current composition is empty."
  },
  {
    "quantity_id": "q12",
    "quantity": "Trace element solution (see Medium [M180])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table / post-cooling additions / final per-liter sulfide addition, as specified",
        "exact_source_quote": "Trace element solution (see Medium No. 187 ) 1.0 ml",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Main-table receiving-batch addition before autoclaving. Retain liquid dose and exact source reference; current composition is empty."
  },
  {
    "quantity_id": "q13",
    "quantity": "Selenite--tungstate solution (see Medium [M431])",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[2].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table / post-cooling additions / final per-liter sulfide addition, as specified",
        "exact_source_quote": "Selenite tungstate solution (see Medium No. 431 ) 1.0 ml",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Main-table receiving-batch addition before autoclaving. Retain liquid dose and exact source reference; current composition is empty."
  },
  {
    "quantity_id": "q14",
    "quantity": "8% NaHCO3 solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[3].concentration",
        "stored": {
          "value": "30",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table / post-cooling additions / final per-liter sulfide addition, as specified",
        "exact_source_quote": "8% NaHCO 3 solution 30.0 ml",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "After cooling, from anaerobic filter-sterilized stocks. Retain liquid dose and exact source reference; current composition is empty."
  },
  {
    "quantity_id": "q15",
    "quantity": "Vitamin solution (see below)",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[4].concentration",
        "stored": {
          "value": "1",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table / post-cooling additions / final per-liter sulfide addition, as specified",
        "exact_source_quote": "Vitamin solution (see below) 1.0 ml",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "After cooling, from anaerobic filter-sterilized stocks. Retain liquid dose and exact source reference; current composition is empty."
  },
  {
    "quantity_id": "q16",
    "quantity": "5% Na2S・9H2O solution",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[5].concentration",
        "stored": {
          "value": "7",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main table / post-cooling additions / final per-liter sulfide addition, as specified",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution 7.0 ml",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "After distribution: explicitly 7 mL per liter, from an anaerobic stock. Do not reinterpret as 7 g/L or assume the initial batch final volume. Retain liquid dose and exact source reference; current composition is empty."
  },
  {
    "quantity_id": "q17",
    "quantity": "Carbon dioxide gas",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[10].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main preparation gas atmosphere",
        "exact_source_quote": "N 2 -CO 2 (80:20, v/v)",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Current VARIABLE does not retain the specified 80:20 v/v N2:CO2 mixture. Record the mixture condition without inventing an absolute gas dose."
  },
  {
    "quantity_id": "q18",
    "quantity": "Nitrogen gas",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[11].concentration",
        "stored": {
          "value": "variable",
          "unit": "VARIABLE"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Main preparation gas atmosphere",
        "exact_source_quote": "N 2 -CO 2 (80:20, v/v)",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Current VARIABLE does not retain the specified 80:20 v/v N2:CO2 mixture. Record the mixture condition without inventing an absolute gas dose."
  },
  {
    "quantity_id": "q19",
    "quantity": "Biotin",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[12].concentration",
        "stored": {
          "value": "20",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Vitamin solution table: exact named ingredient",
        "exact_source_quote": "Biotin 20.0 mg",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "This is a milligram input to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving batch; it is not grams per liter of final medium. No assumed final stock volume or vitamin B12 chemical subtype."
  },
  {
    "quantity_id": "q20",
    "quantity": "p--Aminobenzoic acid",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "80",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[13].concentration",
        "stored": {
          "value": "80",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Vitamin solution table: exact named ingredient",
        "exact_source_quote": "p -Aminobenzoic acid 80.0 mg",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "This is a milligram input to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving batch; it is not grams per liter of final medium. No assumed final stock volume or vitamin B12 chemical subtype."
  },
  {
    "quantity_id": "q21",
    "quantity": "Thiamine・HCl",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[14].concentration",
        "stored": {
          "value": "200",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Vitamin solution table: exact named ingredient",
        "exact_source_quote": "Thiamine·HCl 200.0 mg",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "This is a milligram input to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving batch; it is not grams per liter of final medium. No assumed final stock volume or vitamin B12 chemical subtype."
  },
  {
    "quantity_id": "q22",
    "quantity": "Vitamin B12",
    "decision": "correct",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "ingredients[15].concentration",
        "stored": {
          "value": "50",
          "unit": "G_PER_L"
        }
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Vitamin solution table: exact named ingredient",
        "exact_source_quote": "Vitamin B 1 2 50.0 mg",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "This is a milligram input to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving batch; it is not grams per liter of final medium. No assumed final stock volume or vitamin B12 chemical subtype."
  },
  {
    "quantity_id": "q23",
    "quantity": "Separate vitamin-stock water",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[4].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Vitamin solution table: water row",
        "exact_source_quote": "Vitamin B 1 2 50.0 mg Distilled water 1.0 L",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Retain the independent 1 L vitamin-stock water input; do not sum it with the main water."
  },
  {
    "quantity_id": "q24",
    "quantity": "Stock percentage: 8% NaHCO 3 solution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[3].preferred_term",
        "stored": "8% NaHCO3 solution"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[3].preferred_term",
        "stored": "8% NaHCO3 solution"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Named receiving-stock reagent",
        "exact_source_quote": "8% NaHCO 3 solution",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "The existing name preserves the percentage numeral but lacks attached evidence. Percentage basis is unspecified; no w/v, v/v, density or mass conversion is inferred."
  },
  {
    "quantity_id": "q25",
    "quantity": "Stock percentage: 5% Na 2 S·9H 2 O solution",
    "decision": "evidence_only",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[5].preferred_term",
        "stored": "5% Na2S・9H2O solution"
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[5].preferred_term",
        "stored": "5% Na2S・9H2O solution"
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Named receiving-stock reagent",
        "exact_source_quote": "5% Na 2 S·9H 2 O solution",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "The existing name preserves the percentage numeral but lacks attached evidence. Percentage basis is unspecified; no w/v, v/v, density or mass conversion is inferred."
  },
  {
    "quantity_id": "q26",
    "quantity": "Stock0: 25% HCl (7.7 M) 10.0 ml",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 solution table: exact named row",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q27",
    "quantity": "Stock0: FeCl 2 ·4H 2 O 1.5 g",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 solution table: exact named row",
        "exact_source_quote": "FeCl 2 ·4H 2 O 1.5 g",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q28",
    "quantity": "Stock0: Distilled water 990.0 ml",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 solution table: exact named row",
        "exact_source_quote": "Distilled water 990.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q29",
    "quantity": "Stock1: ZnCl 2 70.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "ZnCl 2 70.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q30",
    "quantity": "Stock1: MnCl 2 ·4H 2 O 100.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "MnCl 2 ·4H 2 O 100.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q31",
    "quantity": "Stock1: H 3 BO 3 6.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "H 3 BO 3 6.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q32",
    "quantity": "Stock1: CoCl 2 ·6H 2 O 190.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "CoCl 2 ·6H 2 O 190.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q33",
    "quantity": "Stock1: CuCl 2 ·2H 2 O 2.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "CuCl 2 ·2H 2 O 2.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q34",
    "quantity": "Stock1: NiCl 2 ·6H 2 O 24.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "NiCl 2 ·6H 2 O 24.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q35",
    "quantity": "Stock1: Na 2 MoO 4 ·2H 2 O 36.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "Na 2 MoO 4 ·2H 2 O 36.0 mg",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q36",
    "quantity": "Stock1: Distilled water 1.0 L",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[1].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "Trace element solution table: exact named row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q37",
    "quantity": "Stock2: NaOH 0.4 g",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate solution table: exact named row",
        "exact_source_quote": "NaOH 0.4 g",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q38",
    "quantity": "Stock2: Na 2 SeO 3 ·5H 2 O 6.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate solution table: exact named row",
        "exact_source_quote": "Na 2 SeO 3 ·5H 2 O 6.0 mg",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q39",
    "quantity": "Stock2: Na 2 WO 4 ·2H 2 O 8.0 mg",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate solution table: exact named row",
        "exact_source_quote": "Na 2 WO 4 ·2H 2 O 8.0 mg",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q40",
    "quantity": "Stock2: Distilled water 1.0 L",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[2].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm431",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431",
        "source_locator": "Selenite-tungstate solution table: exact named row",
        "exact_source_quote": "Distilled water 1.0 L",
        "snapshot_sha256": "cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50",
        "parsed_text_sha256": "79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e"
      }
    ],
    "source_stage_and_basis": "Source-only composition needed for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid inputs and hydrate forms; do not flatten or infer measured final volume."
  },
  {
    "quantity_id": "q41",
    "quantity": "Fe-stock HCl7.7 M",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock HCl row",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Explicit reagent strength 7.7 M, with 10 mL dose to the stock; not final-medium molarity. The parent nested reagent concentration 7.7 MOLAR has matching attached evidence; that evidence does not transfer automatically."
  },
  {
    "quantity_id": "q42",
    "quantity": "Fe-stock HCl25%",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "solutions[0].composition",
        "stored": []
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm187",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187",
        "source_locator": "FeCl2 stock HCl row",
        "exact_source_quote": "25% HCl (7.7 M) 10.0 ml",
        "snapshot_sha256": "e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804",
        "parsed_text_sha256": "eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8"
      }
    ],
    "source_stage_and_basis": "Preserve 25% as printed without inferring its mass/volume basis. The independently explicit 7.7 M is available; do not adopt provider 2.5 g/L as primary chemistry."
  },
  {
    "quantity_id": "q43",
    "quantity": "Default autoclave temperature",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Page default sterilization sentence; applies unless otherwise stated",
        "exact_source_quote": "121°C",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Default main-medium sterilization only; post-cooling stocks are explicitly filter-sterilized and the final sulfide stock is anaerobic. Preserve those exceptions."
  },
  {
    "quantity_id": "q44",
    "quantity": "Default autoclave duration",
    "decision": "add",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "jcm940",
        "source_url": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940",
        "source_locator": "Page default sterilization sentence; applies unless otherwise stated",
        "exact_source_quote": "15 min",
        "snapshot_sha256": "eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9",
        "parsed_text_sha256": "3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c"
      }
    ],
    "source_stage_and_basis": "Default main-medium sterilization only; post-cooling stocks are explicitly filter-sterilized and the final sulfide stock is anaerobic. Preserve those exceptions."
  },
  {
    "quantity_id": "q45",
    "quantity": "Provider-declared main volume1041 mL",
    "decision": "not_quantified",
    "local_fields": [
      {
        "input": "data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml",
        "field_path": "preparation_steps",
        "stored": null
      },
      {
        "input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
        "field_path": "preparation_steps",
        "stored": null
      }
    ],
    "source_snippets": [
      {
        "source_key": "mediadiveJ940api",
        "source_url": "https://mediadive.dsmz.de/rest/medium/J940",
        "source_locator": "$.data.solutions[0].volume",
        "exact_source_quote": "\"volume\": 1041",
        "snapshot_sha256": "e5c9122a189ef1c33688437d0e08caec417eb9faccad29e48eba7ddc794e9cc2"
      }
    ],
    "source_stage_and_basis": "Provider bookkeeping sums the listed liquids; the primary neither reports measured final volume nor cancels the explicit per-liter final sulfide instruction. Do not substitute 1041 mL as a measured denominator."
  }
]

### Asserted ontology and current CHEBI-based secondary metadata

grounding: supported. Targets: CultureMech:010414.

15 distinct asserted primary and current CHEBI-based secondary IDs resolve to matching nonobsolete labels in all inspected layers. Target linkage: 15/16 primary and 10/16 secondary instances; all asserted current mediaingredientmech_chebi_term keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are outside this helper lookup and require a separate historical-correspondence assessment. Source forms are assessed separately.

Instance coverage on a 0–100 percent scale, denominator 16: primary 93.75%; secondary 62.50%. These are linkage metrics, not correctness scores. Missing optional links do not establish wrong identity.

### Transferred stock chemical forms and current parent representations

grounding: concern. Targets: CultureMech:010414.

Target CaCl2 dihydrate, MgCl2 hexahydrate, thiamine hydrochloride, resazurin and named salts have compatible inspected forms; generic B12 is not narrowed. Parent trace CoCl2·6H2O and NiCl2·6H2O are linked to anhydrous 35696/34887, so do not copy those IDs into a proposed stock. Parent M431 flattened selenite values likewise cannot establish final-medium amounts.

### Append-only history and timestamp shape

provenance: supported. Targets: CultureMech:010414.

26 timestamp instances inspected; 0 malformed or timezone-naive instances. Historical import, repair and enrichment statements are provenance, not source confirmation. Preserve old events; append any later authorized clarification rather than silently rewriting historical records.

### Exact source and maintained owner

identity: supported. Targets: CultureMech:010414.

TOGO M987 names JCM_M940; original source title and current provider J940 agree. The generated single-contributor identity resolves to the named normalized owner. M180/JCM187 and M431/JCM431 resolve only as specified stock contexts, not alternative formulations.

### Medium class, growth claims and default gas roles

scope: supported. Targets: CultureMech:010414.

Bacterial, liquid, complex and undefined labels are consistent with the source medium and yeast extract. Microbial cultivation is an application label, not an evidence-backed strain-growth assertion. No target-organism, DOI, PMID or KG crosslink is asserted. Source gas-mixture conditions are assessed explicitly; no parent-medium pH or temperature is transferred.

### Preparation and evidence placement

completeness: concern. Targets: CultureMech:010414.

Both layers lack preparation steps and narrow claim-level source evidence despite available ordered instructions. The exact source has main autoclaving under 80:20 v/v gas, distinct post-cooling filter-sterilized additions, distribution and a final per-liter sulfide step. Source percentages retain unspecified basis; no pH or absolute gas amount is invented.

## Findings

### f1: Stock and receiving-medium quantities are conflated

blocker / open / confirmed; issue key: cm010414-flat-stocks-and-units.

Both layers store vitamin-stock 20/80/200/50 mg as 20/80/200/50 G_PER_L final ingredients, resazurin 0.4 mg as 0.4 G_PER_L, liquid stock doses as G_PER_L and water as mass. Main gram inputs also lack a justified final-volume basis. This materially changes the formulation despite passing schema checks.

### f2: Source preparation and inspectable stock definitions are absent

major / open / confirmed; issue key: cm010414-preparation-stock-evidence.

All six receiving solutions have empty composition and Unknown solution names. The preserved cross-references are identifiable, but the target/owner do not encode the source preparation sequence or attach narrow evidence. Parent stock evidence cannot substitute for target claims, and parent anhydrous cobalt/nickel IDs must not be copied as the source hexahydrates.

### f3: Generated water value predates the maintained duplicate repair

minor / open / confirmed; issue key: cm010414-stale-water-repair.

The target records 2.0 G_PER_L and a summed-duplicate note; the later maintained owner records 1.0 G_PER_L and a collapsed-duplicate note. Neither value validates liquid water units, but regeneration provenance is stale and must be reconciled after scientific repair.

## Recommended Actions And Acceptance Checks

### a1

Reconstruct the maintained receiving recipe and its separate vitamin/Fe/trace/selenite stocks using the exact source amounts and units. Preserve undefined percentage bases and final-volume limits; then separately authorize merge regeneration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- All inventory stages and units reconcile to exact JCM940 and scoped dependency sources; no stock constituent is promoted without a supported dose/basis.

### a2

Represent exact stock definitions, meaningful names, preparation and claim-level supporting snippets in the maintained owner, retaining source-specific chemical forms and parent-scope exclusions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.
- Fe/trace/selenite dependencies resolve with correct supplied forms; original access timestamps and source hashes retained.

### a3

Preserve both historical events and regenerate only after the owner has a source-supported water/stock representation; do not rewrite old history or reproduce the old sum.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch025/248/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch025/248/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml:1:id: CultureMech:010414<br>./data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml:1:id: CultureMech:010414<br> |
| bound-source-integrity | /private/tmp/culturemech-review-work-batch025/source-preflight-bound/248/source-catalog.json; Full per-record bound catalog; raw/text/metadata hashes independently rechecked | supports | 48 exact bound source captures checked. Captured timestamps remain actual original access times; no new retrieval or cross-record substitution. |
| j940 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940; Complete numbered medium940 table, ordered preparation and its own vitamin table | supports | Exact primary identifies this medium and all transferred source stages. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987; $.meta; all four components and both comments | supports | M987 explicitly identifies JCM_M940. Component sections distinguish receiving additions from the vitamin-stock recipe. |
| api | https://mediadive.dsmz.de/rest/medium/J940; $.data.medium and all five solution recipe/step objects | supports | J940 main solution4952 declares 1041 mL; original batch inputs and the final per-liter sulfide instruction remain distinct. This is provider volume bookkeeping, not a measured final volume. |
| j187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; Only FeCl2 solution and Trace element solution tables | supports | Only these two stocks transfer to J940; the parent medium and its vitamin/sulfur content do not. |
| j431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; Only Selenite-tungstate solution table | supports | Exact JCM431 stock differs from similarly named DSMZ formulations. |
| solution3846 | https://mediadive.dsmz.de/rest/solution/3846; $.data; complete exact stock endpoint | supports | Endpoint identity and recipe checked against J940 linkage and the corresponding primary subsection; stock identity is not inferred from a similar name. |
| solution3847 | https://mediadive.dsmz.de/rest/solution/3847; $.data; complete exact stock endpoint | supports | Endpoint identity and recipe checked against J940 linkage and the corresponding primary subsection; stock identity is not inferred from a similar name. |
| solution4172 | https://mediadive.dsmz.de/rest/solution/4172; $.data; complete exact stock endpoint | supports | Endpoint identity and recipe checked against J940 linkage and the corresponding primary subsection; stock identity is not inferred from a similar name. |
| solution4953 | https://mediadive.dsmz.de/rest/solution/4953; $.data; complete exact stock endpoint | supports | Endpoint identity and recipe checked against J940 linkage and the corresponding primary subsection; stock identity is not inferred from a similar name. |
| dependency-claims | /private/tmp/culturemech-review-work-batch025/248/dependency-evidence-audit.json; Twelve exact attached evidence objects in parent M180 Fe/trace stock subtrees | supports | Each literal snippet and historical source hash matched its exact bound capture, with original access dates retained. Correct attached parent water/reagent strengths remain verified only there; absent numerical concentration slots retain source-supported batch amounts in notes. No parent evidence is inherited as target evidence. |
| togoM180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; Exact parent metadata and explicitly transferred stock components | supports | Parent accession resolves; only the named Fe/trace/selenite stock subsection informs this target. |
| togoM431 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; Exact parent metadata and explicitly transferred stock components | supports | Parent accession resolves; only the named Fe/trace/selenite stock subsection informs this target. |
| quantity-inventory | /private/tmp/culturemech-review-work-batch025/248/quantity-inventory.json; Every listed ingredient/stock-addition concentration and explicitly scoped source-only additions | context_only | Native decisions retain literal quotes, stable URLs, exact locators, original units/stages and limitations. Arithmetic is outside quotes. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15377 resolves to water. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:15956 resolves to biotin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:16526 resolves to carbon dioxide. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:17997 resolves to dinitrogen. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:26710 resolves to sodium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:31206 resolves to ammonium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:32588 resolves to potassium chloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86158 resolves to calcium chloride dihydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS obo_id, canonical label, obsolete flag; source forms assessed separately | supports | CHEBI:8806 resolves to Resazurin. Identifier existence and label metadata do not establish source-specific hydrate, stereochemistry or product identity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned exact-key preferred-term rows; adjacent metadata source_commit/hash | supports | {"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256": "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type": "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate", "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type": "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id": "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}} |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; Exact OLS formula/structure versus JCM187 source hexahydrate | supports | These parent-stock IDs denote anhydrous salts, whereas the transferred primary recipe specifies hexahydrates. Amount evidence alone does not certify parent grounding. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS formula/structure versus JCM187 source hexahydrate | supports | These parent-stock IDs denote anhydrous salts, whereas the transferred primary recipe specifies hexahydrates. Amount evidence alone does not certify parent grounding. |
| history-metadata | data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml; Complete curation_history arrays; timestamp shape and source/generated chronology | context_only | [{"input": "target", "events": 13, "timestamp_issues": []}, {"input": "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml", "events": 13, "timestamp_issues": []}] |
| writer-0 | src/culturemech/merge/formulation.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current inspected cleanup collapses identical values rather than summing; current TOGO importer separates primary sections from inline stock composition. These current functions are not proof of the exact historical writer that produced the stale flat record. |
| writer-1 | src/culturemech/import/mediadive_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current inspected cleanup collapses identical values rather than summing; current TOGO importer separates primary sections from inline stock composition. These current functions are not proof of the exact historical writer that produced the stale flat record. |
| writer-2 | scripts/cleanup_media_quality.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current inspected cleanup collapses identical values rather than summing; current TOGO importer separates primary sections from inline stock composition. These current functions are not proof of the exact historical writer that produced the stale flat record. |
| writer-3 | src/culturemech/import/togo_importer.py; Current relevant import/merge/repair functions read; hash pinned in inspection inputs | context_only | Current inspected cleanup collapses identical values rather than summing; current TOGO importer separates primary sections from inline stock composition. These current functions are not proof of the exact historical writer that produced the stale flat record. |

## Limits And Additional Notes

- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No amount or chemical identity from unrelated M180/M431 basal, sulfur or vitamin sections transfers. Parent-only legacy MediaIngredientMech:001072 is absent from the target and maintained owner and from these transferred stock components; current-index absence is not historical invalidity and is not a required target identity gap.
- Primary batch inputs and provider-declared volumes are retained separately. Bare 8%, 5% and 25% bases, absolute gas dose and measured final volume are not supplied; no guessed conversion is proposed.
- The reference validator reported Reference checks: 0; issues: 0. Its successful exit did not validate source support; exact bound collection/provider comparisons supply that assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T142653Z-culturemech-010414-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: aminivibrio_asinoensis_medium (CultureMech:010414)'
started_at: '2026-10-21T14:22:44Z'
finished_at: '2026-10-21T14:26:53Z'
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
summary: JCM940 identity resolves, but the generated record and its owner flatten
  vitamin-stock amounts, use mass units for water and liquid additions, omit preparation,
  and retain different duplicate-water histories. Required source sections are available;
  dependency evidence is restricted to the transferred Fe, trace and selenite stocks.
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
  - path: data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
    sha256: 85c4dbd097d725040de4c7527127b8771cdb0f6d4018bf25a5d54d096c289dbc
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
    sha256: 03de453b2e460645b2abab7b1a371ee3143c4138d9ce4ff69c58298051966782
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
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 248; batch 025 item 8 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding twenty-four task batches
    contain 240 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 033ef56966c19f8948d84a579b3f280e3e94e9e3
    contains 41 validated baseline bundles covering 3 current merged paths. Unioning
    all prior lists with this baseline covers 243 of 6320 current merged paths, including
    3 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010414
targets:
- target_id: CultureMech:010414
  path: data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  label: aminivibrio_asinoensis_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch025/248/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/248/strict.tsv"
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010414
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
  - CultureMech:010414
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:48.945469Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch025/248/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:50.725982Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-025/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch025/248/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:52.444719Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T14:23:53.885177Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T14:26:52Z'
  support: supports
  summary: './data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml:1:id: CultureMech:010414

    ./data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml:1:id:
    CultureMech:010414

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: bound-source-integrity
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/source-preflight-bound/248/source-catalog.json
  locator: Full per-record bound catalog; raw/text/metadata hashes independently rechecked
  accessed_at: '2026-10-21T14:26:52Z'
  support: supports
  summary: 48 exact bound source captures checked. Captured timestamps remain actual
    original access times; no new retrieval or cross-record substitution.
  snapshot_sha256: 5c4458ed3a3330d5dd54ae564f01a033b19592a6c68b143430200fc8977410a6
- evidence_id: j940
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940
  locator: Complete numbered medium940 table, ordered preparation and its own vitamin
    table
  accessed_at: '2026-10-21T14:01:46.745638Z'
  support: supports
  summary: Exact primary identifies this medium and all transferred source stages.
  quote: 940   AMINIVIBRIO ASINOENSIS MEDIUM
  snapshot_sha256: eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987
  locator: $.meta; all four components and both comments
  accessed_at: '2026-10-21T14:01:45.105815Z'
  support: supports
  summary: M987 explicitly identifies JCM_M940. Component sections distinguish receiving
    additions from the vitamin-stock recipe.
  snapshot_sha256: f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J940
  locator: $.data.medium and all five solution recipe/step objects
  accessed_at: '2026-10-21T14:01:43.983909Z'
  support: supports
  summary: J940 main solution4952 declares 1041 mL; original batch inputs and the
    final per-liter sulfide instruction remain distinct. This is provider volume bookkeeping,
    not a measured final volume.
  snapshot_sha256: e5c9122a189ef1c33688437d0e08caec417eb9faccad29e48eba7ddc794e9cc2
- evidence_id: j187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  locator: Only FeCl2 solution and Trace element solution tables
  accessed_at: '2026-10-21T10:35:30.362855Z'
  support: supports
  summary: Only these two stocks transfer to J940; the parent medium and its vitamin/sulfur
    content do not.
  quote: 25% HCl (7.7 M) 10.0 ml
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: j431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  locator: Only Selenite-tungstate solution table
  accessed_at: '2026-10-21T12:23:19.260180Z'
  support: supports
  summary: Exact JCM431 stock differs from similarly named DSMZ formulations.
  quote: NaOH 0.4 g Na 2 SeO 3 ·5H 2 O 6.0 mg Na 2 WO 4 ·2H 2 O 8.0 mg Distilled water
    1.0 L
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: solution3846
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3846
  locator: $.data; complete exact stock endpoint
  accessed_at: '2026-10-21T10:37:16.847261Z'
  support: supports
  summary: Endpoint identity and recipe checked against J940 linkage and the corresponding
    primary subsection; stock identity is not inferred from a similar name.
  snapshot_sha256: 3b17c2e79a0ef85051dc8c41ff95bb0361a83b12179a510184b61ef9edbb96f0
- evidence_id: solution3847
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3847
  locator: $.data; complete exact stock endpoint
  accessed_at: '2026-10-21T10:37:16.847414Z'
  support: supports
  summary: Endpoint identity and recipe checked against J940 linkage and the corresponding
    primary subsection; stock identity is not inferred from a similar name.
  snapshot_sha256: 12084302b4c979541441db0b0961a5744d937930e17ed9c7a326c75e2f787dd8
- evidence_id: solution4172
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4172
  locator: $.data; complete exact stock endpoint
  accessed_at: '2026-10-19T23:38:14.340715Z'
  support: supports
  summary: Endpoint identity and recipe checked against J940 linkage and the corresponding
    primary subsection; stock identity is not inferred from a similar name.
  snapshot_sha256: 9ba49b9796c62b038e0d78787e6c7a6583180e95773cd916b2edab760876e385
- evidence_id: solution4953
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4953
  locator: $.data; complete exact stock endpoint
  accessed_at: '2026-10-21T14:02:49.101031Z'
  support: supports
  summary: Endpoint identity and recipe checked against J940 linkage and the corresponding
    primary subsection; stock identity is not inferred from a similar name.
  snapshot_sha256: 6425bc3112801d36dbb28ac9f822c77c5417a1d2a73bc1cb26ba3095a45287a5
- evidence_id: dependency-claims
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/248/dependency-evidence-audit.json
  locator: Twelve exact attached evidence objects in parent M180 Fe/trace stock subtrees
  accessed_at: '2026-10-21T14:26:52Z'
  support: supports
  summary: Each literal snippet and historical source hash matched its exact bound
    capture, with original access dates retained. Correct attached parent water/reagent
    strengths remain verified only there; absent numerical concentration slots retain
    source-supported batch amounts in notes. No parent evidence is inherited as target
    evidence.
  snapshot_sha256: 84cfb5d14d4310b5b214244ebb650097ff3f8bfd57a9c17d79cb651407fa71c9
- evidence_id: togoM180
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  locator: Exact parent metadata and explicitly transferred stock components
  accessed_at: '2026-10-21T10:35:28.558157Z'
  support: supports
  summary: Parent accession resolves; only the named Fe/trace/selenite stock subsection
    informs this target.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: togoM431
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  locator: Exact parent metadata and explicitly transferred stock components
  accessed_at: '2026-10-21T12:23:17.822513Z'
  support: supports
  summary: Parent accession resolves; only the named Fe/trace/selenite stock subsection
    informs this target.
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: quantity-inventory
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch025/248/quantity-inventory.json
  locator: Every listed ingredient/stock-addition concentration and explicitly scoped
    source-only additions
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Native decisions retain literal quotes, stable URLs, exact locators, original
    units/stages and limitations. Arithmetic is outside quotes.
  snapshot_sha256: 22e8992fd429e7cd08c751a004cac890937b3a860f6c1ae6e6cfe6661dbc7c02
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
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: CHEBI:15956 resolves to biotin. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
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
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: CHEBI:176843 resolves to vitamin B12. Identifier existence and label metadata
    do not establish source-specific hydrate, stereochemistry or product identity.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
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
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: CHEBI:30753 resolves to 4-aminobenzoic acid. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
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
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: CHEBI:49105 resolves to thiamine hydrochloride. Identifier existence and
    label metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi50144
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  locator: Exact OLS obo_id, canonical label, obsolete flag; source forms assessed
    separately
  accessed_at: '2026-10-20T07:22:07.440767Z'
  support: supports
  summary: CHEBI:50144 resolves to sodium pyruvate. Identifier existence and label
    metadata do not establish source-specific hydrate, stereochemistry or product
    identity.
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
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
  accessed_at: '2026-10-21T14:26:52Z'
  support: supports
  summary: '{"source_commit": "6643131b0f12ab40b66f98135245fca04027e0e9", "snapshot_sha256":
    "4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5", "rows": {"CHEBI:15377":
    [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377",
    "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type":
    "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id":
    "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843":
    [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:26710": [{"label": "NaCl", "match_type":
    "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id":
    "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30753":
    [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label":
    "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term":
    "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:50144": [{"label": "Na-pyruvate", "match_type":
    "preferred_term", "identifier": "CHEBI:50144", "preferred_term": "Na-pyruvate",
    "ontology_id": "CHEBI:50144", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier":
    "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:8806": [{"label": "Resazurin", "match_type":
    "preferred_term", "identifier": "CHEBI:8806", "preferred_term": "Resazurin", "ontology_id":
    "CHEBI:8806", "mapping_status": "MAPPED", "ambiguity": "unique"}]}}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: chebi35696
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: Exact OLS formula/structure versus JCM187 source hexahydrate
  accessed_at: '2026-10-21T06:57:48.030715Z'
  support: supports
  summary: These parent-stock IDs denote anhydrous salts, whereas the transferred
    primary recipe specifies hexahydrates. Amount evidence alone does not certify
    parent grounding.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS formula/structure versus JCM187 source hexahydrate
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: These parent-stock IDs denote anhydrous salts, whereas the transferred
    primary recipe specifies hexahydrates. Amount evidence alone does not certify
    parent grounding.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: history-metadata
  kind: record_content
  reference: data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml; data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
  locator: Complete curation_history arrays; timestamp shape and source/generated
    chronology
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: '[{"input": "target", "events": 13, "timestamp_issues": []}, {"input":
    "data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml",
    "events": 13, "timestamp_issues": []}]'
- evidence_id: writer-0
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Current inspected cleanup collapses identical values rather than summing;
    current TOGO importer separates primary sections from inline stock composition.
    These current functions are not proof of the exact historical writer that produced
    the stale flat record.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Current inspected cleanup collapses identical values rather than summing;
    current TOGO importer separates primary sections from inline stock composition.
    These current functions are not proof of the exact historical writer that produced
    the stale flat record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-2
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Current inspected cleanup collapses identical values rather than summing;
    current TOGO importer separates primary sections from inline stock composition.
    These current functions are not proof of the exact historical writer that produced
    the stale flat record.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant import/merge/repair functions read; hash pinned in inspection
    inputs
  accessed_at: '2026-10-21T14:26:52Z'
  support: context_only
  summary: Current inspected cleanup collapses identical values rather than summing;
    current TOGO importer separates primary sections from inline stock composition.
    These current functions are not proof of the exact historical writer that produced
    the stale flat record.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: quantities
  area: quantity
  topic: Complete source-stage quantity decision inventory
  outcome: concern
  summary: 45 source-scoped decisions, including every local concentration and explicit
    source-only quantities. Verified applies only to the named local layer with attached
    matching evidence.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - record
  - quantity-inventory
  details: "[\n  {\n    \"quantity_id\": \"q1\",\n    \"quantity\": \"Distilled water\"\
    ,\n    \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"ingredients[0].concentration\",\n        \"stored\": {\n\
    \          \"value\": \"2.0\",\n          \"unit\": \"G_PER_L\"\n        }\n \
    \     },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.0\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[0]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Distilled water\\\",\\n          \\\"volume\\\"\
    : 1,\\n          \\\"unit\\\": \\\"L\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed. Generated 2.0\
    \ G_PER_L and owner 1.0 G_PER_L both misrepresent liquid water; the owner repair\
    \ does not recover separate main/vitamin water stages.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q2\",\n    \"quantity\": \"Yeast extract\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"Yeast extract 2.0 g\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[1]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Yeast extract\\\",\\n          \\\"volume\\\"\
    : 2,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q3\",\n    \"quantity\": \"NaCl\",\n    \"decision\":\
    \ \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"NaCl 1.0 g\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[2]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NaCl\\\",\\n          \\\"volume\\\": 1,\\n  \
    \        \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q4\",\n    \"quantity\": \"CaCl2・2H2O\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.15\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"CaCl 2 ·2H 2 O 0.15 g\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[3]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"CaCl2・2H2O\\\",\\n          \\\"volume\\\": 0.15,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q5\",\n    \"quantity\": \"KH2PO4\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.2\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"KH 2 PO 4 0.2 g\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[4]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KH2PO4\\\",\\n          \\\"volume\\\": 0.2,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q6\",\n    \"quantity\": \"NH4Cl\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.25\",\n          \"unit\": \"G_PER_L\"\n       \
    \ }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"NH 4 Cl 0.25 g\",\n        \"snapshot_sha256\":\
    \ \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[5]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"NH4Cl\\\",\\n          \\\"volume\\\": 0.25,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q7\",\n    \"quantity\": \"Resazurin\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[6].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"Resazurin 0.4 mg\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[6]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Resazurin\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"mg\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed. Source 0.4 mg\
    \ is not local 0.4 g/L.\"\n  },\n  {\n    \"quantity_id\": \"q8\",\n    \"quantity\"\
    : \"MgCl2・6H2O\",\n    \"decision\": \"correct\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[7].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.4\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"MgCl 2 ·6H 2 O 0.4 g\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[7]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"MgCl2・6H2O\\\",\\n          \\\"volume\\\": 0.4,\\\
    n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q9\",\n    \"quantity\": \"KCl\",\n    \"decision\": \"\
    correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[8].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"0.5\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"KCl 0.5 g\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[8]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"KCl\\\",\\n          \\\"volume\\\": 0.5,\\n \
    \         \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Original main-table batch\
    \ input, with 1 L water plus separate stock additions. Preserve the stated amount\
    \ and unit; neither this water amount nor provider 1041 mL independently establishes\
    \ final-medium volume. No concentration conversion is proposed.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q10\",\n    \"quantity\": \"Sodium pyruvate\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"ingredients[9].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1.1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n  \
    \      \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[9].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1.1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table: exact named ingredient\",\n     \
    \   \"exact_source_quote\": \"Sodium pyruvate 1.1 g\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      },\n      {\n        \"source_key\": \"togoM987\",\n        \"source_url\"\
    : \"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M987\",\n \
    \       \"source_locator\": \"$.components[0].items[9]\",\n        \"exact_source_quote\"\
    : \"\\\"component_name\\\": \\\"Sodium pyruvate\\\",\\n          \\\"volume\\\"\
    : 1.1,\\n          \\\"unit\\\": \\\"g\\\"\",\n        \"snapshot_sha256\": \"\
    f30182c57ea1c125fb5bbf3e4e44555df3a1cb39139634fb6f2bd5644df4ac70\"\n      }\n\
    \    ],\n    \"source_stage_and_basis\": \"Original main-table batch input, with\
    \ 1 L water plus separate stock additions. Preserve the stated amount and unit;\
    \ neither this water amount nor provider 1041 mL independently establishes final-medium\
    \ volume. No concentration conversion is proposed.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q11\",\n    \"quantity\": \"FeCl2 solution (see Medium [M180])\",\n    \"\
    decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions[0].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table / post-cooling additions / final per-liter\
    \ sulfide addition, as specified\",\n        \"exact_source_quote\": \"FeCl 2\
    \ solution (see Medium No. 187 ) 1.0 ml\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main-table receiving-batch\
    \ addition before autoclaving. Retain liquid dose and exact source reference;\
    \ current composition is empty.\"\n  },\n  {\n    \"quantity_id\": \"q12\",\n\
    \    \"quantity\": \"Trace element solution (see Medium [M180])\",\n    \"decision\"\
    : \"correct\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table / post-cooling additions / final per-liter\
    \ sulfide addition, as specified\",\n        \"exact_source_quote\": \"Trace element\
    \ solution (see Medium No. 187 ) 1.0 ml\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main-table receiving-batch\
    \ addition before autoclaving. Retain liquid dose and exact source reference;\
    \ current composition is empty.\"\n  },\n  {\n    \"quantity_id\": \"q13\",\n\
    \    \"quantity\": \"Selenite--tungstate solution (see Medium [M431])\",\n   \
    \ \"decision\": \"correct\",\n    \"local_fields\": [\n      {\n        \"input\"\
    : \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n        \"field_path\"\
    : \"solutions[2].concentration\",\n        \"stored\": {\n          \"value\"\
    : \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n      },\n      {\n    \
    \    \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table / post-cooling additions / final per-liter\
    \ sulfide addition, as specified\",\n        \"exact_source_quote\": \"Selenite\
    \ tungstate solution (see Medium No. 431 ) 1.0 ml\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Main-table receiving-batch\
    \ addition before autoclaving. Retain liquid dose and exact source reference;\
    \ current composition is empty.\"\n  },\n  {\n    \"quantity_id\": \"q14\",\n\
    \    \"quantity\": \"8% NaHCO3 solution\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"30\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table / post-cooling additions / final per-liter\
    \ sulfide addition, as specified\",\n        \"exact_source_quote\": \"8% NaHCO\
    \ 3 solution 30.0 ml\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"After cooling, from anaerobic\
    \ filter-sterilized stocks. Retain liquid dose and exact source reference; current\
    \ composition is empty.\"\n  },\n  {\n    \"quantity_id\": \"q15\",\n    \"quantity\"\
    : \"Vitamin solution (see below)\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"1\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table / post-cooling additions / final per-liter\
    \ sulfide addition, as specified\",\n        \"exact_source_quote\": \"Vitamin\
    \ solution (see below) 1.0 ml\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"After cooling, from anaerobic\
    \ filter-sterilized stocks. Retain liquid dose and exact source reference; current\
    \ composition is empty.\"\n  },\n  {\n    \"quantity_id\": \"q16\",\n    \"quantity\"\
    : \"5% Na2S・9H2O solution\",\n    \"decision\": \"correct\",\n    \"local_fields\"\
    : [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"7\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main table / post-cooling additions / final per-liter\
    \ sulfide addition, as specified\",\n        \"exact_source_quote\": \"5% Na 2\
    \ S·9H 2 O solution 7.0 ml\",\n        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"After distribution: explicitly\
    \ 7 mL per liter, from an anaerobic stock. Do not reinterpret as 7 g/L or assume\
    \ the initial batch final volume. Retain liquid dose and exact source reference;\
    \ current composition is empty.\"\n  },\n  {\n    \"quantity_id\": \"q17\",\n\
    \    \"quantity\": \"Carbon dioxide gas\",\n    \"decision\": \"correct\",\n \
    \   \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[10].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main preparation gas atmosphere\",\n        \"\
    exact_source_quote\": \"N 2 -CO 2 (80:20, v/v)\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Current VARIABLE does not\
    \ retain the specified 80:20 v/v N2:CO2 mixture. Record the mixture condition\
    \ without inventing an absolute gas dose.\"\n  },\n  {\n    \"quantity_id\": \"\
    q18\",\n    \"quantity\": \"Nitrogen gas\",\n    \"decision\": \"correct\",\n\
    \    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[11].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"variable\",\n          \"unit\": \"VARIABLE\"\n  \
    \      }\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Main preparation gas atmosphere\",\n        \"\
    exact_source_quote\": \"N 2 -CO 2 (80:20, v/v)\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Current VARIABLE does not\
    \ retain the specified 80:20 v/v N2:CO2 mixture. Record the mixture condition\
    \ without inventing an absolute gas dose.\"\n  },\n  {\n    \"quantity_id\": \"\
    q19\",\n    \"quantity\": \"Biotin\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[12].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"20\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Vitamin solution table: exact named ingredient\"\
    ,\n        \"exact_source_quote\": \"Biotin 20.0 mg\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"This is a milligram input\
    \ to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving\
    \ batch; it is not grams per liter of final medium. No assumed final stock volume\
    \ or vitamin B12 chemical subtype.\"\n  },\n  {\n    \"quantity_id\": \"q20\"\
    ,\n    \"quantity\": \"p--Aminobenzoic acid\",\n    \"decision\": \"correct\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"80\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[13].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"80\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Vitamin solution table: exact named ingredient\"\
    ,\n        \"exact_source_quote\": \"p -Aminobenzoic acid 80.0 mg\",\n       \
    \ \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"This is a milligram input\
    \ to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving\
    \ batch; it is not grams per liter of final medium. No assumed final stock volume\
    \ or vitamin B12 chemical subtype.\"\n  },\n  {\n    \"quantity_id\": \"q21\"\
    ,\n    \"quantity\": \"Thiamine・HCl\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[14].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"200\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Vitamin solution table: exact named ingredient\"\
    ,\n        \"exact_source_quote\": \"Thiamine·HCl 200.0 mg\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"This is a milligram input\
    \ to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving\
    \ batch; it is not grams per liter of final medium. No assumed final stock volume\
    \ or vitamin B12 chemical subtype.\"\n  },\n  {\n    \"quantity_id\": \"q22\"\
    ,\n    \"quantity\": \"Vitamin B12\",\n    \"decision\": \"correct\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"ingredients[15].concentration\",\n        \"stored\"\
    : {\n          \"value\": \"50\",\n          \"unit\": \"G_PER_L\"\n        }\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Vitamin solution table: exact named ingredient\"\
    ,\n        \"exact_source_quote\": \"Vitamin B 1 2 50.0 mg\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"This is a milligram input\
    \ to a separate vitamin stock containing 1 L water and dosed 1 mL into the receiving\
    \ batch; it is not grams per liter of final medium. No assumed final stock volume\
    \ or vitamin B12 chemical subtype.\"\n  },\n  {\n    \"quantity_id\": \"q23\"\
    ,\n    \"quantity\": \"Separate vitamin-stock water\",\n    \"decision\": \"add\"\
    ,\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[4].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Vitamin solution table: water row\",\n      \
    \  \"exact_source_quote\": \"Vitamin B 1 2 50.0 mg Distilled water 1.0 L\",\n\
    \        \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Retain the independent 1\
    \ L vitamin-stock water input; do not sum it with the main water.\"\n  },\n  {\n\
    \    \"quantity_id\": \"q24\",\n    \"quantity\": \"Stock percentage: 8% NaHCO\
    \ 3 solution\",\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preferred_term\",\n        \"stored\"\
    : \"8% NaHCO3 solution\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[3].preferred_term\",\n        \"stored\"\
    : \"8% NaHCO3 solution\"\n      }\n    ],\n    \"source_snippets\": [\n      {\n\
    \        \"source_key\": \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Named receiving-stock reagent\",\n        \"\
    exact_source_quote\": \"8% NaHCO 3 solution\",\n        \"snapshot_sha256\": \"\
    eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n        \"\
    parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The existing name preserves\
    \ the percentage numeral but lacks attached evidence. Percentage basis is unspecified;\
    \ no w/v, v/v, density or mass conversion is inferred.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q25\",\n    \"quantity\": \"Stock percentage: 5% Na 2 S·9H 2 O solution\"\
    ,\n    \"decision\": \"evidence_only\",\n    \"local_fields\": [\n      {\n  \
    \      \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[5].preferred_term\",\n        \"stored\"\
    : \"5% Na2S・9H2O solution\"\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[5].preferred_term\",\n        \"stored\"\
    : \"5% Na2S・9H2O solution\"\n      }\n    ],\n    \"source_snippets\": [\n   \
    \   {\n        \"source_key\": \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Named receiving-stock reagent\",\n        \"\
    exact_source_quote\": \"5% Na 2 S·9H 2 O solution\",\n        \"snapshot_sha256\"\
    : \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\",\n    \
    \    \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"The existing name preserves\
    \ the percentage numeral but lacks attached evidence. Percentage basis is unspecified;\
    \ no w/v, v/v, density or mass conversion is inferred.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q26\",\n    \"quantity\": \"Stock0: 25% HCl (7.7 M) 10.0 ml\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 solution table: exact named row\",\n  \
    \      \"exact_source_quote\": \"25% HCl (7.7 M) 10.0 ml\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q27\",\n    \"quantity\": \"Stock0: FeCl 2\
    \ ·4H 2 O 1.5 g\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n    \
    \  {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 solution table: exact named row\",\n  \
    \      \"exact_source_quote\": \"FeCl 2 ·4H 2 O 1.5 g\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q28\",\n    \"quantity\": \"Stock0: Distilled\
    \ water 990.0 ml\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 solution table: exact named row\",\n  \
    \      \"exact_source_quote\": \"Distilled water 990.0 ml\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q29\",\n    \"quantity\": \"Stock1: ZnCl 2\
    \ 70.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n \
    \       \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"ZnCl 2 70.0 mg\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q30\",\n    \"quantity\": \"Stock1: MnCl 2\
    \ ·4H 2 O 100.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"MnCl 2 ·4H 2 O 100.0 mg\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q31\",\n    \"quantity\": \"Stock1: H 3 BO\
    \ 3 6.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"H 3 BO 3 6.0 mg\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q32\",\n    \"quantity\": \"Stock1: CoCl 2\
    \ ·6H 2 O 190.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"CoCl 2 ·6H 2 O 190.0 mg\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q33\",\n    \"quantity\": \"Stock1: CuCl 2\
    \ ·2H 2 O 2.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n   \
    \   {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"CuCl 2 ·2H 2 O 2.0 mg\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q34\",\n    \"quantity\": \"Stock1: NiCl 2\
    \ ·6H 2 O 24.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n  \
    \    {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"NiCl 2 ·6H 2 O 24.0 mg\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q35\",\n    \"quantity\": \"Stock1: Na 2 MoO\
    \ 4 ·2H 2 O 36.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n\
    \      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"Na 2 MoO 4 ·2H 2 O 36.0 mg\",\n        \"\
    snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q36\",\n    \"quantity\": \"Stock1: Distilled\
    \ water 1.0 L\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[1].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"Trace element solution table: exact named row\"\
    ,\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n        \"snapshot_sha256\"\
    : \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\",\n    \
    \    \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q37\",\n    \"quantity\": \"Stock2: NaOH 0.4\
    \ g\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions[2].composition\",\n        \"stored\": []\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate solution table: exact named\
    \ row\",\n        \"exact_source_quote\": \"NaOH 0.4 g\",\n        \"snapshot_sha256\"\
    : \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\",\n    \
    \    \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q38\",\n    \"quantity\": \"Stock2: Na 2 SeO\
    \ 3 ·5H 2 O 6.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate solution table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Na 2 SeO 3 ·5H 2 O 6.0 mg\",\n   \
    \     \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q39\",\n    \"quantity\": \"Stock2: Na 2 WO\
    \ 4 ·2H 2 O 8.0 mg\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n \
    \     {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate solution table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Na 2 WO 4 ·2H 2 O 8.0 mg\",\n    \
    \    \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q40\",\n    \"quantity\": \"Stock2: Distilled\
    \ water 1.0 L\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n\
    \        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[2].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm431\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431\"\
    ,\n        \"source_locator\": \"Selenite-tungstate solution table: exact named\
    \ row\",\n        \"exact_source_quote\": \"Distilled water 1.0 L\",\n       \
    \ \"snapshot_sha256\": \"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50\"\
    ,\n        \"parsed_text_sha256\": \"79f8dfb9c70f7429e248406f2fab908fb32bebedba426eb0306e12577bc44a7e\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Source-only composition needed\
    \ for the receiving stock, separate from its 1 mL dose. Retain original g/mg/liquid\
    \ inputs and hydrate forms; do not flatten or infer measured final volume.\"\n\
    \  },\n  {\n    \"quantity_id\": \"q41\",\n    \"quantity\": \"Fe-stock HCl7.7\
    \ M\",\n    \"decision\": \"add\",\n    \"local_fields\": [\n      {\n       \
    \ \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n\
    \        \"field_path\": \"solutions[0].composition\",\n        \"stored\": []\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock HCl row\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M) 10.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Explicit reagent strength\
    \ 7.7 M, with 10 mL dose to the stock; not final-medium molarity. The parent nested\
    \ reagent concentration 7.7 MOLAR has matching attached evidence; that evidence\
    \ does not transfer automatically.\"\n  },\n  {\n    \"quantity_id\": \"q42\"\
    ,\n    \"quantity\": \"Fe-stock HCl25%\",\n    \"decision\": \"add\",\n    \"\
    local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"solutions[0].composition\",\n        \"stored\":\
    \ []\n      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm187\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187\"\
    ,\n        \"source_locator\": \"FeCl2 stock HCl row\",\n        \"exact_source_quote\"\
    : \"25% HCl (7.7 M) 10.0 ml\",\n        \"snapshot_sha256\": \"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804\"\
    ,\n        \"parsed_text_sha256\": \"eb0d86774cb576541037e56d6a13ceb905fccd2ae1523b6e7eee4c83835825f8\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Preserve 25% as printed without\
    \ inferring its mass/volume basis. The independently explicit 7.7 M is available;\
    \ do not adopt provider 2.5 g/L as primary chemistry.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q43\",\n    \"quantity\": \"Default autoclave temperature\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Page default sterilization sentence; applies\
    \ unless otherwise stated\",\n        \"exact_source_quote\": \"121°C\",\n   \
    \     \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Default main-medium sterilization\
    \ only; post-cooling stocks are explicitly filter-sterilized and the final sulfide\
    \ stock is anaerobic. Preserve those exceptions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q44\",\n    \"quantity\": \"Default autoclave duration\",\n    \"decision\"\
    : \"add\",\n    \"local_fields\": [\n      {\n        \"input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      },\n      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"jcm940\",\n        \"source_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=940\"\
    ,\n        \"source_locator\": \"Page default sterilization sentence; applies\
    \ unless otherwise stated\",\n        \"exact_source_quote\": \"15 min\",\n  \
    \      \"snapshot_sha256\": \"eb173679aadf5fd3cc8a4f327ab3fdfbd31c14747acba509220edf91045237e9\"\
    ,\n        \"parsed_text_sha256\": \"3bafdda0e74d127832479b929155bb51a2d842a853d661d64fd384b29ef75f0c\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Default main-medium sterilization\
    \ only; post-cooling stocks are explicitly filter-sterilized and the final sulfide\
    \ stock is anaerobic. Preserve those exceptions.\"\n  },\n  {\n    \"quantity_id\"\
    : \"q45\",\n    \"quantity\": \"Provider-declared main volume1041 mL\",\n    \"\
    decision\": \"not_quantified\",\n    \"local_fields\": [\n      {\n        \"\
    input\": \"data/merge_yaml/merged/AMINIVIBRIO_ASINOENSIS_MEDIUM.yaml\",\n    \
    \    \"field_path\": \"preparation_steps\",\n        \"stored\": null\n      },\n\
    \      {\n        \"input\": \"data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml\"\
    ,\n        \"field_path\": \"preparation_steps\",\n        \"stored\": null\n\
    \      }\n    ],\n    \"source_snippets\": [\n      {\n        \"source_key\"\
    : \"mediadiveJ940api\",\n        \"source_url\": \"https://mediadive.dsmz.de/rest/medium/J940\"\
    ,\n        \"source_locator\": \"$.data.solutions[0].volume\",\n        \"exact_source_quote\"\
    : \"\\\"volume\\\": 1041\",\n        \"snapshot_sha256\": \"e5c9122a189ef1c33688437d0e08caec417eb9faccad29e48eba7ddc794e9cc2\"\
    \n      }\n    ],\n    \"source_stage_and_basis\": \"Provider bookkeeping sums\
    \ the listed liquids; the primary neither reports measured final volume nor cancels\
    \ the explicit per-liter final sulfide instruction. Do not substitute 1041 mL\
    \ as a measured denominator.\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Asserted ontology and current CHEBI-based secondary metadata
  outcome: supported
  summary: '15 distinct asserted primary and current CHEBI-based secondary IDs resolve
    to matching nonobsolete labels in all inspected layers. Target linkage: 15/16
    primary and 10/16 secondary instances; all asserted current mediaingredientmech_chebi_term
    keys have exact pinned MIM rows. Legacy mediaingredientmech_term assertions are
    outside this helper lookup and require a separate historical-correspondence assessment.
    Source forms are assessed separately.'
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - record
  - mim
  - owner-0
  - chebi15377
  - chebi15956
  - chebi16526
  - chebi176843
  - chebi17997
  - chebi26710
  - chebi30753
  - chebi31206
  - chebi32588
  - chebi49105
  - chebi50144
  - chebi63036
  - chebi86158
  - chebi86345
  - chebi8806
  details: 'Instance coverage on a 0–100 percent scale, denominator 16: primary 93.75%;
    secondary 62.50%. These are linkage metrics, not correctness scores. Missing optional
    links do not establish wrong identity.'
- assessment_id: dependency-grounding
  area: grounding
  topic: Transferred stock chemical forms and current parent representations
  outcome: concern
  summary: Target CaCl2 dihydrate, MgCl2 hexahydrate, thiamine hydrochloride, resazurin
    and named salts have compatible inspected forms; generic B12 is not narrowed.
    Parent trace CoCl2·6H2O and NiCl2·6H2O are linked to anhydrous 35696/34887, so
    do not copy those IDs into a proposed stock. Parent M431 flattened selenite values
    likewise cannot establish final-medium amounts.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - j187
  - j431
  - dependency-claims
  - chebi35696
  - chebi34887
- assessment_id: history
  area: provenance
  topic: Append-only history and timestamp shape
  outcome: supported
  summary: 26 timestamp instances inspected; 0 malformed or timezone-naive instances.
    Historical import, repair and enrichment statements are provenance, not source
    confirmation. Preserve old events; append any later authorized clarification rather
    than silently rewriting historical records.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - record
  - history-metadata
  - owner-0
- assessment_id: identity
  area: identity
  topic: Exact source and maintained owner
  outcome: supported
  summary: TOGO M987 names JCM_M940; original source title and current provider J940
    agree. The generated single-contributor identity resolves to the named normalized
    owner. M180/JCM187 and M431/JCM431 resolve only as specified stock contexts, not
    alternative formulations.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - record
  - owner-0
  - togo
  - j940
  - api
  - togoM180
  - togoM431
- assessment_id: classification
  area: scope
  topic: Medium class, growth claims and default gas roles
  outcome: supported
  summary: Bacterial, liquid, complex and undefined labels are consistent with the
    source medium and yeast extract. Microbial cultivation is an application label,
    not an evidence-backed strain-growth assertion. No target-organism, DOI, PMID
    or KG crosslink is asserted. Source gas-mixture conditions are assessed explicitly;
    no parent-medium pH or temperature is transferred.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - record
  - owner-0
  - j940
- assessment_id: preparation
  area: completeness
  topic: Preparation and evidence placement
  outcome: concern
  summary: Both layers lack preparation steps and narrow claim-level source evidence
    despite available ordered instructions. The exact source has main autoclaving
    under 80:20 v/v gas, distinct post-cooling filter-sterilized additions, distribution
    and a final per-liter sulfide step. Source percentages retain unspecified basis;
    no pH or absolute gas amount is invented.
  target_ids:
  - CultureMech:010414
  evidence_ids:
  - record
  - owner-0
  - j940
  - quantity-inventory
findings:
- finding_id: f1
  issue_key: cm010414-flat-stocks-and-units
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock and receiving-medium quantities are conflated
  description: Both layers store vitamin-stock 20/80/200/50 mg as 20/80/200/50 G_PER_L
    final ingredients, resazurin 0.4 mg as 0.4 G_PER_L, liquid stock doses as G_PER_L
    and water as mass. Main gram inputs also lack a justified final-volume basis.
    This materially changes the formulation despite passing schema checks.
  target_ids:
  - CultureMech:010414
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - record
  - quantity-inventory
  - j940
  - togo
  - api
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
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
  issue_key: cm010414-preparation-stock-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and inspectable stock definitions are absent
  description: All six receiving solutions have empty composition and Unknown solution
    names. The preserved cross-references are identifiable, but the target/owner do
    not encode the source preparation sequence or attach narrow evidence. Parent stock
    evidence cannot substitute for target claims, and parent anhydrous cobalt/nickel
    IDs must not be copied as the source hexahydrates.
  target_ids:
  - CultureMech:010414
  field_paths:
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - j940
  - j187
  - j431
  - dependency-claims
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
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
  issue_key: cm010414-stale-water-repair
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated water value predates the maintained duplicate repair
  description: The target records 2.0 G_PER_L and a summed-duplicate note; the later
    maintained owner records 1.0 G_PER_L and a collapsed-duplicate note. Neither value
    validates liquid water units, but regeneration provenance is stale and must be
    reconciled after scientific repair.
  target_ids:
  - CultureMech:010414
  field_paths:
  - ingredients[0]
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - history-metadata
  - quantity-inventory
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
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
  description: Reconstruct the maintained receiving recipe and its separate vitamin/Fe/trace/selenite
    stocks using the exact source amounts and units. Preserve undefined percentage
    bases and final-volume limits; then separately authorize merge regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010414
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
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
  - All inventory stages and units reconcile to exact JCM940 and scoped dependency
    sources; no stock constituent is promoted without a supported dose/basis.
- action_id: a2
  description: Represent exact stock definitions, meaningful names, preparation and
    claim-level supporting snippets in the maintained owner, retaining source-specific
    chemical forms and parent-scope exclusions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010414
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
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
  - Fe/trace/selenite dependencies resolve with correct supplied forms; original access
    timestamps and source hashes retained.
- action_id: a3
  description: Preserve both historical events and regenerate only after the owner
    has a source-supported water/stock representation; do not rewrite old history
    or reproduce the old sum.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010414
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M987_Aminivibrio_Asinoensis_Medium.yaml
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
- No amount or chemical identity from unrelated M180/M431 basal, sulfur or vitamin
  sections transfers. Parent-only legacy MediaIngredientMech:001072 is absent from
  the target and maintained owner and from these transferred stock components; current-index
  absence is not historical invalidity and is not a required target identity gap.
- Primary batch inputs and provider-declared volumes are retained separately. Bare
  8%, 5% and 25% bases, absolute gas dose and measured final volume are not supplied;
  no guessed conversion is proposed.
- 'The reference validator reported Reference checks: 0; issues: 0. Its successful
  exit did not validate source support; exact bound collection/provider comparisons
  supply that assessment.'
tags:
- unreviewed-records
- batch-025
- generated-medium
```
